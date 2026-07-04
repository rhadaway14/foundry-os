# ADR-0002 — Worker / Agent Separation

**Status:** Accepted  
**Date:** 2026-07-04  
**Owner:** Robert Hadaway

---

## Context

Foundry OS must integrate with external systems while also supporting AI-driven reasoning and task execution.

External systems include GitHub, Docker, Kubernetes, filesystems, shells, CI/CD runners, Grafana, Couchbase, and future tools.

AI agents may need to reason about goals, make plans, interpret failures, generate code, write documentation, or recommend next actions.

If integration logic and reasoning logic are mixed together, the system becomes tightly coupled, difficult to test, difficult to secure, and difficult to extend.

---

## Decision

Foundry OS will separate **Workers** from **AI Agents**.

Workers are tool/integration adapters.

AI Agents are reasoning/planning actors.

The Orchestrator coordinates both.

---

## Worker Responsibilities

Workers:

- Communicate with external systems
- Expose explicit capabilities
- Validate inputs
- Return structured results
- Emit events
- Report health
- Enforce low-level safety checks

Workers do not reason about goals.

---

## AI Agent Responsibilities

AI Agents:

- Interpret tasks
- Plan work
- Decide which capabilities are needed
- Request worker capabilities through the Orchestrator
- Produce summaries, recommendations, code, documents, or decisions

AI Agents do not directly access external systems.

---

## Architectural Rules

1. Workers never call other workers.
2. AI Agents never call external systems directly.
3. AI Agents request capabilities through the Orchestrator.
4. The Orchestrator enforces approval policy.
5. Workers expose capabilities, not business workflows.
6. Business workflows belong to the Orchestrator and AI Agents.

---

## Consequences

### Benefits

- Easier testing
- Better security boundaries
- Easier replacement of tools
- Supports multiple AI providers
- Supports non-AI automation
- Keeps integrations deterministic
- Keeps reasoning logic isolated

### Costs

- More abstractions
- More routing through the Orchestrator
- Slightly slower initial development
- Requires clear capability definitions

---

## Examples

### Correct

Engineer Agent requests:

> Run test suite for project `foundry-os`

The Orchestrator calls:

> Shell Worker → execute approved test command

### Incorrect

Engineer Agent directly opens a shell and runs arbitrary commands.

---

## Status

Accepted as a foundational architectural decision.