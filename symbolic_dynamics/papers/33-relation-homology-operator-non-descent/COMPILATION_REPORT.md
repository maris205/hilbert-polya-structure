# Compilation Report — Paper 33 / SD-C35

## Status

`SUCCESS`.

`latexmk` was not installed in the runtime, so the equivalent manual
`pdflatex -> bibtex -> pdflatex -> pdflatex -> pdflatex` sequence was used.

## Output

- PDF: `main.pdf`
- Pages: 10
- Page size: A4 (`595.276 x 841.89 pts`)
- File size: 367,310 bytes
- SHA-256: `f3d23a899a9f855285c0822dda15a7815f17eef144d1da52176e649bef34f3de`

## Checks

- Fatal LaTeX errors: 0
- Undefined references: 0
- Undefined citations: 0
- BibTeX warnings: 0
- Residual `??`, `[?]`, or `[VERIFY]` markers in PDF text: 0
- Fonts: all embedded (`pdffonts`)
- Figures: pure TikZ; no raster figures
- Visual QA: pages 3--6 rendered to PNG and inspected; Figures 1--3 have no
  label collisions after final layout pass
- Route-B/RH/target-zero claims: absent

## Notes

The only remaining LaTeX layout diagnostic is one underfull table-alignment
line in the exact-audit table.  There are no overfull boxes, undefined
references, undefined citations, or rerun requests.  Build auxiliary files are
ignored and were removed after this report was written.
