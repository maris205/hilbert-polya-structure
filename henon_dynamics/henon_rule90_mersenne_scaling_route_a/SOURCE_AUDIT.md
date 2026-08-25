# C150 source audit

## Source lock

The sole source is the local Rule-90 update on a cyclic binary lattice,
encoded as multiplication by `a=x+x^(-1)` in
`F_2[x,x^(-1)]/(x^L-1)`.  Circumferences are derived internally as
`L_r=2^r-1`; the negative controls are `2^s`.  No external bibliography or
priority statement is used.

## Theorem and evidence boundary

Frobenius in characteristic two proves the all-`r` identity.  A polynomial
gcd proves the image rank, and finite-set dynamics proves that periodic points
are exactly the image.  The general multiplication-kernel lemma supplies exact
fixed counts, followed by Möbius inversion.  Ledgers through `r=8` and
power controls through `s=8` are replay sentinels only, not theorem cutoffs.

No external prime or zero table, arithmetic/local factor, root number,
automorphy claim, target divisor, Hilbert--Polya operator, or Route-B input is
used.  Scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
