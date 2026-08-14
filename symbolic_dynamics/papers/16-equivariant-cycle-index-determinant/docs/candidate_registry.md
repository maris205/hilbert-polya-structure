# SD-C18 Candidate Registry

## SD-C18 — Character-resolved cycle-index ledger

- **Family:** Symbolic Dynamics only.
- **Source:** tensor-indecomposable finite full shifts, with entropy variables
  `x_p=exp(-s h(F_p))` used only after the formal multivariable object is
  fixed.
- **Phase space:** the one-vertex full edge shift on nonempty subsets of a
  finite tensor-atom set.
- **Scalar weight:** `epsilon(S)x_S=(-1)^(|S|+1) product_(p in S)x_p`, with
  ordinary temporal powers.
- **Primary refinement:** the signed primitive-cycle class in completed
  Burnside/representation/cycle-index ledgers under atom relabeling, with a
  `C_2` character line carrying scalar sign powers through Adams operations.
- **First residual:** at squarefree content `pqr`,

  ```text
  [S3/S3] + [S3/C3] - [S3/C2],
  character = (0,0,3),
  marks = (0,0,3,1).
  ```

- **Exact finite evidence:** squarefree primitive-cycle totals for `n=2..7`
  are `2,6,26,150,1082,9366`; scalar dimensions cancel, while nontrivial
  character values persist through `S_7`.
- **Fixed-fiber failure:** distinct arithmetic weights have trivial
  permutation stabilizer. Equal weights restore `S_n` symmetry, but the
  rank-one transfer has no nonzero eigenvalue in a nontrivial isotype.
- **Power-ledger failure:** the rank-one shadow has ghosts `b(x)^r`; the
  canonical diagonal subset lift has `b(x^r)`. In all 56 frozen rows the
  witness coefficient is `r` versus `0` for `r>=2`.
- **Determinant failure:** the diagonal superdeterminant contains mixed-subset
  factors and differs from the pure Euler determinant for every frozen
  `n=2..8`.
- **Analytic boundary:** on the raw infinite subset space,
  `D_s in S_q` exactly when `q Re(s)>1`; this belongs to the mixed-subset
  diagonal object, not the pure Euler shadow.
- **Controls:** 455/455 formal, prime, composite-only, shuffled-prime, and
  random-rational rows reproduce the finite identities and no-go results.
  Verdict: `STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.
- **Scalar-shadow firewall:** Paper 14's scalar A2 determinant is an inherited
  shadow only. It is not the character-resolved SD-C18 determinant and cannot
  be spliced into this candidate's route tuple.
- **Route tuple:**

  ```text
  (A0_ANALYTIC_ARITHMETIC_ORIGIN,
   A1_WEAK,
   A2_FAIL,
   A3_FAIL,
   A4_FAIL)
  ```

- **Overall:** `ROUTE_A_REJECTED`; `ROUTE_B_LOCKED`.
- **Latest evaluation:**
  `evaluations/route_a/SD-C18/20260814T050107Z.yaml`.
