---
id: ARC-003
title: Component Architecture
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

# ARC-003 — Component Architecture

**Status:** Draft  
**Version:** 1.0  
**Owner:** Robert Hadaway

---

# Purpose

This document defines the primary runtime components of Foundry OS, their responsibilities, dependencies, and communication boundaries.

---

# Component Categories

Foundry OS is composed of six major component categories:

1. Core Platform
2. Interfaces
3. Workers
4. AI Agents
5. Plugins
6. Storage and State

---

# Core Platform Components

## API Gateway

Exposes REST and WebSocket APIs to clients.

Responsibilities:

- Request validation
- Authentication
- Authorization
- Routing
- API versioning

Dependencies:

- Orchestrator
- State Store
- Event Bus

---

## Orchestrator

Coordinates work across users, workers, agents, tasks, approvals, and events.

Responsibilities:

- Task routing
- Workflow coordination
- Approval enforcement
- Agent dispatch
- Worker capability selection
- State transitions

Dependencies:

- Event Bus
- State Store
- Task Queue
- Scheduler
- Worker Registry
- Agent Registry

Rule:

The orchestrator coordinates work but does not perform external integrations directly.

---

## Event Bus

Publishes and distributes system events.

Responsibilities:

- Event publishing
- Event history
- Subscriber notification
- WebSocket fanout

Dependencies:

- State Store
- WebSocket Gateway

---

## State Store

Maintains current platform state.

Responsibilities:

- Worker state
- Agent state
- Task state
- Approval state
- Project state
- Runtime configuration

---

## Task Queue

## Approval Queue

Stores actions requiring human approval.

Responsibilities:

- Approval request creation
- Approval status tracking
- Approval expiration
- Approval audit history
- Risk classification

Examples:

- Merge pull request
- Deploy to staging
- Restart production service
- Run destructive shell command

---

## Scheduler

Triggers scheduled or recurring work.

Responsibilities:

- Scheduled checks
- Periodic worker polling
- Retry scheduling
- Delayed task execution

---

# Interface Components

## React Dashboard

Primary web UI.

Responsibilities:

- Display state
- Display events
- Display tasks
- Display approvals
- Send user commands

Rule:

The UI never talks directly to workers or agents.

---

## CLI

Command-line control interface.

Responsibilities:

- Local administration
- Debugging
- Worker inspection
- Task submission

---

## Mobile Client

Future mobile-optimized interface.

Responsibilities:

- Approvals
- Notifications
- Task monitoring
- Lightweight command submission

---

# Worker Components

Workers expose capabilities for external systems.

## GitHub Worker

Capabilities:

- List repositories
- List workflow runs
- Get workflow logs
- Create issues
- Comment on issues
- Create pull requests
- Read pull requests
- Merge pull requests

---

## Docker Worker

Capabilities:

- List containers
- Inspect containers
- Stream logs
- Restart containers
- Stop containers
- Start containers

---

## System Worker

Capabilities:

- CPU status
- Memory status
- Disk status
- Process status
- Service status

---

## Runner Worker

Capabilities:

- Check GitHub runner status
- Tail runner logs
- Restart runner service
- Report busy/idle state

---

## Filesystem Worker

Capabilities:

- Read files
- Write files
- Search files
- List directories
- Watch files

---

## Shell Worker

Capabilities:

- Execute approved commands
- Stream command output
- Return exit codes

High-risk commands require approval.

---

# AI Agent Components

AI Agents reason about work and use worker capabilities through the orchestrator.

## Engineer Agent

Responsibilities:

- Implement features
- Fix bugs
- Write tests
- Open pull requests

---

## Architect Agent

Responsibilities:

- Review designs
- Maintain architecture docs
- Validate ADR alignment
- Review pull requests for architectural fit

---

## Test Agent

Responsibilities:

- Run tests
- Interpret failures
- Recommend fixes
- Validate acceptance criteria

---

## Documentation Agent

Responsibilities:

- Generate docs
- Update changelogs
- Produce implementation summaries
- Maintain user guides

---

## Release Agent

Responsibilities:

- Prepare releases
- Validate release readiness
- Generate release notes
- Request deployment approval

---

# Registries

## Worker Registry

Stores available workers and their capabilities.

## Agent Registry

Stores available AI agents and their roles.

## Plugin Registry

Stores installed plugins and metadata.

---

# Communication Rules

1. UI calls API Gateway.
2. API Gateway calls Orchestrator.
3. Orchestrator calls agents and workers.
4. AI Agents request capabilities through the Orchestrator.
5. Workers communicate with external systems.
6. Events are emitted for all meaningful state changes.
7. State Store records current system state.
8. WebSocket Gateway streams events to clients.

---

# Component Lifecycle

Each component has a lifecycle:

1. Registered
2. Initialized
3. Healthy
4. Degraded
5. Failed
6. Disabled
7. Removed

---

# MVP Components

The MVP includes:

- API Gateway
- Orchestrator
- Event Bus
- State Store
- GitHub Worker
- Docker Worker
- System Worker
- Runner Worker
- React Dashboard

The MVP excludes:

- Full plugin loading
- Multi-agent autonomy
- Multi-user permissions
- Cloud deployment
- Mobile app