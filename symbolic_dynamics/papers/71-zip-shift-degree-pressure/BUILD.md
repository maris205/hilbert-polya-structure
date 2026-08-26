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

Run the deterministic companion control with:

```sh
python3 code/verify_degree_pressure.py
```

It must terminate with `ALL CHECKS PASS`. All computations are regression evidence only; the pressure, profile-recovery, periodic, and multifractal statements are proved in the manuscript.

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
pending a specialist audit of current zip-shift thermodynamic work, unresolved
human declarations, and explicit release authorization; no priority clearance
is claimed.

## Stage 2.5 corrected artifact

Correction round 1 repaired the article number, added the located
S-expansiveness preprint, and disclosed the public active thermodynamic-
formalism project strictly as a research objective rather than theorem text.
No theorem or proof was changed. The current canonical `main.pdf` is 9 A4
pages, 409,426 bytes, SHA-256
`971b33083dc14ceb99831f94786167c1186bf9b8365557472fb2a9f493174a9e`.
The official-review PDFs remain historical pre-Stage-2.5 snapshots; see
`stage2_5/CORRECTION_ROUND_1.md`. External release remains **HOLD**.

The strict closure receipt is
`stage2_5/POST_CORRECTION_INTEGRITY_DISPOSITION.md`; it binds 31/31 exact Phase-E
tuple rows and the active batch passport at
`docs/papers67_71_sequence/stage2_5/MATERIAL_PASSPORT.yaml`.
