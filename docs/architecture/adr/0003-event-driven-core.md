---
id: ADR-0003
title: Event Driven Core
status: Accepted
version: '1.0'
owner: Robert Hadaway
reviewers:
- Robert Hadaway
depends_on: []
references: []
implemented_by: []
last_updated: '2026-07-04'
---

# ADR-0003 — Event-Driven Core

**Status:** Accepted  
**Date:** 2026-07-04  
**Owner:** Robert Hadaway

---

## Context

Foundry OS coordinates users, workers, AI agents, infrastructure, CI/CD systems, approvals, and future plugins.

These components should not be tightly coupled through direct calls whenever a state change or operational activity occurs.

The system needs an audit trail, live UI updates, task correlation, debugging visibility, and future support for automation based on system activity.

---

## Decision

Foundry OS will use an event-driven core.

All meaningful system activity must emit structured events using the common event envelope defined in ARC-006.

Events will be used for:

- UI updates
- State updates
- Audit history
- Notifications
- Debugging
- Task correlation
- Plugin integration
- Future automation

---

## Consequences

### Benefits

- Lower coupling between components
- Better observability
- Easier WebSocket streaming
- Easier plugin support
- Better auditability
- Better debugging
- Enables future event replay

### Costs

- More implementation discipline
- Event schemas must be maintained
- Poorly designed events can create noise
- Future persistence requires retention and storage design

---

## Rules

1. Events describe what happened.
2. Events do not command work.
3. Events are immutable.
4. Events must use the standard envelope.
5. Events must include a source.
6. Events must include severity.
7. Events must not contain secrets.
8. High-risk actions must emit approval-related events.

---

## Status

Accepted as a foundational architectural decision.