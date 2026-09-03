# P167 Round-0 build and verification ledger

**Artifact:** `papers/167-minimum-inverse-position-feedback`  
**Status:** `ROUND2 DUAL-REVIEW FREEZE / HOLD_EXTERNAL`  
**Build date:** 2026-09-03 UTC

## Author verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p167.py
decision: AUTHOR_ROUND0_PASS
external status: HOLD_EXTERNAL_OWNER_THIN
assertions: 12,603,676
verifier SHA-256: b7c10bd3738362397a97361ca3780c4f53c7297efbe3e1885175634b345b457b
stdout SHA-256: 1e7348f9eab389cffc14582b3cf26ebeec69cb72a6c77dbdb1fb204abd1e1a8c
stdout bytes: 9,831
fresh process replays: 2/2
byte-identical replay/output match: yes
```

The verifier is a single standard-library file and imports no scouting or
paper module.  It reconstructs the literal identity-default map, checks all
states and targets through `n=7`, and separately checks the local
component/clock and generating-function claims beyond that range.

## Canonical build

Toolchain: pdfTeX `3.141592653-2.6-1.40.22` and BibTeX `0.99d`.
`latexmk` is not installed in this environment, so the equivalent explicit
settling sequence was used:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained canonical logs are `build_pdflatex_1.log`,
`build_bibtex.log`, `build_pdflatex_2.log`, and
`build_pdflatex_3.log`.  The settled LaTeX log and BibTeX log contain zero
warnings, bad boxes, unresolved references/citations, rerun requests,
duplicate destinations, or fatal errors.

Two further builds were performed in distinct fresh directories that began
with only `main.tex` and `references.bib`.  Their settled logs are
`build_cold1_settled.log` and `build_cold2_settled.log`; their BibTeX logs
are retained separately.  Both cold PDFs match the canonical PDF byte for
byte, and both settled log pairs have zero flagged diagnostics.

## Round-0 PDF freeze

```text
canonical PDF: main.pdf
frozen copy: main_round0_original.pdf
round-copy byte match: yes
cold-build byte matches: 2/2
pages: 4
bytes: 285,798
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379
font rows: 21
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
```

All four pages were rendered at 144 dpi and visually inspected.  Equations,
the main theorem table, proof endings, citations, references, page numbers,
and the visible lifecycle line are legible and inside the A4 page box.
Title, author, subject, keywords, creator, and producer metadata fields are
blank; the visible byline and running heads are anonymous.

## Historical Round-0 core hashes

The `main.pdf` row below records that pathname at the instant of the author
freeze; those exact bytes now persist as `main_round0_original.pdf`.  It is
not a hash claim about the repaired live `main.pdf`.

```text
01d2bded0a4457e95f677543227a213dc07057d8e1b8273786e5f7aa3f8606e4  main.tex
4286e4273768a76d295904a91caa1384cfcb11c6fc9157afe9fe8ddd3140a2b6  references.bib
b7c10bd3738362397a97361ca3780c4f53c7297efbe3e1885175634b345b457b  verify_p167.py
1e7348f9eab389cffc14582b3cf26ebeec69cb72a6c77dbdb1fb204abd1e1a8c  verification_output.txt
81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379  main.pdf
81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379  main_round0_original.pdf
```

## Round boundary

This directory is an author-side Round-0 freeze.  It contains no review and
makes no external-release decision.  Its owner status remains
`GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## Round-1 repaired source

Hostile Review A returned `0 Critical / 0 Major / 1 Minor`.  Its sole
finding corrected the Springer publication year of the
Flajolet--Odlyzko chapter from 1989 to 1990; *EUROCRYPT '89* remains the
proceedings title.  The theorem package and exact verifier were unchanged.
The live manuscript also uses a round-independent internal lifecycle label.

The immutable author artifact remains `main_round0_original.pdf`.  The live
`main.pdf` is the repaired source build and is the input to Review B.  Final
cold-build hashes and the paper-local checksum manifest are intentionally
deferred until both hostile reviews close.

## Round-2 dual-review closeout

Hostile Review B independently returned `PROVABLE AS STATED` with
`0 Critical / 0 Major / 1 Minor`.  Its only finding concerned stale
Round-0 artifact pointers, not the manuscript.  The packaging repair is now
closed with the following immutable distinction:

```text
author Round 0: main_round0_original.pdf
post-Review-A:  main_round1.pdf
post-Review-B:  main_round2.pdf
live canonical: main.pdf
```

The last three names are byte-identical repaired builds:

```text
pages: 4
bytes: 285,799
SHA-256: b32b14735d21a4354b7dfc242a98bb7a137d6ae1f5552fe0a4ea623500ad53b9
```

The preserved Round-0 artifact remains 285,798 bytes with SHA-256
`81bfa2ed4944f2750558f06cbb3a09d7081fc0361a0361f05f91869368faf379`.
Review B performed two further source-only cold builds; both matched the live
canonical PDF byte for byte, and both settled log pairs contained zero
flagged diagnostics.  The repaired manuscript retains four A4 pages, 21
embedded/subsetted/Unicode-mapped font rows, blank identifying metadata, no
encryption/forms/JavaScript, and a clean four-page visual render.

The final paper-local `SHA256SUMS` is generated after this closeout and
includes both hostile reviews and every immutable round artifact.  Final
status is `ROUND2 DUAL-REVIEW FREEZE / HOLD_EXTERNAL`.
