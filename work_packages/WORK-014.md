---
artifact_id: WORK-014
status: Backlog
priority: P1
work_package_type: technical
---

# WORK-014 — Implement focus, forest and reward session loop

**Owner/approval:** Systems Engineering (review required). **Target repositories:** matheusns/legacy_app, matheusns/legacy_verification_tooling. **Predecessors:** WORK-005, WORK-010, WORK-012. **Functionality links:** LEGACY-FUNC-011.

## Objective and constraints

Implement focus, forest and reward session loop. This package is bounded by the ConOps, applicable requirements and accepted ADRs. No deployment or requirement promotion is implied by executing implementation work.

## Acceptance criteria

1. timer resilient to pauses and retries.
2. Forest growth derives from valid sessions.
3. reward balance is ledger-based.

## Verification and evidence

Obtain candidate-bound unit/integration evidence and independent tests from verification tooling. For responsive work include phone and desktop deterministic screenshot comparisons. Document security/privacy impacts.

## Exit gate

All predecessors accepted, acceptance criteria evidenced, relevant ADRs accepted, source and test candidate fingerprints recorded, independent review complete, and SE disposition set explicitly. Until then status remains Backlog/In Review/Blocked, not Done.
