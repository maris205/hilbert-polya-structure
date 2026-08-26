# Revision-surface receipt — P67

- Canonical review input: `stage2_5/draft_for_claim_registry_round1.md`
- Canonical-input SHA-256: `cce01e567fca31595efe200e1b31b9d652531e200d83e2ac7337e7acc0477e6a`
- Derived anchored surface: `stage3/ANCHORED_REVIEW_DRAFT.md`
- Anchored-surface SHA-256: `9acf34f77b9a4c65ee7523322ee75388d6e241296675439b07f796a2be086ef8`
- Block manifest SHA-256: `00c0888fbc5d7478147c2b41b0effecf6bb0b0b22a095ee441f45e14d5d541cf`
- Anchor count: 98

The derived surface was made review-addressable by removing Pandoc-only raw
`span`/wrapper `div` markup and inserting stable `<!--block:B...-->` comments.
No prose, equation, citation, source, or canonical PDF was revised. Removing the
block comments from the derived surface and applying the same markup
normalization to the frozen input yields byte-identical streams (`cmp`: PASS).

Status: `DERIVED_SURFACE_REPLAY_PASS`; canonical manuscript mutation: `none`.
