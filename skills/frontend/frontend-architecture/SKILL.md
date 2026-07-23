# Frontend Architecture Skill

## Goal

Design scalable and maintainable frontend project architecture with clear folder structure, state management strategy, and data flow patterns.

## When To Use

- Starting a new frontend project from scratch
- Migrating existing codebase to modern architecture
- Setting up enterprise-scale applications
- Planning monorepo or multi-app architecture
- Refactoring poorly structured projects

## Workflow

### Step 1

Analyze project requirements and constraints.

Identify:
- Application scale (small, medium, enterprise)
- Team size and structure
- Feature complexity
- Performance requirements
- Deployment strategy

### Step 2

Choose folder structure pattern.

Options:
- **Feature-based**: Group by business features (recommended for most projects)
- **Type-based**: Group by technical type (components, services, utils)
- **Hybrid**: Combine feature and type grouping

### Step 3

Design state management architecture.

Define:
- Global state (Zustand, Redux, Context API)
- Server state (React Query, SWR)
- Local state (useState, useReducer)
- Form state (React Hook Form, Formik)

### Step 4

Define data flow patterns.

Establish:
- API integration strategy
- Error handling flow
- Loading state management
- Cache invalidation strategy

### Step 5

Create module boundaries.

Separate:
- Core components (reusable UI)
- Feature components (business logic)
- Shared utilities
- Configuration

### Step 6

Document architecture decisions.

Output:
- Folder structure diagram
- State management map
- Data flow diagrams
- Module dependency graph
- Decision records (ADRs)

## Rules

1. Follow feature-based structure for most projects.
2. Keep folder depth shallow (max 3-4 levels).
3. Use barrel exports for clean imports.
4. Separate business logic from UI components.
5. Co-locate related files (tests, styles, components).
6. Use TypeScript path aliases for clean imports.
7. Define clear boundaries between features.
8. Document architecture decisions with ADRs.

## Output

- Complete folder structure
- State management architecture
- Data flow patterns
- Module boundaries
- Architecture documentation

## Quality Criteria

- Structure is clear and navigable
- State management is predictable
- Data flow is unidirectional
- Modules are loosely coupled
- Easy to onboard new developers
- Scales with team growth
