---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Manifest, GUI Compatibility and Validation

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

## Source of truth
The product definition is owned by `matheusns/legacy`. `traceability/manifest.json` is a direct input to the existing GUI loader; it contains `schema_version`, `project`, `requirements[]`, `functionalities[]`, `work_packages[]` and `artifacts[]`. `traceability/business_baseline.json` carries actor-level use cases, FVT definition records and release governance metadata. The Traceability workspace now projects ConOps, use cases, controlled documents, and requirement → capability → work → planned verification links directly from those sources.

## Workflow adoption prerequisite
Before executing application Work Packages from the GUI, implement and accept **LEGACY-WORK-013** (project component/device filters, native use-case/ConOps panels, GitHub PR provider and application runner integration). Read-only manifest visualization is possible independently; the historical ROS/GitLab execution behavior is not an approved Legavia workflow.

## Engineering schema migration
The dedicated Legavia GUI now uses engineering schema 2 with the declared native application components and separate desktop/mobile profiles. The schema-1 business manifest was migrated explicitly. All issued IDs, requirement wording, Candidate/Backlog/Planned status, target-repository references, use-case/FVT links, and work dependencies remain unchanged. Old schema-1 inputs require migration; the approved fork adaptation does not retain robotics executor compatibility.

`component_ids` references native business capabilities, `repository_ids` and `repository_access` define execution authority, and target profiles distinguish desktop browser, mobile browser, and an installed-PWA adapter that remains unavailable. The local role adapters are configured, while actual product commands and approved screenshot references remain pending. The existing acceptance gate on LEGACY-WORK-013 remains in force.

## Validation commands
```bash
cd legacy
python3 tools/validate_business_baseline.py
cd ../legavia_sdlc_gui
PYTHONPATH=src python3 -m sdlc_gui --manifest ../legacy/traceability/manifest.json --validate-only
PYTHONPATH=src python3 -m sdlc_gui --manifest ../legacy/traceability/manifest.json
```

The last command starts the local dashboard on http://127.0.0.1:8080. Packaged role adapters require the registered host CLI/session. Product execution remains blocked by LEGACY-WORK-013 until its SE acceptance; registered tooling-fixture checks remain separate. Actual product commands, approved screenshot references and source revisions are prerequisites for product verification.

## Traceability relations
Business need → `LEGACY-BIZ` / `LEGACY-FNC` / `LEGACY-UX` / `LEGACY-NFR` → `LEGACY-CAP` → `LEGACY-WORK` → independent `FVT-LEGACY` → verified candidate result. Use-case links and FVT mapping are in `business_baseline.json`; capabilities, requirements, WPs and artifact paths are in `manifest.json`.

## Governance
All requirements are marked Candidate, all Work Packages Backlog and all FVTs Planned; artifacts remain unverified. Work Package IDs belong only in control-plane records, not source code or production PR titles. The first Work Package is SE review; later implementation WPs depend on its accepted disposition.

