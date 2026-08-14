# Compilation report

Date: 2026-08-14

Engine: `pdfTeX 1.40.22` with BibTeX.

Build sequence:

```bash
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

Result:

- `paper.pdf`: 8 pages;
- size: 257310 bytes;
- author metadata: Liang Wang;
- undefined citations/references: 0;
- overfull/underfull boxes: 0;
- compilation warnings after final pass: 0;
- visual inspection: title/abstract page and polynomial/reference appendix
  both fit within page bounds; no blank terminal page.

PDF SHA-256:
`d46cc29e4304b64c5b08f1b148a3c261c5c0e786a75f265c7fc1f574c29ad21d`.
