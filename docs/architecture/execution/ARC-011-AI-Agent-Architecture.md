---
id: ARC-011
title: Ai Agent Architecture
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

# ARC-011 — AI Agent Architecture

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

This document defines the AI Agent Architecture for Foundry OS.

AI Agents are **Reasoning Capability Providers** responsible for planning, analysis, decision support, and workflow execution.

Unlike Workers, AI Agents reason about *what should happen*. They do not directly interact with external systems. Instead, they request capabilities through the Orchestrator.

---

# Vision

AI Agents are specialized experts collaborating to accomplish software engineering work.

Each Agent has:

- A defined role
- A set of capabilities
- A reasoning strategy
- Access to shared context
- Access to the platform state
- Access to deterministic Worker capabilities

Agents never bypass platform controls.

---

# Architectural Principles

AI Agents are:

- Specialized
- Replaceable
- Observable
- Collaborative
- Context-aware
- Capability-driven
- Policy-aware
- Human-supervised

---

# High-Level Architecture

```
                    User
                      │
                      ▼
                Orchestrator
                      │
          Task Assignment
                      │
                      ▼
               AI Agent
                      │
          Capability Requests
                      │
                      ▼
            Capability Registry
                      │
          Worker Capabilities
                      │
                      ▼
             External Systems
```

AI Agents never communicate directly with GitHub, Docker, Kubernetes, or any external service.

---

# Agent Responsibilities

AI Agents are responsible for:

- Planning work
- Breaking work into tasks
- Selecting capabilities
- Interpreting results
- Updating workflow status
- Producing recommendations
- Collaborating with other agents
- Producing human-readable outputs

---

# AI Agents Never

AI Agents must never:

- Execute shell commands directly
- Call GitHub APIs directly
- Modify shared state directly
- Bypass approval policies
- Access secrets directly
- Ignore capability contracts

---

# Agent Interface

Every AI Agent implements:

```python
class Agent:

    metadata()

    initialize()

    shutdown()

    register_capabilities()

    plan()

    execute()

    summarize()

    health_check()
```

---

# Agent Metadata

Each Agent publishes:

- Name
- Version
- Role
- Supported capabilities
- Supported models
- Required context
- Maximum context size
- Health status

---

# Reasoning Lifecycle

```
Receive Task

↓

Gather Context

↓

Read State

↓

Develop Plan

↓

Request Capabilities

↓

Interpret Results

↓

Update Workflow

↓

Summarize Outcome
```

---

# Context Model

AI Agents operate using multiple context sources.

## Platform State

Current system status.

## Task Context

Task description, requirements, acceptance criteria.

## Project Context

Repository metadata, architecture documents, coding standards.

## Historical Context

Previous workflows, approvals, lessons learned.

## User Context

Preferences, constraints, and objectives.

---

# Planning

Agents produce explicit execution plans.

Example

```
Task

↓

Plan

↓

Required Capabilities

↓

Execution

↓

Verification

↓

Summary
```

Plans should be inspectable by humans.

---

# Collaboration

Agents collaborate through the Orchestrator.

Example

```
Architect Agent

↓

Engineer Agent

↓

Testing Agent

↓

Documentation Agent

↓

Release Agent
```

Agents never invoke one another directly.

---

# Capability Registration

Agents register reasoning capabilities.

Example

```
engineer.implement_feature

engineer.fix_bug

architect.review_design

documentation.write

tester.execute_plan

release.prepare
```

These capabilities are published to the Capability Registry.

---

# Memory Model

Agents maintain three forms of memory.

## Working Memory

Current reasoning session.

## Shared Memory

Platform State and Workflow State.

## Persistent Memory

Future enhancement.

May include:

- Lessons learned
- Previous solutions
- Architecture decisions
- Repository knowledge

---

# Human Supervision

Every Agent supports:

- Pause
- Resume
- Cancel
- Approval requests
- Explain reasoning
- Generate execution plans

Humans remain in control.

---

# Observability

Agents emit events.

Examples

```
agent.started

agent.planning

agent.waiting

agent.completed

agent.failed
```

Metrics include:

- Tasks completed
- Success rate
- Average planning time
- Average execution time
- Token usage
- Model latency

---

# Security

Agents:

- Never store secrets
- Never expose credentials
- Operate through Capability Contracts
- Respect approval policies
- Respect role-based permissions
- Produce audit events

---

# Built-in Agents

The MVP includes:

- Engineer Agent
- Architect Agent
- Documentation Agent

Future releases add:

- Testing Agent
- Release Agent
- Security Agent
- DevOps Agent
- Data Engineer Agent
- Research Agent
- Product Manager Agent

---

# Design Rules

1. Agents reason.
2. Workers execute.
3. Agents consume capabilities.
4. Agents never bypass the Orchestrator.
5. Agents collaborate through workflows.
6. Plans should be explainable.
7. Human approval remains authoritative.
8. Agents are replaceable.
9. Agents register reasoning capabilities.
10. Agent execution is observable.

---

# Relationship to Other Architecture Documents

| Document | Relationship |
|----------|--------------|
| ARC-008 | Orchestrator assigns work to Agents |
| ARC-009 | Agents register reasoning capabilities |
| ARC-010 | Agents consume Worker capabilities |
| ARC-006 | Agents emit Events |
| ARC-007 | Agent events update shared State |
| ARC-012 | Plugins may contribute additional Agents |