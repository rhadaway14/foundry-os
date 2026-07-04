# ARC-006 — Event Model

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

This document defines the event architecture used throughout Foundry OS.

Events are the primary communication mechanism between the Orchestrator, Workers, AI Agents, State Store, UI clients, plugins, and future distributed services.

Every significant action within Foundry OS should generate one or more events.

---

# Goals

The event system exists to provide:

- Loose coupling between components
- Complete observability
- Auditability
- Live UI updates
- Workflow coordination
- Plugin integration
- Future distributed execution
- Historical replay (future)

---

# Design Principles

The Foundry OS event system follows these principles:

1. Every meaningful action emits an event.
2. Events describe facts, not commands.
3. Events are immutable.
4. Events use a common schema.
5. Events are timestamped.
6. Events have a source.
7. Events may update shared state.
8. Events may be streamed to clients.
9. Events may be persisted.
10. Events must never contain secrets.

---

# Event Lifecycle

```text
Worker / Agent
       │
       ▼
Publish Event
       │
       ▼
Event Bus
       │
 ┌─────┼───────────────┐
 ▼     ▼               ▼
State  WebSocket    Audit Log
Store  Gateway      (future)
       │
       ▼
 React UI
```

Events are generated once and may have multiple subscribers.

---

# Event Envelope

Every event follows the same structure.

```json
{
  "id": "evt_01J123ABCDEF",
  "type": "github.workflow.completed",
  "source": "github-worker",
  "severity": "info",
  "timestamp": "2026-07-04T19:42:00Z",
  "correlation_id": "task_9842",
  "actor": {
    "type": "worker",
    "id": "github-worker"
  },
  "payload": {}
}
```

---

# Event Fields

| Field | Description |
|--------|-------------|
| id | Globally unique event identifier |
| type | Dot-delimited event name |
| source | Component emitting the event |
| severity | debug, info, warning, error, critical |
| timestamp | UTC ISO-8601 timestamp |
| correlation_id | Groups related events together |
| actor | Human, worker, AI agent, scheduler, or system |
| payload | Event-specific information |

---

# Event Naming Convention

Event names use:

```
domain.resource.action
```

Examples:

```
github.workflow.started

github.workflow.completed

github.workflow.failed

docker.container.started

docker.container.stopped

runner.service.offline

approval.requested

approval.approved

task.created

task.completed

task.failed

agent.started

agent.waiting

system.health.changed
```

---

# Severity Levels

| Level | Meaning |
|--------|---------|
| debug | Diagnostic information |
| info | Normal operation |
| warning | Unexpected but recoverable |
| error | Failed operation |
| critical | Immediate attention required |

---

# Correlation IDs

A Correlation ID links multiple events belonging to the same workflow.

Example:

```
Task Created

↓

GitHub Issue Read

↓

Claude Agent Started

↓

Filesystem Modified

↓

Tests Passed

↓

Pull Request Created
```

All six events share:

```
correlation_id = task_9842
```

This allows complete workflow reconstruction.

---

# Event Categories

## System Events

```
system.started

system.stopped

system.health.changed

system.resource.warning

system.resource.critical
```

---

## Worker Events

```
worker.registered

worker.initialized

worker.health.changed

worker.capability.invoked

worker.capability.completed

worker.capability.failed
```

---

## AI Agent Events

```
agent.registered

agent.started

agent.task.accepted

agent.task.completed

agent.task.failed

agent.waiting
```

---

## Task Events

```
task.created

task.assigned

task.started

task.completed

task.failed

task.cancelled
```

---

## Approval Events

```
approval.requested

approval.approved

approval.rejected

approval.expired
```

---

## GitHub Events

```
github.workflow.started

github.workflow.completed

github.workflow.failed

github.pull_request.opened

github.pull_request.merged

github.issue.created
```

---

## Docker Events

```
docker.container.started

docker.container.stopped

docker.container.restarted

docker.container.failed
```

---

## Infrastructure Events

```
runner.online

runner.offline

runner.busy

runner.idle

kubernetes.pod.started

grafana.alert.created
```

---

# Event Consumers

Events may be consumed by:

- Orchestrator
- State Store
- WebSocket Gateway
- React Dashboard
- Mobile Client
- CLI
- Notification Service
- Audit Service
- Plugins
- Future AI Agents

A single event may have many consumers.

---

# Event Storage

### MVP

Events are stored in memory.

Capabilities:

- Latest events
- Event filtering
- REST retrieval

---

### Future

Persistent event storage will support:

- Querying
- Filtering
- Replay
- Export
- Retention policies
- Distributed event streaming
- Analytics

---

# Security

Events must never contain:

- API tokens
- Passwords
- SSH private keys
- Session cookies
- OAuth tokens
- Environment files
- Sensitive file contents

Instead, events should contain references to protected resources.

---

# Performance

The event system should support:

- Thousands of events per minute
- Multiple subscribers
- Low-latency WebSocket streaming
- Non-blocking publication

Workers should never wait for subscribers to complete.

---

# Event Versioning

Future event schema changes must be backward compatible.

Breaking changes require:

- New event version
- Migration strategy
- Updated SDK

---

# MVP Scope

The MVP event system includes:

- In-memory Event Bus
- Standard Event Envelope
- Event publication
- Event subscription
- Recent event retrieval
- REST endpoint
- Correlation IDs
- WebSocket compatibility

The MVP excludes:

- Persistent storage
- Distributed messaging
- Event replay
- Kafka integration
- RabbitMQ integration
- Cloud event replication

---

# Future Considerations

Future versions may support:

- Event sourcing
- CQRS
- Distributed Event Bus
- Event replay
- Time-travel debugging
- AI event reasoning
- Cross-node synchronization
- Cloud-native messaging