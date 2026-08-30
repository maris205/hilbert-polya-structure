# Deterministic experiment and audit plan

## Frozen census

Use \(\lambda=1/2,2/3,3/4\) and enumerate every binary word of lengths
\(1\leq n\leq12\).  Keep exactly the primitive words that are
lexicographically minimal among their cyclic rotations: 747 words per slope,
2241 rows in all.  For each row, solve the affine return equation over
`Fraction`, intersect the state-domain and carry inequalities, and retain the
closed/open endpoint flags.  The producer currently records 138 nonempty
word-certified components and groups them by carry rotation number without
claiming maximality.

## Independent computation

The checker contains an independent implementation of word generation, affine
composition, interval intersection, endpoint equality evaluation, grouped
components, and a high-precision direct iteration.  It imports no producer
symbols.  The direct ledger uses eight base \(\delta\)-grid points and every
distinct endpoint, runs 360 iterations at 90 decimal digits, and compares the
last repeated suffix with the exact affine fixed point.  SymPy verifies the
generic composition, fixed-point, derivative, carry, and rational spot-check
identities.

## Adversarial controls

Byte replay compares two fresh producer outputs with the canonical evidence.
The hostile suite makes 33 repaired-hash mutations: word, carry, rotation,
derivative, affine states, lower/upper interval and openness, endpoint audits,
grouped components, direct suffix/point/residual fields, counts, source and
evaluator locks, epoch, scope firewall, Route-A tuple, target-match boundary,
theorem overclaims, and unknown keys.  Every changed receipt must be rejected.

This is exact implementation evidence at a finite cutoff.  It is not a claim
of global symbolic completeness, a maximal plateau classification, an external
numerical experiment, or a target arithmetic determinant.
