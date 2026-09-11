# P203 deterministic author builds

Date: 2026-09-05 UTC. Author Round0 build/visual QA only; not final
manuscript-review or terminal-batch acceptance.

## Reproduce a source-only build

BUILD.sh is executable and accepts a new, explicit absolute directory:

```sh
./BUILD.sh /absolute/new/p203-build-directory
```

It refuses an existing target, copies only main.tex and references.bib,
and runs pdflatex, BibTeX, pdflatex, pdflatex. The environment fixes
SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1, TZ=UTC and LC_ALL=C.
The preamble suppresses PDF dates, identifiers and identifying metadata.
latexmk was not installed; the explicit dependency-correct four-pass chain
is the documented fallback. All pass stdout, the final main.log, BibTeX
log and recorder files remain physically in each build directory.

## Two actual final author cold builds

Both followed the final source presentation fixes and used new directories:

```sh
./BUILD.sh /root/autodl-tmp/symbolic_dynamics/papers/203-monochromatic-triangle-complementation/qa/cold_build1
./BUILD.sh /root/autodl-tmp/symbolic_dynamics/papers/203-monochromatic-triangle-complementation/qa/cold_build2
```

Build1 launch bbf219/session99805, completion9c45bb/exit0.
Build2 launch3f1e1b/session78654, completionf89023/exit0.
Actual `cmp` returned0 in receipt4bbeff. Both PDFs have SHA-256
`617cea5d4f8b50a9946d05bafc2cfbf6fb01bbe45dab754813b07f4f12cc1167`.
The earlier qa/draft_build is preserved but is not one of these final
two builds. No existing .aux/.bbl/.pdf was copied into either cold build.

## Mechanical and visual output

The final PDF is four A4 pages and 286,868 bytes, with all21 font entries
embedded. No undefined references, undefined citations, overfull/underfull
boxes, LaTeX warnings or errors matched either final main.log. PDF metadata
author/title/creator/producer fields are empty; the visible byline is Anonymous.

All four final pages were rendered at120dpi to qa/visual_round0/ and
actually viewed individually, then the complete PDF text was inspected.
Page1: title/abstract, exact setup and first obstruction; no clipping.
Page2: complete no-return and sharp witness proofs, then D/C; legible
equation and aligned conditions. Page3: inverse/max theorem and S/K
certificate definitions; no margin or label overflow. Page4: equality
proof, finite-check table, limitations and both references; the table no
longer splits the following paragraph. All proofs are in the main text.

These observations are author-side QA, not paper A/B, and cannot erase
the historical Stage1 archival finding disclosed in PROVENANCE.md.
