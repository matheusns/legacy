---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
artifact_id: LEGACY-WORK-004
artifact_type: work_package
---

# LEGACY-WORK-004 — Implement responsive shell and UX references

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

**Status:** Backlog  
**Type:** technical  
**Priority:** P1  
**Component capabilities:** LEGACY-CAP-005, LEGACY-CAP-002  
**Predecessors:** LEGACY-WORK-003  
**Target repositories:** matheusns/legacy_app, matheusns/legacy_mockups, matheusns/legacy_verification_tooling

## Scope of work
Implement responsive shell and UX references. Changes shall follow approved requirements and architecture, not provisional assumptions.

## Acceptance criteria
- Today/Map/Life/Insights/Me shell and Auto/Mobile/Desktop switch remain functional; capture candidate desktop and phone screenshots using the registered product preview for owner and UX-reviewer disposition.
- Golden references remain unapproved until the owner and UX reviewer record DEC-010 and pin provenance-backed immutable reference revisions. Candidate captures must not be interpreted as approved visual baselines.
- Record trace from controlled requirements to changed implementation or review evidence.
- Preserve privacy and tenant-isolation behavior; attach candidate fingerprint and reviewer disposition.
- A current passing independent application unit-test run is mandatory.

## Done definition
Never infer Done from generated text or commit alone. This package is Done only when Systems Engineering records accepted candidate evidence in the GUI/control manifest.

## Implementation readiness notes (candidate change)

The UX agent's `app` write allowlist is restricted to web presentation and design-token paths. It does not authorize changes to API, authentication, drafts, or domain contracts. `Surfaces.tsx` also contains data-loading code; changes there must remain presentation-only, and review must flag edits to authorization or API behavior.

The manifest registers the real Vite web preview; this does not itself establish a deterministic authenticated screen fixture or an approved golden reference. Screens without pinned approved references can produce **candidate** captures only. The owner and UX reviewer must resolve DEC-010 and provenance before visual baseline acceptance. Goal/Island detail and Focus screen registration remains a separate Systems Engineering scope decision under SE-F-007; do not invent a Focus route or declare it implemented.
