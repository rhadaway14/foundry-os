---
id: ARC-002
title: System Architecture
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

# ARC-002 — System Architecture

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

This document defines the high-level architecture of Foundry OS.

It identifies the major subsystems, their responsibilities, and the communication boundaries between them.

Implementation details are intentionally omitted. Those belong in lower-level architecture documents.

---

# Architectural Principles

Foundry OS follows these principles:

1. Local-first
2. Event-driven
3. API-first
4. Worker abstraction
5. AI-agnostic
6. Replaceable components
7. Human approval before high-risk actions
8. Stateless interfaces
9. Shared system state
10. Plugin-based extensibility

---

# High-Level Architecture

```
                          Users
                             │
      ┌──────────────────────┼──────────────────────┐
      │                      │                      │
      ▼                      ▼                      ▼
  Web UI                  Mobile UI             CLI Client
                             │
─────────────────────────────┼────────────────────────────
                             ▼
                       API Gateway
                             │
─────────────────────────────┼────────────────────────────
                             ▼
                      Orchestrator
                             │
      ┌──────────────┬────────┴────────┬──────────────┐
      ▼              ▼                 ▼              ▼
 Event Bus      State Store      Task Queue      Scheduler
      │
─────────────────────────────┼────────────────────────────
      │
      ▼
 Workers
      │
─────────────────────────────┼────────────────────────────
      │
 GitHub
 Docker
 Kubernetes
 SSH
 Grafana
 Couchbase
 Filesystem
 Claude
 OpenAI
 Local System

─────────────────────────────┼────────────────────────────
      │
      ▼
 AI Agents

 Engineer
 Architect
 Tester
 Documentation
 Release
 Research
 Planner

─────────────────────────────┼────────────────────────────
      │
      ▼
 External Systems
```

---

# Major Subsystems

## User Interfaces

Provides interaction with the platform.

Examples

- React Dashboard
- Mobile Client
- CLI
- REST Clients

---

## API Gateway

Single entry point into the platform.

Responsibilities

- Authentication
- Authorization
- Request validation
- Routing
- API versioning

---

## Orchestrator

The central decision engine.

Responsibilities

- Coordinate workflows
- Dispatch work
- Schedule execution
- Enforce approval policies
- Maintain workflow state

The orchestrator never performs integrations directly.

---

## Event Bus

Provides asynchronous communication.

Every subsystem publishes events.

Examples

- WorkflowStarted
- WorkflowCompleted
- WorkerFailed
- ApprovalRequested

No component communicates directly when an event can be used.

---

## Shared State Store

Provides a single source of truth.

Stores

- Worker status
- Agent status
- Running workflows
- Active approvals
- Configuration
- Metrics

---

## Task Queue

Represents work to be performed.

Tasks may originate from

- Users
- Workers
- AI Agents
- Schedulers

---

## Workers

Workers communicate with external systems.

Workers never perform reasoning.

Workers expose capabilities.

Examples

GitHubWorker

- Create PR
- Merge PR
- Read Actions
- Create Issue

DockerWorker

- List containers
- Restart container
- Stream logs

SSHWorker

- Execute commands
- Read files
- Tail logs

---

## AI Agents

AI Agents reason about work.

Examples

EngineerAgent

Receives

"Implement Feature 42"

Uses

GitHubWorker

FilesystemWorker

TestingWorker

Returns

Pull Request

---

## Plugin System

Allows new workers and agents to be added without modifying the core.

---

# Architectural Rules

1. Workers never call other workers.
2. AI Agents never communicate directly with external systems.
3. All external communication flows through workers.
4. Every important action generates an event.
5. Shared state is the authoritative system state.
6. UI components never communicate with workers directly.
7. The orchestrator owns workflow execution.
8. Plugins must register capabilities before use.

---

# Future Expansion

Future versions may add

- Multiple orchestrators
- Distributed workers
- Cloud synchronization
- Multi-user support
- Agent marketplaces
- Distributed event streaming