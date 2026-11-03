---
project: LEGAVIA
artifact_id: LEGACY-SE-REVIEW-003
artifact_type: se_review_record
artifact_status: review-draft-unsigned
version: 0.1.0
date: 2026-11-02
control_repository: matheusns/legacy
work_package: LEGACY-WORK-014
run_id: DEV-20261102T140805Z-55D5A4
reviewed_control_commit: a5d7d0d84a17b6a63015042d37fe685af1d39d8b
reviewed_gui_commit: d34d8d8690eecd8294b9b4b44698c4d56fbbc6cc
reviewed_verification_commit: 7b7973b6dd463a5a050695eb34288fad52d749ee
review_gate: Human Systems Engineering signature required
---

# LEGACY-SE-REVIEW-003 — Compatibility disposition and verification coverage for the GUI adaptation (LEGACY-WORK-014)

> **Unsigned draft.** Prepared by the Systems Engineering control-plane agent for LEGACY-WORK-014. It proposes a disposition of the WP-013 compatibility conflict, registers bootstrap verification suites and defines one technical predecessor; it grants nothing. No work package changes status, no requirement is promoted, no suite is "ready" because it is registered, and nothing here is execution evidence for any product FVT. The disposition in section 3 takes effect only when a human Systems Engineering reviewer completes section 10 and the control change is committed by a human-controlled action.

## 1. Baseline identification

| Item | Value |
| --- | --- |
| Work package | `LEGACY-WORK-014` — Resolve GUI adaptation contract and verification prerequisites (P0, systems_engineering, Backlog) |
| Predecessor | `LEGACY-WORK-002` — recorded `Done` in `traceability/manifest.json`; its review record `LEGACY-SE-REVIEW-002` is still an unsigned draft and ADR-001..007 read `Proposed` (see finding SE3-F-007) |
| Control repository revision | `matheusns/legacy` `main` @ `a5d7d0d84a17b6a63015042d37fe685af1d39d8b`, clean working tree before this run |
| Frozen source integrity (run context) | `docs/work_packages/LEGACY-WORK-014.md` = `cc884e8f70dcaaa89c09ccb77b472f736c235fbc7d426fdbd94a8f3ef2e124ae` (unchanged by this run); `traceability/manifest.json` = `f525f4901536d893c21c244e9c4d5ed20dfc4b78eca4f70498341a851a1a242a` before the proposed change |
| Sibling repositories (read-only, unchanged) | `legavia_sdlc_gui` @ `d34d8d86`, `legacy_app` @ `0abe8fd6`, `legacy_mockups` @ `ca2e9dbf`, `legacy_verification_tooling` @ `7b7973b6`; all four working trees clean after the run |
| Prior runs on this package | `DEV-20261102T130156Z-86A592` (Codex, blocked by a container sandbox failure, no content); the WP-013 run `DEV-20261102T104129Z-8F4D14` is preserved as historical evidence and is not resumed |
| Business baseline before/after | 129 requirements, 15 capabilities, 35 use cases, 24 planned FVTs; 14 work packages before, 15 after (LEGACY-WORK-015 added) |

### 1.1 Candidate fingerprint of proposed artifacts (SHA-256 at end of run)

| File | Change | SHA-256 |
| --- | --- | --- |
| traceability/manifest.json | modified | `9caa3824ccd5a2c121586cb8d9752d565940710678b3c1389575fc8971cb9318` |
| docs/work_packages/LEGACY-WORK-013.md | modified (v0.1.1) | `de7231b016ec4a59dfb1998efb86c0e7f08131c06d572b469bf898460e3c2838` |
| docs/work_packages/LEGACY-WORK-015.md | new | `1d99004f4dd0070e4dd625ad09d3fce59eb2b569e10e668cad4a4ad468eb0e18` |
| docs/engineering/WP013_READINESS_CHECKLIST.md | new | `62d2bf6f1cfa062690d988b6c78224ffefa0e5fe9cec63fe1d77d63fb1728b99` |
| docs/engineering/ADAPTATION_HANDOFF.md | modified | `0c22f4facd585e362f679baa820444786aab3487003ab9413dbb5878a3da6595` |
| docs/engineering/WORKFLOW.md | modified | `d0077eeba1e04b6d7f92ee97e7da18d31f3aafc3d8895adf0b71e2c92bb7d4a5` |
| docs/business/TRACEABILITY_AND_GUI.md | modified (v0.1.1) | `eeab80b3a2cb1f6f8911bec315ca90766a6c2b04005315b69a2664d41684be97` |
| docs/work_packages/LEGACY-WORK-014.md | unchanged | `cc884e8f70dcaaa89c09ccb77b472f736c235fbc7d426fdbd94a8f3ef2e124ae` |
| traceability/business_baseline.json | unchanged | `519f0aae390df4b8116d74a9dee453ff96b3b5de93d11eb6da95c018f3e52abd` |

Any edit after signature invalidates the signature for that file and requires a new review record version.

## 2. Problem verified at the reviewed heads

1. **Coverage rule.** `legavia_sdlc_gui/src/sdlc_gui/qa.py` (`create_unit_test_run`) derives the expected repository set from a Work Package's non-`read_only` allocation and raises `Work Package test execution must cover its full repository allocation` when the selected suites' `repository_id` set differs. Before this run only `tooling-fixture` (`repository_id: verification`) was registered, so WP-013 (gui, control, verification all `write`) could never pass the runner's registered-check stage. Selection is by `repository_id`; `source_repository_ids` only extend freshness fingerprinting and do not count as coverage.
2. **Schema conflict.** `legavia_sdlc_gui/src/sdlc_gui/project.py` raises `Legavia requires engineering manifest schema_version 2; migrate the project contract before loading it` for any other version, and `tests/test_project_contract.py` locks that behaviour. WP-013 still required "preserve ability to read existing manifest format" and "legacy manifest validation remains supported", deferring the choice to Systems Engineering. The canonical `traceability/manifest.json` is already schema 2 and no schema-1 manifest exists in the control repository.
3. **No structured-report wrapper.** The GUI's native checks (`PYTHONPATH=src python -m unittest discover -s tests`, `node --test tests/test_*.js`) emit no schema-version-1 report; `execution.read_report` requires one, and the JUnit mode reads only XML inside the per-run artifact directory. The control repository has no reporting wrapper either. Only `legacy_verification_tooling/harness/verify-fixture.cjs` writes a correct report to `SDLC_RESULT_PATH`.
4. **Preparation does not pre-check suite readiness.** `development.py` never calls `command_readiness`; readiness is evaluated when a verification run is created. A technical package can therefore be prepared and executed while its suites' wrapper files are produced during the run, which resolves the bootstrap circularity honestly.

## 3. Compatibility disposition (proposed)

### Option A — schema-2-only loading with explicit migration (recommended)

The GUI loads engineering manifest schema 2 only. Any other `schema_version` is rejected with the explicit migration message already implemented; there is no silent fallback and no partial read. "Existing manifest format" is satisfied because the only controlled manifest, `traceability/manifest.json`, is schema 2 and every issued ID, requirement statement, status, dependency, acceptance criterion and target-repository reference was preserved during the migration (GUI `docs/ADAPTATION_VALIDATION.md`). Migration of any future schema-1 input is an explicit, reviewed control change, not a loader behaviour.

Evidence for A: `docs/business/TRACEABILITY_AND_GUI.md` and the GUI's `ADAPTATION_VALIDATION.md` and `WEBSITE_PHONE_ADAPTATION_PLAN.md` already describe this behaviour as the approved dedicated-fork plan; the loader test locks it; the control validator and the GUI ingestion pass on the schema-2 manifest (section 6).

### Option B — add a schema-1 read path (evaluated, not recommended)

Add a compatibility branch in `project.py` that accepts `schema_version: 1`, synthesises default components/profiles, and relaxes `tests/test_project_contract.py`. Rejected because it contradicts the approved dedicated-fork plan and the two control documents above, widens WP-013's scope with a code path that no controlled input exercises, reintroduces the historical ROS/GitLab executor assumptions that schema 1 carried, and would make a loader "success" on an unmigrated input indistinguishable from a reviewed migration.

### Reconciliation applied (effective on signature)

- `docs/work_packages/LEGACY-WORK-013.md` required capability 1 now reads "keep validation of the canonical schema-2 `traceability/manifest.json` supported, and reject schema-1 inputs with explicit migration guidance rather than a silent fallback"; `Depends on` adds LEGACY-WORK-015; the prerequisite section cites this record, the registered suites and the readiness checklist; version 0.1.1.
- `traceability/manifest.json` `work_packages[LEGACY-WORK-013]`: `acceptance_criteria[0]` tail rewritten to the same meaning, `migration_note` extended, `depends_on` adds `LEGACY-WORK-015`. Status (`Backlog`), `unit_test_gate.required` (`true`), `repository_ids`/`repository_access`, `target_repositories` and `executor_agent_id` are unchanged.
- `docs/engineering/ADAPTATION_HANDOFF.md`, `docs/engineering/WORKFLOW.md` and `docs/business/TRACEABILITY_AND_GUI.md` (v0.1.1) point at this record instead of leaving the disposition open.

Compatibility is not waived: the obligation moves from "the loader reads old inputs" to "old inputs are migrated under review and the loader refuses them otherwise", and the WP-013 acceptance test for this criterion is the existing loader test plus the control ingestion check in `control-checks`.

## 4. Registered verification suites (proposed)

| Suite | Repository (`repository_id`) | Kind | Command | Required paths | Source coverage | Profiles | Report | Timeout |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `gui-checks` | gui | unit | `{python} tools/report_checks.py` | `tools/report_checks.py`, `src/sdlc_gui`, `tests` | gui | none (desktop/mobile not applicable; label states it) | `result.json`, schema 1 | 900 s (proposed, unmeasured) |
| `control-checks` | control | unit | `{python} tools/report_control_checks.py` | `tools/report_control_checks.py`, `tools/validate_business_baseline.py`, `traceability/manifest.json`, `traceability/business_baseline.json` | control, gui (ingestion imports the GUI package) | none | `result.json`, schema 1 | 300 s (proposed) |
| `tooling-fixture` | verification | integration | `node harness/verify-fixture.cjs` | `harness/verify-fixture.cjs`, `node_modules/playwright` | verification | desktop-browser, mobile-browser (emulated) | `result.json`, schema 1 | 120 s (unchanged) |

Contract notes: all three satisfy `execution.suites()` validation (unique IDs, declared repositories, argv commands, declared source/component/profile IDs, no metric budgets). `component_ids` is empty for the two new suites because no declared component represents the workbench itself; adding a `workbench` component is a separate control decision (SE3-F-004). Commands receive `SDLC_ARTIFACT_DIR`, `SDLC_RESULT_PATH`, `SDLC_RUN_ID` and `SDLC_SUITE_ID`; reports must contain one case per real test with `passed|failed|error|skipped` and finite durations; an empty report, nonzero exit, timeout or invalid JSON cannot pass. Candidate freshness: the source snapshot of each suite's `repository_id` plus `source_repository_ids` is fingerprinted at request time and re-checked after execution; any change stales the evidence. Fixture isolation: wrappers write only under the artifact directory or Git-ignored paths. Browser smoke tests of the GUI are deliberately not registered (their `NODE_PATH` prerequisite lives in a sibling repository and cannot be declared through confined `required_paths`). `tooling-fixture` evidence remains tooling evidence and implies no product acceptance.

Deviation from the analysis plan: `control-checks.source_repository_ids` includes `gui` as well as `control`, because the ingestion step executes GUI code and its evidence must go stale when the GUI changes.

## 5. Technical predecessor LEGACY-WORK-015 (proposed)

Defined in `docs/work_packages/LEGACY-WORK-015.md` and `traceability/manifest.json`: technical, P0, Backlog, executor `development`, `depends_on` = [`LEGACY-WORK-002`] only (never WP-013), `repository_ids` = [gui, control] with `write` access, capabilities LEGACY-CAP-001/005, components identity-access/app-shell, profiles desktop-browser/mobile-browser, `unit_test_gate.required: true`, no `execution_contract` (so no demo/FVT contract is demanded, as for WP-013). Deliverables are the two wrappers with unit tests, standard library only, no Work Package IDs in product source, CI unchanged. WP-013 depends on it; it does not depend on WP-013, so no cycle exists (validator confirms).

## 6. Checks performed and recorded outputs

| Check | Command | Result |
| --- | --- | --- |
| Business baseline validator (before) | `python3 tools/validate_business_baseline.py` | `Valid candidate baseline: 129 requirements, 15 capabilities, 35 use cases, 24 planned FVTs, 14 work packages; all links resolved.` |
| Business baseline validator (after) | same | `Valid candidate baseline: 129 requirements, 15 capabilities, 35 use cases, 24 planned FVTs, 15 work packages; all links resolved.` (dependency-cycle check included) |
| Control unit tests | `python3 -m unittest discover -s tools -p 'test_*.py'` | `Ran 7 tests … OK` |
| GUI ingestion of the proposed manifest | `PYTHONPATH=../legavia_sdlc_gui/src python3 -m sdlc_gui.cli --manifest traceability/manifest.json --validate-only` | exit 0, `Valid manifest` |
| Suite selection reproduction (read-only; `suites()`, the `create_unit_test_run` filter and `command_readiness` only; no runtime files written) | script kept outside the repository | see below |
| Protected-field audit of the manifest diff | `git diff` filtered for `status`, `review`, `approval`, `application_execution_gate` | only the new WP-015 `"status": "Backlog"` line; no transition, no review/approval field, gate unchanged |
| Product repository audit | `git status --porcelain` in gui, app, ux, verification | all clean at the frozen baseline commits |

Selection reproduction at the proposed manifest:

```
registered suites: gui-checks (gui, unit), control-checks (control, unit), tooling-fixture (verification, integration)
LEGACY-WORK-013: expected {control, gui, verification}; selected gui-checks, control-checks, tooling-fixture -> coverage satisfied: True
  gui-checks:      available=false  reason="Registered prerequisite is unavailable: tools/report_checks.py"
  control-checks:  available=false  reason="Registered prerequisite is unavailable: tools/report_control_checks.py"
  tooling-fixture: available=true   working_directory=…/legacy_verification_tooling
LEGACY-WORK-015: expected {control, gui}; selected gui-checks, control-checks -> coverage satisfied: True (same two readiness reasons)
LEGACY-WORK-014: expected {control}; selected control-checks -> coverage satisfied: True (not executed: SE runs skip the registered-check stage)
```

The two `available=false` results are the intended retained blocker, not a defect: the registration proves coverage; executability arrives with LEGACY-WORK-015. Host observations only: `node` v22.23.4 and `node_modules/playwright` are present on this host, so `tooling-fixture` is available here; it was not executed by this run. No `sdlc-gui` console script is installed on this host; ingestion used `PYTHONPATH`.

## 7. Findings

### SE3-F-001 — Registering suites with future wrapper paths is the only honest bootstrap (Condition)

Registering `gui-checks`/`control-checks` without the wrappers is required because the runner refuses definition changes after a prompt is frozen and WP-015's own acceptance run must cover gui and control. The GUI will show both suites as unavailable until WP-015 lands. **Condition:** nobody may read the registration as readiness; the checklist item 5 requires the GUI to report them available before WP-013 is prepared.

### SE3-F-002 — `control-checks` depends on the GUI package being importable (Condition)

The wrapper resolves the GUI path from `repositories[gui].path`; if the sibling checkout or `sys.path` extension fails, the suite must report an `error` case and exit nonzero. **Condition:** WP-015 acceptance criterion 2 enforces this; the operator's host must keep the five-sibling layout.

### SE3-F-003 — Timeouts are proposed, not measured (Observation)

The GUI Python suite last recorded 443 tests; durations on the operator host are unknown. WP-015 records the measured durations of its first full run; SE confirms or revises `timeout_seconds` afterwards through a control change.

### SE3-F-004 — No declared component represents the workbench (Observation)

`components[]` has no entry for the GUI itself, so both new suites declare `component_ids: []`. If component-level filtering of GUI evidence is wanted, add a `workbench` component in a separate control change; do not reuse product components for tooling.

### SE3-F-005 — WP-013 acceptance wording changed under SE authority (Condition)

Rewriting a candidate acceptance criterion is within the SE drafting boundary, but it is an acceptance-contract change. The `architecture_review` stage may prefer Option B; both options are recorded with evidence. **Condition:** signature in section 10 selects one; if B is selected, revert the WP-013 wording and plan the loader change inside WP-013 or a new technical predecessor.

### SE3-F-006 — Dashboard counts and roadmap table are stale (Observation, out of scope)

`traceability/manifest.json` `dashboard.counts.work_packages` still reads 13 (now 15 packages exist; the GUI recomputes counts on load, so ingestion is unaffected); `docs/business/DELIVERY_ROADMAP.md` lists WP-013 with only LEGACY-WORK-002 as predecessor and omits WP-014/015; `work/done/LEGACY-WORK-002.md` still says `Status: Backlog`. These are fingerprinted or generated records and are left for a separate control change.

### SE3-F-007 — LEGACY-WORK-002 is `Done` while its review record is unsigned (Observation, carried from SE2-F-001)

ADR-001..007 read `Proposed`, `LEGACY-SE-REVIEW-002` is unsigned and `adr_ids` is empty, so ADR-005's report/suite guidance is non-binding; the suites here follow `execution.py`'s actual contract (which does not accept ADR-005's `inconclusive` status). The dependency of WP-014 on WP-002 is satisfied in the manifest only.

### SE3-F-008 — Policy references a missing decision file (Observation)

The frozen policy names `work/decisions/engineering_decisions.md`, which does not exist; zero decisions and zero ADRs were compiled. No active decision constrained this package; create the file or correct the reference in a separate control change.

## 8. Coverage of the LEGACY-WORK-014 acceptance criteria

| Criterion | Proposed evidence | Human action still required |
| --- | --- | --- |
| 1. Explicit SE disposition; synchronise manifest, WP-013 and handoff without silently waiving compatibility | Section 3; WP-013 v0.1.1; manifest WP-013 record; ADAPTATION_HANDOFF.md; TRACEABILITY_AND_GUI.md v0.1.1 | Sign section 10 |
| 2. Real deterministic suites for gui, control, verification incl. GUI Python/JS and GitHub adapter regressions, control ingestion/validation, harness checks | Section 4; `verification_execution.suites` (`gui-checks` runs the full GUI discovery, which includes `tests/test_github.py`; `control-checks` runs validator, control tests and GUI ingestion; `tooling-fixture` unchanged) | Accept; executability pending WP-015 |
| 3. Commands, prerequisites, source coverage, desktop/mobile applicability, schema-1 reports, candidate freshness; fixture evidence not product acceptance | Section 4 notes; WP-015 deliverables; checklist footer | Accept |
| 4. Demonstrate full-allocation coverage; predecessor with executable bootstrap linked to WP-013; blocker retained | Section 6 reproduction; section 5; WP-013 `depends_on`; readiness `available=false` retained | Accept; prepare WP-015 |
| 5. Independent SE review and operator acceptance; retain WP-013 gates; fresh WP-013 prompt | `architecture_review` stage of this run; section 10; WP-013 `unit_test_gate` and `application_execution_gate` unchanged; checklist item 10 | Review, then accept WP-014 |

## 9. Proposed control actions after signature (not applied by this run)

1. Human-controlled commit of the files in section 1.1 to `main` (publication after WP-014 acceptance may be runner-owned per `work_package_publication`).
2. Register this record in `traceability/manifest.json` `artifacts[]` as `{ "id": "LEGACY-SE-REVIEW-003", "type": "review_record", "scope": "all", "status": "Signed", "path": "docs/reviews/LEGACY-SE-REVIEW-003.md", "title": "SE disposition of GUI adaptation compatibility and verification coverage" }` together with the still-missing REVIEW-001/002 entries.
3. Prepare LEGACY-WORK-015 (development role, gui+control write); after its acceptance and publication, run `docs/engineering/WP013_READINESS_CHECKLIST.md` and prepare a fresh LEGACY-WORK-013 prompt.
4. Separate control change for SE3-F-003 (timeouts), SE3-F-004 (optional `workbench` component), SE3-F-006 (dashboard counts, roadmap, work/done wording), SE3-F-007/008 (WP-002 evidence, decision file).

## 10. Signature

| Role | Name | Decision (Option A / Option B / Reject / Defer) | Suites and WP-015 (Accept / Revise) | Date | Reviewed commit |
| --- | --- | --- | --- | --- | --- |
| Systems Engineering owner | | | | | `a5d7d0d84a17b6a63015042d37fe685af1d39d8b` |

Unsigned. Prepared by the Systems Engineering control-plane agent in run DEV-20261102T140805Z-55D5A4 (Claude Fable 5.1, Claude Code). The agent did not and may not accept its own work.
