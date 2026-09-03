# P170 build and verification ledger

**Artifact:** `papers/170-random-permutation-fixed-point-sieve`  
**Status:** `ROUND2 DUAL-REVIEW FREEZE / HOLD_EXTERNAL`  
**Build date:** 2026-09-03 UTC

## Independent author verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p170.py
decision: AUTHOR_ROUND0_PASS
external status: HOLD_EXTERNAL_OWNER_THIN
assertions: 481,935
payload SHA-256: e8f7f38c9e8bf14c2a35aba8b3eb9280127ec71374253056927290a65a5cdb8e
verifier SHA-256: 2a9b9167d0ba8cf36dcf76cd93e6f58f5c2bb0002f21bd2a8c6d25d13427aed8
stdout SHA-256: 985941e0a8b363fcf954d503cf825867e54548dd8fcf416ee105a4cbbac2ba13
stdout bytes: 501
fresh process replays: 2/2
byte-identical replay/output match: yes
```

The program is one standard-library file and imports no scouting, hostile
gate, manuscript, or earlier-paper module.  It regenerates permutations and
subset histories literally.  Its assertion counts by axis are frozen in
`verification_output.txt`.

## Canonical build

Toolchain: pdfTeX `3.141592653-2.6-1.40.22` and BibTeX `0.99d` from TeX Live
2022/Debian.  The explicit settling sequence was

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained canonical logs are `build_pdflatex_1.log`,
`build_bibtex.log`, `build_pdflatex_2.log`, and
`build_pdflatex_3.log`.  The final LaTeX and BibTeX logs have zero actual
warnings, bad boxes, unresolved references/citations, rerun requests,
duplicate destinations, or errors.  The sole raw grep match is the filename
`rerunfilecheck.sty`, not a diagnostic.

Two further builds ran in distinct fresh directories initially containing
only `main.tex` and `references.bib`.  Their settled logs and BibTeX logs are
retained as `build_cold{1,2}_settled.log` and
`build_cold{1,2}_bibtex.log`.  Both cold PDFs equal the canonical PDF byte for
byte; their settled logs have the same zero-diagnostic status.

## Round-0 PDF freeze

```text
canonical PDF: main.pdf
immutable author copy: main_round0_original.pdf
round-copy byte match: yes
cold-build byte matches: 2/2
pages: 4
bytes: 277,277
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034
font rows: 23
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
```

All four pages were rendered at 144 dpi and visually inspected.  The theorem
continuation across pages 1--2, conditional-mean fraction, support/deficit
display, bibliography, running heads, and page numbers are legible and
inside the A4 page box.  Title, author, subject, keywords, creator, and
producer metadata fields are blank.  The visible byline and running heads are
anonymous.

## Frozen core hashes

```text
5ca548eeecf686c16599bebe85b2e18c94f93ada2d577b6e8f5771b390711e74  main.tex
2ce60b1638579e340e5e77eb970603f29e050b207c4ede1649cf38ad475cd839  references.bib
2a9b9167d0ba8cf36dcf76cd93e6f58f5c2bb0002f21bd2a8c6d25d13427aed8  verify_p170.py
985941e0a8b363fcf954d503cf825867e54548dd8fcf416ee105a4cbbac2ba13  verification_output.txt
b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034  main.pdf
b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034  main_round0_original.pdf
```

## Round boundary

The sections above preserve the author-side Round-0 evidence.  Round 0 made
no external-release decision; external circulation remains `HOLD_EXTERNAL`.

## Round-1 and Round-2 no-change closeout

Hostile Review A and independent nonauthor Hostile Review B each returned
`ACCEPT_INTERNAL / PROVABLE AS STATED` with
`0 Critical / 0 Major / 0 Minor`.  Neither requested a source or artifact
repair.  The round distinction is provenance-only:

```text
author Round 0: main_round0_original.pdf
post-Review-A:  main_round1.pdf
post-Review-B:  main_round2.pdf
live canonical: main.pdf
```

All four paths are byte-identical, four-page PDFs of 277,277 bytes with
SHA-256
`b900ad563fe8e2ac8082b4c4acb1da670b7284ea0d5a95f2d64544e3922b2034`.
Review B replayed the 481,935-assertion author verifier and ran an independent
3,001,398-assertion `frozenset`/sparse-polynomial/derangement-recurrence
implementation.  Two further source-only builds, all-page visual inspection,
and font/metadata/anonymity/lifecycle checks passed.

The final paper-local `SHA256SUMS` is regenerated after both review reports
and all round artifacts are present.  Final status is
`ROUND2 DUAL-REVIEW FREEZE / GREEN_OWNER_THIN_WITH_N3_REPAIR /
HOLD_EXTERNAL`.
