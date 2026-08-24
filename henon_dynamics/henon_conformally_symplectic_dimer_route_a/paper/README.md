# C118 paper

Compile from this directory using

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The release preserves `main.pdf` and three round-named snapshots.
