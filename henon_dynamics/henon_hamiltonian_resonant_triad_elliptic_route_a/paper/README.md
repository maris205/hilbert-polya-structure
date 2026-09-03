# Paper build

`main.tex` uses `\CRevisionRound=0,1,2` to produce three substantively increasing manuscripts.  The release script builds every round twice in separate fresh directories with LuaLaTeX, the frozen epoch, and a fixed trailer ID.  `main.pdf` must be byte-identical to `main_round2.pdf`.

The gate rejects compilation warnings, layout warnings, missing glyphs, undefined references, drafting markers, TeX garbage, nonembedded fonts, failed rasterization, stale hashes, and absent revision sentinels.
