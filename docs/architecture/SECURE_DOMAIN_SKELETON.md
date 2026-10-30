---
project: LEGAVIA
artifact_id: LEGACY-ARCH-SKELETON-001
artifact_type: architecture_definition
artifact_status: proposed-candidate
version: 0.1.0
date: 2026-10-30
control_repository: matheusns/legacy
work_package: LEGACY-WORK-002
run_id: DEV-20261030T185520Z-751CB5
review_gate: Systems Engineering acceptance required
---

# Secure domain skeleton — controlled definition for `legacy_app`

> **Proposed candidate.** This document defines the skeleton that `LEGACY-WORK-003` implements once ADR-001..ADR-007 are accepted. It is a control-plane definition, not code; no product repository was modified. Where it names a file or package it describes the required shape, and the implementing work package may propose adjustments through Systems Engineering.

## 1. Purpose and boundaries

The skeleton makes the cross-cutting invariants of the baseline impossible to bypass in the first slice: workspace tenancy with resource-level grants (ADR-002), a single transactional source of truth with an immutable event ledger and idempotent commands (ADR-003), typed shared contracts (ADR-001), deterministic testability (ADR-005), draft/retry semantics (ADR-006) and a reserved AI boundary (ADR-007). It covers the capabilities allocated to this work package, `LEGACY-CAP-001`, `LEGACY-CAP-003` and `LEGACY-CAP-004`, and reserves seams for the others without implementing them (`LEGACY-BIZ-004`).

## 2. Package layout (ADR-001 D1)

```
legacy_app/
  apps/
    api/            Fastify server: route registry, auth edge, command bus, projections, storage adapters
    web/            React + Vite PWA: shell, surfaces, draft store, API client generated from contracts
  packages/
    domain/         Pure TypeScript: aggregates, commands, events, reducers, reward policy, continuity, value types
    contracts/      Zod schemas + types for commands, queries, events, API responses; OpenAPI generated from them
    design-tokens/  Token JSON → CSS custom properties (ADR-004 D2)
    testkit/        Scenario fixtures, Clock, builders, authorization-matrix generator (ADR-005)
    ai-boundary/    Provider port and adapters; no database access (ADR-007)
  assets/           Production artwork + ASSET_MANIFEST.json (ADR-004 D1)
  infra/            Dockerfile, docker-compose (postgres, storage), migration runner
```

Dependency rule: `domain` ← `contracts` ← (`api`, `web`, `testkit`, `ai-boundary`). Nothing imports from `apps/*`. The rule is enforced in CI.

## 3. Shared value types (`packages/domain`)

| Type | Definition | Source |
| --- | --- | --- |
| `Id` | UUIDv7 string, server-generated, except `IdempotencyKey` and draft IDs (client) | ADR-001 D4(12), ADR-003 D2 |
| `Instant` | ISO-8601 UTC string ↔ `timestamptz` | ADR-001 D4(12) |
| `LocalDateTz` | `{ local_date: YYYY-MM-DD, tz: IANA }` derived at event time | ADR-003 D6, `LEGACY-NFR-022` |
| `Money` | `{ minor: bigint, currency: ISO-4217, scale: int }`; arithmetic only through `Money.add/sub/allocate`; FX requires `{ rate, source, at }` | ADR-001 D4(12), `LEGACY-NFR-011` |
| `WorkspaceId`, `PrincipalId` | branded `Id`s so a goal ID cannot be passed where a workspace ID is expected | ADR-002 |
| `Origin` | `manual | import | ai_proposal | integration | system` | ADR-003 D3 |
| `Sensitivity` | `restricted | internal | shareable | public` annotation used by export/redaction | `DOMAIN_MODEL.md` |

## 4. Aggregates in the first slice

| Aggregate | Owner capability | Key fields | Invariants enforced in `domain` |
| --- | --- | --- | --- |
| `User` | CAP-001 | id, email (verified_at), display_name, tz, created_at | one personal workspace; tz is IANA |
| `Workspace` | CAP-001 | id, kind ∈ personal\|shared, owner_principal_id, name, created_at | exactly one owner; personal workspace cannot be shared-kind |
| `Membership` | CAP-001 | workspace_id, principal_id, role ∈ owner\|admin\|member, invited_by, accepted_at, revoked_at | no implicit content access; admin ≠ content |
| `ResourceGrant` | CAP-001 | per ADR-002 D2(6) | resource-specific; revocation immediate; private default |
| `Session` | CAP-001 | id, principal_id, created_at, last_seen_at, expires_at, rotated_from | server-side only; rotation on privilege change |
| `AuditEvent` | CAP-001 | append-only, per ADR-002 D3(12) | never deleted |
| `Goal` | CAP-003 | id, workspace_id, title, horizon ∈ long\|mid\|short, parent_goal_id?, theme_ref?, status, version | horizons form a tree; theme is presentation metadata only |
| `Phase` | CAP-003 | id, goal_id, order, title, unlock_rule, status (derived) | ordered; status derived from milestones |
| `Milestone` | CAP-003 | id, phase_id, order, title, completion_criteria, status (derived: locked\|available\|in_progress\|completed) | status is a projection of linked action completions |
| `Action` (task) | CAP-002/003 | id, workspace_id, milestone_id?, module_ref?, title, due (LocalDateTz), priority, checklist[], status, version | one owning workspace; optional single milestone link |
| `Habit` | CAP-004 | id, workspace_id, schedule (daily\|selected_days\|interval\|target_per_period), polarity, severity, recovery_policy, version | schedule evaluated in member tz |
| `Routine` | CAP-004 | id, ordered habit/action refs | P1 placeholder, schema reserved |
| `Completion` (event-backed) | CAP-004 | event `ActionCompleted`/`HabitLogged` with `LocalDateTz` | exactly-once by idempotency key |
| `RewardTransaction` | CAP-004 | per ADR-003 D3(9) | unique `(source_event_id, kind, skill_id)` |
| `IdempotencyReceipt` | cross-cutting | per ADR-003 D2(5) | unique `(workspace_id, idempotency_key)` |
| `DomainEvent` | cross-cutting | per ADR-003 D3(8) | append-only, immutable `workspace_id` |

Reserved seams (tables and packages not created in S1 but named so later modules do not fork the core): `FocusSession`, `HydrationEntry`, `FinancialAccount/Transaction/Posting/Transfer`, `MemoryEntry/Attachment`, `Course/Lesson`, `Proposal/ConsentGrant/ExternalConnection`, `FeatureFlag`, `StorageUsage`.

## 5. Command and event catalogue (first slice)

| Command (CONOPS §5) | Precondition policy (ADR-002 D3) | Events appended | Reward policy input |
| --- | --- | --- | --- |
| `CreateWorkspace`, `InviteMember`, `AcceptInvitation`, `RevokeMembership` | owner/admin | `WorkspaceCreated`, `MemberInvited`, `MembershipAccepted`, `MembershipRevoked` (+ AuditEvent) | none |
| `GrantResourceAccess`, `RevokeResourceAccess` | `resource_capability(manage)` or owner | `ResourceGranted`, `ResourceRevoked` (+ AuditEvent) | none |
| `CreateGoal`, `AddPhase`, `AddMilestone`, `ArchiveGoal` | `workspace_member` + author or `contribute` grant | `GoalCreated`, `PhaseAdded`, `MilestoneAdded`, `GoalArchived` | none |
| `CreateAction`, `LinkTask` (action ↔ milestone), `RescheduleAction` | as above | `ActionCreated`, `ActionLinked`, `ActionRescheduled` | none |
| `CompleteAction` | as above | `ActionCompleted {local_date, tz}` → projection may append `MilestoneCompleted`, `PhaseCompleted`, `GoalCompleted` | yes: xp_global, xp_skill, achievement_progress, quest_progress |
| `UndoCompletion` | author of original or `manage` | `CompletionReversed {reverses_event_id}` → projection may append `MilestoneReopened` | yes: negative mirror of originals |
| `CreateHabit`, `LogHabit`, `SkipHabit`, `ResumeHabit` | as above | `HabitCreated`, `HabitLogged`, `HabitSkipped`, `HabitResumed` | yes for `HabitLogged`; continuity reducer for all |
| `UpdatePreferences` (tz, display mode, low-gamification) | `self_only` | `PreferenceChanged` | none; display preferences are client-side except tz |

Rules: every command carries `IdempotencyKey`, `expected_version?`, `client_occurred_at`, `client_tz`; every handler runs in one transaction (ADR-003 D3); projections `TodayAgenda`, `MapGraph`, `MilestoneProgress`, `XPLedgerView`, `SkillLevels`, `Continuity`, `InsightsDaily` are reducers with rebuild jobs (ADR-003 D5).

## 6. Authorization context and enforcement points (ADR-002)

1. `apps/api` resolves `AuthContext` from the session cookie once per request; anonymous requests reach only `public` routes (`/api/v1/auth/*`, `/api/v1/meta/candidate`, static assets).
2. The **route registry** is a typed table `{ method, path, policy, command|query schema, idempotent: boolean, fvt_refs[] }`; startup fails on a route without a policy; the authorization-matrix generator (ADR-005 D1) reads this table.
3. Repositories accept `AuthContext` and are the only database access path; a lint rule forbids raw SQL outside `apps/api/src/persistence`.
4. Each request transaction executes `SET LOCAL app.principal_id`, `SET LOCAL app.workspace_id`; RLS policies on every `workspace_id` table allow rows of the active workspace plus rows reachable through an active `ResourceGrant`; the application database role cannot bypass RLS; migrations use a separate role.
5. `workspace_id` columns are immutable by trigger; attempted reassignment is rejected at the schema validation layer and, if it got through, by the database.
6. Admin projections (`WorkspaceMembersView`, `StorageUsageView`, `AuditView`) contain metadata only.

## 7. Database schema sketch (PostgreSQL, ADR-001 D4)

Tables in the first migration set: `users`, `workspaces`, `memberships`, `resource_grants`, `sessions`, `audit_events`, `goals`, `phases`, `milestones`, `actions`, `habits`, `habit_schedules`, `domain_events`, `reward_transactions`, `idempotency_receipts`, `projection_milestone_progress`, `projection_xp_ledger`, `projection_continuity`, `preferences`, `schema_meta`. Conventions: `id uuid primary key`, `workspace_id uuid not null references workspaces`, `created_at timestamptz`, `updated_at timestamptz`, `version integer`, `sensitivity` comment annotation; unique constraints per ADR-003 D2(5) and D3(9); indexes on `(workspace_id, aggregate_id, aggregate_version)` for `domain_events` and on `(workspace_id, occurred_local_date)` for day-bounded projections.

## 8. API conventions (`apps/api`)

- Base path `/api/v1`; JSON only; errors use RFC 9457 problem details with a stable `code` (`not_found`, `forbidden`, `conflict_version`, `conflict_idempotency`, `already_completed`, `gone`, `validation`).
- Mutations: `POST /api/v1/commands/<CommandType>` with the ADR-003 envelope; responses `201` (executed), `200 + Idempotent-Replay: true` (replay), `409` (conflict), `410` (gone).
- Queries: `GET /api/v1/workspaces/{ws}/today`, `/map`, `/goals/{id}`, `/me/xp-ledger`, `/insights?range=`; all require membership or grant; nested IDs resolve parent-first.
- Fixture mode (`LEGAVIA_FIXTURE_MODE=1`, local database URL only): `POST /api/v1/_fixture/load` (ADR-005 D2). Production builds assert the flag is unset at startup.
- OpenAPI document generated from `packages/contracts` and published as a build artefact; the web client is generated from it.

## 9. Client skeleton (`apps/web`)

- Shell with five surfaces and preserved per-surface navigation state (`LEGACY-UX-003`, `LEGACY-UX-010`); `Auto | Mobile | Desktop` display mode and low-gamification mode as token-layer switches (ADR-004 D2(10)).
- Draft store in IndexedDB with pending/conflict states and retry (ADR-006 D1–D2); every mutation goes through `sendCommand(command)` which assigns the idempotency key before the first attempt.
- State panels (loading, empty with next action, error with retry, permission denied, pending) are shared components, so `LEGACY-UX-012` and `LEGACY-UX-007` are satisfied structurally.

## 10. Deterministic test scaffold (ADR-005)

- `packages/testkit/scenarios/S2-first-journey.json` (ADR-005 D2(3)); `Clock` port with `FixedClock` for tests.
- Authorization-matrix test generated from the route registry; projection rebuild equality test; idempotency replay/conflict tests for every command; money and local-date property tests.
- `GET /api/v1/meta/candidate` for fingerprinting; CI publishes `candidate.json`.

## 11. Out of scope for the skeleton

Finance ledger and computation contracts (`DEC-013`, deferred to a `LEGACY-WORK-010` predecessor), focus/hydration modules, memories and attachments beyond the storage port, AI provider adapters beyond the port, social challenges, installed-PWA evidence (`DEC-015`), and any visual asset approval (`DEC-010`).

## 12. Trace to work package acceptance criteria

| LEGACY-WORK-002 criterion | Where satisfied (proposed) |
| --- | --- |
| Accepted ADRs for identity/tenancy | ADR-002 |
| … source of truth | ADR-003 D1 (+ ADR-001 D4) |
| … event idempotency | ADR-003 D2–D4 |
| … app stack | ADR-001 D1–D3 |
| … assets | ADR-004 |
| … hosting | ADR-001 D5 |
| … testability | ADR-005 |
| Trace from controlled requirements to review evidence | each ADR "Traceability" block; `docs/architecture/adr/README.md` register; LEGACY-SE-REVIEW-002 |
| Preserve privacy and tenant isolation; candidate fingerprint and reviewer disposition | ADR-002, ADR-006 D3(10), ADR-007 D2; fingerprints and disposition table in LEGACY-SE-REVIEW-002 |
| SE review and baseline identification; no runtime unit test | LEGACY-SE-REVIEW-002 sections 1 and 9 |
