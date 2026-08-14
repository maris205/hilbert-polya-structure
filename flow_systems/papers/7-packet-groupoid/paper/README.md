# Paper 7 release package

`paper.pdf` is the review-ready release of *Prime Packets without a Packet
Trace: Decomposable Proxies, a Zero-Mode Ledger, and the Same-Object
Boundary*.

## Contents

- `manuscript.tex`: XeLaTeX source, with an English abstract and a
  simplified-Chinese abstract.
- `references.bib`: source-locked primary-source bibliography with versioned
  arXiv locators where applicable.
- `fig_owner_map.tex`: native TikZ diagram separating the four records and
  their analytic owners.
- `fig_ef_collapse.tex`: native TikZ diagram for packetwise surjectivity,
  transverse collapse, strict global non-surjectivity, and the absent proxy
  bridge.
- `paper.pdf`: 22-page A4 release PDF.
- `../notes/sources/paper7_source_manifest.md`: canonical union manifest for
  all 15 locally read primary PDFs and their preflight sidecars.

## Build

Run from this directory with XeLaTeX and BibTeX available:

```bash
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex paper
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
```

The extra final XeLaTeX pass makes the clean-build cross-reference state
stable.  Temporary `.aux`, `.bbl`, `.blg`, `.log`, `.out`, and `.toc` files
are build products rather than release inputs.

## Release audit

The release was clean-built on 14 August 2026.  BibTeX reported no warning or
missing entry.  The final XeLaTeX log contained:

- zero undefined citations or references;
- zero overfull boxes;
- zero missing-glyph diagnostics;
- zero LaTeX or package warnings; and
- 35 nonfatal underfull-box diagnostics, concentrated in narrow audit-table
  cells and long typed identifiers.

`pdfinfo`, `pdffonts`, and `pdftotext -layout` completed successfully.  All
fonts are embedded.  Pages 1, 4, 16, 17, and 22 were visually inspected for
the author and bilingual abstract block, both native figures, the final
object-specific Route table, and the bibliography.

The deterministic control package remains locked at 21/21 tests, nine CSV
artifacts, 407 data rows, and 669 primes through 5000.  Its schema-v2 manifest
SHA-256 is
`fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26`.
The independent object-specific Route-A v0.2.0 audit SHA-256 is
`79261a2e6e70350a22d1fc81336c24c7c86fc1baafaa5ed8acbbebea404a6091`.
The canonical 15-source manifest SHA-256 is
`d99a0e9c9ddcfb4ab5ca3f7a57284dd1a405567664ce3dcc1d7abd1602fd4d0e`.

## Release hashes

```text
5fd2f30d072b5c629a67c2be95b8fcc95a917e694f7e6be13a45f347f0e0c384  manuscript.tex
68d96e5857dafd0594acd5d465637487c9281e06a178faed3e2998c231d3b48f  references.bib
684bb3e83de9f12c92651580797d72c0b528051549b80f8239dc083dfcde03f3  fig_owner_map.tex
fca764ba3ee291961c7b9c013544ea5751cc03f6ce8d4168fbd4ddfff9e86959  fig_ef_collapse.tex
4f0f9fbebf705e6b73c34fb66b01d4dda9d6ac37b7409f587bbefd8fecdcbd8d  paper.pdf
d99a0e9c9ddcfb4ab5ca3f7a57284dd1a405567664ce3dcc1d7abd1602fd4d0e  ../notes/sources/paper7_source_manifest.md
```
