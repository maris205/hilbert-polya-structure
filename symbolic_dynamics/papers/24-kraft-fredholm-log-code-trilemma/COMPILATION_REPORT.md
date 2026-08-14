# Compilation Report — Paper 24

**Main source:** main.tex  
**Output:** main.pdf  
**Build date:** 2026-08-14 UTC  
**Toolchain:** pdfTeX 3.141592653-2.6-1.40.22, BibTeX 0.99d

## Reproducible build

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

## Frozen output

- pages: 10
- page size: A4, 595.276 by 841.890 points
- file size: 352278 bytes
- SHA-256:
  2c2fee8a7487eec67db5a6ba41095249084150598d2156afa37de38d1abadd48
- fonts: 21 font objects; all Type 1, embedded, subset, and Unicode mapped

## Final-pass checks

- LaTeX errors: 0
- LaTeX/package warnings: 0
- undefined citations: 0
- undefined references: 0
- overfull boxes: 0
- underfull boxes: 0
- BibTeX warnings: 0
- control bytes: 0
- auxiliary build artifacts retained after cleanup: 0

Pages 1, 2, 5, 6, and 10 were rendered to raster previews and visually
inspected. The two TikZ figures fit within the text block, have redundant
line-style/text encodings, and remain readable in grayscale.
