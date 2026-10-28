---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Functionality and Component Allocation

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

The following capabilities define behavior owners, not one repository per feature. A capability can span UI, service and persistence components. All records currently use GUI `scope=all` because its legacy `library/node` filters do not truthfully describe web/mobile application components; the namespaced `legavia_extension` preserves intended ownership until the GUI adapter is complete.

| ID | Capability / Owner | Depends on | Requirements |
| --- | --- | --- | --- |
| LEGACY-CAP-001 | Identity, workspace isolation and data governance (identity-access) | — | 37 linked |
| LEGACY-CAP-002 | Today, schedule and daily execution (today) | LEGACY-CAP-001 | 7 linked |
| LEGACY-CAP-003 | Goals, phases, milestones and map navigation (goals-map) | LEGACY-CAP-001 | 3 linked |
| LEGACY-CAP-004 | Habits, completion, continuity and gamification (gamification) | LEGACY-CAP-002, LEGACY-CAP-003 | 13 linked |
| LEGACY-CAP-005 | Shell navigation, search and insights (app-shell) | LEGACY-CAP-001 | 29 linked |
| LEGACY-CAP-006 | Financial accounts, ledgers, budgets and forecasts (finance) | LEGACY-CAP-001 | 17 linked |
| LEGACY-CAP-007 | Learning and course progress (learning) | LEGACY-CAP-001 | 2 linked |
| LEGACY-CAP-008 | Focus and time tracking (focus) | LEGACY-CAP-002 | 2 linked |
| LEGACY-CAP-009 | Books, games and movies (media-library) | LEGACY-CAP-001 | 5 linked |
| LEGACY-CAP-010 | Memories and knowledge timeline (memory) | LEGACY-CAP-001 | 1 linked |
| LEGACY-CAP-011 | CV and achievement evidence (profile) | LEGACY-CAP-003 | 1 linked |
| LEGACY-CAP-012 | Health and wellness activity (health) | LEGACY-CAP-001 | 1 linked |
| LEGACY-CAP-013 | AI-assisted capture, suggestions and feature approval (ai-governance) | LEGACY-CAP-001 | 6 linked |
| LEGACY-CAP-014 | Family and opt-in social collaboration (social) | LEGACY-CAP-001 | 3 linked |
| LEGACY-CAP-015 | External data and portability integrations (integration) | LEGACY-CAP-001 | 2 linked |

## Cross-cutting behavior
Identity and authorization own access enforcement across every module. The core event ledger owns idempotent event identities; reward calculations are derived and never the origin of financial or activity facts. Domain data lives in `legacy_app`; `legacy_mockups` owns design references, `legacy_verification_tooling` owns independent verification, and `legacy` owns approved functional contracts.

## Capability acceptance
Capability status is **Candidate**. Creating or closing a Work Package does not automatically indicate verified functionality. Independent test evidence is linked through FVT IDs, candidate fingerprints and Systems Engineering review.
