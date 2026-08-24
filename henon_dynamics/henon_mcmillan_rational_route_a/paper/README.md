# Paper build

From this directory:

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` preserve
the baseline and two substantive revisions described in the package-level
improvement log.  `main.pdf` is the final round-two paper.
