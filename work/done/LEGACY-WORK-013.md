---
project: LEGAVIA
artifact_id: LEGACY-WORK-013
artifact_type: work_package
artifact_status: baseline-candidate
version: 0.1.1
date: 2026-11-02
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# LEGACY-WORK-013 — Adapt SDLC GUI application profiles and GitHub execution workflow

**Status:** Backlog  
**Type:** Technical  
**Priority:** P0  
**Depends on:** LEGACY-WORK-002, LEGACY-WORK-014, LEGACY-WORK-015  
**Target repositories:** matheusns/legavia_sdlc_gui, matheusns/legacy, matheusns/legacy_verification_tooling

## Required capabilities
- Replace hardcoded library/node/ROS scope projections with configuration-controlled web/mobile application-component and device-profile filters; keep validation of the canonical schema-2 `traceability/manifest.json` supported, and reject schema-1 inputs with explicit migration guidance rather than a silent fallback (disposition drafted in `docs/reviews/LEGACY-SE-REVIEW-003.md`, effective on human signature).
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

## Contract and verification prerequisite

LEGACY-WORK-014 owns resolution of the legacy/schema-2 compatibility conflict and complete registered verification coverage. Its drafted disposition (`docs/reviews/LEGACY-SE-REVIEW-003.md`) selects schema-2-only loading with explicit migration guidance; the compatibility wording above was reconciled to that draft and takes effect only when the record is signed. The registered suites `gui-checks` (gui), `control-checks` (control) and `tooling-fixture` (verification) cover this package's full allocation, but `gui-checks` and `control-checks` bind to wrapper scripts delivered by the technical predecessor LEGACY-WORK-015. This package remains pending until LEGACY-WORK-014 and LEGACY-WORK-015 are accepted and published, and until the readiness checklist in `docs/engineering/WP013_READINESS_CHECKLIST.md` is satisfied. Prepare a fresh prompt from the resulting baseline; do not resume the frozen failed run DEV-20261102T104129Z-8F4D14. The unit-test gate and the product execution gate remain in force; this reconciliation does not accept this package or any product requirement.

## Git publication

- Operator accepted the fingerprinted WP file set. The runner commits and pushes it after this disposition; publication status is tracked separately from approval.
