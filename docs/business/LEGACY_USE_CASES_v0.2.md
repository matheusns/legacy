---
artifact_id: LEGACY-UCS-001
project: LEGAVIA
title: Legavia Use Case Specifications
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Use Case Specifications

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

## Common contract

Every use case acts on an authenticated, explicitly scoped workspace unless it is an onboarding case. Requests are validated and authorized server-side. A rejected, cancelled or unconfirmed AI/import action makes no authoritative write. Errors preserve the previous consistent record and show a next action.

### UC-001 — Open Today and execute the next action

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-004, LEGACY-FUNC-007, LEGACY-FUNC-008.

**Trigger and precondition:** User is authenticated..

**Main success scenario:** System loads today's cross-module agenda; user completes/starts an action; state and progress update..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-002 — Create a habit or routine

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-006.

**Trigger and precondition:** Workspace active..

**Main success scenario:** User selects context, schedule/target, reminder/integration, and optional goal link; system validates and saves..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-003 — Create a long-term goal and phases

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-003.

**Trigger and precondition:** Workspace active..

**Main success scenario:** User creates goal, phases, milestones, success criteria, and optional linked habits/tasks..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-004 — Navigate the goal map

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-005.

**Trigger and precondition:** At least one goal exists..

**Main success scenario:** User opens Map, selects an island/phase, inspects milestone status, and continues the next available step..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-005 — Recover after missed activity

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-006.

**Trigger and precondition:** One or more scheduled actions were missed..

**Main success scenario:** System shows a recovery summary, preserves historical continuity, and lets user resume, reschedule, or intentionally skip..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-006 — Review progress and insights

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-009.

**Trigger and precondition:** History exists..

**Main success scenario:** User selects time range/domain; system shows consistency, milestone progress, trends, and recommended review points..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-007 — Switch life modules without losing context

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-002.

**Trigger and precondition:** Multiple modules enabled..

**Main success scenario:** User switches from one top-level/module context to another and later returns to the prior state..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-008 — Use external data to auto-complete progress

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-022.

**Trigger and precondition:** Integration authorized..

**Main success scenario:** System ingests eligible external signal, maps it to a tracked item, updates progress once, and exposes provenance..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-009 — Collaborate with family on an opt-in goal

**Primary actor:** User / invited family member. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-021.

**Trigger and precondition:** Sharing explicitly enabled..

**Main success scenario:** Owner shares selected goal; collaborator sees only authorized data and contributes progress..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-010 — Submit and approve an AI-generated feature request

**Primary actor:** User / Admin. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-020.

**Trigger and precondition:** AI capture and admin role available..

**Main success scenario:** User records request; AI creates structured proposal; admin edits/approves/rejects; approved item enters beta workflow with audit trail..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-011 — Import a learning course

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-013.

**Trigger and precondition:** Learning module enabled..

**Main success scenario:** User supplies source links; AI extracts candidate modules/lessons/activities; user reviews before saving..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-012 — Review financial goal projection

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-012.

**Trigger and precondition:** Finance module enabled..

**Main success scenario:** User opens a financial goal, reviews current assumptions/imported values and projected trajectory, and updates assumptions explicitly..

**Alternative/exception flow:** Permission, validation, offline retry or empty state is handled explicitly without unintended writes.

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-013 — Run a focused work session

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-011.

**Trigger and precondition:** A workspace and optional task exist.

**Main success scenario:** Select task, start session, pause/resume and finish; record eligible duration.

**Alternative/exception flow:** Interruptions are recorded without awarding duplicate XP

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-014 — Log water intake

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-010.

**Trigger and precondition:** Workspace and local date are configured.

**Main success scenario:** Choose serving or enter volume, confirm, inspect day total and target.

**Alternative/exception flow:** Corrections must update aggregate once

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-015 — Import and reconcile financial data

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-012.

**Trigger and precondition:** Finance access and spreadsheet export are available.

**Main success scenario:** Connect or upload, preview mappings, resolve duplicates, confirm, review categories.

**Alternative/exception flow:** Reject invalid currency/date; never modify source without authorization

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-016 — Review multi-currency savings and projections

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-012.

**Trigger and precondition:** Financial actuals and assumptions exist.

**Main success scenario:** Set month, accounts, currencies, scenarios and view account transfers, savings and forecasts.

**Alternative/exception flow:** Uncertain FX estimates are labeled; remittances not double counted

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-017 — Track reading and predict finish date

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-014.

**Trigger and precondition:** A reading book exists.

**Main success scenario:** Enter pages read with date; see pace window and estimated finish; mark complete.

**Alternative/exception flow:** Insufficient history displays no false certainty

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-018 — Add a movie recommendation

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-015.

**Trigger and precondition:** User can edit personal movie queue.

**Main success scenario:** Enter or dictate film, recommender and notes; inspect rating provenance and sort.

**Alternative/exception flow:** Unavailable ratings remain explicitly unknown

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-019 — Track game play time

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-016.

**Trigger and precondition:** Game exists in library.

**Main success scenario:** Start, pause/resume and stop timer; inspect total game hours.

**Alternative/exception flow:** Duplicate stop and device retries do not double count

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-020 — Capture a memory and search it

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-017.

**Trigger and precondition:** Capture consent is available.

**Main success scenario:** Create text/voice note, review transcription, attach image, search and open.

**Alternative/exception flow:** Private media is access checked; errors keep original content

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-021 — Connect external calendar

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-018, LEGACY-FUNC-022.

**Trigger and precondition:** Provider authorization and available event permissions.

**Main success scenario:** Authorize scoped access; show agenda; link task; revoke access.

**Alternative/exception flow:** Revocation removes future access but preserves user-owned work

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-022 — Convert spoken request to daily task

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-019.

**Trigger and precondition:** Voice capture enabled.

**Main success scenario:** Speak, review structured draft, correct, approve and save.

**Alternative/exception flow:** Low-confidence parsing and rejection create no task

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-023 — Propose tasks from GitHub issues

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-022.

**Trigger and precondition:** Scoped connector and selected project or repo are available.

**Main success scenario:** Read issues, select suggestions, preview and explicitly accept tasks.

**Alternative/exception flow:** No external issue is silently edited

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-024 — Invite family member to shared goal

**Primary actor:** Workspace owner. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-021.

**Trigger and precondition:** An account and private goal exist.

**Main success scenario:** Invite member, select permission, share goal, revoke access.

**Alternative/exception flow:** Unshared user data stays inaccessible

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-025 — Switch responsive display mode

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-002.

**Trigger and precondition:** Responsive app loaded.

**Main success scenario:** Open desktop/mobile mode setting; switch; preserve route and unsaved safe UI context.

**Alternative/exception flow:** Essential actions remain available in both modes

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-026 — Review proposed CV update

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-023.

**Trigger and precondition:** Completed project/milestone evidence exists.

**Main success scenario:** Inspect suggested entry; edit and approve; publish to own CV.

**Alternative/exception flow:** No auto-publication without approval

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-027 — Export or delete personal data

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-022, LEGACY-FUNC-024.

**Trigger and precondition:** Authenticated workspace context.

**Main success scenario:** Choose portable export or deletion workflow; confirm; receive status/evidence.

**Alternative/exception flow:** Other users' content excluded; retention exceptions disclosed

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-028 — Audit user storage quota

**Primary actor:** Admin. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-021.

**Trigger and precondition:** Admin role and storage telemetry exist.

**Main success scenario:** View quota, warn user, reject oversized new uploads and inspect user controls.

**Alternative/exception flow:** Never expose private attachment content in quota UI

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-029 — Track an avoid/negative habit

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-006.

**Trigger and precondition:** Habit definition includes severity and a valid recurrence rule.

**Main success scenario:** Record occurrence, inspect elapsed-since and severity impact; correct accidental log.

**Alternative/exception flow:** No irreversible penalty or hidden user shame mechanic

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-030 — Roll out approved beta feature

**Primary actor:** Admin. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-020.

**Trigger and precondition:** Feature proposal approved and cohort defined.

**Main success scenario:** Select cohort, deploy gated version, monitor, revert; record decision.

**Alternative/exception flow:** No release before approval and security/functional gates

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-031 — Log exercise progress

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-010.

**Trigger and precondition:** Health workspace accessible.

**Main success scenario:** Create activity session, enter metrics, optionally attach to goal.

**Alternative/exception flow:** No medical diagnoses inferred from raw fitness entries

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-032 — Import handwritten notebook

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-017.

**Trigger and precondition:** Compatible export provided.

**Main success scenario:** Upload, preview extracted pages, confirm association with notes.

**Alternative/exception flow:** Failed imports leave existing notes unchanged

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


### UC-033 — Navigate the achievement and low-game modes

**Primary actor:** User. **Lifecycle:** candidate. **Functionality links:** LEGACY-FUNC-008, LEGACY-FUNC-025.

**Trigger and precondition:** User has game-progress events.

**Main success scenario:** Open Me, inspect earned rewards, switch theme; return to tasks.

**Alternative/exception flow:** Progress and essential actions unaffected by theme choice

**Postcondition and acceptance:** The result is visible on the originating and linked views after re-read, is authorized to the active workspace, persists across reload, and does not duplicate side effects on repeated submission. Where the case is read-only, no authoritative state is changed.


## Review gate

For each case, confirm that role permissions, no-data, validation-error, interrupted-network, duplicate-request, consent-revocation and phone/desktop differences are covered by an explicit test or accepted documented exclusion. Link executable test evidence only after deterministic fixture approval.
