# Experiment plan

## Claim-driven objectives

1. Verify the exact `H6`/Arai scaling and plateau inequalities.
2. Reconstruct all closure and primitive quotient polynomials through odd
   period 13 over `QQ`.
3. Certify by Sturm theory that every primitive root is real and simple.
4. Propagate rational root isolators through period 11 and verify unique
   symbolic half-itineraries.
5. Independently enumerate full-shift fixed and primitive words through
   period 13.
6. Reject mutations of the theorem chain, degree laws, statuses, and claim
   boundary.

## Stop conditions

- Any root multiplicity greater than one or nonreal root count stops the
  effectivity claim.
- Any mismatch between `2^n`, Möbius primitive counts, and independent word
  enumeration stops the exhaustion certificate.
- Any source theorem used outside its parameter or object scope stops the
  manuscript.

## Resource policy

All computations are CPU-only, deterministic, and exact except the explicitly
secondary high-precision independent root check.  Period 13 skips rational
orbit propagation to avoid denominator growth; the theorem and Sturm count do
not depend on that optional diagnostic.
