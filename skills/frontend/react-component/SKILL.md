# React Component Skill

## Goal

Design and implement reusable React components with clear prop interfaces, proper state management, and composable architecture.

## When To Use

- Building UI component libraries
- Creating reusable business components
- Designing component APIs for team consumption
- Refactoring existing components for better reusability

## Workflow

### Step 1

Analyze component requirements.

Identify:

- Component purpose and responsibility
- Input data (props)
- User interactions
- Visual states

### Step 2

Design prop interface.

Define:

- Required props
- Optional props
- Default values
- Prop types (TypeScript interfaces)

### Step 3

Design component composition.

Choose pattern:

- Container/Presentational
- Compound components
- Render props
- Custom hooks

### Step 4

Implement state management.

Decide:

- Local state vs lifted state
- Derived state vs stored state
- When to use Context vs props

### Step 5

Implement component logic.

Follow:

- Single responsibility principle
- Composition over inheritance
- Declarative over imperative

### Step 6

Add accessibility and testing.

Include:

- ARIA attributes
- Keyboard navigation
- Unit tests
- Integration tests

### Step 7

Document component API.

Output:

- Props documentation
- Usage examples
- Accessibility notes

Output complete React Component Specification.

## Rules

1. Prefer composition over inheritance.
2. Keep components focused on a single responsibility.
3. Design props for flexibility but enforce required contracts.
4. Use TypeScript for type safety.
5. Separate business logic from presentation.
6. Optimize for reusability across the application.
7. Follow React best practices (hooks, effects, memoization).
8. Ensure accessibility from the start.

## Output

- Component specification document
- TypeScript interfaces
- Usage examples
- Test cases

## Quality Criteria

- Props are well-typed and documented
- Component is reusable and composable
- State management is clear and efficient
- Accessibility requirements met
- Tests cover key scenarios
