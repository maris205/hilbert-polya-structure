# P26 pipeline state

Date: **2026-08-27**

| Item | Status |
|---|---|
| ARS Stage 1 | **IN PROGRESS** |
| Continuous-time object | **FROZEN** — positive time change of `Gamma_0(11)` geodesic flow |
| Arithmetic owner | **FROZEN** — real level-11 newform differential |
| Time-density / speed multiplier | **MODELING_CHOICE / FROZEN** — `rho_epsilon` / `1/rho_epsilon` |
| Generator | **MODELING_CHOICE / FROZEN** — `X_geo/rho_epsilon` |
| Positivity interval | **PROVED** — `|epsilon|<||a||_infinity^(-1)` |
| Primitive period variation | **PROVED** — length plus newform period |
| Bold hypothesis | **HEURISTIC** — exact Hecke/Euler decomposition |
| Round-2 finite ledger | **NUMERICALLY_CERTIFIED** — 125 primitive positive necklaces, 11 satisfying `c=0 mod 11`, cutoff 9 |
| One-form period proxy | **NUMERICAL_OBSERVATION** — q-series axis quadrature with independent stability checks |
| First kill controls | **EXECUTED / NUMERICAL_OBSERVATION** — bounded invariant generic observable, permutation, and simpler-parent length control |
| Reproducibility | **REPRODUCIBLE** — 7/7 tests; two byte-identical runs; tree SHA-256 `e635ee051ea25d543eb4f3fd72bce5ae4da95d64ee2ca9f90b2f5f81ba8a2da5` |
| Round-3 period owner | **PROVED** — oriented `Gamma_0(11)` conjugacy invariant; inverse orientation changes sign; repetition is linear |
| Round-3 finite regression | **PASS** — 99 exact conjugacy rows, 44 translation-covariance rows, maximum observed residual `1.5543122344752192e-15` |
| Round-3 reproducibility | **REPRODUCIBLE** — 5/5 tests; two byte-identical runs; tree SHA-256 `a3e71f86124ec8ae58f3971002fd3e0f11a0f06ccf3851e1f4ed4fad25d03841` |
| Round-4 Hecke owner | **PROVED** — `integral_(T_(p,*)C) alpha_f = a_p integral_C alpha_f` on the correctly normalized cycle pushforward |
| Round-4 exact ledger | **PASS** — 385 branch gluings, 320 eta coefficient identities, 138 closed cycle owners, all 138 finite owners primitive-certified |
| Round-4 numerical ledger | **PASS / NUMERICAL_OBSERVATION** — 55 complex period sums; maximum primary residual `2.229752420147902e-14` |
| Round-4 same-owner control | **PROVED / PASS_BY_GENUS_ONE_COHOMOLOGY** — all compactly extending closed real 1-forms obey the same scalar relation |
| Discriminative Hecke/Euler evidence | **STOP_SCOPED** — the cohomological relation does not select a primitive Euler mechanism |
| Primitive Euler factorization | **NOT ESTABLISHED** — correspondence output is a finite cycle sum, not one primitive owner |
| Round-4 reproducibility | **REPRODUCIBLE** — 8/8 tests; two byte-identical runs; tree SHA-256 `4cd45da8e7fa82e4688bc6975dae44c4206837b40652979167432ffe7b07f20e` |
| Proposal stage | Stage 1 / Route A A0--A1 |
| Formal Route-A tuple | UNASSIGNED |
| Route-A A2 evaluation | NOT RUN |
| Route-B evaluation | NOT RUN |
| Route-B invocation allowed | `false` |
| Manuscript | NOT STARTED |

The positive-word ledger is finite and is not a complete `Gamma_0(11)`
conjugacy-class certificate. The Hecke correspondence-cycle relation is now
`PROVED`, but its use as discriminative primitive-Euler evidence is
`STOP_SCOPED`; no target-prime grouping or zero data were used.

Next gate: derive the smallest exact algebra showing how the **sum-valued**
correspondence enters the first variation of a frozen dynamical zeta while
preserving primitive/repetition ownership, or prove that no primitive Euler
factorization follows from this genus-one cohomological identity. No formal
Route-A tuple is assigned, A2 remains unrun, and Route B remains disallowed.
