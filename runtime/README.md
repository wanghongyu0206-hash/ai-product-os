# AI Product OS Runtime Layer

The Runtime Layer provides the core infrastructure for agent discovery, skill loading, workflow orchestration, and multi-agent handoff in AI Product OS.

## Architecture

The Runtime Layer consists of four key components:

### 1. Agent Discovery

Agents are registered in `agent-registry.yaml` and can be dynamically loaded based on task requirements. Each agent definition includes:

- **Identity**: Name and description
- **Capabilities**: Skills the agent can use
- **Workflows**: Available workflows the agent participates in
- **Handoff**: Next agent in the pipeline

The runtime discovers agents by scanning the registry and loading agent configurations from `agents/<name>/` directories.

### 2. Skill Loading

Skills are registered in `skill-registry.yaml` and loaded on-demand when agents need specific capabilities. Skills are organized by category:

- **Product**: PRD, user stories, requirements
- **UX**: Information architecture, user flow, wireframes
- **UI**: Design systems, components, layout
- **Frontend**: React, Next.js, Tailwind, performance
- **Backend**: API design, database, deployment

The runtime matches agent skill requirements against the registry and loads the corresponding `SKILL.md` files.

### 3. Workflow Routing

Workflows are defined in `workflow-registry.yaml` and describe the sequence of steps and agents involved in completing a task. Common workflows include:

- **Product Design**: Idea → PRD → UX → UI
- **Design to Code**: UI spec → Frontend → Backend → QA
- **Quality Review**: Any output → QA agent → Quality report

The runtime orchestrates workflow execution, manages state, and ensures proper sequencing.

### 4. Multi-Agent Handoff

Agents communicate through structured handoff protocols defined in `router.yaml`. When an agent completes its work, it produces output that becomes input for the next agent:

- **Product Manager** → Architect, UX Designer
- **Architect** → Backend, Frontend
- **UX Designer** → UI Designer
- **UI Designer** → Frontend
- **Frontend/Backend** → QA

The runtime routes outputs to the correct downstream agent and ensures data compatibility.

## Configuration Files

- `agent-registry.yaml` — Agent definitions and capabilities
- `skill-registry.yaml` — Skill catalog and metadata
- `workflow-registry.yaml` — Workflow definitions
- `router.yaml` — Request routing rules

## Usage

The Runtime Layer is invoked when a user submits a task. The system:

1. Routes the request to the appropriate agent via `router.yaml`
2. Loads the agent configuration from `agent-registry.yaml`
3. Identifies required skills from `skill-registry.yaml`
4. Executes the workflow defined in `workflow-registry.yaml`
5. Manages handoff between agents until completion

## Example Flow

```
User Request: "Design a customer service dashboard"
  ↓
Router: product_request → product-manager
  ↓
Workflow: product-design
  ↓
Agent Chain: product-manager → ux-designer → ui-designer → frontend → qa
  ↓
Output: Complete dashboard implementation
```
