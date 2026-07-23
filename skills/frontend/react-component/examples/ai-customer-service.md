# AI Customer Service — Component Example

## Scenario

Build a ConversationCard component for the AI Customer Service dashboard that displays active customer conversations with AI-generated summaries and status indicators.

## Input

- Conversation data (id, customer name, last message, status, AI summary)
- Status types: Active, Waiting, Resolved
- Click action to open conversation detail

## Process

### Step 1: Define Props

```typescript
interface ConversationCardProps {
  conversation: {
    id: string;
    customerName: string;
    lastMessage: string;
    status: 'active' | 'waiting' | 'resolved';
    aiSummary?: string;
    updatedAt: Date;
  };
  onClick?: (id: string) => void;
  className?: string;
}
```

### Step 2: Choose Composition

Use Presentational pattern — pure display component with no internal state.

### Step 3: Implement

- Status badge with color coding
- Truncated last message preview
- AI summary section (optional)
- Relative time display
- Keyboard accessible (Enter to click)

### Step 4: Accessibility

- `role="button"` for clickable cards
- `aria-label` with conversation summary
- Focus ring visible on keyboard navigation

## Output

- `ConversationCard` component with typed props
- Status badge sub-component
- Storybook stories for all states
