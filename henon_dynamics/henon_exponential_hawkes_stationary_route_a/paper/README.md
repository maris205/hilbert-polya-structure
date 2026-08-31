# Paper build

`main.tex` is one self-contained source with a frozen revision selector.
Without an override it builds the final round (`HAWKESROUND=2`).  The archived
artifacts were produced in fresh directories with LuaLaTeX, two passes per
build, and

```text
SOURCE_DATE_EPOCH=1788048000
FORCE_SOURCE_DATE=1
TZ=UTC
```

The three source invocations are:

```sh
lualatex -interaction=nonstopmode -halt-on-error -jobname=main '\def\HAWKESROUND{0}\input{main.tex}'
lualatex -interaction=nonstopmode -halt-on-error -jobname=main '\def\HAWKESROUND{1}\input{main.tex}'
lualatex -interaction=nonstopmode -halt-on-error -jobname=main '\def\HAWKESROUND{2}\input{main.tex}'
```

Run the selected invocation twice.  The archived names are
`main_round0_original.pdf`, `main_round1.pdf`, and `main_round2.pdf`;
`main.pdf` is byte-identical to round 2.  `COMPILE_REPORT.md` records the
fresh-build comparison, page and font audit, and PDF hashes.
