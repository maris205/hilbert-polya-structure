# C152 source audit

## Source and conventions

C152 uses only the unit-square billiard directions already derived in C147.
Pairs `(m,n)` are ordered, positive, and coprime; axes are excluded,
coordinate swap is retained, and equal squared lengths add multiplicity.
Length is `L=2 sqrt(m^2+n^2)`.  The heat variable is positive and no scale is
fitted.

`Q(R)` counts ordered positive lattice points in the real-radius quarter disk
`m^2+n^2<=R^2`; its axes are excluded.  Consequently the Möbius identity uses
the real argument `Q(R/d)`, not `Q(floor(R/d))`.  Exact code implements the
equivalent scaled inequality `d^2(a^2+b^2)<=R^2`.

## Validation

The producer enumerates coefficients directly and applies scalar Möbius
inversion.  The checker imports no producer code, constructs a sieve-based
Möbius function, and rebuilds every coefficient through 20,000 and every
radius count.  SymPy independently reconstructs initial formal-series
coefficients and the leading Stieltjes integral.  Replay requires byte
identity; repaired-hash mutations test semantics.

## Firewall

The direction transform is never identified with a wave trace, a Dirichlet
eigenvalue heat trace, or an isolated-orbit determinant.  No target table,
prime table, arithmetic/local or Euler factor, root number, automorphy datum,
Hilbert--Polya operator, or Route-B input is used.  Literal scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.
