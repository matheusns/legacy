---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
artifact_id: LEGACY-WORK-007
artifact_type: work_package
---

# LEGACY-WORK-007 — Deliver first end-to-end journey and acceptance evidence

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

**Status:** Backlog  
**Type:** technical  
**Priority:** P0  
**Component capabilities:** LEGACY-CAP-002, LEGACY-CAP-003, LEGACY-CAP-004, LEGACY-CAP-005  
**Predecessors:** LEGACY-WORK-004, LEGACY-WORK-006  
**Target repositories:** matheusns/legacy_app, matheusns/legacy_verification_tooling

## Scope of work
Deliver first end-to-end journey and acceptance evidence. Changes shall follow approved requirements and architecture, not provisional assumptions.

## Acceptance criteria
- Representative phone/desktop end-to-end flow, privacy regression and persisted state after reload, with captures and FVT evidence.
- Record trace from controlled requirements to changed implementation or review evidence.
- Preserve privacy and tenant-isolation behavior; attach candidate fingerprint and reviewer disposition.
- A current passing independent application unit-test run is mandatory.

## Done definition
Never infer Done from generated text or commit alone. This package is Done only when Systems Engineering records accepted candidate evidence in the GUI/control manifest.
