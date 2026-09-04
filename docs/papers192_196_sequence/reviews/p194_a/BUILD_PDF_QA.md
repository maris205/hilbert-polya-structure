# P194 Review-A build and PDF QA

## Frozen and current input integrity

From the workspace root:

```text
sha256sum -c docs/papers192_196_sequence/reviews/p194_a/PINNED_INPUTS.sha256
result: all 23 current/preserved inputs OK
paths containing "..": 0
main_round0_original.pdf versus main_round1.pdf: byte-identical
current main.pdf versus either four-page snapshot: intentionally different
```

The pin set contains the batch protocol, central contract/gate documents,
current author inputs, and both preserved snapshots.  It does not pin
Reviewer-A outputs to themselves.

## Independent reviewer replay after the repair

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a_p194.py | cmp - CANONICAL.txt
replay 1 exit: 0
replay 2 exit: 0
canonical/stdout SHA-256: 4e579cb9e2552fe5703e9d0e2ad5f462e8b822c0751a2531d024f901abeb1881
reviewer-code SHA-256: 0f5a94796da5e39fda40de72a60659126380d23055080b47b513cd38816bc763
boxes: 30 (`k=1..5`, `n=1..6`)
states/transitions/targets: 26,214 / 26,214 / 26,214
assertions: 1,202,599
control digest: 75f58e8352bf97f6d02178cc37cc2cf194a2ac7ee84a9f1b00a33b313e12cb43
```

The reviewer program uses only the Python standard library.  It imports no
paper file and does not execute author code.

## Unchanged author-control replay

The author control was treated as a pinned black box and run only after the
reviewer program passed:

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
replay 1 exit: 0
replay 2 exit: 0
author canonical SHA-256: 969d07b598949b7ad14e8e032d7b294f320b09e0bbc05e656efb72282f7673ec
author verifier SHA-256: ba0945a66d47ce074ba5cff9838777edebc640fe7fffa828eee6013bf9ee054c
```

These hashes are identical to the original Review-A pins.  The source repair
therefore changed no executable evidence.

## Original Round-0 source-only cold builds

During the original Review A, the then-frozen `main.tex` and `references.bib`
were copied into two fresh temporary directories.  Both used

```text
SOURCE_DATE_EPOCH=1704067200
TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Environment:

```text
architecture: x86_64
pdfTeX: 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX: 0.99d (TeX Live 2022/dev/Debian)
Poppler pdfinfo/pdffonts/pdftoppm: 22.02.0
Python: 3.12.3
```

Both cold PDFs were byte-identical to each other, the then-current `main.pdf`,
and `main_round0_original.pdf`.  The preserved Round-0 and Round-1 PDFs remain
byte-identical:

```text
pages: 4
page size: A4, 595.276 x 841.89 pt
bytes: 370,448
PDF version: 1.5
SHA-256: 9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207
extracted-text SHA-256: 708ac04b54545100ccd747236312c5182d9f3854024e7071581a4022d7d3c9d0
LaTeX/BibTeX warning, bad-box, unresolved, or fatal matches: 0
font rows embedded/subsetted/Unicode: 27/27/27
encrypted: no
forms: none
embedded files: 0
JavaScript: no
metadata stream: no
title/author/subject/keywords/creator/producer: blank
```

The corresponding Round-0 source hashes were
`c0e4c3291fc5d3f5de1df64094c89bc7325b2372a279f09a430f39697957bfcf`
for `main.tex` and
`b4649d9e22a34a005706625be2472204b1275a722a085dfd19a0b04abd471a54`
for `references.bib`.

## Post-B source-repair cold builds

For this nonregression check, only the current `main.tex` and
`references.bib` were copied into each of two new temporary directories.  The
same deterministic environment and LaTeX/BibTeX sequence were used.  Both
builds completed and are byte-identical to each other and the live
`main.pdf`:

```text
pages: 5
page size: A4, 595.276 x 841.89 pt
bytes: 372,121
PDF version: 1.5
SHA-256: 682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b
extracted-text SHA-256: 8791969b9746b9e68cc6cd1187c0fcbcdcfed9586ac5e29f3b6e4069159bac7b
final LaTeX/BibTeX warning, bad-box, unresolved, or fatal matches: 0
citation keys / bibliography items: 6 / 6
font rows embedded/subsetted/Unicode: 27/27/27
encrypted: no
forms: none
embedded files: 0
JavaScript: no
metadata stream: no
title/author/subject/keywords/creator/producer: blank
```

The current manuscript and bibliography hashes are
`d4c81d389dba055a3a232077e79058c09cae1be40b8822d49f976c4242d97ce9`
and
`b8ab897d271bd4225dc71c4619fb5cbe6843afdc3d6a529705a927d37ce38faa`.
The current PDF is intentionally not byte-identical to the preserved
four-page PDFs: the added source and bibliography entry produce the fifth
page.

## Visual inspection

All four pages from the first cold build were rasterized at 160 dpi and
inspected individually.  The long title, abstract, signature definition,
sample orbit, reverse-RSK display, clock, multiline Schur product, `q=1`
formula, involution EGF, full inverse-set display, staircase formula, finite
control statement, limitations, and all five bibliography entries are
legible and remain inside the page box.  No clipping, overlap, missing glyph,
malformed display, stranded heading, unintended blank page, or identifying
metadata was found.

All five pages of the current first cold build were also rasterized at 160 dpi
and inspected.  The new comparison paragraph is legible on page 1; all
theorems, displays, proofs, the finite-control declaration, and the six-entry
bibliography remain within the page box.  Page 5 contains the final two
bibliography entries and is not blank.  No clipping, overlap, missing glyph,
malformed display, stranded heading, or unintended blank page was observed.

Build/PDF decision: `PASS` for both the preserved Round-0/Round-1 snapshots
and the current post-B source repair.  Reviewer A modified no paper source.
