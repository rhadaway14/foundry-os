---
id: ARC-020
title: Runtime Execution Model
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

# ARC-020 — Runtime Execution Model

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

This document describes the complete runtime behavior of Foundry OS.

It explains how a request flows through the platform from the moment it is received until the resulting state is reflected in the Digital Twin and presented to users.

While previous architecture documents describe individual subsystems, this document describes **how those subsystems work together**.

---

# Runtime Philosophy

Foundry OS is an event-driven, capability-oriented operating platform.

Execution follows four guiding principles:

1. Intent drives execution.
2. Capabilities perform work.
3. Events describe what happened.
4. State represents current truth.

Every runtime interaction follows this model.

---

# Runtime Layers

```
Presentation Layer

    Browser
    Mobile
    CLI
    API

            │
            ▼

API Layer

    REST
    WebSocket

            │
            ▼

Control Layer

    Orchestrator
    Workflow Engine
    Approval Queue

            │
            ▼

Execution Layer

    Capability Registry

            │
      ┌─────┴───────────┐
      ▼                 ▼

 Workers          AI Agents

            │
            ▼

Infrastructure Layer

GitHub
Docker
Filesystem
Runner
Kubernetes
Grafana
Couchbase
Azure DevOps
Slack

            │
            ▼

Observability Layer

Event Bus

↓

State Reducers

↓

State Store

↓

Digital Twin
```

---

# Runtime Components

## Presentation Layer

Responsible for user interaction.

Examples

- React Dashboard
- Mobile Client
- CLI
- Future API Clients

The Presentation Layer never executes work directly.

---

## API Layer

Responsible for:

- Authentication
- Authorization
- Input validation
- Routing
- WebSocket connections

The API Layer translates user requests into platform requests.

---

## Control Layer

The Control Layer determines **what work should happen**.

Components

- Orchestrator
- Workflow Engine
- Approval Queue

This layer owns workflow execution.

---

## Execution Layer

The Execution Layer performs work.

Components

- Capability Registry
- Workers
- AI Agents

Execution occurs through Capability Contracts.

---

## Observability Layer

The Observability Layer records runtime activity.

Components

- Event Bus
- State Reducers
- State Store
- Digital Twin

Nothing bypasses this layer.

---

# Runtime Request Flow

```
User Request

↓

REST API

↓

Authentication

↓

Authorization

↓

Orchestrator

↓

Workflow Engine

↓

Capability Registry

↓

Capability Provider

↓

Worker / AI Agent

↓

Capability Result

↓

Event Bus

↓

Reducers

↓

State Store

↓

Digital Twin

↓

WebSocket

↓

User Interface
```

---

# Detailed Execution Example

## Scenario

User requests:

> "Implement GitHub Issue #42"

---

### Step 1

API Gateway receives request.

Request is authenticated.

Permissions validated.

---

### Step 2

The Orchestrator determines:

- Workflow type
- Required approvals
- Required capabilities

---

### Step 3

Workflow Engine constructs:

```
Read Issue

↓

Architect Review

↓

Engineer Implementation

├──────────────┐
▼              ▼

Tests      Documentation

└──────┬───────┘

       ▼

Approval

↓

Create Pull Request
```

---

### Step 4

Workflow tasks request capabilities.

Examples

```
github.read_issue

↓

GitHub Worker
```

```
engineer.implement_feature

↓

Engineer Agent
```

---

### Step 5

Providers execute capabilities.

Workers perform deterministic work.

Agents perform reasoning.

---

### Step 6

Execution produces events.

Examples

```
workflow.started

capability.invoked

agent.started

worker.completed

approval.requested

workflow.completed
```

---

### Step 7

Reducers consume events.

Reducers update platform state.

---

### Step 8

Digital Twin reflects new reality.

Examples

```
Workflow Status

Running

↓

Completed
```

```
GitHub Runner

Busy

↓

Idle
```

```
Engineer Agent

Working

↓

Waiting
```

---

### Step 9

WebSocket broadcasts state changes.

React updates immediately.

---

# Capability Execution

Every capability follows the same execution model.

```
Resolve

↓

Validate Contract

↓

Authorize

↓

Execute

↓

Emit Events

↓

Return Result

↓

Update State
```

---

# Workflow Execution

Workflow execution is graph-based.

Supported node types include:

- Worker Task
- AI Agent Task
- Human Approval
- Conditional Branch
- Parallel Branch
- Delay
- Retry
- Notification

---

# Human Approval Model

Execution pauses whenever a capability requires approval.

```
Workflow

↓

Approval Requested

↓

Paused

↓

Approved

↓

Continue
```

Rejected approvals terminate or compensate the workflow.

---

# Failure Handling

Failures are first-class runtime events.

Examples

- Capability timeout
- Provider unavailable
- Contract validation failure
- Authentication failure
- Approval rejection
- External API failure

The Workflow Engine determines recovery.

Recovery options include:

- Retry
- Wait
- Escalate
- Compensate
- Abort

---

# State Synchronization

Workers never modify state.

Agents never modify state.

Execution produces events.

Reducers consume events.

Reducers modify state.

This guarantees deterministic state updates.

---

# Digital Twin

The Digital Twin represents the current operational reality of Foundry OS.

It contains:

- System health
- Running workflows
- Active tasks
- Worker health
- Agent health
- Repository status
- Infrastructure
- Approval queue
- Notifications

Every UI consumes the Digital Twin.

---

# Runtime Security

Security is enforced at every layer.

Checks include:

- Authentication
- Authorization
- Capability permissions
- Approval policies
- Contract validation
- Secret redaction
- Audit logging

No provider bypasses platform security.

---

# Runtime Design Rules

1. Intent enters through the API Layer.
2. The Orchestrator determines **what** should happen.
3. The Workflow Engine determines **how** execution proceeds.
4. The Capability Registry determines **who** performs work.
5. Workers provide deterministic capabilities.
6. AI Agents provide reasoning capabilities.
7. Events record every meaningful action.
8. Reducers update platform state.
9. The State Store is the authoritative current view.
10. The Digital Twin is the authoritative runtime representation.
11. User interfaces consume state rather than querying providers.
12. High-risk capabilities require approval.
13. Providers are replaceable.
14. Contracts are validated before execution.
15. Runtime behavior must be fully observable.

---

# Relationship to Other Architecture Documents

| Document | Relationship |
|----------|--------------|
| ARC-002 | Defines the overall system architecture |
| ARC-006 | Defines runtime events |
| ARC-007 | Defines state management and Digital Twin |
| ARC-008 | Defines the Orchestrator |
| ARC-009 | Defines Capability Architecture |
| ARC-010 | Defines Worker providers |
| ARC-011 | Defines AI Agent providers |
| ARC-012 | Defines Workflow Engine |
| ARC-013 | Defines Plugin Architecture |

---

# Future Evolution

Future runtime capabilities may include:

- Distributed execution
- Remote capability providers
- Multi-cluster orchestration
- Policy-driven scheduling
- Autonomous workflow optimization
- Event replay
- Time-travel debugging
- Multi-user collaboration
- Federated Digital Twins
- Marketplace-installed providers