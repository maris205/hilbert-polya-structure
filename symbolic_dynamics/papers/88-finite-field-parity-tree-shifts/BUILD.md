# Build

From this directory run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run the deterministic proof controls with:

```text
python3 code/verify_parity_tree.py
```

The paper is an internal, anonymous `amsart` preprint and names no target
journal.  The explicit four-stage LaTeX/BibTeX sequence is the portable build
contract for the package.

## Release artifact

- Build date: 2026-08-28 UTC
- PDF: `main.pdf`
- Pages: 7
- Size: 370,404 bytes
- PDF format: A4, PDF 1.5
- Final TeX pass: successful
- LaTeX/package warnings: 0
- Overfull/underfull boxes: 0/0
- Undefined references/citations: 0/0
- Fonts: 28/28 embedded, subsetted, and Unicode-mapped
- Bibliography: 9 cited keys / 9 primary-source entries
- Exact controls: 19,764 assertions; all passed
- SHA-256: `bf484b89fc3a319c2b00afa2d0b2b3789edaae83a584b54e006b2db09c808aa2`
