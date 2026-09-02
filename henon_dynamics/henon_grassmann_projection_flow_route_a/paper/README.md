# Paper build

`main.tex` is the single source for revision rounds 0, 1, and 2.  Round 0 is
the global-solution baseline; round 1 adds tie-safe Schubert rates and the
repeated-spectrum Morse--Bott theorem; round 2 adds exact evidence, source and
C185 collision audits, Route-A scope, reproducibility, and AI-use statements.

The release script performs two LuaLaTeX passes in each of two fresh
directories per round with `SOURCE_DATE_EPOCH=1788307200`, checks byte
identity, logs, fonts, text, pages, and raster output, and requires
`main.pdf` to equal `main_round2.pdf`.
