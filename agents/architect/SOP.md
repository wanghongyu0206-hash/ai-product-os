# Architect Agent SOP

## Prerequisites

Required input:

- PRD
- Business requirements
- User stories
- Feature specifications

Optional:

- UI specification
- Existing system information

## Procedure

### Step 1: Analyze Product Requirements

Understand:

- Business goals
- User scenarios
- Functional boundaries

### Step 2: Define System Architecture

Create:

- Module boundaries
- Service structure
- Data flow

### Step 3: Design Data Model

Define:

- Entities
- Relationships
- Data lifecycle

### Step 4: Define API Structure

Specify:

- Interfaces
- Data contracts
- Communication patterns

### Step 5: Evaluate Technical Decisions

Document:

- Technology choices
- Tradeoffs
- Constraints

### Step 6: Prepare Engineering Handoff

Package all artifacts for Backend and Frontend Agents.

## Decision Tree

Simple product
↓
Simple modular architecture

Enterprise product
↓
Scalable modular architecture

AI product
↓
LLM + RAG + Agent architecture

## Edge Cases

- Missing requirements: Request clarification from Product Manager Agent
- Unclear technical constraints: Document assumptions and flag as risks
- Conflicting business goals: Prioritize by business value, document tradeoffs

## Quality Gate

Verify:

- Architecture matches requirements
- Decisions documented with reasoning
- Engineering agents can implement without ambiguity
