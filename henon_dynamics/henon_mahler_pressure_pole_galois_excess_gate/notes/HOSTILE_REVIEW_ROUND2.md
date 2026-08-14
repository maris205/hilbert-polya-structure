# Hostile review — round 2

Date: 2026-08-14

Artifact reviewed: revised LaTeX manuscript after round 1

Mode: independent theorem-boundary and source-normalization re-review

## Verdict

`PASS_WITH_SCOPE_FIREWALL`

No critical or major defect remains in the stated results.  The paper proves
an unconditional result only for the physical summand, and it never promotes
the Galois excess to a Hölder observable.

## Re-verification matrix

| Round-1 item | Verification | Result |
|---|---|---|
| M1: source parameter map | The manuscript now states `P(g-cf)=0`, the fixed-point zeta, and the choices `f=hat tau`, `g=0`, `c=1`, `k=psi`. | Resolved |
| M2: weighted repetition tail | The proof now uses `m(gamma) <= hat ell_gamma/min hat tau` and an absolute majorant. | Resolved |
| M3: `sigma_Gal=1` overstatement | The trichotomy now says the abscissa alone determines neither boundary convergence nor singularity data. | Resolved |
| m1: physical tail | A compact-half-plane Weierstrass majorant is explicit. | Resolved |
| m2: evaluator vocabulary | Exact Route-A labels are used, with A2 explicitly scoped to the physical subsystem. | Resolved |
| m3: executable locator | The one-command finite audit is printed in the paper. | Resolved |

## Second-round attacks

1. **Could the conditional excess residue cancel the physical pole?** No.
   The differentiated excess Euler series has nonnegative coefficients for
   real `s>1`; its residue is therefore nonnegative, while the physical
   residue is strictly positive.
2. **Does the source theorem prove continuation of the full P53 amplitude?**
   No, and the manuscript does not claim it.  The source attaches
   unconditionally only to the normalized suspension roof; its weighted
   version is invoked only under the exact Hölder periodic-sum hypothesis.
3. **Do three exact orbits prove the all-period pole?** No, and the manuscript
   explicitly separates the finite certificate from the source-backed
   all-period theorem.  The three rows certify only the cohomological no-go
   and arithmetic decomposition witnesses.
4. **Does `sigma_Gal>1` exclude analytic continuation?** No.  The manuscript
   now limits that case to failure of the positive defining series.

## Residual limitations (not defects)

- The local Hölder realization of the Galois excess remains `OPEN`.
- The excess abscissa is bounded only by the inherited P53 majorant.
- There is no rational-prime trace, completed divisor, or Route-B operator.
