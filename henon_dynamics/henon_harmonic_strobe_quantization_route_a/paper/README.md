# C178 manuscript build

Compile `main.tex` with LuaLaTeX under the fixed epoch:

```bash
SOURCE_DATE_EPOCH=1787702400 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

Run the command twice in a fresh directory.  The released `main.pdf` is
byte-identical to `main_round2.pdf`.  The manuscript has no bibliography:
its citation and reference registry populations are both zero.
