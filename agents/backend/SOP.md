# Backend Agent SOP

## Prerequisites

- System Architecture Document from Architect Agent
- API Specification from Architect Agent
- Data Model Design from Architect Agent
- AI Architecture Design (when applicable)

## Procedure

### Step 1: Analyze Architecture

- Read system architecture document
- Identify service boundaries and module responsibilities
- Understand data flow between modules
- Review technical constraints and decisions

### Step 2: Design Service Modules

- Define service structure (controllers, services, repositories)
- Design module interfaces
- Plan dependency injection
- Define error handling strategy

### Step 3: Design Database

- Create database schema from data model
- Define table relationships and foreign keys
- Design index strategy for query performance
- Plan migration scripts

### Step 4: Implement APIs

- Design endpoint routes and methods
- Define request/response models with validation
- Implement business logic in service layer
- Add consistent error responses

### Step 5: Integrate Services

- Connect to database
- Integrate external APIs
- Configure LLM/RAG services when applicable
- Set up message queues or event buses if needed

### Step 6: Security Review

- Implement authentication (JWT, OAuth)
- Configure authorization (RBAC, ABAC)
- Add input validation and sanitization
- Set up CORS and rate limiting

### Step 7: Prepare Handoff

- Generate API documentation (OpenAPI/Swagger)
- Document database schema and migrations
- Write deployment configuration
- Package all artifacts for QA Agent

## Decision Tree

Simple application
↓
Single service architecture
↓
Monolithic structure with clear module boundaries

Enterprise system
↓
Modular services
↓
Service-oriented with shared libraries

AI product
↓
LLM + RAG backend architecture
↓
Vector database, embedding pipeline, streaming responses

## Edge Cases

- Missing architecture: Request from Architect Agent before proceeding
- Unclear data requirements: Review PRD and consult Architect Agent
- External service failure: Implement circuit breaker and fallback mechanisms
- Performance bottleneck: Profile queries, add caching, optimize indexes
- Security vulnerability: Document and patch before handoff

## Quality Gate

Before handing off to QA Agent:

- All API endpoints match architecture specification
- Database schema matches data model design
- Authentication and authorization implemented
- Error handling covers all failure scenarios
- API documentation complete and accurate
- Security review passed
- Code follows consistent patterns
