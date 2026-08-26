# Narrative report

## Outcome first

C173 eliminates the positive Lyness five-cycle map as a primary Route-A
candidate for an exact reason, not because a finite computation looked
unpromising.  The map closes after five ticks everywhere.  Its sole fixed
point is the golden-ratio point, and every other point has exact period five.

That complete period classification creates the obstruction.  For
(5\nmid n), (F^n) fixes one point; for (5\mid n), it fixes the entire
positive quadrant.  The coefficient (\#\operatorname{Fix}(F^5)) required
by the classical Artin--Mazur series is therefore uncountable.  It cannot be
silently replaced by a finite formal number, and the primitive period-five
orbits are not a countable isolated family.

The operator side is equally explicit.  The log-symplectic measure
(dx\,dy/(xy)) is invariant, the coordinate swap reverses time, and the
natural Koopman operator is unitary of order five.  Cyclic Fourier
projections split it into all five fifth-root eigenspaces.  Each eigenspace
is infinite-dimensional, so the operator is noncompact, in no finite
Schatten class, and outside the ordinary trace-class Fredholm determinant
framework.  It is also not self-adjoint.

## Why this is progress

The result closes a distinct nonlinear integrable subtype with an all-point
theorem.  It isolates a useful failure mechanism: exact finite order on a
nonatomic continuum can make periodic-orbit counting worse, not better.
At the same time it records a valid natural A4 Koopman lift and a precise
antiunitary reversal.  The tuple

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`

is therefore a resolved decision rather than an inconclusive score.

## Boundary

No regularized, Lefschetz, or distributional determinant is introduced.
No arithmetic relevance, target comparison, Euler data, automorphy,
Hilbert--Pólya operator, or Route-B permission is claimed.  Finite ledgers
serve only as reproducibility sentinels for the exact proofs.
