# C158 paper artifacts

`main.tex` is final.  `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf` retain both internal review transitions; `main.pdf` is
byte-identical to round 2.  The compile report records deterministic builds,
fonts, warnings, text extraction, and rendered-page inspection.

The final source is compiled with LuaLaTeX because it contains an independently
written Simplified Chinese abstract.  The embedded Chinese face is
`/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf`.

From this `paper/` directory, reproduce the audited build with:

```bash
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```
