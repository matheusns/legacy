# Legavia Reference Artifacts

This directory contains durable, agent-readable material that should influence product discovery and implementation decisions across Legavia.

## Current reference set

### `LEGACY_GAMIFICATION_UX_ARCHITECTURE_BASELINE_v0.1.md`

State-of-the-art benchmark and baseline candidate covering:

- habit/productivity/gamification product patterns;
- design principles and anti-patterns;
- application shell and information architecture;
- gamification model;
- reusable UX/agent capabilities;
- candidate business, functional, UX, and non-functional requirements;
- use cases and FVT seeds;
- traceability and release slicing.

**Use it when:** conceiving or reviewing mockups, adding a module, changing navigation, designing gamification mechanics, defining shared domain concepts, deriving requirements/use cases, or creating verification flows.


### LEGACY_FINANCIAL_LIFE_MANAGEMENT_USE_CASES_v0.1.md

Agent-readable **candidate** for the Life → Financial view. Captures Brazil/UAE account and card management, weekly transaction reconciliation, essential/discretionary spending, monthly saving and financial forecasts, car/apartment costs, FX remittances, data import, traceable UC-013–UC-019, LEGACY-FNC-029–043, and FVT-LEGACY-009–014.

**Use it when:** designing the Financial module's UX, data model, import workflows, reporting, financial projections or test plans. The user's 2026 workbook is a **pending reference** for mapping and verification. Do not store actual financial records in this repo. Candidate requirements require approval before formal baseline promotion.

## Brand compatibility

The current product name is **Legavia**. Legacy `LEGACY-*` IDs and `LEGACY_*` filenames are compatibility identifiers and remain authoritative until a separately approved namespace migration.

## Status semantics

`baseline-candidate` means the artifact is authoritative as a **reference constraint and traceability source**, but its candidate requirements are not automatically equivalent to formally approved project requirements. Promotion to the formal project baseline should preserve the IDs already assigned in the artifact.

## Maintenance rule

Do not overwrite historical versions. Add a new version and update `reference-manifest.yaml` so agents can determine the active reference.
