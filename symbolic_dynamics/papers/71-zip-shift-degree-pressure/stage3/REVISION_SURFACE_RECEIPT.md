# Revision-surface receipt — P71

- Canonical review input: `stage2_5/draft_for_claim_registry_round1.md`
- Canonical-input SHA-256: `d085ef0f563ff9da62b83d522354128f48764156d4d84d32674223e0093a8e68`
- Derived anchored surface: `stage3/ANCHORED_REVIEW_DRAFT.md`
- Anchored-surface SHA-256: `8fe0c932d100144720ad8f1d0c127b6a0abe2effb5e0f9d4df06c15a4eda8c60`
- Block manifest SHA-256: `5a4992b5750316963255212280391379e1f0ab94f44d763dcbd7ef4d8e16b6b4`
- Anchor count: 71

The derived surface was made review-addressable by removing Pandoc-only raw
`span`/wrapper `div` markup and inserting stable `<!--block:B...-->` comments.
No prose, equation, citation, source, or canonical PDF was revised. Removing the
block comments from the derived surface and applying the same markup
normalization to the frozen input yields byte-identical streams (`cmp`: PASS).

Status: `DERIVED_SURFACE_REPLAY_PASS`; canonical manuscript mutation: `none`.
