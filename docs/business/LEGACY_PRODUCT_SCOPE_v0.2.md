---
artifact_id: LEGACY-SCOPE-001
project: LEGAVIA
title: Legavia Product Scope and Release Slicing
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Product Scope and Release Slicing

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

## Product value proposition

One coherent life-management application integrates daily execution, goals and achievements, fitness/wellbeing, finance, learning and personal knowledge. It prioritizes fast data capture and reliable retrieval over game-driven administrative tasks.

## Functional module catalog

| Domain / module | Principal capability | Planned release | Implementation allocation |
|---|---|---|---|
| core — Identity, workspace and privacy | Authenticate, authorize and isolate all user-owned content and media. | P0 | LEGACY-FUNC-001 |
| ux — App shell and responsive UX | Five destinations, responsive layouts, accessible navigation and explicit state feedback. | P0 | LEGACY-FUNC-002 |
| goals — Goals, phases and milestones | Create and maintain nested goal progression and explicit success criteria. | P0 | LEGACY-FUNC-003 |
| today — Tasks and Today | Create goal-linked actions and execute daily tasks from one consolidated view. | P0 | LEGACY-FUNC-004 |
| map — Goal world map | Render goal and phase progression with accessible visual states. | P0 | LEGACY-FUNC-005 |
| habits — Habits and recovery | Schedule positive and avoid/negative behaviors, continuity and recovery. | P0 | LEGACY-FUNC-006 |
| core — Completion and progress ledger | Persist completions, reversal and exactly-once cross-module progress. | P0 | LEGACY-FUNC-007 |
| gamification — XP, rewards and achievements | Materialize skills, levels, awards and currency derived from verified actions. | P0 | LEGACY-FUNC-008 |
| insights — Insights and trends | Aggregate dated actions, milestones and meaningful progress signals. | P0 | LEGACY-FUNC-009 |
| health — Water and activity | Capture hydration with servings and targets, optionally workouts and runs. | P0 | LEGACY-FUNC-010 |
| focus — Focus forest | Track named focus sessions and derive forest growth and optional reward transactions. | P1 | LEGACY-FUNC-011 |
| finance — Financial ledger and planning | Import accounts/transactions, monthly savings and scenario projections with provenance. | P1 | LEGACY-FUNC-012 |
| learning — Courses and learning | Track course hierarchy, progress and user-reviewed AI extraction. | P1 | LEGACY-FUNC-013 |
| books — Book reading tracker | Manage books and estimate completion using timestamped observation trends. | P1 | LEGACY-FUNC-014 |
| movies — Movie recommendation queue | Capture recommendations with attribution and externally sourced rating information. | P1 | LEGACY-FUNC-015 |
| games — Games and timers | Track owned games, individual sessions, and cumulative playtime. | P1 | LEGACY-FUNC-016 |
| memory — Notes, memory and media | Capture personal notes, voice, photos, notebook imports and mind-map relationships. | P1 | LEGACY-FUNC-017 |
| calendar — Calendar and reminders | Present authorized calendar context and configurable direct-action reminders. | P1 | LEGACY-FUNC-018 |
| ai — Voice/chat action capture | Produce previewable AI-generated structured proposals and require confirmation before writes. | P1 | LEGACY-FUNC-019 |
| governance — AI feature governance | Capture feature requests, review proposals, authorize beta promotion and audit decisions. | P1 | LEGACY-FUNC-020 |
| family — Family, permissions and quotas | Manage invited members, shared goals and tenant resource limits. | P1 | LEGACY-FUNC-021 |
| integrations — Integrations and import/export | Manage external connectors, data provenance, exports and GitHub proposed work. | P1 | LEGACY-FUNC-022 |
| career — CV and professional profile | Create career history and propose reviewed updates based on completed work. | P2 | LEGACY-FUNC-023 |
| platform — Data resilience, security and release quality | Protect lifecycle integrity, tenant boundaries, backups and independent test evidence. | P0 | LEGACY-FUNC-024 |
| ux — Design themes and accessibility | Use approved visual language and offer low-gamification theming without breaking controls. | P1 | LEGACY-FUNC-025 |
| insights — Cross-domain activity insights | Combine privacy-safe activity, habits, tasks and financial view models without duplicating source data. | P1 | LEGACY-FUNC-026 |

## Release boundaries

**P0 — Integrated coherent core:** authentication/workspaces and server-side privacy boundaries; Today, goals, milestone graph, tasks, habit essentials, responsive shell, usable Map, exactly-once completion/undo/XP, water log and basic insights. Independent critical-path verification and phone/desktop visual evidence are mandatory. The first user journey is goal → milestone → Today task → complete → XP/map update → undo → persisted reload.

**P1 — Product depth:** focus forest, expense and savings management with spreadsheet import and multicurrency rules, learning, books, movies, games, voice/notes, safe AI drafts, feature governance, family sharing, authorized integrations and reminders. These are separate bounded increments behind verified core primitives.

**P2 — Optional ecosystem:** reMarkable import, mind-map, career profile/CV proposals, rich financial assets/depreciation, advanced health activity and beta rollout controls, contingent on separate privacy/security/UX decisions.

**Release rule:** A module is not shippable because a page renders; persistence, explicit permission checks, test/trace evidence, mobile/desktop states and user journey validation must be complete.

## Explicit out-of-scope until an approved change

Automated payments; financial advice or investment transactions; clinical diagnosis; covert profile data aggregation; mandatory public competition; unsafe automated feature deployments; unconsented content scraping. The presence of a future domain in navigation is not acceptance of its full implementation.

## Dependencies and prioritization

Identity/workspace, core domain entities and event idempotency precede gamification projections. Common UI patterns and responsive reference baselines precede full-screen visual experiences. Reconciliation/provenance semantics precede data imports. Data-loss and privacy controls precede private media/voice. See Work Package predecessor graph in `traceability/manifest.json`.

## Candidate product acceptance KPI families

Daily action friction, successful state restoration, user-controlled correction, import reconciliation accuracy, accessible navigation, consent/revocation efficacy, privacy-boundary testing, release stability and time spent configuring versus benefiting. Numeric SLOs and telemetry collection details require explicit ADR/product decisions before being used as acceptance limits.
