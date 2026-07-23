# Frontend Performance Skill

## Goal

Optimize frontend performance through rendering optimization, bundle size reduction, loading performance improvements, and runtime performance tuning.

## When To Use

- Optimizing slow-loading pages
- Reducing bundle size
- Improving Core Web Vitals scores
- Optimizing React component rendering
- Implementing code splitting
- Reducing time to interactive
- Optimizing images and assets

## Workflow

### Step 1

Measure current performance baseline.

Analyze:
- Core Web Vitals (LCP, FID, CLS)
- Bundle size and composition
- Rendering performance metrics
- Network waterfall analysis
- JavaScript execution time

### Step 2

Optimize rendering performance.

Techniques:
- React.memo for expensive components
- useMemo for expensive calculations
- useCallback for stable function references
- Virtual list for large datasets
- Lazy loading for below-fold content

### Step 3

Reduce bundle size.

Strategies:
- Code splitting with dynamic imports
- Tree shaking optimization
- Dependency analysis and pruning
- Route-based chunking
- Vendor chunk separation

### Step 4

Optimize loading performance.

Implement:
- Critical CSS extraction
- Resource hints (preload, prefetch)
- Image optimization (WebP, AVIF)
- Font loading strategy
- Progressive hydration

### Step 5

Optimize runtime performance.

Apply:
- Debounce/throttle for user input
- Web Workers for heavy computation
- RequestAnimationFrame for animations
- Efficient event handling
- Memory leak prevention

### Step 6

Implement caching strategies.

Configure:
- Service Worker caching
- HTTP cache headers
- CDN configuration
- API response caching

### Step 7

Monitor and iterate.

Set up:
- Performance monitoring (Web Vitals)
- Real User Monitoring (RUM)
- Performance budgets
- Automated performance testing

## Rules

1. Measure before optimizing—avoid premature optimization.
2. Focus on user-perceived performance (Core Web Vitals).
3. Set performance budgets and enforce them.
4. Optimize the critical rendering path first.
5. Use code splitting to reduce initial bundle size.
6. Lazy load non-critical resources.
7. Optimize images—they're often the largest assets.
8. Monitor performance in production continuously.

## Output

- Performance audit report
- Optimization recommendations
- Implementation plan
- Performance metrics before/after
- Monitoring setup

## Quality Criteria

- LCP < 2.5s, FID < 100ms, CLS < 0.1
- Bundle size within budget
- No render-blocking resources
- Optimized image delivery
- Efficient caching strategy
- Performance monitoring in place
