# C231 paper build

`main.tex` defaults to revision 2 and uses `\CRevisionRound` to expose the
three substantive revisions.  Build each revision twice in independent fresh
directories with LuaLaTeX and `SOURCE_DATE_EPOCH=1787875200`; copy the settled
round-2 PDF to both `main_round2.pdf` and `main.pdf`.  Remove all `.aux`,
`.log`, `.out`, `.toc`, `.fls`, `.fdb_latexmk`, `.synctex.gz`, and Python
bytecode sidecars before manifest closure.  See `COMPILE_REPORT.md` for the
final hashes, font and visual audit.
