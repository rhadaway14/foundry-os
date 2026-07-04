# Foundry OS Implementation Backlog

## Epic 1 — Capability Registry

### Story 1.1 — Register Capability Contracts

As a platform developer, I want to register capability contracts so that the Orchestrator can discover executable functionality.

Acceptance Criteria:

- Contract includes name, version, provider, risk, approval requirement, input schema, and output schema
- Invalid contracts are rejected
- Duplicate capability names are rejected
- Unit tests exist

Technical Tasks:

- Implement CapabilityContract model
- Implement CapabilityRegistry
- Add validation logic
- Add tests

FOAS Links:

- ARC-009
- ARC-010
- ARC-011
- ARC-020

### Story 1.2 — Resolve Capabilities

As the Orchestrator, I want to resolve a capability by name so that I do not need to know which provider implements it.

Acceptance Criteria:

- Registry returns provider metadata
- Missing capabilities return structured error
- Provider health is considered

Technical Tasks:

- Add lookup by capability name
- Add provider metadata
- Add tests

FOAS Links:

- ARC-009
- ARC-020

## Epic 2 — Event Bus

### Story 2.1 — Publish Events

As a platform component, I want to publish structured events so that runtime activity is observable.

Acceptance Criteria:

- Event has ID, type, source, severity, timestamp, correlation ID, actor, and payload
- Invalid event envelopes are rejected
- Events are stored in recent history

Technical Tasks:

- Implement Event model
- Implement EventBus
- Add validation
- Add tests

FOAS Links:

- ARC-006
- ADR-0003

## Epic 3 — State Store

### Story 3.1 — Maintain Digital Twin State

As a UI client, I want to read current state so that I do not need to query workers directly.

Acceptance Criteria:

- State has version
- State has updated timestamp
- State is updated by reducers
- `/state` endpoint returns current state

Technical Tasks:

- Implement StateStore
- Implement reducer interface
- Add API endpoint
- Add tests

FOAS Links:

- ARC-007
- ADR-0004
- ARC-020

## Epic 4 — Architecture Worker

### Story 4.1 — Expose FOAS Validation as Capability

As an Architect Agent, I want to validate FOAS through a worker capability so that architecture compliance can be automated.

Acceptance Criteria:

- Capability name is `architecture.validate`
- Capability runs FOAS validator
- Result returns pass/fail and errors
- Capability emits events

Technical Tasks:

- Implement ArchitectureWorker
- Register `architecture.validate`
- Add tests

FOAS Links:

- ARC-009
- ARC-010
- FOAS-000

## Epic 5 — REST API

### Story 5.1 — Expose Runtime Status

As a dashboard user, I want REST endpoints for state, events, and capabilities so that the UI can display the platform.

Acceptance Criteria:

- `/health`
- `/state`
- `/events`
- `/capabilities`
- `/workers`

Technical Tasks:

- Implement FastAPI app
- Add routers
- Add response models
- Add tests

FOAS Links:

- ARC-020
- SPEC-001

## Epic 6 — React Dashboard

### Story 6.1 — Display Digital Twin

As Robert, I want a dashboard that shows the current Foundry OS state.

Acceptance Criteria:

- Shows system state
- Shows workers
- Shows events
- Shows capability registry
- Reads state APIs only

Technical Tasks:

- Create React app
- Add API client
- Add dashboard layout
- Add state cards

FOAS Links:

- ARC-007
- ARC-020

## Epic 7 — Workflow Engine

### Story 7.1 — Execute Simple Workflow

As the Orchestrator, I want to execute a workflow graph so that multi-step work can be coordinated.

Acceptance Criteria:

- Workflow has tasks
- Tasks have dependencies
- Tasks execute in order
- Events are emitted
- State is updated

Technical Tasks:

- Define workflow model
- Define task model
- Implement executor
- Add tests

FOAS Links:

- ARC-012
- ARC-020

## Epic 8 — AI Agent Runtime

### Story 8.1 — Register Agent Capability

As an AI Agent developer, I want agents to register reasoning capabilities.

Acceptance Criteria:

- Agent capability is contract-defined
- Agent is discoverable through registry
- Agent never accesses workers directly

Technical Tasks:

- Define AgentProvider interface
- Add sample ArchitectAgent
- Add tests

FOAS Links:

- ARC-011
- ARC-009
