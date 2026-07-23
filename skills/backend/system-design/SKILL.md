# System Design Skill

## Goal

Design scalable, reliable, and maintainable backend system architectures that meet functional and non-functional requirements.

## When To Use

- Designing new backend systems from scratch
- Redesigning existing systems for scalability
- Choosing architectural patterns (monolith, microservices, serverless)
- Planning system integration points
- Designing for high availability and fault tolerance

## Workflow

### Step 1

Gather and analyze requirements.

Identify:
- Functional requirements (features, user flows)
- Non-functional requirements (performance, scalability, availability)
- Constraints (budget, timeline, team skills)
- Integration points (third-party services, legacy systems)

### Step 2

Choose architectural pattern.

Evaluate:
- **Monolith**: Simple, fast development, good for small teams
- **Microservices**: Scalable, independent deployment, complex
- **Serverless**: Pay-per-use, auto-scaling, vendor lock-in
- **Event-driven**: Asynchronous, loosely coupled, complex debugging
- **Hybrid**: Combine patterns based on needs

### Step 3

Design system components.

Define:
- Application layer (API servers, workers)
- Data layer (databases, caches, message queues)
- Integration layer (APIs, webhooks, event buses)
- Infrastructure layer (load balancers, CDN, monitoring)

### Step 4

Design data flow and communication.

Plan:
- Synchronous communication (REST, GraphQL, gRPC)
- Asynchronous communication (message queues, event buses)
- Data consistency patterns (eventual consistency, saga pattern)
- Caching strategies (read-through, write-through, cache-aside)

### Step 5

Design for scalability and reliability.

Implement:
- Horizontal scaling (load balancers, auto-scaling)
- Database scaling (sharding, replication, read replicas)
- Fault tolerance (circuit breakers, retries, fallbacks)
- High availability (multi-region, disaster recovery)

### Step 6

Design security architecture.

Include:
- Authentication and authorization
- Data encryption (at rest, in transit)
- API security (rate limiting, input validation)
- Compliance requirements (GDPR, HIPAA, PCI-DSS)

### Step 7

Document system design.

Create:
- Architecture diagrams (C4 model)
- Component descriptions
- Data flow diagrams
- API specifications
- Deployment architecture
- Disaster recovery plan

## Rules

1. Start simple—avoid over-engineering.
2. Design for the current scale, but plan for growth.
3. Prefer proven patterns over novel solutions.
4. Document trade-offs and decisions.
5. Design for failure—assume components will fail.
6. Separate concerns—each component has one responsibility.
7. Use async communication for decoupling.
8. Monitor everything—observability is critical.

## Output

- System architecture diagram
- Component specifications
- Data flow diagrams
- API specifications
- Deployment architecture
- Disaster recovery plan
- Architecture decision records (ADRs)

## Quality Criteria

- Architecture meets functional requirements
- Non-functional requirements addressed (scalability, availability, performance)
- Clear component boundaries
- Well-defined communication patterns
- Security considerations included
- Comprehensive documentation
- Trade-offs documented and justified
