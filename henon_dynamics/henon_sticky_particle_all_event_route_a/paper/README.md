# Manuscript build

`main.tex` is one conditional source.  Define `\CRevisionRound` as 0, 1, or
2 before input to reproduce the three retained substantive rounds.  Use two
LuaLaTeX passes with `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`,
and `TZ=UTC`.  The release manifest performs two isolated fresh-directory
builds for every round and checks bytes, settled warnings, fonts, pages, and
extracted text.  `main.pdf` is byte-identical to `main_round2.pdf`.
