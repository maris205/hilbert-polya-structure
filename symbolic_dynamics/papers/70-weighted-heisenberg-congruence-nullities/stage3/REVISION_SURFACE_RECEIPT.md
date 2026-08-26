# Revision-surface receipt — P70

- Canonical review input: `stage2_5/draft_for_claim_registry_round1.md`
- Canonical-input SHA-256: `7945d73d2bdede0ec36743b71ccbaf34f91baadf2363a5a3c85bcaf5509b2ec7`
- Derived anchored surface: `stage3/ANCHORED_REVIEW_DRAFT.md`
- Anchored-surface SHA-256: `0fa45f796d7cc3cec28313c34d20c3c3ca5a8fabb18d6bbcdf69fb42e7886fe7`
- Block manifest SHA-256: `52a2e2672262853285cb52ebb71a680dd88c85a4106788d86bf380a33d1f1713`
- Anchor count: 71

The derived surface was made review-addressable by removing Pandoc-only raw
`span`/wrapper `div` markup and inserting stable `<!--block:B...-->` comments.
No prose, equation, citation, source, or canonical PDF was revised. Removing the
block comments from the derived surface and applying the same markup
normalization to the frozen input yields byte-identical streams (`cmp`: PASS).

Status: `DERIVED_SURFACE_REPLAY_PASS`; canonical manuscript mutation: `none`.
