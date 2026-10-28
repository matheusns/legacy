# Legavia business and systems engineering baseline (v0.2)

**Status:** Candidate for Systems Engineering / product-owner review; not yet approved for execution. Date: 2026-10-29.

## Read in this order

1. [ConOps](LEGACY_CONOPS_v0.2.md) — actors, operating modes and end-to-end scenarios.
2. [Product scope](LEGACY_PRODUCT_SCOPE_v0.2.md) — modules, release slices and boundaries.
3. [Requirements](LEGACY_REQUIREMENTS_v0.2.md) — preserved baseline candidates and extended SHALL statements.
4. [Use cases](LEGACY_USE_CASES_v0.2.md) — goal-oriented interaction contracts and alternate flows.
5. [Functionalities](LEGACY_FUNCTIONALITIES_v0.2.md) — technical behavior decomposition and dependencies.
6. [Domain model](LEGACY_DOMAIN_MODEL_v0.2.md) — core entity ownership, transactions, events and cross-domain data semantics.
7. [UX contract](LEGACY_UX_CONTRACT_v0.2.md) — mobile/desktop visual baseline and reference governance.
8. [Verification plan](LEGACY_VERIFICATION_PLAN_v0.2.md) — design-only FVT catalogue and release gates.
9. [Engineering governance](LEGACY_SDLC_CONTRACT_v0.2.md) — agents, work packages, GitHub, evidence and review gates.
10. [Open architectural decisions](LEGACY_DECISIONS_v0.2.md) — questions requiring explicit ADRs prior to implementation.

## Machine-readable artifacts

- [GUI manifest](../../traceability/manifest.json): matches the existing `sdlc_gui.model.load_manifest` contract (schema_version, project, requirements, functionalities, work_packages, artifacts). All component records currently use `scope=all`, as the unadapted GUI only accepts library/node/all filters. `component` is additional metadata and SHALL NOT be misinterpreted as a supported filter.
- [Use case catalog](../../traceability/use_cases.json): complete actors, scenario and trace links.
- [FVT seed catalog](../../traceability/verification_seed_catalog.json): specification-only cases; **not** registered as runnable tests.
- [Work packages](../../work_packages/): execution-bound initial backlog, explicit predecessors and target repositories.

**Critical compatibility note:** This creates the project-owned manifest that the legacy GUI expects, but does not automatically implement its web/mobile adapter, GitHub PR provider, runner, product-specific scopes, or browser verification wiring. Until those changes are integrated, the GUI is usable as a **traceability/read-only planning surface**, not evidence of end-to-end development readiness.

## Identifier and precedence policy

Keep `LEGACY-*` IDs and historical filenames, despite the brand being **Legavia**. Accepted requirements and ADRs supersede this candidate. Existing [reference](../reference/README.md) remains the UX and product benchmark, not a silently approved requirements authority.

## Validation

```bash
PYTHONPATH=../legavia_sdlc_gui/src python3 -m sdlc_gui --manifest traceability/manifest.json --validate-only
python3 tools/validate_business_baseline.py
```

The first command requires the sibling GUI checkout. The second is repository-local deterministic traceability integrity validation (no runtime agents or external services).
