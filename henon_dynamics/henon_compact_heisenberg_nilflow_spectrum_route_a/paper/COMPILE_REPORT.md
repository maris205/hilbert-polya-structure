# Compile report

Every round was built twice in fresh directories at epoch 1788566400, with two LuaLaTeX passes per build. Each pair is byte identical. All fonts are embedded/subset, all pages rasterize and settled logs contain no warning.

| round | pages | fonts | bytes | SHA256 |
|---|---:|---:|---:|---|
| 0 | 2 | 15 | 81852 | 1ab57bfdc379b72fd77a26db9008511394d5bc158da8ffa5bcdd0408abbf163e |
| 1 | 4 | 17 | 102432 | ecb4414c5aced99541ec29c1aad82c93d4fe3197a23f73b6c41ab641f89e0e1e |
| 2 | 5 | 17 | 121448 | a9f25212a5e6a9234b0157bdfca39e0cbfcae9338a8adc4003df3de57cc434c7 |

main.pdf equals round2. Round0 proves every rational-slope return and clean fixed torus; round1 adds the entire signed-mode spectrum and self-adjoint domains; round2 adds unique ergodicity, same-clock reversal, noncompactness and source/target separation. Raw settled logs are retained as .txt files.
