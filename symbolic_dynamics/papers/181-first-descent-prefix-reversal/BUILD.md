# P181 build and verification ledger

**Round:** Round 2, dual hostile review accepted with zero open findings  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## Paper-local exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p181.py
result: PASS
exact assertions: 6,273,070
complete groups: S_1,...,S_9
largest box: 362,880 states and 181,440 image targets
objects checked: literal update, full image, full incoming sets, orbit tails,
                 periods, two-cycle pairs, depth-two bijection, maximizers
canonical replay: byte-identical
transcript lines/bytes: 19 / 989
transcript SHA-256: 31cfd5449454e6c682ebb105059329ddd53825df7ea047dfe1d61e7b91d1f24c
```

The verifier imports no scouting, manuscript, or prior-paper code.  It
rebuilds the exact inverse table rather than copying the breadth pilot's
summary.  Finite enumeration is falsification pressure, not proof or owner
evidence.

## Build method and preserved Round 0

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final LaTeX and BibTeX logs contain zero warnings, bad boxes, unresolved
references/citations, rerun requests, and fatal errors.

```text
pages: 3
bytes: 345,262
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 1df6b41b097c29cc933123906fa1539a37c0944bd843d007204c07b2dc824ad0
round0 copy byte-identical: yes
deterministic settled replay byte-identical: yes
font rows: 28
embedded/subsetted/Unicode rows: 28/28/28
encrypted: no
forms: none
JavaScript: no
metadata title/author/subject/keywords/creator/producer: blank
```

All three pages were rendered at 120 dpi and visually inspected.  The
continued theorem, inverse formula, depth-two bijection, small atlases,
footnote URLs, bibliography, running heads, and page numbers are legible and
remain inside the page box.

## Frozen Round-0 core hashes

```text
090a010f27688156432c863f1b30e2ccf2a44d8ab111a51771ac7b525713439d  main.tex
34511e9149dd34c6b107da0bf2902d09163f4e55a7141a25003e26de51384ba8  references.bib
487845aa9b404e05dbc381c23c3f02173bb17da0240ba9901aeb1f9181abe42d  verify_p181.py
4a849f6a230efe22d4c4357b792f9538d5ee86d33a8abfc44e2313413ee0dbb2  verification_output.txt
1df6b41b097c29cc933123906fa1539a37c0944bd843d007204c07b2dc824ad0  main_round0_original.pdf
```

## Round-1 boundary repair

Review A requested closure of the meaningful `S_1` boundary.  The manuscript
now gives the unique fixed arrow, image/core, depth, and fibre, while the
author control checks eight explicit `S_1` properties.  The settled receipt
is:

```text
pages: 3
bytes: 345,290
main.tex SHA-256: 95909031cae2c75f09399452a472597e72a1bf3a91d10cf4286df54e54e2fb82
verifier SHA-256: a9ceeb2a3cab7a8df112e33e28ddbc3b1de1d25d03153d2d6a41bf23c0adb16f
transcript SHA-256: 31cfd5449454e6c682ebb105059329ddd53825df7ea047dfe1d61e7b91d1f24c
Round-1 PDF SHA-256: 57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861
main.pdf equals main_round1.pdf: yes
font rows embedded/subsetted/Unicode: 28/28/28
metadata identifying fields: blank
```

The author verifier replays byte-identically with 6,273,070 assertions.

## Round-2 dual-review and final artifact gate

No theorem source or paper-local verifier changed after the accepted Round-1
boundary repair.  Round 2 closes both process-separated hostile reviews:

```text
Review A assertions: 17,364,060
Review A open findings: 0 Critical / 0 Major / 0 Minor
Review B assertions: 377,591
Review B open findings: 0
Round-2 PDF SHA-256: 57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861
main.pdf equals main_round1.pdf: yes
main.pdf equals main_round2.pdf: yes
```

Two source-only cold builds reproduce the live PDF byte for byte:

```text
qa_final/cold_build_1/main.pdf: 57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861
qa_final/cold_build_2/main.pdf: 57f62423e760c5a7f4f3add7bd94a559d99468acea3b05082afa5b28e1d24861
pages/bytes: 3 / 345,290
font rows embedded/subsetted/Unicode: 28/28/28
bibliography entries: 3
```

The final three-page raster was visually inspected and the anonymity and
metadata checks remain clean.  Both reviewers preserve
`OWNER_AMBER / HOLD_EXTERNAL`; their acceptance is theorem-level internal
closure, not owner clearance or external-release authorization.
