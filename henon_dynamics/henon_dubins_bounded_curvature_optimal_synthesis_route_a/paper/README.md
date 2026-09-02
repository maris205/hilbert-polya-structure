# C310 paper build

`main.tex` defines substantive rounds 0, 1, and 2 through
`\CRevisionRound`.  Every retained PDF is built twice with LuaLaTeX at fixed
epoch `1788393600`.  The release checker requires warning-free settled logs,
embedded/subset fonts, text sentinels, rasterized pages, byte-deterministic
rebuilds, and `main.pdf == main_round2.pdf`.
