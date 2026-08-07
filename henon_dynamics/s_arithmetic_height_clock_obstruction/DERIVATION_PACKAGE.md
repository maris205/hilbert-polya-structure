# Derivation package

This document gives the proof chain used by HCS-C16.  All inline and display
formulae use literal Markdown math delimiters so that the package can be read
independently of the compiled paper.

## 1. Arithmetic setup

Let

\[
B=(-1,3)_{\mathbb Q}
=\mathbb Q\langle i,j:i^2=-1,\ j^2=3,\ ij=-ji\rangle
\]

and let

\[
\mathcal O=\mathbb Z[1,i,j,ij].
\]

It is an order in \(B\), and

\[
\operatorname{nrd}(a+bi+cj+dij)=a^2+b^2-3c^2-3d^2.
\]

For an odd prime \(q\), the standard Hilbert-symbol formula shows that
\((-1,3)_q=1\) unless \(q=3\), where it equals \(-1\).  The \(2\)-adic
formula gives \((-1,3)_2=-1\), and the real symbol is \(+1\) because the
second entry is positive.  Therefore \(B\) is ramified exactly at \(2,3\).
In particular,

\[
B\otimes\mathbb R\simeq M_2(\mathbb R),
\qquad
B\otimes\mathbb Q_{13}\simeq M_2(\mathbb Q_{13}),
\]

the latter also following from \(3\equiv4^2\pmod {13}\).

Let \(G=\operatorname{PGL}_1(B)\).  The \(S\)-arithmetic lattice theorem
applied to the localized order gives

\[
\Gamma=P(\mathcal O[1/13]^\times)
<G(\mathbb R)\times G(\mathbb Q_{13})
\simeq
\operatorname{PGL}_2(\mathbb R)\times
\operatorname{PGL}_2(\mathbb Q_{13}).
\]

Since \(B\) is a division algebra, \(G\) is \(\mathbb Q\)-anisotropic, so the
quotient is uniform.

Put

\[
K=\mathbb Q(j)=\mathbb Q(\sqrt3),
\qquad
\mathcal O_K=\mathbb Z[\sqrt3],
\]

and define

\[
\varepsilon=2+j,\qquad \pi=4+j.
\]

Then

\[
N_{K/\mathbb Q}(\varepsilon)=1,\qquad
N_{K/\mathbb Q}(\pi)=13,
\]

and

\[
\varepsilon^{-1}=2-j,\qquad
\pi^{-1}=\frac{4-j}{13}.
\]

Both projective classes lie in \(\Gamma\).

## 2. The exact projective centralizer

### Proposition 1

The projective centralizer of \([\pi]\) in \(\Gamma\) is

\[
C_\Gamma([\pi])
=\mathcal O_K[1/13]^\times/\mathbb Z[1/13]^\times
\cong\mathbb Z^2,
\]

with basis \([\varepsilon],[\pi]\).

### Proof

Suppose \([x]\) centralizes \([\pi]\).  In \(B^\times\) this means

\[
x\pi x^{-1}=q\pi
\]

for some \(q\in\mathbb Q^\times\).  Reduced trace is invariant under
conjugation, while \(\operatorname{trd}(\pi)=8\), so \(8=8q\) and \(q=1\).
Thus \(x\) belongs to the ordinary centralizer of \(\pi\), which is the
quadratic field \(K\).  Moreover,

\[
\mathcal O[1/13]\cap K
=\mathcal O_K[1/13].
\]

The field \(K\) has class number one and

\[
\mathcal O_K^\times=\{\pm\varepsilon^m:m\in\mathbb Z\}.
\]

The factorization

\[
13=\pi\pi',\qquad \pi'=4-j,
\]

shows that every \(13\)-unit is

\[
\pm\varepsilon^m\pi^a(\pi')^b.
\]

Modulo rational \(13\)-units, \(\pi'\equiv\pi^{-1}\), while \(-1\) also
disappears.  Hence \([\varepsilon],[\pi]\) are a free basis. \(\square\)

Set

\[
\gamma_{m,n}=[\varepsilon^m\pi^n].
\]

The only rational class in this torus is \(\gamma_{0,0}\).  Indeed, a
rational class must have equal valuations at the two primes over \(13\), so
\(n=0\); then \(\varepsilon^m\) is rational only for \(m=0\).  Thus every
nonzero pair gives a regular element.  Its two real conjugates are positive,
so its reduced trace is nonzero.  Repeating the trace argument of Proposition
1 shows that its projective centralizer is the same \(K\)-torus.

For \((m,n)\ne(0,0)\),

\[
\gamma_{m,n}^k=\gamma_{km,kn}.
\]

Any projective root centralizes the element and therefore lies in this same
projective centralizer.  Consequently,

\[
\gamma_{m,n}\text{ is primitive}
\quad\Longleftrightarrow\quad
\gcd(m,n)=1.
\]

If two regular \(K\)-elements are conjugate in \(B^\times\), the conjugator
normalizes \(K\).  The quotient

\[
N_{B^\times}(K)/K^\times
\]

is the order-two Galois group.  Conjugation by \(i\) realizes its nontrivial
element and sends both generators to their projective inverses.  Therefore
the only identification among the lattice directions is

\[
(m,n)\sim(-m,-n).
\]

## 3. Exact joint Cartan lengths

For \(a+b\sqrt3\in K\), multiplication on the basis \((1,\sqrt3)\) is

\[
M(a,b)=
\begin{pmatrix}
a&3b\\
b&a
\end{pmatrix},
\qquad
\det M(a,b)=a^2-3b^2.
\]

Define

\[
A=2\log(2+\sqrt3),
\qquad
C=\log\frac{4+\sqrt3}{4-\sqrt3}.
\]

### Theorem 2 (rank-two clock)

After orienting the real axis and the \(13\)-adic apartment,

\[
\mathbf c(\gamma_{m,n})=(mA+nC,n).
\]

Hence

\[
\ell_\infty(\gamma_{m,n})=|mA+nC|,
\qquad
\ell_{13}(\gamma_{m,n})=|n|,
\]

and

\[
\det
\begin{pmatrix}
A&C\\
0&1
\end{pmatrix}
=A\ne0.
\]

### Proof

At the two real embeddings, the eigenvalue ratios of \(\varepsilon\) and
\(\pi\) are

\[
\frac{2+\sqrt3}{2-\sqrt3}=(2+\sqrt3)^2,
\qquad
\frac{4+\sqrt3}{4-\sqrt3},
\]

whose logarithms are \(A,C\).  Hensel's lemma lifts the two roots of
\(X^2-3\) congruent to \(4\) and \(-4\) modulo \(13\).  The two components
of \(\varepsilon\) are units.  Since \(N(\pi)=13\), the two components of
\(\pi\) have valuations \(0,1\).  Translation length on the Bruhat--Tits
tree is the absolute eigenvalue-valuation difference.  Additivity on the
torus proves the formula. \(\square\)

There is also a projectively invariant check.  Let \(x\) be
orientation-preserving hyperbolic at the real place, with positive reduced
norm \(N>0\), and split regular at a finite prime \(p\).  If

\[
t=\operatorname{trd}(x),\qquad
\Delta=t^2-4N,
\]

then

\[
\ell_\infty(x)
=2\operatorname{arcosh}\frac{|t|}{2\sqrt N},
\qquad
\ell_p(x)
=\max\{0,v_p(N)-v_p(\Delta)\}.
\]

For unequal finite-place eigenvalue valuations \(a<b\),
\(v_p(\Delta)=2a\) and \(v_p(N)=a+b\); equal valuations give zero
projective tree translation.  In our example,

\[
(t,N,\Delta)(\varepsilon)=(4,1,12),
\qquad
(t,N,\Delta)(\pi)=(8,13,12),
\]

which yields \((A,0)\) and \((C,1)\).

## 4. The periodic flat

For a bi-hyperbolic class \(\gamma\),

\[
\operatorname{Min}(\gamma)
=\operatorname{Axis}_\infty(\gamma)
\times\operatorname{Axis}_{13}(\gamma)
\cong\mathbb R^2.
\]

The centralizer lattice acts on this plane with translation basis
\((A,0),(C,1)\).  Therefore

\[
C_\Gamma(\gamma)\backslash\operatorname{Min}(\gamma)
\]

is a compact flat torus of area \(A\) in the chosen normalization.  It maps
to the arithmetic quotient as an immersed periodic flat; quotienting further
by the finite Weyl normalizer can give a torus modulo the inversion
orbifold.  In either description, a primitive lattice direction gives a
one-parameter family of parallel closed geodesics, not an isolated orbit.

The correct higher-rank trace datum is therefore

\[
\text{periodic flat}
+
\text{centralizer lattice}
+
\text{regulator/clean-fixed-set weight}.
\]

## 5. Primitive near-wall classes

### Theorem 3

There are coprime pairs \((m_k,n_k)\) such that

\[
|n_k|\longrightarrow\infty,
\qquad
|m_kA+n_kC|\longrightarrow0.
\]

### Proof

First \(C/A\notin\mathbb Q\).  A relation \(qC=rA\) would imply

\[
\left(\frac{\pi}{\pi'}\right)^q
=\left(\frac{\varepsilon}{\varepsilon'}\right)^r.
\]

At either prime of \(K\) over \(13\), the left side has nonzero valuation
when \(q\ne0\), whereas the right side is a unit.  This is impossible.

Let \(p_k/q_k\) be continued-fraction convergents of \(C/A\).  Then
\((m_k,n_k)=(-p_k,q_k)\) are coprime, \(q_k\to\infty\), and

\[
|m_kA+n_kC|=A|q_kC/A-p_k|=O(q_k^{-1}).
\]

This proves the claim. \(\square\)

The exact computation includes

\[
(-6,17),\ (-19,54),\ (-44,125),\ (-113,321),
\]

with real lengths

\[
0.0411391,\quad0.0242590,\quad0.00737883,\quad0.00212249.
\]

## 6. Euler-product consequences

Let \(\mathcal P_F\) be the primitive lattice directions modulo simultaneous
sign.  The real-only class product

\[
\prod_{(m,n)\in\mathcal P_F}
\left(1-e^{-s|mA+nC|}\right)^{-1}
\]

has no finite nonzero ordinary product under any enumeration when
\(\Re s>0\).  Along the sequence in Theorem 3,

\[
e^{-s|m_kA+n_kC|}\longrightarrow1,
\]

so the inverse local factors fail the necessary condition of approaching
one.

For real \(s,w>0\), the two-variable product

\[
Z_F(s,w)=
\prod_{(m,n)\in\mathcal P_F}
\left(1-e^{-s\ell_\infty-w\ell_{13}}\right)^{-1}
\]

does converge absolutely.  Indeed,

\[
\sup_{t\in\mathbb R}
\sum_{m\in\mathbb Z}e^{-sA|m-t|}<\infty,
\]

and the remaining sum over the canonical representatives \(n\ge0\) is
bounded by a geometric series in \(e^{-w}\).  The same bounds on compact
subsets justify termwise differentiation, giving

\[
\partial_s\partial_w\log Z_F(s,w)
=
\sum_{\mathcal P_F}\sum_{r\ge1}
r\ell_\infty\ell_{13}
e^{-r(s\ell_\infty+w\ell_{13})}>0.
\]

Thus \(Z_F\) cannot factor as \(F(s)G(w)\) in its convergence region.

## 7. The Weil-height clock

For \(\alpha=\varepsilon^m\pi^n\), let

\[
r_\gamma=\frac{\alpha}{\alpha'},
\]

well defined up to inversion by the projective class.  Its real logarithms
are \(x,-x\), where \(x=mA+nC\).  Its finite divisor is

\[
n(\mathfrak p-\mathfrak p')
\]

at the two degree-one primes over \(13\), so its two \(13\)-adic logarithms
are \(n\log13,-n\log13\).  All other finite local terms vanish.

With the standard normalized absolute values, the absolute logarithmic Weil
height is therefore

\[
h(r_\gamma)
=\frac12\bigl(|x|+|n|\log13\bigr).
\]

### Theorem 4 (canonical height identity)

\[
\boxed{
2h(r_\gamma)
=\ell_\infty(\gamma)+(\log13)\ell_{13}(\gamma).
}
\]

Thus

\[
H(m,n)=|mA+nC|+(\log13)|n|
\]

is a canonical proper scalar clock and

\[
H(km,kn)=|k|H(m,n).
\]

## 8. Primitive lattice asymptotics

The linear map

\[
(m,n)\longmapsto(x,y)=(Am+Cn,n)
\]

has determinant \(A\).

For joint boxes, the rectangle

\[
|x|\le X,\qquad |y|\le Y
\]

has area \(4XY\).  Visible lattice points have density \(6/\pi^2\), and
quotienting by simultaneous sign divides by two.  Hence, as
\(X,Y\to\infty\) with their ratio bounded away from \(0,\infty\),

\[
\#\{\ell_\infty\le X,\ell_{13}\le Y\}_{\mathrm{primitive}}/\{\pm1\}
\sim\frac{12XY}{\pi^2A}.
\]

For the height clock, the diamond

\[
|x|+(\log13)|y|\le R
\]

has area \(2R^2/\log13\).  The same visible-point argument gives

\[
N_H(R)
\sim
\frac{6}{\pi^2A\log13}R^2
\qquad(R\to\infty).
\]

The reported finite counts are reproducible numerical illustrations of these
proved asymptotics.  Their current cutoff decisions were independently
rechecked at high precision; the proof does not depend on those finite
tables.

## 9. Bounded-Hecke Weyl obstruction

Let \(M=\Gamma_0^+\backslash\mathbb H\) be the compact orientation-preserving
arithmetic orbifold from the unlocalized order, let \(\Delta_M\ge0\) be its
hyperbolic Laplacian, and let \(T_{13}\) be the normalized self-adjoint Hecke
operator associated with the \(13\)-double coset.  It is bounded and commutes
with \(\Delta_M\).

For bounded real Borel \(f\) and \(b\in\mathbb R\), define

\[
D_{b,f}=\sqrt{\Delta_M+1}+b f(T_{13}).
\]

This is a bounded self-adjoint perturbation of an operator with compact
resolvent, so it is self-adjoint with compact resolvent.  If

\[
C=|b|\,\|f(T_{13})\|,
\]

the min--max principle squeezes its counting function

\[
N_{D_{b,f}}(T)
=\#\{\lambda_j(D_{b,f})\le T\},
\]

with multiplicity, between the counts for \(\sqrt{\Delta_M+1}\) at
\(T-C\) and \(T+C\).  The surface Weyl law gives

\[
N_{D_{b,f}}(T)
\sim\frac{\operatorname{area}(M)}{4\pi}T^2.
\]

This cannot equal the Riemann--von Mangoldt \(T\log T\) order after a fixed
affine spectral change.

The theorem is scoped to the full compact spherical spectrum and bounded
functions of one fixed Hecke operator.  It does not cover a canonically
selected sparse projection, conductor growth, scattering resonances, or a
new unbounded operator derived from the height clock.
