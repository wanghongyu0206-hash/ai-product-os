# shadcn Component Skill

## Goal

Implement and customize shadcn/ui components to build consistent, accessible, and production-ready interfaces.

## When To Use

- Building applications with shadcn/ui component library
- Customizing existing shadcn components for specific needs
- Creating new variants of base components
- Ensuring accessibility compliance

## Workflow

### Step 1

Analyze component requirements.

Identify:

- Required component types
- Customization needs
- Accessibility requirements
- Integration points

### Step 2

Install and configure components.

Actions:

- Install via CLI
- Configure theme tokens
- Set up component aliases
- Verify dependencies

### Step 3

Customize component variants.

Approach:

- Extend base component props
- Add custom variants using CVA
- Override default styles
- Create compound components

### Step 4

Implement accessibility.

Include:

- ARIA attributes
- Keyboard navigation
- Focus management
- Screen reader support

### Step 5

Integrate with application.

Steps:

- Import and compose components
- Handle state management
- Add event handlers
- Test interactions

### Step 6

Document customizations.

Output:

- Component API documentation
- Usage examples
- Accessibility notes
- Customization guide

Output complete shadcn Component Implementation.

## Rules

1. Always use the CLI to install components initially.
2. Extend rather than replace base components.
3. Maintain accessibility as a first-class concern.
4. Use CVA (Class Variance Authority) for variants.
5. Keep customizations in a dedicated directory.
6. Document all custom props and variants.
7. Test keyboard navigation thoroughly.
8. Follow shadcn/ui conventions and patterns.

## Output

- Customized component code
- Variant definitions
- Accessibility implementation
- Usage documentation

## Quality Criteria

- Components are fully accessible (WCAG AA)
- Variants work correctly across states
- Keyboard navigation is smooth
- Documentation is complete and accurate
- No breaking changes to base component API
