# Database Design Example

## Scenario

Design a PostgreSQL database schema for a multi-tenant AI Customer Service platform with conversation history, knowledge base, and analytics.

## Input

**Data Requirements**:
- 1000+ tenants (organizations)
- 50,000+ daily conversations
- 100,000+ knowledge base documents
- User management with role-based access
- Conversation analytics and reporting

**Query Patterns**:
- List conversations by tenant (paginated)
- Search knowledge base by semantic similarity
- Retrieve conversation history with messages
- Aggregate analytics (daily, weekly, monthly)
- Real-time active conversation count

**Performance Requirements**:
- Conversation list: < 100ms
- Knowledge search: < 200ms
- Analytics aggregation: < 500ms

## Process

### Step 1: Choose Database Type

**Decision**: PostgreSQL (relational) + Redis (caching) + Pinecone (vector search)

**Rationale**:
- PostgreSQL: ACID transactions, complex queries, mature ecosystem
- Redis: Session storage, real-time counts, caching
- Pinecone: Semantic search for knowledge base

### Step 2: Design Schema Structure

**Core Entities**:
```sql
-- Tenants (organizations)
CREATE TABLE tenants (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  name VARCHAR(255) NOT NULL,
  slug VARCHAR(100) UNIQUE NOT NULL,
  plan VARCHAR(50) NOT NULL DEFAULT 'free',
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Users
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  email VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  role VARCHAR(50) NOT NULL DEFAULT 'member',
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(tenant_id, email)
);

-- Conversations
CREATE TABLE conversations (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  customer_id UUID REFERENCES users(id) ON DELETE SET NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'active',
  priority VARCHAR(50) DEFAULT 'medium',
  assigned_to UUID REFERENCES users(id) ON DELETE SET NULL,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW(),
  closed_at TIMESTAMPTZ
);

-- Messages
CREATE TABLE messages (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  conversation_id UUID NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
  sender_type VARCHAR(50) NOT NULL, -- 'customer', 'agent', 'ai'
  sender_id UUID,
  content TEXT NOT NULL,
  metadata JSONB,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

-- Knowledge Base Documents
CREATE TABLE knowledge_documents (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  title VARCHAR(500) NOT NULL,
  content TEXT NOT NULL,
  category VARCHAR(100),
  tags TEXT[],
  embedding_vector VECTOR(1536), -- For semantic search
  created_at TIMESTAMPTZ DEFAULT NOW(),
  updated_at TIMESTAMPTZ DEFAULT NOW()
);

-- Conversation Analytics (aggregated daily)
CREATE TABLE conversation_analytics (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  tenant_id UUID NOT NULL REFERENCES tenants(id) ON DELETE CASCADE,
  date DATE NOT NULL,
  total_conversations INTEGER DEFAULT 0,
  resolved_conversations INTEGER DEFAULT 0,
  avg_response_time_seconds INTEGER,
  customer_satisfaction_score DECIMAL(3,2),
  created_at TIMESTAMPTZ DEFAULT NOW(),
  UNIQUE(tenant_id, date)
);
```

### Step 3: Design Indexes

**Based on Query Patterns**:
```sql
-- Conversation list by tenant (most frequent query)
CREATE INDEX idx_conversations_tenant_status 
  ON conversations(tenant_id, status, created_at DESC);

-- Message retrieval by conversation
CREATE INDEX idx_messages_conversation 
  ON messages(conversation_id, created_at);

-- Knowledge base search by tenant and category
CREATE INDEX idx_knowledge_tenant_category 
  ON knowledge_documents(tenant_id, category);

-- Analytics by tenant and date range
CREATE INDEX idx_analytics_tenant_date 
  ON conversation_analytics(tenant_id, date DESC);

-- User lookup by email (authentication)
CREATE INDEX idx_users_tenant_email 
  ON users(tenant_id, email);

-- Partial index for active conversations only
CREATE INDEX idx_conversations_active 
  ON conversations(tenant_id) 
  WHERE status = 'active';
```

### Step 4: Design for Scalability

**Partitioning Strategy** (for large tables):
```sql
-- Partition messages by month
CREATE TABLE messages (
  ...
) PARTITION BY RANGE (created_at);

-- Create monthly partitions
CREATE TABLE messages_2024_01 PARTITION OF messages
  FOR VALUES FROM ('2024-01-01') TO ('2024-02-01');

CREATE TABLE messages_2024_02 PARTITION OF messages
  FOR VALUES FROM ('2024-02-01') TO ('2024-03-01');
```

**Read Replicas**:
- 1 primary (read/write)
- 3 read replicas (analytics queries, reporting)

**Connection Pooling**:
```sql
-- PgBouncer configuration
[databases]
production = host=db-primary.example.com port=5432

[pgbouncer]
pool_mode = transaction
max_client_conn = 1000
default_pool_size = 20
reserve_pool_size = 5
```

### Step 5: Design Migration Strategy

**Using Alembic (Python) or Flyway (Java)**:

```python
# alembic/versions/001_initial_schema.py
def upgrade():
    op.create_table('tenants', ...)
    op.create_table('users', ...)
    op.create_table('conversations', ...)
    op.create_table('messages', ...)
    op.create_table('knowledge_documents', ...)

def downgrade():
    op.drop_table('knowledge_documents')
    op.drop_table('messages')
    op.drop_table('conversations')
    op.drop_table('users')
    op.drop_table('tenants')
```

**Zero-Downtime Migration**:
1. Add new columns (nullable)
2. Deploy application with dual-write logic
3. Backfill existing data
4. Deploy application using new columns
5. Remove old columns

### Step 6: Optimize Queries

**Example: Conversation List with Pagination**:
```sql
-- Optimized query using cursor-based pagination
SELECT c.id, c.status, c.created_at,
       COUNT(m.id) as message_count
FROM conversations c
LEFT JOIN messages m ON m.conversation_id = c.id
WHERE c.tenant_id = :tenant_id
  AND c.status = :status
  AND c.created_at < :cursor
GROUP BY c.id
ORDER BY c.created_at DESC
LIMIT :page_size;
```

**Query Execution Plan**:
```
Limit  (cost=0.56..12.34 rows=20)
  ->  GroupAggregate  (cost=0.56..12.34 rows=20)
        ->  Nested Loop Left Join  (cost=0.56..12.00)
              ->  Index Scan using idx_conversations_tenant_status
              ->  Index Only Scan using idx_messages_conversation
```

**Performance**: < 50ms (target: < 100ms) ✅

## Output

### Entity-Relationship Diagram

```
tenants (1) ──< (N) users
    │
    ├──< (N) conversations ──< (N) messages
    │
    ├──< (N) knowledge_documents
    │
    └──< (N) conversation_analytics
```

### Schema Documentation

**Total Tables**: 6
**Total Indexes**: 8
**Estimated Storage**: 500GB (1 year)

### Performance Benchmarks

| Query | Target | Actual | Status |
|-------|--------|--------|--------|
| Conversation list | < 100ms | 45ms | ✅ |
| Message retrieval | < 50ms | 23ms | ✅ |
| Knowledge search | < 200ms | 150ms | ✅ |
| Analytics aggregation | < 500ms | 320ms | ✅ |

### Key Decisions

1. **Why PostgreSQL?**: ACID compliance, mature ecosystem, excellent JSONB support
2. **Why partition messages?**: Table will grow to 100M+ rows, partitioning improves query performance
3. **Why cursor-based pagination?**: More efficient than OFFSET for large datasets
4. **Why read replicas?**: Separate analytics queries from transactional workload
5. **Why JSONB for metadata?**: Flexible schema for evolving message metadata

### Next Steps

1. Implement database connection pooling
2. Set up automated backups (daily full, hourly WAL)
3. Configure monitoring and alerts
4. Plan capacity planning for 12 months
5. Document query optimization guidelines
