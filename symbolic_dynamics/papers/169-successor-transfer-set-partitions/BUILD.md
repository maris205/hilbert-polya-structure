# P169 Round-0 build and verification ledger

**Artifact:** `papers/169-successor-transfer-set-partitions`  
**Status:** `ROUND2 DUAL-REVIEW FREEZE / HOLD_EXTERNAL`  
**Build date:** 2026-09-03 UTC

## Author verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p169.py
decision: AUTHOR_ROUND0_PASS
external status: HOLD_EXTERNAL_OWNER_THIN
assertions: 1,217,025
verifier SHA-256: e4566e997ec656f3eaa41fa4f23953773222293cf23189ebd6c7d9a64aab950b
stdout SHA-256: e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f
stdout bytes: 1,785
fresh process replays: 2/2
byte-identical replay/output match: yes
```

The verifier is one standard-library file and imports no scouting or paper
module.  It exhausts every set partition through `n=10`, compares the trace
formula with literal predecessor counts for every target through `n=9`,
checks 532,467 queue-cone cases, and follows every sharp witness stratum
through `n=50`.

## Canonical build

Toolchain: pdfTeX `3.141592653-2.6-1.40.22` and BibTeX `0.99d` from TeX Live
2022/Debian.  `latexmk` is absent in this environment, so its explicit
settling sequence was used:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained canonical logs are `build_pdflatex_1.log`,
`build_bibtex.log`, `build_pdflatex_2.log`, and
`build_pdflatex_3.log`.  The final LaTeX and BibTeX logs contain zero
warnings, bad boxes, unresolved references/citations, rerun requests,
duplicate destinations, or fatal errors.

Two further builds ran in distinct fresh directories that initially contained
only `main.tex` and `references.bib`.  Their settled logs are
`build_cold1_settled.log` and `build_cold2_settled.log`; their BibTeX logs are
retained separately.  Both cold PDFs match the canonical PDF byte for byte,
and both settled log pairs have zero flagged diagnostics.

## Round-0 PDF freeze

```text
canonical PDF: main.pdf
frozen copy: main_round0_original.pdf
round-copy byte match: yes
cold-build byte matches: 2/2
pages: 5
bytes: 392,917
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2
font rows: 28
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
```

All five pages were rendered at 144 dpi and visually inspected.  The theorem
continuation, max-plus formulas, sharp word trajectories, two state tables,
boxed entry rule, four numerical matrices, predecessor lists, bibliography,
page numbers, and lifecycle line are legible and inside the A4 page box.
Title, author, subject, keywords, creator, and producer metadata fields are
blank; visible bylines and running heads are anonymous.

## Historical Round-0 core hashes

The `main.pdf` row below records that pathname at the instant of the author
freeze; those exact bytes now persist as `main_round0_original.pdf`.  It is
not a hash claim about the repaired live `main.pdf`.

```text
676675f260f1ad756b8a658ea07ab6390698a8be05d10e63fc9150f1cfb2c512  main.tex
0a20bea8b28b93815c08b689b8fe2ab13957bc316bbd5ba7588c61ea951cf195  references.bib
e4566e997ec656f3eaa41fa4f23953773222293cf23189ebd6c7d9a64aab950b  verify_p169.py
e59891873e682c0a271a28197e681f6ba813f394f4104140b02d5eb4e5ce258f  verification_output.txt
df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2  main.pdf
df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2  main_round0_original.pdf
```

## Round boundary

This directory is an author-side Round-0 freeze.  It contains no review and
makes no release decision.  The owner status remains
`GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## Round-1 repaired source

Hostile Review A returned `0 Critical / 0 Major / 1 Minor`.  Its sole
finding replaced the valid arXiv-only Ji--Li--Wang record by the 2025 formal
publication in *Annals of Combinatorics*, volume 29, issue 4, pages
1155--1175, DOI `10.1007/s00026-025-00760-3`.  The arXiv identifier remains
as auxiliary metadata.  The citation key was renamed to `JiLiWang2025`, and
the live manuscript now uses a round-independent internal lifecycle phrase.

No theorem, proof, formula, example, verifier, claim ceiling, owner
subtraction, or external lifecycle decision changed.  The immutable author
artifact remains `main_round0_original.pdf`; the repaired live source and
PDF are the input to Hostile Review B.  Its cold-build hashes and final
paper-local checksum manifest are recorded only after that review closes.

## Round-2 dual-review closeout

Hostile Review B returned `PROVABLE AS STATED` with
`0 Critical / 0 Major / 1 Minor`.  Its only finding concerned stale
Round-0 artifact pointers.  The final distinction is

```text
author Round 0: main_round0_original.pdf
post-Review-A:  main_round1.pdf
post-Review-B:  main_round2.pdf
live canonical: main.pdf
```

The last three names are byte-identical repaired builds:

```text
pages: 5
bytes: 392,380
SHA-256: 419e91685b4a663fb8ab711abca28517436a2477a92184add424575d8bac77d3
```

The preserved Round-0 artifact remains 392,917 bytes with SHA-256
`df03b864b47ae963c467831ba7f5b47231663f1e369facf21eee1d468b17c9c2`.
Review B performed two additional source-only cold builds; both matched the
live PDF byte for byte.  All settled logs have zero flagged diagnostics, all
28 font rows are embedded/subsetted/Unicode mapped, identifying metadata is
blank, and all five rendered pages pass visual inspection.

The final paper-local `SHA256SUMS` includes both hostile reviews and every
immutable round artifact.  Final status is
`ROUND2 DUAL-REVIEW FREEZE / HOLD_EXTERNAL`.
