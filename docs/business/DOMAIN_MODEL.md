---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Conceptual Domain Model and Invariants

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

## Canonical entities (candidate)
| Aggregate | Core fields and relationships | Key invariant |
| --- | --- | --- |
| Identity & Access | User, Workspace, Membership, Role, ResourceGrant, AuditEvent, FeatureFlag, StorageUsage | Owner/workspace mandatory; grant is resource-specific; admin metadata access ≠ content access |
| Goal execution | Goal → Phase → Milestone → Action/Task; Schedule; Checklist; Habit; Routine | Map, Today and Insights are projections of shared entities |
| Event ledger | DomainEvent(event_id, actor, workspace, origin, occurred_at, idempotency_key, version), Completion, Reversal, RewardTransaction | Exactly-once user-intent mutation; compensating undo; no double XP |
| Time/Wellness | FocusSession, TimerEvent, HydrationEntry, ExerciseEvent, HealthSource | Elapsed time reconstructed from events; no medical diagnosis |
| Learning/Media | Course, Module, Lesson, LearningActivity, Book, ReadingProgress, Game, PlaySession, MovieRecommendation | Dated observations; predictions and ratings are derived, not source facts |
| Knowledge | MemoryEntry, Attachment, VoiceTranscript, Tag, ConceptLink, SourceDocument | Private media access scoped; mind map is a query view |
| Finance | FinancialAccount, CreditCard, Transaction, Posting, Transfer, ImportBatch, Category, Budget, Scenario, Asset, Liability | Fixed-point money; balance = postings; transfers ≠ income; immutable provenance |
| Integration/AI | ExternalConnection, ConsentGrant, ImportJob, Proposal, ApprovalDecision, ProviderReference | No provider auto-commits; explicit approval, limited scopes and revocation |
| Collaboration | Friendship, SharedGoal, Challenge, SocialEvent, ResourceVisibility | Friendship does not create permissions; public is opt-in |

## Data and event rules
- Every mutable domain aggregate has stable ID, owner/workspace, created_at, updated_at, expected_version and, when imported, source_type/source_record_id.
- Commands use a client-supplied stable idempotency key. A repeated key with different payload returns a deterministic conflict, not new side effects.
- Completing an action atomically appends a completion event and one reward transaction. Reversal references the original completion and posts compensating reward entries; existing unrelated progress is unchanged.
- Goal/milestone/map, personal-level XP, forest state, trends, finish-date predictions and financial forecasts are deterministic read projections over authoritative records.
- Financial postings are decimal or minor-unit integers per currency; card purchases increase expense and payable, card payments settle payable but not expense. Fees and currency conversions are separate posted components.
- Dated reading progress must be monotonic unless an explicit correction is recorded; insufficient observations produce an undetermined completion date rather than fabricated certainty.
- Timer state transitions are validated; missing stop is displayed as an interrupted/pending session, not silently counted as a full interval.
- All import and AI proposals use staging collections; promotion requires authenticated review action.

## Sensitivity classification
**Restricted:** finance records, personal health records, raw voice recordings, private photos/memories, account tokens and personal contact data. **Internal:** user activity plans, goals and achievements. **Shareable only on permission:** explicitly selected social goal and CV fields. **Public by design:** generic UI artwork, code and synthetic test fixtures. No Restricted data in repository history, telemetry, generated AI tests or public screenshot fixtures.

## Candidate architectural boundaries
App shell / UI adapters, identity & policy, goal/task/habit domain, event and reward engine, specialist modules, import/AI boundary, read-model analytics, object storage and independent verification adapters. Split as logical modules before adding microservices. Database/provider selection is an ADR, not a baseline assumption.
