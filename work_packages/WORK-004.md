---
artifact_id: WORK-004
status: Backlog
priority: P0
work_package_type: technical
---

# WORK-004 — Implement shared goals, milestones and task persistence

**Owner/approval:** Systems Engineering (review required). **Target repositories:** matheusns/legacy_app, matheusns/legacy_verification_tooling. **Predecessors:** WORK-003. **Functionality links:** LEGACY-FUNC-003, LEGACY-FUNC-004.

## Objective and constraints

Implement shared goals, milestones and task persistence. This package is bounded by the ConOps, applicable requirements and accepted ADRs. No deployment or requirement promotion is implied by executing implementation work.

## Acceptance criteria

1. create/edit task and goal stable across reload.
2. manual task visible on Today.
3. relationship invariants tested.

## Verification and evidence

Obtain candidate-bound unit/integration evidence and independent tests from verification tooling. For responsive work include phone and desktop deterministic screenshot comparisons. Document security/privacy impacts.

## Exit gate

All predecessors accepted, acceptance criteria evidenced, relevant ADRs accepted, source and test candidate fingerprints recorded, independent review complete, and SE disposition set explicitly. Until then status remains Backlog/In Review/Blocked, not Done.
