# PREREGISTRATION — Paper 14

## Frozen date and candidate

- Date: 2026-08-14.
- Candidate: `SD-C16`, the reduced tensor bar-code one-vertex countable
  signed edge shift.
- Primary family: Symbolic Dynamics only.
- Riemann-zero data: prohibited.
- Route B: prohibited.

## Questions fixed before the final run

1. Can a functorial abelian charge be nontrivial on a tensor atom while
   vanishing on every composite object?
2. Can a coherent tensor-divisor cocycle supply non-gauge character
   dependence?
3. Does the reduced tensor bar-code shift have an honest same-object
   determinant in an explicitly proved convergence domain?
4. Is the tensor Mangoldt profile an output of the entropy roof derivative,
   rather than an inserted weight?
5. Does the construction distinguish the arithmetic full-shift inventory
   from generic weighted inventories?

## Analytic predictions

The following are theorem predictions and are not fitted to data.

- For every abelian target, `2q(p)=3q(p)=0` implies `q(p)=0`.
- Every thin divisor-category cocycle is `kappa(d,n)=b(n)-b(d)`.
- Pure presentation shuffles leave all functorial spectra, traces, and
  determinants invariant.
- With `B(s)=zeta(s)-1`, raw bar convergence occurs exactly when
  `B(Re(s))<1`; on the real axis the boundary is
  `sigma_bar=1.7286472389981836181...`.
- For `Re(s)>sigma_bar`, `F_bar=B/(1+B)` and
  `D_bar(s,1)=1/zeta(s)`.
- Endpoint coefficients equal `-mu_tensor(n)` exactly and give an
  incidence-completed series for `Re(s)>1`.
- The roof derivative coefficient is `Lambda_tensor=mu_tensor*h`:
  prime powers are positive and mixed-factor composites vanish.
- Every generic inventory control also obeys
  `D_X=1/(1+B_X)`, which counts against arithmetic selectivity.

## Numerical audit matrix

### Local character and grammar audit

- Parameters: `s=2`, `z=1/3`.
- Cutoffs: `N in {16,32,64,128}`.
- Presentation shuffles: 16 deterministic seeds.
- Random grammar controls: 16 deterministic seeds.
- Named local rules: 18.
- Exhaustive binary radius-one truth tables: 256.
- One- and two-state Mealy rules: 260.

The purpose is to falsify local character escapes, not to discover a fitted
rule.  Pure shuffles must remain invariant; random rewiring is a distinct
grammar control.

### Global tensor incidence audit

- Endpoint cutoffs: `X in {64,128,256,512}`.
- Entropy relabel controls: 8 deterministic seeds.
- Exact integer endpoint coefficients are computed before any floating
  evaluation.
- Prime powers and composites with at least two distinct atoms are reported
  as separate strata.

### Bar-code audit

- Raw word-length truncation:
  `F_L=sum_{ell<=L}(-1)^(ell+1)(zeta(s)-1)^ell`.
- Raw test points are restricted to `Re(s)>sigma_bar`.
- At `s=2`, the geometric tail is evaluated exactly from
  `B(2)=pi^2/6-1` and compared with high-precision residuals.
- Endpoint-first grouped coefficients are tested independently for
  `1<Re(s)<=sigma_bar` and are never labeled raw convergence.
- Trace-log repetitions are tested only where `|zF|<1`.
- Generic controls include composite-only, randomized increasing, and
  synthetic positive inventories.

## Decision rules

```text
GO_FUNCTORIAL_COCYCLE_RIGIDITY
  if the exact algebraic certificates and every finite implementation agree.

GO_TENSOR_MOBIUS_INCIDENCE_DETERMINANT
  if endpoint coefficients, raw-domain determinant, grouped completion,
  and roof derivative all agree in their separately declared domains.

STOP_PRIME_EXCLUSIVE_ABELIAN_CHARACTER
  follows analytically from the p^2/p^3 obstruction.

STOP_SHUFFLE_COLLAPSE
  follows from functorial conjugacy under pure relabeling.

STOP_ORBITWISE_PRIME_CORRESPONDENCE
  unless a primitive-cycle quotient is proved before the trace-log.

STOP_ARITHMETIC_SELECTIVITY / PROVES_TOO_MUCH
  if the identical inversion succeeds on generic inventories.
```

No numerical residual can upgrade Route A.  The route decision is based on
the frozen object and theorem content.
