---
artifact_id: LEGACY-CONOPS-001
project: LEGAVIA
title: Legavia Concept of Operations (ConOps)
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Concept of Operations (ConOps)

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

## 1. Mission and intended outcomes

Legavia provides one private, cohesive personal operating system for everyday execution and long-range planning. Users can turn personal, professional, wellness and financial aspirations into explicit goals, actions, measurable progress and optional game rewards. The product reduces bookkeeping burden through authorized imports and AI-assisted drafting while preserving human control of private data and feature evolution.

**Success outcomes:** user can reliably execute daily work, recover from missed activity, inspect progress and financial trajectory, and add new modules without rebuilding the interaction model. Gamification reflects meaningful actions; it cannot replace them.

## 2. Actors and external entities

| Actor / system | Responsibility / trust boundary |
|---|---|
| Individual user | Owns and operates private data, captures tasks, habits, goals, progress and reflections |
| Workspace owner | Invites members and grants explicit sharing permissions |
| Family collaborator | Accesses only shared objects within role permissions |
| Product administrator | Reviews feature/beta proposals and storage quotas; no implied access to unrelated private content |
| Engineering reviewer / SE | Reviews requirements, ADRs, verification semantics and acceptance evidence outside production data flows |
| AI proposal engine | Drafts proposed structures or insights, never self-authorizes persisted changes or baseline updates |
| Calendar, GitHub, Google Sheets, health or media data providers | Optional external systems accessed using scoped user consent and provenance |
| Web/smartphone client | Different presentation environments over the same authorized domain model |

## 3. Operational environments and modes

**Environments:** mobile browser/PWA-compatible presentation, desktop browser and future native shell subject to ADR; same backend domain invariants. User's timezone and local day drive Today, reminders and hydration aggregates; storage records unambiguous timestamps.

**Operating modes:** (a) onboarding/no content; (b) connected normal; (c) transient offline/degraded, with write queue only when a reconciliation policy is implemented; (d) reconnect/sync and conflict resolution; (e) imported-data review; (f) admin beta; (g) incident/recovery; (h) accessibility/low-gamification preference. Unsupported offline-write functionality must be visibly disabled, never advertised as saved.

## 4. Operational scenarios

### OPR-01 — Morning planning and daily execution

The user opens Today, sees aggregated tasks, due habits, water progress and authorized calendar context; starts an action or focus session. A completion is written to the domain ledger, downstream goal progress and XP are derived exactly once, and a possible undo reverts only linked contributions. No mandatory game-only check-in.

### OPR-02 — Long-range goal to world-map achievement

The user defines a long-term goal, phases, milestones and short actions. The Map renders their actual dependency graph as an island/phase. Locked/available/progress/completed states derive from milestone rules, not copied map data. The operator can navigate by tap/click or keyboard without drag.

### OPR-03 — Recovery after inactivity

After missed days, the user sees an actionable replan/reschedule/skip choice. Historical progress and completed rewards persist, while scheduling, consistency and current due counts are recalculated without punitive reset-to-zero semantics.

### OPR-04 — Financial control across jurisdictions

The user imports or records account transactions (including transfers between own accounts), maps categories, reviews a month/annual savings trend and adjusts future assumptions. Original currency, rates, timestamps and source row identifiers remain visible. Transferring funds between own accounts does not become income/expense twice. Investment/asset estimated value is separate from realized cash flow.

### OPR-05 — AI input with approval

A voice or chat note yields a structured draft (task, habit, thought, film, book or feature suggestion). The user reviews, edits and explicitly confirms; a feature request then enters an administrator-governed proposal → approved/rejected → beta/released path. AI is advisory, with versioned original input and a visible provenance chain.

### OPR-06 — Personal archive and enrichment

The user logs reading and receives an estimated finish date with confidence/insufficient history states, captures media memories, imports compatible notes, starts/stops a game timer, adds movie recommendations with attribution, and reviews course progress. Records are private unless expressly shared.

### OPR-07 — Family sharing and safety

A workspace owner invites a family member to a specific goal with least-privilege access. The recipient cannot list private notes, finance, memories or other users' resources by manipulating API calls, media URLs or exports. Revocation takes effect in server-side authorization checks.

### OPR-08 — Multi-device and uncertain connectivity

The user performs an eligible action on mobile and later opens the desktop app. Identical source events are reconciled with idempotency keys. A retry never duplicates progress, focus time, water intake or XP. Conflicts are presented explicitly, not silently overwritten.

## 5. Measures of effectiveness

- Completion from Today requires one interaction for visible, eligible items, or one detail transition when needed.
- Time spent maintaining Legavia is measured alongside time spent completing real-world work.
- All P0 private-data paths are authorization-isolated and independently tested.
- Completion/undo/retry consistency is deterministic; account changes produce audit trails.
- Phone and desktop capture sets conform to approved references for essential states.
- Changes to user-controlled financial assumptions and AI drafts require explicit confirmation.

## 6. System boundaries

**In scope:** planning, tracking, gamified projections, personal archives, authorized data imports, insight derivation, governance and responsive presentation.

**Not implicitly in scope:** medical diagnosis; bank transfers or trading; automated publication of a CV; autonomous modification of GitHub issues; public leaderboards; universal perfect offline synchronization; guaranteed external-rating availability. Any extension requires a new requirement, security and ADR review.
