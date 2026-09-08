# C422 — A uniform orbit bound for discrete Painlevé I over finite fields

Current manuscript-production entry, 8 September 2026: [final paper PDF](main.pdf).
The two complete manuscript-review rounds have passed; the coordinator accepted
both reviews and the two approved presentation edits. The same-input final
dual-build and all-page production checks have also passed. Batch-level formal
evaluation, integration and release adjudication remain coordinator-owned.

The final PDF is **14 pages, 352289 bytes**, SHA-256:

```text
83691c4b0f36d28373642ed8a6a1c290db29333986de601aaf914b08120c3079
```

The article proves the original all-state upper bound for the specified
resolved discrete Painlevé I system over every finite field: if the nonzero
phase multiplier has order `r`, the least native period `ell` satisfies
`r | ell` and `ell/r <= q + 1 + 2 sqrt(q)`. The proof treats all seven
native branches, including exceptional-line zero coordinates, and establishes
integrality and reducedness of every finite geometric invariant fibre.
It does not settle the source's distribution conjecture, assert universal
generic smoothness, or establish external Euler factors, root numbers or
spectral realizations. The PDF includes the full proof and its source boundaries.

## Current files and review trail

- [Final PDF](main.pdf), copied after checks from [fresh build 1](build_final1/main.pdf);
  [fresh build 2](build_final2/main.pdf) is byte-identical.
- [Final build report](FINAL_BUILD_REPORT.md): exact commands, actual exits,
  environment, hashes, metadata-only adjustment, and all 14 final-page checks.
- [Reviewed production manifest](build_round1/source_snapshot/source_inputs.sha256):
  the unchanged 17 TeX/Bib inputs; verify it from this paper directory.
- [LaTeX entry](main.tex), [bibliography](references.bib), and the section/table
  files it includes. The annotated [table index](figures/latex_includes.tex)
  is navigation only, not an additional compiler input.
- [Round-one full raw review](../../manuscript_reviews/round1/C422_REVIEW.md),
  [author's itemized response](REVISION_ROUND1.md), and
  [round-two full raw review](../../manuscript_reviews/round2/C422_REVIEW.md).
  Both reviews have zero mandatory fixes; the two optional first-round
  presentation items were accepted, implemented, and closed in round two.

These are current-team AI-assisted nonauthor reviews, not external human
peer review or a claim of worldwide priority.

## Preserved history

The [original baseline PDF](main_round0_original.pdf),
[successful baseline build](build_round0_attempt2/main.pdf),
[reviewed revision PDF](build_round1/main.pdf),
[original source snapshot](source_snapshot_round0/main.tex), and
[revised source snapshot](build_round1/source_snapshot/main.tex) are retained.
The original failed build directory and all old logs were not cleaned.

[BUILD_REPORT.md](BUILD_REPORT.md), [SOURCES_AND_EVIDENCE.md](SOURCES_AND_EVIDENCE.md),
[PAPER_PLAN.md](PAPER_PLAN.md), and [REVISION_ROUND1.md](REVISION_ROUND1.md)
retain their historical stage descriptions, including then-pending gates.
This README and the final build report identify the current production status;
old receipts were not rewritten to imply that later actions had already occurred.

## Reproduce without replacing retained outputs

The exact two commands actually executed are in [FINAL_BUILD_REPORT.md](FINAL_BUILD_REPORT.md).
For another reproduction, use a new output directory, first confirming it does
not exist. From this paper directory, an example is:

```bash
set -euo pipefail
sha256sum -c build_round1/source_snapshot/source_inputs.sha256
test ! -e build_reproduce_new
test ! -L build_reproduce_new
mkdir build_reproduce_new
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build_reproduce_new \
  -pdflatex='pdflatex %O -jobname=main "\pdftrailerid{}\input{main.tex}"' \
  main.tex 2>&1 | tee build_reproduce_new/compile_console.log
cmp main.pdf build_reproduce_new/main.pdf
```

This is an example for a future run, not an additional execution receipt.
The compiler-only `\pdftrailerid{}` omits the path/time-dependent automatic
PDF ID while leaving reviewed TeX unchanged. The final PDF differs from the
approved revision solely by this 75-character metadata entry; a read-only
exact comparison is documented in the report. No mathematical program was
rerun to prepare the manuscript or its final build.
