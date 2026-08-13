# Candidate Registry

## SD-C09 — entropy-oriented anticommutator successor shift

- Family: **Symbolic Dynamics**, exclusively.
- Atom source: tensor-indecomposable finite full shifts, generated internally.
- Intrinsic order/clock: increasing entropy `log(p)`.
- Transfer:

  \[
  D_se_n=p_n^{-s}e_n,\qquad
  L_s=D_s+\frac{D_sS+SD_s}{2}.
  \]

- Periodic grammar: one pure loop at every atom plus forward successor edges;
  no successor edge occurs in a closed word.
- Euler convention: `det(I-zL_s)` on `Re(s)>1`.
- Critical-axis scalar: `det(I-L_t^*L_t)` at `s=1/2+it`.
- Chiral convention: `B_t=[[0,L_t],[L_t^*,0]]`; finite `det_3` has the same
  `z=1` roots because its multiplier is strictly positive.
- Parameters: no fitted phase, scale, offset, adjacency, or boundary condition.
- Data firewall: no Riemann-zero data and no target-root comparison.

### Exact accomplishments

1. `Tr L_s^r=sum_p p^(-rs)` and
   `det(I-zL_s)=product_p(1-zp^(-s))` on the honest Euler half-plane.
2. Successor edges mix unequal entropy masses but create no mixed periodic
   word.
3. The one-sided ansatz `D_(1/2+it)K` is gauge-trivial for arbitrary `K`.
4. The endpoint average has strict Schatten-fourth/singular motion, whereas
   source-only and target-only endpoints have none.
5. The two-atom crossing formula is exact.

### Numerical benchmark

For `N=2,3,4,8,16,32,64,128`, frozen-grid positive sign-change counts of
`det(I-L_t^*L_t)` are respectively `3,5,11,21,41` in windows
`T=20,40,80,160,320`.  The result is stable under grid-step halving but is
not an argument-principle certification and is not compared with target
zeros.

### Specificity boundary

Shuffled atoms, composites, random integers, randomized forward endpoint
phases, and all 24 random upper-DAG controls retain the same triangular
ledger while showing spectral motion.  The mechanism is therefore
`PROVES_TOO_MUCH` as an RH-divisor criterion.  Reverse edges create mixed
cycles and fail the ledger at power two.

### Route status

```text
(A0_ANALYTIC_ARITHMETIC_ORIGIN,
 A1_PASS_ANALYTIC,
 A2_ANALYTIC_DETERMINANT,
 A3_PARTIAL_ANALYTIC_STRUCTURE,
 A4_FORMAL_HINT)

ROUTE_A_ANALYTIC_CANDIDATE
GO_A3_CHIRAL_MOTION / STOP_UNIFIED_DIVISOR
route_b_invocation_allowed: false
```

Canonical evaluation:
`evaluations/route_a/SD-C09/20260813T235900Z.yaml`.

