# Compilation report

- Engine: LuaLaTeX.
- Frozen epoch: `1788480000`.
- Procedure: two passes in each of two fresh directories for every revision
  round.
- Determinism: PASS for all three rounds.
- Settled LaTeX warnings: 0.
- Undefined references or citations: 0.
- Embedded/subset fonts: PASS for every font row.
- Extracted-text controls and page rasterization: PASS.
- `main.pdf` equals `main_round2.pdf`: PASS.

| round | file | pages | bytes | font rows | SHA-256 |
|---:|---|---:|---:|---:|---|
| 0 | `main_round0_original.pdf` | 2 | 135,329 | 17 | `28d36fa94cbd994ca9571dab034949e89e61cd7e3f702181b006fd5442177aa5` |
| 1 | `main_round1.pdf` | 2 | 148,671 | 18 | `716a7e04cc125bd871e54deb25aafb3f9f00909c86655639b822b98dbe931149` |
| 2 | `main_round2.pdf` | 3 | 160,328 | 19 | `fa189eb25322876c2114408e738ddcae400e3286258c1bf914eb385e985ff44c` |
| final | `main.pdf` | 3 | 160,328 | 19 | `fa189eb25322876c2114408e738ddcae400e3286258c1bf914eb385e985ff44c` |

Round 0 proves normalization and primitive periods. Round 1 adds arbitrary
fixed times, Morse--Bott kernels, transverse return and exceptional indices.
Round 2 adds the Seifert quotient, the explicit two-normal-direction
principal RS derivation and Milnor capping convention, sign theorem, finite
receipt, limitations, and Route-A closure.
