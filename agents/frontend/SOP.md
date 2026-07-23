# Frontend Agent SOP

## Prerequisites

- UI Specification from UI Designer Agent (design tokens, component spec, layout spec, interaction rules)
- Frontend Architecture from Architect Agent (project structure, API contracts, technical constraints)

## Procedure

### Step 1: Analyze UI Requirements

- Read design token specification
- Review component specification and hierarchy
- Understand layout rules and breakpoints
- Map interaction states to component props

### Step 2: Define Project Structure

- Set up directory structure (components, pages, hooks, utils, styles)
- Configure build tooling
- Set up design token integration (CSS variables or theme provider)
- Define routing structure

### Step 3: Create Component Plan

- Map UI components to React component tree
- Identify reusable base components
- Define prop interfaces for each component
- Plan component variants and states

### Step 4: Implement Frontend

- Build base design token layer
- Implement base components first
- Build page-level components
- Apply responsive layout rules
- Add interaction states (hover, loading, error, empty)

### Step 5: Integrate Backend APIs

- Create API service layer
- Implement data fetching with loading/error states
- Handle form submissions and validation
- Manage authentication state

### Step 6: Review Quality

- Check component reuse rate
- Verify design token compliance
- Test responsive behavior
- Run accessibility audit
- Check performance (bundle size, render performance)

## Decision Tree

Simple dashboard
↓
Component-based React implementation
↓
Flat component structure, minimal state

Enterprise application
↓
Scalable frontend architecture
↓
Module-based structure, shared component library

AI application
↓
Streaming UI and async states
↓
Real-time data components, progressive rendering

## Edge Cases

- Missing design specification: Request from UI Designer Agent before proceeding
- Missing API contract: Request from Architect Agent; use mock data as temporary fallback
- Conflicting requirements: Prioritize UI specification for visual; prioritize Architect for data flow
- Performance bottleneck: Profile, then optimize with memoization, virtualization, code splitting
- Accessibility gap: Document known issues and provide remediation plan

## Quality Gate

Before handing off to QA Agent:

- All components follow design system tokens
- Component reuse rate is high (no duplicate components)
- Responsive behavior works on mobile, tablet, desktop
- All interaction states implemented
- Error handling covers API failures and form validation
- Accessibility requirements met (contrast, keyboard nav, ARIA)
- Code follows consistent patterns and naming conventions
