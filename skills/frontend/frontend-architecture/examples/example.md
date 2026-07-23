# Frontend Architecture Example

## Scenario

Enterprise AI Customer Service SaaS with 15 developers, 50+ pages, and complex state management requirements.

## Input

- **Team Size**: 15 developers (3 feature teams)
- **Features**: Conversations, Knowledge Base, Analytics, Settings, User Management
- **State Complexity**: High (real-time updates, forms, server data)
- **Scale**: Large (50+ pages, 200+ components)

## Process

### Folder Structure Decision

**Chosen Pattern**: Feature-based with shared modules

```
src/
├── app/                    # Next.js app router
│   ├── (auth)/            # Auth pages
│   ├── (dashboard)/       # Main dashboard
│   └── (public)/          # Public pages
├── features/              # Feature modules
│   ├── conversations/
│   │   ├── components/    # Conversation components
│   │   ├── hooks/         # Conversation hooks
│   │   ├── services/      # Conversation API
│   │   ├── store/         # Conversation state
│   │   ├── types/         # Conversation types
│   │   └── index.ts       # Barrel export
│   ├── knowledge-base/
│   ├── analytics/
│   ├── settings/
│   └── user-management/
├── shared/                # Shared modules
│   ├── components/        # Reusable UI components
│   │   ├── ui/           # Base UI (Button, Input)
│   │   ├── forms/        # Form components
│   │   └── layouts/      # Layout components
│   ├── hooks/            # Shared hooks
│   ├── utils/            # Utility functions
│   ├── types/            # Shared types
│   └── constants/        # App constants
├── services/             # Global services
│   ├── api/             # API client
│   ├── auth/            # Auth service
│   └── websocket/       # WebSocket service
├── styles/              # Global styles
└── types/               # Global types
```

### State Management Architecture

**Multi-layer Strategy**:

1. **Server State**: React Query
   - All API data
   - Automatic caching
   - Background refetching

2. **Global UI State**: Zustand
   - Theme preferences
   - User settings
   - Global notifications
   - Sidebar state

3. **Local UI State**: useState
   - Form inputs
   - Modal visibility
   - Component-specific state

4. **Form State**: React Hook Form
   - Form validation
   - Field management
   - Submission handling

**State Flow Example**:

```
User Action
    ↓
React Query (API call)
    ↓
Cache Update
    ↓
Component Re-render
    ↓
UI Update
```

### Data Flow Patterns

**Read Flow**:
```
Component → useQuery → API Client → Server
           ← Cache ← Response ←
```

**Write Flow**:
```
User Action → useMutation → API Client → Server
            ← Cache Update ← Response ←
            ← UI Update (onSuccess)
```

**Real-time Flow**:
```
WebSocket Event → Event Handler → State Update → UI Update
```

### Module Boundaries

**Feature Modules**:
- Own their components, hooks, services
- Export only public API via barrel files
- Cannot import from other features directly
- Use shared modules for common functionality

**Shared Modules**:
- Provide reusable components and utilities
- Cannot import from feature modules
- Maintain zero dependencies on features

**Dependency Rules**:
```
Features → Shared (allowed)
Features → Features (not allowed)
Shared → Features (not allowed)
```

## Output

### Architecture Documentation

1. **Folder Structure**: Feature-based with clear boundaries
2. **State Management**: React Query + Zustand + React Hook Form
3. **Data Flow**: Unidirectional with clear patterns
4. **Module System**: Strict boundaries with barrel exports
5. **Scalability**: Supports 3+ feature teams

### Key Benefits

- ✅ Clear feature ownership
- ✅ Easy to onboard developers
- ✅ Scales with team growth
- ✅ Predictable state management
- ✅ Maintainable codebase
- ✅ Testable architecture

### Migration Path

**Phase 1** (Week 1-2): Set up folder structure
**Phase 2** (Week 3-4): Migrate components to features
**Phase 3** (Week 5-6): Implement state management
**Phase 4** (Week 7-8): Refine and document

### Metrics

- **Onboarding Time**: Reduced from 2 weeks to 3 days
- **Feature Development**: 40% faster
- **Bug Rate**: Reduced by 30%
- **Code Duplication**: Reduced by 50%
