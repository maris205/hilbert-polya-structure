# C186 exact-verification plan

## Claim-driven tests

1. Generate exact rational sentinels for six strictly triaxial inertia triples, three angular-momentum magnitudes, five positions in each of the two regular energy regimes: 180 rows total.
2. In every row reconstruct the three amplitude squares, Jacobi modulus, frequency, sphere constraint, energy constraint, and all three Euler-equation coefficient identities using `Fraction` arithmetic.
3. Independently evaluate the common \(4K/\Omega\) period and KKS cap-action quadrature to 62 recorded digits.
4. Cover every axial linearization type, every separatrix normalization, both stable small-oscillation limits, and monotone divergence sentinels from both sides of \(e=b\).
5. Run a producer-independent checker, a separate symbolic derivation, canonical byte replay, 18 repaired-hash semantic mutations, and one stale-hash mutation.

## Interpretation

Exact finite rows detect normalization, branch, and sign errors. The proof in `THEOREM_PACKAGE.md` establishes the infinite family. No numerical integration or parameter fitting is used; no experiment is reported as proof.

## Release gates

The paper must have three content-distinct rounds, a fixed-epoch byte-identical double build, embedded fonts, no unresolved references or layout warnings, rendered-page inspection, and a 27-payload self-excluded manifest.
