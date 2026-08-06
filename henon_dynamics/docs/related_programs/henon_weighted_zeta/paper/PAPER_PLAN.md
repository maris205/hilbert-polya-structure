# Paper 3 working manuscript plan

## Working title

**Weighted Cycle Expansions and Finite-Resolution Spectral Audits for a Reversible Area-Preserving Hénon Map**

## One-sentence contribution

For an explicitly certified four-h-set survivor of the reversible map
\(H_6(x,y)=(1-6x^2-y,x)\), we combine an exact symbolic/contraction result with
independent finite-volume operator checks and a preregistered common-finest-cloud
audit; the new audit separates a small direct/common spectral-gap component from a
mixed dyadic-smoothing result. A post-freeze metric audit shows that the formal
localization gate measures target occupancy/support; internal target-cell phase
remains unresolved.

## Claim/evidence boundary

| Claim | Evidence | Status |
|---|---|---|
| Area preservation, reversibility, reciprocal multipliers | analytic identities | theorem |
| Four-h-set survivor and exact symbolic entropy | R059 contraction audit | theorem, local survivor only |
| Restricted periodic catalogue bridge | R059 high-precision catalogue | numerical confirmation, not global completeness |
| Finite-volume operator window | R059--R060 matrices, residuals, independent checkers | finite-resolution numerical evidence |
| Common-cloud sensitivity | R061 CSR projection and q-order control | mixed finite-resolution audit; coupling is confounded by effective budget |
| Row localization | frozen G2 plus post-freeze metric audit | occupancy/support association; cell-boundary phase unresolved |
| Continuous operator/global-zeta/Riemann claims | no certificate | explicitly out of scope |

## Sections

1. Introduction and contribution map.
2. Related work: reversible maps, dynamical zeta, hyperbolic transfer operators,
   Ulam approximation, and spectral-pollution diagnostics.
3. Geometry, reversibility, and the certified four-h-set survivor.
4. Weighted cycle expansions and conditional determinant language.
5. Periodic-orbit catalogue and independent restricted-operator construction.
6. Operator cross-check and sensitivity, including R060 and the R061 common-cloud
   coarsening/row-localization audit.
7. Discussion, limitations, reproducibility, and conclusion.
8. Appendix: a complete exact proof of transition exclusion, signed-recurrence
   contraction, conjugacy, primitive-necklace correspondence, entropy, and
   two-sided cone hyperbolicity; plus the gate ledger, hashes, and full R061
   tables.

## R061 subsection map

- Frozen parent chains and common-cloud projection formula.
- Direct/common leading-modulus gaps.
- Dyadic contrast \(D=\Delta_{\rm final}-\Delta_{\rm first}\).
- Row energy \(E_i=\tfrac12\lVert D_i-C_i\rVert_1\), formal occupancy association,
  and conditional lower-threshold sensitivity.
- Common q=8/q=12 quadrature control.
- Effective-budget caveat and anti-claims.

## Planned figures/tables

- Fig. 1: map/reversor/open-domain schematic (manual TikZ or schematic PDF).
- Fig. 2: R059 weighted-cycle cutoff convergence.
- Fig. 3: direct/common spectral-gap medians by chain and budget.
- Fig. 4: dyadic \(D\) comparison, direct versus common.
- Fig. 5: localization-metric degeneracy and conditional sensitivity.
- Fig. 6: q=8/q=12 common control.
- Tables 1--2: theorem and protocol ledger.
- Tables 3--5: R061 gaps, dyadic contrasts, and localization summaries.

## Current drafting rule

The manuscript is an internal, non-anonymous working draft. All claims are
phrased at the strongest level supported by the frozen ledgers; R059 G4 remains
negative, and no result is described as a continuous limit or a global Hénon
zeta theorem.
