# P212 two terminal build artifacts accepted

2026-09-11 UTC. ACCEPT_TWO_TERMINAL_SOURCE_ONLY_BUILD_ARTIFACTS. The two
separately granted commands returned actual sessions 51996 and 30227 and each
completed exit 0. Each output tree has exactly 160 files, controller exit 0,
14 recorded build/diagnostic/page supervisor exits all 0, and zero bytes over
all controller/per-command stderr streams. Each source-only tree began with
exactly the eight frozen TeX/Bib inputs; pre/post runtime, frozen source and
cold source guard outputs are raw equal.

Each build retained eight before/after pass snapshots. Presence counts are:
pass1 0->4, BibTeX 4->6, pass2 6->6, pass3 6->6 among the fixed eight generated
roles. All six final product manifest entries pass from the correct
`source_only` base. AUX and BBL each contain all five bibliography keys; the
actual corrected Holroyd Lemma 4.9 body locator and three-locator bibliography
note are present. Each final FLS contains 236 ordered INPUT and 3 OUTPUT
events. The raw FLS files differ because their first/related records carry
different cold-build absolute roots; substituting only `cold_build_1` versus
`cold_build_2` makes their complete ordered event streams equal. No raw FLS
equality is claimed.

Both PDFs are six-page A4, 191507 bytes, SHA-256
`096adcb6b24fd6ae1853cf8fecff4cd0acc1a6d4b9aab0e9470bdb3e66997c31`.
They are whole-byte equal to each other and frozen Round2. LOG, AUX, BBL and
BLG pairs are also raw equal. Each font table has 13 rows, all Type 1,
embedded/subset/Unicode yes. Each complete PDF text capture has 20,406 bytes
and six form-feed page frames. Final diagnostic selection contains only
`main.log:3: file:line:error style messages enabled.`, an informational
format announcement; there are no final warnings, undefined references,
overfull/underfull boxes, missing characters or BibTeX errors.

Reception failures remain explicit. A preflight first used the Round2
directory-relative manifest from the wrong cwd; no build was created. A later
FINAL_PRODUCTS check likewise first used workspace cwd before succeeding from
source_only. A deliberately too-strong raw FLS pair assertion failed on the
expected cwd identity. `identify` was unavailable, and a first whitespace
field parser misclassified font columns; `file`, PNG headers and the full font
rows supplied the corrected checks. None is hidden or labelled a build retry.
No source, PDF, frozen file, science, Git or external action changed.
