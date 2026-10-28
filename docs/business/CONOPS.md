---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Concept of Operations (ConOps)

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

## 1. Operational context and mission
Legavia runs as a personal life-control surface through a secure browser on phone and desktop. A user starts the day on Today, checks actionable context, executes work, records outcomes, then reviews goal progression. The server is the authority for persisted entities, permissions and event-based rewards; local UI optimistically provides feedback but reconciles to the authoritative event state.

## 2. Actors, systems and trust boundaries
Primary actors: account owner, invited collaborator, workspace administrator, Systems Engineering reviewer. External systems: optional calendar/health provider, GitHub issues, AI speech/text model, finance file/Google Sheets input, reference/movie-rating service and media object storage. External services are **untrusted inputs**; connection and content scope are explicitly consented to. Private entries are never made visible by social relationship alone.

## 3. Operating modes
- **Unauthenticated:** marketing/entry/login only; no private data fetch.
- **Personal:** authenticated account and explicit active workspace, no sharing by default.
- **Collaborative:** explicit resource permission grants and revocation; collaboration cannot bypass workspace RBAC.
- **Capture:** manual, camera, audio or imported source; AI inference creates staged proposals rather than authoritative entries.
- **Intermittent connectivity:** retain visible pending/draft state with deterministic retry keys; only call an operation synchronized after server acknowledgement.
- **Adaptive display:** Auto follows browser viewport; Mobile/Desktop override affects layout only, never authorization or data.
- **Review/beta:** administrator reviews feature proposals and controls cohort releases, distinct from end-user content.

## 4. Operational scenarios
### OPS-01 — Morning activation
Authenticate → choose private workspace → load Today dashboard (tasks, goals, due habits, water, focus and calendar context if authorized) → choose next action → complete once → see updated task, milestone, XP and insight projections. A duplicated tap or retried request must not mint additional XP.

### OPS-02 — Structured long-term goal
Create goal → phases/islands → milestone with completion criteria → linked actionable task → visualize locked/available/in-progress/completed states → complete task and recompute progress. The map is a projection of the canonical goal graph, not a second independent source of truth.

### OPS-03 — Recovery and self-regulation
After missed days, show a recovery option, not a destructive reset. The user may reschedule, deliberately skip or resume. Negative habits may carry user-configured severity; consequences must be explicit, reversible where appropriate and never punish health-related behavior in an unsafe manner.

### OPS-04 — Capture via voice and AI
User gives a spoken instruction → receive transparent transcript/structured proposal → correct intent, destination and permissions → approve → persist with origin/provenance → show undo where applicable. Missing microphone permission, AI failure or disagreement routes to manual entry.

### OPS-05 — Financial review
Import or enter transaction data → stage, classify and reconcile per account → distinguish transfers/expenses/income/valuation → review monthly and multiyear projections with uncertainty. Original currency and external source provenance remain immutable in the source ledger; corrections are revisioned, not silent overwrites.

### OPS-06 — Shared goal
Owner chooses a goal and selected invited users → grants bounded access → invited user sees only granted content → contributes progress → revocation removes access and invalidates cached shared context. Friendship, household membership and social participation do not imply universal read rights.

### OPS-07 — Focus/reading/memory
Start a named focus timer, read a book, or capture media → persist dated events with stable IDs → derive plant growth, page completion prediction or memory map → recover interrupted sessions without duplicating events.

### OPS-08 — User requests product evolution
User submits idea → AI creates proposal with requirements/acceptance candidates → authorized administrator reviews → Systems Engineering approves controlled baseline change → beta release to explicit cohort → monitor, accept or roll back. Product requests and user content remain distinct trust domains.

## 5. Information exchange and failures
Canonical domain commands include CreateGoal, LinkTask, CompleteAction, UndoCompletion, LogHabit, RecordFocusEvent, RecordHydration, ProposeCapture, ApproveProposal, ImportBatch, GrantResourceAccess and RevokeResourceAccess. Each mutation binds authenticated principal, workspace, event key, data version and audit metadata. Timeout/retry returns committed result or safe conflict; it never blindly replays economic or XP effects.

## 6. Operational constraints
Require explicit timezones for dates, deterministic amount calculations, at-rest/in-transit encryption, server-side permission checks, accessible keyboard/tap alternatives, bounded media uploads and data export/deletion policy. AI must not receive the entire user's personal dataset merely to answer a local task request. Hosted infrastructure and numerical SLOs require approved architecture.

## 7. Transition and decommissioning
Import from spreadsheets/legacy app only after schema preview and user confirmation. Preserve provenance and migration checkpoints. Provide user data export and deletion lifecycle before production migration, including attachment retention and backups per published policy.
