# C147 narrative report

## Outcome

C147 introduces an integrable billiard subtype with exact, reproducible
primitive directions and a natural quantization.  Its progress is also its
obstruction: rational periodic trajectories occur in clean cylinders, so the
full reduced Poincare derivative has a family-tangent unit eigenvalue and the
ordinary isolated-orbit denominator vanishes.

## Exact structural progress

The unit-square unfolding gives the all-direction length theorem and precise
orientation/reflection bookkeeping.  The cutoff-40 certificate contains 979
positive absolute-direction representatives, with four signed sectors and two
time-reversal pairs each, exact length-square degeneracy groups, and a
Möbius-count identity.  The first collision beyond coordinate-swap
symmetry is `(1,8)` versus `(4,7)` at square 65.

## Geometric control

Changing the rectangle height to `2^(1/4)` replaces square length coefficients
by the independent basis `1,sqrt(2)`, removing all distinct positive-direction
collisions.  This proves that the square collision is not an unavoidable
feature of rectangular unfolding.

## Scope repair

Internal audit narrowed “positive-measure family”: each regular cylinder has
positive length in its transverse slice, but a fixed direction has zero
Liouville measure in the full energy shell.  It also replaced “one interval”
with the correct transverse circle minus finitely many singular offsets,
possibly producing several open cylinders.

## Route-A interpretation

Primitive direction families justify `A1_WEAK`; nonisolation blocks A2.  The
positive Dirichlet half-wave is a natural unitary quantization whose principal
symbol preserves the unit-speed length clock; complex conjugation gives exact
antiunitary time reversal and the Dirichlet bounce phase agrees with the
classical reflection ledger.  This justifies `A4_NATURAL_QUANTIZATION`, but it
supplies neither a clean-family trace bridge nor a target match.  Route B
remains disabled.
