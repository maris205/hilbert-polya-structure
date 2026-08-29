# C231 compile report

Build contract: LuaLaTeX (LuaHBTeX 1.14.0), fixed
`SOURCE_DATE_EPOCH=1787875200`, two settled passes in each of two independent
fresh directories per revision.  Settled logs are scanned for warnings,
overfull/underfull boxes, undefined references, missing citations, duplicate
destinations, missing characters, and errors.  Final pages are visually
checked at 120 dpi; all 25 listed fonts are embedded and subset.

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 2 | `97fd5fa4144e89b2a6046987219cdae3d1ed180fa9ffe2ded3dbed4c33fb199d` |
| `main_round1.pdf` | 3 | `6865d6baa8488c7b4f6b7b7526f08151b83f16f59f72668ccb45d0d249300114` |
| `main_round2.pdf` | 3 | `65c3b37e47c36442fa9faebc694eaf4c3b59fd31831a89d50b66d71c3d9f578f` |
| `main.pdf` | 3 | `65c3b37e47c36442fa9faebc694eaf4c3b59fd31831a89d50b66d71c3d9f578f` |

The three round hashes are distinct and `main.pdf` is byte-identical to
`main_round2.pdf`.  Page counts are 2/3/3; the declaration block follows a page
break so it is not truncated.  A 120-dpi visual inspection found no clipping,
overlap, broken glyph, or orphaned heading.  The independent checker reports
204 assertions, SymPy reports 13 identities, byte replay is stable, and the
hostile suite catches 21/21 mutations.
