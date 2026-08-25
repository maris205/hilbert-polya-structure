# C149 paper build

From this directory run:

```bash
SOURCE_DATE_EPOCH=1787616000 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` preserve
the two genuine internal-repair stages.  Final `main.pdf` is byte-identical to
round 2.  No bibliography or external figure is used.
