---
id: ARC-007
title: State Management
status: Draft
version: '1.0'
owner: Robert Hadaway
reviewers:
- Robert Hadaway
depends_on: []
references: []
implemented_by: []
last_updated: '2026-07-04'
---

# ARC-007 — State Management

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

This document defines how runtime state is managed throughout Foundry OS.

Events describe what happened.

State describes what is true right now.

---

# Core Decision

Foundry OS will maintain a shared State Store that represents the current known condition of the platform.

The State Store is the primary read model for user interfaces, APIs, AI agents, plugins, and automation.

---

# Digital Twin State

The State Store acts as a live digital twin of the development environment.

It represents:

- System health
- Worker status
- AI agent status
- Project status
- GitHub workflow status
- Docker and infrastructure status
- Tasks
- Approvals
- Workflow progress
- Repository health
- Deployment state
- Architecture version
- Operational bottlenecks

The goal is not just to store values, but to represent the current operating reality of the software organization.

---

# State vs Events

| Concept | Meaning |
|---|---|
| Events | Historical facts |
| State | Current truth |
| Events answer | What happened? |
| State answers | What is true now? |

Example:

```text
github.workflow.started
github.workflow.completed
github.workflow.failed
```

Those are events.

Current state:

```json
{
  "projects": {
    "foundry": {
      "latestWorkflowStatus": "failed"
    }
  }
}
```

---

# State Flow

```text
Worker / Agent
      |
      v
Event
      |
      v
Event Bus
      |
      v
State Reducer
      |
      v
State Store
      |
      v
REST / WebSocket
      |
      v
UI / CLI / Agents
```

---

# State Store Responsibilities

The State Store is responsible for:

- Holding current platform state
- Serving read requests
- Supporting WebSocket synchronization
- Tracking state version
- Supporting future persistence
- Supporting future replay from events

---

# State Reducers

State is updated through reducers.

Reducers consume events and deterministically update state.

Example:

```text
github.workflow.completed
        |
        v
GitHubWorkflowReducer
        |
        v
projects.foundry.workflows.latest.status = completed
```

Workers do not directly write state.

---

# State Categories

```json
{
  "system": {},
  "workers": {},
  "agents": {},
  "projects": {},
  "tasks": {},
  "approvals": {},
  "infrastructure": {},
  "workflows": {},
  "notifications": {},
  "configuration": {}
}
```

---

# State Access Rules

1. UI reads state.
2. CLI reads state.
3. AI Agents read state through the Orchestrator.
4. Workers emit events.
5. Reducers update state.
6. Orchestrator may create tasks and approval requests.
7. Direct state writes are restricted to platform internals.

---

# API Read Model

The API should expose state-first endpoints:

```text
GET /state
GET /state/system
GET /state/workers
GET /state/agents
GET /state/projects
GET /state/tasks
GET /state/approvals
GET /state/infrastructure
```

---

# State Versioning

Every state update increments a global state version.

Example:

```json
{
  "version": 128,
  "updated_at": "2026-07-04T00:00:00Z",
  "state": {}
}
```

State versions support:

- UI refresh
- WebSocket synchronization
- optimistic updates
- debugging
- future replay validation

---

# Persistence

## MVP

In-memory state.

## Future

Supported persistence options may include:

- SQLite
- Redis
- Couchbase
- Event replay
- Snapshot storage

---

# Security

State must not expose:

- Tokens
- Passwords
- SSH private keys
- Environment files
- Secret values
- Sensitive file contents

State may expose safe references to protected resources.

---

# MVP Requirements

The MVP State Store must support:

- In-memory state
- State categories
- Version tracking
- Updated timestamp
- REST state endpoints
- Event-driven updates
- Future WebSocket compatibility

---

# Future Capabilities

Future versions may support:

- Persistent state snapshots
- State replay from events
- State diffing
- Time-travel debugging
- Distributed state replication
- Digital twin visualization
- State-based AI reasoning