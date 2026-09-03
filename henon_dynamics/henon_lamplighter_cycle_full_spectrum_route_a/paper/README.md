# Paper build

`main.tex` uses `\CRevisionRound=0,1,2` to produce three substantively
increasing manuscripts.  Every checked PDF is compiled in two fresh temporary
directories with LuaLaTeX at `SOURCE_DATE_EPOCH=1788393600`; the resulting
bytes must match.  `main.pdf` is byte-identical to `main_round2.pdf`.
