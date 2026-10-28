---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Product Vision, Stakeholders and Scope

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

## Product purpose
Legavia is an integrated, privacy-first life-management system for mobile and desktop browsers. It connects actionable goals, habits, schedules, learning, finances, health context, memories, personal media, focus time and optional collaborative goals with deterministic progression mechanics. The product should reduce data-entry friction rather than create a game that requires constant maintenance.

## Stakeholders and roles
- **Individual account owner:** plans, records, reviews and exports personal activities; has primary ownership of private data.
- **Invited family/friend collaborator:** participates only in explicitly shared resources.
- **Workspace administrator:** manages memberships, quotas, approvals, feature flags and audit trails; does not automatically gain content-read permissions.
- **Product/Systems Engineering owner:** approves controlled requirements, use cases, acceptance criteria and architectural decisions.
- **UX agent and human reviewer:** create/refine reference-driven phone/desktop screen contracts and review visual evidence.
- **Architecture, Development and QA agents:** work on bounded scopes against approved constraints; only independent testing constitutes verification evidence.

## Business outcomes and candidate KPIs
- A user can convert a long-term goal into a daily action and observe a correct progress/XP projection using one coherent user journey.
- Critical daily completions require one direct interaction from the Today screen where feasible; show immediate local feedback.
- Every saved item has an owning workspace, access policy, event history and source provenance where applicable.
- Zero confirmed cross-workspace authorization failures and zero duplicate completion rewards across retry tests are release gates.
- Mobile and desktop screen states must visually match approved baselines at controlled fixtures and viewports (numeric visual thresholds must be set by an ADR, not invented).
- Weekly voluntary usage and time spent on configuration versus real activity are review metrics, not hard-to-achieve retention promises.

## Incremental delivery
**Foundation/P0:** privacy, auth and workspace isolation; common domain/events; Today; goals/phases/milestones; task lifecycle; exactly-once completion; XP/map progress; basic insights; responsive five-surface shell; deterministic tests; export readiness.

**P1:** recurring/negative habits; recovery; hydration; focus; books and course tracking; photo/voice notes; finance ledger/import; calendar/health permission-based imports; AI-reviewed task proposals; configurable rewards; reminders.

**P2:** game timer, IMDb ranking with licensed source, interactive CV, deep social challenges, beta feature rollout, quota administration and advanced AI planning. Modules may be promoted by approved reprioritization.

## Explicit out of scope for initial vertical slice
Native iOS binary/App Store publication, medical diagnosis, automated bank transfers or trading, unattended AI changes to permanent records, public-by-default social data, autonomous external issue changes, and unverified financial forecasts. The first app target is responsive web/PWA; native packaging remains an architecture option.

## Assumptions and dependencies
The five-surface shell **Today / Map / Life / Insights / Me** remains the current UX invariant. Product brand is Legavia; historical LEGACY identifiers and repository names persist. GitHub is the version-control provider. User-supplied design image references are required to establish approved pixel-art fidelity; no exact screenshot equivalence is claimed until comparison evidence exists. Integration credentials, data hosting, consent and platform API availability remain decisions.

## Product acceptance authority
These are **candidate** requirements. Only Systems Engineering approval of an identified revision may promote them. Release readiness additionally depends on accepted architecture and passing independent verification; mere code completion is insufficient.
