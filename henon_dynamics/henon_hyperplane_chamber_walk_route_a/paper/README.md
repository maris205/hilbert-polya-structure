# Paper artifacts

`main.tex` is the final round-2 source and `main.pdf` is its deterministic final
build.  The retained content-distinct round artifacts are:

- `main_round0_original.pdf`: theorem/operator core;
- `main_round1.pdf`: stationary sampler, strict-SST boundary, and nonseparating
  simplex repair;
- `main_round2.pdf`: ownership ledger, finite-oracle audit, and final Route-A
  verdict.

Compilation uses `SOURCE_DATE_EPOCH=1787788800`, `TZ=UTC`, and `pdflatex`
twice per fresh build.  The final PDF must have embedded fonts, a clean log, no
undefined references/citations, and visual inspection of every page.
