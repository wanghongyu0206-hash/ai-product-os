# Example: Custom Data Table with Sorting and Filtering

## Scenario

Build a custom data table component for an AI-powered analytics dashboard using shadcn/ui's Table component as the base.

## Input

- Base component: shadcn/ui Table
- Requirements: Sorting, filtering, pagination, row selection
- Data: Analytics metrics with 1000+ rows
- Accessibility: Full keyboard navigation

## Process

1. **Install Base Component**

```bash
npx shadcn-ui@latest add table
```

2. **Create Custom Wrapper**

```tsx
// components/data-table/data-table.tsx
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"

interface DataTableProps<TData> {
  data: TData[]
  columns: ColumnDef<TData>[]
  enableSorting?: boolean
  enableFiltering?: boolean
  enableSelection?: boolean
}

export function DataTable<TData>({ data, columns, ...props }: DataTableProps<TData>) {
  // Implementation with sorting, filtering, pagination
}
```

3. **Add Variants with CVA**

```tsx
const tableVariants = cva("w-full", {
  variants: {
    size: {
      sm: "text-sm",
      md: "text-base",
      lg: "text-lg",
    },
    density: {
      compact: "py-2",
      comfortable: "py-4",
    },
  },
  defaultVariants: {
    size: "md",
    density: "comfortable",
  },
})
```

4. **Implement Accessibility**

- Add `role="grid"` to table
- Keyboard navigation for row selection
- ARIA labels for sort buttons
- Announce sort changes to screen readers

## Output

- `DataTable` component with full feature set
- Type-safe column definitions
- Keyboard-accessible sorting and selection
- Complete usage documentation with examples
