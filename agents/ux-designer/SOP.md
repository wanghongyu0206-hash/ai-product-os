# UX Designer Agent SOP

## Prerequisites

- PRD.md received from Product Manager Agent
- User Stories available
- Feature Requirements defined
- User Personas identified

## Procedure

### Step 1: Receive and Analyze PRD

- Read PRD.md
- Extract functional requirements
- Identify business goals
- Note key metrics

### Step 2: Analyze User Goals

- Map user personas to goals
- Identify primary user scenarios
- List user tasks by frequency
- Prioritize core workflows

### Step 3: Define Information Architecture

- Group features into logical modules
- Design navigation hierarchy (depth ≤ 3)
- Generate page list
- Create sitemap

### Step 4: Design User Flow

- Define entry and exit points for each flow
- Map decision points
- Identify system responses
- Optimize for efficiency

### Step 5: Create Interaction Specification

- Define user actions (click, input, upload, etc.)
- Define system feedback (loading, success, error)
- Define confirmation actions (delete, archive, reset)
- Define page states (empty, loading, error, no permission)

### Step 6: Create Wireframe Specification

- Identify page purpose and primary task
- Define page regions (header, navigation, main content)
- Arrange content by importance
- Place UI components
- Review layout hierarchy

### Step 7: Review UX Quality

- Check navigation clarity
- Check user flow completeness
- Check interaction consistency
- Check accessibility compliance
- Generate improvement suggestions

## Decision Tree

- If PRD is incomplete → Request clarification from Product Manager Agent
- If user goals are unclear → Conduct user analysis using skills/ux/user-flow
- If navigation depth > 3 → Simplify information architecture
- If flow has unnecessary steps → Optimize using skills/ux/user-flow
- If interaction is inconsistent → Review using skills/ux/interaction

## Edge Cases

- Multi-role users: Design for primary role first, support secondary roles
- Empty states: Always provide guidance (create, upload, invite)
- Error states: Always provide recovery path
- Permission denied: Show clear message and alternative actions
- Network offline: Cache data and sync when online

## Quality Gate

Before handing off to UI Designer Agent:

- All core user flows complete
- Navigation depth ≤ 3 levels
- Every page has one clear responsibility
- Interaction states defined (loading, empty, error, success)
- Accessibility requirements met
- UX Review Report generated
