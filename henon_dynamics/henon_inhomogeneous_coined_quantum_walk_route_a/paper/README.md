# Paper build

Compile twice with:

```bash
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The release retains three distinct review snapshots.  The final
`main.pdf` must equal `main_round2.pdf` byte for byte.
