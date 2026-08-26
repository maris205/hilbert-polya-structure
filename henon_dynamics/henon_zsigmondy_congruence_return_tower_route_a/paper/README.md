# C179 manuscript build

Compile `main.tex` with LuaLaTeX under the fixed epoch:

```bash
SOURCE_DATE_EPOCH=1787788800 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex --interaction=nonstopmode --halt-on-error main.tex
```

Run the command twice in each fresh isolated directory.  The released
`main.pdf` is byte-identical to `main_round2.pdf`.  The manuscript has four
attributed references; Zsigmondy's existence theorem is explicitly external
and not claimed new.
