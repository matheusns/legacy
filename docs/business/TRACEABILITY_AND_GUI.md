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
The product definition is owned by `matheusns/legacy`. `traceability/manifest.json` is a direct input to the existing GUI loader; it contains `schema_version`, `project`, `requirements[]`, `functionalities[]`, `work_packages[]` and `artifacts[]`. `traceability/business_baseline.json` carries actor-level use cases, FVT definition records and release governance metadata that the current GUI does **not yet display natively**.

## Workflow adoption prerequisite
Before executing application Work Packages from the GUI, implement and accept **LEGACY-WORK-013** (project component/device filters, native use-case/ConOps panels, GitHub PR provider and application runner integration). Read-only manifest visualization is possible independently; the historical ROS/GitLab execution behavior is not an approved Legavia workflow.

## Compatibility boundary
The upstream GUI currently recognizes scopes `all/library/node`, and some views continue to label library and ROS node. **All Legavia business records have `scope=all`**, preventing misleading assignment to an unrelated robotics component. The future adapter shall use `legavia_extension.application_components` and `legavia_extension.target_profiles` for filters and show native Use Cases/ConOps tabs. The new namespaced metadata is preserved without assuming it is currently interpreted.

## Validation commands
```bash
cd legacy
python3 tools/validate_business_baseline.py
cd ../legavia_sdlc_gui
PYTHONPATH=src python3 -m sdlc_gui --manifest ../legacy/traceability/manifest.json --validate-only
PYTHONPATH=src python3 -m sdlc_gui --manifest ../legacy/traceability/manifest.json
```

The last command starts the read-only dashboard on http://127.0.0.1:8080 when no project-specific agent runner is configured. Do not activate Development, FVT, QA or preview execution until approved application-specific runner adapters and source revisions exist.

## Traceability relations
Business need → `LEGACY-BIZ` / `LEGACY-FNC` / `LEGACY-UX` / `LEGACY-NFR` → `LEGACY-CAP` → `LEGACY-WORK` → independent `FVT-LEGACY` → verified candidate result. Use-case links and FVT mapping are in `business_baseline.json`; capabilities, requirements, WPs and artifact paths are in `manifest.json`.

## Governance
All requirements are marked Candidate, all Work Packages Backlog and all FVTs Planned; artifacts remain unverified. Work Package IDs belong only in control-plane records, not source code or production PR titles. The first Work Package is SE review; later implementation WPs depend on its accepted disposition.
