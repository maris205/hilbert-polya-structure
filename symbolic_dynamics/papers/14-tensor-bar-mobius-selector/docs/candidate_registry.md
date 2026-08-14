# SD-C16 Candidate Registry

## SD-C16 — Reduced tensor bar-code shift

- **Family:** Symbolic Dynamics only.
- **Source:** tensor monoid of finite full shifts
  `F_m tensor F_n = F_(mn)` with intrinsic entropy `h(F_n)=log n`.
- **Phase space:** one-vertex countable signed edge shift; an edge is a
  nonempty ordered word of nonunit tensor objects.
- **Raw operator:** scalar weighted adjacency `L_bar,s=F_bar(s)` on `C`.
- **Determinant:** `D_bar(s,z)=1-zF_bar(s)`.
- **Raw domain:** `Re(s)>sigma_bar`, where
  `sigma_bar=1.728647238998183618135103010297691...`.
- **Endpoint completion:** coefficient grouping gives
  `[n]F_bar=-mu_tensor(n)` and `D_bar(s,1)=1/zeta(s)` for `Re(s)>1`.
- **Canonical observable:** the frozen roof derivative gives
  `Lambda_tensor=mu_tensor*h`.
- **Primitive boundary:** primitive bar-code necklaces are ordered
  factorization histories, not tensor atoms or rational primes.
- **Control verdict:** universal inversion succeeds for every generic weighted
  inventory; `STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.
- **Route tuple:**

  ```text
  (A0_ANALYTIC_ARITHMETIC_ORIGIN,
   A1_WEAK,
   A2_ANALYTIC_DETERMINANT,
   A3_FAIL,
   A4_FAIL)
  ```

- **Overall:** `ROUTE_A_REJECTED`; `ROUTE_B_LOCKED`.
- **Latest evaluation:**
  `evaluations/route_a/SD-C16/20260814T040551Z.yaml`.

## Data-type separation

The Paper 13 local character family, the global tensor-incidence ledger, and
the SD-C16 bar determinant are distinct objects/readouts. SD-C16 derives its
incidence coefficients from its own ordered-word endpoint grouping; it does
not paste `Lambda_tensor` into the Paper 13 local operator.
