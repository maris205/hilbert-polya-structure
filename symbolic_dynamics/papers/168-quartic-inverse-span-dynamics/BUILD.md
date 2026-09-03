# P168 build and verification ledger

**Artifact:** `papers/168-quartic-inverse-span-dynamics`  
**Status:** `ROUND2 DUAL-REVIEW FREEZE / HOLD_EXTERNAL`  
**Build date:** 2026-09-03 UTC

## Author verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p168.py
decision: AUTHOR_ROUND0_PASS
external status: HOLD_EXTERNAL_OWNER_THIN
assertions: 32,754
verifier SHA-256: c3c40bfc0e92c19fe3a6fe6b7b924c7d0cb6f2a518f6478363701ae4bab1f6f1
stdout SHA-256: 8c0b77d99e976e9666ae658f4af7525ccf185f927948e660e3323a0f6f7f3d74
stdout bytes: 827
fresh process replays: 2/2
byte-identical replay/output match: yes
```

The verifier is a self-contained standard-library program.  It constructs
finite fields from irreducible quartics, enumerates every subspace in RREF,
computes the complete edge map, constructs the quadratic subfield
independently, and tests ranks, recurrence, cycles, depths, images, and every
target fibre at times one through four for `p=2,3,5`.

The frozen edge SHA-256 values are:

```text
p=2: 9cf33ab3287ac44734e8c9641b86378ab4501beb95ea85d6e57ae7e5e309b05f
p=3: 3f68d54205102badfd3b7f64bbbc257f96b5599c352b2099085c32386e3cb18d
p=5: 85d4058674bab2962f4c5dfe0f0f992a90088f46835516583b987d10bb9c0105
```

## Canonical build

Toolchain: pdfTeX `3.141592653-2.6-1.40.22` and BibTeX `0.99d`.
`latexmk` is not installed, so the equivalent explicit settling sequence was
used:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained canonical logs are `build_pdflatex_1.log`,
`build_bibtex.log`, `build_pdflatex_2.log`, and `build_pdflatex_3.log`.
The settled build contains no LaTeX/package warning, bad box, unresolved
reference/citation, rerun request, or fatal error.

Two additional builds ran in distinct fresh directories initially containing
only `main.tex` and `references.bib`.  Their settled logs are
`build_cold1_settled.log` and `build_cold2_settled.log`, with the corresponding
BibTeX logs retained.  Both cold PDFs match the canonical PDF byte for byte,
and both settled builds have zero flagged diagnostics.

## Round-0 PDF freeze

```text
canonical PDF: main.pdf
frozen copy: main_round0_original.pdf
round-copy byte match: yes
cold-build byte matches: 2/2
pages: 5
bytes: 322,829
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e
font rows: 23
unembedded/unsubsetted/non-Unicode font rows: 0
encrypted: no
forms: none
JavaScript: no
```

All five pages were rendered at 144 dpi and visually inspected.  The theorem
and both tables, displayed formulae, proof endings, citations, references,
page numbers, and lifecycle line are legible and contained in the A4 page
box.  Title, author, subject, keywords, creator, and producer metadata fields
are blank; the visible byline and running heads are anonymous.

## Frozen core hashes

```text
866951e658c3dd54c944e14c9d94b5690fa974e566d83bc35847663658571b8b  main.tex
aa6a1ec380d5a24114e4c1ce896afd668f2abaeb2fcf65ec14f36dc5849805e3  references.bib
c3c40bfc0e92c19fe3a6fe6b7b924c7d0cb6f2a518f6478363701ae4bab1f6f1  verify_p168.py
8c0b77d99e976e9666ae658f4af7525ccf185f927948e660e3323a0f6f7f3d74  verification_output.txt
846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e  main.pdf
846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e  main_round0_original.pdf
```

## Historical Round-0 boundary

At author freeze, this directory contained no manuscript review and made no
release decision.  That immutable source/PDF state remains preserved as
`main_round0_original.pdf`; its lifecycle was and remains
`GREEN_OWNER_THIN / HOLD_EXTERNAL`.

## Round-1 and Round-2 no-change closeout

Hostile Review A and independent nonauthor Hostile Review B each returned
`PROVABLE AS STATED` with `0 Critical / 0 Major / 0 Minor`.  Neither review
requested a source or artifact repair.  The round distinction is therefore
provenance-only:

```text
author Round 0: main_round0_original.pdf
post-Review-A:  main_round1.pdf
post-Review-B:  main_round2.pdf
live canonical: main.pdf
```

All four paths are byte-identical, five-page PDFs of 322,829 bytes with
SHA-256
`846dcfde4e16cacda57434939eb732c45383f7ed3f3b68540ee69aef4cca0b5e`.
Review B replayed the 32,754-check author verifier twice and ran two
independent reviewer implementations totalling 1,567,354 assertions.  It
also performed two additional source-only builds, full five-page visual and
bounding-box checks, and font/metadata/anonymity/lifecycle checks; all passed.

The author-side paragraphs above remain historical Round-0 evidence.  The
final paper-local `SHA256SUMS` is regenerated only after both reports and all
three immutable round PDFs are present.  Final status is
`ROUND2 DUAL-REVIEW FREEZE / GREEN_OWNER_THIN / HOLD_EXTERNAL`.
