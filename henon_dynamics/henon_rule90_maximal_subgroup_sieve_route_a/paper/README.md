# C160 paper build

Build with:

```text
SOURCE_DATE_EPOCH=1700000000 FORCE_SOURCE_DATE=1 \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

Release requires a byte-identical fixed-epoch double build, two A4 pages,
embedded/subset fonts, no LaTeX warning or box/reference/citation defect, and
an exact self-excluded manifest.
