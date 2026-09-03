# Paper build

`main.tex` accepts `CRevisionRound=0,1,2`.  Each round is substantively
different; the final PDF is byte-identical to round 2.  Release builds every
round twice in fresh temporary directories with LuaLaTeX and the fixed source
epoch, then checks logs, page rasters, extracted text, embedded/subset fonts,
and byte determinism.
