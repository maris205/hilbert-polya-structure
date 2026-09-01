# P142 Round-0 author build record

Date: 2026-09-01 UTC.  External status: `HOLD_EXTERNAL`.

## Canonical verifier replay

```bash
cmp -s verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 verify_p142.py)
```

Result: `cmp=0`.  The dependency-free exact replay completed in under one
second in the current environment and ended with

```text
TOTAL_ASSERTIONS=319074
STATUS=PASS
```

Coverage is 508 odd-prime boxes with 33,528 state/orbit/fibre targets, twelve
fixed iterates per box, and 47 binary boxes with 1,222 states and sixteen
equal-valuation exceptions.

## Manuscript build

The canonical four-stage protocol was

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All stages exited zero.  The settled `main.log` and `main.blg` contain:

```text
LaTeX/package warnings     0
overfull/underfull boxes   0
undefined citations       0
undefined references      0
multiply defined labels   0
rerun requests            0
BibTeX warnings            0
```

Only three bibliography entries are present, all three are cited, and there
are no missing or uncited keys.

## Isolated reproducibility build

Only `main.tex` and `references.bib` were copied to a fresh directory under
`/tmp`, then compiled with the same four stages.  The isolated PDF compared
byte for byte with the paper-local `main.pdf` (`cmp=0`).  This is an
author-side reproducibility check, not an external release certification.

## PDF audit

```text
pages=5
page_size=A4 (595.276 x 841.89 pt)
file_size=373697 bytes
pdf_version=1.5
encrypted=no
forms=none
javascript=no
custom_metadata=no
metadata_stream=no
visible_author=Anonymous
pdf_author_metadata=blank
font_rows=28
nonembedded_fonts=0
text_lines=364
text_words=2604
text_bytes=13253
```

All five pages were rasterized at 120 dpi and inspected.  No clipping,
collision, malformed display, illegible table, or orphaned heading was found.
Page 5 contains the three-item bibliography and intentional residual
whitespace.  No figure is required or present, as frozen in `PAPER_PLAN.md`.

## Frozen Round-0 hashes

```text
feca558213f6ea5e934016d44d330d430d0b4fa8fac0be7cd3c9a1ede90bae06  main.tex
d10774849bef277c7f8212ab1a590bb72e4e7aa56b3c851a1f1c729ef91d8ee4  references.bib
88198d07e2aed9e7cd1c46262808507ba25af54d2a7764b9933fa40ccd78a0a8  main.pdf
88198d07e2aed9e7cd1c46262808507ba25af54d2a7764b9933fa40ccd78a0a8  main_round0_original.pdf
6fdebe63456cb73707e5595141d2f4d51106d7be23b3766c903bcacbdabd7a19  verify_p142.py
038c6655f517df31e0ecfbba257823169619347fd1b3d27354cdd3dc428f7fa1  verification_output.txt
```

`main.pdf` and `main_round0_original.pdf` compare byte for byte.  These are
author-side Round-0 pins, not novelty, priority, ownership, or submission
clearance.  No review artifacts were created.

## Reviewed build closure

- Round 1 repaired the equality-branch overlap wording and froze
  `main_round1.pdf` at
  `205059fecbbf17fd89bb0f957bd7bcb13b186265e65fa7e550acd4331f1db512`.
- Independent hostile review B accepted the theorem package with no critical
  or major finding and two local minors.
- Round 2 replaced the mildly circular recurrence sentence by direct orbit
  logic and refreshed package provenance.
- Current `main.pdf` and `main_round2.pdf`: 5 A4 pages, 373,966 bytes,
  SHA-256
  `7ba3c97a6c7f6b2a32d8f7d303e66d7d6d41bc3f7d77ea70389309cfb42deccd`.
- Round-0 and round-1 artifacts retain their historical hashes.
- Current canonical verifier replay, isolated four-stage build, warning scan,
  embedded-font audit, and byte comparison all pass.
- Final internal review result: ACCEPT / `HOLD_EXTERNAL`.
