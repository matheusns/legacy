---
project: LEGAVIA
artifact_id: LEGACY-WORK-015
artifact_type: work_package
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-11-02
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# LEGACY-WORK-015 — Deliver schema-version-1 report wrappers for the GUI and control verification suites

**Status:** Backlog  
**Type:** Technical  
**Priority:** P0  
**Depends on:** LEGACY-WORK-002  
**Unblocks:** LEGACY-WORK-013 (together with LEGACY-WORK-014)  
**Target repositories:** matheusns/legavia_sdlc_gui (gui, write), matheusns/legacy (control, write)  
**Executor:** development

## Problem and evidence

LEGACY-WORK-014 registered the verification suites `gui-checks` and `control-checks` in `traceability/manifest.json` so that a WP-013 acceptance run can cover its full gui/control/verification allocation. Both suites bind to wrapper scripts that do not exist yet:

- `legavia_sdlc_gui/tools/report_checks.py` — the GUI's native checks are `PYTHONPATH=src python -m unittest discover -s tests` and `node --test tests/test_*.js` (README, `.github/workflows/tests.yml`). Neither emits the schema-version-1 JSON report that `sdlc_gui.execution.read_report` requires, and the JUnit mode only reads XML under the per-run artifact directory, which an argv command cannot target without a wrapper.
- `legacy/tools/report_control_checks.py` — the control repository has only `tools/validate_business_baseline.py`, its unittest file and `tools/test_codex_model_configuration.py`; none writes a structured report.

Until these wrappers exist, `command_readiness` reports `Registered prerequisite is unavailable` for both suites. That is the intended retained blocker recorded in `docs/reviews/LEGACY-SE-REVIEW-003.md`; it must not be read as readiness. This package is the separately allocated technical predecessor that makes the registered commands executable.

## Scope and deliverables

### gui: `tools/report_checks.py`

1. Run, from the GUI repository root, `python -m unittest discover -s tests` with `PYTHONPATH=src` and `node --test tests/test_*.js` (expanded by the wrapper, not a shell). Use `sys.executable` for Python and `node` from `PATH`; record the resolved versions in `metrics` or `artifacts`.
2. Parse real results into one report case per executed test: unique `name` (module/class/method or JS test name), `status` one of `passed`, `failed`, `error`, `skipped`, finite nonnegative `duration_seconds`, and a bounded `message` for non-passing cases. Use a machine-readable source (for example a `unittest` result object driven in-process or the `node --test` TAP/spec output) rather than scraping summary lines.
3. Write `{"schema_version": 1, "tests": [...], "metrics": {...}, "artifacts": [...]}` to `$SDLC_RESULT_PATH` (fall back to `test-results/gui-checks.json` under the current directory when unset). Keep all generated files inside `$SDLC_ARTIFACT_DIR` or Git-ignored paths.
4. Exit 1 when any case is `failed` or `error`, when either runner cannot start, or when zero tests were discovered. Never emit synthetic passing cases; a runner that cannot start must appear as an `error` case naming the runner.
5. Add unit tests (`tests/test_report_checks.py`) covering: report schema and uniqueness, status mapping for pass/fail/error/skip, nonzero exit on failure, missing `node` reported as an error case, and that the report is written to `SDLC_RESULT_PATH`. Keep `.github/workflows/tests.yml` running the plain commands; do not make CI depend on the wrapper.

### control: `tools/report_control_checks.py`

1. Run, from the control repository root: `tools/validate_business_baseline.py` as a subprocess (the module validates on import); `python -m unittest discover -s tools -p "test_*.py"`; and the GUI ingestion `python -m sdlc_gui.cli --manifest traceability/manifest.json --validate-only` with `sys.path`/`PYTHONPATH` extended by `<gui repository path>/src`, where the GUI path is resolved from `repositories[].path` of the manifest (`../legavia_sdlc_gui`).
2. Emit the same schema-version-1 report to `$SDLC_RESULT_PATH`: one case for the validator, one per unittest case, one for GUI ingestion. If the `sdlc_gui` package cannot be imported, record an `error` case `gui-ingestion: sdlc_gui unavailable` and exit 1; never skip silently.
3. Add `tools/test_report_control_checks.py` covering the schema, the error mapping for a failing validator, a missing GUI package, and the result path contract.
4. Do not introduce third-party dependencies in either wrapper (standard library only, consistent with `validate_business_baseline.py`).

### Common constraints

- No Work Package ID or run ID in product source, wrapper code, test names or PR titles; cite them only in control documents and manifest records.
- Do not register browser smoke tests (`tests/browser_*.cjs`) in these suites: they need `NODE_PATH=../legacy_verification_tooling/node_modules`, and `required_paths` are confined to the suite's working directory, so the prerequisite cannot be declared truthfully.
- Do not modify `tooling-fixture`, the `application_execution_gate`, any Work Package status, or LEGACY-WORK-013's acceptance criteria.
- The suite registrations in `traceability/manifest.json` are owned by Systems Engineering (LEGACY-WORK-014). If the implementation needs a different command, path, environment or timeout, report the deviation; the control change is reviewed separately.
- `timeout_seconds` values (900 for `gui-checks`, 300 for `control-checks`) are proposed; record the measured durations of the first full run so SE can confirm or revise them.

## Acceptance criteria

1. `legavia_sdlc_gui/tools/report_checks.py` runs the Python unittest discovery and the JavaScript `node --test` suites, writes one schema-version-1 case per real test with actual status and duration to `SDLC_RESULT_PATH`, exits nonzero on any failure, error or empty discovery, and never fabricates cases.
2. `legacy/tools/report_control_checks.py` runs the business-baseline validator, the control `tools` unittest discovery and the GUI `--validate-only` ingestion of `traceability/manifest.json` with the same report contract; an unavailable GUI package is an `error` case, never a silent skip.
3. Wrapper unit tests exist in both repositories and cover passing, failing, erroring and missing-runner paths plus the report schema; GUI CI keeps running the wrapper-free commands.
4. At the delivered candidate, the GUI verification status reports `gui-checks` and `control-checks` as available, and a WP-015 acceptance run covering gui and control completes with outcome Pass and a recorded candidate fingerprint.
5. No Work Package ID appears in product source; `tooling-fixture`, the product execution gate and LEGACY-WORK-013's status and acceptance criteria are unchanged.

## Gate

Candidate-bound unit test gate required. The runner's registered-check stage selects `gui-checks` and `control-checks` for this package (its non-read-only allocation is gui and control); the wrappers written during the run make those commands executable in the same run. Independent `code_style` and `design` reviews inspect the candidate; operator acceptance establishes Done. Acceptance of this package does not accept LEGACY-WORK-013 and does not establish any product FVT outcome.

## Verification and completion boundary

Evidence: the runner-owned verification run for this package (schema-version-1 reports for both suites, candidate fingerprint, source snapshot), the GUI CI results for the implementation PR, and the independent reviews. Fixture and tooling passes are tooling evidence only. After acceptance and publication to `origin/main` in both repositories, follow `docs/engineering/WP013_READINESS_CHECKLIST.md` before preparing a fresh LEGACY-WORK-013 prompt.
