# HCS-C275 compile report

All three manuscript stages were built with LuaLaTeX under
`SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`. Each stage
received two LuaLaTeX passes in each of two fresh temporary build directories.
The two fresh outputs were byte-identical at every stage.

| Stage | Pages | Bytes | SHA-256 |
|---|---:|---:|---|
| `main_round0_original.pdf` | 2 | 96148 | `67f59b377c1cd7a59e2c803a1db4811a7528e65381601eb7221df9a31c1173af` |
| `main_round1.pdf` | 2 | 138747 | `32d6033c240aebdd779d4b49963b48b60084aa732419532bd36324a21eb4e566` |
| `main_round2.pdf` | 3 | 151359 | `77b15baa296c7107990f36208099118e7186632a2fc075a3087d74989ec948a1` |
| `main.pdf` | 3 | 151359 | `77b15baa296c7107990f36208099118e7186632a2fc075a3087d74989ec948a1` |

The settled logs are warning-free: no LaTeX warning, overfull or underfull
box, undefined reference, multiply-defined label, or rerun request remains.
`pdffonts` reports 19 fonts; every font is embedded and subset. A rendered
three-page visual audit found no clipped equations, collisions, missing
glyphs, or unreadable material. The three revision PDFs have distinct hashes,
and `main.pdf` is byte-for-byte identical to the Round-2 PDF.

Round 0 establishes the confocal owner, Jacobi covering, and exact rotation
formula. Round 1 adds strict monotonicity, all four endpoint paths, and the
minimal-period Poncelet porism. Round 2 adds the unit restricted derivative,
clean periodic-family obstruction, 24 repaired-hash mutations, the ambient
Dirichlet formal hint with explicit same-clock and fixed-caustic
phase/weight failures, and the Route-A and elliptic-sector firewalls.
