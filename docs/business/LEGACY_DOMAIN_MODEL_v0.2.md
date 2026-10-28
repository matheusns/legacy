---
artifact_id: LEGACY-DOMAIN-001
project: LEGAVIA
title: Legavia Domain Model and Data Contracts
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Domain Model and Data Contracts

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

## Shared aggregate boundaries

| Aggregate / entity | Key properties (conceptual) | Invariants |
|---|---|---|
| User / Workspace / Membership | user_id, workspace_id, role, consent, state | No cross-tenant read/write without explicit, revocable permission |
| Goal / Phase / Milestone | id, parent_id, status, criterion, dependencies, target_date | Parent/child graph has no cycles; Map references source IDs, not duplicated goals |
| Task / Schedule / Habit / Occurrence | owner, due_at, recurrence, goal_id, event_id, timezone | Schedule/occurrence distinct from single completion; user can correct occurrence |
| CompletionEvent / ReversalEvent | idempotency_key, entity_id, actor_id, occurred_at, supersedes | Uniqueness enforced per workspace + source command; reversal references original event |
| XPTransaction / RewardTransaction | source_event_id, amount, reward_type, reversal_ref | Exactly-once credit per eligible action; never derived from UI click count |
| FocusSession | task_id, start/stop/pause epochs, elapsed_ms, eligible_duration | Time overlap and repeated stop do not inflate credited time |
| HydrationEntry | quantity_ml, local_day, recorded_at, source | Correcting/deleting entry causes deterministic recalculation of daily totals |
| FinancialAccount / Transaction / Transfer / FXRate / Projection | currency, amount_minor, account, category, import_key, scenario | Account transfer pairs net to zero in income/expense; cash and unrealized estimates segregated |
| Book / ReadingObservation | pages_total, page_offset, observed_at, status | Reading progress bounded to [0,total]; prediction is derivative and optional |
| Film / Recommendation | title, recommender, captured_at, external_rating, retrieved_at | Rating unknown does not imply zero and attribution is preserved |
| Game / PlaySession | game_id, opened_at, closed_at, paused_intervals | No overlapping active sessions on one timer; total derived from sessions |
| Course / Module / Lesson / Activity | hierarchy, duration, resources, completed_at | Imported extraction is draft until reviewed |
| Memory / MediaAttachment / Relation | source format, transcription, media pointer, ACL, created_at | Attachments and index always follow ownership rules |
| FeatureProposal / Approval / Rollout | source_input, revision, reviewer, status, cohort, audit_event | AI cannot transition to approved/released without authorized actor and gates |
| ImportJob / SourceRecord | provider, external_id, checksum, source_version, status | Preview + approval + deterministic deduplication before authoritative commit |
| CVEntry / SuggestedUpdate | provenance, proposed_content, review state | Auto suggestion never equals publication |

## Transactional integrity and event processing

**Command:** authorize → validate → compute idempotency scope → write source event and required atomic ledger entries → materialize views or process via outbox. A retry returns the same logical result; concurrency must not mint duplicate rewards. Undo/reverse creates a compensating event, never erases unrelated business history. Read projections are rebuildable and cannot be treated as independent truth.

**Time:** persist UTC instants and explicit IANA timezone/offset metadata where required; represent user-local due dates separately from instants. Money is represented in smallest units with ISO 4217 currency identifiers and source/exchange-rate metadata (precision and rounding ADR required). A book estimate uses an explicitly defined sample window and missing-data behavior.

**Privacy:** every record, media pointer, import job, search index and async job includes tenant scope and permission checks. Use least-privilege connection tokens and avoid raw private content in engineering evidence. Shared objects have explicit membership edges; revocation invalidates future reads. AI context contains only user-approved information.

## Logical API/event candidates (architecture approval pending)

`CreateGoal`, `CreateTask`, `CompleteAction`, `ReverseCompletion`, `LogWater`, `CloseFocusSession`, `ApproveImport`, `GrantShare`, `RevokeShare`, `ApproveFeatureProposal`, `StartBeta`; event names `ActionCompleted`, `CompletionReversed`, `WaterEntryRecorded`, `ImportApproved`, `WorkspaceAccessRevoked`.

Endpoints, schema migrations, event transport and database selection must be governed by an ADR and contract tests. These names are design concepts, not implemented APIs.
