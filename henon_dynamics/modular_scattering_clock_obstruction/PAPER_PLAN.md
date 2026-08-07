# Paper plan and claim--evidence map

## Working title

**Modular Scattering Denominators Do Not Define Closed-Orbit Clocks**

Subtitle: **A Stable-Closure Obstruction for Dynamical-Zeta Constructions**

## One-sentence contribution

The modular cusp denominator produces the classical scattering zeta quotient,
but every nonzero total clock depending only on the final denominator violates
closed-orbit repetition, while its canonical stable homogenization is exactly
the Selberg hyperbolic length.

## Claims and evidence

| Claim | Status | Evidence |
|---|---|---|
| Oriented big-cell cusp double cosets at level \(c\) have multiplicity \(\varphi(c)\) | proved/classical | exact double-coset proof and finite audit through \(c=80\) |
| Their arithmetic series is \(\zeta(2s-1)/\zeta(2s)\) for \(\Re s>1\) | proved/classical | Euler product plus bounded-tail numerical regression |
| The full coefficient is \(\Lambda(2s-1)/\Lambda(2s)\) | classical input | Eisenstein constant term and physical-line numerical regression |
| Final denominator is not a closed conjugacy/cyclic invariant | proved | exact group and even Gauss-word witnesses |
| Any \(F(\alpha|c|)\) satisfying square repetition on all positive hyperbolic matrices is zero | proved/new compatibility theorem | positive \(\gamma_{m,n}\) family; no regularity assumption |
| \(c(g^n)=c(g)U_{n-1}(\operatorname{tr}g/2)\) | proved/classical | Cayley--Hamilton and 48 exact checks |
| Stable denominator height equals hyperbolic translation length | proved | exact Chebyshev expansion and high-precision regression |
| A standard closed Euler product cannot keep only final-denominator norms and standard repetitions | proved, scoped | corollary of the zero theorem |
| A zero-free source normalization cannot turn affine \(\Phi\) into one entire \(\xi\) | proved, scoped | divisor locations and no cross-cancellation |
| A Hilbert--Pólya operator follows | not claimed | Route-A stops before Route B |

## Section order

1. Introduction and the open/closed category error.
2. Modular scattering, double cosets, and the arithmetic clock.
3. Closed hyperbolic coding and exact cyclic witnesses.
4. The denominator-only repetition theorem.
5. Stable closure and return to Selberg length.
6. Consequences for Euler products, divisors, and Hilbert--Pólya claims.
7. Exact computational protocol and finite controls.
8. Limitations and next systems.
9. Appendix with full proofs and machine-readable schema.

## Proof versus computation

Every headline statement is proved symbolically.  Computation verifies frozen
instances, detects implementation drift, and reports finite Gauss-word
incidence.  No asymptotic or universal claim is inferred from the 274-word
census, and no Riemann-zero list is loaded.

## Red-line wording

Do not claim:

- that \(Pg^nP\) is the repeated open scattering channel associated with
  \(PgP\);
- that raw \(\varphi(c)\) always counts reversal-identified geometric
  scattering geodesics;
- that the bare zeta ratio is the full scattering coefficient;
- that stable translation length is the unique possible repair;
- that all cusp-derived, local, endpoint, cohomological, or word-dependent
  clocks are excluded;
- that scattering resonances are a discrete self-adjoint Hilbert--Pólya
  spectrum;
- external novelty for the classical modular formulas.

## Release figures and tables

No decorative figure is necessary.  The main paper should contain:

- one category-comparison table: open double cosets versus closed conjugacy
  classes;
- one theorem-flow table: arithmetic signal, repetition obstruction, stable
  closure, Route-A verdict;
- one compact reproducibility table containing the 274/259/0 word counts and
  exact-audit sizes.
