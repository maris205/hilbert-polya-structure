# HCS-C49 theorem package

## 1. Frozen chronological object

Let \(p>3\) be prime with \(p\equiv1\pmod 3\), and fix
\(\rho\in\mathbf F_p^\times\) of order three.  The third chronological
moment is the zero fibre of the **ordered six-step phase**

\[
 \Phi_{p,3}(x_0,\ldots,x_5)
 =2\sum_{i=0}^{5}x_i^3
  +\sum_{i=0}^{4}x_ix_{i+1}+\rho x_5x_0 .                 \tag{1}
\]

The coefficient of every cubic is still \(2\).  The subscript \(3\) counts
the third power of the local operator, hence six chronological kernel
steps; it does not replace the source phase by \(3\sum x_i^3\).

Put

\[
 Z_{p,3}=\#\{x\in\mathbf F_p^6:\Phi_{p,3}(x)=0\},\qquad
 C_{p,3}=2p^{-2}Z_{p,3}-2p^3,
\]
\[
 d_p=\frac{p-1}{2},\qquad c_{p,3}=\frac{C_{p,3}}{d_p}.    \tag{2}
\]

These are the inherited C45 normalizations.  In particular, no rounding
of \(C_{p,3}\) to an integer is permitted.

## 2. Projective direction theorem

Write

\[
 \mathcal C=\sum_{i=0}^{5}x_i^3,
 \qquad
 \mathcal Q_\rho=\sum_{i=0}^{4}x_ix_{i+1}+\rho x_5x_0,
\]

and in \(\mathbf P^5\) put

\[
 S=V(\mathcal C),\qquad Q_\rho=V(\mathcal Q_\rho),
 \qquad X_\rho=S\cap Q_\rho.                              \tag{3}
\]

For every projective direction \([v]\),

\[
 \Phi_{p,3}(\lambda v)
 =\lambda^2\bigl(2\lambda\mathcal C(v)+\mathcal Q_\rho(v)\bigr).
\]

Directions outside \(S\cup Q_\rho\) have exactly one nonzero radial root;
directions in \(X_\rho\) have all \(p-1\) nonzero radial roots; the other
two strata have none.  Hence

\[
 \boxed{Z_{p,3}=1+\#\mathbf P^5(\mathbf F_p)-\#S(\mathbf F_p)
                  -\#Q_\rho(\mathbf F_p)+p\#X_\rho(\mathbf F_p).} \tag{4}
\]

This is an exact partition of the genuine ordered phase, not an averaged
transition-matrix calculation.

## 3. The split quadric fourfold

Set \(e=(x_0,x_2,x_4)^t\), \(o=(x_1,x_3,x_5)^t\).  Then

\[
 \mathcal Q_\rho=e^tM_\rho o,
 \qquad
 M_\rho=
 \begin{pmatrix}1&0&\rho\\1&1&0\\0&1&1\end{pmatrix},
 \qquad \det M_\rho=1+\rho=-\rho^2\ne0.                  \tag{5}
\]

Thus \(Q_\rho\) is a smooth split quadric fourfold.  Counting first \(e=0\)
and then \(e\ne0\) gives \(p^3+(p^3-1)p^2\) affine zeros, whence

\[
 \boxed{\#Q_\rho(\mathbf F_p)=1+p+2p^2+p^3+p^4.}         \tag{6}
\]

## 4. Fermat cubic fourfold and its exact arithmetic trace

Let \(\chi\) be either cubic character of \(\mathbf F_p^\times\), extended
by \(\chi(0)=0\), and put

\[
 \pi_p=J(\chi,\chi)=\sum_{u+v=1}\chi(u)\chi(v),
 \qquad a_p=\pi_p^2+\overline{\pi}_p^{\,2}.               \tag{7}
\]

Then \(\pi_p\overline\pi_p=p\), \(a_p\in\mathbf Z\), and
\(|a_p|\le2p\).  The choice \(\chi\leftrightarrow\bar\chi\) only conjugates
\(\pi_p\), so \(a_p\) is canonical.  A direct six-variable additive-character
calculation gives

\[
 \boxed{\#S(\mathbf F_p)=1+p+p^2+p^3+p^4+20p^2+pa_p.}   \tag{8}
\]

Cohomologically, \(b_4(S)=23\), the ambient Tate line contributes \(p^2\),
and the primitive rank-22 trace is

\[
 A_p:=\operatorname{Tr}
   (F_p\mid H^4_{\mathrm{prim}}(S_{\overline{\mathbf F}_p},\mathbf Q_\ell))
 =20p^2+pa_p.                                            \tag{9}
\]

Here and below \(F_p\) denotes geometric Frobenius with
\(F_p\mid\mathbf Q_\ell(-1)=p\).  The twenty mixed cubic-character sectors
are Tate and the two pure sectors are \(p\pi_p^2,p\bar\pi_p^2\).

Equivalently, choosing the classical representation
\(4p=L_p^2+27M_p^2\) attached to the cubic Jacobi sum gives

\[
 a_p=L_p^2-2p=\frac{L_p^2-27M_p^2}{2};                  \tag{10}
\]

formula (7), rather than a choice of signs for \(L_p,M_p\), is the frozen
definition.

## 5. The \((2,3)\) Fano threefold

The characteristic-zero member \(X_\rho\) is smooth.  Smoothness is open,
so there is a finite, effectively computable set \(\Sigma_{\mathrm{sm}}\)
of prime ideals of \(\mathbf Z[\rho,1/6]\) outside which the reduction is
smooth.  This finite-exception statement is the theorem-level scope used
below; it is already sufficient for every Euler-product conclusion.

An exact elimination described in `PROOF_PACKAGE.md` strongly sharpens the
statement: its residual resultant is
\(2^{21}3^{12}23^3\), and \(23\equiv2\pmod3\).  The proposed all-split
strengthening therefore says that \(X_\rho\) is smooth for every split
prime \(p>3\).  That strengthening is a release gate until the independent
code lane reproduces the stated normal forms and the finite
leading-coefficient audit; it is not needed in order to claim the
half-plane theorem.

At every smooth prime, adjunction and the degree calculation give

\[
 K_X=\mathcal O_X(2+3-6)=\mathcal O_X(-1),\qquad
 H^3=\deg X=6=2g-2,
\]

so \(X_\rho\) is a Fano threefold of genus \(g=4\).  Moreover

\[
 c(TX)=\frac{(1+H)^6}{(1+2H)(1+3H)}
       =1+H+4H^2-6H^3,
\]

and therefore

\[
 \chi_{\mathrm{top}}(X)=\int_Xc_3(TX)=-6\cdot6=-36.
\]

Weak Lefschetz supplies \(b_0=b_2=b_4=b_6=1\) and no other odd
cohomology except \(H^3\).  Consequently

\[
 \boxed{b_3(X)=40,\qquad h^{2,1}(X)=h^{1,2}(X)=20.}       \tag{11}
\]

Define

\[
 B_p=\operatorname{Tr}
 (F_p\mid H^3(X_{\overline{\mathbf F}_p},\mathbf Q_\ell)).
\]

The trace formula and Deligne's weight theorem give

\[
 \boxed{\#X_\rho(\mathbf F_p)=1+p+p^2+p^3-B_p,
        \qquad |B_p|\le40p^{3/2}.}                       \tag{12}
\]

There is also an exact integrality gain.  Chevalley--Warning applied to
the affine cone cut out by degrees \(2\) and \(3\) in six variables gives
\(\#X_\rho(\mathbf F_p)\equiv1\pmod p\).  Thus

\[
 b_p:=B_p/p\in\mathbf Z,\qquad |b_p|\le40\sqrt p.        \tag{13}
\]

This divisibility is a theorem; any more refined distribution or hidden
abelian-variety model for \(b_p\) remains experimental.

## 6. Exact third-moment decomposition

Substitution of (6), (8), and (12) into (4) gives

\[
 \boxed{Z_{p,3}=p^5-p^2-A_p-pB_p}                        \tag{14}
\]

and hence

\[
 \boxed{C_{p,3}=-2-\frac{2A_p}{p^2}-\frac{2B_p}{p}.}     \tag{15}
\]

Using (9) and (13), this becomes the arithmetic splitting

\[
 \boxed{C_{p,3}=-42-2b_p-\frac{2a_p}{p},\qquad
 c_{p,3}=-\frac{4}{p-1}\left(21+b_p+\frac{a_p}{p}\right).} \tag{16}
\]

All signs and factors in (14)--(16) follow from geometric Frobenius and
the minus sign of odd \(H^3\).  In particular,

\[
 |C_{p,3}|\le46+80\sqrt p,
 \qquad
 \boxed{|c_{p,3}|\le\frac{92+160\sqrt p}{p-1}
        =O(p^{-1/2}).}                                   \tag{17}
\]

Thus the cubic-fourfold trace contributes only \(O(p^{-1})\) after the
\(d_p\)-normalization, while the Fano \(H^3\) trace contributes
\(O(p^{-1/2})\).  There is no normalized \(O(1)\) third-moment
obstruction.

## 7. Fourth-abscissa Euler theorem

Retain the exact C48 estimates

\[
 c_{p,1}=-\frac{12}{p-1},\qquad c_{p,2}=O(p^{-1/2}),
\]

and the inherited uniform estimate \(|c_{p,n}|\le4\cdot4^n\).  Then

* \(n=1\) is summable for \(\Re s>0\);
* \(n=2\) is summable for \(\Re s>1/4\);
* (17) makes \(n=3\) summable already for \(\Re s>1/6\);
* the tail \(n\ge4\) is locally normally summable for \(\Re s>1/4\).

The finitely many primes in \(\Sigma_{\mathrm{sm}}\), if any, are handled
by the local unitary bound and do not change an abscissa.  Therefore

\[
 \boxed{
 \sum_{p\equiv1\pmod3}\sum_{n\ge1}\frac{|c_{p,n}|}{n}p^{-n\sigma}<\infty
 \quad(\sigma>1/4),}                                    \tag{18}
\]

locally uniformly.  The canonical normalized Euler germ

\[
 \mathcal G(s)=\exp\left(-\sum_{p\equiv1\pmod3}
                    \sum_{n\ge1}\frac{c_{p,n}}n p^{-ns}\right)
\]

is consequently holomorphic and nonzero on \(\Re s>1/4\).

## 8. Eighth-order normalized-semifinite determinant

For the inherited normalized semifinite trace \(\tau\),

\[
 X_s\in L^q(\mathcal M,\tau)\Longleftrightarrow q\Re s>2.
\]

Thus \(L^8\) is the least fixed integer ideal covering all of
\(\Re s>1/4\).  Put

\[
 \ell_n(s)=\sum_{p\equiv1\pmod3}c_{p,n}p^{-ns}\qquad(1\le n\le7).
\]

Every counterterm converges on that half-plane, and the exact inherited
operator identity becomes

\[
 \boxed{
 \mathcal G(s)=
 \exp\left(-\sum_{n=1}^{7}\frac{\ell_n(s)}n\right)
 \operatorname{Det}_{8,\tau,\mathrm{gr}}(I-X_s).}        \tag{19}
\]

This is a normalized-semifinite graded determinant.  The unregularized
\(\tau\)-determinant still begins only at \(\Re s>2\).  On the underlying
Hilbert direct sum, classical \(S^q\) membership still requires
\(q\Re s>3\), and its determinant encodes the ordinary Galois norm rather
than the normalized root.

## 9. Route-A scope

The status remains

\[
(\mathrm{A1\_WEAK},
 \mathrm{A2\_ANALYTIC\_DETERMINANT},
 \mathrm{A3\_PARTIAL\_ANALYTIC\_STRUCTURE},
 \mathrm{A4\_NATURAL\_QUANTIZATION}).
\]

Suggested overall label:
`ROUTE_A_EXPLORATORY_FANO_THREEFOLD_QUARTER_ABSCISSA`.

The advance is exact arithmetic geometry plus a larger certified
half-plane.  It is not meromorphic continuation through \(\Re s=1/4\), a
functional equation, a Riemann divisor, a prime-orbit correspondence, or a
self-adjoint Hilbert--Pólya operator.
