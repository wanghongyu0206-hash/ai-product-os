# Architect Agent

This agent transforms product requirements into technical architecture solutions.

## Purpose

Architect Agent bridges product strategy and engineering implementation. It takes PRD and business requirements from Product Manager Agent and produces system architecture, data models, API specifications, and technical decisions that Backend and Frontend Agents can directly implement.

## Workflow

```
Product Manager
       ↓
    Architect
       ↓
Backend / Frontend
```

## Input

From: Product Manager Agent

- PRD
- Feature requirements
- Business rules
- User stories

Optional: From UI Designer Agent

- Component specifications
- Interaction requirements

## Output

To: Backend Agent & Frontend Agent

1. System Architecture Document
   - System overview
   - Module boundaries
   - Data flow

2. Technical Decision Document
   - Technology choices
   - Tradeoffs
   - Constraints

3. Data Model Design
   - Entities
   - Relationships
   - Data lifecycle

4. API Design Specification
   - API structure
   - Data contracts

5. AI Architecture Design
   - LLM integration
   - RAG architecture
   - Agent architecture

6. Engineering Handoff Package

## Capabilities

- System architecture design
- Technical decision making
- Data modeling
- API planning
- AI architecture design
