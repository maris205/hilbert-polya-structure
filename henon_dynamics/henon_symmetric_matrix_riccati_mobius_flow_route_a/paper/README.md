# C309 paper build

`main.tex` contains three retained revisions selected by
`\CRevisionRound=0,1,2`.  LuaLaTeX is run twice in isolated directories with
`SOURCE_DATE_EPOCH=1788393600`; the final `main.pdf` is byte-identical to
`main_round2.pdf`.  The release verifier checks settled warnings, embedded
and subset fonts, page rasterization, text sentinels, and two independent
rebuilds of every round.
