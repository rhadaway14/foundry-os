---
id: ARC-001
title: Vision And Scope
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

# 01 - Vision and Scope

Status: Draft  
Project: Foundry OS  
Owner: Robert Hadaway  
Last Updated: 2026-07-04

## Purpose

Foundry OS is a local-first AI development operations platform that coordinates humans, AI agents, development tools, infrastructure, and software delivery workflows.

## Vision

Foundry OS should act as the operating layer for AI-assisted software development. It should allow a human operator to supervise, approve, redirect, and observe work performed by AI agents and automation systems across code repositories, CI/CD pipelines, infrastructure, and documentation.

## Core Principle

Every component should be replaceable.

Workers integrate with tools.  
AI agents reason about tasks.  
The orchestrator coordinates work.  
The UI is only a client.

## Primary Users

- Individual developers using AI coding tools
- Software architects coordinating AI-assisted implementation
- Technical leads supervising multiple repositories
- Platform engineers managing local or self-hosted automation

## In Scope

- Local AI operations dashboard
- Worker architecture for GitHub, Docker, system, runner, Kubernetes, Grafana, and future tools
- AI agent architecture for engineering, architecture, testing, documentation, and release workflows
- Event bus
- Shared state store
- Approval queue
- REST API
- WebSocket updates
- Plugin system
- Local-first deployment

## Out of Scope for MVP

- Multi-tenant SaaS
- Billing
- Public marketplace
- Fully autonomous production deployments without approval
- Replacing GitHub, Docker, Kubernetes, or existing CI/CD systems

## Success Criteria

The MVP is successful when Foundry OS can:

- Monitor GitHub Actions on a self-hosted runner
- Show worker and system status
- Track events and shared state
- Expose status through a React UI
- Support approval-gated tasks
- Provide a clean SDK path for future workers and AI agents