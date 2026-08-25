# C164 paper build

Build from this directory with the frozen environment:

```text
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

The checked-in `main.pdf` equals `main_round2.pdf`.  Round 0, round 1, and
round 2 are content-distinct manuscript snapshots documented in the package
improvement log.  Release requires two fresh byte-identical final builds,
embedded subset fonts, a log without warnings or box/reference/citation
errors, and rendered-page inspection.
