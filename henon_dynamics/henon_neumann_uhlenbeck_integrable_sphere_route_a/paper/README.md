# Manuscript builds

`main.tex` is built with LuaLaTeX under fixed epoch `1788393600`. Revision rounds 0, 1, and 2 are selected by `\CRevisionRound`; `main.pdf` must be byte-identical to `main_round2.pdf`.

The release gate performs two fresh two-pass builds of each round, checks warning-free logs, embedded/subset fonts, extracted-text sentinels, rasterization, and the exact compile-report hashes.
