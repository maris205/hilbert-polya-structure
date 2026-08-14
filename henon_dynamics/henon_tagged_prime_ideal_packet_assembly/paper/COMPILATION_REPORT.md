# Compilation Report

## Command

```bash
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
bibtex paper
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
pdflatex -interaction=nonstopmode -halt-on-error paper.tex
```

## Result

- status: `PASS`;
- output: `paper/paper.pdf`;
- pages: 6;
- PDF metadata author: Liang Wang;
- paper size: A4;
- unresolved citations: 0;
- unresolved references: 0;
- overfull boxes: 0;
- underfull boxes: 0.

The generated table `figures/collision_ledger.tex` is regenerated from the
canonical JSON certificate before compilation.
