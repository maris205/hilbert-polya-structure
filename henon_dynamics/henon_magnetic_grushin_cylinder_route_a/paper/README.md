# Manuscript build

`main.tex` conditionally produces Rounds 0, 1, and 2 via
`\CRevisionRound`.  Reproduction uses two LuaLaTeX passes with
`SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
The release script compiles each round twice in fresh directories, demands
byte identity with its archive, scans the settled log, checks every font is
embedded/subset, verifies page and extracted-text contracts, and requires
`main.pdf` to equal `main_round2.pdf`.
