# AI Customer Service — Next.js App Router Example

## Scenario

Design the route architecture for an AI Customer Service SaaS application with multi-tenant support, role-based access, and real-time conversation updates.

## Input

- Route requirements: Dashboard, Conversations, Knowledge Base, Analytics, Settings
- Authentication: OAuth 2.0 with role-based access
- Real-time: WebSocket for live conversation updates

## Process

### Step 1: Route Tree

```
app/
├── (auth)/
│   ├── login/page.tsx          # Client Component
│   └── layout.tsx              # Auth layout
├── (dashboard)/
│   ├── layout.tsx              # Dashboard layout (Server)
│   ├── page.tsx                # Overview (Server)
│   ├── conversations/
│   │   ├── page.tsx            # List (Server + Streaming)
│   │   ├── [id]/
│   │   │   └── page.tsx        # Detail (Client — WebSocket)
│   ├── knowledge/
│   │   ├── page.tsx            # List (Server)
│   │   └── [id]/page.tsx       # Detail (Server)
│   ├── analytics/page.tsx      # Charts (Server + Client charts)
│   └── settings/
│       ├── page.tsx            # General (Server)
│       └── team/page.tsx       # Team management (Client)
└── api/
    ├── conversations/route.ts  # REST API
    └── knowledge/route.ts      # REST API
```

### Step 2: Component Classification

| Route | Type | Reason |
|-------|------|--------|
| Dashboard overview | Server | Static data, SEO |
| Conversation list | Server + Streaming | Initial SSR, live updates via Suspense |
| Conversation detail | Client | WebSocket, real-time typing |
| Knowledge base | Server | CRUD with Server Actions |
| Analytics | Server + Client | Server data, Client chart rendering |
| Settings | Mixed | General: Server, Team: Client |

### Step 3: Data Fetching

- Dashboard: Server Component with `async` data fetching
- Conversations: Server Component + `<Suspense>` for streaming
- Chat detail: Client Component with `useEffect` + WebSocket
- Analytics: Server fetch + Client chart library (Recharts)

### Step 4: Middleware

```typescript
// middleware.ts
export function middleware(request: NextRequest) {
  // Auth check
  // Tenant resolution
  // Rate limiting
}
```

## Output

- Complete route tree with Server/Client classification
- Data fetching strategy per route
- Middleware specification
- Streaming boundaries defined
