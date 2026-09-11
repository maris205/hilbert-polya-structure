# P196 Review-B build and PDF QA

## Frozen artifact

The pinned Round-1 PDF and current working PDF are byte-identical:

```text
file: papers/196-cyclic-godel-implication/main_round1.pdf
pages: 3
bytes: 345,811
SHA-256: bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948
current main.pdf SHA-256: bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948
```

The Round-1 and Round-0 PDFs also have the same hash; Review A requested no
author delta.

## Source-only cold builds

Only the pinned `main.tex` and `references.bib` were copied into each of two
fresh `/tmp` directories.  Both builds used:

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Environment:

```text
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
Poppler pdfinfo 22.02.0
```

Results:

```text
cold build 1 SHA-256: bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948
cold build 2 SHA-256: bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948
Round-1 equality: PASS
cold-build byte replay: PASS
extracted-text SHA-256: 5f0dce5f3800b07eaec4166b957bd766fa56ea49a1b9559ea1933d2a828be8c6
```

Intermediate passes emit the expected first-build citation/reference rerun
messages.  The final `main.log` has zero LaTeX/package warnings, zero overfull
or underfull boxes, zero unresolved citations or references, and no fatal or
emergency diagnostic.

## Structural and active-content checks

```text
page size: A4, 595.276 x 841.89 pt
PDF version: 1.5
encrypted: no
forms: none
JavaScript: no
embedded files: 0
signatures: none
metadata stream: no
title/author/subject/keywords/creator/producer metadata: blank
font rows: 27
fonts embedded/subsetted/Unicode mapped: 27/27/27
rasterized images stored in PDF: 0
citation keys / resolved bibliography records: 5 / 5
```

The source contains the anonymous author label and no identifying PDF
metadata.  All numbered equations, theorem labels, and bibliography entries
appear in extracted text.

## Page-level visual inspection

All pages were rasterized independently at 160 dpi.  Raster hashes were:

```text
page 1: bc06a777808e789d72ac27515f4af67e8566a6610f2cea887eeca82547564cda
page 2: ed9287dac1b636d9aafa5eef63fb5af7ef8be2f16970655fdf58c74cbc0d889a
page 3: 53e0401f6623f98e71262f72a0ef5f2a14cb2370bdecd1a34f2ef763a12ff75d
```

- Page 1: title, anonymous byline, abstract, definitions, ownership boundary,
  core theorem, and the beginning of its proof are legible and inside the
  text block.
- Page 2: the continued core proof, transfer theorem, characteristic
  recurrence, gap definition, and fibre theorem are complete and aligned.
- Page 3: the fibre proof, mass identity, limitations, and all five references
  are legible; there is no clipping, overlap, missing glyph, malformed
  display, or unintended blank page.

The page break inside the core proof and the fibre proof's continuation are
ordinary, unambiguous continuations.  No presentation finding was opened.

Build/PDF decision: `PASS` for the pinned Round-1 artifact.  Review B did not
modify the manuscript or its build products.
