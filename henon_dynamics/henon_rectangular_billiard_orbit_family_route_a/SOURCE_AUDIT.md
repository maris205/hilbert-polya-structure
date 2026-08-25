# C147 source audit

## Source class

C147 is an exact geometric construction.  It uses only the unit square,
straight-line unfolding, integer lattice directions, gcd, and symbolic square
roots.  There is no fitted parameter, downloaded table, numerical optimizer,
or external source claim.

## Frozen conventions

- Square: `[0,1]^2`, unit speed.
- Direction ledger: ordered positive absolute representatives `(m,n)` with
  `gcd(m,n)=1`.
- Each row records four signed unfolded sectors `(+-2m,+-2n)` and their two
  time-reversal pairs; these multiplicities are not silently discarded.
- Coordinate swap is retained in the ordered ledger and separately tagged as
  a square symmetry.
- Horizontal `(1,0)` and vertical `(0,1)` are the two time-reversal-quotiented
  axis classes, recorded separately and excluded from the positive ledger.
- Primitive unfolded displacement is `(2m,2n)` and length is
  `2 sqrt(m^2+n^2)`.
- Vertex-hitting offsets are excluded from the regular billiard families.
- The finite cutoff is `1<=m,n<=40`; the geometric family theorem is not
  cutoff-dependent.

## Measure and orientation boundary

For a fixed rational direction, the quotient transverse to the straight flow
is a circle.  Removing finitely many singular offsets produces open cylinders
of positive transverse length.  The fixed-direction set has zero Liouville
measure in the full energy shell; no ambient positive-measure claim is made.
Each regular primitive trajectory has `2m+2n` reflections.  Under a Dirichlet
reflection convention its total reflection phase is therefore `+1`.  The
ordinary obstruction uses the full reduced Poincare derivative: the fixed-
family tangent is a unit eigenvector, hence `det(I-DP)=0`; no scalar surrogate
for the full derivative is used.

## Independence and controls

The checker imports no producer code and reconstructs all 979 direction rows,
Möbius count, degeneracy groups, collision minimality, family flags, aspect
control, and scope boundary.  SymPy independently checks the Poincare
singularity, collision, irrational basis, and Möbius formula.  Replay demands
byte identity.  Each hostile semantic mutation carries a repaired hash before
rejection; a stale-hash control is separate.

## Firewall

No target table, prime table, arithmetic/local factor, Euler factor, root
number, automorphy datum, target divisor, Hilbert--Polya operator, or Route-B
input is used.  Literal scope: `NO_BAD_EULER_OR_ROOT_NUMBER`.
