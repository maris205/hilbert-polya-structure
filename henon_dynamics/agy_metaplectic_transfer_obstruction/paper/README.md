# Paper build

The note is a self-contained source/application paper for HCS-C25.  It uses
the published AGY article as the formula authority and labels every
project-derived operator statement separately.

Build from this directory with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The release includes `main.pdf` only after the independent exact checker,
reference scan, and clean LaTeX build all pass.
