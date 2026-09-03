# Compile report

Fresh LuaLaTeX was run twice for each revision with `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.

| Round | SHA-256 | Pages | Embedded/subset font rows |
|---|---|---:|---:|
| 0 | `72d5d3beff2bf88817b640022dc6b891d2802cd3859d7b1156e48aa031a48146` | 2 | 16 |
| 1 | `b279ee7b0e44126bdcea0a680f2c6577ae210833f474664a7251a44ce032fb38` | 2 | 20 |
| 2/final | `679a8ba2b778610da80eb774aa47da8a4e047106afea735cf408b91ece16e3ac` | 3 | 21 |

All rounds are byte-distinct and `main.pdf` equals round 2. Fresh double builds are byte-deterministic. Logs contain no LaTeX/package warnings, overfull or underfull boxes, undefined references/citations, rerun requests, or missing glyphs. Every page rasterizes; extracted text contains no replacement or forbidden control character and no literal `qquad`, `??`, or `[verify]` artifact; every font is embedded and subset.
