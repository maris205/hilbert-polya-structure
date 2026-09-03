# P177 build and verification ledger

**Round:** Round 2 dual-review freeze  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## Paper-local author-side exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p177.py
result: PASS
exact assertions: 1,095,999
algebraic boxes: d=2,...,8; t=1,...,16 for both TV comparisons
full literal carriers: d=2,3,4 (8, 128, and 32,768 states)
literal ordered histories: t=0,...,5
exhaustive Boolean characters: d=2,3,4
canonical replay: byte-identical
transcript lines/bytes: 22 / 811
transcript SHA-256: 1ca091424ae0125bf443594b7bbf8c4b61a0fe61826635d7cd9d2e94c1eee501
```

The verifier imports no scouting, manuscript, or prior-paper code.  It is an
author-side regression control organized by theorem contracts rather than the
breadth-scout ledger; process-independent evidence is supplied only by the
hostile reviewers.  Its finite checks are falsifiers, not proofs or novelty
evidence.

## Build method

The deterministic settling sequence was

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The current LaTeX and BibTeX logs contain zero warnings, bad boxes, unresolved
references or citations, rerun requests, and fatal errors.

## Preserved Round 0

```text
pages: 4
bytes: 341,372
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 28f719fc52d8a06d61b0425df82f718b4592e736028b3137dc7a0212fe053fec
immutable file: main_round0_original.pdf
deterministic settled replay byte-identical: yes
font rows: 29
embedded/subsetted/Unicode rows: 29/29/29
encrypted: no
forms: none
JavaScript: no
metadata title/author/subject/keywords/creator/producer: blank
```

All four pages were rasterized at 120 dpi and visually inspected.  The
continued theorem, theorem table, displayed formulas, bibliography, running
heads, and page numbers are legible and remain inside the A4 page box.

## Round-1 repair build

Review A found that the endpoint-coordinate condition alone overstated
history existence at `t=0` and `t=1`.  The theorem and proof now require
positive history count and spell out the exact support; the verifier adds
explicit boundary sentinels.  The settled Round-1 receipt is:

```text
pages: 4
bytes: 342,318
PDF SHA-256: ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c
main.pdf equals main_round1.pdf: yes
main.tex SHA-256: fb4cf3eb309e97724a53e037aaf6888881a3f57de6f1e035dc350c7dd40dc06a
verifier SHA-256: fb404980298bd94ee60c343ab6700f7df0b57745ebb6ad8202c7a09c110bcc56
transcript SHA-256: 1ca091424ae0125bf443594b7bbf8c4b61a0fe61826635d7cd9d2e94c1eee501
font rows embedded/subsetted/Unicode: 29/29/29
metadata identifying fields: blank
```

The author verifier replays byte-identically.

## Immutable-round core hashes

```text
964015f77d7c749c228435241e628994bb955fda3b9fc4c5f2c8ac5c8bd8d016  references.bib
fb4cf3eb309e97724a53e037aaf6888881a3f57de6f1e035dc350c7dd40dc06a  main.tex
fb404980298bd94ee60c343ab6700f7df0b57745ebb6ad8202c7a09c110bcc56  verify_p177.py
1ca091424ae0125bf443594b7bbf8c4b61a0fe61826635d7cd9d2e94c1eee501  verification_output.txt
28f719fc52d8a06d61b0425df82f718b4592e736028b3137dc7a0212fe053fec  main_round0_original.pdf
ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c  main.pdf
ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c  main_round1.pdf
```

## Final Round 2

Reviewer A (algebra) closed at 36,510 exact assertions; Reviewer B (root,
tuple-vector/frozenset reconstruction) closed at 224,874.  Both have zero
open findings and passing review-local manifests.  Round 2 is a deliberate
no-source-change rebuild of the accepted Round-1 theorem:

```text
main.pdf/main_round1.pdf/main_round2.pdf:
ff93b3bf239536ad2256948c6c2877b27435d437f71f2df7f411771a0420516c
two source-only cold builds: byte-identical PASS
final visual pages inspected: 4/4 PASS
```

See `FINAL_QA.md` for the complete final gate.
