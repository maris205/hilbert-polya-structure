# C323 compile report

All rounds were compiled with LuaLaTeX, two passes per fresh build,
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The
release gate repeats each round in two isolated directories and requires both
fresh byte streams to equal the checked-in artifact.

| round | pages | bytes | embedded subset font rows | SHA-256 |
|---:|---:|---:|---:|---|
| 0 | 2 | 126634 | 18 | `7fec3f40aaac15a41167b570d0c26094aa1a1e2e71d861b171054e0d0b5b1f41` |
| 1 | 3 | 140095 | 18 | `b73fea8a9d4d2276f3549315575356cbc75e3ab5c173892748dea14258624a77` |
| 2 | 3 | 152030 | 19 | `b8cf1279c76f0fd269337886d159434617dda9e1d84ee58f5885436e1f94cc17` |

`main.pdf` is byte-identical to round 2.  Every final log is free of LaTeX
and package warnings, overfull/underfull boxes, undefined references or
citations, rerun requests, and missing characters.  Every page rasterizes,
all three final pages were visually inspected, and `pdffonts` reports every
font embedded and subset.
