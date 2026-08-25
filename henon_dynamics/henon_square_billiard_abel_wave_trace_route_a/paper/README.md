# C157 paper build

The Chinese abstract requires LuaLaTeX and `Droid Sans Fallback`.  Build the
deterministic release with

```bash
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 \
  lualatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 \
  lualatex -interaction=nonstopmode -halt-on-error main.tex
```

Round 0, round 1, and round 2 PDFs preserve both internal revision passes.
`main.pdf` is byte-identical to `main_round2.pdf`.  Fresh-directory double
builds, font inspection, log/text scans, and rendered-page review form the
release gate.
