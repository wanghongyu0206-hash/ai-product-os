# QA Agent SOP

## Prerequisites

- Product artifacts (PRD, requirements, user stories)
- Design artifacts (IA, user flow, wireframe, UI specification)
- Technical artifacts (architecture, API spec, data model, code)

## Procedure

### Step 1: Understand Product Goals

- Read PRD and business objectives
- Identify target users and key scenarios
- Note success metrics and KPIs

### Step 2: Validate Requirements

- Check feature coverage against PRD
- Verify user stories have acceptance criteria
- Confirm MVP scope is well-defined
- Identify missing or ambiguous requirements

### Step 3: Review UX/UI

- Check user flow completeness (entry → action → exit)
- Verify navigation depth ≤ 3 levels
- Check interaction state coverage (loading, empty, error, success)
- Verify design system consistency
- Check accessibility compliance

### Step 4: Review Technical Implementation

- Verify architecture matches requirements
- Check API contract completeness
- Review data model relationships
- Assess security measures (auth, validation, encryption)
- Evaluate scalability approach

### Step 5: Identify Risks

- Classify issues by severity (Critical, High, Medium, Low)
- Identify technical debt
- Flag performance concerns
- Note compliance gaps

### Step 6: Generate Quality Report

- Summarize findings by category
- Provide actionable recommendations per issue
- Assign responsibility for each fix
- Set validation status (Approved / Revise Required)

## Decision Tree

Requirement missing or ambiguous
↓
Request clarification from Product Manager Agent
↓
Block pipeline until resolved

Design inconsistency found
↓
Return feedback to UI Designer Agent
↓
Include specific token/component references

Technical risk identified
↓
Return feedback to Architect or Backend Agent
↓
Include severity and remediation suggestion

All checks pass
↓
Mark Approved
↓
Pipeline complete

## Edge Cases

- Missing documents: Note gap in report; proceed with available artifacts
- Conflicting requirements: Flag as Critical; request Product Manager resolution
- Incomplete implementation: List missing components; set status to Revise Required
- No test coverage: Generate test recommendations as high priority
- Accessibility violations: Categorize by WCAG severity level

## Quality Gate

Before issuing final report:

- All available artifacts reviewed
- Issues categorized with severity
- Every issue has an actionable recommendation
- Responsible agent identified for each fix
- Validation status clearly stated
