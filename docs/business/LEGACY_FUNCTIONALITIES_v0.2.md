---
artifact_id: LEGACY-FUNC-CATALOG-001
project: LEGAVIA
title: Legavia Functionality Decomposition
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Functionality Decomposition

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

A **functionality** is a grouped behavior used by the GUI to connect requirements, work packages and independent evidence; it is not the same thing as a functional-requirement ID. Dependencies mean the successor needs the predecessor's contract.

| ID | Functionality | Component | Release | Dependencies | Requirement allocation |
|---|---|---|---|---|---|
| LEGACY-FUNC-001 | Identity, workspace and privacy: Authenticate, authorize and isolate all user-owned content and media. | core | P0 | — | LEGACY-FNC-001, LEGACY-NFR-002, LEGACY-NFR-003, LEGACY-NFR-009, LEGACY-NFR-016, LEGACY-BIZ-003, LEGACY-BIZ-006 |
| LEGACY-FUNC-002 | App shell and responsive UX: Five destinations, responsive layouts, accessible navigation and explicit state feedback. | ux | P0 | LEGACY-FUNC-001 | LEGACY-FNC-017, LEGACY-FNC-061, LEGACY-UX-001, LEGACY-UX-002, LEGACY-UX-003, LEGACY-UX-004, LEGACY-UX-005, LEGACY-UX-006, LEGACY-UX-007, LEGACY-UX-008, LEGACY-UX-009, LEGACY-UX-010, LEGACY-UX-012, LEGACY-NFR-001, LEGACY-NFR-012, LEGACY-NFR-013 |
| LEGACY-FUNC-003 | Goals, phases and milestones: Create and maintain nested goal progression and explicit success criteria. | goals | P0 | LEGACY-FUNC-001 | LEGACY-FNC-003 |
| LEGACY-FUNC-004 | Tasks and Today: Create goal-linked actions and execute daily tasks from one consolidated view. | today | P0 | LEGACY-FUNC-002, LEGACY-FUNC-003 | LEGACY-FNC-002, LEGACY-FNC-007 |
| LEGACY-FUNC-005 | Goal world map: Render goal and phase progression with accessible visual states. | map | P0 | LEGACY-FUNC-002, LEGACY-FUNC-003 | LEGACY-FNC-004, LEGACY-FNC-005 |
| LEGACY-FUNC-006 | Habits and recovery: Schedule positive and avoid/negative behaviors, continuity and recovery. | habits | P0 | LEGACY-FUNC-001, LEGACY-FUNC-004 | LEGACY-FNC-006, LEGACY-FNC-008, LEGACY-FNC-011, LEGACY-FNC-012, LEGACY-FNC-057, LEGACY-FNC-058 |
| LEGACY-FUNC-007 | Completion and progress ledger: Persist completions, reversal and exactly-once cross-module progress. | core | P0 | LEGACY-FUNC-003, LEGACY-FUNC-004 | LEGACY-FNC-009, LEGACY-FNC-010, LEGACY-NFR-005, LEGACY-NFR-010, LEGACY-FNC-066 |
| LEGACY-FUNC-008 | XP, rewards and achievements: Materialize skills, levels, awards and currency derived from verified actions. | gamification | P0 | LEGACY-FUNC-007 | LEGACY-FNC-013, LEGACY-FNC-014, LEGACY-FNC-015, LEGACY-FNC-016, LEGACY-FNC-067, LEGACY-BIZ-002 |
| LEGACY-FUNC-009 | Insights and trends: Aggregate dated actions, milestones and meaningful progress signals. | insights | P0 | LEGACY-FUNC-007 | LEGACY-FNC-021 |
| LEGACY-FUNC-010 | Water and activity: Capture hydration with servings and targets, optionally workouts and runs. | health | P0 | LEGACY-FUNC-002, LEGACY-FUNC-001 | LEGACY-FNC-031, LEGACY-FNC-032, LEGACY-FNC-062 |
| LEGACY-FUNC-011 | Focus forest: Track named focus sessions and derive forest growth and optional reward transactions. | focus | P1 | LEGACY-FUNC-007, LEGACY-FUNC-008 | LEGACY-FNC-029, LEGACY-FNC-030 |
| LEGACY-FUNC-012 | Financial ledger and planning: Import accounts/transactions, monthly savings and scenario projections with provenance. | finance | P1 | LEGACY-FUNC-001, LEGACY-FUNC-002 | LEGACY-FNC-028, LEGACY-FNC-033, LEGACY-FNC-034, LEGACY-FNC-035, LEGACY-FNC-036, LEGACY-FNC-037, LEGACY-FNC-038, LEGACY-FNC-059, LEGACY-FNC-064 |
| LEGACY-FUNC-013 | Courses and learning: Track course hierarchy, progress and user-reviewed AI extraction. | learning | P1 | LEGACY-FUNC-001, LEGACY-FUNC-002 | LEGACY-FNC-027, LEGACY-FNC-039 |
| LEGACY-FUNC-014 | Book reading tracker: Manage books and estimate completion using timestamped observation trends. | books | P1 | LEGACY-FUNC-001, LEGACY-FUNC-002 | LEGACY-FNC-040, LEGACY-FNC-041, LEGACY-NFR-017 |
| LEGACY-FUNC-015 | Movie recommendation queue: Capture recommendations with attribution and externally sourced rating information. | movies | P1 | LEGACY-FUNC-001, LEGACY-FUNC-002 | LEGACY-FNC-042, LEGACY-FNC-043 |
| LEGACY-FUNC-016 | Games and timers: Track owned games, individual sessions, and cumulative playtime. | games | P1 | LEGACY-FUNC-001, LEGACY-FUNC-002 | LEGACY-FNC-044 |
| LEGACY-FUNC-017 | Notes, memory and media: Capture personal notes, voice, photos, notebook imports and mind-map relationships. | memory | P1 | LEGACY-FUNC-001, LEGACY-FUNC-002 | LEGACY-FNC-045, LEGACY-FNC-046, LEGACY-FNC-047, LEGACY-FNC-048 |
| LEGACY-FUNC-018 | Calendar and reminders: Present authorized calendar context and configurable direct-action reminders. | calendar | P1 | LEGACY-FUNC-004 | LEGACY-FNC-019, LEGACY-FNC-020, LEGACY-FNC-050, LEGACY-FNC-060 |
| LEGACY-FUNC-019 | Voice/chat action capture: Produce previewable AI-generated structured proposals and require confirmation before writes. | ai | P1 | LEGACY-FUNC-004 | LEGACY-FNC-051 |
| LEGACY-FUNC-020 | AI feature governance: Capture feature requests, review proposals, authorize beta promotion and audit decisions. | governance | P1 | LEGACY-FUNC-019 | LEGACY-FNC-025, LEGACY-FNC-026, LEGACY-FNC-055, LEGACY-NFR-006, LEGACY-BIZ-005 |
| LEGACY-FUNC-021 | Family, permissions and quotas: Manage invited members, shared goals and tenant resource limits. | family | P1 | LEGACY-FUNC-001 | LEGACY-FNC-024, LEGACY-FNC-053, LEGACY-FNC-054, LEGACY-FNC-065 |
| LEGACY-FUNC-022 | Integrations and import/export: Manage external connectors, data provenance, exports and GitHub proposed work. | integrations | P1 | LEGACY-FUNC-001 | LEGACY-FNC-022, LEGACY-FNC-023, LEGACY-FNC-052, LEGACY-FNC-056, LEGACY-FNC-063 |
| LEGACY-FUNC-023 | CV and professional profile: Create career history and propose reviewed updates based on completed work. | career | P2 | LEGACY-FUNC-003 | LEGACY-FNC-049 |
| LEGACY-FUNC-024 | Data resilience, security and release quality: Protect lifecycle integrity, tenant boundaries, backups and independent test evidence. | platform | P0 | LEGACY-FUNC-001 | LEGACY-NFR-011, LEGACY-NFR-014, LEGACY-NFR-015, LEGACY-NFR-018, LEGACY-NFR-019, LEGACY-BIZ-009 |
| LEGACY-FUNC-025 | Design themes and accessibility: Use approved visual language and offer low-gamification theming without breaking controls. | ux | P1 | LEGACY-FUNC-002 | LEGACY-UX-011, LEGACY-FNC-005, LEGACY-NFR-007 |
| LEGACY-FUNC-026 | Cross-domain activity insights: Combine privacy-safe activity, habits, tasks and financial view models without duplicating source data. | insights | P1 | LEGACY-FUNC-009, LEGACY-FUNC-012 | LEGACY-FNC-021, LEGACY-FNC-059, LEGACY-NFR-008 |

## Ownership model

Identity, shared goal graph, completion events and the reward ledger are canonical platform-owned entities; module UIs do not create private copies of them. Read models and map/insights projections may be rebuilt from source records. Separate module adapters implement import/ingest rules with consent and provenance.

## GUI and component compatibility

Current `sdlc_gui.model` validates `scope` using legacy `all/library/node` values. All Legavia project functionalities use `scope: all` until product-specific component-filter support is implemented and regression-tested. The `component` property is future-facing machine-readable metadata, **not** an active filter. This prevents misrepresenting finance as a ROS node or Goal Map as a library.
