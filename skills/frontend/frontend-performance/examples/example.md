# Frontend Performance Example

## Scenario

E-commerce SaaS dashboard experiencing slow page loads and poor Core Web Vitals scores.

## Input

**Current Performance**:
- LCP: 4.2s (target: < 2.5s)
- FID: 180ms (target: < 100ms)
- CLS: 0.25 (target: < 0.1)
- Bundle size: 2.8MB (target: < 500KB)
- Time to Interactive: 6.5s

**Tech Stack**:
- React 18 + Next.js 14
- Redux Toolkit
- Recharts (charting library)
- Material-UI

## Process

### Step 1: Performance Audit

**Bundle Analysis**:
```
Total Bundle: 2.8MB
├── react + react-dom: 140KB
├── redux-toolkit: 80KB
├── recharts: 890KB (problem!)
├── material-ui: 620KB
├── moment.js: 320KB (problem!)
└── app code: 750KB
```

**Issues Identified**:
1. Recharts imported entirely (890KB)
2. moment.js included (320KB, replace with date-fns)
3. Material-UI not tree-shaken
4. No code splitting
5. Large images not optimized

### Step 2: Rendering Optimization

**Applied Techniques**:

1. **React.memo for List Components**:
```typescript
const ProductList = React.memo(({ products }) => {
  return products.map(product => (
    <ProductCard key={product.id} {...product} />
  ));
});
```

2. **useMemo for Expensive Calculations**:
```typescript
const filteredProducts = useMemo(() => {
  return products.filter(p => 
    p.name.toLowerCase().includes(searchTerm.toLowerCase())
  );
}, [products, searchTerm]);
```

3. **Virtual List for Large Datasets**:
```typescript
import { FixedSizeList } from 'react-window';

<FixedSizeList
  height={600}
  itemCount={products.length}
  itemSize={100}
>
  {ProductRow}
</FixedSizeList>
```

### Step 3: Bundle Size Reduction

**Actions Taken**:

1. **Replace moment.js with date-fns**:
```typescript
// Before: import moment from 'moment'; (320KB)
// After: import { format } from 'date-fns'; (tree-shakeable)
```

2. **Lazy Load Recharts**:
```typescript
const Chart = lazy(() => import('./Chart'));

<Suspense fallback={<ChartSkeleton />}>
  <Chart data={analyticsData} />
</Suspense>
```

3. **Route-Based Code Splitting**:
```typescript
const Dashboard = lazy(() => import('./pages/Dashboard'));
const Analytics = lazy(() => import('./pages/Analytics'));
const Settings = lazy(() => import('./pages/Settings'));
```

4. **Tree-Shake Material-UI**:
```typescript
// Before: import { Button } from '@mui/material';
// After: import Button from '@mui/material/Button';
```

### Step 4: Loading Performance

**Optimizations**:

1. **Critical CSS Inline**:
```html
<style>
  /* Critical above-the-fold styles */
  .header { ... }
  .nav { ... }
  .hero { ... }
</style>
```

2. **Resource Hints**:
```html
<link rel="preload" href="/fonts/inter.woff2" as="font" crossorigin>
<link rel="prefetch" href="/dashboard.js">
```

3. **Image Optimization**:
```typescript
import Image from 'next/image';

<Image
  src="/product.jpg"
  width={800}
  height={600}
  placeholder="blur"
  blurDataURL="data:image/jpeg;base64,..."
/>
```

4. **Font Loading Strategy**:
```css
@font-face {
  font-family: 'Inter';
  src: url('/fonts/inter.woff2') format('woff2');
  font-display: swap;
}
```

### Step 5: Runtime Performance

**Optimizations**:

1. **Debounce Search Input**:
```typescript
import { debounce } from 'lodash';

const debouncedSearch = debounce((term) => {
  setSearchResults(searchProducts(term));
}, 300);
```

2. **Web Worker for Data Processing**:
```typescript
// worker.js
self.onmessage = (event) => {
  const processed = heavyComputation(event.data);
  self.postMessage(processed);
};

// main.js
const worker = new Worker('./worker.js');
worker.postMessage(largeDataset);
worker.onmessage = (event) => {
  setResults(event.data);
};
```

### Step 6: Caching Strategy

**Service Worker Configuration**:
```javascript
// Cache static assets
workbox.routing.registerRoute(
  /\.(?:js|css|woff2)$/,
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: 'static-assets',
  })
);

// Cache images
workbox.routing.registerRoute(
  /\.(?:png|jpg|jpeg|svg|gif|webp)$/,
  new workbox.strategies.CacheFirst({
    cacheName: 'images',
    expiration: {
      maxEntries: 50,
      maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
    },
  })
);
```

## Output

### Performance Results

**After Optimization**:
- LCP: 1.8s ✅ (from 4.2s)
- FID: 45ms ✅ (from 180ms)
- CLS: 0.05 ✅ (from 0.25)
- Bundle size: 420KB ✅ (from 2.8MB)
- Time to Interactive: 2.1s ✅ (from 6.5s)

**Bundle Reduction**:
```
Before: 2.8MB
After:  420KB
Reduction: 85%
```

### Key Improvements

1. **Bundle Size**: -85% through code splitting and tree shaking
2. **LCP**: -57% through image optimization and critical CSS
3. **FID**: -75% through lazy loading and code splitting
4. **CLS**: -80% through image dimensions and font loading strategy

### Monitoring Setup

**Web Vitals Tracking**:
```typescript
import { onCLS, onFID, onLCP } from 'web-vitals';

onCLS(sendToAnalytics);
onFID(sendToAnalytics);
onLCP(sendToAnalytics);
```

**Performance Budget**:
```json
{
  "performance": {
    "budget": {
      "maxBundleSize": "500KB",
      "maxImageSize": "200KB",
      "maxFirstLoad": "3s"
    }
  }
}
```

### Lessons Learned

1. **Measure first**—don't optimize blindly
2. **Focus on user metrics**—Core Web Vitals matter
3. **Code splitting is powerful**—85% bundle reduction
4. **Images are often the culprit**—always optimize
5. **Lazy load everything non-critical**
6. **Monitor continuously**—performance regresses

### Next Steps

1. Set up automated performance testing in CI/CD
2. Implement Real User Monitoring (RUM)
3. Create performance dashboards
4. Establish performance review process
5. Train team on performance best practices
