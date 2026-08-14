# Source audit

## External sources

1. Anthony Flatters, *Primitive Divisors of Some Lehmer--Pierce
   Sequences*, J. Number Theory 129 (2009), 209--219,
   DOI `10.1016/j.jnt.2008.05.008`, arXiv `0708.2190`.
   The source exists and studies
   \(N_{K/\mathbb Q}(u^n-1)\) for real quadratic units.  It is cited only
   for the P51 boundary context; P52's Abel asymptotic does not import its
   primitive-divisor theorem.

2. Tom M. Apostol, *Introduction to Analytic Number Theory*, Springer,
   1976, DOI `10.1007/978-1-4757-5579-4`.
   The bibliographic metadata is verified from the publisher.  P52 proves
   the required summatory-totient estimate directly, so the reference is
   background rather than an unproved dependency.

## Internal sources

- HCS-P49 proves the reciprocal half-packet normalization.
- HCS-P51 defines the universal weighted tagged space and proves the exact
  packet norm identity.

Both internal source files and the P51 certificate are locked by SHA256 and
rehash-verified by the independent checker.

## Claim-source boundary

No external source is cited as proving the P52 scalar Abel constant, Gamma
profile or tagged-space obstruction.  Those statements are proved in the
project's `PROOF_PACKAGE.md`.
