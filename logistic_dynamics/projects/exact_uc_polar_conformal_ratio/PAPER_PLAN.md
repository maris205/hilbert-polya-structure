# Paper plan — explicit conformal ratios for LOG-0001

## One-sentence contribution

For the unchanged exact-\(U_c\) polar Fredholm determinant, an elementary
hyperbolic path theorem makes the two normalized stadium restriction ratios
explicit and yields certified numerical constants in the existing quadratic
growth envelope.

## Claim--evidence matrix

| Claim | Evidence | Boundary |
|---|---|---|
| The two normalized restriction ratios have one explicit upper bound. | Domain monotonicity of the curvature-`-1` Poincare metric, an interval path of cost `500*pi`, a disk path of cost `log(4)`, and normalized Riemann-map isometry. | The exact conformal ratio is not computed. |
| The gap below one is rigorously resolved. | Stable formulas through `t=exp(-D_*)` and 4096-bit outward Arb arithmetic. | Ordinary floating point is explicitly excluded. |
| The same determinant has fully numerical quadratic-growth constants. | The inherited two-stream coefficient bound, `1-r_*` denominator control, elementary logarithmic inequalities, and a shifted-Gaussian lattice sum. | The constants are upper bounds, not the true type or a lower-growth theorem. |

## Fixed outline

1. Abstract
2. Frozen determinant and theorem
3. Hyperbolic stadium path bound
4. Explicit two-stream coefficient majorant
5. Certified constants and reproducibility
6. Limitations and conclusion
7. Proof appendix

## Reproducibility boundary

The certificate evaluates only exact frozen geometry and outward scalar Arb
intervals.  It does not run a conformal solver, evaluate the determinant,
search for roots, or read prime, Riemann-zero, zeta, xi, or USTC data.

