---
project: LEGAVIA
artifact_id: LEGACY-SE-REVIEW-002
artifact_type: se_review_record
artifact_status: review-draft-unsigned
version: 0.1.0
date: 2026-10-30
control_repository: matheusns/legacy
work_package: LEGACY-WORK-002
run_id: DEV-20261030T185520Z-751CB5
resumed_from_run_id: DEV-20261029T133455Z-DF9AA5
reviewed_control_commit: caca50c7e23a892d37e63cc14091f8cf725374d6
review_gate: Human Systems Engineering signature required
---

# LEGACY-SE-REVIEW-002 — Architecture decision set and secure domain skeleton for LEGACY-WORK-002

> **Unsigned draft.** Prepared by the Systems Engineering control-plane agent. It proposes seven ADRs and one skeleton definition and recommends a disposition; it does not grant one. No ADR is accepted, no work package status changes, and no requirement is verified until a human Systems Engineering reviewer completes section 10 and the control manifest is updated by a human-controlled commit. Nothing here is execution evidence for any product FVT.

## 1. Baseline identification

| Item | Value |
| --- | --- |
| Work package | `LEGACY-WORK-002` — Architecture decisions and secure domain skeleton (P0, systems_engineering, Backlog) |
| Predecessor | `LEGACY-WORK-001` — recorded `Done` in `traceability/manifest.json` (review disposition `Accepted`, run `DEV-20261029T123218Z-587BA0`); see finding SE2-F-001 |
| Control repository revision | `matheusns/legacy` `main` @ `caca50c7e23a892d37e63cc14091f8cf725374d6`, clean working tree before this run |
| Frozen source integrity (run context) | `docs/work_packages/LEGACY-WORK-002.md` = `5275740b0455adbbd07bd5edb20e5d062c36f8f5928cd3e0fa4f6cba4ab91207`; `traceability/manifest.json` = `15a56ecb62cd9f199ee158371e43316165cc30010d4d4a3486c9a3c640d88132` — both verified unchanged before and after this run |
| Business baseline | v0.1.0 (candidate), 129 requirements, 15 capabilities, 35 use cases, 24 planned FVTs, 13 work packages |
| Reference set | LEGACY-REF-UX-001, LEGACY-REF-FIN-001, LEGACY-REF-FIN-002 (all `baseline-candidate`, unchanged) |
| Sibling repositories (read-only) | `legavia_sdlc_gui` @ `80bb232d`, `legacy_app` @ `0abe8fd6`, `legacy_mockups` @ `ca2e9dbf`, `legacy_verification_tooling` @ `7b7973b6` |
| Validator | `python3 tools/validate_business_baseline.py` → `Valid candidate baseline … all links resolved.` (unchanged by this run) |

### 1.1 Candidate fingerprint of proposed artifacts (SHA-256 at end of run)

| File | SHA-256 |
| --- | --- |
| docs/architecture/adr/ADR-001-application-stack-hosting-persistence.md | `b218393e21d3b80d27e1069eba692e6b8e067720f62388b7968243e8bc44b55b` |
| docs/architecture/adr/ADR-002-identity-tenancy-authorization.md | `1642a89062494ac0d6b86a4b3959ddb7c119b1ae644c9d23f8cb853f99c0cf73` |
| docs/architecture/adr/ADR-003-source-of-truth-events-idempotency-rewards.md | `c6ea2e4e51709f598f82ab97d1b999d008a3a3fd0ff66dbce5dc95f82175d9be` |
| docs/architecture/adr/ADR-004-visual-assets-design-system-golden-baseline.md | `6352143b55b43b2a67ce37ad4271172502ecb6b2111e15920baad1849ea4a3af` |
| docs/architecture/adr/ADR-005-testability-verification-adapters-fingerprints.md | `92181245198de3020336570391d4fcefd4eff1f4861996e020e9b262578ee42b` |
| docs/architecture/adr/ADR-006-connectivity-drafts-conflicts-backup-deletion.md | `a39d52dd4e9ff8fd8020808cd488b9f2540c5e4db1e5cba1a51714f96a6f02dc` |
| docs/architecture/adr/ADR-007-ai-consent-provider-scopes-approval-speech-privacy.md | `2641fe5f55175deccea47e395af9202d110dcafa6ca1f333466c2e599180ea3c` |
| docs/architecture/adr/README.md | `8b95f87dd2a44434b61581eb3235ea10b1f0b7c880d42944d87d6e5fa517bc21` |
| docs/architecture/SECURE_DOMAIN_SKELETON.md | `a6ab7a87271e809556dcbfc3cdaca4b759dfdd20e395ddd2b7a0ad7109531639` |

Any edit after signature invalidates the signature for that file and requires a new review record version.

## 2. Scope and method

**Produced:** seven ADRs resolving the complete candidate register `ADR-CAND-001..007` (`DEC-001..007`, plus `DEC-008`, `DEC-009` method and `DEC-011`), a register index, and the secure domain skeleton definition `LEGACY-ARCH-SKELETON-001`. All are **Proposed**; the Status section of each ADR deliberately does not match the workbench's accepted-status detection, and no manifest `artifacts[]` entry was added.

**Read before deciding (per AGENTS.md and the SE contract):** `AGENTS.md`; `docs/reference/README.md`, `reference-manifest.yaml`, LEGACY-REF-UX-001 sections 1, 5–9, 12–15, LEGACY-REF-FIN-001 sections 1, 3–5, 7, LEGACY-REF-FIN-002 sections 1–3, 5; all eleven business documents; `LEGACY-SE-REVIEW-001`; `docs/engineering/WORKFLOW.md` and `ADAPTATION_HANDOFF.md`; `agents/systems-engineering.md`; work packages 002, 003, 004, 009, 013; `architecture/README.md`, `model.json`, `layout.json`. Read-only inspection of sibling repositories was limited to structure, READMEs, AGENTS files, `legacy_app/docs/IMPLEMENTATION_BOUNDARIES.md`, the verification harness source and CI, the mockup asset listing, and the workbench's ADR discovery and materialisation code (to match its file format).

**Checks performed:** frozen hashes verified before and after; every `LEGACY-*`, `UC-LEGACY-*` and `FVT-LEGACY-*` identifier cited in the new documents resolves in `manifest.json`/`business_baseline.json` (one typo found and corrected during the run); none of the ADR files matches the workbench's `Status: Accepted` patterns; validator still passes; privacy scan of new files (no credentials, workbook data, or personal records); no product repository modified; `git status` shows only the new `docs/architecture/` tree.

**Not performed, by policy:** no commits, no manifest or work-package edits, no execution of the `tooling-fixture` suite, no claim about any FVT outcome, no acceptance of the agent's own work.

## 3. Conformance to invariants and precedence

| Invariant / rule | Where honoured |
| --- | --- |
| Five-surface shell unchanged | ADR-001 D2(5), ADR-004 D2(9), skeleton §9 |
| Gamification derived from meaningful actions; no game-only maintenance | ADR-003 D1, D5(13) |
| Expressive theming only on progression surfaces | ADR-004 D2(6) two token layers |
| Goal → Phase → Milestone → Action; map is a projection | ADR-003 D1(2), skeleton §4–5 |
| Recovery over destructive reset | ADR-003 D5(12) reducers for continuity/recovery |
| Social opt-in; no implicit access | ADR-002 D2(6) |
| Non-drag, non-colour-only, reduced-motion alternatives | ADR-004 D2(7–8), ADR-006 D1(1) pending marker |
| AI evolution needs human approval | ADR-007 D3(7–8) |
| Finance invariants (deferred module) | `Money` type and FX provenance fixed in ADR-001 D4(12); computation contracts deferred (DEC-013) |
| LEGACY IDs preserved; Legavia brand | `ADR-CAND-*` cited not renumbered; product name Legavia throughout |
| Precedence: approved requirements/ADRs → use cases → references → mockups → inference | Each ADR cites baseline documents first; mockup state explicitly non-authoritative (ADR-003 D1(1)); where a value had no baseline source (ADR-004 bands, ADR-006 RPO/RTO, ADR-001 provisional performance targets) it is labelled a proposed value with a calibration or measurement obligation |

No baseline invariant conflict was found. No requirement statement, reference artifact or fingerprinted v0.1.0 document was altered.

## 4. Findings

### SE2-F-001 — LEGACY-WORK-001 is `Done` in the manifest while LEGACY-SE-REVIEW-001 remains an unsigned draft (Condition)

`traceability/manifest.json` records `LEGACY-WORK-001.status = Done` with `review.disposition = Accepted` (commit `0b63e1e`), but `docs/reviews/LEGACY-SE-REVIEW-001.md` still carries `artifact_status: review-draft-unsigned` with an empty signature table, and the manifest `artifacts[]` does not register the review record (its section 9 item 1). The dependency of WORK-002 on WORK-001 is therefore satisfied in the manifest but not evidenced in the controlled document. **Proposed resolution:** the human reviewer completes section 10 of REVIEW-001 (or records the GUI acceptance there), and the manifest `artifacts[]` gains the `LEGACY-SE-REVIEW-001` entry. This does not block reviewing the ADRs; it blocks treating WORK-001's conditions (SE-F-001/002/006/009) as tracked.

### SE2-F-002 — ADR identifier scheme differs from the candidate register (Observation, resolved by mapping)

The workbench canonicalises ADR IDs as `ADR-<digits>`, so `ADR-CAND-00N` cannot be the materialised file ID. The register README records the 1:1 mapping and every ADR cites its `ADR-CAND-*` and `DEC-*` origins. **Resolution needed from the reviewer:** confirm the mapping; if a different numbering is preferred, rename before acceptance (renaming after acceptance would break `adr_ids`).

### SE2-F-003 — Some decisions had no baseline source for their numbers (Observation)

ADR-004 D4 (visual diff bands 0.1 % / 1.0 %), ADR-006 D3 (PITR ≥ 7 days, RPO ≤ 24 h, RTO ≤ 8 h, 7-day draft retry, 30-day receipts, 14-day deletion grace) and ADR-001 D6 (provisional LCP 2.5 s / 100 ms feedback) propose concrete values because the baseline requires them to be set by an ADR rather than invented in tooling. Each is marked as a proposed value with a calibration or measurement obligation and a revision path. **Reviewer action:** accept, revise, or defer each number explicitly; do not let tooling treat them as acceptance thresholds before this is recorded.

### SE2-F-004 — Hosting provider and region are intentionally not selected (Observation)

ADR-001 D5 fixes the hosting model and four binding constraints but defers vendor and region to an owner addendum before the first hosted environment, because cost, residency for a UAE/Brazil user base and account ownership are operator decisions. If the reviewer wants a vendor named in the accepted ADR, that choice must be recorded in D5(15) before acceptance.

### SE2-F-005 — SE-F-002/003/004 (WORK-001 conditions assigned to WORK-002) are decided, not applied (Observation)

ADR-005 D5 fixes the closed verification-method vocabulary and D6 the verification allocation for P0 BIZ/UX/NFR requirements; SE-F-004 (`refines` relations) is not addressed by an ADR because it is a catalog change with no architectural content. Applying D5/D6 touches `REQUIREMENTS.md`, `manifest.json` and `business_baseline.json` and requires the validator extension of SE-F-009 (`DEC-012`); it must be a separate control change after ADR acceptance, together with the SE-F-001 trace restoration. **Owner:** control-only change, proposed as the first WORK-002 follow-up (section 9 item 4).

### SE2-F-006 — Finance decision DEC-013 is out of this package's capability scope (Observation)

`LEGACY-WORK-002` is allocated CAP-001/003/004. DEC-013 (finance computation contracts) is deferred to a `LEGACY-WORK-010` predecessor as REVIEW-001 allowed; only the cross-cutting `Money` primitive is fixed now (ADR-001 D4(12)) because every later ledger depends on it.

### SE2-F-007 — Prior run DEV-20261029T133455Z-DF9AA5 left no artefacts (Observation)

The resumed run reported `execution_blocked` with no files created or modified and no recorded challenge text; nothing was reused. The working tree matched the baseline commit before this run.

## 5. Coverage of the work package acceptance criteria

| Criterion | Proposed evidence | Human action still required |
| --- | --- | --- |
| Accepted ADRs for identity/tenancy | ADR-002 | Accept |
| … source of truth | ADR-003 D1, ADR-001 D4 | Accept |
| … event idempotency | ADR-003 D2–D4 | Accept |
| … app stack | ADR-001 D1–D3 | Accept |
| … assets | ADR-004 | Accept; reference image approval separate (DEC-010) |
| … hosting | ADR-001 D5 | Accept; vendor addendum before first environment |
| … testability | ADR-005 | Accept |
| Record trace from controlled requirements to changed implementation or review evidence | Traceability blocks in every ADR; register table; skeleton §12; this record | Sign |
| Preserve privacy and tenant-isolation behaviour; attach candidate fingerprint and reviewer disposition | ADR-002, ADR-006 D3(10)/D5, ADR-007 D2; section 1.1; section 10 | Sign |
| SE review and baseline identification mandatory; no runtime unit-test requirement | Sections 1–3; no tests claimed | Sign |

## 6. Unresolved decisions register (carried forward)

| ID | Decision | Status after this run | Owner |
| --- | --- | --- | --- |
| DEC-001..007 | ADR-CAND-001..007 | Proposed as ADR-001..007 | Human SE acceptance |
| DEC-008 | Visual diff method and bands | Proposed in ADR-004 D4 with calibration obligation | Human SE acceptance |
| DEC-009 | Performance budgets | Method fixed (ADR-001 D6, ADR-005 D1); numbers after measurement | Verification (WORK-009) + SE |
| DEC-010 | Reference image approval and pinning | Procedure in ADR-004 D3; no image approved | Owner + UX reviewer |
| DEC-011 | Verification allocation and vocabulary | Decided in ADR-005 D5–D6; application pending | Control-only change |
| DEC-012 | Validator semantics for `Approved` | Open; prerequisite for any promotion | Control-only change |
| DEC-013 | Finance computation contracts | Deferred to WORK-010 predecessor | SE |
| DEC-014 | Namespace migration | Deferred | Owner |
| DEC-015 | Installed-PWA adapter | Open | WORK-009 |
| DEC-016 | Allocation for CAP-007/010/011/012/014 | Open | Roadmap revision |
| DEC-017 | Provenance pinning | Open | Control-only change |
| NEW DEC-018 | Hosting provider and region addendum to ADR-001 D5 | Open; before first hosted environment | Owner |
| NEW DEC-019 | Calibration of ADR-004 bands after ten baselines | Open; before Review band may auto-pass | Verification + SE |

## 7. Disposition recommendation

| Artifact | Recommended disposition | Conditions |
| --- | --- | --- |
| ADR-001 | Accept | Record SE2-F-004 position (vendor now or addendum later); confirm provisional performance targets are non-acceptance values |
| ADR-002 | Accept | None |
| ADR-003 | Accept | None |
| ADR-004 | Accept | Explicitly confirm or revise D4 bands (SE2-F-003); DEC-010 stays separate |
| ADR-005 | Accept | D5/D6 application as a follow-up control change with validator extension |
| ADR-006 | Accept | Explicitly confirm or revise D3 recovery objectives and D4/D5 retention periods |
| ADR-007 | Accept | None |
| SECURE_DOMAIN_SKELETON.md | Accept as controlled definition input for LEGACY-WORK-003 | Implementation may propose adjustments through SE |
| LEGACY-WORK-002 | No status change by this record | Done only when all seven ADRs are accepted and the manifest records `adr_ids` and this review |

**Overall recommendation:** accept the seven ADRs as the architecture baseline for S1/S2 with the explicit numeric confirmations noted, so that `LEGACY-WORK-003`, `LEGACY-WORK-009` and `LEGACY-WORK-013` can be planned against accepted decisions. Do not promote requirement or FVT statuses in the same action (DEC-012 still open).

## 8. Meaning of acceptance

Accepting an ADR establishes its Decision section as a constraint that outranks reference artifacts, mockups and agent inference for all downstream work packages. It does **not** verify any requirement, approve any visual reference, select a hosting vendor beyond the stated constraints, register any product command, or mark any FVT executable. Deviations from an accepted ADR require a superseding ADR or an SE-approved scoped deviation.

## 9. Proposed control changes after signature (not applied by this run)

1. For each accepted ADR: rewrite its `## Status` to `Accepted — <date>` and add to `traceability/manifest.json` `artifacts[]`: `{ "id": "ADR-00N", "type": "design", "name": "<title>", "repository": "legacy", "scope": "all", "path": "docs/architecture/adr/ADR-00N-<slug>.md", "ref": "main", "status": "Accepted", "requirement_ids": [...], "functionality_ids": [...] }` using the IDs in each ADR's Traceability block.
2. `work_packages[LEGACY-WORK-002].adr_ids = ["ADR-001", …, "ADR-007"]`; add `{ "id": "LEGACY-SE-REVIEW-002", "type": "review_record", "scope": "all", "status": "Signed", "path": "docs/reviews/LEGACY-SE-REVIEW-002.md", "title": "SE review of architecture decision set" }` and the still-missing `LEGACY-SE-REVIEW-001` entry (SE2-F-001).
3. Register `docs/architecture/SECURE_DOMAIN_SKELETON.md` as `{ "id": "LEGACY-ARCH-SKELETON-001", "type": "specification", "status": "Accepted" | "Candidate", … }` and add it to `architecture_workspace.documents`.
4. First follow-up control change (SE-F-001/002/003 + ADR-005 D5/D6 + DEC-012 validator extension) as one reviewed change set; `DELIVERY_ROADMAP.md` ADR register section updated to point at ADR-001..007 (new document version, not an in-place rewrite of the fingerprinted v0.1.0 file).
5. `LEGACY-WORK-002` status transition by human action citing this record once items 1–2 are in place.

## 10. Signature

| Role | Name | Decision (Accept / Accept with conditions / Reject / Defer) per ADR | Date | Reviewed commit |
| --- | --- | --- | --- | --- |
| Systems Engineering owner | | ADR-001: · ADR-002: · ADR-003: · ADR-004: · ADR-005: · ADR-006: · ADR-007: · Skeleton: | | `caca50c7e23a892d37e63cc14091f8cf725374d6` |

Unsigned. Prepared by the Systems Engineering control-plane agent in run DEV-20261030T185520Z-751CB5 (Claude Fable 5.1, Claude Code). The agent did not and may not accept its own work.
