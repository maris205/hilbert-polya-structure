# Compile report

## Fixed build contract

- Engine: LuaLaTeX, two settled passes in a fresh directory.
- Epoch: `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Determinism: each revision round is built in two independent fresh
  directories and required to be byte-identical.
- Trailer identifier: fixed in `main.tex`.

## Final round ledger

| Round | Content boundary | Pages | Embedded/subset font rows |
|---|---|---:|---:|
| 0 | branch-safe Schur function and exactly two physical poles | 2 | 17 |
| 1 | sign-correct Stone-complete spectral measure, residues, mass, and scattering | 3 | 19 |
| 2 | degenerations, evidence, sources, collisions, and Route-A scope | 4 | 21 |

`main.pdf` is byte-identical to `main_round2.pdf`.  All three revision PDFs
are byte-distinct.  The settled logs contain zero LaTeX/package warnings,
overfull boxes, underfull boxes, undefined references/citations, rerun
requests, or missing-character reports.  Every font row is embedded and
subset.  `pdftotext -layout` has no forbidden control byte or literal TeX
debris, and every page rasterizes successfully with `pdftoppm`.

The exact PDF hashes and per-page raster byte counts are recorded in the
self-excluding `C345_RELEASE_MANIFEST.json`.
