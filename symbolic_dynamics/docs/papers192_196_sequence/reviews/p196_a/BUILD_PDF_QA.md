# P196 Review-A build and PDF QA

## Frozen author-control replay

The author verifier was treated as a pinned black-box control and was replayed
only after the independent reviewer program had passed.

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
exit: 0
canonical SHA-256: f6c7bb13a0e43a97967ad4f97c3b1267ff292f8c6642393d66279de7b005a2fd
```

## Reviewer replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a_p196.py | cmp - CANONICAL.txt
replay 1 exit: 0
replay 2 exit: 0
stdout SHA-256: fffc707f1e80dc5b7ff79e0cacbd6d2d175c827760789b0fd6e44862b91e9a37
states/transitions: 123,032 / 123,032
assertions: 370,380
control digest: f382efcbf3d3bcf0886753db89f27b174817d6351c49cb5547a174268b482122
```

The reviewer verifier uses only the Python standard library and imports no
author file.

## Cold build

Only frozen `main.tex` and `references.bib` were copied to each of two fresh
temporary directories.  With `SOURCE_DATE_EPOCH=1704067200` and `TZ=UTC`, the
sequence `pdflatex; bibtex; pdflatex; pdflatex` produced byte-identical PDFs:

```text
pages: 3
page size: A4, 595.276 x 841.89 pt
bytes: 345,811
SHA-256: bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948
extracted-text SHA-256: 5f0dce5f3800b07eaec4166b957bd766fa56ea49a1b9559ea1933d2a828be8c6
warning/bad-box/unresolved/fatal matches: 0
font rows embedded/subsetted/Unicode: 27/27/27
encrypted: no
forms: none
JavaScript: no
metadata stream: no
```

The cold-build hash equals both frozen files, `main.pdf` and
`main_round0_original.pdf`.

## Visual inspection

All three pages were rasterized at 160 dpi and inspected individually.  The
title, abstract, theorem statements, long binomial formulas, proof displays,
limitations paragraph, declarations, and bibliography are visible and remain
inside the page box.  No clipping, overlap, missing glyph, malformed display,
stranded heading, unintended blank page, or suspicious active content was
found.

Build/PDF decision: `PASS` for frozen Round 0.
