# Final QA report -- Papers 112--116

Checkpoint: 2026-08-29 UTC

Result: **5/5 PASS INTERNAL; FINAL FREEZE; EXTERNAL HOLD**.

| paper | pages | bytes | exact control | independent gate | fonts | visual pages |
|---:|---:|---:|---:|---|---:|---:|
| P112 | 8 | 332,780 | 1,677,508 | `GO_INTERNAL` | 23/23 | 8/8 |
| P113 | 4 | 325,001 | 10,110,035 | `GO_INTERNAL` | 23/23 | 4/4 |
| P114 | 3 | 318,137 | 400,105 | `GO_INTERNAL` | 24/24 | 3/3 |
| P115 | 7 | 397,625 | 2,259,162 | `GO_INTERNAL` | 27/27 | 7/7 |
| P116 | 10 | 419,711 | 1,183,356 | `GO_INTERNAL` | 29/29 | 10/10 |
| **total** | **32** | **1,793,254** | **15,630,166** | **5/5** | **126/126** | **32/32** |

Assertion counts are heterogeneous finite-control executions, not independent
theorems, proof substitutes, or paper-quality scores.

## Control and build replay

After hostile-review repairs, every canonical verifier was run in a fresh
Python process with bytecode disabled and compared byte for byte with its
stored output.  All five comparisons passed.  The frozen assertion totals are
1,677,508; 10,110,035; 400,105; 2,259,162; and 1,183,356.

Each manuscript passed an isolated
`pdflatex -> bibtex -> pdflatex -> pdflatex` build.  Settled-build and extra-
pass PDFs reproduced the frozen SHA-256 digest byte for byte.  Final log/BLG
scans found zero emitted warnings, undefined citations or references,
multiply-defined labels, overfull/underfull boxes, fatal errors, emergency
stops, or actionable rerun requests.

## Bibliography, PDF, text, and visual gates

The paper-local bibliography closures are 13/13, 4/4, 11/11, 9/9, and 14/14,
for **51/51 cited and resolved entries**.  All PDFs are A4, unencrypted,
rotation zero, date-free, JavaScript-free, form-free, and carry an empty PDF
Author metadata field.

All **126/126** font rows are embedded, subsetted, and Unicode-mapped.  A
consistent fresh `pdftotext -layout` extraction contains **135,614 bytes** in
**1,838 lines**.  Placeholder, unresolved-reference, internal-draft,
verification-marker, and known stale-token scans are clean.

All **32/32** final pages were rendered and inspected page by page.  Titles,
abstracts, theorem statements, proofs, tables, equations, owner boundaries,
conclusions, and references are legible.  There is no clipping, overlap,
unexpected blank page, broken rule, missing glyph, malformed display, or
rotation.  Sparse final-reference whitespace is benign.

## Integrity gate

The five paper-local `SHA256SUMS` files cover **84 frozen evidence files** and
pass entry by entry.  Their own SHA-256 values are:

| paper | manifest entries | `SHA256SUMS` SHA-256 |
|---:|---:|---|
| P112 | 15 | `9153b7a0a9ab357ecf41dc16cbdbf4548755c9a1739e399b9c2b4a0534078273` |
| P113 | 15 | `375a6875c11826f6c9a09a31187753fddb2afd2af557157b462c04e2e3da25f9` |
| P114 | 15 | `b4c2786b29326100d3e262bbab6b8a44d33d12bd69cfe9473ebb0242aa46f596` |
| P115 | 15 | `321a6f3ed0cef6e60e36629467176d56410de31e6857a7dd0afbb0ce8a818ea1` |
| P116 | 24 | `ea091be59d97e05122fcd05dc94dc286a6c9eb8b85a39ac403c7dd244d488fa6` |

The five canonical PDF digests are frozen in
[`CANONICAL_PDF_MANIFEST.sha256`](CANONICAL_PDF_MANIFEST.sha256), which passes
5/5.  Its SHA-256 is
`6712a0cd5370610ff22136791e81d63cbed3278a109750e74d071d034333163c`.

This report certifies internal consistency, reproducibility, and artifact
mechanics only.  External release and owner clearance remain **HOLD**.
