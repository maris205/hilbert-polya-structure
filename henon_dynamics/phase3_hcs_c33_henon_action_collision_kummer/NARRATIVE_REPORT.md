# HCS-C33 Phase-3 narrative report

The starting signal was a finite-field collision from C32: two primitive
period-five Hénon points at \(A=6\) had the same action but different Hill
determinants.  A longer prime scan would have been a small door.  C33 instead
asked whether this event was the reduction of a characteristic-zero
parameter-space structure.

The first surprise was negative.  The period-five action coordinate does
not create a new six-sheet cover.  A linear subresultant recovers the old
marker coordinate, so the two plane models have the same function field.
This kills ordinary cover novelty.

The singular embedding contains the new information.  The action
discriminant has one factor not present in the normalization discriminant:
the degree-nine polynomial \(P_9\), with exponent two.  Exact quotient-field
arithmetic shows that a generic \(P_9\) point has one repeated action value
and exactly two distinct normalization points above it.  The plane tangent
cone is nondegenerate, and the two branch slopes differ.  The factor is
therefore an ordinary equal-action node, not a nonreduced artifact.

The second surprise is dynamical.  Both node branches are exact-period-five
Morse points.  The cyclic action Hessian equals the chronological Hill
determinant \(h=\det(I-DH_A^5)\).  A separate resultant with
\(4-h=\det(I+DH_A^5)\) rules out the multiplier \(-1\), a condition that the
Morse gate alone would miss.

Branch exchange destroys the individual labels \(h_1,h_2\), but it fixes
their product.  That product is the quadratic norm of the Hill polynomial
on the two-point fiber.  Its rational field norm has odd prime valuations,
so it cannot be a square in the degree-nine collision field.  The equation
\(u^2=h_1h_2\) is therefore a nontrivial Kummer extension attached to the
action node.

This is the meaningful gain: a bare orbit permutation cover has acquired a
gauge-stable arithmetic decoration derived from chronological stability.
The gain remains fixed-period.  No all-period trace law or self-adjoint
operator follows, so Route A stays rejected.  The next large door is to test
independence of the conjugate Kummer classes or construct a trace-compatible
family across periods.
