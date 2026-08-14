# HCS-C50 derivation package

## 1. Why two mechanisms are required

If \(c_{p,n}=O(p^{-\alpha_n})\), then

\[
\sum_p|c_{p,n}|p^{-n\sigma}
\]

converges whenever \(n\sigma+\alpha_n>1\). Covering every
\(\sigma>1/5\) therefore requires

\[
\alpha_n\ge1-\frac n5.
\]

The C49 bounds already clear \(n=1\) and \(n=3\). The \(n=2\) Weil bound
has only \(\alpha_2=1/2<3/5\), while the previously untreated \(n=4\)
tail had \(\alpha_4=0<1/5\). Improving only one leaves the other wall at
\(1/4\). HCS-C50 therefore combines:

1. analytic resummation, rather than a false pointwise trace improvement,
   at \(n=2\); and
2. a cohomological square-root gain at \(n=4\).

## 2. Source-derived elliptic structure

The automorphisms in the theorem package arise from the branch sets

\[
\{0,\rho,\infty\}\qquad\text{and}\qquad
\{-1,-\rho,-\rho^2\}
\]

of the cyclic cubic cover. They are verified directly on the frozen C48
equation before any finite-prime fitting. The representation decomposition
forces two standard \(S_3\)-blocks with opposite central sign, hence two
elliptic multiplicity spaces, each occurring twice.

Completely decomposable trigonal genus-four Jacobians and group-algebra
decompositions are classical. Jiménez's genus-four table includes
reduced-\(D_3\) and reduced-\(D_6\) rows whose Jacobians are products of
four elliptic curves. C50 proves only an order-\(12\) subgroup and does not
determine the full automorphism group or identify the curve with either
row. Those results are precedents, not theorems about \(C\). The increment
here is the
explicit \(K\)-rational action and idempotents on this Hénon fibre, the
forced squared factors, and their exact chronological use.

## 3. Matching the second logarithm

From

\[
c_{p,2}=-\frac{28+4a_p}{p-1}
\]

one obtains

\[
-\frac{c_{p,2}}2p^{-2s}
=\frac{14+2a_p}{p-1}p^{-2s}
=(14+2a_p)p^{-(2s+1)}
+\text{more convergent terms}.
\]

At a split rational prime, the coefficient \(14\) is supplied by the two
degree-one primes in \(\zeta_K(2s+1)^7\). The coefficient \(2a_p\) is
the sum of the first Frobenius traces at those two primes in
\(L(H^1(C/K),2s+1)\). Both exponents are integers, so no fractional
\(L\)-function root or branch choice is introduced.

Higher prime powers and missing inert primes are retained in the absolutely
convergent logarithm defining \(H_2\). Using full \(K\)-Euler functions in
this way preserves arithmetic information; it does not replace split-prime
chronology by an averaged transition matrix.

## 4. Eight-step projective direction count

For a nonzero projective direction \(v\),

\[
\Phi_{p,4}(\lambda v)
=\lambda^2\bigl(2\lambda\mathcal C(v)+\mathcal Q(v)\bigr).
\]

Directions outside \(S\cup Q\) have one nonzero radial root; directions in
exactly one of \(S,Q\) have none; directions in \(X=S\cap Q\) have all
\(p-1\). Adding the origin gives

\[
Z_{p,4}=1+\#\mathbf P^7-\#S-\#Q+p\#X.
\]

Writing even and odd coordinates separately gives

\[
M_\rho=
\begin{pmatrix}
1&0&0&\rho\\
1&1&0&0\\
0&1&1&0\\
0&0&1&1
\end{pmatrix},
\qquad \det M_\rho=1-\rho.
\]

Thus \(Q\) is split. Substituting

\[
\#S=P_6+A_p,\qquad \#Q=P_6+p^3,\qquad
\#X=P_5-B_p
\]

cancels every ambient Tate term except \(p^7-p^3\):

\[
Z_{p,4}=p^7-p^3-A_p-pB_p.
\]

The moment normalization gives the displayed \(C_{p,4}\) formula.

## 5. Smoothness and finite bad fibres

Characteristic-zero smoothness is an exact recurrence theorem. Gradient
dependence is normalized to

\[
x_0^2=x_1+\rho x_7,\qquad
x_i^2=x_{i-1}+x_{i+1},\qquad
x_7^2=x_6+\rho x_0.
\]

Together with \(\mathcal Q=0\) and \(\rho^2+\rho+1=0\), the reduced
Singular basis is

\[
x_7,x_6,\ldots,x_0,\rho^2+\rho+1.
\]

Only the affine origin occurs, so there is no projective singular point.
Openness then gives a finite bad set; it is not itself the smoothness proof.
The explicit \(p=181\) witness explains why this cannot be strengthened to
all split primes.

## 6. Cohomology and the fifth abscissa

The Chern calculations give primitive ranks \(86\) and \(168\). Their
weights are six and five, so

\[
\frac{A_p}{p^3}=O(1),\qquad
\frac{B_p}{p^2}=O(\sqrt p).
\]

After division by \(d_p\asymp p\), the normalized fourth moment is
\(O(p^{-1/2})\). Thus \(n=4\) is harmless already for
\(\Re s>1/8\). Once \(n=2\) is extracted exactly, the first untreated
generic term is \(n=5\), giving the new boundary \(\Re s=1/5\).

The same clock determines the regularization order. The normalized
semifinite law \(q\Re s>2\) gives order ten, whereas the classical Hilbert
law \(q\Re s>3\) gives order fifteen. These categories cannot be merged:
the latter records the ordinary Galois norm and does not realize the
degree-normalized Euler continuation.
