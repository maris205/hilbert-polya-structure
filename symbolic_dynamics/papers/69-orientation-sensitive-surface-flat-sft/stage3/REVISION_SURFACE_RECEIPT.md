# Revision-surface receipt — P69

- Canonical review input: `stage2_5/draft_for_claim_registry_round1.md`
- Canonical-input SHA-256: `276cb82f2fcb4d2aaa70a609bb999c0297261ad1fbfd870e3785fc2b08c8760b`
- Derived anchored surface: `stage3/ANCHORED_REVIEW_DRAFT.md`
- Anchored-surface SHA-256: `c4715fd7f9f34b37911b6da11634bde04326a635393f8fdec8cacaca456ddf9d`
- Block manifest SHA-256: `c12f7f6975ab1e066999949a56bcbf5366bf149172ec550966f0bed2806f3e4d`
- Anchor count: 115

The derived surface was made review-addressable by removing Pandoc-only raw
`span`/wrapper `div` markup and inserting stable `<!--block:B...-->` comments.
No prose, equation, citation, source, or canonical PDF was revised. Removing the
block comments from the derived surface and applying the same markup
normalization to the frozen input yields byte-identical streams (`cmp`: PASS).

Status: `DERIVED_SURFACE_REPLAY_PASS`; canonical manuscript mutation: `none`.
