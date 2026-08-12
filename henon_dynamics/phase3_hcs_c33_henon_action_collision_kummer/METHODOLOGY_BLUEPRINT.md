# HCS-C33 Phase-3 methodology blueprint

## 1. Frozen dynamical object

Use the area-preserving family

\[
H_A(q,p)=(1-Aq^2-p,q)
\]

with diagonal initial state \((x_0,x_{-1})=(q,q)\) and chronological
recurrence

\[
x_{i+1}=1-Ax_i^2-x_{i-1}.
\]

No averaged transition matrix, numerical orbit finder, or imported pilot
coefficient is allowed.

## 2. Marker and action reconstruction

Derive \(x_4-q\) and \(x_5-q\), take their gcd over \(\mathbb Q(A)[q]\),
remove the fixed-point factor \(Aq^2+2q-1\), and canonically primitive-scale
the remaining sextic \(G_A(q)\).

On its orbit coordinates define

\[
\Phi_{5,A}=\sum_{i\bmod5}
\left(x_ix_{i+1}-x_i+\frac A3x_i^3\right).
\]

Reduce \(3A^2\Phi_{5,A}\) modulo \(G_A\) to obtain \(R_A(q)\), then
eliminate \(q\):

\[
W_5(A,c)=A^{-30}\operatorname{Res}_q
\bigl(G_A(q),3A^2c-R_A(q)\bigr).
\]

The producer must also derive a linear subresultant
\(U(A,c)q+V(A,c)\), proving generically that
\(q=-V/U\) and hence \(\mathbb Q(A,q)=\mathbb Q(A,c)\).

## 3. Separate the old cover from the new singular embedding

Factor both discriminants exactly:

\[
\operatorname{Disc}_qG_A=2^6A^{30}P_2P_5,
\]

\[
\operatorname{Disc}_cW_5
=2^{12}3^{30}A^{60}P_2^5P_5^3P_9^2.
\]

The factors \(P_2,P_5\) belong to the known normalization ramification.
The new target is the coprime degree-nine equal-action factor \(P_9\).  The
square exponent alone is not accepted as a node proof.

## 4. Exact node gate over the collision field

Work in \(K_9=\mathbb Q[A]/(P_9)\).  Compute

\[
\gcd(W_5,W_{5,c})=c-c_0
\]

and then

\[
g_2(q)=\gcd\bigl(G_A(q),3A^2c_0-R_A(q)\bigr)
=q^2+bq+d.
\]

Require:

- \(b^2-4d\ne0\);
- \(g_2\) is coprime to \(G_A/g_2\);
- \(W=W_A=W_c=0\), \(W_{cc}\ne0\), and
  \(W_{Ac}^2-W_{AA}W_{cc}\ne0\);
- the two normalization slopes are distinct.  Reduce

  \[
  s(q)=\frac{(A\partial_A R-2R)(\partial_qG)
  -A(\partial_q R)(\partial_AG)}{3A^3\partial_qG}
  \]

  modulo \(g_2\) as \(uq+v\), and require
  \(u^2(b^2-4d)\ne0\).

## 5. Exact-period and nonparabolic gates

Because five is prime, removing the fixed-point factor leaves exact period
five away from the marker discriminant.  Certify the relevant coprimalities
with \(P_9\).

Form the chronological derivative product

\[
M=D_4D_3D_2D_1D_0,
\qquad
D_i=\begin{pmatrix}-2Ax_i&-1\\1&0\end{pmatrix},
\]

and \(h=\det(I-M)\).  Reconstruct the cyclic action Hessian and verify
\(\det D^2\Phi_{5,A}=h\) on \(G_A=0\).

The resultant with \(h\) excludes multiplier \(+1\).  Since \(\det M=1\)
and \(h=2-\operatorname{tr}M\), the separate resultant with \(4-h\)
excludes multiplier \(-1\).  Both must be coprime to \(P_9\).

## 6. Hill--Kummer gate

In \(E=K_9[q]/(g_2)\), reduce \(h=\ell q+m\) and compute

\[
N_H=N_{E/K_9}(h)=\ell^2d-\ell mb+m^2.
\]

Branch exchange fixes \(N_H=h_1h_2\).  A common Hill normalization
\(h_i\mapsto\nu h_i\), with \(\nu\in K_9^\times\), multiplies \(N_H\) by
\(\nu^2\), so its square class is unchanged.  Compute the rational field
norm with the leading-coefficient
correction for nonmonic \(P_9\), factor it, and reject the square class if
the norm is a rational square.

## 7. Arithmetic and finite controls

Prove \(\operatorname{Gal}(P_9/\mathbb Q)=S_9\) from exact unramified
factorizations with cycle types

\[
(9),\qquad(5,2,1,1),\qquad(8,1).
\]

Replay every prime divisor of \(P_9(6)\).  The finite rows are controls; the
characteristic-zero norm is the theorem.  Prime \(61\) remains labelled
post-hoc because it was first found in C32.

## 8. Reproducibility and failure discipline

The producer serializes canonical rational coefficient vectors.  The
checker imports no producer code, reconstructs the chronology and quotient
arithmetic, rejects unknown fields and type confusion, and distinguishes a
mathematical gate failure from an unexpected checker error.  Mutations must
kill the \(-1\)-multiplier gate, tangent gate, norm correction, finite
controls, Route-A ceiling, and scope firewalls.
