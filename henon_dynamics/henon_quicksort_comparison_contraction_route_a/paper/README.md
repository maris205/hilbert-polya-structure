# Paper build

The single source `main.tex` selects three substantive states with
`\CRevisionRound`: round 0 closes exact finite PGFs and moments; round 1 adds
the contraction and mixed-subproblem limsup proof; round 2 adds the `L3`
tree-series license, exact non-Gaussian moment, evidence, and Route-A boundary.

The release script compiles each round twice in each of two fresh directories
under `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
It requires both fresh outputs to equal the archived PDF, checks warnings and
fonts with Poppler, rasterizes every page, and enforces
`main.pdf == main_round2.pdf`.
