---
project: LEGAVIA
artifact_id: LEGACY-WORK-013
artifact_type: work_package
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# LEGACY-WORK-013 — Adapt SDLC GUI application profiles and GitHub execution workflow

**Status:** Backlog  
**Type:** Technical  
**Priority:** P0  
**Depends on:** LEGACY-WORK-002  
**Target repositories:** matheusns/legavia_sdlc_gui, matheusns/legacy, matheusns/legacy_verification_tooling

## Required capabilities
- Replace hardcoded library/node/ROS scope projections with configuration-controlled web/mobile application-component and device-profile filters; preserve ability to read existing manifest format.
- Present ConOps, use cases, requirement catalogs, controlled references and bidirectional links from `traceability/business_baseline.json` and `traceability/manifest.json` without duplicating their authority in GUI state.
- Implement GitHub PR/status/review-provider integration; no GitLab provider default for Legavia runs.
- Register safe app build/unit, browser UX and independent integration adapters; no unregistered command execution.
- Include UX Preview evidence: reference version, app candidate, viewport, artwork version, screenshot and independently reviewed diff.
- Keep Systems Engineering acceptance, candidate fingerprints, CI failures, rollback and freshness invalidation explicit.

## Acceptance criteria
1. GUI displays real Legavia component and target-profile filters; it does not label a web module as a ROS 2 node.
2. At least one candidate requirement → capability → Work Package → FVT path is navigable, including source ConOps/use-case details.
3. GitHub PR/check state and branch provenance are visible for a synthetic sandbox test without requiring production tokens in fixtures.
4. Unit, browser and integration runner contracts execute deterministically with clean fixtures and candidate/version fingerprints.
5. Independent GUI Python/JS regression tests and a simulated application acceptance workflow pass.

## Gate
The GUI's current read-only manifest import is available, but **Development/QA/Preview activation is blocked** until this package is accepted. This package itself requires a passing candidate-bound unit test gate and Systems Engineering review.
