---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-11-14
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
artifact_id: LEGACY-WORK-016
artifact_type: work_package
---

# LEGACY-WORK-016 — Provision deterministic application UX capture fixtures

> Candidate prerequisite for LEGACY-WORK-004. This package does not grant approval of golden references.

**Type:** Technical · **Priority:** P0 · **Executor:** Development Agent
**Predecessor:** LEGACY-WORK-003 (Done)
**Writable repository:** `matheusns/legacy_app`
**Verification repository:** `matheusns/legacy_verification_tooling` (verify-only)
**Accepted architectural inputs:** ADR-001, ADR-004, ADR-005

## Why this package exists

LEGACY-WORK-004 repeatedly stopped during read-only analysis because the UX agent cannot create application API fixtures or edit the read-only control manifest. Its acceptance criterion nevertheless requires reproducible desktop and phone captures. Separate infrastructure and authenticated data setup from presentation work.

## Implementation scope

1. Reuse the existing `packages/testkit/scenarios/S2-first-journey.json` and `apps/api/src/cli/fixture-load.ts`. Do not modify the controlled scenario simply to make a screenshot look better. A new synthetic scenario requires explicit traceability.
2. Provide a local-only orchestration entry point for the application preview, API, isolated PostgreSQL fixture database, deterministic seed, readiness and teardown. A fixture loader must refuse non-local databases and production environments. Do not modify a developer's regular database or reuse their session.
3. Supply reproducible authentication using the existing sign-in route and fixture principal in an isolated test environment. Never add public or authentication-bypass routes for screenshots. Keep fixture secrets out of published screenshots, diagnostics and logs.
4. Register and test candidate-bound captures for Today, Map, Life, Insights and Me in desktop and phone browser profiles. Respect the browser harness's actual supported steps (click, fill, press) and its source fingerprint. Preserve stable clock, locale, timezone, browser settings and fixture identity/hash.
5. Produce a precise **control handoff** describing `application.preview` setup, `ux.screens[].fixture`, optional `steps` and `ready_selector`, their paths and verification commands. The control manifest is read-only to this technical work package; Systems Engineering must review and apply those changes separately before acceptance.
6. Add automated integration tests proving real authentication, candidate freshness, workspace isolation, screen readiness and clean failure when any capture prerequisite is missing.

## Acceptance criteria

- Local, disposable fixture setup can start, capture and clean up without touching live or operator data.
- The application renders all five screens from a consistent authenticated seed on both registered browser profiles.
- Actual capture reports identify the candidate source revision and deterministic fixture data.
- Negative cases cannot produce a false passing screenshot or bypass authentication.
- An explicit SE control update replaces placeholder fixture labels; verification evidence is reproduced against the resulting frozen configuration.
- Registered tests pass and independent review is recorded. **No model or test automatically approves visual golden references** (DEC-010).

## Completion rule

This technical package cannot be marked Done solely from a design proposal or successful sequential application unit tests. Require actual application + browser integration evidence, an applied controlled capture contract, independent review and operator acceptance.
