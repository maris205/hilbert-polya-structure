# HCS-C48 theorem package

## 1. Frozen chronological phase

Let \(p>3\), \(p\equiv1\pmod3\), and let \(\rho\) have order three in
\(\mathbf F_p^\times\).  The two-repetition, four-step chronological phase is

\[
\Phi(x_0,x_1,x_2,x_3)
=2\sum_{i=0}^3x_i^3+x_0x_1+x_1x_2+x_2x_3+\rho x_3x_0. \tag{1}
\]

Write \(Z_p=\#\Phi^{-1}(0)\).  The HCS-C45 trace convention gives

\[
C_{p,2}=\frac{2Z_p}{p}-2p^2,
\qquad c_{p,2}=\frac{C_{p,2}}{d_p},
\qquad d_p=\frac{p-1}{2}. \tag{2}
\]

No edge order is averaged in (1).

## 2. Projective direction theorem

Put

\[
\mathcal C=\sum x_i^3,
\qquad
\mathcal Q=x_0x_1+x_1x_2+x_2x_3+\rho x_3x_0
\]

on \(\mathbf P^3\), and let \(S=V(\mathcal C)\), \(R=V(\mathcal Q)\),
and \(X=S\cap R\).  On a nonzero affine line \(\lambda v\),

\[
\Phi(\lambda v)=\lambda^2(2\lambda\mathcal C(v)+\mathcal Q(v)).
\]

Counting the nonzero roots direction by direction gives exactly

\[
Z_p=1+\#\mathbf P^3-\#S-\#R+p\#X. \tag{3}
\]

Since \(\mu_3\subset\mathbf F_p\), the Fermat cubic surface is split and

\[
\#S=p^2+7p+1. \tag{4}
\]

The change \(y=x_1+\rho x_3\), \(w=x_1+x_3\) gives
\(\mathcal Q=x_0y+x_2w\).  Hence \(R\simeq\mathbf P^1\times\mathbf P^1\) and

\[
\#R=(p+1)^2. \tag{5}
\]

Equations (3)--(5) yield

\[
Z_p=p^3-p^2-8p+p\#X. \tag{6}
\]

## 3. Genus-four curve

The construction is defined over

\[
\mathcal R=\mathbf Z[\rho,1/6]/(\rho^2+\rho+1).
\]

Since \(N(\rho-1)=3\), the element \(\rho-1\) is a unit.  With
\(y=x_1+\rho x_3\) and \(w=x_1+x_3\), the standard split-quadric
isomorphism is

\[
x_0=rt,\quad x_2=ru,\quad y=-su,\quad w=st.
\]

On the split quadric use coordinates

\[
x_0=rt,\quad x_2=ru,\quad
x_1=\frac{s(\rho t+u)}{\rho-1},\quad
x_3=-\frac{s(t+u)}{\rho-1}.
\]

Using \((\rho-1)^2=-3\rho\), the exact restriction identity is
\(\rho\mathcal C|_R=F\), where

\[
F=\rho r^3(t^3+u^3)+\rho^2s^3t^2u-s^3tu^2=0. \tag{7}
\]

This divisor has type \((3,3)\).  It is smooth over the algebraic closure in
every characteristic other than two and three.  Indeed write

\[
F=A(t,u)r^3+B(t,u)s^3,
\quad A=\rho(t^3+u^3),
\quad B=tu(\rho^2t-u).
\]

If \(rs\ne0\), the two radial derivatives force \(A=B=0\).  Then
\(tu\ne0\), \(u=\rho^2t\), and \(t^3+u^3=2t^3\ne0\), a contradiction.  If
\(r=0\), singularity would require a multiple root of the binary cubic \(B\),
whose three roots are distinct.  If \(s=0\), it would require a multiple root
of \(A\), which is separable outside characteristic three.  Thus \(X\) is
smooth.  If it were geometrically disconnected, partition its components
into effective divisors of bidegrees \((a,b)\) and \((3-a,3-b)\).  They would
be disjoint, whereas

\[
(a,b)\mathbin{\cdot}(3-a,3-b)=a(3-b)+b(3-a)>0
\]

for every nontrivial partition.  Hence \(X\) is geometrically connected and
geometrically irreducible.  Adjunction gives

\[
g(X)=(3-1)(3-1)=4. \tag{8}
\]

## 4. Exact moment formula and Weil gain

Define

\[
a_p=p+1-\#X(\mathbf F_p).
\]

Substituting (6) into (2) gives the exact identity

\[
\boxed{C_{p,2}=-14-2a_p},
\qquad
\boxed{c_{p,2}=-\frac{28+4a_p}{p-1}}. \tag{9}
\]

The Hasse--Weil bound for the genus-four curve gives

\[
|a_p|\le8\sqrt p,
\qquad
|c_{p,2}|\le\frac{28+32\sqrt p}{p-1}. \tag{10}
\]

The two choices of order-three element define isomorphic curves, not merely
formally conjugate equations.  If

\[
T([r:s],[t:u])=([r:-s],[u:t]),
\]

then \(F_{\rho^{-1}}=\rho F_\rho\circ T\).  Their point counts and
Frobenius traces therefore agree over \(\mathbf F_p\).

## 5. Third-abscissa Euler theorem

The first normalized moment is \(c_{p,1}=-12/(p-1)\).  Equation (10) makes

\[
\sum_p|c_{p,2}|p^{-2\sigma}
\]

convergent for \(\sigma>1/4\).  For \(n\ge3\), retain the uniform HCS-C45
bound \(|c_{p,n}|\le4\cdot4^n\).  Therefore

\[
\sum_p\sum_{n\ge1}\frac{|c_{p,n}|}{n}p^{-n\sigma}<\infty
\qquad(\sigma>1/3), \tag{11}
\]

locally uniformly.  Consequently the canonical normalized Euler product is
holomorphic and nonzero on \(\Re s>1/3\).

To justify the local-uniform statement, fix
\(\sigma_0>1/3\) below the real parts on a compact set and choose \(P_0\) so
that \(4p^{-\sigma_0}\le1/2\) for \(p>P_0\).  Then

\[
\sum_{p>P_0}\sum_{n\ge3}\frac{|c_{p,n}|}{n}p^{-n\sigma_0}
\ll\sum_{p>P_0}p^{-3\sigma_0}<\infty.
\]

For the finitely many \(p\le P_0\), unitarity gives
\(|c_{p,n}|\le\tau_p(I)=(8p+4)/3\), and the logarithmic series converges
because \(p^{-\sigma_0}<1\).

## 6. Sixth-order normalized-semifinite determinant

Let \((\mathcal M,\tau)\) be the HCS-C47 product algebra with its normalized
faithful semifinite trace, and let \(X_s\) be its block operator.  For every
\(q>0\),

\[
\tau(|X_s|^q)
=\sum_{p\equiv1(3)}\frac{8p+4}{3}p^{-q\Re s},
\qquad
X_s\in L^q(\mathcal M,\tau)
\Longleftrightarrow q\Re s>2. \tag{12}
\]

In particular, \(X_s\) is \(\tau\)-trace class exactly on \(\Re s>2\).
That is the domain of the unregularized \(\tau\)-associated analytic graded
determinant.  On \(\Re s>1/3\), one instead has
\(X_s\in L^6(\mathcal M,\tau)\).  Put

\[
\ell_n(s)=\sum_pc_{p,n}p^{-ns},\qquad1\le n\le5.
\]

Using (10) for \(n=2\), all five counterterms converge on that half-plane,
and

\[
\boxed{
\mathcal G(s)=
\exp\!\left(-\sum_{n=1}^5\frac{\ell_n(s)}n\right)
\det_{6,\tau,\mathrm{gr}}(I-X_s)}. \tag{13}
\]

Here \(\det_{6,\tau,\mathrm{gr}}\) is the quotient of the
\(\tau\)-trace-associated sixth-order regularized determinants in the
positive and negative grades, or equivalently the canonical normalized
supertrace logarithm beginning at \(n=6\).
Order six is the least fixed **integer** Schatten order covering all
\(\Re s>1/3\) by positive \(L^q(\mathcal M,\tau)\)-membership; this does not
classify unrelated regularization schemes.

This normalized-semifinite statement must be distinguished from the
classical Schatten ideals of the underlying Hilbert direct sum
\(\mathcal H=\bigoplus_p\mathcal H_p\).  Since

\[
\dim\mathcal H_p
=d_p\tau_p(I)
=\frac{(p-1)(4p+2)}3,
\]

one has

\[
\operatorname{Tr}_{\mathcal H}(|X_s|^q)
=\sum_{p\equiv1(3)}\frac{(p-1)(4p+2)}3p^{-q\Re s},
\qquad
\boxed{X_s\in S^q(\mathcal H)\Longleftrightarrow q\Re s>3}. \tag{14}
\]

Thus classical Hilbert trace class begins only at \(\Re s>3\).  Its signed
moments are unnormalized:

\[
\operatorname{Str}_{\mathcal H_p}(W_p^n)=d_pc_{p,n}=C_{p,n}.
\]

Writing \(G_p\) for the local normalized root, its local trace-log
exponentiates to \(G_p(z)^{d_p}=N_p(z)\), the ordinary Galois norm, rather
than \(G_p\) itself.  The gain from \(1/2\) to \(1/3\) is arithmetic cancellation in
the second moment within the normalized \(\tau\)-category, not improved
positive-ideal membership.

## 7. Scope

This proves a genus-four Frobenius interpretation, a nonzero holomorphic
Euler germ on \(\Re s>1/3\), and a sixth-order regularized graded determinant
relative to the normalized semifinite trace.  It is not a classical Fredholm
determinant on that half-plane.
It does not prove continuation through \(1/3\), a functional equation, a
Gamma factor, a Riemann divisor, or a self-adjoint Hilbert--Pólya operator.
