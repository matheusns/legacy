---
artifact_id: WORK-013
status: Backlog
priority: P1
work_package_type: technical
---

# WORK-013 — Implement finance import and projections slice

**Owner/approval:** Systems Engineering (review required). **Target repositories:** matheusns/legacy_app, matheusns/legacy_verification_tooling. **Predecessors:** WORK-003, WORK-010, WORK-012. **Functionality links:** LEGACY-FUNC-012.

## Objective and constraints

Implement finance import and projections slice. This package is bounded by the ConOps, applicable requirements and accepted ADRs. No deployment or requirement promotion is implied by executing implementation work.

## Acceptance criteria

1. spreadsheet fixture import with duplicate and FX test.
2. monthly savings with transfer accounting.
3. forecasts labeled estimates.

## Verification and evidence

Obtain candidate-bound unit/integration evidence and independent tests from verification tooling. For responsive work include phone and desktop deterministic screenshot comparisons. Document security/privacy impacts.

## Exit gate

All predecessors accepted, acceptance criteria evidenced, relevant ADRs accepted, source and test candidate fingerprints recorded, independent review complete, and SE disposition set explicitly. Until then status remains Backlog/In Review/Blocked, not Done.
