# Foundry OS Implementation Roadmap

Status: Draft  
Owner: Robert Hadaway  
Architecture Source: FOAS

## Phase 0 — Architecture Foundation

- [x] FOAS document structure
- [x] FOAS metadata bootstrap
- [x] FOAS validation
- [x] FOAS graph generation
- [x] Runtime architecture
- [x] Capability architecture
- [x] Worker architecture
- [x] AI Agent architecture
- [x] Workflow engine architecture

## Phase 1 — Core Runtime Kernel

### Epic 1: Capability Registry

FOAS Links:

- ARC-009 Capability Architecture
- ARC-010 Worker Architecture
- ARC-011 AI Agent Architecture
- ARC-020 Runtime Execution Model

Features:

- Register capability providers
- Register capability contracts
- Validate contracts
- Resolve capabilities by name
- Track provider health

Acceptance Criteria:

- Capabilities can be registered statically
- Invalid contracts are rejected
- Duplicate capability names are detected
- Capability metadata can be queried
- Unit tests cover registration, lookup, and validation

Technical Tasks:

- Create backend capability registry module
- Create capability contract model
- Create provider model
- Add registry tests
- Add sample Architecture Worker capability

---

### Epic 2: Event Bus

FOAS Links:

- ARC-006 Event Model
- ADR-0003 Event-Driven Core

Features:

- Publish structured events
- Subscribe to events
- Store recent events in memory
- Validate event envelope

Acceptance Criteria:

- Events follow standard envelope
- Events can be retrieved through API
- Invalid events are rejected
- Tests cover publish, subscribe, and retrieval

Technical Tasks:

- Create event model
- Create event bus service
- Create event validator
- Add `/events` API endpoint
- Add tests

---

### Epic 3: State Store / Digital Twin

FOAS Links:

- ARC-007 State Management
- ADR-0004 Shared State Store
- ARC-020 Runtime Execution Model

Features:

- Maintain current runtime state
- Update state from events
- Expose state through API
- Track state version

Acceptance Criteria:

- State has version and timestamp
- Reducers update state from events
- `/state` returns current Digital Twin
- Tests cover reducer behavior

Technical Tasks:

- Create state store
- Create reducer interface
- Add system reducer
- Add worker reducer
- Add `/state` API endpoint

---

### Epic 4: Architecture Worker

FOAS Links:

- ARC-009 Capability Architecture
- ARC-010 Worker Architecture
- FOAS-000 Architecture Index

Features:

- Validate FOAS documents
- Generate FOAS graph
- Generate FOAS status report
- Bootstrap FOAS metadata

Acceptance Criteria:

- Architecture Worker exposes capabilities
- FOAS validation can run through the worker
- Worker capabilities map to FOAS CLI commands
- Tests cover successful and failed validation

Technical Tasks:

- Wrap FOAS toolchain as worker
- Define capability contracts
- Add worker health check
- Add unit tests

## Phase 2 — API and UI

### Epic 5: REST API

FOAS Links:

- SPEC-001 REST API
- ARC-020 Runtime Execution Model

Features:

- Health endpoint
- Capability endpoints
- Event endpoints
- State endpoints
- Worker endpoints

Acceptance Criteria:

- API returns structured JSON
- API errors are standardized
- OpenAPI docs are generated

---

### Epic 6: React Dashboard

FOAS Links:

- ARC-007 State Management
- ARC-020 Runtime Execution Model

Features:

- System state view
- Worker status
- Capability catalog
- Event stream
- Approval queue placeholder

Acceptance Criteria:

- UI reads from state APIs
- UI does not call workers directly
- Dashboard refreshes automatically

## Phase 3 — Workflow Runtime

### Epic 7: Workflow Engine

FOAS Links:

- ARC-012 Workflow Engine
- ARC-020 Runtime Execution Model

Features:

- Define workflow DAG
- Execute tasks
- Handle task dependencies
- Support approval gates
- Emit workflow events

Acceptance Criteria:

- Simple workflow executes end-to-end
- Failed task marks workflow failed
- Approval task pauses workflow

## Phase 4 — AI Agent Runtime

### Epic 8: Agent Runtime

FOAS Links:

- ARC-011 AI Agent Architecture
- ARC-009 Capability Architecture

Features:

- Register AI Agent providers
- Execute reasoning capabilities
- Produce plans
- Request worker capabilities through orchestrator

Acceptance Criteria:

- Agent never calls external systems directly
- Agent plan is visible
- Agent execution emits events

## Phase 5 — Production Hardening

### Epic 9: Security

FOAS Links:

- ARC-017 Security Architecture

Features:

- Authentication
- Authorization
- Secret redaction
- Approval policies
- Audit trail

### Epic 10: Persistence

FOAS Links:

- ARC-019 Persistence Architecture

Features:

- Persist events
- Persist state snapshots
- Persist workflows
- Recover after restart
