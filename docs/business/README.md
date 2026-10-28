---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Legavia Business Baseline — Navigation

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

This document set defines a testable system-level product contract. Source material includes the existing [UX/gamification reference](../reference/LEGACY_GAMIFICATION_UX_ARCHITECTURE_BASELINE_v0.1.md), product discovery, and the earlier financial use-case draft (kept as a candidate). No personal financial records, audio recordings, images or access tokens belong here.

## Read order and ownership

1. [Product Vision and Scope](PRODUCT_VISION_AND_SCOPE.md) — outcomes, assumptions, release slicing.
2. [ConOps](CONOPS.md) — actors, operational modes, nominal and failure scenarios.
3. [Use Cases](USE_CASES.md) — actor-level user journeys, alternatives, linked requirements.
4. [Requirements](REQUIREMENTS.md) — complete ID-stable requirements including existing UX and finance IDs.
5. [Functionalities](FUNCTIONALITIES.md) — component-owned product capabilities and dependencies.
6. [Domain and Data Model](DOMAIN_MODEL.md) — conceptual entities, invariants and data classifications.
7. [UX Contract](UX_CONTRACT.md) — reference fidelity and responsive interface acceptance.
8. [External Interfaces](EXTERNAL_INTERFACES.md) — consent, imports and integration boundaries.
9. [Verification and Acceptance](VERIFICATION_AND_ACCEPTANCE.md) — candidate functional and quality test cases.
10. [Delivery Roadmap](DELIVERY_ROADMAP.md) — vertical slices, prerequisite ADRs and Work Package gate.
11. [Traceability and GUI](TRACEABILITY_AND_GUI.md) — manifest integration, validation and known limitations.

Machine-readable truth for the dashboard: `traceability/manifest.json`. Machine-readable business records: `traceability/business_baseline.json`. The canonical candidate is valid only when both pass `python3 tools/validate_business_baseline.py`; no validation outcome by itself grants approval.

**Precedence:** approved requirements/ADRs → approved use cases/verification → candidate business baseline → research reference → mockups/agent assumptions. A candidate cannot override an approved artifact.
