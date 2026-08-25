# C150 paper build

Build with a fixed epoch:

```bash
SOURCE_DATE_EPOCH=1787616000 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The three preserved snapshots record the original, round-1, and round-2
papers.  Final `main.pdf` is byte-identical to round 2.  The manuscript uses no
bibliography or external figure.
