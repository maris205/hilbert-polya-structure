# Compilation report

- Engine: LuaLaTeX.
- Frozen epoch: `1788480000`.
- Procedure: two passes in each of two fresh directories for every revision
  round.
- Determinism: PASS for all three rounds.
- Settled LaTeX warnings: 0.
- Undefined references or citations: 0.
- Embedded/subset fonts: PASS for every font row.
- Extracted-text control-byte hygiene and full page rasterization: PASS.
- Unescaped `quad`/`qquad` source rejection and literal `qquad` PDF-text
  rejection: PASS.
- `main.pdf` equals `main_round2.pdf`: PASS.

| round | file | pages | bytes | font rows | SHA-256 |
|---:|---|---:|---:|---:|---|
| 0 | `main_round0_original.pdf` | 2 | 151,564 | 19 | `2d8a17ebec4a597baa419ae2078f8a2ecba2524c90d89593793b23554d774439` |
| 1 | `main_round1.pdf` | 3 | 170,415 | 20 | `820dcd69392bc88e9880ae7d6f019837961f5feed12c9ff5de96a308fb089058` |
| 2 | `main_round2.pdf` | 4 | 182,773 | 21 | `814d3b8a1cfdddc7d9b3c682cf73d5e6f4f8c3429d93c91b65da89e874df2e29` |
| final | `main.pdf` | 4 | 182,773 | 21 | `814d3b8a1cfdddc7d9b3c682cf73d5e6f4f8c3429d93c91b65da89e874df2e29` |

Round 0 proves the exact turning/action theorem, action Hamiltonian,
frequency-period lock, and complete classical face atlas. Round 1 adds the
Friedrichs operator, Jacobi eigenfunctions, directly counted multiplicity,
completeness, flat limit, and Dirichlet-hemisphere zero-coupling endpoint.
Round 2 adds the necessary-and-sufficient identity-revival theorem, proves the
global phase is one, and closes evidence, sources, collisions, limitations,
and Route-A scope.
