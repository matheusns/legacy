---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Development Slices, Dependencies and Engineering Decisions

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

## Delivery policy
A branch/candidate is not accepted until the SE approval and verification gates are satisfied. GitHub remains the system of record for code history; `legacy` contains controlled contracts and Work Packages. Avoid creating an agent-per-screen: use Systems Engineering, Architecture, UX, Development, Independent QA, Security/Privacy and Integration roles with scoped write permissions.

## Proposed sequence
| Stage | Scope | Exit criterion |
| --- | --- | --- |
| S0 — Baseline | Approve business docs and issue architectural decisions | Signed baseline and ADR register with no unresolved P0 blocker |
| S1 — Secure foundation | Reproducible app, identity/tenancy, canonical goal/task data | Multi-workspace authorization tests and deterministic fixtures pass |
| S2 — Coherent MVP | Five-surface shell, goal hierarchy, linked task, exactly-once XP, undo, map progress | Complete phone+desktop journey with persisted state and FVT-001/002/004/005 evidence |
| S3 — Consistency | Habit schedules, recovery, basic insights, offline/draft behavior | Recovery tests and no duplicate events across retry |
| S4 — Domain expansion | Finance ledger/import, focus, water, books, learning, memory | Independent module tests, privacy gates and data provenance |
| S5 — Assisted/social | AI proposal pipeline, imports, collaborative goals, optional badges | Explicit consent and share permissions; rollback-tested feature flags |

## ADR decisions required before S1/S2 implementation
- ADR-CAND-001: application stack, hosting and persistence; avoid backend/frontend lock-in before trade study.
- ADR-CAND-002: user/workspace/role and resource-sharing authorization model, threat model.
- ADR-CAND-003: immutable domain events, idempotency keys, projections, undo and rewards.
- ADR-CAND-004: pixel-art asset licensing/source versioning, UX golden baseline and responsive design system.
- ADR-CAND-005: application test adapters, candidate fingerprints and GitHub PR/check integration into GUI.
- ADR-CAND-006: offline cache/retry behavior, conflict resolution, backup/restore/deletion.
- ADR-CAND-007: AI consent, provider scopes, approval and speech input privacy.

## Principal risks
Incorrect permission scopes, silently duplicated XP or finance postings, visual mismatch against accepted images, incomplete GUI migration from ROS/GitLab, unreviewed AI persistence, financial import mismatches and irreversible media loss. Each risk requires a corresponding requirement, test and responsible owner before release.

## Initial execution Work Packages
| Work Package | Type | Predecessors | Target repositories |
| --- | --- | --- | --- |
| LEGACY-WORK-001 | systems_engineering | — | legacy |
| LEGACY-WORK-002 | systems_engineering | LEGACY-WORK-001 | legacy |
| LEGACY-WORK-003 | technical | LEGACY-WORK-002 | legacy_app, legacy_verification_tooling |
| LEGACY-WORK-004 | technical | LEGACY-WORK-003 | legacy_app, legacy_mockups, legacy_verification_tooling |
| LEGACY-WORK-005 | technical | LEGACY-WORK-003 | legacy_app, legacy_verification_tooling |
| LEGACY-WORK-006 | technical | LEGACY-WORK-005 | legacy_app, legacy_verification_tooling |
| LEGACY-WORK-007 | technical | LEGACY-WORK-004, LEGACY-WORK-006 | legacy_app, legacy_verification_tooling |
| LEGACY-WORK-008 | technical | LEGACY-WORK-007 | legacy_app, legacy_verification_tooling |
| LEGACY-WORK-009 | technical | LEGACY-WORK-002 | legacy_verification_tooling, legavia_sdlc_gui |
| LEGACY-WORK-010 | technical | LEGACY-WORK-003 | legacy_app, legacy_verification_tooling |
| LEGACY-WORK-011 | technical | LEGACY-WORK-007 | legacy_app, legacy_verification_tooling |
| LEGACY-WORK-012 | technical | LEGACY-WORK-007 | legacy_app, legacy_verification_tooling |

The controlled details are in `docs/work_packages/` and the traceability manifest. No Work Package is marked Done by this document generation.
