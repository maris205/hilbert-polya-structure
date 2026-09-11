# P192 Review-A build and PDF QA

**Decision:** `PASS` on the accepted repair.  
**Open build/PDF findings:** `0 Critical / 0 Major / 0 Minor`.  
**External state:** `OWNER_RED_AMBER / HOLD_EXTERNAL`.

## Frozen author-control replay

The author programs were treated as pinned black-box controls and replayed
only after the independent reviewer implementation passed.

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
exit: 0

g++ -std=c++17 -O3 -Wall -Wextra -pedantic code/verify_n9.cpp -o /tmp/p192_review_a_n9
/tmp/p192_review_a_n9 | cmp - code/CANONICAL_N9.txt
exit: 0; compiler warnings: 0
```

The `n=9` transcript remains finite conjecture evidence only.  Review A does
not use it in a proof.

## Reviewer replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a_p192.py | cmp - CANONICAL.txt
replay 1 exit: 0
replay 2 exit: 0
stdout SHA-256: d5b3433826d96c0ae3746316bdeae4d61d922482355857a04938fdab8a38bf6c
sequences scanned: 769,601
factorizations/transitions/targets: 1,441 / 1,441 / 1,441
assertions: 305,104
control digest: 63cd3a6f4f86f054d128508f7cf399ef80b5bacb93f168d493325b5b577d1410
```

The reviewer verifier uses only the Python standard library.  It imports no
author file and generates the carrier by direct product filtering.

## Accepted-repair cold build

Only accepted `main.tex` and `references.bib` were copied to each of two fresh
temporary directories.  With `SOURCE_DATE_EPOCH=1788480000`,
`FORCE_SOURCE_DATE=1`, and `TZ=UTC`, the
sequence `pdflatex; bibtex; pdflatex; pdflatex` produced byte-identical PDFs:

```text
pages: 4
page size: A4, 595.276 x 841.89 pt
bytes: 323,972
SHA-256: e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57
extracted-text SHA-256: 5cd9a75128779e52679e4513061c55d127e0e164eef6238d095768dbb8efcf3e
warning/bad-box/unresolved/fatal matches: 0
font rows embedded/subsetted/Unicode: 25/25/25
encrypted: no
forms: none
JavaScript: no
metadata stream: no
```

The two cold outputs are byte-identical to the accepted-repair `main.pdf`.
The immutable Round-0 baseline is separately pinned as
`main_round0_original.pdf`, a three-page file with SHA-256
`aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1`.
It is not relabelled as the repaired current PDF.  The superseded
pre-metadata-audit snapshot is not an input to this review.

## Visual inspection

All four accepted-repair pages were rasterized at 160 dpi and inspected
individually.  The title, abstract, factorization displays, theorem blocks,
inverse criterion, conjecture quarantine, limitations, and bibliography are
visible and remain inside the page box.  No clipping, overlap, missing glyph,
malformed display, stranded heading, unintended blank page, or suspicious
active content was found.  Page 4 is a deliberately sparse bibliography
continuation, not a layout defect.

Build/PDF decision: the accepted repair is technically `PASS`.  Two fresh
cold builds and the visual reinspection close the build surface; the
immutable Round-0 PDF remains preserved only as the review baseline.
