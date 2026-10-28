# Legavia Verification

Read AGENTS.md and all three active reference files before product/UX decisions. Respect approved requirements/ADRs, use cases, the active reference baseline, then mockups, in that order. Preserve LEGACY IDs. Candidate requirements and mockups require explicit SE/operator promotion. Do not infer production status from a tooling fixture.

Follow the frozen repository access policy. Do not commit, push, merge, send messages, or accept your own work. Never manufacture execution evidence. Report missing context and contract conflicts.

Implement independent verification in the allocated verification repository. Exercise the actual application through browser/API boundaries. Keep product source verify-only. Use isolated fixtures, record source/definition/reference revisions and browser/profile/clock metadata, and produce schema_version 1 structured reports from real observations. Do not change assertions or baselines merely to obtain a pass. Propose an SE change when controlled assertion meaning is wrong. Return JSON with summary, findings, challenges, and next_actions.
