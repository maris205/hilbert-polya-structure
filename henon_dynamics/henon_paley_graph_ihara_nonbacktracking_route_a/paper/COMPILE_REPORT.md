# Compile report

All rounds were built twice from fresh temporary directories with LuaLaTeX,
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

| round | pages | bytes | SHA-256 | embedded/subset font rows |
|---|---:|---:|---|---:|
| 0 | 2 | 42591 | `7e371366ca0af6079530e53a7bed822f6b610080fab6feed4cceea061811ae20` | 7 |
| 1 | 2 | 48250 | `196219a52d213118f9f1f3daae73b5828fb7e5b92b91705ff79fa7046eb2068c` | 7 |
| 2 | 3 | 51012 | `286ba44628b8f27df7fd352f11d53514c6388f0bea2b3e4c0818b910c8bed502` | 7 |

`main.pdf` is byte-identical to round 2.  All settled logs have zero LaTeX,
package, overfull, underfull, undefined-reference, or missing-glyph warnings.
Every page rasterizes nontrivially.  Extracted text contains no low control
bytes, `qquad`, `??`, `[VERIFY]`, or unfinished marker.
