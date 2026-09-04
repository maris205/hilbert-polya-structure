# P193 Round-0 build record

**State:** `ROUND0_AUTHOR_FREEZE`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## Paper-local exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
result: PASS
complete range: S_1,...,S_9
source transitions: 409,113
exact assertions: 7,985,745
transition SHA-256: 28eedb5ba198c502e491d2788354ab2fe6de9785af1852bc3b4dd00f69f33761
two fresh verifier processes: byte-identical
```

The digest is updated in lexicographic permutation order with the exact bytes
of `(n, source, target)` for every transition.  The verifier imports no
scouting or previous-paper code.  It checks:

- literal mutual nominations versus direct-sum block surgery;
- disjointness and strict component refinement;
- actual orbit tail versus the recursive pointwise height;
- sharp maximum and complete deepest-state count;
- the indecomposable-parent lemma;
- every coefficient of `A_t` and `B_t` in the complete range;
- every labelled target fibre and image membership;
- fibre mass and the unique maximum-fibre target.

Finite enumeration is author-side falsification pressure, not proof,
experiment, process-separated review, or ownership evidence.

## Deterministic LaTeX build

Run from the paper directory:

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Settled Round-0 result:

```text
status: PASS
pages: 5
bytes: 389,209
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: e41e171c8f412cf93aae9510052ed0d8ad165125be1bd4c04133f1b410048267
repeat deterministic pass: byte-identical
font rows embedded/subsetted/Unicode: 29/29/29
encrypted: no
forms: none
JavaScript: no
metadata stream: no
title/author/subject/keywords/creator/producer: blank
undefined references/citations: 0/0
warnings and bad boxes: 0
```

All five pages were rasterized at 160 dpi and inspected.  No clipping,
overlap, missing glyph, malformed display, broken table, unintended blank
page, or bibliography defect was observed.  Extracted text contains no
unresolved marker or author identity.

## Frozen source hashes

```text
3a217db814e618e445eaa7591daf4962432a36f5f9e5530b9d66a5b1947a9841  main.tex
a427a43b8adf6142661ff0763cb6af6b50a31af09b8657120763c8f5a89625c4  references.bib
111e4f51476eeb51d5cbe47f34f025f448ba91cec1a051f0348638a1b1bcc702  code/verify.py
```
