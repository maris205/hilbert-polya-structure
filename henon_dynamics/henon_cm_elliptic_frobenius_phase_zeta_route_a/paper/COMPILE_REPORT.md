# Compile report

All three sources were built twice in fresh directories with LuaLaTeX at epoch1788566400. Each pair matched byte for byte. Settled logs contain no layout/reference/package warning. Every font is embedded and subset, each PDF has bilingual abstracts and six keywords in each language, and every page rasterizes.

| round | pages | fonts | bytes | SHA256 |
|---|---:|---:|---:|---|
| 0 | 2 | 16 | 78604 | 5631e813a4fb70669ada01f6b4eb7563f4fe885fb8a9d3f4b52d3bf4ae2ae394 |
| 1 | 3 | 16 | 94404 | d648e69419a486c4dd26153cd844cc386818c4ea780132182286f863b00b3c0d |
| 2 | 4 | 17 | 119717 | 2188253cf1d609932aee9eb2fdec5c38807ecef57463ed980a79a333f481000e |

main.pdf equals round2. Round0 owns sign-complete CM; round1 adds phase and all-degree orbits; round2 adds determinant, obstruction, evidence and evaluator. Settled compiler logs are retained as compile_round0/1/2.txt so Git preserves the receipts.
