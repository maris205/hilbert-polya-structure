# Paper build

`main.tex` is the single source for three substantive revisions.  Define
`CRevisionRound` as 0, 1, or 2 before input to build the archived baseline,
proof-hardened, or final audit-hardened version.  The release script performs
two LuaLaTeX passes in each of two fresh directories per round with
`SOURCE_DATE_EPOCH=1788307200`, checks settled logs, fonts, pages, text, and
byte identity, and requires `main.pdf` to equal `main_round2.pdf`.
