---
project: LEGAVIA
artifact_id: LEGACY-WORK-014
artifact_type: work_package
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-11-02
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# LEGACY-WORK-014 — Resolve GUI adaptation contract and verification prerequisites

**Status:** Backlog  
**Type:** Systems Engineering  
**Priority:** P0  
**Depends on:** LEGACY-WORK-002  
**Unblocks:** LEGACY-WORK-013  
**Target repository:** matheusns/legacy (control, write)  
**Executor:** architecture (Systems Engineering)

## Problem and evidence

Run DEV-20261102T104129Z-8F4D14 stopped in Analysis & Plan before implementation. At control 8e26087 / GUI 6e34c95 / verification 7b7973b, WP-013 allocates gui, control and verification, but only the verification-owned tooling-fixture suite is registered. The runner's full-allocation check therefore rejects the run. Its preflight-loaded manifest and frozen definition prevent an implementer from repairing that run by registering suites during execution.

WP-013 also requires existing-format/legacy-manifest support while the dedicated GUI fork rejects schema versions other than 2. Its migration note and adaptation handoff leave this compatibility disposition to Systems Engineering.

## Scope and deliverables

- Resolve the compatibility conflict explicitly. Evaluate schema 2 with controlled migration against direct backward compatibility; document the selected behavior, migration responsibilities, preserved IDs and validation evidence for human acceptance. This WP's creation does not approve either choice.
- Reconcile traceability/manifest.json, docs/work_packages/LEGACY-WORK-013.md and docs/engineering/ADAPTATION_HANDOFF.md with the reviewed disposition.
- Establish verification_execution.suites entries covering gui, control and verification with real commands and valid structured reports. Inspect runner suite selection by repository_id; source_repository_ids alone must not be mistaken for allocation coverage.
- Include native GUI Python/JS and mock GitHub tests, control business/manifest validation and independent harness checks. Define prerequisites, timeouts, fixture isolation, result paths, source provenance and profile applicability.
- Keep this execution control-only. If a usable adapter/report wrapper does not exist, create a separately allocated technical predecessor with mandatory tests and a viable verification bootstrap. Link it to WP-013 without depending on WP-013 or weakening its gate. Do not register nonexistent commands as ready.
- Supply a readiness checklist and evidence links for the next fresh WP-013 preparation. Preserve the failed run as historical evidence.

## Acceptance criteria

1. Record an explicit SE disposition of WP-013 legacy-manifest compatibility versus schema-2-only loading; synchronize the manifest, WP-013 document and adaptation handoff without silently waiving compatibility.
2. Define and register real deterministic verification suites for every non-read-only WP-013 repository (gui, control, verification), including GUI Python/JS and GitHub adapter regressions, control ingestion/validation, and harness checks.
3. Specify executable commands, prerequisites, source repository coverage, desktop/mobile applicability, schema-version-1 result reports and candidate freshness; tooling-fixture evidence must not imply product acceptance.
4. Demonstrate suite selection covers WP-013's full allocation before a fresh preparation. If adapters are missing, create separately allocated technical predecessor WPs with an executable verification bootstrap, link them to WP-013 and retain the blocker until they are accepted.
5. Record independent SE review and operator acceptance of the reconciled contract; retain WP-013's unit-test and product execution gates and require a fresh WP-013 prompt after prerequisite acceptance.

## Verification and completion boundary

Run python3 tools/validate_business_baseline.py and the GUI manifest validator against the proposed definition. Check dependency references and absence of cycles. Inspect the same selection logic used by create_unit_test_run for WP-013; record exact suite IDs and repositories. Exercise available registered commands with valid reports, and explicitly identify any execution pending a technical predecessor.

The SE unit-test gate is Not Applicable only because this WP changes controlled definitions, not executable adapters. It is not a waiver for WP-013 or any new technical predecessor. Independent architecture review and explicit operator acceptance remain required.

WP-014 may complete with explicitly mapped technical prerequisites, but WP-013 remains blocked until all of its predecessors are accepted and runnable suite coverage is demonstrated. Do not mark WP-013 Done, promote product requirements, remove application_execution_gate, claim tooling-fixture product acceptance, or resume the frozen failed run. After all prerequisites are accepted and published, update the workspace to main and generate a fresh WP-013 prompt.
