# Compile report

Fresh two-pass LuaLaTeX builds use `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

| Round | Pages | Font rows | SHA-256 |
|---|---:|---:|---|
| 0 | 2 | 11 | `65b4a5c6966feda3221e505098cb140c325435907af56669a1647db1407e5781` |
| 1 | 2 | 11 | `132ff9b25045e43d26fdd10d8c57071f89c539a04ef1cf1cef2e90b5de0711d8` |
| 2/final | 3 | 11 | `326f73bece2f5e4688a96b35e99a78e4617961bf15e4afcbf8f0e6fab7ae74ec` |

All fonts are embedded and subset. Logs contain no LaTeX/package warning, overfull or underfull box, missing glyph, or undefined reference. Every page rasterizes nontrivially, extracted text has no forbidden control bytes or literal TeX artifacts, and all three final pages were visually inspected. `main.pdf` is byte-identical to round 2.
