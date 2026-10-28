---
artifact_id: WORK-005
status: Backlog
priority: P0
work_package_type: technical
---

# WORK-005 — Implement exactly-once completion/undo ledger

**Owner/approval:** Systems Engineering (review required). **Target repositories:** matheusns/legacy_app, matheusns/legacy_verification_tooling. **Predecessors:** WORK-004. **Functionality links:** LEGACY-FUNC-007, LEGACY-FUNC-008.

## Objective and constraints

Implement exactly-once completion/undo ledger. This package is bounded by the ConOps, applicable requirements and accepted ADRs. No deployment or requirement promotion is implied by executing implementation work.

## Acceptance criteria

1. concurrent repeat does not double issue XP.
2. undo reverses only own contribution.
3. integration tests cover retries.

## Verification and evidence

Obtain candidate-bound unit/integration evidence and independent tests from verification tooling. For responsive work include phone and desktop deterministic screenshot comparisons. Document security/privacy impacts.

## Exit gate

All predecessors accepted, acceptance criteria evidenced, relevant ADRs accepted, source and test candidate fingerprints recorded, independent review complete, and SE disposition set explicitly. Until then status remains Backlog/In Review/Blocked, not Done.
