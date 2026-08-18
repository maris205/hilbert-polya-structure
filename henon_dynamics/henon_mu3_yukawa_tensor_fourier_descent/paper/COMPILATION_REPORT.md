# HCS-C61 paper compilation report

Status: **`PAPER_COMPILED / PAPER_HOSTILE_PASS`**.  This report is additive
paper provenance; it does not alter the frozen C61 machine/formal inputs.

## Build

- Engine: pdfTeX 1.40.22 (TeX Live 2022/dev/Debian).
- Command, run twice in the paper directory:
  `pdflatex -interaction=nonstopmode -halt-on-error main.tex`.
- Environment variables `LD_LIBRARY_PATH`, `BASH_ENV`, and `PYTHONPATH` were
  removed for the build.
- Exit status: zero on both passes.
- Output: `main.pdf`, 9 A4 pages, 297919 bytes.
- PDF SHA-256:
  `7fc2af35298df1eaa15b2ec842b83e7aade01288f34826c382f96f2461c578e8`.
- Source inventory: `README.md`, `main.tex`, and `references.bib` (three
  regular mode-0644 files, link count one).
- Ordered source lines and aggregate:
  `b35138c8497f7f9f0e5cb3db426c9c3b667f1395fc2d8a221fe737ce24633bf6`.

The first pass emitted only the normal cross-reference convergence notice;
the second pass emitted no warnings.  No auxiliary files are part of the
paper inventory or release manifest.

## Static and visual checks

- Undefined citations: 0; undefined cross-references: 0.
- Orphan citations or bibliography entries: 0 (10 cited keys, 10 entries).
- Overfull/underfull boxes on the stabilized pass: 0.
- Fatal, engine, missing-character, and placeholder diagnostics: 0.
- Text extraction: PASS; 445 layout lines and 28365 bytes.
- Extracted-paper residual `TODO`, `FIXME`, `XXX`, `??`, `[?]`, `/root`,
  `/tmp`, `PAPER_PENDING`, and `NOT_RELEASED`: 0.
- Rendered first-page inspection: PASS; title, abstract, theorem, and scope
  firewall are legible and unclipped.

## Content checks

The manuscript contains the complete 36 tensor rows, 18 Q types, 8 P types,
the mixed 160/12/8 dictionary, product-form/noncollision bridge, normalized
Fourier equations and rank-three proof, seed-149 embedded equality, the
`A/B/M/F_+` diamond, global rows for C1--C4, E1--E8 and B, both ToM 140/206
local branches, the claim-to-evidence matrix, and the explicit
`NO_BAD_EULER_OR_ROOT_NUMBER` nonclaim firewall.

The paper cites Gassmann, Perlis, Bartel--Dokchitser, Parzanchevski, Lin--
Shinder--Zimmermann, Étienne, James, Kida, GAP, and TomLib.  The source audit
assigns the generic mechanisms to prior work and bounds novelty to this exact
released `W(E_6)` instance.
