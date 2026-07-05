---
id: ARC-028
title: Adaptive Capability Evolution
status: Draft
version: 1.0
owner: Robert Hadaway
reviewers:
  - Robert Hadaway
depends_on:
  - ARC-009
  - ARC-010
  - ARC-011
  - ARC-012
  - ARC-019
  - ARC-020
references:
  - ADR-0002
  - ADR-0003
  - ADR-0004
implemented_by: []
last_updated: 2026-07-04
---

# ARC-028 — Adaptive Capability Evolution

---

# Purpose

One of the primary design goals of Foundry OS is to evolve over time.

When a workflow requires functionality that does not currently exist, the platform should not simply fail or return an error.

Instead, Foundry OS should recognize the missing capability, determine whether an existing implementation already exists, and if necessary design, implement, validate, document, approve, register, and persist a new capability so that future workflows may reuse it.

Adaptive Capability Evolution transforms Foundry OS from a static automation platform into an extensible operating system that continuously expands through governed evolution.

---

# Philosophy

Traditional automation systems are static.

```
Need new feature

↓

Engineer writes code

↓

Deploy

↓

Repeat
```

Foundry OS is dynamic.

```
Need new capability

↓

Capability Missing

↓

Capability Evolution Workflow

↓

Human Approval

↓

Architecture

↓

Implementation

↓

Testing

↓

Registration

↓

Persistence

↓

Resume Workflow
```

The platform becomes increasingly capable over time.

---

# Design Principles

Adaptive Capability Evolution follows these principles.

## Capabilities are permanent assets

Generated capabilities are never temporary.

They become reusable components of the platform.

## Humans remain in control

Foundry OS may design and implement capabilities.

Only humans decide whether those capabilities become trusted platform functionality.

## Architecture precedes implementation

Every generated capability must first define:

- Architecture
- Capability Contract
- Security Model
- Tests
- Documentation

before implementation begins.

## Every capability is reusable

If a capability is created once, it should never need to be recreated.

Future workflows should automatically discover and reuse it.

---

# Capability Evolution Lifecycle

```
User Request

↓

Workflow Planning

↓

Capability Resolution

↓

Capability Missing

↓

Capability Proposal

↓

Approval to Build

↓

Architecture Generation

↓

Specification Generation

↓

Implementation

↓

Testing

↓

Security Review

↓

Approval to Enable

↓

Registration

↓

Persistence

↓

Resume Original Workflow
```

---

# Capability Discovery

Before generating anything, Foundry OS must attempt discovery.

Discovery order:

1. Capability Registry

2. Disabled Providers

3. Local Plugin Repository

4. Installed Packages

5. Enterprise Plugin Catalog

6. Community Marketplace (future)

7. Internal Similarity Search

Only after all discovery methods fail may capability generation begin.

---

# Capability Proposal

Every generated capability begins as a proposal.

Example

```yaml
name: email.send

provider: Email Worker

reason:
  Original workflow requires sending customer email.

risk: Medium

estimated_files:

  - worker.py

  - contract.yaml

  - tests.py

  - README.md

required_secrets:

  - SMTP_SERVER

  - SMTP_USERNAME

  - SMTP_PASSWORD

approval_required:

  - Build

  - Enable

  - Execute
```

The proposal is stored in the platform state.

---

# Architecture Generation

Before writing code, Foundry OS generates architecture.

Artifacts include:

- ARC document additions
- SPEC document
- MODEL changes
- Capability Contract
- Security analysis
- Dependency analysis

This guarantees that architecture remains the source of truth.

---

# Implementation

Once architecture is approved, the platform may implement:

Worker

Plugin

SDK updates

REST endpoints

WebSocket messages

Documentation

Tests

Configuration

CI updates

Deployment manifests

Implementation is treated exactly like any human-written code.

---

# Validation

Generated capabilities must successfully pass:

Static analysis

Unit tests

Integration tests

Security scanning

Capability contract validation

Architecture validation

FOAS validation

No capability may be enabled until validation succeeds.

---

# Persistence

Generated capabilities become permanent platform assets.

Persisted artifacts include:

Capability Contract

Worker source code

Tests

Configuration

Plugin Manifest

Documentation

FOAS references

Deployment metadata

Version history

Approval history

Registration metadata

Nothing is discarded after execution.

---

# Registration

Only validated capabilities may enter the Capability Registry.

Registration records:

Capability Name

Provider

Version

Status

Risk

Owner

Required Secrets

Dependencies

Approval Metadata

Registration Time

Once registered, the capability becomes discoverable by every future workflow.

---

# Versioning

Generated capabilities follow semantic versioning.

Example

```
email.send

1.0.0

↓

1.1.0

↓

2.0.0
```

Upgrades follow the normal approval workflow.

---

# Human Approval

Three approval gates exist.

## Build Approval

May the platform implement this capability?

## Enablement Approval

May this capability become part of Foundry OS?

## Execution Approval

Should this capability execute when required?

Approval policies depend on capability risk.

---

# Secrets

Generated capabilities never store secrets.

Instead they define secret requirements.

Example

```yaml
required_secrets:

- SMTP_HOST

- SMTP_USERNAME

- SMTP_PASSWORD
```

Administrators provide actual values through the configured secrets provider.

---

# Workflow Recovery

The original workflow pauses.

It never fails.

Once capability registration completes:

```
Capability Ready

↓

Registry Updated

↓

Workflow Reloaded

↓

Resume From Blocked Step
```

The user experiences a temporary delay rather than failure.

---

# Capability Evolution Worker

Adaptive evolution is itself implemented through a Worker.

Capabilities include:

```
capability.detect_missing

capability.propose

capability.search

capability.generate

capability.test

capability.validate

capability.register

capability.rollback

capability.disable

capability.upgrade
```

This allows Foundry OS to evolve using the same architecture as every other subsystem.

---

# Digital Twin

The Digital Twin records:

Missing Capabilities

Capability Proposals

Build Status

Approval Status

Test Results

Security Results

Registration Events

Version History

Usage Metrics

Retirement Status

The platform therefore understands not only what capabilities exist, but how they came into existence.

---

# Events

Adaptive Capability Evolution emits events.

```
capability.missing

capability.proposal.created

capability.build.started

capability.build.completed

capability.tests.started

capability.tests.passed

capability.tests.failed

capability.security.passed

capability.security.failed

capability.enablement.requested

capability.enabled

capability.registered

capability.disabled

capability.upgraded

workflow.resumed
```

---

# Future Extensions

Adaptive Capability Evolution may later support:

Enterprise Plugin Marketplace

Capability recommendation engine

Automatic refactoring

Capability quality scoring

Duplicate capability detection

Capability deprecation

Cross-platform capability sharing

Automatic documentation generation

Automatic release generation

Architecture impact analysis

---

# Relationship to Other Architecture

| Document | Purpose |
|------------|---------------------------------------------|
| ARC-009 | Capability contracts and registry |
| ARC-010 | Worker architecture |
| ARC-011 | AI Agent architecture |
| ARC-012 | Workflow execution |
| ARC-019 | Capability persistence |
| ARC-020 | Runtime execution |
| FOAS-000 | Architecture governance |

---

# Guiding Principle

> **Foundry OS does not merely execute work.**
>
> **Foundry OS improves itself by creating permanent, governed, reusable capabilities that become part of the operating system for future work.**

A capability generated today should become a first-class citizen of the platform tomorrow. Every improvement strengthens the system for subsequent users and workflows, allowing Foundry OS to evolve continuously while remaining architecturally consistent, secure, and under human governance.