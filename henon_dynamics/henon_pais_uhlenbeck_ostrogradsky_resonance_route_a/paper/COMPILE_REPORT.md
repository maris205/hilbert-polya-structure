# C359 compile report

The release gate compiled every revision twice in fresh directories with LuaLaTeX and `SOURCE_DATE_EPOCH=1788480000`, then compared bytes.

| round | pages | font rows | SHA-256 |
|---:|---:|---:|---|
| 0 | 2 | 10 | `df845b683e41b88910ea61dcde10dac027169e1e9d582ac111a6d3754ef74cb8` |
| 1 | 2 | 10 | `bba4b90d7122bc2ae2e931c9e9159db13d42e25dab62b1bd6408b866009b6748` |
| 2 | 3 | 12 | `199a2855ae36a1a40ef8c34657066779411d544f01ecdbc025a86167f7f7b5c2` |

All six fresh builds were byte deterministic. Settled logs had zero warnings, overfull/underfull boxes, undefined references/citations, rerun notices, and missing glyphs. Every font was embedded and subset; extracted text had no forbidden token or control byte, and every page raster passed. `main.pdf` is byte-identical to round 2.
