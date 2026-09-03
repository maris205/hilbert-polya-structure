# Compile report

All rounds were compiled with LuaLaTeX twice in each of two fresh directories
under SOURCE_DATE_EPOCH=1788393600, FORCE_SOURCE_DATE=1, and TZ=UTC. Each pair
was byte-identical and equals the checked-in PDF.

| round | pages | font rows | SHA-256 |
|---:|---:|---:|---|
| 0 | 2 | 13 | 7fcc245e500f2db0f8afbe1f25a694b7b3fe32b40ced666ac19db599af673f45 |
| 1 | 2 | 13 | a633bb175929cf9e1fd9407c40876cb6f21d50f89be81502f7075cac440fee88 |
| 2 | 3 | 13 | 229823ee78f2831d573820db647f0199a9b0b11631195ce2b31c414fab9d9dcc |

main.pdf is byte-identical to round 2. Settled logs contain no LaTeX/package
warning, overfull/underfull box, undefined reference/citation, rerun request, or
missing-character event. Every font row is embedded and subset.
pdftotext -layout contains no forbidden control byte or drafting/TeX-garbage
sentinel. All seven pages across the three rounds rasterize successfully. The
three final pages were inspected visually for equations, margins, page breaks,
references, and footer placement.
