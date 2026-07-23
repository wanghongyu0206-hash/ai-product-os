# AI Customer Service — Tailwind System Example

## Scenario

Configure a Tailwind CSS design system for an AI Customer Service SaaS application with enterprise branding, dark mode support, and responsive dashboard layouts.

## Input

- Brand colors: Primary blue (#0066FF), Success green, Warning amber, Error red
- Typography: Inter font family
- Spacing: 8px base grid
- Dark mode required

## Process

### Step 1: Design Tokens

```typescript
// tailwind.config.ts
export default {
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#E6F0FF',
          100: '#CCE0FF',
          500: '#0066FF',
          600: '#0052CC',
          700: '#003D99',
        },
        success: { DEFAULT: '#10B981', light: '#D1FAE5' },
        warning: { DEFAULT: '#F59E0B', light: '#FEF3C7' },
        error: { DEFAULT: '#EF4444', light: '#FEE2E2' },
        surface: {
          DEFAULT: 'var(--surface)',
          secondary: 'var(--surface-secondary)',
        },
      },
      fontFamily: { sans: ['Inter', 'sans-serif'] },
      spacing: {
        '0.5': '2px',
        '1': '4px',
        '2': '8px',
        '3': '12px',
        '4': '16px',
        '6': '24px',
        '8': '32px',
        '12': '48px',
        '16': '64px',
      },
      borderRadius: {
        sm: '4px',
        DEFAULT: '8px',
        md: '12px',
        lg: '16px',
      },
      boxShadow: {
        card: '0 1px 3px rgba(0,0,0,0.1)',
        dropdown: '0 4px 12px rgba(0,0,0,0.15)',
        modal: '0 8px 24px rgba(0,0,0,0.2)',
      },
    },
  },
}
```

### Step 2: CSS Variables for Dark Mode

```css
:root {
  --surface: #ffffff;
  --surface-secondary: #f5f5f5;
  --text-primary: #171717;
  --text-secondary: #525252;
  --border: #e5e5e5;
}

.dark {
  --surface: #171717;
  --surface-secondary: #262626;
  --text-primary: #fafafa;
  --text-secondary: #a3a3a3;
  --border: #404040;
}
```

### Step 3: Responsive Breakpoints

| Breakpoint | Width | Usage |
|-----------|-------|-------|
| sm | 640px | Mobile landscape |
| md | 768px | Tablet |
| lg | 1024px | Desktop |
| xl | 1280px | Large desktop |
| 2xl | 1536px | Extra large |

### Step 4: Component Patterns

```tsx
// Card pattern
<div className="rounded-lg bg-surface border border-border shadow-card p-6">

// Button pattern
<button className="rounded-md bg-primary-500 text-white px-4 py-2 hover:bg-primary-600">

// Dashboard grid
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
```

## Output

- Complete `tailwind.config.ts` with all tokens
- CSS variables for light/dark mode
- Responsive breakpoint documentation
- Common component utility patterns
