# Next.js App Router Skill

## Goal

Design and implement Next.js App Router applications with proper Server/Client Component separation, routing patterns, and data fetching strategies.

## When To Use

- Building full-stack Next.js applications
- Migrating from Pages Router to App Router
- Designing route architecture for SaaS products
- Implementing server-side rendering strategies

## Workflow

### Step 1

Analyze route requirements.

Identify:

- Page hierarchy
- Dynamic routes
- Layout nesting
- Authentication boundaries

### Step 2

Design route structure.

Define:

- File-based routing tree
- Shared layouts
- Loading and error boundaries
- Route groups

### Step 3

Classify components.

Separate into:

- Server Components (default)
- Client Components (interactive)
- Shared Components

### Step 4

Design data fetching strategy.

Choose:

- Server-side fetching (async components)
- Client-side fetching (SWR, React Query)
- Streaming and Suspense
- Cache invalidation strategy

### Step 5

Implement middleware and API routes.

Include:

- Authentication middleware
- Route handlers
- Server Actions
- Edge functions

### Step 6

Optimize performance.

Apply:

- Static generation where possible
- Incremental Static Regeneration
- Image optimization
- Font optimization

### Step 7

Document routing architecture.

Output:

- Route tree diagram
- Component classification
- Data flow documentation

Output complete Next.js Implementation Plan.

## Rules

1. Default to Server Components unless interactivity is required.
2. Keep Client Components as leaf nodes in the component tree.
3. Use layouts for shared UI across routes.
4. Implement loading states with Suspense boundaries.
5. Use Server Actions for form mutations.
6. Cache data aggressively with proper revalidation.
7. Keep route handlers focused on single responsibilities.
8. Use middleware for cross-cutting concerns (auth, logging).

## Output

- Route tree structure
- Component classification (Server/Client)
- Data fetching strategy
- Middleware specification

## Quality Criteria

- Clear Server/Client boundary
- Data fetching is efficient
- Loading states handled gracefully
- SEO-friendly rendering
- Type-safe route parameters
