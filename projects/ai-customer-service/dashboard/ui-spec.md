# UI Specification for AI Customer Service Dashboard

## Color Scheme
- Primary: Blue (#007bff)
- Success: Green (#28a745)
- Warning: Orange (#ffc107)
- Danger: Red (#dc3545)
- Background: Light gray (#f8f9fa)
- Text: Dark gray (#343a40)

## Typography
- Font family: Arial, Helvetica, sans-serif
- Font size: 14px
- Line height: 1.5
- Headings: Bold, uppercase for section titles

## Grid System
- 12-column responsive grid
- Mobile-first approach
- Desktop: Full width with side navigation
- Mobile: Single column with hamburger menu

## Header
- Logo on left
- User profile dropdown on right
- Navigation links in the center
- Notification icon with badge

## Navigation
- Side navigation (desktop)
- Hamburger menu (mobile)
- Active link highlighted
- Expandable sections for ticket management

## KPI Cards
- 4 equal columns on desktop
- 2 columns on tablet
- 1 column on mobile
- Card background: white
- Box shadow for elevation
- Icon size: 24px
- Value font size: 28px
- Status indicator: small dot next to value

## Charts
- Chart.js library
- Line chart for ticket volume
- Tooltips on hover
- Responsive to container size
- Legend below chart

## Tables
- Compact rows
- Alternating row colors
- Hover effect
- Status badges:
  - Open: Blue
  - In Progress: Orange
  - Resolved: Green
  - Closed: Gray
- Clickable rows

## Activity Feed
- Timeline layout
- Avatar for each participant
- Time stamps relative (e.g., 2 hours ago)
- Filter controls above feed
- Load more button at the bottom

## Quick Actions
- Floating action button (FAB) in bottom right
- Menu items:
  - Create Ticket (primary action)
  - Knowledge Base
  - Agent Status
- Icons for each action

## Responsive Breakpoints
- Mobile: < 768px
- Tablet: 768px - 992px
- Desktop: > 992px

## Accessibility
- ARIA labels for all interactive elements
- Keyboard navigation support
- Sufficient color contrast
