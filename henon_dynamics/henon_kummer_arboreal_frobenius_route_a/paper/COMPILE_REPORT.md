# Compile report

Each manuscript source was built twice in fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788480000`; both builds matched byte for byte. Settled logs contain no warning, overfull/underfull box, badness, or undefined-reference sentinel. Every font is embedded and subset, extracted text is clean, and every page rasterizes.

| round | source | pages | fonts | SHA-256 | theorem increment |
|---|---|---:|---:|---|---|
| 0 | `paper/main_round0.tex` | 2 | 16 | `34b55c1d6b04dff632a0fa388d41e1e5f93676cff365b32424549a692e7bea7c` | intersection, degree, exact finite image, and restriction theorem |
| 1 | `paper/main_round1.tex` | 3 | 16 | `3ab3d818bef9e56a2a53a85981d90d5ca69b8813b9b0e9185ccbca1b4cef2414` | complete fixed-root spectrum and Chebotarev density theorem |
| 2 | `paper/main_round2.tex` | 5 | 18 | `d53d5f74dbbdaaec4b2d8893ee2c55c30b1891f28edf6995f4143ba312c7bb06` | inverse limit, all-iterate dictionary, exact evidence, finite Koopman boundary, and Route-A closure |

`paper/main.pdf` is byte-identical to round 2.
