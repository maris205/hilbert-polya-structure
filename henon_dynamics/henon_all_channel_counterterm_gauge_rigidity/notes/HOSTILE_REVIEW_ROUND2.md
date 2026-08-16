# Hostile review round 2

## Attack 1: coefficient rigidity was promoted to absolute uniqueness

It was not.  Once `d_m=c_m`, the residual is `exp(G)`.  The theorem states
that admissible multipliers form a torsor under `O(D)^x`; absolute
canonicity is explicitly OPEN.

## Attack 2: genus `m-1` trivialization proves that the original object is
meaningless

It proves only that the declared principal-part normalization with `G=0`
carries the full channel logarithm and cancels it.  Genus `m` is equally
normally convergent and order independent but leaves the nonconstant
residual `exp(-2 sum_(m>=2)c_m t^m)`.  The comparison is a canonicity
warning, not a universal triviality theorem.

## Attack 3: the genus `m` residual should have a plus sign

Each genus-`m` multiplier orbit has log
`c_m Phi(t^m)-2c_m t^m`.  It multiplies the relative log
`-c_m Phi(t^m)`, so the residual is `-2c_m t^m`.  Coefficients through degree
96 are checked twice, including an independent implementation.

## Attack 4: a finite normalization at zero fixes the gauge

For every `N`, `exp(lambda t^(N+1))` is nowhere zero, preserves the `N`-jet,
and is nonconstant for nonzero `lambda`.  Value normalization and every
finite jet therefore fail.

## Attack 5: the primary product is already a Fredholm determinant

No operator, trace ideal, nuclearity estimate, determinant identity, or
spectral zero theorem is supplied.  The manuscript states this firewall in
the abstract, body, conclusion, certificate, and route evaluation.
