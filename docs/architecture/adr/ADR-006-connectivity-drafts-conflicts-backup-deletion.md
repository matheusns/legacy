# ADR-006 — Intermittent connectivity, drafts and retry, conflict resolution, backup, restore, retention and deletion

## Status

Proposed — 2026-10-30. Awaiting explicit Systems Engineering acceptance; this record is not accepted and grants nothing until a human reviewer changes this section and the control manifest records the artifact.

Resolves candidate register item `ADR-CAND-006` and decision `DEC-006` of LEGACY-SE-REVIEW-001. Scope note: this ADR fixes the invariants the S1/S2 skeleton must honour and the policy for S3; it does not claim offline synchronisation capability.

## Traceability

- Functionalities: `LEGACY-CAP-001`, `LEGACY-CAP-002`, `LEGACY-CAP-004`
- Requirements: `LEGACY-FNC-009`, `LEGACY-FNC-010`, `LEGACY-FNC-023`, `LEGACY-FNC-062`, `LEGACY-FNC-064`, `LEGACY-FNC-074`, `LEGACY-NFR-004`, `LEGACY-NFR-005`, `LEGACY-NFR-012`, `LEGACY-NFR-016`, `LEGACY-NFR-017`, `LEGACY-NFR-021`
- Use cases: UC-LEGACY-035, UC-LEGACY-001
- Work package: `LEGACY-WORK-002`; consumers `LEGACY-WORK-003`, `LEGACY-WORK-005`
- Decision owner: Systems Engineering
- Prepared in run `DEV-20261030T185520Z-751CB5` against control commit `caca50c7e23a892d37e63cc14091f8cf725374d6`

## Context

The baseline distinguishes two things that are easy to conflate: a **recoverable draft or retry state** for interrupted requests, required now (`LEGACY-NFR-016`, P0), and **offline synchronisation**, a P1 aspiration (`LEGACY-NFR-004`) that "shall not be claimed until independently verified". CONOPS mode "Intermittent connectivity" says: retain visible pending/draft state with deterministic retry keys; call an operation synchronised only after server acknowledgement. `LEGACY-FNC-064` requires session navigation and allowed local draft state to survive reload. `LEGACY-NFR-017` requires documented backup, restore, retention and recovery testing before irreplaceable memories or finance records are stored; `LEGACY-FNC-062` and `LEGACY-NFR-012` require user-controlled export and deletion. ADR-003 already provides client-generated idempotency keys and `expected_version` conflicts, which this ADR builds on.

## Decision

### D1. Connectivity model for S1–S3

1. **Online-first with durable drafts.** The client never pretends a mutation succeeded. A user action creates a **draft** record in IndexedDB `{ idempotency_key, command, created_at, status ∈ pending|sending|acknowledged|conflict|rejected, attempts, last_error }` *before* the request. The UI renders the item optimistically with a visible **"pending"** marker (text and icon, not colour alone) until the server acknowledges; acknowledged drafts are deleted.
2. **Retry is automatic only for idempotent commands** (all ADR-003 commands carry a key, so all qualify), with exponential backoff capped at 5 minutes while the app is open, and on next launch. Retry always reuses the same key; the ADR-003 receipt guarantees exactly-once effects (`LEGACY-NFR-005`). Drafts older than **7 days** stop auto-retrying and are shown to the user for manual resend or discard; the server receipt retention (30 days) exceeds this window.
3. The service worker caches the **application shell and static assets only** (ADR-001 D2). Authenticated data is cached in memory and IndexedDB **as a read cache labelled with its fetch time**; stale views show an "as of" indicator. No queued mutation is replayed by the service worker; replay happens in the page with the user's session.
4. **No offline synchronisation claim.** Product text, release notes and the manifest describe the behaviour as "drafts and retry". Full offline (`LEGACY-NFR-004`) is reconsidered in S3 with a revision of this ADR and an independent FVT; until then the `mobile-pwa` profile remains an unavailable adapter (`DEC-015`).

### D2. Conflict resolution

5. **Server state wins; the user decides.** On `409` from `expected_version` mismatch, the client marks the draft `conflict`, fetches the current aggregate and the events since the expected version (ADR-003 D2), and presents a **reconciliation view**: keep server state, re-apply my change on top (new command, new key), or discard. No silent last-writer-wins and no automatic merge of domain content.
6. **Completion-type commands are not conflicts by default**: completing an action that is already completed by the same key is a replay (`200`); by a different key it returns `409 AlreadyCompleted` with the original event, which the client shows as "already done" and discards. This keeps UC-LEGACY-035 free of duplicate XP.
7. **Deletions are soft.** A `*Archived` or `*Deleted` event hides the aggregate; a later command against it returns `410 Gone` with the deleting event ID so the client can explain rather than fail silently.

### D3. Backup, restore and recovery (`LEGACY-NFR-017`)

8. The managed PostgreSQL of ADR-001 D5 must provide **daily automated snapshots and point-in-time recovery with at least 7 days** of WAL retention; object storage uses versioning with 30-day retention of overwritten or deleted objects. A **weekly logical dump** (`pg_dump`) and an object-storage inventory are exported to a second provider or offline location controlled by the owner, encrypted at rest.
9. A **restore drill** (`RESTORE-DRILL-001` in ADR-005 D6) restores the latest snapshot plus PITR to a point within the last 24 hours into a throwaway environment, runs the schema integrity and projection-rebuild checks, and records duration and data loss window. The drill is required **before** the first production environment that stores finance records, memories or media, and repeated at least every 6 months or after a major infrastructure change. Recovery objectives for that first environment: **RPO ≤ 24 h, RTO ≤ 8 h**; these are the documented commitments, tightened only by a revision with evidence.
10. Backups contain Restricted data and are themselves Restricted: access is logged, and backups are never copied to developer machines or fixtures (`LEGACY-NFR-015`).

### D4. Retention

11. **Domain events, reward transactions and audit events are retained for the life of the workspace**; they are the explanation history (`LEGACY-FNC-074`). Idempotency receipts: 30 days. Sessions: until expiry plus 7 days for forensics. Telemetry: 90 days, pseudonymous, no user content (`LEGACY-NFR-008`). Soft-deleted aggregates: purged by the deletion workflow (D5) or after 30 days in trash, whichever is earlier.
12. **Attachments**: quota per user enforced at upload (`LEGACY-NFR-021`), bounded size, type sniffing and malware scan before any share link exists; orphaned objects (no referencing row after soft-delete purge) are garbage-collected weekly.

### D5. Export and deletion (`LEGACY-FNC-062`, `LEGACY-FNC-023`, `LEGACY-NFR-012`)

13. **Export** is a user-initiated, asynchronous job producing a ZIP with `manifest.json`, one JSON Lines file per aggregate type (including the event ledger and reward transactions for the user's own content), and attachments under their storage keys; delivered through a signed URL valid 24 hours; completion and download are audit events. Workspace-level export is available to the owner and includes only content the owner can read under ADR-002 grants.
14. **Deletion** is a two-step workflow: request (soft-delete, 14-day grace, export offered), then **hard purge** of content rows, attachments and search indexes. Events authored by the deleted user in *shared* workspaces are **pseudonymised** (actor replaced by a tombstone ID) rather than removed, so other members' ledgers stay consistent; the user's personal workspace ledger is purged. Backups age out naturally under D3 retention; the disclosed constraint is "copies may persist in encrypted backups for up to 37 days".
15. Account deletion revokes all grants, sessions, integration tokens and AI consents immediately at request time, before the grace period.

## Considered alternatives

- **Full offline-first with CRDTs or a sync engine (Replicache, ElectricSQL, PowerSync).** Rejected for S1–S3: large complexity, licensing and vendor surface for a requirement the baseline explicitly forbids claiming before verification; the draft/retry model covers the P0 need.
- **Service-worker background sync replaying mutations.** Rejected: runs outside the user's visible session and complicates exactly-once reasoning; in-page retry with durable drafts is sufficient.
- **Last-writer-wins on version conflicts.** Rejected: silently loses personal content; contradicts UC-LEGACY-035 "no lost personal content".
- **Hard delete on user deletion including shared ledgers.** Rejected: breaks other members' explanations and reward history; pseudonymisation chosen.
- **Rely solely on provider snapshots without owner-controlled export.** Rejected: provider lock-in and single point of failure for irreplaceable memories.

## Consequences

### Positive

- Users get visible, honest pending state and safe retries now, without an unverified offline claim.
- Conflicts become an explicit user decision with the event history available.
- Backup, restore, retention and deletion have numbers and a drill that `LEGACY-NFR-017` can be verified against.

### Negative

- Reconciliation UI is extra S2/S3 work and must be designed for phone and desktop.
- Weekly external dumps and drills are recurring operator duties.
- Pseudonymised tombstones in shared ledgers are a disclosed limitation of deletion.

## Control provenance

Prepared by the Systems Engineering control-plane agent (Claude Fable 5.1, Claude Code) for LEGACY-WORK-002 as a reviewable proposal. Inputs: `CONOPS.md` sections 3, 5–7, `USE_CASES.md` UC-LEGACY-035, `EXTERNAL_INTERFACES.md` rows "Media storage" and "Browser/PWA", `VERIFICATION_AND_ACCEPTANCE.md` gate 7, reference baseline NFR-004/005. Acceptance requires a human Systems Engineering decision.
