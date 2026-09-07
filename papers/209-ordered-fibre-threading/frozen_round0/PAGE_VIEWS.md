# P209 actual author page views

2026-09-07 UTC. The P209 author actually opened all four rendered pages
from **each** completed source-only build, using eight individual image
view calls. This is an author visual inspection, not an independent
manuscript review. It is not inferred from PNG existence, matching hashes
or root's separately reported viewing.

Both source PDFs are 280,267 bytes with SHA256
`ca2e381904905939e121b7931641b050ba24657c16661df3bb5008c88c28884f`.
Both are four pages; the render commands used the installed `pdftoppm`
at 120 dpi. Their original command and PDF pins are in the immutable
build receipts. The corresponding page digests were checked after viewing.

| Page | Actual build 01 image | Actual build 02 image | Visual inspection |
|---|---|---|---|
| 1 | [01 page 1](author_build_01/cold_build/pages/page-1.png) | [02 page 1](author_build_02/cold_build/pages/page-1.png) | Title, anonymous author and abstract fit; old-fibre rule and two-cycle display are legible; related-work text and citations stay within margins. |
| 2 | [01 page 2](author_build_01/cold_build/pages/page-2.png) | [02 page 2](author_build_02/cold_build/pages/page-2.png) | Recurrent theorem, labelled-period formula, finite/infinite heights and image/head inequalities are legible; proof labels and equations do not overlap. The sufficiency paragraph continues naturally onto page 3. |
| 3 | [01 page 3](author_build_01/cold_build/pages/page-3.png) | [02 page 3](author_build_02/cold_build/pages/page-3.png) | Period proof ends cleanly; both decoder conditions, exact inverse, unchanged-arrow example and unique-extremizer proof fit. All equation references and mathematical symbols render. |
| 4 | [01 page 4](author_build_01/cold_build/pages/page-4.png) | [02 page 4](author_build_02/cold_build/pages/page-4.png) | Finite-check limitations and all four references are readable. URL/DOI line breaks fit their entries. Remaining white space is natural at the note's end, not a missing page. |

The corresponding PNGs have these same hashes in both builds:

| Page | SHA256 |
|---|---|
| 1 | `fc7bb428c539008212cbfa93c094101aa96472513787136a8e8023a4c645f7af` |
| 2 | `8c93a002f94d9191c39f514656f444c5e8b1cbae53e83be95d3150d65ba4bdd3` |
| 3 | `6843be793eafb17ae752a441ca8119cc09032c75c163ee5afd03b292b3a9fcd7` |
| 4 | `0a320b457523122f55637c5d34176e26aaa37129974459a1808b6b700c43888d` |

**Result: all eight actual page views passed.** No clipping, overlap,
missing symbols, anonymous-identity leak or material layout issue was
found. No source edit follows these views. This report records precisely
these rendered PDFs; later changed PDFs require their own affected views.
