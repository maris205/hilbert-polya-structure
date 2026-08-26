# Revision-surface receipt — P68

- Canonical review input: `stage2_5/draft_for_claim_registry_round1.md`
- Canonical-input SHA-256: `bb07f6f44433f69e76697dba6aa1b096e695905d9a1485a199e38396b3478806`
- Derived anchored surface: `stage3/ANCHORED_REVIEW_DRAFT.md`
- Anchored-surface SHA-256: `232b1b6b51d15a7a87d62266fe69ad5ba4a2cad09ed0ba154812b87126f1b412`
- Block manifest SHA-256: `8ac140bcbbf0928c14208363feb2053709cd93f83ab43cb91f1f15deb5bab7b3`
- Anchor count: 60

The derived surface was made review-addressable by removing Pandoc-only raw
`span`/wrapper `div` markup and inserting stable `<!--block:B...-->` comments.
No prose, equation, citation, source, or canonical PDF was revised. Removing the
block comments from the derived surface and applying the same markup
normalization to the frozen input yields byte-identical streams (`cmp`: PASS).

Status: `DERIVED_SURFACE_REPLAY_PASS`; canonical manuscript mutation: `none`.
