---
artifact_id: WORK-008
status: Backlog
priority: P0
work_package_type: technical
---

# WORK-008 — Implement water tracking and user-configured targets

**Owner/approval:** Systems Engineering (review required). **Target repositories:** matheusns/legacy_app, matheusns/legacy_verification_tooling. **Predecessors:** WORK-003, WORK-006. **Functionality links:** LEGACY-FUNC-010.

## Objective and constraints

Implement water tracking and user-configured targets. This package is bounded by the ConOps, applicable requirements and accepted ADRs. No deployment or requirement promotion is implied by executing implementation work.

## Acceptance criteria

1. water log correctable.
2. daily sums timezone-aware.
3. phone quick add and desktop UI covered.

## Verification and evidence

Obtain candidate-bound unit/integration evidence and independent tests from verification tooling. For responsive work include phone and desktop deterministic screenshot comparisons. Document security/privacy impacts.

## Exit gate

All predecessors accepted, acceptance criteria evidenced, relevant ADRs accepted, source and test candidate fingerprints recorded, independent review complete, and SE disposition set explicitly. Until then status remains Backlog/In Review/Blocked, not Done.
