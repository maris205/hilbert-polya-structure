# P26 pipeline state

Date: **2026-08-28**

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
| Round-4 exact ledger | **PASS** — 385 branch gluings, 320 eta coefficient identities, 138 closed cycle-owner instances, all primitive-certified; global cross-instance conjugacy deduplication not run |
| Round-4 numerical ledger | **PASS / NUMERICAL_OBSERVATION** — 55 complex period sums; maximum primary residual `2.229752420147902e-14` |
| Round-4 same-owner control | **PROVED / PASS_BY_GENUS_ONE_COHOMOLOGY** — all compactly extending closed real 1-forms obey the same scalar relation |
| Discriminative Hecke/Euler evidence | **STOP_SCOPED** — the cohomological relation does not select a primitive Euler mechanism |
| Primitive Euler factorization | **NOT ESTABLISHED** — correspondence output is a finite cycle sum, not one primitive owner |
| Round-4 reproducibility | **REPRODUCIBLE** — 8/8 tests; two byte-identical runs; tree SHA-256 `4cd45da8e7fa82e4688bc6975dae44c4206837b40652979167432ffe7b07f20e` |
| Round-5 log-zeta convention | **FROZEN** — reciprocal oriented primitive Ruelle product and reciprocal frozen-stability Selberg-type product; switching reciprocal convention only flips derivative sign |
| Round-5 primitive/repetition variation | **PROVED** — the `rI` period variation cancels the log-series `1/r`; Hecke cycle degree `d` remains distinct from zeta repetition `r` |
| Canonical inverse-paired first variation | **PROVED / EXACT ZERO** — inverse primitive flow orbits have equal length and opposite real 1-form period |
| Hecke degree-moment criterion | **PROVED** — a naive all-`s` recurrence on the finite output multiset is equivalent to `P_1=a_p I(M)` and `P_d=0` for every `d>1` |
| Hecke period relation implies zeta recurrence | **FALSE / NON-IMPLICATION PROVED** — Round 4 supplies only the unweighted sum `sum_d P_d=a_p I(M)` |
| Round-5 finite ledger | **PASS WITH NEGATIVE RESULT** — 1,104 orientation/repetition rows, 110 degree-moment rows, 165 one-sided zeta rows; 38 mixed and 17 uniform-nonunit degree groups |
| Round-5 weighted observations | **NUMERICAL_OBSERVATION** — 51/55 alpha groups violate all-`s` moments; 153/165 naive Ruelle and 153/165 naive frozen-Selberg rows fail |
| Round-5 same-owner control | **PROVED ZERO CANONICALLY / 53 OF 55 ONE-SIDED GROUPS FAIL MOMENTS** — the control does not rescue discriminative evidence |
| Round-5 reproducibility | **REPRODUCIBLE** — 11/11 tests; two byte-identical runs; tree SHA-256 `7b21a0c25ee269d28b53cd8c0551c8b2a977307641c2d07be78810be2e975731` |
| Round-6 inverse-pair second variation | **PROVED / ORIENTATION-EVEN** — inverse contributions add as `2s^2 I^2 sum_r r exp(-srL)`, with the frozen stability denominator in the Selberg-type kernel |
| Round-6 quadratic moment criterion | **PROVED** — any predeclared `p`-only scalar all-`s` law on the finite output multiset is equivalent to `Q_1=lambda_p I(M)^2`, `Q_d=0` for `d>1` |
| Round-6 primary finite audits | **PASS WITH NEGATIVE RESULT / NUMERICAL_OBSERVATION** — `a_p` and `a_p^2` each fail 51/55 group moments and 153/165 rows per kernel; four `p=5` groups survive numerically only |
| Round-6 secondary control | **NEGATIVE CONTROL ONLY** — `a_p^2-p` fails 55/55 groups and 165/165 rows per kernel |
| Round-6 scope | **FINITE/LOCAL ONLY** — 552 inverse-pair/repetition rows, 110 moment rows, 165 weighted rows; no complete primitive enumeration, global continuation, determinant root count, or zero comparison |
| Round-6 reproducibility | **REPRODUCIBLE** — 12/12 tests; two byte-identical runs; tree SHA-256 `fc553aa18bc4fb54d70ea8f4c0bdbc41efc3c0905b3f2942c49e1f6f8c62f864` |
| Proposal stage | Stage 1 / Route A A0--A1 |
| Formal Route-A tuple | **`(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)`** |
| Overall Route-A status | **`ROUTE_A_EXPLORATORY`** — no promotion |
| Route-A A2 evaluation | **FAIL / NOT_TESTABLE** — no formal A2 campaign; only the finite/local variation audit ran |
| Route-B evaluation | NOT RUN |
| Route-B invocation allowed | `false` |
| Manuscript | NOT STARTED |

The positive-word ledger is finite and is not a complete `Gamma_0(11)`
conjugacy-class certificate. The Hecke correspondence-cycle relation is now
`PROVED`, but its use as discriminative primitive-Euler evidence is
`STOP_SCOPED`; no target-prime grouping or zero data were used.

Round 5 closes the prior next gate: the sum-valued correspondence enters only
through an unweighted period identity, whereas zeta variation uses
owner-length kernels.  The complete oriented first variation is exactly zero;
the one-sided audit is noncanonical and requires additional degree moments
that are not implied by Hecke homology.  Round 6 answers the smallest
orientation-even question: the intrinsic inverse-pair second variation is
nonzero in general, but a scalar Hecke law requires new quadratic moments and
fails in 51/55 frozen groups for both primary scalars.  The four numerical
`p=5` survivors require exact homology certification before any stronger local
claim.  The formal evaluation remains exploratory, A2 is `FAIL/NOT_TESTABLE`,
and Route B remains disallowed.
