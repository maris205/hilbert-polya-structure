# Compile report — HCS-C126

## Frozen build

```text
SOURCE_DATE_EPOCH=1787529600
TZ=UTC
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

- source SHA-256:
  `d965dbfb88469acaa685683da7983172063ae385691522bb6e9afeb4a3c28ea5`;
- final PDF SHA-256:
  `3d305aa2d96114418059db7f2a6987ab2365d88f7dabf7d9b5edb507e3b6740b`;
- page count: `3`;
- page size: US Letter, 612 by 792 points;
- all fonts embedded: `PASS`;
- final-log package, citation, reference, overfull, and underfull warning scan:
  `PASS`;
- rendered three-page visual inspection: no clipping, collision, blank content,
  truncated formula, or broken table;
- two fresh isolated fixed-date builds: byte-identical to one another and to
  `main.pdf`.

The three improvement snapshots and final PDF are byte-identical release
reconciliations of the final source.  The internal proof and scope changes are
preserved textually in `../PAPER_IMPROVEMENT_LOG.md`; no binary snapshot retains
an obsolete claim boundary.
