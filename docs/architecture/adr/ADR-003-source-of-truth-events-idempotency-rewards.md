# ADR-003 — Source of truth, immutable domain events, idempotency, projections, undo and rewards

## Status

Proposed — 2026-10-30. Awaiting explicit Systems Engineering acceptance; this record is not accepted and grants nothing until a human reviewer changes this section and the control manifest records the artifact.

Resolves candidate register item `ADR-CAND-003` and decision `DEC-003` of LEGACY-SE-REVIEW-001. Governs the design of FVT-LEGACY-001, FVT-LEGACY-015, FVT-LEGACY-019 and FVT-LEGACY-023.

## Traceability

- Functionalities: `LEGACY-CAP-003`, `LEGACY-CAP-004`, `LEGACY-CAP-002`
- Requirements: `LEGACY-BIZ-002`, `LEGACY-FNC-003`, `LEGACY-FNC-004`, `LEGACY-FNC-009`, `LEGACY-FNC-010`, `LEGACY-FNC-011`, `LEGACY-FNC-013`, `LEGACY-FNC-014`, `LEGACY-FNC-015`, `LEGACY-FNC-016`, `LEGACY-FNC-068`, `LEGACY-FNC-069`, `LEGACY-FNC-074`, `LEGACY-NFR-005`, `LEGACY-NFR-010`, `LEGACY-NFR-014`, `LEGACY-NFR-022`, `LEGACY-UX-021`
- Use cases: UC-LEGACY-001, UC-LEGACY-003, UC-LEGACY-004, UC-LEGACY-005, UC-LEGACY-035
- Work package: `LEGACY-WORK-002` (acceptance topics: source of truth, event idempotency)
- Decision owner: Systems Engineering
- Prepared in run `DEV-20261030T185520Z-751CB5` against control commit `caca50c7e23a892d37e63cc14091f8cf725374d6`

## Context

The baseline requires that a completion updates the item, milestone progress, analytics and gamification state atomically (`LEGACY-FNC-009`), that undo removes only the matching effects (`LEGACY-FNC-010`), that repeated submissions yield one logical event and one reward (`LEGACY-NFR-005`, `LEGACY-NFR-014`), that XP, levels, badges and currency are computed from a deterministic event ledger with visible explanations (`LEGACY-FNC-069`, `LEGACY-UX-021`), and that every progress- or finance-affecting mutation keeps a stable event identity, origin and compensating history (`LEGACY-FNC-074`). CONOPS states that "the server is the authority for persisted entities, permissions and event-based rewards; local UI optimistically provides feedback but reconciles to the authoritative event state", and that the map is a projection of the canonical goal graph, not a second source of truth (OPS-02; AGENTS.md map rule). `DOMAIN_MODEL.md` already sketches `DomainEvent(event_id, actor, workspace, origin, occurred_at, idempotency_key, version)`, `Completion`, `Reversal`, `RewardTransaction` and the rule "repeated key with different payload returns a deterministic conflict".

The exploratory mockups keep state in browser `localStorage`; `legacy_mockups` explicitly disclaims backend or security meaning. The reference baseline principle DP-02 ("one core graph, many views") and invariant 2 (no game-only maintenance) constrain how rewards may be derived.

## Decision

### D1. Source of truth

1. **The server-side PostgreSQL database of ADR-001 is the single source of truth** for all domain state, permissions and rewards. The browser holds a cache plus unsynchronised drafts (ADR-006); mockup or local storage state is never authoritative and is never imported as fact.
2. Within the database, **authoritative facts are the append-only `domain_events` ledger together with the current-state aggregate tables written in the same transaction**. Today, Map, Insights, XP/levels, skills, continuity, forest state, quests and achievements are **projections**: deterministic read models that can be rebuilt from the ledger (D5). The Goal → Phase → Milestone → Action graph is stored once; the Map renders it with theme metadata and never holds its own progress state (`LEGACY-FNC-003`, `LEGACY-FNC-004`).
3. The control repository `legacy` remains the source of truth for contracts and acceptance meaning; this ADR concerns runtime data only.

### D2. Command envelope and idempotency

4. Every mutation is a **command** with the envelope `{ command_type, idempotency_key, workspace_id, aggregate_id?, expected_version?, payload, client_occurred_at, client_tz }` authenticated by the ADR-002 `AuthContext`. The **idempotency key is a client-generated UUIDv7 per user intent**, created when the user acts (tap, submit), persisted in the client draft store before the request, and reused verbatim on every retry.
5. The server stores `(workspace_id, idempotency_key)` as a **unique constraint** on an `idempotency_receipts` table that records the command fingerprint (SHA-256 of canonical payload), resulting event IDs and the response body. Semantics:
   - unseen key → execute in one transaction, store receipt, respond `201`;
   - seen key with identical fingerprint → **do not execute**, return the stored response with `200` and an `Idempotent-Replay: true` header;
   - seen key with different fingerprint → `409 Conflict` with the original event ID; no side effects.
   Receipts are retained for at least 30 days, longer than any offline retry window permitted by ADR-006.
6. `expected_version` enables optimistic concurrency on aggregates; a mismatch returns `409` with the current version and the events since the expected version, so the client can reconcile instead of overwriting.

### D3. One transaction, one event set, one reward

7. A command handler runs in a **single database transaction** that (a) validates against the aggregate's current state, (b) appends one or more `domain_events`, (c) applies them to current-state tables, (d) appends zero or more `reward_transactions` computed by the pure reward policy from those events, (e) updates synchronous projections, (f) writes the idempotency receipt. Partial application is impossible; this satisfies `LEGACY-FNC-009`, `LEGACY-NFR-010` and `LEGACY-NFR-014` with database semantics rather than application retries.
8. `domain_events` schema: `event_id (UUIDv7, PK)`, `workspace_id`, `aggregate_type`, `aggregate_id`, `aggregate_version`, `event_type`, `payload (jsonb, schema-versioned)`, `actor_principal_id`, `origin ∈ {manual, import, ai_proposal, integration, system}`, `causation_event_id`, `correlation_id (= idempotency_key)`, `occurred_at timestamptz`, `occurred_tz`, `occurred_local_date`, `recorded_at`. Rows are **never updated or deleted** by application code; corrections are new events (`LEGACY-FNC-074`, `LEGACY-NFR-022`).
9. `reward_transactions` schema: `reward_tx_id`, `workspace_id`, `principal_id`, `source_event_id` (unique per reward kind), `kind ∈ {xp_global, xp_skill, coin, achievement_progress, quest_progress}`, `skill_id?`, `amount (integer, signed)`, `policy_version`, `explanation (structured)`, `reverses_reward_tx_id?`. The uniqueness of `(source_event_id, kind, skill_id)` is the **database-level guarantee against double XP** (`LEGACY-NFR-005`).

### D4. Undo and compensation

10. **Undo is a compensating event**, never a delete: `UndoCompletion` appends `CompletionReversed { reverses_event_id }`, restores the item's state, and appends negative `reward_transactions` referencing the originals. Unrelated progress is untouched because compensation is scoped to the reversed event's own effects (`LEGACY-FNC-010`). Undo of an already-reversed event is idempotent (`409` with the existing reversal).
11. Milestone and goal completion derived from a reversed action are recomputed by the projection, so a milestone can return to `in_progress`; achievements already granted are marked `revoked` with explanation rather than erased, keeping the history honest (`LEGACY-UX-021`).

### D5. Projections and rebuild

12. Projections are written synchronously in the command transaction for S1–S3 (no broker). Each projection has a **pure, versioned reducer** `(state, event) → state` in `packages/domain` and a `rebuild` job that replays the ledger per workspace; rebuild equality with incremental state is a required test (ADR-005). Continuity (`LEGACY-FNC-011`), streak with grace (`LEGACY-FNC-012`), habit severity and recovery (`LEGACY-FNC-068`), quests (`LEGACY-FNC-016`) and achievements (`LEGACY-FNC-014`) are all reducers over the same ledger; none introduces a new fact table.
13. **Reward policy is configuration, versioned and pure**: `(event, policy_version) → reward_transactions[]`. Changing XP values creates a new `policy_version`; historical rewards are not recomputed unless an explicit migration event is appended. Caps and diminishing returns (reference RISK-07) are policy parameters. Virtual currency never gates core functionality (`LEGACY-FNC-015`).
14. **Explanations are stored, not inferred**: every reward transaction carries the structured reason (`event_type`, difficulty weight, multipliers, cap applied) rendered verbatim in Me and Insights.

### D6. Time semantics

15. Scheduling (habit due dates, "today", day boundaries, grace windows) uses the **workspace member's IANA time zone at `occurred_at`**, stored on the event as `occurred_tz` and `occurred_local_date`. Day-boundary projections (hydration totals, daily quests) group by `occurred_local_date`, never by UTC date (FVT-LEGACY-019 midnight case). Timezone changes append a `PreferenceChanged` event; past local dates are not rewritten.

## Considered alternatives

- **CRUD tables with an audit log on the side.** Rejected: an after-the-fact audit log cannot guarantee that rewards were derived from exactly one event, and undo would become ad-hoc reverse mutations.
- **Full event sourcing (no current-state tables, rebuild on read) with an external broker.** Rejected for S1–S3: higher operational and cognitive cost; synchronous projections in one transaction meet the atomicity and immediacy requirements. Asynchronous projections may be introduced later for heavy analytics without changing the ledger.
- **Server-generated idempotency keys (e.g. hash of payload + time window).** Rejected: a user may legitimately log two identical hydration entries within seconds; intent identity must come from the client action.
- **Reward recalculation on policy change (retroactive).** Rejected: contradicts "visible explanations" and would alter history; forward-only policy versions are chosen.
- **Hard delete on undo.** Rejected: violates `LEGACY-FNC-074` and breaks explanations.

## Consequences

### Positive

- Exactly-once reward and completion effects are enforced by unique constraints and one transaction, which FVT-LEGACY-001/015/023 can verify by replaying requests.
- Every number on Me and Insights can be explained from stored reward transactions; rebuild tests detect projection drift.
- The Map is provably a view of the goal graph, satisfying the AGENTS.md map rule and `LEGACY-BIZ-002`.

### Negative

- Every module must express mutations as commands and events; quick CRUD shortcuts are not available.
- Synchronous projections lengthen the command transaction; the number of projections per command must stay bounded (monitor in ADR-005 integration tests).
- Idempotency receipts and ledger growth require retention and partitioning planning before S4 data volumes.

## Control provenance

Prepared by the Systems Engineering control-plane agent (Claude Fable 5.1, Claude Code) for LEGACY-WORK-002 as a reviewable proposal. Inputs: `DOMAIN_MODEL.md` "Data and event rules", `CONOPS.md` sections 1, 5 and OPS-01/02/03/07, `VERIFICATION_AND_ACCEPTANCE.md` FVT-001/003/015/019/023, reference baseline sections 7 and 14. Acceptance requires a human Systems Engineering decision.
