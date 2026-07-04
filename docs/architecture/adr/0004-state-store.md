# ADR-0004 — Shared State Store

**Status:** Accepted  
**Date:** 2026-07-04  
**Owner:** Robert Hadaway

---

## Context

Foundry OS needs a consistent way to represent the current condition of the platform.

Events describe what happened, but user interfaces, AI agents, workflows, and approvals need to know what is true right now.

If each worker, agent, or UI queries external systems independently, the platform becomes inconsistent, slow, difficult to secure, and difficult to reason about.

---

## Decision

Foundry OS will use a shared State Store as the authoritative current read model.

The State Store will act as a digital twin of the development environment.

Workers emit events.  
Reducers update state.  
Clients read state.  
The Orchestrator coordinates changes.

---

## Rules

1. State represents current truth.
2. Events represent historical facts.
3. Workers do not directly write state.
4. State updates are performed by reducers or approved platform internals.
5. UI clients read state instead of querying workers.
6. AI Agents access state through the Orchestrator.
7. State must never expose secrets.
8. State should be reconstructable from events over time.

---

## Consequences

### Benefits

- Consistent UI
- Cleaner API design
- Better AI agent context
- Better observability
- Easier WebSocket synchronization
- Supports digital twin visualization
- Enables future replay and debugging

### Costs

- Requires reducer design
- Requires state schema discipline
- Requires careful handling of stale data
- Requires security filtering

---

## Status

Accepted as a foundational architectural decision.