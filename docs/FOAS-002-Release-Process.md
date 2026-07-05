---
id: FOAS-002
title: FOAS Release Process
status: Draft
version: 1.0.0
owner: Robert Hadaway
reviewers:
  - Robert Hadaway
depends_on:
  - FOAS-000
  - FOAS-001
references:
  - ARC-020
implemented_by: []
last_updated: 2026-07-04
---

# FOAS-002 — FOAS Release Process

FOAS is released as an engineering product. Every release represents a stable architectural baseline for Foundry OS.

## Release Types

- Patch: typo fixes, clarifications, metadata fixes
- Minor: backward-compatible additions
- Major: breaking architecture or contract changes

## Required Release Artifacts

- Architecture Index
- Validation Report
- Dependency Graph
- Release Notes
- Migration Guide
- Compatibility Matrix

## Required Validation

- `foas validate`
- duplicate ID check
- broken reference check
- dependency graph generation
- compatibility check

## Guiding Principle

FOAS releases define the platform. The runtime implements the platform.
