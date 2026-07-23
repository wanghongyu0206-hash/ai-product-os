# UI Designer Agent SOP

## Prerequisites

- Information Architecture from UX Designer Agent
- User Flow from UX Designer Agent
- Wireframe Specification from UX Designer Agent
- Interaction Specification from UX Designer Agent

## Procedure

### Step 1: Analyze UX

- Read Information Architecture
- Review User Flow
- Study Wireframe Specification
- Understand Interaction Specification
- Identify key pages and components

### Step 2: Select Design Direction

- Evaluate product type (Enterprise, Consumer, AI)
- Evaluate target users
- Use skills/ui/style-selector to choose visual direction
- Reference styles/ for design tokens and guidelines
- Confirm direction before proceeding

### Step 3: Apply Design System

- Load design tokens (colors, typography, spacing)
- Define or extend the design system using skills/ui/design-system
- Ensure token consistency
- Document light/dark mode if required

### Step 4: Define Components

- Identify required components from Wireframe Specification
- Use skills/ui/component-library to select base components
- Define component variants (primary, secondary, ghost)
- Define component states (default, hover, active, disabled, loading, error)
- Use skills/ui/dashboard, skills/ui/card, skills/ui/form, skills/ui/chart as needed

### Step 5: Prepare Handoff

- Generate Component Specification with exact token values
- Generate Page Layout Specification with grid and breakpoints
- Prepare Figma Design Brief
- Package all artifacts for Frontend Agent

## Decision Tree

Enterprise SaaS product
↓
Professional, structured design
↓
Ant Design / Enterprise style

AI product
↓
Modern, intelligent interface
↓
ChatGPT / Claude / Linear style

Consumer product
↓
Friendly, emotional design
↓
Apple / Stripe / Notion style

Dashboard-heavy product
↓
Data-dense layout
↓
skills/ui/dashboard

Form-heavy product
↓
Structured input flows
↓
skills/ui/form

## Edge Cases

- Missing UX document: Request from UX Designer Agent before proceeding
- Missing brand guidelines: Use style-selector to choose a default direction
- Conflicting requirements: Prioritize user experience over visual preference
- No matching component in library: Define new component following design system rules
- Dark mode required: Extend design tokens to include dark mode values

## Quality Gate

Before handing off to Frontend Agent:

- All design tokens defined with exact values
- All components have defined states
- Visual consistency verified across all pages
- Responsive behavior documented (mobile, tablet, desktop)
- Component reuse maximized
- Developer-ready specification with implementation notes
