# ARC-009 — Worker Architecture

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

This document defines the Worker architecture used throughout Foundry OS.

Workers provide standardized integrations with external systems. They expose capabilities that can be safely invoked by the Orchestrator while remaining isolated from AI reasoning and business workflows.

Workers are deterministic software components. They communicate with external systems but never decide *what* work should be performed.

---

# Design Principles

Workers follow these principles:

1. Single Responsibility
2. Deterministic behavior
3. Capability-based interface
4. Stateless execution
5. Structured responses
6. Event emission
7. Health reporting
8. Security by default
9. Replaceable implementations
10. AI-independent

---

# What is a Worker?

A Worker is an integration adapter that exposes one or more capabilities.

Examples include:

- GitHub Worker
- Docker Worker
- System Worker
- Runner Worker
- Filesystem Worker
- Shell Worker
- Kubernetes Worker
- Grafana Worker
- Couchbase Worker
- Notification Worker

Workers interact with external systems so that AI Agents never need to.

---

# Responsibilities

Workers are responsible for:

- Communicating with external systems
- Exposing named capabilities
- Validating inputs
- Returning structured outputs
- Reporting health
- Publishing events
- Enforcing capability permissions
- Redacting secrets
- Handling retries where appropriate

---

# Workers Do NOT

Workers must never:

- Make business decisions
- Plan workflows
- Call LLMs
- Call other Workers directly
- Store workflow state
- Bypass the Orchestrator
- Ignore approval policies
- Expose secrets

---

# Worker Interface

Every Worker implements a common interface.

```python
class Worker:

    name: str

    version: str

    description: str

    capabilities: list

    def initialize(self):

    def shutdown(self):

    def health_check(self):

    def invoke(self, capability, request):
```

---

# Capability Model

Every Worker exposes one or more capabilities.

A capability is the smallest executable unit offered by a Worker.

Example:

```json
{
  "name": "github.list_workflow_runs",
  "description": "Returns recent GitHub Actions workflow runs.",
  "risk": "low",
  "approval_required": false,
  "input_schema": {},
  "output_schema": {}
}
```

Capabilities become part of the Worker Registry.

---

# Capability Discovery

Workers register their capabilities during startup.

Example:

```
GitHub Worker

↓

Registers

↓

github.list_runs

github.get_pr

github.create_pr

github.merge_pr

↓

Worker Registry
```

The Orchestrator queries the Worker Registry rather than individual Workers.

---

# Worker Registry

The Worker Registry maintains:

- Registered Workers
- Worker versions
- Health status
- Available capabilities
- Capability metadata
- Risk classifications

Example:

```
Worker Registry

GitHub Worker
    list_runs
    create_issue
    create_pr

Docker Worker
    list_containers
    restart_container

System Worker
    cpu_usage
    memory_usage
```

---

# Capability Risk Levels

Each capability has a risk classification.

| Level | Description |
|--------|-------------|
| Low | Read-only operations |
| Medium | Changes development state |
| High | Changes infrastructure or repositories |
| Critical | Destructive or irreversible actions |

Examples

| Capability | Risk |
|------------|------|
| github.list_runs | Low |
| github.create_issue | Medium |
| github.merge_pr | High |
| docker.list_containers | Low |
| docker.restart_container | High |
| shell.execute | Critical |

---

# Approval Policy

Workers declare whether a capability requires approval.

Examples

```
github.list_runs

↓

Approval

No
```

```
github.merge_pr

↓

Approval

Yes
```

Approval policies are enforced by the Orchestrator.

Workers do not decide whether approval is required.

---

# Worker Lifecycle

Workers move through the following states:

```
Registered

↓

Initializing

↓

Healthy

↓

Degraded

↓

Failed

↓

Disabled

↓

Removed
```

---

# Health Model

Each Worker periodically reports health.

Example

```json
{
  "status": "healthy",
  "last_check": "...",
  "latency_ms": 42,
  "error_count": 0,
  "capabilities_available": 12
}
```

---

# Worker Events

Workers emit structured events.

Examples

```
worker.registered

worker.initialized

worker.health.changed

worker.capability.started

worker.capability.completed

worker.capability.failed
```

---

# Error Model

Workers return structured errors.

Example

```json
{
  "success": false,
  "error": {
    "code": "github.timeout",
    "message": "GitHub API timeout."
  }
}
```

Workers never throw implementation-specific exceptions outside their boundary.

---

# Security

Workers must:

- Validate all input
- Redact secrets
- Use least privilege
- Authenticate with external systems
- Log safely
- Emit security events when appropriate

Workers must never expose:

- API tokens
- SSH keys
- Passwords
- Environment variables
- Private credentials

---

# MVP Workers

The MVP includes:

- GitHub Worker
- Docker Worker
- Runner Worker
- System Worker

---

# Future Workers

Future releases may include:

- Filesystem Worker
- Shell Worker
- Kubernetes Worker
- Grafana Worker
- Couchbase Worker
- Redis Worker
- Azure DevOps Worker
- Jira Worker
- Slack Worker
- Email Worker
- Notification Worker
- GitLab Worker
- Terraform Worker

---

# Design Rules

1. Workers are deterministic.
2. Workers expose capabilities.
3. Workers never reason.
4. Workers never call other Workers.
5. Workers never own workflow state.
6. Workers emit events.
7. Workers report health.
8. Workers are replaceable.
9. Workers communicate only through the Orchestrator.
10. Every capability must be discoverable through the Worker Registry.

---

# Future Considerations

Future versions may support:

- Remote Workers
- Worker containers
- Distributed Worker clusters
- Capability load balancing
- Capability versioning
- Worker sandboxing
- Marketplace-installed Workers
- Dynamic capability discovery