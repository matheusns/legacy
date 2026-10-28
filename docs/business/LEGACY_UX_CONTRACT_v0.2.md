---
artifact_id: LEGACY-UX-CONTRACT-001
project: LEGAVIA
title: Legavia Responsive UX and Visual Design Contract
version: 0.2
status: candidate-for-SE-review
date: 2026-10-29
control_repository: matheusns/legacy
---

# Legavia Responsive UX and Visual Design Contract

> This artifact is a candidate systems-engineering baseline. Existing stable identifiers are preserved. Review and approve before treating any proposal as an accepted specification or an executable FVT.

## Contract and user-supplied design references

The approved design direction is reference-image-led, adaptable to phone and desktop; expressive pixel-art/Donkey-Kong-like progression motifs are concentrated in Map/Me, while high-frequency task/finance/learning screens remain legible. Existing supplied images are **not** reinterpreted as pixel-perfect approved files in this repository until an operator pins source, usage rights, viewport, fixture, content state and version. The implementation should use actual image assets where the reference requires artwork; oversized hand-coded SVGs/icons that do not match the reference are not acceptable substitutes.

**Compact shell:** Today / Map / Life / Insights / Me (five destinations). A desktop sidebar maps to the same routes; a user may switch preview mode to phone/desktop without losing state. The Map is a view of Goal → Phase → Milestone → Action, not a second database.

## Required screen contract template

Each screen must specify route, goal, audience, mobile and desktop viewport, primary action, secondary actions, input validation, loading/empty/populated/error/permission-denied/disabled states, focus and keyboard order, scrolling/resizing, visual artwork reference, test fixtures, accessibility rationale, and captures. Capture metadata: reference ID and hash; layout mode and pixel dimensions; content fixture version; design-token/artwork version; app revision; rendering engine; timestamp; diff disposition.

## Acceptance criteria

- All essential controls are keyboard/single-pointer reachable with no drag-only requirements; touch regions meet 44 × 44 pt and web WCAG 2.2 AA criteria applicable to the interface.
- Navigation is one tap/click between top-level routes and preserves inner context.
- One primary action per high-frequency screen; visible feedback explains errors, retry and disabled actions.
- Colors do not carry status alone; animations respect reduced-motion preferences.
- Actual screenshot is compared against the pinned reference after loading an identical deterministic fixture at the specified viewport. Reference changes require review, not silent screenshot regeneration.
- Phone mode, desktop mode and responsive auto behavior share identical tenant permissions and business results.

## Initial screen sequence

1. Sign-in/onboarding and empty Today.
2. Today with pending tasks, due habits, hydration progress, calendar hint, plus completion/undo.
3. Goal Map full-screen/phone/desktop, phase states, accessible milestone detail.
4. Life module hub with finite navigation, not a mini-app tab explosion.
5. Focus Forest and finance views after P0 core is independently verified.

## Reference precedence

Accepted requirements/ADRs → approved use cases/verification → active `docs/reference` UX baseline → image/prototype references pinned by reviewers → agent inference. No agent may claim visual parity based exclusively on DOM inspection or element presence.
