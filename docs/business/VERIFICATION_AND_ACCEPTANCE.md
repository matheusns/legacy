---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Independent Verification, Validation and Quality Gates

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

## Verification philosophy
`FVT-LEGACY-001..024` are **planned acceptance definitions**. No executable test, passing result or implementation evidence is asserted. `legacy_verification_tooling` will host the deterministic implementation and screenshots when developed. A controlled test records revision, fixtures, environment, command, asserted result, artifacts, reviewer, disposition and expiry/freshness fingerprint.

### FVT-LEGACY-001 — Goal-linked Today completion and XP

**Stimulus:** Create task linked to milestone; complete from Today twice with same operation ID.  
**Expected:** One task completion, one XP grant and correct milestone progress; undo reverses only the matching effects.  
**Trace:** LEGACY-FNC-002, LEGACY-FNC-003, LEGACY-FNC-007, LEGACY-FNC-009, LEGACY-FNC-010, LEGACY-FNC-013, LEGACY-FNC-074  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-002 — Map progression and non-drag access

**Stimulus:** Create phases with milestones and evaluate transitions.  
**Expected:** Locked/available/active/completed states follow prerequisites; accessible controls work without drag.  
**Trace:** LEGACY-FNC-003, LEGACY-FNC-004, LEGACY-FNC-005  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-003 — Missed-day recovery

**Stimulus:** Miss multiple planned days and revisit.  
**Expected:** Historical events retained; recovery and continuity behavior available.  
**Trace:** LEGACY-FNC-011, LEGACY-FNC-012, LEGACY-FNC-068  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-004 — Cross-module navigation

**Stimulus:** Navigate among three modules on mobile and desktop.  
**Expected:** State preserved; one-step shell access and responsive override respected.  
**Trace:** LEGACY-FNC-017, LEGACY-FNC-060, LEGACY-FNC-064  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-005 — Workspace isolation

**Stimulus:** Create two workspaces and varied sharing roles; request unauthorized objects.  
**Expected:** No cross-workspace exposure even through direct API and nested resources.  
**Trace:** LEGACY-FNC-001, LEGACY-FNC-056, LEGACY-FNC-061  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-006 — AI change governance

**Stimulus:** Create, reject, revise, approve and beta-route a proposed feature.  
**Expected:** No unapproved baseline mutation; complete audit evidence.  
**Trace:** LEGACY-FNC-025, LEGACY-FNC-026, LEGACY-FNC-055, LEGACY-FNC-058  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-007 — Learning import

**Stimulus:** Import a sample course and edit extracted lessons.  
**Expected:** Candidate content saved only after explicit approval.  
**Trace:** LEGACY-FNC-027, LEGACY-FNC-067  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-008 — Accessibility and visual fidelity

**Stimulus:** Run keyboard, screen-reader, small-screen, contrast and approved screenshot comparison.  
**Expected:** Applicable WCAG 2.2 AA criteria and reference comparison accepted.  
**Trace:** LEGACY-FNC-005, LEGACY-FNC-060  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-009 — Finance transactions and batches

**Stimulus:** Ingest duplicate batch and review classification.  
**Expected:** One approved ledger mutation per row; provenance retained.  
**Trace:** LEGACY-FNC-029, LEGACY-FNC-030, LEGACY-FNC-031, LEGACY-FNC-041  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-010 — Card liability and account balances

**Stimulus:** Purchase, settle card, reverse and reconcile account.  
**Expected:** No duplicated expenses; assets/liabilities balanced.  
**Trace:** LEGACY-FNC-029, LEGACY-FNC-032, LEGACY-FNC-033  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-011 — Cross-border transfer and FX

**Stimulus:** Transfer AED to BRL with fees and partial settlement.  
**Expected:** Two linked legs, correct currency, fees and no income duplication.  
**Trace:** LEGACY-FNC-033, LEGACY-FNC-034, LEGACY-FNC-042, LEGACY-FNC-043  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-012 — Finance savings and budgets

**Stimulus:** Compute period actuals versus budget with refunds, gains and transfers.  
**Expected:** Source-drilldowns reconcile; correct financial classification.  
**Trace:** LEGACY-FNC-035, LEGACY-FNC-036, LEGACY-FNC-043  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-013 — Financial workbook approved import

**Stimulus:** Load synthetic workbook mapping including duplicated rows.  
**Expected:** Preview, review, approve; deduplicate and reconcile.  
**Trace:** LEGACY-FNC-031, LEGACY-FNC-040, LEGACY-FNC-041  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-014 — Vehicle and apartment scenarios

**Stimulus:** Compare ownership/rental, cash flows and liabilities over one to five years.  
**Expected:** Principal, operating expense, debt and valuation properly distinguished.  
**Trace:** LEGACY-FNC-037, LEGACY-FNC-038, LEGACY-FNC-039, LEGACY-FNC-042  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-015 — Focus and XP idempotency

**Stimulus:** Start/pause/stop focus session; replay stop command.  
**Expected:** Session duration and reward computed once; linked task remains consistent.  
**Trace:** LEGACY-FNC-045, LEGACY-FNC-046, LEGACY-FNC-069, LEGACY-FNC-074  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-016 — Book prediction

**Stimulus:** Record three dated reading updates and an insufficient-data case.  
**Expected:** Predicted finish updates with evidence and uncertainty; invalid page input rejected.  
**Trace:** LEGACY-FNC-047, LEGACY-FNC-070  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-017 — Movie/audio intake

**Stimulus:** Use text fallback and a simulated transcript; external ratings unavailable.  
**Expected:** User reviews before save; recommender/date retained; manual ranking works.  
**Trace:** LEGACY-FNC-049, LEGACY-FNC-054, LEGACY-FNC-071  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-018 — Memory privacy and export

**Stimulus:** Create photo and voice entries; revoke access; export workspace.  
**Expected:** Attachments scoped to owner, exported correctly, deleted/revoked per policy.  
**Trace:** LEGACY-FNC-050, LEGACY-FNC-062  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-019 — Water logging

**Stimulus:** Add, retry and undo hydration update; test midnight boundary.  
**Expected:** Correct target totals, no duplicate and local day semantics.  
**Trace:** LEGACY-FNC-044, LEGACY-FNC-073  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-020 — Display mode responsive visuals

**Stimulus:** Check Auto/Mobile/Desktop on sample phone and desktop profiles.  
**Expected:** Accepted layout capture and UX states; no inaccessible primary actions.  
**Trace:** LEGACY-FNC-060, LEGACY-FNC-064  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-021 — Social resource permissions

**Stimulus:** Share one goal with one friend then revoke.  
**Expected:** Only selected resources accessible, zero implicit friend/household access.  
**Trace:** LEGACY-FNC-024, LEGACY-FNC-056, LEGACY-FNC-057  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-022 — AI consent and external issue suggestions

**Stimulus:** Submit text/voice task and candidate GitHub issue suggestion.  
**Expected:** Explicit review and authorization; no silent writes to either service.  
**Trace:** LEGACY-FNC-054, LEGACY-FNC-055, LEGACY-FNC-066  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-023 — Recovery and data integrity

**Stimulus:** Interrupt network mid mutation and replay with same event ID.  
**Expected:** Exactly-once ledger effects and understandable reconciliation state.  
**Trace:** LEGACY-FNC-009, LEGACY-FNC-010, LEGACY-FNC-074  
**Status:** Planned; independent evidence missing.

### FVT-LEGACY-024 — Administrative beta and quota

**Stimulus:** Roll out beta to one cohort and test other workspaces; trigger upload quota.  
**Expected:** Correct feature flags, no data disclosure and safe upload rejection.  
**Trace:** LEGACY-FNC-058, LEGACY-FNC-059, LEGACY-FNC-061  
**Status:** Planned; independent evidence missing.

## Release quality gates
1. Requirements and approved ConOps/use cases are baselined by Systems Engineering; approved ADRs address architecture and security.
2. Source branch builds reproducibly; unit and integration suites pass with clean candidate fingerprint; failing checks are not waived silently.
3. Server-side tenant and object-level authorization tests pass for every data access path, including nested IDs and shared-resource revocation.
4. Idempotency and event correctness tests confirm one completion → one reward, correct undo and retry outcomes.
5. Applicable WCAG 2.2 AA, keyboard, touch and reduced-motion tests pass. Phone and desktop screenshots are compared to *approved* references.
6. Privacy review confirms no personal files, credentials or raw transcripts entered code repository, test fixtures or telemetry.
7. Backup/restore and data export/deletion readiness are verified before durable personal finance or memory rollout.

**Important:** GUI imported ROS unit runner and GitLab review provider are not equivalent to Legavia application CI. Until adapters land, run these checks independently and attach accepted evidence; never mark an FVT passing merely because this catalog exists.
