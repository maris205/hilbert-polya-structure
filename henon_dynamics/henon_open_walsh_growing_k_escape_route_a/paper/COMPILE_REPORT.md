# C153 compilation report

## Final artifact

- Status: SUCCESS
- Source: `paper/main.tex`
- PDF: `paper/main.pdf`
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`
- Engine: pdfLaTeX via latexmk
- Pages: 2
- Bytes: 291,408
- Source SHA-256: `1230bac8ed901c20417bf6b327ca27b910a8254d1eb8cc38f25e7d0f388268ad`
- PDF SHA-256: `3cb61a11554f1b54dd7d951c5722791f5881f792655b4989878409884c82508c`
- `main_round2.pdf`: byte-identical to `main.pdf`

The preserved round hashes are:

- round 0: `bcfdfdda9dc194b034a3e22d07f50a6c949fdbfc591411dc856490a08d002892`
- round 1: `6109ade538fa34ddbcbf837a73ea697c11aeb9e8a5a51e134143500f5cdb05a4`
- round 2/final: `3cb61a11554f1b54dd7d951c5722791f5881f792655b4989878409884c82508c`

All three snapshots are pairwise distinct.

## Build and determinism

```text
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC \
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final source was copied into fresh directories
`/tmp/c153-final-a-yBR2rN` and `/tmp/c153-final-b-LydpyL`.  Both isolated
builds and the release PDF have the same SHA-256
`3cb61a11554f1b54dd7d951c5722791f5881f792655b4989878409884c82508c`.

## Automated checks

- LaTeX errors: 0
- warnings: 0
- overfull boxes: 0
- underfull boxes: 0
- undefined references or citations: 0
- multiply defined labels: 0
- literal source-token scan (`qquad`, `??`): clean
- `pdffonts`: every listed font is embedded and subset
- `pdfinfo`: two pages, valid 291,408-byte PDF 1.5
- `pdftotext`: successful extraction of both pages

## Visual inspection

Both pages were rasterized at 144 dpi in
`/tmp/c153-final-render-1PkFe9` and inspected at original resolution.  The
title, abstract, all eight numbered displays, theorem and proof, parity
witness, controls, validation counts, Route-A verdict, and scope boundary are
legible.  There is no clipping, overlap, truncated line, broken glyph,
duplicate display tag, unexpected token, or blank page.
