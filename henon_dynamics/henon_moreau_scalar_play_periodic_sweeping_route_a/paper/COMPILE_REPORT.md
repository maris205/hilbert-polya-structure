# Compile report

Fresh LuaLaTeX was run twice per revision with `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

| Round | SHA-256 | Pages | Embedded/subset font rows |
|---|---|---:|---:|
| 0 | `fece7433cb66d238394f9353a0eed4bf2897028a673343b59cf8ad479d76f209` | 1 | 18 |
| 1 | `04a6d93e6f073c54c8f3a745e61145921467e2950e7fe560811d2e6d5c394976` | 2 | 18 |
| 2/final | `0fd91d8d949aa6e6b86ceb9e109b9e4c5b982ba4fe4c435ef1a99dbd9c41fedf` | 3 | 21 |

The three PDFs are byte-distinct and `main.pdf` equals round 2. Repeated fresh double builds are byte-identical. Logs have no LaTeX/package warnings, overfull or underfull boxes, undefined references/citations, rerun requests, or missing glyphs. Every page rasterizes, extracted text is free of replacement and forbidden control characters, and all fonts are embedded and subset.
