# C156 paper build

The Chinese abstract requires LuaLaTeX and the installed
`Droid Sans Fallback` font.  The deterministic release command is

```bash
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 \
  lualatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 \
  lualatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` preserve
the two internal revision rounds.  `main.pdf` is byte-identical to round 2.
Fresh-directory double builds, `pdffonts`, `pdfinfo`, log scans, extracted
text, and rendered-page inspection form the final release gate.
