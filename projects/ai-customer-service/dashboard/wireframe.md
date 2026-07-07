# Dashboard Wireframe

## Desktop View (1200px+)

```
+------------------------------------------------------------+
| Logo | Navigation | User Profile                           |
+------------------------------------------------------------+
| Side Navigation |                                           |
|-----------------|                                           |
| Tickets         | 4 KPI Cards (Open, Response Time,        |
| Agents          | Satisfaction, Active)                     |
| Knowledge Base  |                                           |
+-----------------+-------------------------------------------+
|                   Ticket Volume Trend (24h)                |
|                   [Chart.js Line Chart]                    |
+------------------------------------------------------------+
| Recent Tickets (Latest 10)                                  |
| +--------------------------------------------------------+ |
| | ID | Customer | Priority | Status | Assigned To | Created | |
| +--------------------------------------------------------+ |
| | 1  | John D   | High     | Open   | Agent A     | 2h ago  | |
| | 2  | Jane S   | Medium   | Closed | Agent B     | 3h ago  | |
| | ...                                                    | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+
| Activity Feed                                               |
| +--------------------------------------------------------+ |
| | [Avatar] John D - Created ticket (2h ago)              | |
| | [Avatar] Agent A - Assigned to Jane (1h ago)           | |
| | [Avatar] Jane S - Closed ticket (30 min ago)           | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+
| Floating Action Button: + (Create Ticket)                   |
+------------------------------------------------------------+
```

## Tablet View (768px-1200px)

```
+------------------------------------------------------------+
| Logo | Hamburger | Notification                           |
+------------------------------------------------------------+
| Search Bar                                                  |
+------------------------------------------------------------+
| 2 KPI Cards per row                                         |
| (Open & Response Time)                                     |
+------------------------------------------------------------+
| (Satisfaction & Active)                                    |
+------------------------------------------------------------+
| Ticket Volume Trend (24h)                                   |
| [Chart.js Line Chart]                                       |
+------------------------------------------------------------+
| Recent Tickets                                              |
| +--------------------------------------------------------+ |
| | ID | Customer | Status | Assigned To | Created            | |
| +--------------------------------------------------------+ |
| | 1  | John D   | Open   | Agent A     | 2h ago             | |
| | 2  | Jane S   | Closed | Agent B     | 3h ago             | |
| | ...                                                    | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+
| Activity Feed                                               |
| +--------------------------------------------------------+ |
| | [Avatar] John D - Created ticket (2h ago)              | |
| | [Avatar] Agent A - Assigned to Jane (1h ago)           | |
| | [Avatar] Jane S - Closed ticket (30 min ago)           | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+
| Floating Action Button: + (Create Ticket)                   |
+------------------------------------------------------------+
```

## Mobile View (<768px)

```
+------------------------------------------------------------+
| Hamburger | Notification                                     |
+------------------------------------------------------------+
| Search Bar                                                  |
+------------------------------------------------------------+
| KPI Card                                                  |
| [Open Tickets]                                            |
| Large number: 24                                          |
| Description: Current open tickets                           |
+------------------------------------------------------------+
| KPI Card                                                  |
| [Avg. Response Time]                                      |
| Large number: 15 min                                      |
| Description: Average response time                          |
+------------------------------------------------------------+
| KPI Card                                                  |
| [Satisfaction]                                            |
| Large number: 89%                                         |
| Description: Customer satisfaction                          |
+------------------------------------------------------------+
| KPI Card                                                  |
| [Active Agents]                                           |
| Large number: 12                                          |
| Description: Currently active agents                        |
+------------------------------------------------------------+
| Ticket Volume Trend (24h)                                   |
| [Chart.js Line Chart]                                       |
+------------------------------------------------------------+
| Recent Tickets                                              |
| +--------------------------------------------------------+ |
| | John D - Open - 2h ago                                 | |
| | Jane S - Closed - 3h ago                               | |
| | ...                                                    | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+
| Activity Feed                                               |
| +--------------------------------------------------------+ |
| | [Avatar] John D - Created ticket (2h ago)              | |
| | [Avatar] Agent A - Assigned to Jane (1h ago)           | |
| | [Avatar] Jane S - Closed ticket (30 min ago)           | |
| +--------------------------------------------------------+ |
+------------------------------------------------------------+
| Floating Action Button: + (Create Ticket)                   |
+------------------------------------------------------------+
```

## Key Interactions

1. KPI Cards
   - Hover shows detailed metric information
   - Click opens metric details page

2. Ticket Table
   - Click on row opens ticket details
   - Status filter dropdown
   - Search bar at top

3. Chart
   - Time range selector (24h, 7d, 30d)
   - Tooltip on hover showing exact numbers

4. Activity Feed
   - Filter by agent or customer
   - Load more button at bottom

5. Quick Actions
   - Floating action button expands to show all actions
   - Primary action (Create Ticket) always visible

6. Navigation
   - Side navigation on desktop
   - Hamburger menu on mobile/tablet
   - Active section highlighted

## Responsiveness

1. Desktop
   - Full 12-column grid
   - Side navigation
   - All table columns visible

2. Tablet
   - 12-column grid with 2 KPI cards per row
   - Hamburger menu
   - Condensed table view

3. Mobile
   - Single column layout
   - Simplified KPI cards
   - Compact activity feed
   - Hamburger menu

## Visual Hierarchy

1. Highest priority: KPI Cards
2. Second priority: Ticket Volume Trend
3. Third priority: Recent Tickets
4. Fourth priority: Activity Feed

## Color Application

1. Primary Blue (#007bff): Action buttons, headers
2. Success Green (#28a745): Resolved tickets, success states
3. Warning Orange (#ffc107): Pending tickets, warnings
4. Danger Red (#dc3545): Critical issues, errors

## Typography

1. Headings: 24px, Bold, Uppercase
2. KPI Values: 28px, Bold
3. KPI Descriptions: 14px, Gray
4. Table Text: 14px
5. Activity Feed: 14px

## Spacing

1. Card padding: 16px
2. Grid gutter: 20px
3. Section spacing: 30px
4. Mobile spacing: 15px

## Accessibility

1. ARIA labels for all interactive elements
2. Keyboard navigation support
3. Sufficient color contrast
4. Screen reader support for all content

## States

1. Loading state: Skeleton screens for cards and charts
2. Empty state: Illustration and message when no tickets
3. Error state: Error message with refresh button
4. Success state: Toast notification after actions

## Transitions

1. KPI card hover: 0.2s ease-in-out
2. Chart loading: 0.5s fade-in
3. Table row hover: 0.15s background transition
4. Mobile menu: 0.3s slide-in from left

## Error Handling

1. Data loading error: Retry button with error message
2. Action error: Toast notification with error
3. Empty data: Illustration and message
4. Network error: Offline indicator with retry

## Performance

1. Initial load: 2 seconds or less
2. Data refresh: 5 minute interval
3. User interactions: 0.5 seconds or less response
4. Mobile optimization: 3G network support

## Implementation Plan

1. Create Figma file with design system
2. Design dark/light mode variants
3. Create responsive components
4. Implement layout
5. Add data visualization
6. Implement interactions
7. Add accessibility support
