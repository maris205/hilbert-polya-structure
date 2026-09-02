# C315 paper build

`main.tex` contains three retained revisions selected by
`\CRevisionRound=0,1,2`.  LuaLaTeX runs twice in isolated directories with
`SOURCE_DATE_EPOCH=1788393600`; final `main.pdf` must equal
`main_round2.pdf`.  The release gate checks settled warnings, text
sentinels, page rasterization, fonts, and two independent builds per round.
