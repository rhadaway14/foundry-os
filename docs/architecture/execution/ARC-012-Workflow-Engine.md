---
id: ARC-012
title: Workflow Engine
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

# ARC-012 — Workflow Engine

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

The Workflow Engine is responsible for executing, coordinating, monitoring, and recovering workflows within Foundry OS.

A workflow is a directed graph of tasks that may involve AI Agents, Workers, platform services, approvals, and human interaction.

The Workflow Engine transforms high-level goals into executable, observable workflows.

---

# Relationship to the Orchestrator

The Orchestrator and Workflow Engine have distinct responsibilities.

The Orchestrator decides:

- Which workflow to start
- Which capabilities are required
- Policy enforcement
- Approval requirements

The Workflow Engine manages:

- Task execution
- Dependency tracking
- Parallel execution
- Retry handling
- Timeouts
- Human approval waits
- Completion
- Rollback
- Recovery

---

# Design Goals

The Workflow Engine shall:

- Execute deterministic workflow graphs
- Support AI-assisted workflows
- Support human approvals
- Support long-running workflows
- Persist execution state
- Recover after restart
- Emit complete execution events

---

# Workflow Model

Every workflow is a Directed Acyclic Graph (DAG).

Nodes represent executable tasks.

Edges represent dependencies.

```
Issue Assigned

↓

Architect Review

↓

Engineer Implementation

├──────────────┐
▼              ▼

Tests      Documentation

└──────┬───────┘

       ▼

Security Review

↓

Approval

↓

Merge

↓

Deploy
```

---

# Task Types

Supported task types include:

- Worker Task
- AI Agent Task
- Human Approval
- Delay / Timer
- Conditional Branch
- Parallel Group
- Notification
- Platform Task

---

# Workflow States

A workflow may be:

- Created
- Ready
- Running
- Waiting
- Blocked
- Completed
- Failed
- Cancelled
- Rolled Back

---

# Task Lifecycle

Every task follows:

```
Created

↓

Queued

↓

Running

↓

Waiting

↓

Completed

↓

Archived
```

Failure paths include:

- Failed
- Cancelled
- Retried
- Timed Out

---

# Dependency Management

Tasks execute only after all dependencies are satisfied.

The engine continuously evaluates the workflow graph to determine runnable tasks.

---

# Parallel Execution

Independent branches may execute concurrently.

The Workflow Engine synchronizes branches before downstream tasks begin.

---

# Human Approval Gates

Approval tasks suspend workflow execution until:

- Approved
- Rejected
- Expired

Approval events are emitted and reflected in the State Store.

---

# Retry Policy

Tasks may define retry behavior.

Supported strategies:

- None
- Immediate
- Fixed Delay
- Exponential Backoff
- Custom Policy

---

# Compensation

Failed workflows may define compensation tasks.

Examples:

- Delete temporary branch
- Close pull request
- Stop container
- Roll back deployment

Compensation is explicit and workflow-defined.

---

# Persistence

Workflow execution state must be recoverable.

Future persistence options include:

- SQLite
- Redis
- Couchbase

---

# Observability

The Workflow Engine emits events such as:

- workflow.created
- workflow.started
- workflow.paused
- workflow.waiting
- workflow.completed
- workflow.failed
- workflow.cancelled

Metrics include:

- Active workflows
- Workflow duration
- Success rate
- Failure rate
- Retry count
- Approval wait time

---

# Design Rules

1. Workflows are DAGs.
2. Tasks are deterministic.
3. Dependencies must be explicit.
4. Parallel execution is supported.
5. Human approval pauses execution.
6. Workflow state is recoverable.
7. Every state transition emits an event.
8. Workflows update the State Store through events.

---

# Relationship to Other Architecture Documents

| Document | Relationship |
|----------|--------------|
| ARC-008 | The Orchestrator starts workflows. |
| ARC-009 | Workflow tasks invoke capabilities. |
| ARC-010 | Worker tasks execute deterministic capabilities. |
| ARC-011 | AI Agent tasks perform reasoning. |
| ARC-006 | Workflow transitions emit events. |
| ARC-007 | Workflow state contributes to the Digital Twin. |