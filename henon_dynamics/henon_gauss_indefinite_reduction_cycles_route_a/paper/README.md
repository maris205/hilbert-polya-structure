# C364 paper build

`main.tex` is compiled with LuaLaTeX and fixed `SOURCE_DATE_EPOCH=1788480000`.

- round 0: finite reduced permutation, stabilizer, multiplier, determinant core;
- round 1: predecessor, reversal, full source zeta, and exact receipt;
- round 2: norm-sign split, all excluded boundaries, source/collision audit, and Route-A firewall.

The release gate builds each round twice in fresh temporary directories, rejects all settled-log warnings and layout boxes, checks embedded/subset fonts, extracts clean text, rasters every page, and requires `main.pdf` to equal round 2 byte for byte.
