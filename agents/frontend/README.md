# Frontend Agent

This agent transforms UI specifications and technical architecture into maintainable frontend implementations.

## Purpose

Frontend Agent is the implementation layer of the AI Product OS pipeline. It takes visual design specs from UI Designer Agent and technical architecture from Architect Agent, then produces production-ready React code with proper component structure, API integration, and interaction states.

## Workflow

```
UI Designer Agent  +  Architect Agent
         ↓
    Frontend Agent
         ↓
      QA Agent
```

## Input

From: UI Designer Agent

- Design tokens (colors, typography, spacing)
- Component specification (hierarchy, variants, states)
- Layout specification (grid, breakpoints)
- Interaction rules

From: Architect Agent

- Frontend architecture (project structure, state management)
- API contracts (endpoints, data shapes)
- Technical constraints

## Output

To: QA Agent

1. Frontend Architecture
   - Project structure
   - Component architecture
   - State management strategy

2. Component Implementation Plan
   - Component hierarchy
   - Reusable components
   - Props design

3. Frontend Code
   - React components
   - Pages
   - Hooks
   - Styles

4. Integration Specification
   - API integration
   - Error handling
   - Loading states

5. Frontend Quality Report

6. QA Handoff Package

## Capabilities

- Component development (React, Next.js)
- Frontend architecture design
- API integration implementation
- Performance optimization
- Responsive layout implementation
- Design system token application
