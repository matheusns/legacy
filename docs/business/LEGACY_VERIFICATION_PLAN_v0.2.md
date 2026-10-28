---
artifact_id: LEGACY-VVP-001
project: LEGAVIA
title: Legavia Verification and Validation Plan
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Verification and Validation Plan

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

## Scope, evidence and status semantics

The scenarios below are **design-only FVT seeds**, including eight preserved historical IDs. This PR must not install fake commands, mark them passed or cause automatic completion of functionalities. The GUI manifest has an intentionally empty `functionality_verification.tests` list. The separate machine catalog records future test intent. QA/SE shall later define executable Build/Setup/Exercise/Assertions/Cleanup for each test, fixture version, timeouts, target repository and pass/fail/blocked criteria.

## Candidate FVT suite

| ID | Scenario | Stimulus | Expected result | Linked functionalities |
|---|---|---|---|---|
| FVT-LEGACY-001 | Daily execution loop | Create linked goal + habit + task; complete from Today. | Item completion, milestone progress, XP, continuity, and analytics update exactly once. | LEGACY-FUNC-004, LEGACY-FUNC-007, LEGACY-FUNC-008 |
| FVT-LEGACY-002 | Goal map progression | Complete prerequisites across two themed phases. | Correct locked/available/in-progress/completed transitions; user can navigate with tap-only controls. | LEGACY-FUNC-003, LEGACY-FUNC-005 |
| FVT-LEGACY-003 | Missed-day recovery | Build history, miss scheduled action, reopen after inactivity. | Continuity degrades per rule but historical progress remains; recovery flow offers resume/reschedule/skip. | LEGACY-FUNC-006 |
| FVT-LEGACY-004 | Cross-module navigation | Navigate deeply in Health, switch to Finance, return to Health. | Per-destination state is preserved and top-level switch requires one tap/click. | LEGACY-FUNC-002 |
| FVT-LEGACY-005 | Authorization isolation | Create two users/family workspaces and shared/nonshared items. | Each account sees only authorized data; shared item visibility matches permission policy. | LEGACY-FUNC-001, LEGACY-FUNC-021 |
| FVT-LEGACY-006 | AI feature governance | Submit voice/text request, generate proposal, reject once, approve revised version. | No baseline promotion before explicit approval; all decisions are auditable. | LEGACY-FUNC-020 |
| FVT-LEGACY-007 | Learning import review | Import course links and intentionally alter extracted structure. | No extracted content becomes authoritative until user accepts/edits it. | LEGACY-FUNC-013 |
| FVT-LEGACY-008 | Accessibility/navigation audit | Run keyboard/touch/screen-reader checks across app shell and map. | WCAG 2.2 AA applicable checks pass; touch targets and drag alternatives meet requirements. | LEGACY-FUNC-002, LEGACY-FUNC-025 |
| FVT-LEGACY-009 | Water logging and correction | Fixture seeded for same-day readings and timezone transitions | Correct entry results in exact daily amount, with no duplicate on retry | LEGACY-FUNC-010 |
| FVT-LEGACY-010 | Focus timer and reward idempotence | Synthetic session state machine with pause/resume/cancel | Only eligible completed durations persist and award once | LEGACY-FUNC-011 |
| FVT-LEGACY-011 | Finance import and remittance accounting | Two-currency spreadsheet fixture with transfer and duplicate rows | Preview/confirmation mandatory; remittance counted once; exchange rate provenance preserved | LEGACY-FUNC-012 |
| FVT-LEGACY-012 | Reading finish estimate | Insufficient, irregular and steady reading observations | Estimate uses configured window; insufficient data and uncertain cases labeled | LEGACY-FUNC-014 |
| FVT-LEGACY-013 | Voice and AI confirmation | Mocked voice transcript and proposal response | No state change before review/approval; authorization enforced | LEGACY-FUNC-019 |
| FVT-LEGACY-014 | Movie recommendation and provenance | Recommendation plus unavailable/existing external ratings | Recommender/date retained and rating source explicit | LEGACY-FUNC-015 |
| FVT-LEGACY-015 | Game session retry safety | Pause/resume/stop/retry synthetic clock | Cumulative duration correct after repeated stop | LEGACY-FUNC-016 |
| FVT-LEGACY-016 | Memory media isolation | Two users, uploaded photo and note fixture | Signed media access and search observe tenant policy | LEGACY-FUNC-017 |
| FVT-LEGACY-017 | Family sharing revocation | Shared and private goal fixture with member removal | Visibility revoked server-side without affecting owner content | LEGACY-FUNC-021 |
| FVT-LEGACY-018 | Web/phone visual match | Approved references and deterministic viewport/fixture states | Phone and desktop critical journeys preserve behavior; differences reviewed | LEGACY-FUNC-002, LEGACY-FUNC-025 |
| FVT-LEGACY-019 | Backups and restoration | Isolated synthetic database corruption and restore fixture | Restore documentation and referential consistency confirmed | LEGACY-FUNC-024 |
| FVT-LEGACY-020 | Career proposal review | Completed-goal fixture with suggested CV entry | No CV write until manual approval | LEGACY-FUNC-023 |

## Verification methods by level

**Unit:** domain invariants (graph cycle prevention, completion/undo ledger, timezone, reward, finance accounting, estimation, timer arithmetic).

**Component/integration:** server authorization, persistence, connector import reconciliation, AI proposal/approval, materialized read views and retry behavior.

**E2E/FVT:** deterministic user journeys, mobile and desktop equivalence, real navigation, application reload and failure recovery. Use isolated synthetic users and fixtures only.

**Accessibility:** keyboard, focus, touch, screen reader semantics, contrast and reduced motion. Validate against applicable WCAG 2.2 AA and user-facing touch requirements.

**UX visual:** approved source-image or mockup capture at exact viewport with controlled fixture. Review human perceptual differences, not solely pixel metrics.

**Security:** cross-tenant negative API tests, private-media token access, admin least-privilege, connector revocation and sanitized logs. Recheck all affected boundaries after a domain change.

**Resilience/data:** corruption/restore simulation, migration/replay, event reprocessing and idempotent retries.

## Definition of done and release gates

1. Approved requirement/use case/functionality trace to bounded WP and target repos.
2. Architecture constraints accepted; code changes are implementation evidence, not acceptance by themselves.
3. Candidate-bound unit checks and independent test artifacts recorded in verification tooling.
4. Affected FVTs executed with controlled definitions and pass; blocked or absent evidence is not a pass.
5. Phone/desktop reference captures inspected with findings addressed or accepted deviation.
6. Security, privacy, accessibility and relevant data recovery checks pass.
7. SE accepts the WP; product owner explicitly authorizes promotion/release; GitHub PR/release provenance retained.

## Test seed ownership

SE owns scenario semantics, QA owns deterministic implementation/fixtures, UX reviews visual fidelity, Development can repair product code, Architecture validates design compliance. Failed verification may produce a finding and dependent WP, but cannot silently rewrite assertions.
