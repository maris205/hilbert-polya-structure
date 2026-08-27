# C202 claim-driven validation plan

## Analytic claim

Prove one all-speed theorem for the complete Fisher--KPP traveling-wave ODE,
not five numerical slices.  The proof obligations are normalization, the
critical/supercritical trapping triangle, unstable-manifold uniqueness,
reflection, subcritical focus obstruction, the `c=0` Hamiltonian boundary,
energy/divergence identities, and all three leading-edge asymptotics.

## Deterministic regression

- classify 17 rational dimensionless speeds from `-4` through `4`;
- recompute 340 exact vector-field, energy and divergence rows;
- test 25 supercritical/critical trapping-boundary rows;
- reconstruct six bounded Hamiltonian oval components by independent root
  bracketing;
- verify nine exact Ablowitz--Zeppetella samples;
- test six physical `(D,r)` scalings.

The producer uses exact fractions and `mpmath`; the checker imports no
producer code and uses `Fraction`, `Decimal.sqrt` and its own bisection.  A
third SymPy path proves the structural polynomial identities.  Byte replay,
recursive schema closure and repaired-hash mutations complete the executable
boundary.

## Paper and release gates

Round 0 freezes the model and closes the positive-speed trapping theorem.
Round 1 adds reflected/subcritical/stationary regimes and all asymptotics.
Round 2 adds the exact control, evidence ledger, source ownership, declarations
and strict Route-A stop.  All three PDF hashes must differ; final must equal
round 2; two fixed-epoch fresh builds must be byte-identical.  The release has
exactly 27 manifest payload files plus its self-excluded manifest.
