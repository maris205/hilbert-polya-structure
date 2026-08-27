# Exact regression experiment plan

## Claim-to-test map

| Analytic claim | Finite sentinel | What the sentinel cannot prove |
|---|---|---|
| Cole--Hopf converts drift--heat to Burgers | exact Laurent numerator after clearing \(w^3\) | the all-function Sobolev conjugacy |
| positive projective heat cone is invariant | exact conservative L1 margins before/after snapshots | positivity for every positive function |
| physical-time dynamics is a semigroup | two algebraic heat/drift steps equal one composed step | global PDE well-posedness |
| first active lift mode sets leading decay | exact leading coefficients, gap, and remainder exponent | asymptotics for arbitrary infinite Fourier tails |
| linearized spectrum is explicit | modes \(-8\le k\le8\) in all 24 cases | spectral completeness |

## Deterministic census

- Normalize only the oracle to \(L=2\pi\); the theorem retains every \(L>0\).
- Use 24 real Hermitian Laurent polynomials with degrees, gaps, viscosities, and means
  chosen by fixed formulas in the producer.
- Enforce strict positivity by the exact sufficient bound
  \(a_0-2\sum_{k>0}(|\Re a_k|+|\Im a_k|)>0\).
- Represent a drift--heat snapshot by rational data \(\rho\in(0,1)\) and a rational
  unit-circle phase \(\zeta\), acting as \(a_k\mapsto a_k\rho^{k^2}\zeta^k\).
  This probes the universal commuting heat/translation multiplier. The physical
  one-parameter curve is \(\rho=e^{-\nu t},\zeta=e^{-imt}\); an exact rational
  sentinel is not claimed to lie on that curve.
- Store canonical JSON with a semantic payload hash.

## Validation layers

1. Producer generates the deterministic certificate.
2. Checker independently regenerates all cases and identities without importing the
   producer.
3. SymPy independently expands nine representative Laurent identities.
4. Replay regenerates and compares every evidence byte.
5. Mutation tests repair the semantic hash after 22 adversarial changes and require
   every change to be rejected; one stale-hash mutation tests hash enforcement.
6. The paper is compiled at a fixed epoch in three content-distinct revisions; the
   final version is rebuilt twice in fresh directories and audited for byte identity,
   embedded fonts, clean logs, extractable text, and every rendered page.

## Stop conditions

Any incorrect sign, nonpositive margin, nonzero residual, mismatched semigroup step,
wrong leading gap, surviving semantic mutation, nondeterministic final PDF, missing
font embedding, layout warning, manifest mismatch, or scope expansion blocks release.
