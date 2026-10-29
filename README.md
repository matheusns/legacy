# Legavia

Legavia is a multi-domain life-management product that integrates goals, daily execution, habits, learning, health, finance, insights, and gamified progression in one coherent experience.

## Repository reference material

Agents and contributors should read [`AGENTS.md`](AGENTS.md) before making cross-cutting product, UX, mockup, or architecture changes.

The active product/UX reference baseline is indexed under [`docs/reference/README.md`](docs/reference/README.md).

## Brand and namespace compatibility

The product brand is **Legavia**. The repositories remain `matheusns/legacy` and `matheusns/legacy_mockups` for now. Existing `LEGACY-*` traceability IDs and `LEGACY_*` artifact filenames remain stable until an explicit namespace migration is approved, so historical links and requirement/FVT references are not broken.

## Controlled business baseline (candidate)

The [Business Baseline](docs/business/README.md) contains the ConOps, use cases, formal requirements, functionality allocations, conceptual domain model, responsive UX contract, external interfaces and independent verification plan. The [traceability manifest](traceability/manifest.json) uses engineering schema 2 with native application component/device profiles, preserved business identifiers, and explicit repository access. The schema-1 business input was migrated without changing requirement wording or approval status.

Validate using `python3 tools/validate_business_baseline.py` and load the GUI using `PYTHONPATH=src python3 -m sdlc_gui --manifest ../legacy/traceability/manifest.json` from `legavia_sdlc_gui`. All new records remain candidate or backlog until Systems Engineering approval.


## Local engineering workbench

Read [the workflow](docs/engineering/WORKFLOW.md) for role configuration and setup. The GUI adaptation and independent harness require their linked companion PRs. Product execution remains gated by Systems Engineering acceptance of LEGACY-WORK-013; the tooling fixture establishes no product approval.
