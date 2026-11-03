# LEGACY-WORK-013 readiness checklist

Use this checklist before preparing the next fresh LEGACY-WORK-013 prompt. Every item must be evidenced by a human-visible record; agent prose, GUI fixture passes and this document itself are not evidence. The frozen failed run `DEV-20261102T104129Z-8F4D14` remains historical evidence and must never be resumed.

| # | Condition | Evidence | Owner |
| --- | --- | --- | --- |
| 1 | `docs/reviews/LEGACY-SE-REVIEW-003.md` (version 0.1.1 or a later re-baselined version whose reviewed commits match the heads being prepared) section 10 is signed (schema-2-only loading with explicit migration, Option A) or the alternative disposition is recorded and the WP-013 wording re-synchronised; the manifest `artifacts[]` entry for the record is updated from `Draft` by a human-controlled commit. | Signed review record; human-controlled control commit. | Systems Engineering owner |
| 2 | LEGACY-WORK-014 is accepted by the operator; its control changes (manifest suites, WP-013 reconciliation, WP-015 definition, handoff and workflow updates) are published to `origin/main`. | GUI acceptance record; control commit on `main`. | Operator |
| 3 | LEGACY-WORK-015 is accepted and published to `origin/main` in both `legavia_sdlc_gui` and `legacy`. | GUI acceptance record; commits on both `main` branches. | Operator |
| 4 | The WP-015 acceptance run passed with schema-version-1 reports for `gui-checks` and `control-checks`, a recorded candidate fingerprint and `evidence_current: true`. | Verification run JSON under `.sdlc/runtime/verification/results/`. | Deterministic runner, inspected by operator |
| 5 | The GUI Verification workspace reports `gui-checks`, `control-checks` and `tooling-fixture` as available on the host that will run WP-013 (`node` ≥ 22 and `node_modules/playwright` present in `legacy_verification_tooling`). | Verification status panel or `unit_test_execution_status` output. | Operator |
| 6 | A read-only suite-selection check for LEGACY-WORK-013 shows selected repositories `{gui, control, verification}` equal to its non-read-only allocation, with all three suites available. | Re-run the demonstration recorded in LEGACY-SE-REVIEW-003 section 6 at the new heads. | Systems Engineering |
| 7 | All five checkouts are on clean `main` at `origin/main` (`legavia-update` or Choose main baseline). | `git status` / Project States snapshot. | Operator |
| 8 | `python3 tools/validate_business_baseline.py` and the GUI ingestion `python -m sdlc_gui --manifest traceability/manifest.json --validate-only` (package `__main__`; `python -m sdlc_gui.cli` exits 0 without validating) print their success lines at the new control head. | Command output recorded with the preparation, including the `Valid manifest:` line. | Operator |
| 9 | `application_execution_gate` still names LEGACY-WORK-013 with required status Done; WP-013 status is Backlog; its `unit_test_gate.required` is true; its `depends_on` lists LEGACY-WORK-002, LEGACY-WORK-014 and LEGACY-WORK-015. | Manifest inspection. | Systems Engineering |
| 10 | The WP-013 prompt is prepared fresh from the new baseline with provider, model and repository access selected explicitly; no resume of any earlier WP-013 run. | New run ID in the Development workspace. | Operator |

Passing `tooling-fixture` exercises the independent harness against its own fixture application only. It establishes no product compliance, no FVT outcome and no acceptance of LEGACY-WORK-013.
