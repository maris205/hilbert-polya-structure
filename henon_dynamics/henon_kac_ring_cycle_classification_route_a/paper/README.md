# C170 manuscript build

Compile `main.tex` with LuaLaTeX under the fixed epoch:

```bash
SOURCE_DATE_EPOCH=1787702400 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

The released `main.pdf` equals `main_round2.pdf`. Use a fresh directory so auxiliary files stay outside the 27-file payload. The citation/reference registry population is zero, so there is no bibliography.
