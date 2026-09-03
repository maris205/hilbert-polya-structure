# Paper build

`main.tex` is the sole source.  It is compiled with LuaLaTeX and an explicit
revision macro:

```bash
SOURCE_DATE_EPOCH=1788393600 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main '\def\CRevisionRound{2}\input{main.tex}'
```

Run the command twice in a fresh directory.  Rounds 0, 1, and 2 are materially
different; `main.pdf` is byte-identical to `main_round2.pdf`.  The release gate
repeats each fresh build twice, rejects LaTeX/layout/reference/glyph warnings
and extracted control or TeX-garbage strings, checks each page raster, and
requires every font to be embedded and subset.
