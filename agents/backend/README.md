# Backend Agent

This agent transforms technical architecture into reliable backend systems and services.

## Purpose

Backend Agent implements the server-side logic of the AI Product OS pipeline. It takes architecture specifications from Architect Agent and produces production-ready API services, database schemas, authentication systems, and AI infrastructure integrations.

## Workflow

```
Architect Agent
       ↓
Backend Agent
       ↓
   QA Agent
```

## Input

From: Architect Agent

- System Architecture Document
- API Specification
- Database Model
- Technical Decisions
- AI Architecture Design (when applicable)

## Output

To: QA Agent

1. Backend Architecture Plan
   - Service structure
   - Module design
   - Runtime architecture

2. API Implementation Plan
   - Endpoint design
   - Request/response models
   - Error handling

3. Database Implementation Plan
   - Schema design
   - Data relationships
   - Index strategy

4. Authentication and Authorization Design
   - User identity
   - Permission model

5. AI Backend Implementation Plan
   - LLM service integration
   - Vector database
   - Retrieval pipeline

6. QA Handoff Package

## Capabilities

- API development (REST, GraphQL)
- Database design and implementation
- Authentication and authorization
- AI infrastructure (LLM, RAG, vector DB)
- Security configuration
- Performance optimization
