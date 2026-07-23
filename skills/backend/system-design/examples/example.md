# System Design Example

## Scenario

Design a backend system for an AI Customer Service SaaS platform handling 10,000 concurrent conversations with real-time AI responses.

## Input

**Functional Requirements**:
- Real-time chat between customers and AI agents
- Knowledge base management (upload, search, retrieval)
- Conversation history and analytics
- Multi-tenant support (1000+ organizations)
- Integration with external LLM providers (OpenAI, Anthropic)

**Non-Functional Requirements**:
- Latency: < 500ms for chat responses
- Availability: 99.9% uptime
- Scalability: Handle 10,000 concurrent conversations
- Security: End-to-end encryption, GDPR compliance
- Cost: <$50K/month infrastructure

## Process

### Step 1: Choose Architectural Pattern

**Decision**: Hybrid architecture combining microservices and event-driven patterns

**Rationale**:
- Microservices: Independent scaling of chat, knowledge base, analytics
- Event-driven: Real-time updates, decoupled components
- Serverless: LLM integration for cost efficiency

### Step 2: Design System Components

```
┌─────────────────────────────────────────────────────────┐
│                    Load Balancer                         │
└─────────────────────────────────────────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Chat API    │  │  KB API      │  │ Analytics    │
│  Service     │  │  Service     │  │ Service      │
└──────────────┘  └──────────────┘  └──────────────┘
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │   Message Queue      │
              │   (Kafka/RabbitMQ)   │
              └──────────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
        ▼                 ▼                 ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│  Chat        │  │  Knowledge   │  │  Analytics   │
│  Database    │  │  Base DB     │  │  Database    │
│  (Redis)     │  │  (PostgreSQL)│  │  (ClickHouse)│
└──────────────┘  └──────────────┘  └──────────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │   Vector Database    │
              │   (Pinecone/Weaviate)│
              └──────────────────────┘
                          │
                          ▼
              ┌──────────────────────┐
              │   LLM Provider       │
              │   (OpenAI/Anthropic) │
              └──────────────────────┘
```

### Step 3: Design Data Flow

**Chat Message Flow**:
```
1. User sends message → Chat API Service
2. Chat API validates and stores in Redis
3. Chat API publishes "MessageReceived" event
4. AI Worker consumes event
5. AI Worker retrieves relevant knowledge (vector search)
6. AI Worker calls LLM provider
7. AI Worker publishes "AIResponse" event
8. Chat API receives event, streams response to user
9. Analytics Service consumes both events for tracking
```

**Knowledge Base Update Flow**:
```
1. Admin uploads document → KB API Service
2. KB API stores document in PostgreSQL
3. KB API publishes "DocumentUploaded" event
4. Embedding Worker consumes event
5. Embedding Worker generates embeddings via LLM
6. Embedding Worker stores in Vector Database
7. KB API publishes "DocumentReady" event
```

### Step 4: Design Scalability Strategy

**Horizontal Scaling**:
- Chat API: Auto-scale based on active connections (10-100 instances)
- KB API: Auto-scale based on CPU usage (2-10 instances)
- AI Workers: Auto-scale based on queue depth (5-50 instances)

**Database Scaling**:
- Redis: Cluster mode with 6 nodes (3 masters, 3 replicas)
- PostgreSQL: Read replicas (1 master, 3 replicas)
- ClickHouse: Distributed cluster (3 shards, 2 replicas)
- Vector DB: Managed service with auto-scaling

**Caching Strategy**:
- Redis: Session data, recent messages, rate limiting
- CDN: Static assets, knowledge base articles
- Application cache: Frequently accessed knowledge (LRU)

### Step 5: Design Reliability

**Fault Tolerance**:
- Circuit breakers for LLM provider calls
- Retry logic with exponential backoff
- Fallback responses when LLM unavailable
- Dead letter queues for failed messages

**High Availability**:
- Multi-region deployment (US-East, EU-West)
- Database replication across regions
- Global load balancer with health checks
- Disaster recovery: RPO < 1 hour, RTO < 4 hours

**Monitoring**:
- Metrics: Prometheus + Grafana
- Logs: ELK stack (Elasticsearch, Logstash, Kibana)
- Traces: Jaeger for distributed tracing
- Alerts: PagerDuty integration

### Step 6: Design Security

**Authentication & Authorization**:
- JWT tokens with refresh tokens
- OAuth 2.0 for third-party integrations
- Role-based access control (RBAC)
- API rate limiting (1000 req/min per tenant)

**Data Protection**:
- TLS 1.3 for all communications
- AES-256 encryption at rest
- PII data masking in logs
- GDPR compliance (data residency, right to deletion)

**API Security**:
- Input validation and sanitization
- SQL injection prevention (parameterized queries)
- XSS prevention (output encoding)
- CSRF protection (tokens)

## Output

### Architecture Diagram

Complete C4 model with:
- Context diagram (system boundaries)
- Container diagram (applications, databases)
- Component diagram (services, APIs)
- Code diagram (key classes/interfaces)

### Component Specifications

1. **Chat API Service**: Node.js + Express, WebSocket support
2. **KB API Service**: Python + FastAPI, document processing
3. **Analytics Service**: Go, high-throughput event processing
4. **AI Worker**: Python, LLM integration, embedding generation
5. **Message Queue**: Apache Kafka, 3 brokers, 3 partitions per topic

### Deployment Architecture

**Infrastructure**: AWS
- ECS Fargate for containerized services
- RDS for PostgreSQL
- ElastiCache for Redis
- MSK for Kafka
- S3 for document storage

**Cost Estimate**: $45K/month
- Compute: $20K
- Database: $12K
- Message Queue: $5K
- LLM API: $8K

### Key Decisions

1. **Why hybrid architecture?**: Balance between scalability and complexity
2. **Why Kafka?**: High throughput, durability, replay capability
3. **Why Redis for chat?**: Low latency, pub/sub support
4. **Why ClickHouse for analytics?**: Column-oriented, fast aggregations
5. **Why multi-region?**: GDPR compliance, disaster recovery

### Trade-offs

**Pros**:
- Highly scalable and available
- Real-time capabilities
- Cost-efficient LLM usage
- Clear service boundaries

**Cons**:
- Complex deployment and monitoring
- Eventual consistency challenges
- Higher operational overhead
- Requires specialized skills

### Next Steps

1. Create detailed API specifications (OpenAPI)
2. Design database schemas
3. Plan CI/CD pipeline
4. Set up monitoring infrastructure
5. Conduct security audit
6. Plan load testing strategy
