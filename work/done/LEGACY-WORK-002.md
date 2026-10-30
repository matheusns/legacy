---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
artifact_id: LEGACY-WORK-002
artifact_type: work_package
---

# LEGACY-WORK-002 — Architecture decisions and secure domain skeleton

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

**Status:** Backlog  
**Type:** systems_engineering  
**Priority:** P0  
**Component capabilities:** LEGACY-CAP-001, LEGACY-CAP-003, LEGACY-CAP-004  
**Predecessors:** LEGACY-WORK-001  
**Target repositories:** matheusns/legacy

## Scope of work
Architecture decisions and secure domain skeleton. Changes shall follow approved requirements and architecture, not provisional assumptions.

## Acceptance criteria
- Accepted ADRs for identity/tenancy, source of truth, event idempotency, app stack, assets, hosting and testability.
- Record trace from controlled requirements to changed implementation or review evidence.
- Preserve privacy and tenant-isolation behavior; attach candidate fingerprint and reviewer disposition.
- Systems Engineering review and baseline identification are mandatory; no runtime unit-test requirement.

## Done definition
Never infer Done from generated text or commit alone. This package is Done only when Systems Engineering records accepted candidate evidence in the GUI/control manifest.
