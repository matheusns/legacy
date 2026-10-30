# ADR-004 — Pixel-art asset provenance and versioning, responsive design system, visual golden baseline and comparison method

## Status

Proposed — 2026-10-30. Awaiting explicit Systems Engineering acceptance; this record is not accepted and grants nothing until a human reviewer changes this section and the control manifest records the artifact.

Resolves candidate register item `ADR-CAND-004` and decisions `DEC-004` and `DEC-008` of LEGACY-SE-REVIEW-001. Does **not** approve any reference image (`DEC-010` remains an owner plus UX-reviewer action).

## Traceability

- Functionalities: `LEGACY-CAP-005`, `LEGACY-CAP-003`, `LEGACY-CAP-004`
- Requirements: `LEGACY-FNC-004`, `LEGACY-FNC-005`, `LEGACY-FNC-060`, `LEGACY-UX-001`, `LEGACY-UX-005`, `LEGACY-UX-006`, `LEGACY-UX-008`, `LEGACY-UX-009`, `LEGACY-UX-011`, `LEGACY-UX-017`, `LEGACY-UX-018`, `LEGACY-UX-019`, `LEGACY-UX-020`, `LEGACY-UX-023`, `LEGACY-NFR-001`, `LEGACY-NFR-015`
- Work packages: `LEGACY-WORK-002` (acceptance topic: assets), consumers `LEGACY-WORK-004`, `LEGACY-WORK-009`
- Decision owner: Systems Engineering (asset approval: owner + UX reviewer)
- Prepared in run `DEV-20261030T185520Z-751CB5` against control commit `caca50c7e23a892d37e63cc14091f8cf725374d6`

## Context

`UX_CONTRACT.md` requires reference-led pixel-art theming on progression surfaces with restrained operational screens, phone (390×844) and desktop (1440×900) captures per approved screen, recorded fixture, revision, browser, viewport, pixel ratio, artwork version and reference version, and states twice that the screenshot diff threshold and art asset licences "require explicit approval; do not invent pass/fail percentages". `PRODUCT_VISION_AND_SCOPE.md` repeats that numeric visual thresholds must be set by an ADR. `WORKFLOW.md` defines how an approved PNG is pinned (`repository_id`, immutable `revision`, `path`, `status: approved`) and that no screenshot is currently approved.

The exploratory `legacy_mockups` repository holds four reference screens (`assets/screens/{home,world-map,island-career,focus}.webp`) and a composite board (`docs/references/geek-ui-reference-board.webp`) produced in a design session; the repository records no licence, author, generation tool or source for them. The verification harness `capture.cjs` already implements a comparison: pixelmatch with per-pixel colour `threshold: 0.1`, `includeAA: true`, a dimension mismatch counted as 100 % difference, reduced motion forced, animations disabled, fonts awaited, and a `diff_ratio` metric reported without a pass/fail verdict. The reference baseline fixes the design-system and accessibility constraints (sections 5–6, UX-001..012, NFR-001).

## Decision

### D1. Asset provenance and licensing

1. **No visual asset ships without a provenance record.** `legacy_app` holds `assets/ASSET_MANIFEST.json` (schema: `asset_id`, `path`, `sha256`, `kind ∈ {sprite, tileset, illustration, icon, font, reference}`, `source`, `author_or_tool`, `license`, `license_evidence_ref`, `created_at`, `artwork_version`, `derived_from[]`). CI fails when a file under `assets/` is absent from the manifest or its hash differs.
2. **Permitted licences**: CC0, CC-BY 4.0 (attribution rendered in Me → About), SIL OFL for fonts, MIT/Apache-licensed icon sets, and commercially licensed packs whose licence proof is stored **outside** the public repository and referenced by `license_evidence_ref`. Copyleft-for-assets (CC-BY-SA) and non-commercial licences are not permitted for production assets.
3. **AI-generated artwork is permitted** only when the manifest records the tool, prompt reference and date, the tool's terms allow commercial use, and the asset is reviewed for reproduction of identifiable third-party game art. Reproductions or upscales of copyrighted game sprites are prohibited.
4. The four mockup screens and the reference board are **design references, not production assets**; they stay in `legacy_mockups`, receive a provenance record there before any of them is pinned as an approved reference, and are never bundled into `legacy_app`.
5. **Artwork is versioned** by `artwork_version` (semantic version of the asset set) and per-file hash; capture evidence records both so a baseline is invalidated when the art changes (`LEGACY-UX-020`).

### D2. Responsive design system

6. **Tokens first.** A single token file (CSS custom properties generated from JSON in `packages/design-tokens`) defines colour roles, type scale, spacing (4 px base), radius, elevation, motion durations and the **two theme layers**: `operational` (restrained, system-UI or humanist sans, high contrast, no decorative sprites) and `progression` (pixel font and sprite frames). The layer is set per surface: Map, goal/island detail, rewards and selected Me moments use `progression`; Today, Life, Insights, settings and all forms use `operational` (`LEGACY-UX-017`, reference DP-09, RISK-04).
7. **Pixel-art rendering rules**: sprites are authored at a base grid (16 px or 32 px per tile), scaled only by **integer factors** with `image-rendering: pixelated`, never fractional; layout uses CSS pixels so 1×, 2× and 3× device pixel ratios render crisply; decorative art never carries state or text (`LEGACY-UX-008`).
8. **Accessibility baseline** (`LEGACY-NFR-001`): contrast ≥ 4.5:1 for text and ≥ 3:1 for UI boundaries in both layers; touch targets ≥ 44×44 CSS px (`LEGACY-UX-006`); visible focus ring token; every drag or pinch interaction on the Map has a tap/keyboard equivalent (`LEGACY-UX-009`); `prefers-reduced-motion` disables sprite animation and parallax; the pixel font is used for headings and HUD values only, with body copy in the operational face.
9. **Component contract**: shell (bottom tab bar ≤ 5 items on compact, sidebar on ≥ 1024 px), primary/secondary action buttons, list row, card, status badge (text + icon, never colour alone), state panels (loading, empty with next action, error with retry, permission denied), map node (locked/available/in-progress/completed with textual label), progress ring, toast with undo. Every screen composes these; a new primitive requires a design-system change record.
10. **Display mode** (`LEGACY-FNC-060`, `LEGACY-UX-018`): `Auto | Mobile | Desktop` is a client preference persisted per device that switches the layout breakpoint only; it never changes routes, data or authorization. **Low-gamification mode** (`LEGACY-UX-011`, `LEGACY-UX-023`) swaps the `progression` layer for `operational` tokens on the same components; domain data is unchanged.

### D3. Visual golden baseline

11. A **golden baseline** is a pinned, approved PNG per `(screen, state, target_profile)` captured by the registered harness from a **deterministic fixture** (fixed seed, frozen clock `2026-01-01T12:00:00Z` as registered, `en-US`, `UTC`, reduced motion) on pinned Chromium with bundled web fonts (no system font fallback), at DPR 1. It is pinned in `traceability/manifest.json` `ux.screens[].references.<profile_id>` with immutable `revision`, exactly as `WORKFLOW.md` prescribes.
12. **Approval is human**: the first capture of a screen is a candidate; the owner and the read-only UX reviewer compare it with the design reference and record a disposition before it becomes a baseline (`DEC-010`). Candidates never auto-promote.
13. Every baseline carries the evidence tuple from `UX_CONTRACT.md` plus `artwork_version`, asset hashes, harness commit and browser version, so staleness is computable.

### D4. Comparison method and thresholds (`DEC-008`)

14. **Method**: the existing harness algorithm is adopted as the controlled method: pixelmatch per-pixel colour distance threshold **0.1**, `includeAA: true`, full-viewport capture (not full page), dimension mismatch is a failure. Changing any of these parameters is a control change invalidating all baselines.
15. **Disposition bands on `diff_ratio`** (different pixels ÷ total pixels) for a same-dimension comparison:

| Band | `diff_ratio` | Disposition |
| --- | --- | --- |
| Identical or sub-perceptual | ≤ 0.1 % (0.001) | Pass automatically |
| Review | > 0.1 % and ≤ 1.0 % | Inconclusive; requires human review of `diff.png`; may be accepted as a new baseline only with recorded rationale |
| Fail | > 1.0 % or any dimension mismatch | Fail |

16. These bands are **proposed initial values with a calibration obligation**: after the first ten approved baselines exist, the verification role reports the observed `diff_ratio` distribution for unchanged candidates (re-capture noise) and for intentional changes; Systems Engineering then confirms or revises the bands in an ADR revision. Until calibration is recorded, the Review band may not be converted into an automatic pass by tooling. This satisfies the "do not invent" rule by making the number an explicit, reviewed decision with a measurement plan rather than an assertion of equivalence.
17. A passing comparison is **consistency evidence**, not fidelity evidence: fidelity to the design reference is the human disposition of D3(12). Reports must label the two separately (`LEGACY-UX-020`).

## Considered alternatives

- **No licence manifest; rely on repository history.** Rejected: provenance of AI-generated and session-produced art is otherwise unrecoverable; `LEGACY-NFR-015` and the privacy gate need an enumerable asset list.
- **Perceptual metrics (SSIM, DSSIM) instead of pixelmatch.** Rejected for now: the harness already implements pixelmatch deterministically; perceptual metrics hide pixel-art regressions (single-pixel sprite errors are real defects here). May be added as a secondary metric later.
- **A single strict threshold (0 %).** Rejected: font hinting and compositor differences across Chromium builds produce sub-perceptual noise; the 0.1 % band absorbs it while a dimension mismatch still fails.
- **A lenient threshold (≥ 2 %).** Rejected: on a 390×844 capture, 2 % is ~6,600 pixels, enough to hide a missing badge or wrong map-node state.
- **Pixel-art everywhere.** Rejected by reference invariant 3 and DP-09.
- **Fractional sprite scaling for responsive fit.** Rejected: destroys pixel-art legibility; integer scaling with layout flexibility is chosen.

## Consequences

### Positive

- Every production image is licensed and traceable; design references are cleanly separated from shipped assets.
- A two-layer token system lets the same components serve restrained and expressive surfaces, and makes low-gamification mode a token swap.
- The comparison method and bands are explicit, reviewable and calibratable, closing the "not to be invented" gap without pretending to be final.

### Negative

- The asset manifest and CI check add friction to every art change.
- Until calibration, Review-band results need human time for each candidate.
- Bundling web fonts and pinning Chromium versions adds maintenance.

## Control provenance

Prepared by the Systems Engineering control-plane agent (Claude Fable 5.1, Claude Code) for LEGACY-WORK-002 as a reviewable proposal. Inputs: `UX_CONTRACT.md`, `WORKFLOW.md`, reference baseline sections 5–6 and 9.3, `legacy_mockups` asset and docs listing (read-only), `legacy_verification_tooling/harness/capture.cjs` and `baselines/README.md` (read-only). Acceptance requires a human Systems Engineering decision; reference image approval is a separate owner/UX-reviewer action.
