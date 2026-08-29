# Paper build

`main.tex` defaults to revision 2.  Revision 0 contains the exact pregel and
critical theorem; revision 1 adds the two postgel closures and source/uniqueness
firewalls; revision 2 adds reproducibility and Route-A analysis.  The three
released PDF hashes must therefore be distinct.

Every revision is built twice with LuaLaTeX under
`SOURCE_DATE_EPOCH=1787875200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  Final
`main.pdf` is byte-identical to `main_round2.pdf`.  See `COMPILE_REPORT.md` for
log, font, text, deterministic-build and visual checks.
