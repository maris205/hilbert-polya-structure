# Compile report

- Engine: `latexmk -pdf` with `SOURCE_DATE_EPOCH=0`.
- Result: successful two-page PDF.
- References/citations: none; no undefined references or citations.
- Layout: no overfull/underfull boxes in the final log.
- Fonts: embedded and verified with `pdffonts`.
- Determinism: two isolated builds were byte-identical.
