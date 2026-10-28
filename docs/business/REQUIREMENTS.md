---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# Controlled Requirement Catalog

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

## Conventions and maturity
Existing IDs from the research reference (`LEGACY-BIZ-001..005`, `LEGACY-FNC-001..028`, `LEGACY-UX-001..012`, `LEGACY-NFR-001..008`) and financial-use-case draft (`LEGACY-FNC-029..043`, `LEGACY-UX-013..016`, `LEGACY-NFR-009..012`) are preserved. The latter originated on a feature branch and remain **candidate**, not tacitly approved. Extensions start at the next unused ID. In this revision P0/P1/P2 express candidate implementation priority, not approval.

Requirements use testable 'shall' language where possible; where a historical row says 'may', its optional nature remains intact. Numeric thresholds not grounded in an agreed baseline remain an explicit decision, not a fictitious acceptance target.

## BIZ requirements

| ID | Priority | Statement | Verification method |
| --- | --- | --- | --- |
| LEGACY-BIZ-001 | P0 | The product shall provide one unified life-management environment spanning multiple domains while preserving a consistent interaction model. | Architecture review |
| LEGACY-BIZ-002 | P0 | Gamification shall reinforce completion of meaningful real-world objectives and shall not require separate game-only maintenance to preserve progress. | Product inspection + telemetry |
| LEGACY-BIZ-003 | P0 | Each user shall have a private workspace, with explicit sharing controls for family or collaborative features. | Security/FVT |
| LEGACY-BIZ-004 | P1 | The product shall support adding new life modules without changing the top-level interaction principles or duplicating core domain entities. | Architecture test |
| LEGACY-BIZ-005 | P1 | Feature requests generated from user input may be proposed by AI but shall require explicit authorized approval before becoming a production baseline item. | Workflow FVT |
| LEGACY-BIZ-006 | P0 | Legavia shall expose the same core user journeys through a responsive browser experience on mobile and desktop before considering native-client dependencies. | Independent functional verification |
| LEGACY-BIZ-007 | P1 | The product shall support a coherent life-management history across productivity, focus, health, learning, media, finance and memories without requiring all modules to be enabled. | Independent functional verification |
| LEGACY-BIZ-008 | P0 | Access to another person's data shall be granted at resource level and shall not arise implicitly from friendship, household membership or an invitation. | Independent functional verification |
| LEGACY-BIZ-009 | P1 | External integrations and AI recommendations shall require explicit user authorization, show data provenance and remain usable through manual alternatives. | Independent functional verification |
| LEGACY-BIZ-010 | P0 | The development program shall require approved use-case, requirement, UX and verification evidence before production promotion. | Independent functional verification |

## FNC requirements

| ID | Priority | Statement | Verification method |
| --- | --- | --- | --- |
| LEGACY-FNC-001 | P0 | The system shall authenticate users and load only the data authorized for the active workspace. | Security/FVT |
| LEGACY-FNC-002 | P0 | The Today view shall aggregate due habits, tasks, calendar context, and the next recommended action without requiring navigation into each module. | FVT |
| LEGACY-FNC-003 | P0 | The system shall represent goals using long-term, mid-term, and short-term relationships and allow decomposition into phases and milestones. | FVT |
| LEGACY-FNC-004 | P0 | The Map view shall visualize phases/milestones as navigable nodes and indicate locked, available, in-progress, and completed states. | Visual FVT |
| LEGACY-FNC-005 | P1 | The Map shall support distinct visual themes by phase/island while retaining a consistent interaction grammar. | Visual inspection |
| LEGACY-FNC-006 | P0 | Users shall be able to create recurring habits using daily, selected-day, interval, and target-per-period schedules. | Functional test |
| LEGACY-FNC-007 | P0 | Users shall be able to create one-off tasks with due date, optional checklist, priority, and linkage to a goal or module. | Functional test |
| LEGACY-FNC-008 | P1 | Users shall be able to group ordered habits/actions into reusable routines. | Functional test |
| LEGACY-FNC-009 | P0 | A completion action shall update the underlying item, relevant milestone progress, analytics, and gamification state atomically. | Integration FVT |
| LEGACY-FNC-010 | P0 | Users shall be able to undo an accidental completion without losing unrelated progress. | Functional test |
| LEGACY-FNC-011 | P0 | The system shall calculate a continuity metric that preserves historical progress after isolated misses rather than relying only on a reset-to-zero streak. | Algorithm test |
| LEGACY-FNC-012 | P1 | The system may show traditional streaks in addition to the continuity metric, with user-configurable grace or recovery behavior. | Functional test |
| LEGACY-FNC-013 | P0 | Verified actions shall award configurable XP to a global level and one or more domain skills. | Functional test |
| LEGACY-FNC-014 | P1 | The system shall support achievements and milestone unlocks with in-progress and completed states. | Functional test |
| LEGACY-FNC-015 | P1 | The system shall support optional virtual currency and user-defined rewards without gating core task/habit functionality. | Functional test |
| LEGACY-FNC-016 | P1 | The system shall support finite daily/weekly quests derived from current goals and habits. | FVT |
| LEGACY-FNC-017 | P0 | Users shall be able to access Personal, Work, Health, Finance, Learning, and future modules through a common module hub. | Navigation FVT |
| LEGACY-FNC-018 | P1 | The system shall provide a global search entry point capable of locating goals, tasks, habits, modules, lessons, and other indexed entities. | Search FVT |
| LEGACY-FNC-019 | P1 | The system shall support context-aware reminders that can be snoozed, completed, or opened directly to the relevant item. | Notification test |
| LEGACY-FNC-020 | P1 | The system shall support glanceable widgets for a small set of high-value signals and deep-link widget interactions to the relevant app context. | Widget FVT |
| LEGACY-FNC-021 | P0 | The system shall provide history and analytics by day, week, month, and selected life domain. | Analytics test |
| LEGACY-FNC-022 | P1 | Where authorized, the system shall ingest eligible external signals such as calendar and health data to reduce manual logging. | Integration test |
| LEGACY-FNC-023 | P1 | The system shall provide export of user-owned structured data in at least one portable format. | Export test |
| LEGACY-FNC-024 | P1 | Family/social features shall be opt-in and support cooperative goals without requiring public leaderboard participation. | Permission + FVT |
| LEGACY-FNC-025 | P1 | Users shall be able to submit a feature request by text or voice and receive an AI-generated structured proposal containing scope, rationale, dependencies, and acceptance criteria. | Workflow FVT |
| LEGACY-FNC-026 | P1 | An authorized administrator shall be able to approve or reject an AI-generated feature proposal and route approved proposals into a beta/release workflow. | Workflow FVT |
| LEGACY-FNC-027 | P1 | The Learning module shall represent courses, modules, lessons, and activities and support importing source links for AI-assisted content extraction subject to user review. | Learning FVT |
| LEGACY-FNC-028 | P1 | The Finance module shall support goal-linked projections and preserve separation between user-entered assumptions and imported financial data. | Finance FVT |
| LEGACY-FNC-029 | P0 | Support multiple accounts/cards across UAE and Brazil with type, currency, opening balance, as-of date, status, issuer, and ownership/workspace. | Inspection |
| LEGACY-FNC-030 | P0 | Capture, edit, split, undo and batch-create categorized transactions, with essential flag independent of category, payment source, date, status, and provenance. | Inspection |
| LEGACY-FNC-031 | P0 | Support weekly review of card and account activity including duplicate preview, classification, bulk approval, and statement reconciliation. | Inspection |
| LEGACY-FNC-032 | P0 | Correctly model credit-card purchases as expenses and card liabilities, while card payments settle liabilities without creating duplicate expenses. | Inspection |
| LEGACY-FNC-033 | P0 | Track balances for debit/savings accounts through posted activity, transfers, adjustments, and reconciliation with independently supplied statements. | Inspection |
| LEGACY-FNC-034 | P0 | Represent cross-border remittances and account transfers as linked legs; preserve native amounts/currencies, fees, actual conversion rate, rate timestamp/source, and FX impact. | Inspection |
| LEGACY-FNC-035 | P0 | Summarize monthly and annual income, expenses, savings/savings rate, budget variance and essential/non-essential spending by country, account and category. | Inspection |
| LEGACY-FNC-036 | P1 | Maintain monthly budgets and planned/recurring/fixed/variable/installment commitments, with actual vs forecast cash flow and bill reminders. | Inspection |
| LEGACY-FNC-037 | P1 | Track vehicle costs as ownership/rental operating expenses separately from financing principal, depreciation and one-time acquisition costs. | Inspection |
| LEGACY-FNC-038 | P1 | Track apartment-related payments, property asset valuation, related debt, equity and optional rental revenue while avoiding double counting. | Inspection |
| LEGACY-FNC-039 | P1 | Project one-to-five-year cash flow, saving potential, net worth and goal trajectories, supporting multiple scenarios and recorded assumptions. | Inspection |
| LEGACY-FNC-040 | P0 | Preview and map spreadsheet/CSV/Google Sheets financial data, support manual adjustment and explicit import approval, and suppress duplicate import rows. | Inspection |
| LEGACY-FNC-041 | P0 | Expose source/provenance, creation/edit history, reconciliation status and reversible correction for imported and manually entered transactions. | Inspection |
| LEGACY-FNC-042 | P1 | Calculate account-level balances and a consolidated balance/net-worth view in selectable presentation currency without overwriting native-currency ledger entries. | Inspection |
| LEGACY-FNC-043 | P0 | Distinguish earned income, refunds, reimbursements, investment profit/loss (realized/unrealized), internal transfers and valuation changes in reporting. | Inspection |
| LEGACY-FNC-044 | P1 | The Today surface shall let the user log, correct and review daily water consumption against a configurable daily target. | Independent functional verification |
| LEGACY-FNC-045 | P1 | A focus session shall have a named timer, start, pause, resume and stop actions, and optional association with a task or goal. | Independent functional verification |
| LEGACY-FNC-046 | P1 | Completed focus time shall generate a configurable forest or plant progression projection and period-based focus statistics without duplicating time events. | Independent functional verification |
| LEGACY-FNC-047 | P1 | The Books module shall record reading status, total pages, pages completed, dated reading events and completed-book history. | Independent functional verification |
| LEGACY-FNC-048 | P2 | The Games module shall maintain a game library and distinct start, pause, resume and stop playtime events with aggregated playtime. | Independent functional verification |
| LEGACY-FNC-049 | P1 | The Movies module shall capture a recommendation, recommender, recommendation date and watching status through text or reviewed voice capture. | Independent functional verification |
| LEGACY-FNC-050 | P1 | The Memory module shall accept text, voice, photos and linked note sources and support navigating memories through a searchable timeline and mind-map projection. | Independent functional verification |
| LEGACY-FNC-051 | P2 | The user shall be able to maintain an interactive CV or portfolio with evidence-linked achievements and explicitly approved updates generated from milestones. | Independent functional verification |
| LEGACY-FNC-052 | P1 | The Health module shall track user-entered exercise and wellness events and optionally ingest authorized health signals without making diagnostic claims. | Independent functional verification |
| LEGACY-FNC-053 | P1 | The user shall be able to view task schedules alongside authorized calendar events and plan daily or weekly actions without silently editing the external calendar. | Independent functional verification |
| LEGACY-FNC-054 | P1 | Text or voice commands shall create reviewable proposals for tasks, goals, habits or journal entries; no persistent change shall occur until confirmed by an authorized user. | Independent functional verification |
| LEGACY-FNC-055 | P1 | AI-proposed changes shall have preview, modify, approve and reject states and an auditable provenance record. | Independent functional verification |
| LEGACY-FNC-056 | P1 | The application shall expose user-configurable permissions for optional family or shared workspaces and enforce invitations, revocation and isolation. | Independent functional verification |
| LEGACY-FNC-057 | P2 | Shared goals, social events and challenges shall use explicit resource-level visibility (private, selected users, friends, party or public) with private as default. | Independent functional verification |
| LEGACY-FNC-058 | P2 | Administrators shall be able to enable and roll back approved features for designated beta cohorts without exposing unauthorized workspace content. | Independent functional verification |
| LEGACY-FNC-059 | P2 | Administrators shall be able to monitor configured per-user storage quotas and manage retention without seeing users' private content by default. | Independent functional verification |
| LEGACY-FNC-060 | P0 | The user shall be able to switch an explicit Auto, Mobile or Desktop presentation mode, with Auto adapting to viewport and input characteristics. | Independent functional verification |
| LEGACY-FNC-061 | P0 | Users shall be able to create and manage separate personal and invited workspaces with a documented owner, member and administrator role model. | Independent functional verification |
| LEGACY-FNC-062 | P1 | The application shall support user-controlled export and deletion requests for supported personal data and attachments, subject to disclosed retention constraints. | Independent functional verification |
| LEGACY-FNC-063 | P1 | Notifications and reminders shall be permission-based, user-configurable and deep-link to the related entity when supported. | Independent functional verification |
| LEGACY-FNC-064 | P0 | The web application shall provide installable mobile-friendly behavior and preserve session navigation and allowed local draft state on reload. | Independent functional verification |
| LEGACY-FNC-065 | P2 | An invited user shall be able to participate in a selected collaborative challenge without gaining access to other private modules. | Independent functional verification |
| LEGACY-FNC-066 | P2 | An authorized GitHub connection may suggest daily or weekly tasks from selected project issues, with source links and explicit approval before importing them. | Independent functional verification |
| LEGACY-FNC-067 | P1 | The Learning module shall capture course progress and permit reviewed AI extraction of modules and lessons from approved links or supplied materials. | Independent functional verification |
| LEGACY-FNC-068 | P1 | Habits shall support positive or negative polarity, configurable severity, recovery policy and transparent non-destructive consequences. | Independent functional verification |
| LEGACY-FNC-069 | P0 | XP, levels, badges and virtual currency shall be computed from a deterministic event ledger with visible explanations of rewards and reversals. | Independent functional verification |
| LEGACY-FNC-070 | P1 | The Books module shall recalculate an estimated reading completion date from dated page-progress observations and show insufficient-data uncertainty. | Independent functional verification |
| LEGACY-FNC-071 | P2 | The Movies watchlist may rank candidate titles by a timestamped external rating when licensed data is available, retaining a manual order fallback. | Independent functional verification |
| LEGACY-FNC-072 | P1 | The user shall be able to record goal-linked financial objectives without mistaking projections for actual account balances. | Independent functional verification |
| LEGACY-FNC-073 | P1 | The Today dashboard shall let the user see assigned actions, reminders, active focus session and hydration status without entering individual modules. | Independent functional verification |
| LEGACY-FNC-074 | P0 | Every domain mutation affecting progress or finances shall retain a stable event identity, origin and reversible or compensating correction history. | Independent functional verification |

## UX requirements

| ID | Priority | Statement | Verification method |
| --- | --- | --- | --- |
| LEGACY-UX-001 | P0 | The compact/mobile shell shall expose no more than five default top-level destinations. | Design inspection |
| LEGACY-UX-002 | P0 | Top-level navigation controls shall navigate between sections and shall not be repurposed as action buttons. | Design inspection |
| LEGACY-UX-003 | P0 | Switching top-level destinations shall preserve the navigation state of each destination. | Navigation FVT |
| LEGACY-UX-004 | P0 | Advanced or infrequently used options shall be progressively disclosed rather than presented in the default daily workflow. | Usability inspection |
| LEGACY-UX-005 | P0 | Each high-frequency screen shall present one clearly identifiable primary action and visually subordinate secondary actions. | Design inspection |
| LEGACY-UX-006 | P0 | Primary touch targets shall provide at least a 44×44 pt hit region on iOS-class interfaces. | UI audit |
| LEGACY-UX-007 | P0 | The interface shall provide visible feedback for success, failure, disabled actions, and recoverable errors, including an explanation when an action cannot proceed. | FVT |
| LEGACY-UX-008 | P0 | No essential state or instruction shall be communicated by color alone, and reduced-motion preferences shall be honored. | Accessibility audit |
| LEGACY-UX-009 | P0 | All drag-based nonessential interactions shall have a single-pointer non-drag alternative. | Accessibility FVT |
| LEGACY-UX-010 | P0 | The user shall be able to switch between any two top-level destinations with one tap/click from the app shell. | Navigation FVT |
| LEGACY-UX-011 | P1 | The interface shall support a low-gamification presentation mode that preserves productivity functionality while reducing decorative game elements. | Visual FVT |
| LEGACY-UX-012 | P0 | Empty states shall contain an explanation and at least one valid next action when the user has permission to create or configure content. | State coverage test |
| LEGACY-UX-013 | P0 | Weekly reconciliation supports efficient multi-row review; classify multiple transactions without reopening a modal for every field. | Inspection |
| LEGACY-UX-014 | P0 | Overview metrics have drill-downs to the constituent transactions, accounts and calculation definitions; the displayed reporting currency and FX assumptions remain visible. | Inspection |
| LEGACY-UX-015 | P0 | Present actuals, commitments, projections and uncertainty as distinguishable states; do not present forecasts as account balances. | Inspection |
| LEGACY-UX-016 | P0 | Saving, discarding and undoing a batch must have explicit feedback and guard against loss of partially reviewed work. | Inspection |
| LEGACY-UX-017 | P0 | Pixel-art fantasy RPG theming shall closely follow the accepted Legavia visual references on progression surfaces while preserving readable, accessible operational views. | Visual inspection and interaction test |
| LEGACY-UX-018 | P0 | The app shall provide consistent responsive layouts for mobile and desktop, including a persistent Auto/Mobile/Desktop preview override. | Visual inspection and interaction test |
| LEGACY-UX-019 | P0 | The design system shall define typography, contrast, icon scale, artwork placement, spacing, focus states and reusable components; decorative icons shall not crowd core controls. | Visual inspection and interaction test |
| LEGACY-UX-020 | P0 | Every approved journey shall have matching mobile and desktop UX states and reference-versus-actual visual-regression evidence. | Visual inspection and interaction test |
| LEGACY-UX-021 | P1 | Gamification state shall always expose a textual explanation for progression, currency and penalties. | Visual inspection and interaction test |
| LEGACY-UX-022 | P1 | Permission requests for microphone, camera, health and calendar integrations shall be contextual, revocable and accompanied by a manual fallback. | Visual inspection and interaction test |
| LEGACY-UX-023 | P1 | User-selected low-gamification and reduced-motion presentation preferences shall not alter domain correctness. | Visual inspection and interaction test |

## NFR requirements

| ID | Priority | Statement | Verification method |
| --- | --- | --- | --- |
| LEGACY-NFR-001 | P0 | Web surfaces shall conform to WCAG 2.2 Level AA for applicable success criteria. | Accessibility audit |
| LEGACY-NFR-002 | P0 | User and workspace authorization boundaries shall be enforced server-side for every data access path. | Security test |
| LEGACY-NFR-003 | P0 | Sensitive user data shall be encrypted in transit and at rest using platform-standard mechanisms. | Security review |
| LEGACY-NFR-004 | P1 | Critical daily actions shall remain usable under intermittent connectivity and synchronize safely when connectivity returns. | Offline/sync FVT |
| LEGACY-NFR-005 | P0 | Synchronization shall be idempotent for repeated completion/update requests and shall prevent duplicate XP/reward issuance. | Integration test |
| LEGACY-NFR-006 | P1 | The system shall keep an auditable history for admin approval of AI-generated feature proposals and beta promotion decisions. | Audit test |
| LEGACY-NFR-007 | P0 | High-frequency completion interactions shall provide perceived feedback immediately; any longer-running operation shall expose visible progress/state. | Performance UX test |
| LEGACY-NFR-008 | P1 | Product analytics shall minimize collection to events required for UX/product decisions and shall distinguish telemetry from user content. | Privacy review |
| LEGACY-NFR-009 | P0 | Financial transactions are private by default; workspace permissions must be enforced server-side and data encrypted in transit and at rest. | Inspection |
| LEGACY-NFR-010 | P0 | Posting/importing transactions and transfer legs must be idempotent; partial failures cannot leave inconsistent account or card balances. | Inspection |
| LEGACY-NFR-011 | P0 | Amount arithmetic uses deterministic decimal/fixed-point values with explicit per-currency scale; reporting FX conversions preserve provenance and rounding. | Inspection |
| LEGACY-NFR-012 | P0 | Imported statements and personal finance data must not be committed to public code repositories or exposed through telemetry/logs; support data export and deletion. | Inspection |
| LEGACY-NFR-013 | P0 | Authentication and authorization tests shall cover every API and storage lookup, including nested object access and workspace reassignment attempts. | Independent quality and security verification |
| LEGACY-NFR-014 | P0 | Repeated completion, focus and financial event submissions shall produce one logical event and one reward or ledger effect. | Independent quality and security verification |
| LEGACY-NFR-015 | P0 | Imported files and private media shall be segregated from public code repositories, development fixtures and observability logs. | Independent quality and security verification |
| LEGACY-NFR-016 | P0 | The product shall offer a recoverable draft or retry state for interrupted network requests and shall not claim offline synchronization until independently verified. | Independent quality and security verification |
| LEGACY-NFR-017 | P0 | Production infrastructure shall document backup, restore, retention and recovery testing before storing irreplaceable personal memories or financial records. | Independent quality and security verification |
| LEGACY-NFR-018 | P1 | The team shall establish measured mobile/desktop interaction and startup performance budgets using representative devices before release acceptance. | Independent quality and security verification |
| LEGACY-NFR-019 | P1 | AI providers shall receive only authorized minimum necessary content and shall not hold privileged direct-write credentials to production data. | Independent quality and security verification |
| LEGACY-NFR-020 | P0 | Development releases shall include automated build, unit, integration, authorization and representative mobile/desktop visual tests with candidate fingerprints. | Independent quality and security verification |
| LEGACY-NFR-021 | P1 | Attachment quotas, virus/content validation and bounded upload size shall be enforced before files become available to other users. | Independent quality and security verification |
| LEGACY-NFR-022 | P0 | The system shall store timestamps with timezone semantics and handle DST, local-date scheduling, currency precision and historical revisions deterministically. | Independent quality and security verification |

## Traceability and controls
Machine-readable requirement records, including linked capabilities and FVT references, are in `traceability/manifest.json`. No requirement is verified until a candidate-bound independent test or accepted review produces evidence. To change a statement, record review rationale and preserve the issued ID; do not silently replace its meaning.
