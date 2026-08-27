# Exact validation plan

## Claims and sentinels

| Claim | Proof owner | Executable path | Mutation target |
|---|---|---|---|
| nondimensional system | chain rule | symbolic scaling | change `kappa` |
| first integral | differentiation | SymPy Lie derivative | change log sign |
| peak and threshold | sign of `y'` | 24 exact starts | corrupt peak |
| final lower root | monotonicity + invariant | Lambert `W_0` producer | branch swap |
| upper companion | same level set | Decimal bisection checker | move below one |
| sensitivity | implicit differentiation | two symbolic/numeric paths | sign mutation |
| no recurrence | strict `R` monotonicity | literal theorem gate | promote A1 |

## Independent numerical paths

The producer uses `mpmath.lambertw` at high precision.  The checker never calls
Lambert W: it uses `Decimal` logarithms and 360 steps of monotone bisection on
each side of the minimum of `x-log x`.  SymPy independently derives invariant,
scaling, phase curve, peak, Jacobian and sensitivity identities, then tests
both reported roots by their defining equation.

## Grid

Eight exact susceptible ratios cross all three regimes; three positive
infected ratios give 24 cases.  Each retains lower and upper roots, peak,
residual and sensitivity.  Four rational `(beta,gamma)` pairs test the physical
scaling.  The infection-free boundary is proved separately and is not hidden
inside the positive grid.

## Integrity and release

Canonical byte replay, twelve repaired-hash semantic mutations, one stale-hash
attack, two substantive manuscript revisions, fixed-epoch double builds,
embedded fonts, clean logs and page-by-page visual inspection are mandatory.
Any branch, boundary, scope or hash failure stops release.
