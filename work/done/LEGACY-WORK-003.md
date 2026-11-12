---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.1
date: 2026-11-09
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
artifact_id: LEGACY-WORK-003
artifact_type: work_package
---

# LEGACY-WORK-003 — Bootstrap web/mobile application and persistence

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

**Status:** Backlog  
**Type:** technical  
**Priority:** P0  
**Component capabilities:** LEGACY-CAP-001, LEGACY-CAP-005  
**Predecessors:** LEGACY-WORK-002, LEGACY-WORK-013

**Target repositories:** matheusns/legacy_app, matheusns/legacy_verification_tooling

## Scope of work
Bootstrap web/mobile application and persistence. Changes shall follow approved requirements and architecture, not provisional assumptions.

The secure domain skeleton in `docs/architecture/SECURE_DOMAIN_SKELETON.md` identifies ADR-001 through ADR-007 as inputs. Systems Engineering records the disposition for each decision and the skeleton in section 10 of `docs/reviews/LEGACY-SE-REVIEW-002.md`. Prepare a fresh development prompt after the accepted decisions are published.

## Application test contract

Deliver `scripts/report-app-tests.mjs` in `legacy_app` with the bootstrap. The runner executes the registered `app-unit` suite after implementation by running `node scripts/report-app-tests.mjs` in the application checkout. The initial scaffold will report the script as unavailable until this package delivers it.

The script must execute the candidate's real domain, API and account-isolation tests and write a schema-version-1 JSON report to `SDLC_RESULT_PATH`. Report one uniquely named case per test with its observed outcome and duration. Return a nonzero exit for a failed check, missing dependency, report error or discovery with no executed tests. Keep transient output in `SDLC_ARTIFACT_DIR` or ignored paths so verification preserves the candidate fingerprint. The independent runner also selects `tooling-fixture` for the verification checkout. That suite exercises the harness itself.

## Acceptance criteria
- Reproducible local startup and CI; isolated accounts; secured CRUD API; deterministic fixtures and unit tests.
- Record trace from controlled requirements to changed implementation or review evidence.
- Preserve privacy and tenant-isolation behavior; attach candidate fingerprint and reviewer disposition.
- A current passing independent application unit-test run is mandatory.

## Done definition
Never infer Done from generated text or commit alone. This package is Done only when Systems Engineering records accepted candidate evidence in the GUI/control manifest.

## Git publication

- Operator accepted the fingerprinted WP file set. The runner commits and pushes it after this disposition; publication status is tracked separately from approval.
