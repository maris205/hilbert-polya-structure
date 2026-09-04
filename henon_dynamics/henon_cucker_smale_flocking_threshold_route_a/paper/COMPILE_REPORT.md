# Compile report

Each conditional manuscript round was built twice in fresh directories with LuaLaTeX under `SOURCE_DATE_EPOCH=1788480000`; both bytes matched the stored artifact.  Settled logs have no warnings or layout defects, all fonts are embedded and subset, extracted text has no control garbage, and every page rasterizes.

| round | pages | font rows | SHA-256 | substantive addition |
|---|---:|---:|---|---|
| 0 | 1 | 11 | `b08a29027baee87210da9ecf5acf126e2b26cc6a4192d8d0a23a53287e2d8b6e` | global flow, dissipation, diameter lemma, and tail barrier |
| 1 | 2 | 12 | `c8136de66a177a77ae605e2271b9659ac2a0ca0fa5fb82b32ebece9fc5ff3be4` | endpoint, explicit radius, and exact scalar threshold sharpness |
| 2 | 2 | 16 | `6405689843fa3a82a6ee3ad6961080d3b1d06e2a54ebd20d75bff690db5d7e79` | degenerate atlas, source boundary, evidence semantics, and route firewall |

`main.pdf` is byte-identical to round 2.
