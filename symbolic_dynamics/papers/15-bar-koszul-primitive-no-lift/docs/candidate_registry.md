# SD-C17 Candidate Registry

## SD-C17 — Tensor-atom squarefree subset shift

- **Family:** Symbolic Dynamics only.
- **Source:** a finite set of tensor-indecomposable full shifts, with tensor
  entropy variables `x_p=exp(-s h(F_p))` available only as a specialization
  of the formal-variable object.
- **Phase space:** one-vertex finite full edge shift whose edges are nonempty
  squarefree subsets of the frozen atom set.
- **Weight:** ordinary scalar
  `epsilon(S)x_S=(-1)^(|S|+1) product_(p in S)x_p`.
- **Primitive convention:** cyclic necklaces modulo rotation only;
  reflection is not quotiented.
- **Repetition convention:** actual scalar powers `w(gamma)^r/r`.
- **Determinant:**

  ```text
  D_k(x,z)=1-z sum_(S nonempty) epsilon(S)x_S,
  D_k(x,1)=product_p(1-x_p).
  ```

- **Strongest positive:** exact finite scalar Koszul determinant and exact
  cancellation of every mixed squarefree log coefficient.
- **Primitive failure:** at `p^2q^2`, target primitives have signed count
  `1-2=-1`; the zero full coefficient needs two lower-degree `r=2` terms.
- **Naturality failure:** at `pqr`, the virtual `S_3` character is
  `(0,0,3)=1+sign-standard`.
- **Parity firewall:** scalar `(-w)^r` is not odd supertrace `-w^r`; a genuine
  contractible two-term block has a different primitive ledger.
- **Control verdict:** 112/112 arbitrary rational inventories pass exactly;
  `STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH`.
- **Route tuple:**

  ```text
  (A0_ANALYTIC_ARITHMETIC_ORIGIN,
   A1_FAIL,
   A2_ANALYTIC_DETERMINANT,
   A3_FAIL,
   A4_FAIL)
  ```

- **Overall:** `ROUTE_A_REJECTED`; `ROUTE_B_LOCKED`.
- **Latest evaluation:**
  `evaluations/route_a/SD-C17/20260814T043738Z.yaml`.
