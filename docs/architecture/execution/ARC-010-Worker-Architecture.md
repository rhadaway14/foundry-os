# ARC-010 — Worker Architecture

**Status:** Draft  
**Version:** 2.0  
**Owner:** Robert Hadaway

---

# Purpose

This document defines the Worker Architecture used throughout Foundry OS.

Workers are deterministic Capability Providers.

Their purpose is to expose reliable, observable, and secure execution capabilities for external systems while remaining completely independent of AI reasoning.

---

# Vision

Workers are the "device drivers" of Foundry OS.

Just as an operating system uses device drivers to communicate with hardware, Foundry OS uses Workers to communicate with external systems.

Workers never decide *what* should happen.

They only execute approved capabilities.

---

# Worker Definition

A Worker is a deterministic software component that provides one or more capabilities through a Capability Contract.

Workers interact with:

- GitHub
- Docker
- Kubernetes
- Local Filesystems
- Shells
- Couchbase
- Grafana
- Prometheus
- Azure DevOps
- Slack
- Jira

Future Workers can support any external technology.

---

# Worker Characteristics

Every Worker must be:

- Deterministic
- Stateless
- Observable
- Secure
- Replaceable
- Discoverable
- Independently deployable
- Independently testable

---

# Worker Responsibilities

Workers are responsible for:

- Registering capabilities
- Validating requests
- Executing capabilities
- Authenticating to external systems
- Returning structured results
- Publishing events
- Reporting health
- Respecting capability contracts

Workers never:

- Make workflow decisions
- Call LLMs
- Plan work
- Modify shared state directly
- Call other Workers directly

---

# Worker Interface

Every Worker implements a standard interface.

```python
class Worker:

    metadata()

    initialize()

    shutdown()

    register_capabilities()

    health_check()

    invoke()
```

---

# Capability Registration

During startup every Worker registers itself.

```
Worker

↓

Capability Registry

↓

Capabilities Available
```

Example:

```
GitHub Worker

↓

github.list_runs

github.create_pr

github.merge_pr

github.read_issue
```

---

# Worker Metadata

Every Worker publishes:

- Name
- Version
- Description
- Provider Type
- Supported Capabilities
- Health Status
- Dependencies
- Authentication Methods

---

# Worker Health

Health includes:

```yaml
status: Healthy

latency: 18ms

last_check: ...

availability: 100%

registered_capabilities: 14
```

---

# Capability Execution

Capability execution always follows the same lifecycle.

```
Invoke

↓

Validate

↓

Authorize

↓

Execute

↓

Publish Event

↓

Return Result
```

Workers never skip validation.

---

# Security

Workers must:

- Validate every request
- Authenticate every connection
- Never expose secrets
- Enforce least privilege
- Respect approval policies
- Produce audit events

---

# Error Model

Workers return structured errors.

Example

```json
{
  "success": false,
  "error": {
    "code": "github.timeout",
    "message": "GitHub API timeout"
  }
}
```

Implementation exceptions never escape the Worker boundary.

---

# Worker Lifecycle

```
Discovered

↓

Initialized

↓

Healthy

↓

Busy

↓

Degraded

↓

Failed

↓

Disabled

↓

Retired
```

---

# Observability

Workers publish:

Events

Metrics

Logs

Health

Capabilities

The platform should always know:

- What every Worker is doing
- How healthy it is
- Which capabilities are available
- Which capabilities are failing

---

# Built-in Workers

The MVP includes:

- GitHub Worker
- Docker Worker
- System Worker
- Runner Worker

Phase 2 adds:

- Filesystem Worker
- Shell Worker
- Kubernetes Worker
- Couchbase Worker
- Grafana Worker
- Notification Worker

---

# Design Rules

1. Workers are deterministic.
2. Workers provide capabilities.
3. Workers never reason.
4. Workers never plan.
5. Workers never call other Workers.
6. Workers never own shared state.
7. Workers emit events.
8. Workers are replaceable.
9. Workers register capabilities.
10. Workers implement Capability Contracts.
11. Workers are independently testable.
12. Workers may be deployed locally or remotely.

---

# Relationship to Other Architecture Documents

| Document | Relationship |
|----------|--------------|
| ARC-008 | Orchestrator invokes Worker capabilities |
| ARC-009 | Workers register Capability Contracts |
| ARC-011 | AI Agents consume Worker capabilities |
| ARC-006 | Workers emit Events |
| ARC-007 | Worker events update State |
| ARC-012 | Plugins may contribute Workers |