# C175 manuscript build

Compile `main.tex` with LuaLaTeX under the fixed epoch:

```bash
SOURCE_DATE_EPOCH=1787702400 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

The released `main.pdf` equals `main_round2.pdf`. Build in a fresh directory so auxiliaries do not enter the package. The manuscript has no bibliography because citation and reference registry populations are zero.
