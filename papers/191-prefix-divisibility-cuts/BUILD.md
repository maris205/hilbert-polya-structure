# P191 build and immutable receipts

**State:** `ROUND1_REVIEW_A_ACCEPTED_NO_CHANGE`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## Paper-local exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
result: PASS
complete range: N=1,...,18
source transitions: 262,143
exact assertions: 3,408,240
canonical lines/bytes: 24 / 1,439
canonical SHA-256: c4643a6639ddf269dee59c97acc53aee504d081a0279d0bbe2898183f674373c
two fresh processes: byte-identical
```

The verifier imports no scouting or prior-paper code.  It enumerates the
literal composition map and complete functional graph, checks every claimed
boundary and witness time, and reconstructs every labelled target fibre in
two ways.  The global no-skip recurrence and the interval product are each
compared pointwise with literal indegree before image and mass totals are
checked.  Enumeration is author-side falsification pressure, not proof,
experiment, process-separated review, or ownership evidence.

## Deterministic LaTeX build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled log and BibTeX transcript contain zero warnings, bad boxes,
unresolved references or citations, rerun requests, and fatal errors.  Frozen
receipt:

```text
pages: 4
bytes: 380,787
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b
Round-0 copy byte-identical: yes
font rows embedded/subsetted/Unicode: 28/28/28
encrypted: no
forms: none
JavaScript: no
metadata stream: no
title/author/subject/keywords/creator/producer: blank
```

All four pages were rasterized at 220 dpi (`1819 x 2573` pixels) and inspected
at original resolution.  No clipping, overlap, malformed formula or table,
unintended blank or truncated page, broken citation, bibliography defect, or
header/footer/page-number issue was found.

## Frozen Round-0 core hashes

```text
bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84  main.tex
1141067122be2dc4613007009d732fdcfc1dd35edf0c85d19ced38ef47acad0c  references.bib
70efeb7bdb522b501d64775d3ad1c300d70d9ffc83d94d65ff7924e633c59d50  code/verify.py
c4643a6639ddf269dee59c97acc53aee504d081a0279d0bbe2898183f674373c  code/CANONICAL.txt
d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b  main_round0_original.pdf
```

## Round-1 no-change receipt

Hostile Review A reconstructed the carrier as cut-mask bitsets, recovered
recurrence/depth by indegree peeling and reverse BFS, and checked both global
and interval inverse counts target by target. Its 920,748 exact assertions
returned `Critical 0 / Major 0 / Minor 0` and `ACCEPTED_NO_CHANGE`.

`main_round1.pdf` is therefore intentionally byte-identical to Round 0 at
SHA-256
`d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`.
Review B and terminal QA remain required; `HOLD_EXTERNAL` remains active.
