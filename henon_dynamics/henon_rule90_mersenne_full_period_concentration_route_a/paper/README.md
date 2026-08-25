# C155 paper build

From this directory run:

```bash
SOURCE_DATE_EPOCH=1787616000 TZ=UTC latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf` preserve
the two genuine internal-repair stages.  Final `main.pdf` is byte-identical to
round 2.  LuaLaTeX and the embedded Droid Sans Fallback font render the
independently written Chinese abstract.  No bibliography or external figure
is used.
