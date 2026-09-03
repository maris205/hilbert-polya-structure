# C350 compile report

All three revisions were compiled twice in separate fresh directories with
LuaLaTeX, `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and
`TZ=UTC`.  Each same-round pair was byte-identical, and a further release
rebuild reproduced every checked PDF.

| revision | pages | bytes | font rows | SHA-256 |
|---|---:|---:|---:|---|
| round 0 | 1 | 28,249 | 6 | `495ef248da1dca9c1e2af49c0b247ed6a4b3de0ed7b0e36147e8ceeeb5445c9c` |
| round 1 | 2 | 38,696 | 6 | `f21b7e603b719efc4148e4276963e1f0ccd643d48a0af430e9e1000c9742dd70` |
| round 2 | 3 | 47,216 | 6 | `a7350723ba41d6e58b5d91c26f81a455a10a93d18ef67c1d3f758a7284a0c8a6` |
| final | 3 | 47,216 | 6 | `a7350723ba41d6e58b5d91c26f81a455a10a93d18ef67c1d3f758a7284a0c8a6` |

Settled logs contain zero LaTeX/package warnings, overfull or underfull
boxes, undefined references/citations, missing characters, or rerun notices.
Every font row is embedded and subset.  `pdftotext -layout` passed the UTF-8,
control-byte, source-sentinel, and Route-B-lock gates; `pdftoppm` rasterized
every page.  Visual review of all six revision pages found no clipping,
overlap, blank page, malformed delimiter, stray TeX token, or anomalous
mathematical layout.  `main.pdf` is byte-identical to round 2.
