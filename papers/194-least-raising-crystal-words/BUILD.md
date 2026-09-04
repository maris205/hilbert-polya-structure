# P194 Round-0 build record

**State:** `ROUND0_AUTHOR_FREEZE`  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## Paper-local exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
result: PASS
complete word grid: 1 <= k <= 4, 1 <= n <= 7
source transitions: 25,384
labelled targets: 25,384
exact assertions: 618,419
transition SHA-256: 15eae7619f324f7730af7dddb103820cb72434ebf897ee8ec4fde1c611e8df49
two fresh verifier processes: byte-identical
canonical stdout SHA-256: 969d07b598949b7ad14e8e032d7b294f320b09e0bbc05e656efb72282f7673ec
```

The verifier imports no scouting or prior-paper implementation.  It checks:

- literal signatures, raising/lowering positions, and least-colour updates;
- ballot/highest equivalence and complete orbit termination;
- reverse-RSK shape invariance and the exact pointwise clock;
- the sharp maximum and unique deepest state in every word box;
- complete actual versus predicted source sets for every labelled target;
- crystal components, unique highest vertices, and `f^lambda` multiplicities;
- independent SSYT depth histograms versus the principal-specialization
  product;
- hook length by an independent corner-removal recurrence;
- bounded-height involution shape counts through `S_8`;
- direct staircase maximum-fibre witnesses through `k=9`.

Finite enumeration is author-side falsification pressure, not proof,
experiment, process-separated review, novelty evidence, or ownership
clearance.

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
pages: 4
bytes: 370,448
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207
repeat deterministic pass: byte-identical
isolated source-only cold build: byte-identical
font rows embedded/subsetted/Unicode: 27/27/27
encrypted: no
forms: none
JavaScript: no
metadata stream: no
title/author/subject/keywords/creator/producer: blank
undefined references/citations: 0/0
warnings and bad boxes: 0
```

All four pages were rasterized at 150 dpi and inspected.  No clipping,
overlap, missing glyph, malformed display, broken bibliography, or unintended
blank page was observed.  Extracted text contains no unresolved marker or
identifying author information.

## Frozen Round-0 source hashes

```text
c0e4c3291fc5d3f5de1df64094c89bc7325b2372a279f09a430f39697957bfcf  main.tex
b4649d9e22a34a005706625be2472204b1275a722a085dfd19a0b04abd471a54  references.bib
ba0945a66d47ce074ba5cff9838777edebc640fe7fffa828eee6013bf9ee054c  code/verify.py
969d07b598949b7ad14e8e032d7b294f320b09e0bbc05e656efb72282f7673ec  code/CANONICAL.txt
```

The four-page Round-0 PDF is preserved byte-for-byte as both
`main_round0_original.pdf` and the accepted no-change `main_round1.pdf`, with
SHA-256
`9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207`.

## Review-B source-repair build

The current manuscript adds and subtracts Defant--Williams crystal pop-stack
sorting without changing any theorem or author verifier. A fresh source-only
four-pass build gives:

```text
status: PASS
pages: 5
bytes: 372,121
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b
font rows embedded/subsetted/Unicode: 27/27/27
warnings, bad boxes, unresolved references/citations: 0
encrypted: no
JavaScript: no
```

Current manuscript inputs are:

```text
d4c81d389dba055a3a232077e79058c09cae1be40b8822d49f976c4242d97ce9  main.tex
b8ab897d271bd4225dc71c4619fb5cbe6843afdc3d6a529705a927d37ce38faa  references.bib
203ae4ce3c750b5d45380db94f4096b99fcd776e035c2f880faef826f9e2323f  SOURCE_VERIFICATION.md
```

The current PDF is intentionally not byte-identical to either frozen
four-page snapshot. The accepted repair and its final pins are recorded by
the process-separated review packages; the owner gate remains
`OWNER_AMBER/HOLD_EXTERNAL`.
