# C318 compile report

All rounds were compiled with LuaLaTeX, two passes per fresh build,
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
The release gate repeats each round in two isolated directories and requires
both fresh byte streams to equal the checked-in artifact.

| round | pages | bytes | embedded subset font rows | SHA-256 |
|---:|---:|---:|---:|---|
| 0 | 2 | 130562 | 17 | `43a73c91aafbc66fb41f6c2b254323644938901b3f5d9015f9222ef0dcfa61fb` |
| 1 | 3 | 152227 | 18 | `92acf84d635a082d8f7834ba9030de0e8bd7cbcdc8302c312a16f41263a2f7f4` |
| 2 | 4 | 167932 | 19 | `b079037a4a7ba33a2db35076cb2b75114643016c6388fb65647c13e06a934947` |

`main.pdf` is byte-identical to round 2.  Every final log is free of LaTeX
and package warnings, overfull/underfull boxes, undefined references or
citations, rerun requests, and missing characters.  Every page rasterizes,
and `pdffonts` reports every font embedded and subset.
