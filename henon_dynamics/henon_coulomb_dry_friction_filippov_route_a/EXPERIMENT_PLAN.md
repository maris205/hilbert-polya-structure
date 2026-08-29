# Deterministic experiment and audit plan

## Frozen rows

Eight rest starts cover one-step, threshold, multi-half-cycle, negative, and
already-sticking cases.  Eight arbitrary signed initial states cover both
constant-force centers and a partial first slip arc.  Five zero-velocity rows
cover the static interval, both thresholds, and both release directions.  Four
harmonic rows cover `c=0`; five energy rows check the work drop on a first
sliding arc.

## Independent computation

All inputs are rational.  Exact Fraction arithmetic determines
\(a_f=c/\omega^2\), turning maps, and integer ceilings.  `mpmath` at 90
digits evaluates only square roots, `atan2`, trigonometric phases and times.
The checker reimplements these formulas independently and uses no producer
imports.  SymPy verifies both slip energy identities, threshold signs,
half-cycle maps, radius/center formulas, and the harmonic solution.

## Adversarial controls

Byte replay compares two fresh producer outputs.  Twenty-eight hostile mutations
include stale and repaired hashes, center-sign/phase and partial-arc fields,
turning points, energies, counts, release regimes, harmonic values, forward-
time well-posedness, the positive-friction capture hypothesis, route and scope
flags, and unknown keys.  Any accepted mutant or stopping turn outside
the static interval fails the release.

The finite receipt is implementation evidence, not an external mechanical
experiment and not a primitive-orbit census.
