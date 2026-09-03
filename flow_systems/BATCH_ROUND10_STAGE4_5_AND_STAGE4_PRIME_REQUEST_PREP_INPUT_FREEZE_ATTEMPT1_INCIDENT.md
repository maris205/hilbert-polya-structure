# Input-freeze attempt 1 incident

Date: **2026-09-04 workflow date**

The first input-freeze emission parsed as JSON but failed the independent
unique-path invariant. Three dedicated Route-crosswalk paths were also selected
by the broad `stage4_*` track-input glob:

- `papers/29-bianchi-ideal-owner-refinement/notes/stage4_route_crosswalk.md`;
- `papers/32-homology-cover-renormalization-uniformity/notes/stage4_route_crosswalk.md`;
- `papers/33-bolza-control-matched-census/notes/stage4_route_crosswalk.md`.

The invalid attempt is preserved as
`BATCH_ROUND10_STAGE4_5_AND_STAGE4_PRIME_REQUEST_PREP_INPUT_FREEZE_ATTEMPT1_INVALID.json`
with SHA-256
`9c07dafac34dabd71f543b744dadf6aa45f42a2817a3e8b0d60a76355e2ffbc4`.
It is not an authority input and must not be consumed downstream.

The builder was narrowed to subtract the two dedicated per-paper paths
(`stage1_prestart_brief.md` and `stage4_route_crosswalk.md`) from the broad
track-input selection before emission. No manuscript, bibliography, PDF,
science/result file, initial-system definition, Route evaluator, or Route
coordinate changed.
