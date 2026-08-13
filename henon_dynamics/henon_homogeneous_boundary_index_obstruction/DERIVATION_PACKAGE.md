# Derivation Package

## Target

Decide whether the homogeneous cubic Hénon chirp produces a genuine
Poisson-boundary/scaling-site index, or whether the proposed anomaly is
either exactly trivial or not determinant class.

## Status

`COHERENT AFTER REFRAMING / EXTRA ASSUMPTION`

The original phrase “Poisson-boundary index” was too broad because the
Poisson map can be noninjective.  The coherent theorem has two exact parts:

- functorial scaling-site descent is equivariantly trivial;
- the standard Hardy restricted-unitary escape is obstructed.

A separately constructed nonfunctorial Poisson quotient remains outside the
theorem.

## Invariant Object

The invariant object is the equivariant class of the unit-modulus scalar
cocycle

\[
c(a,x)=\phi(ax)\phi(x)^{-1},
\qquad \phi(x)=\psi(P_0(x)),\qquad P_0(x)=2x^3,
\]

together with any index obtained by descending or compressing it.  The
question is whether this class survives the scaling quotient, not whether
its Mellin transform has an attractive formula.

## Assumptions

1. The adelic additive character is the standard character of
   \(\mathbb A_{\mathbb Q}/\mathbb Q\).
2. Rational and idele scalings act by half-density dilation.
3. A “functorial descent” preserves equivariant isomorphisms.
4. The pre-Poisson boundary functionals are continuous on the chosen
   Schwartz/Schwartz--Bruhat topology.
5. The Hardy obstruction uses the standard archimedean Hardy projection;
   compactness of its commutator with a bounded multiplier is governed by
   the classical VMO compact-commutator theorem.
6. No injectivity of the Poisson map on the two boundary directions is
   assumed.

## Notation

- \(\Gamma=\mathbb Q^\times\): rational scaling group.
- \(A=\mathbb A^\times\): idele scaling group.
- \(X=\mathbb A\), or any invariant locus on which the expressions are
  defined.
- \(D_a\): half-density dilation.
- \(M_\phi\): multiplication by \(\phi\).
- \(\Lambda_Q(f)=\int\psi(Q(x))f(x)\,dx\).
- \(V=\ker(ev_0)\).
- \(P_+\): the standard Hardy projection on \(L^2(\mathbb R)\).

## Derivation Strategy

First work on the transformation-groupoid atlas, where gauges can be tested
exactly.  Next compute the only intrinsic finite-codimension boundary-pair
index available before Poisson quotienting.  Finally test whether the gauge
can create a determinant-line anomaly after standard Hardy compression.

This order prevents a nonfunctorial compression from being silently called
a property of the original cocycle.

## Derivation Map

1. \(P_0\) gives the area-preserving Hénon map and scalar chirp.
2. Homogeneity gives the scaling increment
   \(P_0(ax)-P_0(x)\).
3. The increment is the groupoid coboundary \(\delta\phi\).
4. The same gauge trivializes rational descent and idele scaling.
5. Prime-loop products telescope to one.
6. The pre-Poisson boundary pair consists of two distinct hyperplanes and
   has index zero.
7. The cubic gauge is not VMO, so it is outside the standard restricted
   unitary group and supplies no Hardy determinant-line anomaly.
8. The exact Mellin formula is retained only as a strip-safety/triviality
   shadow.

## Main Derivation

### Step 1. Classical homogeneous Hénon map — identity

For

\[
S_0(q,Q)=qQ+2q^3
\]

and the convention \(p=-\partial_qS_0\), \(P=\partial_QS_0\),

\[
(Q,P)=(-6q^2-p,q)=H_0(q,p).
\]

Moreover

\[
DH_0(q,p)=
\begin{pmatrix}-12q&-1\\1&0\end{pmatrix},
\qquad \det DH_0=1.
\]

### Step 2. Scaling cocycle — identity

Let \(\phi(x)=\psi(2x^3)\).  Define

\[
c(a,x)=\frac{\phi(ax)}{\phi(x)}
=\psi\bigl(2(a^3-1)x^3\bigr).
\]

Then

\[
c(ab,x)=c(a,bx)c(b,x).
\]

Coefficientwise this is

\[
2((ab)^3-1)
=2(a^3-1)b^3+2(b^3-1).
\]

Thus \(c\) is a chronological scaling cocycle, but it is visibly the
coboundary \(\delta\phi\).

### Step 3. Simultaneous quotient trivialization — proposition

Twist the rational action on \(X\times\mathbb C\) by

\[
q\cdot(x,v)=
\left(qx,\frac{\phi(qx)}{\phi(x)}v\right),
\qquad q\in\Gamma,
\]

and lift idele scaling by the analogous formula

\[
a\cdot(x,v)=
\left(ax,\frac{\phi(ax)}{\phi(x)}v\right).
\]

The compatibility square commutes because both routes multiply by

\[
\frac{\phi(aqx)}{\phi(x)}.
\]

Now set

\[
T(x,v)=(x,\phi(x)^{-1}v).
\]

Then

\[
T\left(qx,\frac{\phi(qx)}{\phi(x)}v\right)
=(qx,\phi(x)^{-1}v),
\]

and the same equality holds for every \(a\).  Hence \(T\) simultaneously
conjugates rational descent and idele scaling to their untwisted actions.
The equivariant line bundle and its groupoid \(H^1\)-class are trivial.

This step is functorial: any construction that respects equivariant
isomorphism must send the Hénon decoration to the undecorated class.

### Step 4. Prime repetitions — identity

For a prime \(p\) and repetition \(r\), the raw exponent along successive
scales is

\[
\sum_{j=0}^{r-1}2(p^3-1)p^{3j}x^3
=2(p^{3r}-1)x^3.
\]

The endpoint gauge contributes

\[
P_0(x)-P_0(p^rx)=-2(p^{3r}-1)x^3.
\]

The total closed holonomy is therefore one.  The clock
\(r\log p\) remains the scaling-site clock, but the scalar Hénon weight is
trivial for every repetition.

### Step 5. Pre-Poisson boundary-pair index — proposition

Inside \(V=\ker(ev_0)\), put

\[
K_0=V\cap\ker\Lambda_0,
\qquad
K_a=V\cap\ker\Lambda_{-P_a},
\]

where \(P_a(x)=2a^3x^3\).  The restrictions of the two functionals to
\(V\) are independent.  Choose factorized adelic tests whose finite
components have nonzero integral and are supported in a compact open set
on which both finite characters are trivial.  The problem reduces to real
Schwartz functions in \(\ker(ev_0)\).  If a linear combination vanished
there, the resulting real distribution would be a multiple of \(ev_0\);
away from zero its smooth density would vanish.  A linear relation between
the smooth kernels \(1\) and \(e^{-i\tau a^3x^3}\) would give, at orders
zero and three,

\[
\alpha+\beta=0,
\qquad -i\tau a^3\beta=0,
\]

so \(\alpha=\beta=0\) when \(a>0\) and \(\tau\ne0\).

For

\[
W=K_0\cap K_a
\]

one has

\[
\dim(K_0/W)=\dim(K_a/W)=1.
\]

On a Hilbert completion where the two continuous functionals have Riesz
vectors \(u,v\ne0\), the hyperplanes are \(u^\perp,v^\perp\). Their
orthogonal projections obey

\[
P_{K_0}-P_{K_a}=p_v-p_u\in\mathcal S_1,
\qquad \operatorname{Tr}(P_{K_0}-P_{K_a})=1-1=0.
\]

Equivalently, the compression \(P_{K_a}|_{K_0}:K_0\to K_a\) is Fredholm
and has index zero.  This is the essential-codimension/relative-projection
index; the two infinite-dimensional hyperplanes are not called a Fredholm
pair under conventions that demand a finite-dimensional intersection.

Also \(M_\phi K_0\ne K_0\), so no automorphism of the boundary quotient is
induced without choosing an additional splitting.

This result is deliberately pre-Poisson.  After applying a noninjective
Poisson map, the two one-dimensional directions might collapse
asymmetrically.  No image-pair index is inferred here.

This firewall is necessary, not cosmetic.  Let
\(V=K\oplus\mathbb Ce_1\oplus\mathbb Ce_2\),
\(K_0=K\oplus\mathbb Ce_1\), and
\(K_a=K\oplus\mathbb Ce_2\).  A linear map that is the identity on \(K\),
sends \(e_1\) to zero, and sends \(e_2\) to a new vector \(f\perp K\) has

\[
E(K_0)=K,\qquad E(K_a)=K\oplus\mathbb Cf.
\]

The image projections have essential codimension \(-1\), even though the
preimage essential codimension is zero.  An explicit Poisson-kernel/equal-
collapse theorem is therefore genuinely required for any residual escape.

### Step 6. Standard Hardy anomaly is unavailable — proposition

At the real place use

\[
b(x)=e^{4\pi i x^3}.
\]

For an integer \(n\ge2\), let

\[
I_n=\left[n,n+\frac1{12n^2}\right]
\]

and rescale \(x=n+y/(12n^2)\).  Removing the constant phase gives

\[
4\pi(x^3-n^3)
=\pi y+\frac{\pi}{12n^3}y^2
+\frac{\pi}{432n^6}y^3.
\]

For \(0\le y\le1\), \(n\ge2\), and \(3<\pi<22/7\), the error beyond
\(\pi y\) is less than \(1/30\).  Since

\[
\left|\int_0^1e^{i\pi y}\,dy\right|=\frac2\pi<\frac23,
\]

the modulus of the average of \(b\) on \(I_n\) is less than \(7/10\).
Therefore

\[
\frac1{|I_n|}\int_{I_n}|b-b_{I_n}|^2\,dx
=1-|b_{I_n}|^2>\frac{51}{100}.
\]

But \(|I_n|\to0\).  Thus \(b\notin\mathrm{VMO}\).  The classical compact-
commutator theorem gives

\[
[P_+,M_b]\quad\hbox{noncompact}.
\]

Hence \(M_b\) is not in the standard restricted unitary group: at least
one off-diagonal Hardy block is noncompact, so the commutator is not
Hilbert--Schmidt.  The corresponding determinant line/index anomaly is
unavailable.

This does not classify an unspecified exotic polarization or a separately
constructed semifinite crossed-product index.

The same obstruction is present after passing to logarithmic scale.  For
\(\widetilde b(t)=e^{4\pi i e^{3t}}\), take

\[
J_T=[T,T+e^{-3T}/12].
\]

After rescaling, \(\widetilde b/\widetilde b(T)\) converges uniformly to
\(e^{i\pi u}\) on \([0,1]\), so the log-scaling Hardy symbol is also not in
VMO.

### Step 7. Mellin shadow — identity and interpretation

The homogeneous Mellin channels are

\[
\kappa_\pm^{(0)}(z)=
\frac13(4\pi)^{-z/3}\Gamma(z/3)e^{\pm i\pi z/6}.
\]

Thus

\[
A_0(z)=\frac23(4\pi)^{-z/3}\Gamma(z/3)\cos(\pi z/6),
\]

\[
B_0(z)=\frac23(4\pi)^{-z/3}\Gamma(z/3)\sin(\pi z/6).
\]

Neither channel has a zero or pole in \(0<\Re z<1\).  Dividing by the
fully derived homogeneous gamma--trigonometric kinematic factors leaves the
constant pair \((1,1)\), so the normalized relative anomaly is one.

This is an analytic shadow of the groupoid trivialization, not a new
dynamical determinant.

## Remarks and Interpretation

- Homogeneity repaired the unsafe C36 strip divisor but simultaneously made
  the scalar scaling lift transparently gauge exact.
- A coboundary can produce an anomaly only when the gauge is inadmissible for
  a chosen polarization.  The standard Hardy choice is indeed inadmissible,
  but in the wrong way: the commutator is noncompact, so no determinant-line
  index exists.
- The inherited scaling zeta remains mathematically valid; the Hénon
  decoration contributes no new prime holonomy.
- The next plausible object must be nonscalar.  A natural candidate is the
  three-channel Kummer/Tate lift forced by cubic homogeneity, where the
  degree-three channels are permuted rather than simultaneously removable
  by one scalar gauge.

## Boundaries and Non-Claims

- No proof of RH or of a Hilbert--Pólya operator is claimed.
- No index is claimed after an unspecified noninjective Poisson map.
- The theorem does not exclude a genuinely nonfunctorial quotient equipped
  with an independently proved bounded index map.
- The theorem does not exclude matrix-valued, graded, projective, or Kummer
  cocycles.
- The pointwise homogeneous Mellin factors are not promoted to an ordinary
  Fredholm determinant.
- The prime orbits and \(\log p\) clock remain imported from the scaling
  mother system.

## Open Risks

1. An exotic Poisson quotient could in principle kill the two boundary
   directions asymmetrically and carry a new index.  It would be a new
   construction and must state its kernel and trace theorem.
2. The VMO theorem addresses the standard Hardy polarization only.
3. The proposed \(\mathbb Z/3\)-graded pivot still needs a single fixed
   chronological operator and an all-prime compatibility theorem.
