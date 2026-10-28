---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
artifact_id: LEGACY-WORK-006
artifact_type: work_package
---

# LEGACY-WORK-006 — Implement exactly-once completion and reward ledger

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

**Status:** Backlog  
**Type:** technical  
**Priority:** P1  
**Component capabilities:** LEGACY-CAP-004, LEGACY-CAP-003, LEGACY-CAP-002  
**Predecessors:** LEGACY-WORK-005  
**Target repositories:** matheusns/legacy_app, matheusns/legacy_verification_tooling

## Scope of work
Implement exactly-once completion and reward ledger. Changes shall follow approved requirements and architecture, not provisional assumptions.

## Acceptance criteria
- Atomic completion, XP award, map projection, undo and retry safety under two concurrent requests.
- Record trace from controlled requirements to changed implementation or review evidence.
- Preserve privacy and tenant-isolation behavior; attach candidate fingerprint and reviewer disposition.
- A current passing independent application unit-test run is mandatory.

## Done definition
Never infer Done from generated text or commit alone. This package is Done only when Systems Engineering records accepted candidate evidence in the GUI/control manifest.
