# Exact theorem package

Let

\[
M(x,y)=\left(-\frac{4x}{1+x^2}-y,x\right),\qquad
I(x,y)=x^2y^2+x^2+y^2+4xy.
\]

All identities below are understood on the common domains of the displayed
rational compositions.

## Proposition 1 — inverse, reversor, area and invariant

The inverse is

\[
M^{-1}(x,y)=\left(y,-\frac{4y}{1+y^2}-x\right).
\]

For \(S(x,y)=(y,x)\), one has \(S^2=\mathrm{id}\) and
\(SMS=M^{-1}\).  Moreover, \(\det DM=1\) and \(I\circ M=I\).

## Proposition 2 — fixed locus with domain validation

The fixed equation reduces to

\[
-\frac{2x(x^2+3)}{x^2+1}=0.
\]

Thus the valid fixed points over \(\mathbb C\) are
\((0,0)\) and \((\pm i\sqrt3,\pm i\sqrt3)\), with matched signs.
Only the origin is real.  None lies on the pole divisor.

## Proposition 3 — valid primitive real two-cycle

After clearing denominators in \(M^2-\mathrm{id}\), the raw resultant is

\[
-8x(x-1)(x+1)(x^2+1)^2(x^2+3).
\]

The factor \((x^2+1)^2\) is removed because \(M\) is undefined at its
roots.  The remaining valid factor is
\(x(x-1)(x+1)(x^2+3)\).  The roots \(x=\pm1\) yield the genuine cycle

\[
(1,-1)\longmapsto(-1,1)\longmapsto(1,-1),
\]

with invariant value \(-1\).

## Proposition 4 — local monodromy

At either cycle point,

\[
DM=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\qquad
P_2=DM(-1,1)DM(1,-1)=-I_2.
\]

Therefore \(\det P_2=1\), \(\operatorname{tr}P_2=-2\),
\(\det(\lambda I-P_2)=(\lambda+1)^2\), and
\(\det(I-zP_2)=(1+z)^2\).  This is a local derivative polynomial, not a
transfer or Fredholm determinant.
