---
project: LEGAVIA
artifact_status: baseline-candidate
version: 0.1.0
date: 2026-10-29
control_repository: matheusns/legacy
review_gate: Systems Engineering approval required
---

# UX, Visual Fidelity and Responsive Interaction Contract

> Controlled **candidate**, not an approved specification. Preserve existing LEGACY IDs; changes require review and traceability updates.

## Baseline visual intention
Preserve the reference-led fantasy RPG/pixel-art experience and original island/goal world, while maintaining task readability and low interaction latency. The previously supplied reference images are design inputs but **no frozen screenshot hashes or approved golden renders are currently available in this repository**. UX acceptance must therefore be evidence-driven, not asserted by similarity claims.

## Information architecture
Five persistent destinations: **Today / Map / Life / Insights / Me**. Desktop uses a sidebar or comparable navigation, compact mobile uses bottom navigation; both preserve current context. High-frequency screens prioritize task execution; pixel-art dominates Map, progression and reward surfaces. Avoid oversized icons, cramped text and generic SVG-only substitutions for reference artwork where image assets are needed.

## Required screen contracts for first journey
| Surface | Phone and desktop contents | Primary action | States |
| --- | --- | --- | --- |
| Today | Date, due linked task, next action, context from habits/water/focus | Complete next action | Loading, empty, populated, optimistic, retry, error, permission denied |
| Map | Themed island/phase, navigable milestones with textual state | Open next available milestone | Locked, available, active, completed, no goal, failed |
| Goal/Island detail | Goal hierarchy, progress criteria, linked tasks | Create/complete next action | Draft, saved, invalid, conflict, archived |
| Life | Module launcher and resumable module context | Open module | Available, disabled, coming soon, permission denied |
| Insights | Period/domain analytics with metrics and provenance | Inspect contributing events | No data, loaded, partial, error |
| Me | Profile, XP ledger, preferences, workspace, export | Review profile/settings | Loading, personal, collaborator, admin, revoked |
| Focus | Named timer, task association, timeline, plant projection | Start/pause/stop | Idle, active, paused, completed, interrupted |

## Viewport and visual evidence
For every approved screen, capture at least one representative phone viewport (390×844 CSS px) and desktop viewport (1440×900 CSS px), plus relevant narrow/large variants. Store fixture ID, application revision, browser, viewport, pixel ratio, artwork version, reference version, actual screenshot and findings. Test Auto/Mobile/Desktop override on both physical classes. The screenshot diff threshold and art asset licenses require explicit approval; do not invent pass/fail percentages.

## Interaction and accessibility
Visible focus, adequate contrast, keyboard navigation, high-visibility status badges for *real* status only, ≥44×44pt touch affordances, reduced motion, non-drag controls, no color-only state, human-readable progress/penalties and explicit destructive-action confirmation. Voice and camera requests provide text/file fallback. Each critical flow shall work without animations and without permission to external providers.

## Candidate UX review gates
1. The designer inspects approved source images, identifies exact assets and tokens, and presents a mobile+desktop layout specification.
2. The implementer renders actual running screens under deterministic fixture state.
3. Independent UX verification compares captures and logs findings; missing assets or wrong ratios block acceptance.
4. Systems Engineering resolves any proposed change to navigation, design invariants or acceptance thresholds before promotion.
