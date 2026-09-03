# Compile report

Fresh LuaLaTeX was run twice per revision with
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

| Round | SHA-256 | Pages | Embedded/subset font rows |
|---|---|---:|---:|
| 0 | `dac0b3f8e5ed7b395b30a8a1fe42bf8f383707b9cf64520208e863730d1e8001` | 2 | 20 |
| 1 | `1267731c062b25c628c832a721ceaf508a65907a7003218739897c189afaf860` | 3 | 22 |
| 2/final | `eecd570218803814ae0042512ef5d72196e8b00a9e93c497c3492cebdbe4881c` | 3 | 23 |

The PDFs are pairwise byte-distinct and `main.pdf` equals Round 2.  Repeated
fresh builds are byte-identical.  Settled logs have no LaTeX/package warnings,
overfull or underfull boxes, undefined references/citations, rerun requests or
missing glyphs.  Every page rasterizes, extracted text has no replacement or
forbidden control characters, and every font is embedded and subset.
The extracted text contains no bare `qquad` command residue.
