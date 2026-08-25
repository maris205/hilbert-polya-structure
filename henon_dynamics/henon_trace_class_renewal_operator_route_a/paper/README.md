# Paper build

Run twice with a fixed epoch:

```bash
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final release retains the original, round-one, and round-two PDF
snapshots.  `main.pdf` must be byte-identical to `main_round2.pdf`.
