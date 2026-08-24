# C130 narrative report

## One-sentence contribution

A frozen mixing two-state suspension with roof `(1,sqrt(2))` gives an explicit
all-period primitive determinant whose irrational clock separates symbol-count
sectors, while a roof-only rational control restores both cross-sector
collisions and vertical periodicity.

## Why this construction matters

A discrete symbolic determinant can own all primitive periods yet retain only
an integer return clock.  Passing to a suspension adds a continuous length to
each orbit.  The key question is whether that clock is visible exactly rather
than through numerical approximations.  Here it is: the bivariate determinant
stores the two symbol counts, and the substitution `(u,v)=(e^-s,e^-sqrt(2)s)`
turns them into nonlattice suspension times.

## Exact evidence

The positive full-shift adjacency makes the base mixing.  The rank-one matrix
`M(u,v)=[[u,v],[u,v]]` has determinant `det(I-M)=1-u-v` and trace
`Tr M^n=(u+v)^n`.  Regrouping rooted words by primitive roots gives the
all-period dynamical Euler product.  The replay through period 10 independently
checks 2,046 rooted words, 226 primitive necklaces, and 65 clock sectors.

The algebraic basis `{1,sqrt(2)}` separates different population vectors at
all periods.  It does not identify an orbit inside its population vector:
`000111` and `001011` are distinct primitive period-six necklaces with the
same roof.  This caveat is structural, not a finite-prefix defect.

## Negative control

Replacing the roof by `(1,2)` leaves the full shift and matrix convention
unchanged.  The determinant becomes `1-e^-s-e^-2s=1-q-q^2`.  The second
repeat of `[0]` and primitive `[1]` meet at time 2, and the determinant is
`2*pi*i` periodic.  Thus irrational sector separation and absence of a
nonzero imaginary period disappear under a single controlled change.

## Validation story

The standard-library checker independently rebuilds matrix powers and the
degree-10 primitive product; it does not import producer code or SymPy.  A
fresh SymPy program supplies a second algebraic representation.  Canonical
byte replay passes.  All 44 hostile mutations are rejected: 43 carry a
repaired internal hash and one deliberately carries a stale hash.  The split
separates semantic rejection from checksum-gate rejection.

## Route-A interpretation

This is real internal progress: primitive orbits, continuous roof lengths,
traces, and the determinant belong to one all-period source.  It is not a
target-facing result.  No target divisor, arithmetic local factor, root number,
functional equation, counting law, or natural self-adjoint lift is present.
The correct tuple remains
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` with Route B disabled.
