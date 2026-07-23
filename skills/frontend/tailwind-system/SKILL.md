# Tailwind System Skill

## Goal

Build a consistent and scalable Tailwind CSS design system with design tokens, responsive utilities, and theme architecture.

## When To Use

- Setting up Tailwind for a new project
- Migrating an existing design system to Tailwind
- Creating a custom theme with brand tokens
- Standardizing utility usage across a team

## Workflow

### Step 1

Analyze design requirements.

Identify:

- Brand colors
- Typography scale
- Spacing system
- Border radius values
- Shadow definitions

### Step 2

Define design tokens.

Map to Tailwind config:

- `colors` — brand palette, semantic colors
- `fontSize` — type scale
- `spacing` — spacing scale
- `borderRadius` — corner values
- `boxShadow` — elevation levels

### Step 3

Configure responsive system.

Define:

- Breakpoints (sm, md, lg, xl, 2xl)
- Mobile-first approach
- Container widths

### Step 4

Set up theme architecture.

Organize:

- `tailwind.config.ts` — base configuration
- CSS variables — dynamic theming
- Dark mode support
- Component-level overrides

### Step 5

Define utility patterns.

Establish:

- Common component patterns
- Custom utilities (if needed)
- Plugin usage
- @apply rules (minimize)

### Step 6

Document the system.

Output:

- Token reference
- Usage guidelines
- Responsive patterns
- Dark mode guide

Output complete Tailwind Design System.

## Rules

1. Use design tokens over hardcoded values.
2. Prefer utility classes over @apply.
3. Follow mobile-first responsive design.
4. Use semantic color names (primary, secondary, danger).
5. Keep the Tailwind config organized and documented.
6. Support dark mode from the start.
7. Avoid custom CSS unless absolutely necessary.
8. Use plugins for repeated patterns.

## Output

- Tailwind configuration file
- Design token documentation
- Responsive breakpoint guide
- Dark mode setup

## Quality Criteria

- All design tokens mapped to Tailwind config
- Responsive system works across all breakpoints
- Dark mode fully supported
- No hardcoded values in components
- Consistent utility patterns
