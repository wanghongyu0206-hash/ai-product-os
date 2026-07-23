# Database Design Skill

## Goal

Design efficient, scalable, and maintainable database schemas that support application requirements while ensuring data integrity and optimal query performance.

## When To Use

- Designing new database schemas from scratch
- Redesigning existing schemas for better performance
- Choosing between SQL and NoSQL databases
- Optimizing slow queries
- Planning database migrations
- Designing for high-traffic applications
- Implementing data partitioning strategies

## Workflow

### Step 1

Analyze data requirements.

Identify:
- Entities and their attributes
- Relationships between entities
- Data volume and growth rate
- Read/write patterns
- Consistency requirements (strong vs eventual)
- Query patterns and access frequency

### Step 2

Choose database type.

Evaluate options:
- **Relational (PostgreSQL, MySQL)**: ACID transactions, complex queries, structured data
- **Document (MongoDB)**: Flexible schema, nested data, rapid iteration
- **Key-Value (Redis)**: High performance, simple lookups, caching
- **Column-family (Cassandra)**: High write throughput, time-series data
- **Graph (Neo4j)**: Complex relationships, social networks
- **Vector (Pinecone)**: Semantic search, AI embeddings

### Step 3

Design schema structure.

For SQL databases:
- Normalize to 3NF (reduce redundancy)
- Denormalize for read-heavy workloads
- Define primary keys, foreign keys, indexes
- Choose appropriate data types
- Design for partitioning if needed

For NoSQL databases:
- Design based on access patterns
- Embed related data when appropriate
- Plan for eventual consistency
- Design document/collection structure

### Step 4

Design indexes and query optimization.

Implement:
- Primary key indexes
- Foreign key indexes
- Composite indexes for common queries
- Partial indexes for filtered queries
- Covering indexes for frequently accessed columns
- Analyze query execution plans

### Step 5

Design for scalability.

Plan:
- Horizontal partitioning (sharding) strategy
- Read replicas for read-heavy workloads
- Connection pooling configuration
- Query caching strategy
- Database connection limits

### Step 6

Design data migration strategy.

Include:
- Schema versioning
- Backward compatibility
- Zero-downtime migrations
- Rollback procedures
- Data validation steps

### Step 7

Document database design.

Create:
- Entity-relationship diagrams (ERD)
- Schema documentation
- Index strategy documentation
- Query optimization notes
- Migration procedures

## Rules

1. Start with normalized design, denormalize only when necessary.
2. Index based on query patterns, not assumptions.
3. Use appropriate data types (don't use VARCHAR for everything).
4. Design for the access pattern, not just storage.
5. Plan for data growth from day one.
6. Use transactions for data consistency.
7. Monitor query performance continuously.
8. Document schema decisions and trade-offs.

## Output

- Entity-relationship diagram (ERD)
- Complete schema definition (DDL)
- Index strategy
- Query optimization plan
- Migration strategy
- Performance benchmarks
- Schema documentation

## Quality Criteria

- Schema meets all functional requirements
- Queries execute within performance targets
- Indexes optimize common query patterns
- Schema is normalized appropriately
- Migration strategy is safe and reversible
- Documentation is comprehensive
- Design supports future growth
