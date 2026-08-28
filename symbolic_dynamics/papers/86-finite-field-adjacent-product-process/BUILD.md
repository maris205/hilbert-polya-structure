# Build

From this directory run:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Run the deterministic proof control with:

```text
python3 code/verify_adjacent_product.py
```

The build is intentionally an explicit four-stage LaTeX/BibTeX build rather
than a venue-specific submission workflow.  This is an internal `amsart`
preprint and names no target journal.

Artifact metadata and warning counts are recorded in `FINAL_QA.md` after the
release build.

## Release artifact

- Build date: 2026-08-28 UTC
- PDF: `main.pdf`
- Pages: 7
- Size: 318,027 bytes
- Final TeX pass: successful with zero LaTeX/package warnings
