---
id: FOAS-001
title: FOAS Versioning
status: Draft
version: 1.0.0
owner: Robert Hadaway
reviewers:
  - Robert Hadaway
depends_on:
  - FOAS-000
references:
  - ARC-009
  - ARC-010
  - ARC-011
  - ARC-012
  - ARC-020
implemented_by: []
last_updated: 2026-07-04
---

# FOAS-001 — FOAS Versioning

---

# Purpose

FOAS (Foundry OS Architecture Specification) is the authoritative engineering specification for Foundry OS.

Unlike traditional documentation, FOAS is a machine-readable specification that governs:

- Platform Architecture
- Runtime Contracts
- APIs
- SDKs
- Workers
- AI Agents
- Plugins
- Domain Models
- Data Models
- Event Models
- Security Requirements
- Deployment Architecture

Because these specifications define how the platform behaves, FOAS itself is versioned as a product.

---

# Vision

The architecture is the contract.

The implementation must conform to the architecture—not the other way around.

Every runtime component should explicitly declare the version of FOAS it implements.

```
              FOAS 1.0

                   │

     ┌─────────────┼─────────────┐

     ▼             ▼             ▼

 Runtime       Worker SDK     Agent SDK

     ▼             ▼             ▼

 Workers       Plugins      Applications
```

This allows Foundry OS to evolve while maintaining compatibility across versions.

---

# Version Format

FOAS follows Semantic Versioning.

```
MAJOR.MINOR.PATCH
```

Example:

```
1.0.0

1.1.0

1.2.4

2.0.0
```

---

# Version Meanings

## Patch Releases

Patch releases contain:

- Documentation corrections
- Clarifications
- Typographical fixes
- Diagram updates
- Metadata improvements

They never change platform behavior.

Example

```
1.0.0

↓

1.0.1
```

---

## Minor Releases

Minor releases introduce backward-compatible additions.

Examples

- New architecture documents

- New SDK specifications

- Additional APIs

- New capability contracts

- Additional workflow features

Existing implementations remain compatible.

Example

```
1.0.0

↓

1.1.0
```

---

## Major Releases

Major releases contain breaking architectural changes.

Examples

- Runtime redesign

- Capability contract changes

- Worker interface changes

- Event schema changes

- State model redesign

- Plugin manifest changes

Implementations must be updated before claiming compatibility.

Example

```
1.x

↓

2.0
```

---

# Compatibility

Every runtime component declares which FOAS version it supports.

Example

```yaml
foas:

  version: 1.0.0

  compatibility:

    min: 1.0.0

    max: 1.x
```

Supported components include:

- Runtime Kernel
- Workers
- AI Agents
- Plugins
- REST APIs
- WebSocket APIs
- SDKs
- Workflow Definitions
- Capability Contracts

---

# Runtime Compatibility

At startup the Runtime validates compatibility.

```
Worker

↓

FOAS Version

↓

Compatible?

↓

YES

↓

Load Worker

↓

NO

↓

Reject Worker
```

This prevents incompatible plugins from loading.

---

# Plugin Compatibility

Plugin manifests include FOAS compatibility.

Example

```yaml
plugin:

  name: Email Worker

  version: 1.2.0

  foas:

    min: 1.0.0

    max: 1.x
```

Plugins incompatible with the running platform are disabled automatically.

---

# Worker Compatibility

Workers also declare compatibility.

```
Architecture Worker

↓

FOAS 1.x

↓

Compatible

↓

Load
```

Workers should never assume runtime behavior outside their supported FOAS versions.

---

# AI Agent Compatibility

AI Agents depend on:

- Capability Contracts

- Event Models

- Workflow Definitions

- State Models

Because those evolve, Agents must also declare FOAS compatibility.

---

# Capability Compatibility

Capability Contracts include a required FOAS version.

Example

```yaml
capability:

  name: email.send

  foas:

    version: 1.0.0
```

This guarantees contracts remain stable.

---

# API Compatibility

REST

WebSocket

GraphQL (future)

must all reference the FOAS version that defines them.

---

# SDK Compatibility

Worker SDK

Plugin SDK

Agent SDK

all evolve alongside FOAS.

Each SDK release references the architecture version it implements.

---

# Migration

Every major FOAS release includes migration guidance.

Example

```
FOAS 1.x

↓

Migration Guide

↓

FOAS 2.0
```

Migration documents should identify:

Breaking changes

Required implementation updates

Deprecated features

Replacement architecture

Upgrade steps

---

# Validation

The FOAS Validator verifies:

- Valid document metadata

- Dependency integrity

- Duplicate IDs

- Broken references

- Version compatibility

Future versions should also verify:

Worker compatibility

Plugin compatibility

Agent compatibility

REST compatibility

Workflow compatibility

---

# Release Artifacts

Every FOAS release produces:

```
FOAS Release

↓

Architecture Index

↓

Dependency Graph

↓

Validation Report

↓

Architecture Portal

↓

Release Notes

↓

Migration Guide
```

This creates a complete engineering release.

---

# Governance

FOAS is the highest engineering authority within Foundry OS.

Changes to FOAS require:

Architecture review

Validation

Approval

Version assignment

Release notes

Once released, implementations should update to the new architecture rather than modifying architecture to match implementation.

---

# Future Roadmap

Future FOAS versions may introduce:

Automatic migration analysis

Architecture diff generation

Dependency impact reports

Plugin compatibility matrices

Worker compatibility reports

AI Agent compatibility reports

Architecture quality scoring

Automated release generation

---

# Design Rules

1. FOAS is versioned independently of the runtime.
2. The architecture is the source of truth.
3. Implementations declare FOAS compatibility.
4. Workers declare FOAS compatibility.
5. Plugins declare FOAS compatibility.
6. AI Agents declare FOAS compatibility.
7. Capability Contracts declare FOAS compatibility.
8. Breaking architectural changes require a major version.
9. Backward-compatible additions require a minor version.
10. Clarifications require a patch version.
11. The runtime validates compatibility before loading components.
12. Every FOAS release includes validation, release notes, and migration guidance.

---

# Relationship to Other Documents

| Document | Purpose |
|------------|----------------------------------------------|
| FOAS-000 | Master Architecture Index |
| ARC-009 | Capability Contracts |
| ARC-010 | Worker Architecture |
| ARC-011 | AI Agent Architecture |
| ARC-012 | Workflow Engine |
| ARC-020 | Runtime Execution Model |

---

# Guiding Principle

> **The implementation follows the architecture.**
>
> **FOAS defines the platform.**
>
> **Every worker, plugin, API, SDK, and AI agent must explicitly declare which version of the Foundry OS Architecture Specification it implements.**

By versioning the architecture itself, Foundry OS ensures that its design, implementation, and ecosystem evolve together in a controlled, traceable, and backward-compatible manner. FOAS is not simply documentation—it is the engineering contract that governs the entire platform.