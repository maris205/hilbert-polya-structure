# Build and verification

From this package directory:

```sh
export SOURCE_DATE_EPOCH=1787616000
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

This sequence contains exactly **three total `pdflatex` runs**: one before
BibTeX and two after BibTeX.  “Two after BibTeX” is authoritative; it must not
be expanded to three post-BibTeX runs.

In a from-empty scratch build, TeX may conservatively request a label rerun
after the third run even when both the AUX file and canonical PDF are already
stable.  One additional no-op diagnostic pass may be used to confirm a clean
log; it is not part of the authoritative build sequence and must not be
reported as three post-BibTeX runs.

Run the deterministic companion control with:

```sh
python3 code/verify_complete_bipartite.py
```

It must terminate with `ALL CHECKS PASS`. The finite enumerations are regression evidence only; the manuscript proves all infinite-system statements directly.

## Expected artifact

- PDF: `main.pdf`
- format: anonymous A4 `amsart`
- required warnings: zero undefined references/citations and zero overfull boxes
- code dependency: Python 3 standard library only

## Release status

The supplemental cross-agent review track is separately preserved with its
scores.  The official, unscored `gpt-5.4 xhigh` track completed two rounds and
returned mathematics **PASS** with no official-round source change.  The clean
build and synchronized package integrity checks pass.

This is an anonymous internal Stage-2 draft. Strict ARS 0.1.27 Stage 2.5
integrity closure is complete with notes. External release remains **HOLD**
pending the specialist exact-neighbor/source gate, unresolved human
declarations, and explicit release authorization; no priority clearance is
claimed.

## Stage 2.5 corrected artifact

Correction round 1 repaired the exact author-hosted lecture title and did not
change any theorem or proof. The current canonical `main.pdf` is 7 A4 pages,
348,079 bytes, SHA-256
`9527da716429ba4644271086dee8eebdd5a1c201a73cb2a0a39046cc957de61a`.
The official-review PDFs remain historical pre-Stage-2.5 snapshots. A clean
build reproduces the corrected PDF byte-for-byte; see
`stage2_5/CORRECTION_ROUND_1.md`. External release remains **HOLD**.

The strict closure receipt is
`stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`; it binds 23/23 exact Phase-E
tuple rows and the active batch passport at
`docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`.
