---
artifact_id: LEGACY-REQS-001
project: LEGAVIA
title: Legavia Requirements Baseline Candidate
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Requirements Baseline Candidate

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

## Specification conventions

All existing 53 September requirements retain their exact identifier and original wording. New identifiers start after the previous maximum in each category. `P0` is first coherent slice, `P1` next iterations, `P2` deferred. **Proposed** does not mean accepted. Functional requirement prefix `LEGACY-FNC-` is distinct from the GUI's behavior functionality identifier `LEGACY-FUNC-`.

The requirement table is derived into `traceability/manifest.json`; it is the same source text, not a separately editable approximation.

| ID | Priority | Requirement statement | Allocated functionalities |
|---|---|---|---|
| LEGACY-BIZ-001 | P0 | The product shall provide one unified life-management environment spanning multiple domains while preserving a consistent interaction model. | Pending allocation review |
| LEGACY-BIZ-002 | P0 | Gamification shall reinforce completion of meaningful real-world objectives and shall not require separate game-only maintenance to preserve progress. | LEGACY-FUNC-008 |
| LEGACY-BIZ-003 | P0 | Each user shall have a private workspace, with explicit sharing controls for family or collaborative features. | LEGACY-FUNC-001 |
| LEGACY-BIZ-004 | P1 | The product shall support adding new life modules without changing the top-level interaction principles or duplicating core domain entities. | Pending allocation review |
| LEGACY-BIZ-005 | P1 | Feature requests generated from user input may be proposed by AI but shall require explicit authorized approval before becoming a production baseline item. | LEGACY-FUNC-020 |
| LEGACY-FNC-001 | P0 | The system shall authenticate users and load only the data authorized for the active workspace. | LEGACY-FUNC-001 |
| LEGACY-FNC-002 | P0 | The Today view shall aggregate due habits, tasks, calendar context, and the next recommended action without requiring navigation into each module. | LEGACY-FUNC-004 |
| LEGACY-FNC-003 | P0 | The system shall represent goals using long-term, mid-term, and short-term relationships and allow decomposition into phases and milestones. | LEGACY-FUNC-003 |
| LEGACY-FNC-004 | P0 | The Map view shall visualize phases/milestones as navigable nodes and indicate locked, available, in-progress, and completed states. | LEGACY-FUNC-005 |
| LEGACY-FNC-005 | P1 | The Map shall support distinct visual themes by phase/island while retaining a consistent interaction grammar. | LEGACY-FUNC-005, LEGACY-FUNC-025 |
| LEGACY-FNC-006 | P0 | Users shall be able to create recurring habits using daily, selected-day, interval, and target-per-period schedules. | LEGACY-FUNC-006 |
| LEGACY-FNC-007 | P0 | Users shall be able to create one-off tasks with due date, optional checklist, priority, and linkage to a goal or module. | LEGACY-FUNC-004 |
| LEGACY-FNC-008 | P1 | Users shall be able to group ordered habits/actions into reusable routines. | LEGACY-FUNC-006 |
| LEGACY-FNC-009 | P0 | A completion action shall update the underlying item, relevant milestone progress, analytics, and gamification state atomically. | LEGACY-FUNC-007 |
| LEGACY-FNC-010 | P0 | Users shall be able to undo an accidental completion without losing unrelated progress. | LEGACY-FUNC-007 |
| LEGACY-FNC-011 | P0 | The system shall calculate a continuity metric that preserves historical progress after isolated misses rather than relying only on a reset-to-zero streak. | LEGACY-FUNC-006 |
| LEGACY-FNC-012 | P1 | The system may show traditional streaks in addition to the continuity metric, with user-configurable grace or recovery behavior. | LEGACY-FUNC-006 |
| LEGACY-FNC-013 | P0 | Verified actions shall award configurable XP to a global level and one or more domain skills. | LEGACY-FUNC-008 |
| LEGACY-FNC-014 | P1 | The system shall support achievements and milestone unlocks with in-progress and completed states. | LEGACY-FUNC-008 |
| LEGACY-FNC-015 | P1 | The system shall support optional virtual currency and user-defined rewards without gating core task/habit functionality. | LEGACY-FUNC-008 |
| LEGACY-FNC-016 | P1 | The system shall support finite daily/weekly quests derived from current goals and habits. | LEGACY-FUNC-008 |
| LEGACY-FNC-017 | P0 | Users shall be able to access Personal, Work, Health, Finance, Learning, and future modules through a common module hub. | LEGACY-FUNC-002 |
| LEGACY-FNC-018 | P1 | The system shall provide a global search entry point capable of locating goals, tasks, habits, modules, lessons, and other indexed entities. | Pending allocation review |
| LEGACY-FNC-019 | P1 | The system shall support context-aware reminders that can be snoozed, completed, or opened directly to the relevant item. | LEGACY-FUNC-018 |
| LEGACY-FNC-020 | P1 | The system shall support glanceable widgets for a small set of high-value signals and deep-link widget interactions to the relevant app context. | LEGACY-FUNC-018 |
| LEGACY-FNC-021 | P0 | The system shall provide history and analytics by day, week, month, and selected life domain. | LEGACY-FUNC-009, LEGACY-FUNC-026 |
| LEGACY-FNC-022 | P1 | Where authorized, the system shall ingest eligible external signals such as calendar and health data to reduce manual logging. | LEGACY-FUNC-022 |
| LEGACY-FNC-023 | P1 | The system shall provide export of user-owned structured data in at least one portable format. | LEGACY-FUNC-022 |
| LEGACY-FNC-024 | P1 | Family/social features shall be opt-in and support cooperative goals without requiring public leaderboard participation. | LEGACY-FUNC-021 |
| LEGACY-FNC-025 | P1 | Users shall be able to submit a feature request by text or voice and receive an AI-generated structured proposal containing scope, rationale, dependencies, and acceptance criteria. | LEGACY-FUNC-020 |
| LEGACY-FNC-026 | P1 | An authorized administrator shall be able to approve or reject an AI-generated feature proposal and route approved proposals into a beta/release workflow. | LEGACY-FUNC-020 |
| LEGACY-FNC-027 | P1 | The Learning module shall represent courses, modules, lessons, and activities and support importing source links for AI-assisted content extraction subject to user review. | LEGACY-FUNC-013 |
| LEGACY-FNC-028 | P1 | The Finance module shall support goal-linked projections and preserve separation between user-entered assumptions and imported financial data. | LEGACY-FUNC-012 |
| LEGACY-UX-001 | P0 | The compact/mobile shell shall expose no more than five default top-level destinations. | LEGACY-FUNC-002 |
| LEGACY-UX-002 | P0 | Top-level navigation controls shall navigate between sections and shall not be repurposed as action buttons. | LEGACY-FUNC-002 |
| LEGACY-UX-003 | P0 | Switching top-level destinations shall preserve the navigation state of each destination. | LEGACY-FUNC-002 |
| LEGACY-UX-004 | P0 | Advanced or infrequently used options shall be progressively disclosed rather than presented in the default daily workflow. | LEGACY-FUNC-002 |
| LEGACY-UX-005 | P0 | Each high-frequency screen shall present one clearly identifiable primary action and visually subordinate secondary actions. | LEGACY-FUNC-002 |
| LEGACY-UX-006 | P0 | Primary touch targets shall provide at least a 44×44 pt hit region on iOS-class interfaces. | LEGACY-FUNC-002 |
| LEGACY-UX-007 | P0 | The interface shall provide visible feedback for success, failure, disabled actions, and recoverable errors, including an explanation when an action cannot proceed. | LEGACY-FUNC-002 |
| LEGACY-UX-008 | P0 | No essential state or instruction shall be communicated by color alone, and reduced-motion preferences shall be honored. | LEGACY-FUNC-002 |
| LEGACY-UX-009 | P0 | All drag-based nonessential interactions shall have a single-pointer non-drag alternative. | LEGACY-FUNC-002 |
| LEGACY-UX-010 | P0 | The user shall be able to switch between any two top-level destinations with one tap/click from the app shell. | LEGACY-FUNC-002 |
| LEGACY-UX-011 | P1 | The interface shall support a low-gamification presentation mode that preserves productivity functionality while reducing decorative game elements. | LEGACY-FUNC-025 |
| LEGACY-UX-012 | P0 | Empty states shall contain an explanation and at least one valid next action when the user has permission to create or configure content. | LEGACY-FUNC-002 |
| LEGACY-NFR-001 | P0 | Web surfaces shall conform to WCAG 2.2 Level AA for applicable success criteria. | LEGACY-FUNC-002 |
| LEGACY-NFR-002 | P0 | User and workspace authorization boundaries shall be enforced server-side for every data access path. | LEGACY-FUNC-001 |
| LEGACY-NFR-003 | P0 | Sensitive user data shall be encrypted in transit and at rest using platform-standard mechanisms. | LEGACY-FUNC-001 |
| LEGACY-NFR-004 | P1 | Critical daily actions shall remain usable under intermittent connectivity and synchronize safely when connectivity returns. | Pending allocation review |
| LEGACY-NFR-005 | P0 | Synchronization shall be idempotent for repeated completion/update requests and shall prevent duplicate XP/reward issuance. | LEGACY-FUNC-007 |
| LEGACY-NFR-006 | P1 | The system shall keep an auditable history for admin approval of AI-generated feature proposals and beta promotion decisions. | LEGACY-FUNC-020 |
| LEGACY-NFR-007 | P0 | High-frequency completion interactions shall provide perceived feedback immediately; any longer-running operation shall expose visible progress/state. | LEGACY-FUNC-025 |
| LEGACY-NFR-008 | P1 | Product analytics shall minimize collection to events required for UX/product decisions and shall distinguish telemetry from user content. | LEGACY-FUNC-026 |
| LEGACY-BIZ-006 | P0 | Users shall retain ownership and control over their personal records and sharing permissions. | LEGACY-FUNC-001 |
| LEGACY-BIZ-007 | P0 | Legavia shall support responsive desktop-web and smartphone workflows using the same business data and permissions. | Pending allocation review |
| LEGACY-BIZ-008 | P1 | Importing external financial, calendar, or media data shall not silently replace user-authored authoritative records. | Pending allocation review |
| LEGACY-BIZ-009 | P0 | The product shall support incremental modules with bounded, independently testable release increments. | LEGACY-FUNC-024 |
| LEGACY-BIZ-010 | P0 | The product shall distinguish user wellbeing data from diagnostics and shall not sell or expose private content as public game state. | Pending allocation review |
| LEGACY-FNC-029 | P1 | Users shall start, pause, resume, cancel, and complete named focus sessions linked to tasks or goals, recording elapsed and effective duration. | LEGACY-FUNC-011 |
| LEGACY-FNC-030 | P1 | Completed eligible focus sessions shall contribute to a persistent virtual forest and optional in-app reward balance without duplicating rewards on retry. | LEGACY-FUNC-011 |
| LEGACY-FNC-031 | P0 | Users shall record, correct, and review daily water consumption using configurable serving sizes and units. | LEGACY-FUNC-010 |
| LEGACY-FNC-032 | P0 | Users shall configure daily water targets and review daily progress with explicit date and local-timezone semantics. | LEGACY-FUNC-010 |
| LEGACY-FNC-033 | P1 | The Finance module shall categorize imported and manual transactions and track monthly income, expenses, savings, and account balances. | LEGACY-FUNC-012 |
| LEGACY-FNC-034 | P1 | Users shall import financial data from user-authorized spreadsheets with source provenance, preview, deduplication, and confirmation before commit. | LEGACY-FUNC-012 |
| LEGACY-FNC-035 | P1 | The Finance module shall represent accounts, transfers and remittances across currencies without double-counting intra-user transfers as income or expenditure. | LEGACY-FUNC-012 |
| LEGACY-FNC-036 | P1 | Financial projections shall distinguish historical actuals, planned budgets, and assumptions, including housing and vehicle ownership costs. | LEGACY-FUNC-012 |
| LEGACY-FNC-037 | P1 | Users shall compare budget to actual spending by month and category and inspect transactions driving a variance. | LEGACY-FUNC-012 |
| LEGACY-FNC-038 | P2 | Users shall track asset-related costs, financing, service, insurance and estimated depreciation separately from realized cash flows. | LEGACY-FUNC-012 |
| LEGACY-FNC-039 | P1 | The Learning module shall track course enrollment, modules, lessons, activities, completion, and related resources. | LEGACY-FUNC-013 |
| LEGACY-FNC-040 | P1 | Users shall maintain books in reading, planned, and completed states with total-page and read-page progress. | LEGACY-FUNC-014 |
| LEGACY-FNC-041 | P1 | The reading module shall estimate completion dates using recent timestamped reading observations, exposing insufficient-data and uncertainty states. | LEGACY-FUNC-014 |
| LEGACY-FNC-042 | P1 | Users shall register movie recommendations by voice or text with recommender attribution, submission timestamp, and personal queue status. | LEGACY-FUNC-015 |
| LEGACY-FNC-043 | P1 | When an external movie rating is available, the queue shall display its source, retrieval date and sort ordering; unknown scores shall remain unranked. | LEGACY-FUNC-015 |
| LEGACY-FNC-044 | P1 | Users shall maintain a game library and track per-game play sessions with start, pause, resume, stop, and cumulative elapsed duration. | LEGACY-FUNC-016 |
| LEGACY-FNC-045 | P1 | Users shall capture searchable notes and reflections using text or voice, retaining original input and transcription provenance. | LEGACY-FUNC-017 |
| LEGACY-FNC-046 | P2 | Users shall import compatible notebook documents from user-provided reMarkable exports with explicit review, file size limits and source metadata. | LEGACY-FUNC-017 |
| LEGACY-FNC-047 | P1 | Users shall attach photos and documents to private memories and review them in chronological context. | LEGACY-FUNC-017 |
| LEGACY-FNC-048 | P2 | Users shall organize thoughts and memories into an editable relationship map without duplicating source records. | LEGACY-FUNC-017 |
| LEGACY-FNC-049 | P2 | Users shall maintain a CV/experience profile with manually approved updates proposed from completed goals, projects or milestones. | LEGACY-FUNC-023 |
| LEGACY-FNC-050 | P1 | Users shall view calendar context and schedule or reschedule Legavia tasks while preserving original external calendar event ownership. | LEGACY-FUNC-018 |
| LEGACY-FNC-051 | P1 | Voice or chat capture shall produce a previewable structured task, habit, note, or request; persisted changes shall require user confirmation. | LEGACY-FUNC-019 |
| LEGACY-FNC-052 | P2 | When GitHub is authorized, the system shall propose daily or weekly work items from selected issues or project items, subject to user acceptance. | LEGACY-FUNC-022 |
| LEGACY-FNC-053 | P1 | Workspace owners shall be able to invite family users and grant explicit least-privilege roles for shared objects. | LEGACY-FUNC-021 |
| LEGACY-FNC-054 | P2 | Administrators shall view storage use per workspace and enforce configurable quotas and safe rejection semantics. | LEGACY-FUNC-021 |
| LEGACY-FNC-055 | P2 | Administrators shall assign approved features to a bounded beta cohort, revoke access, and record rollout and rollback decisions. | LEGACY-FUNC-020 |
| LEGACY-FNC-056 | P1 | Users shall review and revoke external connector authorizations and inspect the last successful import timestamp. | LEGACY-FUNC-022 |
| LEGACY-FNC-057 | P1 | Habit configuration shall distinguish positive and avoid/negative behaviors and support optional severity-dependent penalty rules. | LEGACY-FUNC-006 |
| LEGACY-FNC-058 | P1 | Avoid/negative behavior tracking shall expose time elapsed since a confirmed occurrence and provide correction or reversal of an erroneous record. | LEGACY-FUNC-006 |
| LEGACY-FNC-059 | P1 | The Finance module shall provide multi-period savings and expense trends including configurable category drilldowns and annual projections. | LEGACY-FUNC-012, LEGACY-FUNC-026 |
| LEGACY-FNC-060 | P1 | Users shall configure notification/reminder preferences per module and disable nonessential alerts. | LEGACY-FUNC-018 |
| LEGACY-FNC-061 | P0 | Users shall be able to switch between mobile and desktop preview layouts without losing the underlying working state. | LEGACY-FUNC-002 |
| LEGACY-FNC-062 | P2 | Users shall record workouts, runs, or activity sessions manually and link progress to optional goals, without implying medical diagnosis. | LEGACY-FUNC-010 |
| LEGACY-FNC-063 | P1 | Users shall download user-owned content in portable machine-readable form and initiate account-data deletion through authenticated controls. | LEGACY-FUNC-022 |
| LEGACY-FNC-064 | P1 | Users shall manage financial accounts and recurring obligations across jurisdictions while retaining original transaction currency and exchange-rate provenance. | LEGACY-FUNC-012 |
| LEGACY-FNC-065 | P1 | Administrators shall inspect audit records for data-sharing and feature-approval actions without browsing unrelated private user content. | LEGACY-FUNC-021 |
| LEGACY-FNC-066 | P1 | Users shall attach task or goal evidence and inspect the source event behind XP, currency, and progress changes. | LEGACY-FUNC-007 |
| LEGACY-FNC-067 | P1 | Users shall visualize completed and pending skills, awards and milestones without public disclosure by default. | LEGACY-FUNC-008 |
| LEGACY-NFR-009 | P0 | All user content shall be tenant-scoped and enforced by server authorization, including media links, exports and background jobs. | LEGACY-FUNC-001 |
| LEGACY-NFR-010 | P0 | State-changing actions and imports shall be retry-safe and record sufficient provenance for deterministic reconciliation. | LEGACY-FUNC-007 |
| LEGACY-NFR-011 | P0 | Timezone-aware timestamps shall be stored in an unambiguous representation; displayed calendar days shall use user-selected timezone. | LEGACY-FUNC-024 |
| LEGACY-NFR-012 | P0 | The same supported feature shall preserve its essential business behavior across mobile and desktop layouts. | LEGACY-FUNC-002 |
| LEGACY-NFR-013 | P0 | Each required screen state and critical journey shall have a deterministic fixture and independently reviewable visual evidence for mobile and desktop. | LEGACY-FUNC-002 |
| LEGACY-NFR-014 | P0 | Release approval shall depend on passing defined security, functional, accessibility and regression gates for the changed scope. | LEGACY-FUNC-024 |
| LEGACY-NFR-015 | P1 | The system shall offer user-controlled content export and deletion with retention exceptions documented in a user-accessible policy. | LEGACY-FUNC-024 |
| LEGACY-NFR-016 | P0 | Sensitive media, access tokens and external integration credentials shall not appear in agent prompts, debug bundles or routine telemetry. | LEGACY-FUNC-001 |
| LEGACY-NFR-017 | P1 | Financial projections and estimated reading-completion dates shall identify assumptions and distinguish estimates from observed facts. | LEGACY-FUNC-014 |
| LEGACY-NFR-018 | P0 | The product shall provide documented recovery procedures for storage corruption and restore tests before promoting data-dependent releases. | LEGACY-FUNC-024 |
| LEGACY-NFR-019 | P0 | Application and testing instrumentation shall not use production user data as public fixture inputs without explicit authorized sanitization. | LEGACY-FUNC-024 |

## Acceptance and verification protocol

1. Product/SE reviewer checks need, unambiguous subject, singular behavior and feasible verification method.
2. Functionalities and use cases must give the requirement a traceable implementation context; unallocated candidates must be dispositioned rather than silently deleted.
3. Security, interoperability, privacy and performance criteria are made objectively testable in their own acceptance gate; open thresholds remain explicit decisions, never made up by agents.
4. If an existing candidate is ambiguous (e.g. use of 'may'), preserve original text and raise a proposed controlled revision rather than silently editing its identity.
5. Promote only the approved subset and retain rejected/deferred IDs with disposition.

## Known pending decisions

Precise offline synchronization guarantees; tech stack/hosting and backup objective; connector import format versions and provider capabilities; exact performance targets; finance FX source and rate rules; AI consent and data retention; gamification penalty ethics; legal data retention and minors/family scope; visual references at each viewport. See `LEGACY_DECISIONS_v0.2.md`.
