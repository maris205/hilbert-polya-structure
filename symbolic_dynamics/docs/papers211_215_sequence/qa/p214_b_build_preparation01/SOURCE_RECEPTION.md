# P214 Review B no-change build source prepared

2026-09-11 UTC. `SOURCE_READY_NOT_BUILT`.

The complete 144-line `BUILD_REQUEST.sh` was read and Bash-syntax checked.
It starts from accepted physical `frozen_round1`, copies only the nine pinned
TeX/Bib sources into a fresh cold tree, checks exact source membership and
absence of products, then proposes the fixed pdflatex/BibTeX/pdflatex/
pdflatex sequence, diagnostics, fonts, text and all-page rendering.

All nine source rows freshly pass and are byte-identical to the accepted A
build02 source key; this is the proposed no-change B build. The mechanism is
mechanical reuse of the accepted ordinary P214 source-only policy, not reuse
of A's grant, output, page views or review credit. The output path is new
`reviews/p214_b/build01` and was absent at preparation.

The recipe also checks seven B science/history pins before and after: accepted
initial DATA, B canonical, strict pair and all three preserved receiver-failure
notes. It does not alter or relabel those failures. No TeX/build/render or
scientific verifier was run by source preparation. `HOLD_EXTERNAL`.
