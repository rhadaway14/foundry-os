# ARC-009 — Capability Architecture

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

This document defines the Capability Architecture for Foundry OS.

Capabilities are the fundamental unit of execution within the platform.

Rather than invoking specific Workers or AI Agents directly, the Orchestrator requests capabilities from the Capability Registry. The registry resolves the most appropriate provider based on contracts, health, permissions, and policy.

Capabilities form the stable execution interface of Foundry OS.

---

# Vision

Everything executable within Foundry OS is represented as a capability.

Examples include:

- Reading GitHub workflow runs
- Restarting a Docker container
- Creating a Pull Request
- Reviewing architecture
- Writing documentation
- Executing tests
- Sending notifications
- Requesting approvals
- Deploying software

Workers, AI Agents, Platform Services, and Plugins all provide capabilities through a common interface.

---

# Architectural Principles

Capabilities are:

- Discoverable
- Self-describing
- Provider-independent
- Versioned
- Secure
- Composable
- Observable
- Replaceable
- Testable
- Contract-driven

---

# High-Level Architecture

```
                          Users
                            │
                            ▼
                     API Gateway
                            │
                            ▼
                      Orchestrator
                            │
                            ▼
                  Capability Registry
                            │
        ┌──────────────┬──────────────┬──────────────┐
        ▼              ▼              ▼              ▼

     Workers       AI Agents     Platform      Plugins
```

The Orchestrator never calls implementations directly.

It requests capabilities.

---

# Capability Registry

The Capability Registry is the authoritative catalog of executable functionality.

Responsibilities:

- Provider registration
- Capability discovery
- Metadata storage
- Version tracking
- Health awareness
- Approval metadata
- Risk metadata
- Contract validation

---

# Provider Types

Foundry OS supports multiple provider types.

## Workers

Examples

- GitHub Worker
- Docker Worker
- System Worker
- Runner Worker
- Filesystem Worker

---

## AI Agents

Examples

- Engineer Agent
- Architect Agent
- Documentation Agent
- Testing Agent
- Release Agent

---

## Platform Services

Examples

- Approval Service
- Notification Service
- Scheduler
- Workflow Engine

---

## Plugins

Future extensions that register additional capabilities.

---

# Capability Definition

A capability represents a single executable action.

Example

```yaml
name: github.create_pull_request
provider: github-worker
provider_type: worker
version: 1.0.0
description: Create a GitHub Pull Request.
```

Capabilities should remain small, deterministic, and reusable.

---

# Capability Contracts

Every capability must be defined by a machine-readable contract.

Capability Contracts provide:

- Validation
- SDK generation
- Documentation generation
- Plugin compatibility
- AI planning
- Approval enforcement
- Testing

A capability cannot be registered without a valid contract.

---

# Contract Structure

Every Capability Contract includes:

| Field | Description |
|--------|-------------|
| name | Unique capability identifier |
| version | Semantic version |
| provider | Provider name |
| provider_type | Worker, Agent, Platform, Plugin |
| description | Human-readable description |
| input_schema | Request schema |
| output_schema | Response schema |
| risk | Risk classification |
| approval_required | Approval requirement |
| permissions | Required permissions |
| idempotent | Safe to repeat |
| side_effects | Expected changes |
| timeout | Maximum execution time |
| retry_policy | Retry behavior |
| error_model | Structured errors |

---

# Example Capability Contract

```yaml
name: github.create_pull_request

version: 1.0.0

provider: github-worker

provider_type: worker

description: Create a GitHub Pull Request.

risk: medium

approval_required: false

permissions:
  - github.pull_requests.write

idempotent: false

side_effects:
  - github.pull_request.created

timeout: 30s

retry_policy: exponential

input_schema:
  type: object
  required:
    - repository
    - source_branch
    - target_branch
    - title

output_schema:
  type: object
  properties:
    pull_request_number:
      type: integer

    url:
      type: string

error_model:
  - github.authentication_failed
  - github.validation_failed
  - github.rate_limited
```

---

# Capability Lifecycle

Capabilities move through the following lifecycle:

```
Discovered

↓

Validated

↓

Registered

↓

Available

↓

Executing

↓

Completed

↓

Deprecated

↓

Retired
```

---

# Capability Discovery

The Orchestrator requests capabilities by name.

Example

```
Need:

github.create_pull_request

↓

Capability Registry

↓

GitHub Worker

↓

Invoke
```

The caller never knows who implements the capability.

---

# Capability Resolution

The Capability Registry resolves providers using:

1. Capability name
2. Version compatibility
3. Provider health
4. Required permissions
5. Risk policy
6. Approval policy
7. Configuration rules

Future versions may consider:

- Cost
- Performance
- Geographic location
- Preferred providers
- AI model selection

---

# Capability Composition

Complex workflows are composed from independent capabilities.

Example

```
engineer.complete_feature

↓

github.read_issue

↓

filesystem.modify_files

↓

shell.run_tests

↓

documentation.update

↓

github.create_pull_request
```

Each capability remains independent and reusable.

---

# Versioning

Capabilities use Semantic Versioning.

```
1.0.0

↓

1.1.0

↓

2.0.0
```

Breaking changes require a major version.

Multiple versions may coexist.

---

# Security

Capabilities declare:

- Risk level
- Required permissions
- Approval requirement
- Authentication requirements
- Audit requirements

The Orchestrator enforces these policies before execution.

---

# Observability

Every invocation emits events.

Examples:

```
capability.registered

capability.invoked

capability.completed

capability.failed

capability.timeout
```

Metrics include:

- Invocation count
- Success rate
- Failure rate
- Average latency
- P95 latency
- Retry count

---

# State Integration

Capability execution updates the State Store through Events.

Workers never modify state directly.

Capabilities produce Events.

Reducers update State.

State becomes the authoritative digital twin.

---

# Design Rules

1. Everything executable is a capability.
2. Capabilities are provider-independent.
3. Providers may expose many capabilities.
4. Providers may be replaced without affecting callers.
5. Capabilities are discoverable.
6. Capabilities are versioned.
7. Capabilities emit events.
8. Capability execution updates shared state.
9. Capabilities declare risk.
10. Capabilities declare approval requirements.
11. Every capability must have a machine-readable contract.
12. Invalid contracts prevent registration.
13. Capability names are globally unique.
14. Capability contracts are immutable after registration.
15. Providers must pass contract validation before becoming available.

---

# MVP

The MVP Capability Registry supports:

- Static registration
- Worker capabilities
- AI Agent capabilities
- Metadata lookup
- Capability discovery
- Contract validation
- Risk metadata
- Approval metadata

---

# Future

Future releases may support:

- Dynamic plugin loading
- Distributed Capability Registry
- Marketplace providers
- Remote capability execution
- Capability dependency graphs
- AI-assisted provider selection
- Cost-aware routing
- Capability sandboxing
- Multi-cluster execution
- Automatic SDK generation from contracts

---

# Relationship to Other Architecture Documents

| Document | Relationship |
|----------|--------------|
| ARC-008 — Orchestration Engine | The Orchestrator discovers and invokes capabilities. |
| ARC-010 — Worker Architecture | Workers provide capabilities. |
| ARC-011 — AI Agent Architecture | AI Agents provide reasoning capabilities. |
| ARC-006 — Event Model | Capability execution emits events. |
| ARC-007 — State Management | Capability events update the State Store. |
| ARC-012 — Plugin Architecture | Plugins register additional capability providers. |