# Narrative report

C33 found an exact transverse equal-action collision of two primitive
period-five area-preserving Hénon orbits. Its collision parameter field has
degree nine and Galois group \(S_9\). The product of the two chronological
Hill determinants descends to a nontrivial square class \(\beta\) in that
field, but C33 did not test whether the nine conjugate classes become
dependent in the common splitting field.

C34 resolves that question positively at maximal rank. A direct Newton
polygon at \(p=19\), after the translation \(A=1802+T\), isolates two roots
with valuation \(5/2\). The Hill numerator has a unique linear leading term
on this cluster, giving odd integer-normalized valuation \(5\) at both roots;
the other seven conjugates are units. Thus one splitting-field valuation
has parity support \(e_1+e_2\).

Full \(S_9\) symmetry propagates this row to every pair. Any square relation
must consequently have all nine coordinates equal. The only remaining
candidate is the product of all conjugates, but its rational square class is
\(3\cdot13\cdot19\cdot41\cdot59\), whereas the unique quadratic sign field
of the \(S_9\)-extension has discriminant class
\(13\cdot19\cdot41\cdot59\). Their ratio is \(3\), so the all-ones relation
also fails.

The Kummer rank is therefore nine. The normal closure has kernel \(C_2^9\)
over the C33 splitting field and embeds into \(C_2\wr S_9\); equality follows
from the exact order \(2^9 9!=185794560\). The general Kummer and wreath
machinery is standard. The contribution is the explicit Hénon-specific
maximality theorem and its small local certificate.

The result remains fixed-period. It does not provide an all-period zeta,
prime law, critical-line theorem, or self-adjoint operator. Route A is
rejected with tuple `(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`.
