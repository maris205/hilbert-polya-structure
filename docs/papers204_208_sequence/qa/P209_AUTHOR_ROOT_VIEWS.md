# P209: root inspection of author builds and all four pages

2026-09-07 UTC. **PASS_AUTHOR_BUILD_ADOPTION_SCOPE / HOLD_EXTERNAL**.
This is author-stage build/view evidence, not manuscript A/B, Round0 freeze,
terminal cold builds or paper completion.

Root read the full author recorder and its actual build receipt, engine/
font results and final diagnostics. The [new read-only build inspector](inspect_p209_author_builds.py)
and [full actual output](P209_AUTHOR_BUILDS_ROOT_INSPECTION.actual.json)
checked both 680-payload build seals and both 10-payload outer-launch seals
completely, then checked every payload again at the end. All 125 commands
per build actually exited zero, including 110 linkage commands and the
source-only pdflatex/BibTeX/pdflatex/pdflatex sequence. The paper-compile
checks use these explicit passes because latexmk is unavailable; no tool
installation, source deletion or external submission is implied.

Each build has 118,409 before/after known inputs, 4,598 runtime files,
113,733 TeX resources and 131 actually recorded external TeX/bibliography
inputs. Root checked every recorded before/after equality, recaptured the
declared TeX path sets, checked configuration presence/path sets and hashed
all 118,418 distinct current input paths across the pair. The initial
eight-file source-only sets match the unchanged live TeX/bibliography.
All three exclusive user TeX roots remain absent. Observed runtime closure
has no uncovered file or bytecode. These are bounded recorded inventories
and sampled observations, not continuous tracing or OS-hermetic execution.

Both PDFs have four A4 pages, 280,267 bytes and SHA-256
`ca2e381904905939e121b7931641b050ba24657c16661df3bb5008c88c28884f`.
All twenty reported font rows are embedded. The final undefined-reference,
citation, overfull, underfull, warning and rerun lists are empty; the PDF
text has no unresolved markers. Root's actual raw `cmp` of the two PDFs
exited zero, as did four separate comparisons of corresponding page PNGs.
No compiler or renderer was rerun by the archive inspector.

## Actual root page views

Root actually opened and visually inspected the four page PNGs from
`papers/209-ordered-fibre-threading/author_build_01/cold_build/pages/`.
This was four individual images, not a file listing or hash-only check.
The separately proved raw identity extends those same page bytes to build
02; root does not claim eight page-opening actions.

| Page | Actual content inspected | Result |
|---|---|---|
| 1 | Anonymous title/abstract, literal map, cycle witness and source comparison | Legible; no clipping, overlapping text or missing symbols |
| 2 | Recurrent theorem, image inclusions, frozen heights and necessity proof | Equations and proof readable; continuation to page 3 is coherent |
| 3 | Exact labelled period, all-target decoder and unique extremizer proofs | Complete displayed formulas and proof endings; no layout defect |
| 4 | Fixed original finite-check scope, limitations and four references | No unresolved citation markers; wrapped URLs/DOI remain legible |

The viewed page digests, in order, are:

```text
fc7bb428c539008212cbfa93c094101aa96472513787136a8e8023a4c645f7af
8c93a002f94d9191c39f514656f444c5e8b1cbae53e83be95d3150d65ba4bdd3
6843be793eafb17ae752a441ca8119cc09032c75c163ee5afd03b292b3a9fcd7
0a320b457523122f55637c5d34176e26aaa37129974459a1808b6b700c43888d
```

The main text concludes on page 4 and the references begin on that page;
there is no appendix or submission-specific page-limit assertion. Root
requests no TeX or scientific change from these views. The unchanged
manuscript still excludes a sharp entrance clock and general-time inverse.
The author package's final documentary seal and root's separate fresh
mathematical pair/adoption/freeze obligations remain distinct.
