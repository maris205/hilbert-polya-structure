# Manuscript

`main.tex` is a self-contained mathematical note for COPRIME-0001. It uses a
generic article layout because this stage is a theorem/obstruction report,
not a conference submission. No external bibliography is required.

Build twice (or with `latexmk`) from this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```
