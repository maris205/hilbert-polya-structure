# HCS-C19 results

## Exact source diagnosis and one-fibre formula selection

The final term printed in Endler--Gallas Eq. (16) fails an exact period-seven
Hénon doublet over \(\mathbb F_{103}\).  Replacing it by

\[
-2a^3+6a^2+2a+3+(a^3-4a^2+a-2)\sigma
\]

recovers the seven coordinate roots of both reversed cycles at that fibre.
The source status is `EXACT_SPECIALIZATION_CERTIFIED_APPARENT_PRINT_ERROR`;
no official erratum or claim about the authors' historical intent is made.
Generic dynamical certification is the separate theorem below.

## Exact generic Hénon reconstruction

In \(\mathbb Q(\sigma)[x]/(P)\), the last nonzero subresultant in \(y\) of

\[
P(\sigma,y),\qquad P(\sigma,a-y^2-x)
\]

has degree two, while the degree-one and degree-zero subresultants vanish.  If
the quadratic is \(c_2y^2+c_1y+c_0\), then exactly

\[
c_1=c_2(x^2-a),
\qquad y_1+y_2=a-x^2.
\]

Its discriminant and diagonal value are nonzero.  The induced root graph is
therefore simple and two-regular; geometric transitivity in prime degree seven
forces one seven-cycle.  The generic ordered-edge cover has degree 14, and

\[
\tau(x,y)=(a-x^2-y,x)
\]

has exact order seven.  A regular completely split control at
\((p,\sigma,a)=(43,7,35)\) independently realizes the cycle
\(8\to16\to29\to38\to24\to23\to41\to8\).

## Exact geometric result for the frozen candidate curve

\[
\operatorname{Disc}_xP=(4\sigma-9)^2Q_6(\sigma)^3,
\qquad \operatorname{Disc}(Q_6)=2^{63}\cdot97.
\]

The six roots of \(Q_6\) contribute 18 simple ramification points.  The
finite node and all seven infinity branches are unramified.  Hence the smooth
projective normalization is geometrically integral of genus three.

## Branch-corrected finite-field counts

| \(p\) | affine \((A_1,A_2,A_3)\) | branch-corrected candidates \((\widehat N_1,\widehat N_2,\widehat N_3)\) |
|---:|---:|---:|
| 5 | \((3,31,141)\) | \((9,39,147)\) |
| 11 | \((11,159,1163)\) | \((19,167,1171)\) |
| 13 | \((10,234,2125)\) | \((16,242,2131)\) |

The frozen branch correction is seven rational infinity branches plus
\(+1\) or \(-1\) according to whether the two node tangents are rational over
the extension field.

## Candidate local numerators

\[
\begin{aligned}
\widehat L_5(T)&=1+3T+11T^2+31T^3+55T^4+75T^5+125T^6,\\
\widehat L_{11}(T)&=1+7T+47T^2+161T^3+517T^4+847T^5+1331T^6,\\
\widehat L_{13}(T)&=1+2T+38T^2+51T^3+494T^4+338T^5+2197T^6.
\end{aligned}
\]

Each is irreducible over \(\mathbb Q\), reciprocal with the genus-three
weight, and numerically has reciprocal roots on \(|T|=p^{-1/2}\).  A
simultaneous-normalization/good-reduction theorem is not supplied, so these
are not yet asserted local factors of the characteristic-zero curve.  The
largest recorded modulus residual is below \(2.2\times10^{-15}\).

The candidate numerators predict the branch-corrected sequence

| \(p\) | \((\widehat N_1,\ldots,\widehat N_6)\) |
|---:|---:|
| 5 | \((9,39,147,547,2939,16215)\) |
| 11 | \((19,167,1171,14595,162319,1769615)\) |
| 13 | \((16,242,2131,27834,372326,4832765)\) |

The independent checker directly obtains the branch-corrected candidate
\(\widehat N_{5,4}=547\).

## Decision

The characteristic-zero genus-three theorem and generic oriented time lift
are positive results relative to the earlier zero-dimensional and genus-zero
obstructions.  The scalar candidate numerators are not equivariant traces of
the lift, and fixed period seven is not a cross-period clock.  The result
therefore provides no Riemann divisor, cross-period zeta, or Hilbert--Pólya
operator.
