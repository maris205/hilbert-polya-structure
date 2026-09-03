# Compile report

Fresh two-pass LuaLaTeX builds use `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

| Round | Pages | Font rows | SHA-256 |
|---|---:|---:|---|
| 0 | 1 | 12 | `8f6b3e8485f3b97d0cd84b3f620546c06312377389c9af18a9fe634c047683fa` |
| 1 | 2 | 13 | `e7d7de5b27b29fc3ebc56b31e0b65acc2a3aa25c78826b6885734184329c6c7b` |
| 2/final | 3 | 13 | `2a671d242db3ab2beabbc13deecb66cf3229625ccc64f543c29a8a8bbb97654d` |

All fonts are embedded and subset.  Logs contain no LaTeX/package warning, overfull or underfull box, missing glyph, or undefined reference.  Every page rasterizes nontrivially, extracted text has no forbidden control bytes or literal TeX artifacts, and all three final pages were visually inspected.  `main.pdf` is byte-identical to round 2.
