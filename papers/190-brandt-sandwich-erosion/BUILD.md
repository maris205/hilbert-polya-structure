# P190 build and immutable receipts

**State:** `ROUND1_REVIEW_A_REPAIR_BUILT`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## Paper-local exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p190.py
result: PASS
parameter boxes: 26
exact assertions: 1,555,420
canonical lines/bytes: 32 / 4,693
canonical SHA-256: 9652d76deed795b561f9ceddd28ff4db1f296215f920d97ad4014b3ca75e6b2f
two fresh processes: byte-identical
```

The verifier imports no scouting or prior-paper code.  It enumerates the
literal Brandt update, rebuilds every target fibre by cyclic source-letter
paths, checks dense matrix products in small boxes, and attacks the claimed
integer eigenspaces.  Enumeration is falsification pressure, not proof,
experiment, independent review, or ownership evidence.

## Deterministic LaTeX build

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final settled PDF remained byte-identical under an additional LaTeX
replay with the same environment.  Frozen receipt:

```text
pages: 4
bytes: 383,744
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66
Round-0 copy byte-identical: yes
font rows embedded/subsetted/Unicode: 29/29/29
encrypted: no
forms: none
JavaScript: no
metadata stream: no
title/author/subject/keywords/creator/producer: blank
```

The settled log contains zero warnings, bad boxes, unresolved references or
citations, rerun requests, and fatal errors.  All four rendered pages were
inspected at full-page scale: no clipping, overlap, corruption, or unintended
blank page was found.

## Frozen Round-0 core hashes

```text
84d4c4f736e6a7088f99356b4737585c1047284ee76781b3f69f799b9be613fd  main.tex
3bca1bf9c1f5bff1717e0c84a8263cf71d0763902389f9f647d436bf860a4dc9  references.bib
99bccb56fd9324409f7ee23742dbceda04c76cb887cac7bd8553a1ee84b4f081  code/verify_p190.py
9652d76deed795b561f9ceddd28ff4db1f296215f920d97ad4014b3ca75e6b2f  code/CANONICAL.txt
5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66  main_round0_original.pdf
```

## Round-1 Review-A repair build

Review A requested two one-token presentation repairs: delete the empty
leading subscript field in Eq. (11), and allow `amsart` to supply the single
full stop after the CRediT heading. The deterministic command sequence above
was rerun without changing the bibliography or author control.

```text
main.tex SHA-256: 73cb3d23aa88247ecbc22a75651f48f94aaf94113ccb649b1f13d64f9c37d300
main_round1.pdf SHA-256: 81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d
pages / bytes: 4 / 383,748
author canonical replay: PASS
settled diagnostics: 0
font rows embedded/subsetted/Unicode: 29/29/29
```

`main_round0_original.pdf` remains byte-immutable at its recorded Round-0
hash. Review-A delta acceptance and Review B remain separate gates;
`HOLD_EXTERNAL` remains active.
