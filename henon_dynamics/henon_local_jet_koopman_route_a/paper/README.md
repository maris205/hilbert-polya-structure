# Paper build — C114

Run from this directory:

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The fixed trailer ID, omitted PDF dates, fixed environment, and embedded
Latin Modern fonts make isolated builds deterministic.  `main_round0_original.pdf`,
`main_round1.pdf`, and `main_round2.pdf` preserve the two-pass improvement
trail; `main.pdf` is the final artifact.
