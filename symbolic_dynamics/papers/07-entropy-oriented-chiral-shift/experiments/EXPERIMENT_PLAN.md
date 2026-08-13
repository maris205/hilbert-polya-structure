# SD-C09 Frozen Experiment Plan

## Source lock

The only promoted system is the entropy-ordered tensor-atom symbolic shift

\[
D_s=\operatorname{diag}(p_n^{-s}),\qquad
L_{\alpha,s}=D_s+\alpha D_sS+(1-\alpha)SD_s,
\]

with the candidate value `alpha=1/2`.  Multiplicative indecomposables are
generated internally; no prime file, Riemann-zero file, target loss, fitted
scale, or fitted offset is allowed.

## Exact tests

1. Verify opaque-variable trace powers through `r=8` and the determinant
   product symbolically.
2. Census all based closed walks through length 8 and require that every
   closed walk is a pure loop.
3. Add reverse successor edges and require the mixed-cycle ledger failure to
   appear at power two.
4. Verify the universal one-sided identity
   `D_(1/2+it)K=U_t D_(1/2)K` for a frozen random noncommuting `K`.
5. Compare `alpha=0,1/8,1/4,1/2,3/4,7/8,1`; endpoints are phase-gauge
   controls and the midpoint must show a nonconstant Schatten-fourth
   invariant.
6. Verify finite-dimensional conjugation/reflection, the block determinant
   identity, and the positive `det_3` multiplier.

## Frozen crossing census

The scalar is fixed before computation:

\[
f_N(t)=\det(I-(L_{1/2+it}^{(N)})^*L_{1/2+it}^{(N)}).
\]

- Cutoffs: `N=2,3,4,8,16,32,64,128`.
- Windows: `T=20,40,80,160,320`.
- Frozen grid step: `1/256`; validation step: `1/512`.
- Count only sign-changing brackets on `0<t<=T`; report doubled counts only
  as reflection counts.
- For `N=2`, compare with the exact crossing family.
- Do not compare any root with Riemann zeros.

This is a grid sign-change census, not an argument-principle certificate and
not a census of hypothetical even-multiplicity tangencies.

## Controls

- shuffled tensor atoms;
- composites only;
- matched-count random integers;
- randomized forward endpoint phases;
- 24 random upper-triangular DAGs;
- positive recurrent reverse-edge control;
- virtual-character radical, positive, random-signed, nilpotent, and
  truncated free-group controls.

The random-DAG and randomized-forward-phase mechanisms are preregistered as
`PROVES_TOO_MUCH` whenever they preserve the ledger and spectral motion.
