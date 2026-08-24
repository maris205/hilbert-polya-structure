# C120 paper build

Build deterministically from this directory:

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final audit requires a repeated isolated build with the same SHA-256,
embedded fonts, and no final LaTeX, reference, citation, or box warnings.
