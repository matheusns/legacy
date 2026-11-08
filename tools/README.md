# Control verification report adapter

`report_control_checks.py` executes the business-baseline validator, unittest
discovery of `tools/test_*.py`, and GUI `--validate-only` ingestion. It resolves the
GUI source checkout from `traceability/manifest.json` relative to the control root;
a missing GUI is an error, never a skip or an installed-package fallback.

The schema-version-1 report goes to `SDLC_RESULT_PATH` (default:
`test-results/result.json`). Logs, Python case results and the Python runtime
version go to `SDLC_ARTIFACT_DIR` (default: `test-results/artifacts`). Defaults are
ignored. The runner supplies per-run destinations and enforces timeouts and
candidate binding. The validator and ingestion each contribute one command case;
unittest contributes individual test-method cases with measured durations.

`report_support.py` is intentionally mirrored from the GUI tools, allowing this
wrapper to report errors independently of GUI availability. Keep both copies
identical. Subtest outcomes aggregate into their test method; fixture failures are
error cases, expected failures are skipped and unexpected successes are failed.
Empty discovery and missing runners fail the command. No report grants acceptance.
Wrapper tests run temporary fixture suites, never the enclosing discovery.

Report `artifacts` lists absolute paths to the runtime version, worker report and
command logs produced by the invocation. Messages are capped at 4,000 characters
with a truncation marker; full runner diagnostics remain in the referenced logs.
Missing runners produce error diagnostics, and stale logs for unexecuted Node or
GUI ingestion commands are excluded. Artifact references add no passing cases.

The Python worker report is validated before aggregation: schema version, case
names, statuses, durations and messages must be valid. Malformed worker output
becomes an infrastructure error case; a nonzero worker exit cannot pass.
