# Frontend Review Example

## Scenario

Review a pull request adding a new product search feature to an e-commerce dashboard.

## Input

**Pull Request Details**:
- 15 files changed
- 450 lines added
- New search component with filters
- API integration for product search
- Unit tests included

## Process

### Step 1: Code Structure Review

**Findings**:
✅ Good: Follows feature-based folder structure
✅ Good: Proper barrel exports
⚠️ Issue: Search component in wrong folder (should be in `features/search/`)
⚠️ Issue: Inconsistent file naming (some PascalCase, some kebab-case)

### Step 2: Component Design Review

**Findings**:
✅ Good: Clear prop interfaces with TypeScript
✅ Good: Separation of concerns (UI vs logic)
❌ Critical: Component doing too much (search + filter + results display)
⚠️ Issue: Missing error boundary

**Recommendation**:
```typescript
// Split into smaller components
<SearchBar onSearch={handleSearch} />
<SearchFilters filters={filters} onChange={handleFilterChange} />
<SearchResults results={results} loading={loading} />
```

### Step 3: Accessibility Review

**Findings**:
✅ Good: Semantic HTML (nav, main, section)
✅ Good: ARIA labels on search input
❌ Critical: Missing keyboard navigation for filter dropdown
❌ Critical: Search results not announced to screen readers
⚠️ Issue: Focus not managed when results update

**Recommendation**:
```typescript
// Add live region for search results
<div aria-live="polite" aria-atomic="true">
  {results.length} products found
</div>

// Add keyboard navigation
const handleKeyDown = (event: KeyboardEvent) => {
  if (event.key === 'ArrowDown') {
    focusNextFilter();
  }
};
```

### Step 4: Performance Review

**Findings**:
✅ Good: Debounced search input (300ms)
⚠️ Issue: No React.memo on SearchResults component
❌ Critical: Re-fetching on every keystroke (debounce not working)
⚠️ Issue: Large product images not optimized

**Recommendation**:
```typescript
// Fix debounce
const debouncedSearch = useMemo(
  () => debounce((term: string) => {
    searchProducts(term);
  }, 300),
  []
);

// Add React.memo
const SearchResults = React.memo(({ results, loading }) => {
  // ...
});
```

### Step 5: Code Quality Review

**Findings**:
✅ Good: TypeScript usage throughout
✅ Good: Comprehensive unit tests (85% coverage)
⚠️ Issue: Some magic numbers (pagination size hardcoded)
⚠️ Issue: Missing JSDoc comments on complex functions
❌ Critical: Console.log statements left in code

**Recommendation**:
```typescript
// Extract constants
const PAGINATION_SIZE = 20;
const SEARCH_DEBOUNCE_MS = 300;

// Add JSDoc
/**
 * Searches products with filters and pagination
 * @param searchTerm - The search query string
 * @param filters - Applied filter criteria
 * @param page - Current page number
 * @returns Promise with search results and metadata
 */
async function searchProducts(...) { }
```

### Step 6: Security Review

**Findings**:
✅ Good: Input validation on search term
✅ Good: No sensitive data in client code
⚠️ Issue: Search term not sanitized (potential XSS)
✅ Good: API uses authentication tokens

**Recommendation**:
```typescript
// Sanitize search input
import DOMPurify from 'dompurify';

const sanitizedSearch = DOMPurify.sanitize(searchTerm);
```

## Output

### Review Report Summary

**Overall Rating**: ⚠️ Needs Revision

**Issues Found**:
- 🔴 Critical: 3
- 🟡 High: 2
- 🟢 Medium: 4
- 🔵 Low: 2

### Priority Action Items

1. **CRITICAL**: Fix component responsibility (split into 3 components)
2. **CRITICAL**: Fix keyboard navigation for accessibility
3. **CRITICAL**: Fix debounce implementation
4. **HIGH**: Add screen reader announcements
5. **HIGH**: Remove console.log statements
6. **MEDIUM**: Add React.memo optimizations
7. **MEDIUM**: Extract magic numbers to constants
8. **LOW**: Add JSDoc comments

### Positive Patterns

✅ Clean TypeScript usage
✅ Good folder structure
✅ Comprehensive unit tests
✅ Proper API integration pattern
✅ Good separation of concerns

### Recommendation

**Status**: Request Changes

**Blocking Issues**: 3 critical issues must be fixed before merge
**Non-blocking**: 8 medium/low issues can be addressed in follow-up PR

**Estimated Fix Time**: 2-3 hours

### Follow-up Actions

1. Address critical issues in current PR
2. Create follow-up PR for medium/low issues
3. Add accessibility testing to CI pipeline
4. Update coding standards documentation
5. Schedule team review session on accessibility

### Lessons Learned

1. **Component size matters**—keep components focused
2. **Accessibility is non-negotiable**—test with screen readers
3. **Debounce carefully**—verify it's actually working
4. **Clean up before PR**—remove console.logs, TODOs
5. **Document complex logic**—future developers will thank you
