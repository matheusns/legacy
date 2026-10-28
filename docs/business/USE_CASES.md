---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# System Use Case Catalog

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

Each use case specifies an actor-level intent and testable system behavior. Precondition and alternative flows are first-class; all claims are **candidate** pending Systems Engineering review. Original UC-001..012 and finance UC-013..019 retain their numeric identity with the stable `UC-LEGACY-` prefix in machine-readable traceability.

## UC-LEGACY-001 — Open Today and execute the next action

**Primary actor:** User  
**Preconditions:** User is authenticated.  
**Main success flow:** System loads today's cross-module agenda; user completes/starts an action; state and progress update.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** The action has one committed event ID, updated projections and an available undo operation.  
**Linked requirements:** LEGACY-FNC-002, LEGACY-FNC-009, LEGACY-FNC-010, LEGACY-FNC-013, LEGACY-FNC-074  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-002 — Create a habit or routine

**Primary actor:** User  
**Preconditions:** Workspace active.  
**Main success flow:** User selects context, schedule/target, reminder/integration, and optional goal link; system validates and saves.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-006, LEGACY-FNC-008, LEGACY-FNC-019  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-003 — Create a long-term goal and phases

**Primary actor:** User  
**Preconditions:** Workspace active.  
**Main success flow:** User creates goal, phases, milestones, success criteria, and optional linked habits/tasks.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-003, LEGACY-FNC-004  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-004 — Navigate the goal map

**Primary actor:** User  
**Preconditions:** At least one goal exists.  
**Main success flow:** User opens Map, selects an island/phase, inspects milestone status, and continues the next available step.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-004, LEGACY-FNC-005  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-005 — Recover after missed activity

**Primary actor:** User  
**Preconditions:** One or more scheduled actions were missed.  
**Main success flow:** System shows a recovery summary, preserves historical continuity, and lets user resume, reschedule, or intentionally skip.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-011, LEGACY-FNC-012  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-006 — Review progress and insights

**Primary actor:** User  
**Preconditions:** History exists.  
**Main success flow:** User selects time range/domain; system shows consistency, milestone progress, trends, and recommended review points.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-021  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-007 — Switch life modules without losing context

**Primary actor:** User  
**Preconditions:** Multiple modules enabled.  
**Main success flow:** User switches from one top-level/module context to another and later returns to the prior state.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-017, LEGACY-FNC-060  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-008 — Use external data to auto-complete progress

**Primary actor:** User  
**Preconditions:** Integration authorized.  
**Main success flow:** System ingests eligible external signal, maps it to a tracked item, updates progress once, and exposes provenance.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-022, LEGACY-FNC-074  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-009 — Collaborate with family on an opt-in goal

**Primary actor:** User / invited family member  
**Preconditions:** Sharing explicitly enabled.  
**Main success flow:** Owner shares selected goal; collaborator sees only authorized data and contributes progress.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-024, LEGACY-FNC-056  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-010 — Submit and approve an AI-generated feature request

**Primary actor:** User / Admin  
**Preconditions:** AI capture and admin role available.  
**Main success flow:** User records request; AI creates structured proposal; admin edits/approves/rejects; approved item enters beta workflow with audit trail.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-025, LEGACY-FNC-026, LEGACY-FNC-055  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-011 — Import a learning course

**Primary actor:** User  
**Preconditions:** Learning module enabled.  
**Main success flow:** User supplies source links; AI extracts candidate modules/lessons/activities; user reviews before saving.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-027, LEGACY-FNC-067  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-012 — Review financial goal projection

**Primary actor:** User  
**Preconditions:** Finance module enabled.  
**Main success flow:** User opens a financial goal, reviews current assumptions/imported values and projected trajectory, and updates assumptions explicitly.  
**Alternatives / failure behavior:** Show recoverable failure; retain draft; deny unauthorized access and avoid partial persistence.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-028, LEGACY-FNC-039  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-013 — Record and reconcile weekly transactions

**Primary actor:** User  
**Preconditions:** Finance workspace active  
**Main success flow:** Review card and account activity; stage transactions; classify category and essentiality; detect duplicates; approve and reconcile with statement.  
**Alternatives / failure behavior:** Reject conflicting duplicates, keep staged rows, report balance mismatch.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-029, LEGACY-FNC-030, LEGACY-FNC-031, LEGACY-FNC-041  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-014 — Manage bank accounts, credit cards and invoices

**Primary actor:** User  
**Preconditions:** Account and currency defined  
**Main success flow:** Create debit, savings and credit accounts; enter purchases and payments; reconcile statements.  
**Alternatives / failure behavior:** Card payment settles liability but is not a second consumption expense.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-029, LEGACY-FNC-032, LEGACY-FNC-033  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-015 — Review savings, budget performance and financial trajectory

**Primary actor:** User  
**Preconditions:** Financial entries available  
**Main success flow:** Choose period and country; inspect income, spending, savings, cash flow and net-worth projections; drill into source entries.  
**Alternatives / failure behavior:** Distinguish cash flow, gains and net worth; show FX sources and assumptions.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-035, LEGACY-FNC-036, LEGACY-FNC-039, LEGACY-FNC-043  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-016 — Remit money between UAE and Brazil

**Primary actor:** User  
**Preconditions:** Two account currencies available  
**Main success flow:** Record source and destination transfer legs with FX rate, fees and settlement dates; reconcile both accounts.  
**Alternatives / failure behavior:** Owned-account transfers are not earned income; pending/partial settlement remains visible.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-033, LEGACY-FNC-034, LEGACY-FNC-042  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-017 — Plan vehicle, property and recurring obligations

**Primary actor:** User  
**Preconditions:** Financial workspace active  
**Main success flow:** Record vehicle, apartment, subscriptions, loans and recurring commitments; select a scenario; compare 1–5 year effects.  
**Alternatives / failure behavior:** Separate principal, expense, depreciation, asset valuation and cash flow.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-036, LEGACY-FNC-037, LEGACY-FNC-038, LEGACY-FNC-039  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-018 — Import a reference financial workbook

**Primary actor:** User  
**Preconditions:** File or authorized sheet available  
**Main success flow:** Select workbook or sheet; map columns; preview normalized rows; review duplicates; approve import and reconcile.  
**Alternatives / failure behavior:** Unmapped or private data never enters the ledger without approval.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-030, LEGACY-FNC-040, LEGACY-FNC-041  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-019 — Correct and audit a transaction

**Primary actor:** User  
**Preconditions:** Transaction already exists  
**Main success flow:** Open transaction; inspect provenance and dependencies; apply correction or reversal; recompute affected reports.  
**Alternatives / failure behavior:** Preserve revision history; avoid orphaned transfer legs and duplicate expense.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-030, LEGACY-FNC-041, LEGACY-FNC-074  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-020 — Log hydration on Today

**Primary actor:** User  
**Preconditions:** Authenticated workspace  
**Main success flow:** Set target; add or correct water intake; inspect totals.  
**Alternatives / failure behavior:** Handle duplicated tap and timezone-bound day changes.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-044, LEGACY-FNC-073  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-021 — Run a named focus session

**Primary actor:** User  
**Preconditions:** Task optional  
**Main success flow:** Name session; start/pause/resume/stop timer; save duration; optionally earn a plant.  
**Alternatives / failure behavior:** Crash/reconnect must not double-count duration.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-045, LEGACY-FNC-046, LEGACY-FNC-074  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-022 — Track reading and predict completion

**Primary actor:** User  
**Preconditions:** Book and pages defined  
**Main success flow:** Add dated page update; show remaining pages, trend and estimated completion date.  
**Alternatives / failure behavior:** Show no confident estimate with insufficient history; reject pages above total.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-047, LEGACY-FNC-070  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-023 — Track game playtime

**Primary actor:** User  
**Preconditions:** Game in library  
**Main success flow:** Start and stop named game session; inspect total hours.  
**Alternatives / failure behavior:** Recover interrupted timer and avoid double stop.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-048, LEGACY-FNC-074  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-024 — Capture a movie recommendation by voice

**Primary actor:** User  
**Preconditions:** Recording permitted or text fallback  
**Main success flow:** Record suggestion; review transcript/title/recommender/date; approve watchlist entry.  
**Alternatives / failure behavior:** Missing IMDb information falls back to manual order.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-049, LEGACY-FNC-054, LEGACY-FNC-071  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-025 — Capture memory with attachments and mind map

**Primary actor:** User  
**Preconditions:** Workspace authorized  
**Main success flow:** Save text, photo, voice or linked document; tag relations; browse timeline or mind-map projection.  
**Alternatives / failure behavior:** Denied media permission still permits text; attachments remain private.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-050, LEGACY-FNC-062  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-026 — Maintain evidence-linked CV

**Primary actor:** User  
**Preconditions:** Achievement/milestone exists  
**Main success flow:** Select completed milestones and evidence; preview proposed CV change; approve and publish to selected visibility.  
**Alternatives / failure behavior:** Unapproved or private milestones are not published.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-051, LEGACY-FNC-055  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-027 — Plan activities using calendar signals

**Primary actor:** User  
**Preconditions:** Calendar permission optional  
**Main success flow:** Authorize calendar read; review conflicts and proposed daily tasks; approve schedule.  
**Alternatives / failure behavior:** Revoke integration and continue manually.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-053, LEGACY-FNC-022  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-028 — Propose an activity by natural language

**Primary actor:** User  
**Preconditions:** AI integration allowed  
**Main success flow:** Record or type intent; inspect structured draft and destination; accept correction or reject.  
**Alternatives / failure behavior:** Provider unavailable yields manual entry; no silent persistent write.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-054, LEGACY-FNC-055  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-029 — Request and release a new feature

**Primary actor:** User, administrator  
**Preconditions:** Authorized roles  
**Main success flow:** Submit idea; create structured candidate; review impact; approve; release to beta; record audit decision.  
**Alternatives / failure behavior:** Unapproved candidate never reaches production baseline.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-025, LEGACY-FNC-026, LEGACY-FNC-058  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-030 — Invite collaborator to selected goal

**Primary actor:** Owner and invitee  
**Preconditions:** Sharing enabled  
**Main success flow:** Select goal and visibility; invite collaborator; record acceptance; authorize limited contribution.  
**Alternatives / failure behavior:** Revocation removes access immediately; other private data stays inaccessible.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-024, LEGACY-FNC-056, LEGACY-FNC-057  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-031 — Switch Auto, Mobile and Desktop UI

**Primary actor:** User  
**Preconditions:** Browser loaded  
**Main success flow:** Choose display override; preserve working state; reload and verify chosen layout.  
**Alternatives / failure behavior:** Forced desktop view retains accessibility and keyboard support.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-060, LEGACY-FNC-064  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-032 — Manage household workspaces and quotas

**Primary actor:** Owner / administrator  
**Preconditions:** Role verified  
**Main success flow:** Invite user; assign role; inspect usage metadata; change quota or revoke membership.  
**Alternatives / failure behavior:** Administrator cannot automatically inspect private content.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-059, LEGACY-FNC-061  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-033 — Import GitHub issues into a weekly plan

**Primary actor:** User  
**Preconditions:** GitHub project connected  
**Main success flow:** Select repository/issue subset; preview suggested actions and references; approve candidate tasks.  
**Alternatives / failure behavior:** No issue is modified or task created without permission.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-066, LEGACY-FNC-054  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-034 — Review health or exercise trends

**Primary actor:** User  
**Preconditions:** Health module available  
**Main success flow:** Add workout or authorize source; inspect dated activity and goal trends.  
**Alternatives / failure behavior:** Avoid diagnostic inferences; show missing/uncertain data.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-052, LEGACY-FNC-022  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.

## UC-LEGACY-035 — Recover from an offline or failed edit

**Primary actor:** User  
**Preconditions:** Intermittent network  
**Main success flow:** Queue or save draft; show unsynced state; retry with same event ID; reconcile visible state.  
**Alternatives / failure behavior:** No duplicate completion/XP or lost personal content.  
**Postconditions:** Only authorized, explicitly confirmed effects are persisted; traceable evidence is recorded.  
**Linked requirements:** LEGACY-FNC-009, LEGACY-FNC-010, LEGACY-FNC-074  
**Acceptance:** Independent acceptance shall verify the happy path, authorization boundary, duplicate/retry handling and the listed alternate flow.
