# Frontend Review Skill

## Goal

Conduct comprehensive frontend code reviews covering code quality, architecture compliance, accessibility, performance, and maintainability.

## When To Use

- Reviewing pull requests
- Conducting code audits
- Onboarding new developers
- Identifying technical debt
- Ensuring coding standards compliance
- Pre-release quality gates

## Workflow

### Step 1

Review code structure and organization.

Check:
- File naming conventions
- Folder structure compliance
- Component organization
- Import/export patterns
- Module boundaries

### Step 2

Review component design and implementation.

Evaluate:
- Component responsibilities (single responsibility principle)
- Props interface design
- State management approach
- Side effects handling
- Error boundaries

### Step 3

Review accessibility implementation.

Verify:
- Semantic HTML usage
- ARIA attributes
- Keyboard navigation
- Screen reader compatibility
- Color contrast ratios
- Focus management

### Step 4

Review performance considerations.

Assess:
- Rendering optimizations (memo, useMemo, useCallback)
- Bundle size impact
- Lazy loading usage
- Image optimization
- Network request patterns

### Step 5

Review code quality and maintainability.

Analyze:
- TypeScript usage and type safety
- Code duplication
- Naming conventions
- Comment quality
- Test coverage
- Documentation completeness

### Step 6

Review security practices.

Check:
- XSS prevention
- Input validation
- Sensitive data handling
- Authentication/authorization
- Dependency vulnerabilities

### Step 7

Generate review report.

Document:
- Issues found (categorized by severity)
- Recommendations
- Positive patterns
- Action items
- Priority ranking

## Rules

1. Focus on maintainability and readability first.
2. Check accessibility compliance rigorously.
3. Verify performance optimizations are applied.
4. Ensure consistent coding standards.
5. Review for security vulnerabilities.
6. Provide constructive, actionable feedback.
7. Prioritize issues by impact (critical, high, medium, low).
8. Highlight positive patterns and best practices.

## Output

- Comprehensive review report
- Issue list with severity ratings
- Recommendations for improvements
- Action items with priorities
- Code examples for fixes

## Quality Criteria

- All accessibility standards checked
- Performance optimizations verified
- Security vulnerabilities identified
- Code quality issues documented
- Actionable recommendations provided
- Clear priority ranking established
