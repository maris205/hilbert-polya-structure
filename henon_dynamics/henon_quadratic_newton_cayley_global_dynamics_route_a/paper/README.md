# C257 paper build

Build each revision twice with LuaLaTeX under the fixed environment:

```bash
SOURCE_DATE_EPOCH=1788048000 FORCE_SOURCE_DATE=1 TZ=UTC \
  lualatex -interaction=nonstopmode -halt-on-error \
  -jobname=main '\\def\\CRevisionRound{2}\\input{main.tex}'
```

The release retains `main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf`; `main.pdf` must equal round 2 byte for byte.  See
`COMPILE_REPORT.md` for hashes and quality gates.
