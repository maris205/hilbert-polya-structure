# C364 compile report

The release gate compiled every revision twice in fresh directories with LuaLaTeX and `SOURCE_DATE_EPOCH=1788480000`, then compared the resulting bytes.

| round | pages | font rows | SHA-256 |
|---:|---:|---:|---|
| 0 | 2 | 12 | `980874c6fd09918a1eda5ed8db9600e057573f46de8acdb77c7352d99cabf72f` |
| 1 | 3 | 12 | `f35d00d53f64a9c176ac6e5d789fc8672744e4b065dc381b85553ea457628f4f` |
| 2 | 3 | 12 | `69cb518f0b6db10e88192e1ff3910155213ad6b6215afe4956f48b0edc625ff0` |

All six fresh builds were byte deterministic. Settled logs had zero warnings, overfull or underfull boxes, undefined references or citations, rerun notices, and missing glyphs. Every font was embedded and subset. Extracted text contained no forbidden marker or control byte, every page rasterized above the minimum size, and `main.pdf` is byte-identical to round 2.
