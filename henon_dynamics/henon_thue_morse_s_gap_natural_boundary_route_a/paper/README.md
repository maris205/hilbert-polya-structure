# C159 paper build

Build from this directory with a fixed epoch:

```text
SOURCE_DATE_EPOCH=1700000000 FORCE_SOURCE_DATE=1 \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

The checked-in `main.pdf` is the final two-round artifact.  The three round
PDFs preserve the manuscript snapshots used by the internal improvement log.
The final release requires a byte-identical isolated double build, embedded
fonts, and a log without warnings or box/reference/citation errors.
