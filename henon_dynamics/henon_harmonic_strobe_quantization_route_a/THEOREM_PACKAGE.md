# C178 theorem package

Let

\[
H(q,p)=\frac{q^2+p^2}{2},\qquad
T_\theta(q,p)=
\bigl(q\cos\theta+p\sin\theta,
-q\sin\theta+p\cos\theta\bigr),
\]

where \(\theta\in\mathbb R\) is physical Hamiltonian time at unit
frequency.  The classical projection satisfies
\(T_{\theta+2\pi}=T_\theta\), but the physical-time parameter itself is not
quotiented: the quantum lift below retains the metaplectic sign.  Write
\(q-ip=re^{i\varphi}\).

## Theorem 1: all-angle classical fixed-set law

For every \(n\ge1\),

\[
T_\theta^n=T_{n\theta},\qquad
\operatorname{Fix}(T_\theta^n)=
\begin{cases}
\mathbb R^2,&n\theta\in2\pi\mathbb Z,\\
\{(0,0)\},&n\theta\notin2\pi\mathbb Z.
\end{cases}
\]

If \(\alpha=\theta/(2\pi)\) is irrational, the origin is the only
periodic point and

\[
\zeta_{\rm AM}(z)
=\exp\!\left(\sum_{n\ge1}\frac{z^n}{n}\right)
=\frac1{1-z}.
\]

If \(\alpha=a/b\) is reduced, then \(b\mid n\) is equivalent to
\(\operatorname{Fix}(T_\theta^n)=\mathbb R^2\).  Thus the classical
Artin--Mazur cardinality series is undefined.  For \(b>1\), every nonzero
point has exact least period \(b\); for \(b=1\), every point is fixed.

### Proof

The rotation group law gives \(T_\theta^n=T_{n\theta}\).  A nonidentity
planar rotation fixes only the origin, while the identity fixes the plane.
The irrational and reduced-rational conclusions follow immediately.  The
irrational zeta is the Taylor identity
\(-\log(1-z)=\sum_{n\ge1}z^n/n\).  At a rational resonance the required
fixed-point cardinality is uncountable, not a finite coefficient. \(\square\)

The involution \(S(q,p)=(q,-p)\) satisfies
\(ST_\theta S=T_{-\theta}=T_\theta^{-1}\).

## Theorem 2: invariant-Gaussian Koopman spectrum

Let

\[
d\gamma=\pi^{-1}e^{-(q^2+p^2)}\,dq\,dp,
\qquad U_\theta f=f\circ T_\theta .
\]

For \(m\in\mathbb Z\) and \(k\ge0\), define

\[
\psi_{k,m}(r,\varphi)=
\sqrt{\frac{k!}{(k+|m|)!}}\,
r^{|m|}L_k^{|m|}(r^2)e^{im\varphi}.
\]

Then \(\{\psi_{k,m}\}\) is an orthonormal basis of
\(L^2(\mathbb R^2,\gamma)\), and

\[
U_\theta\psi_{k,m}=e^{im\theta}\psi_{k,m}.
\]

For irrational \(\theta/(2\pi)\), the eigenvalues indexed by \(m\) are
distinct and dense on the unit circle, and each has countably infinite
radial multiplicity.  For reduced rational \(a/b\), the spectrum consists
of all \(b\)-th roots of unity, each again with countably infinite
multiplicity.

### Proof

Rotation preserves \(r\), hence \(\gamma\), and advances the frozen angular
coordinate \(\varphi\) by \(\theta\).  After \(x=r^2\), angular Fourier
orthogonality and

\[
\int_0^\infty e^{-x}x^{|m|}
L_k^{|m|}(x)L_\ell^{|m|}(x)\,dx
=\frac{(k+|m|)!}{k!}\,\delta_{k\ell}
\]

give the stated normalization and completeness.  The action follows from
the angular phase.  Irrational rotation powers are distinct and dense;
rational powers run through the \(b\)-th roots.  Varying \(k\) proves every
listed multiplicity is infinite. \(\square\)

Consequently \(U_\theta\) is noncompact for every angle, belongs to no
finite Schatten class, is not trace class, and has no ordinary determinant
\(\det(I-zU_\theta)\) for \(z\ne0\).  If \(V_Sf=f\circ S\) and \(K\) is
complex conjugation, then \(\Theta_G=V_SK\) is antiunitary and
\(\Theta_GU_\theta\Theta_G^{-1}=U_\theta^{-1}\).

## Theorem 3: natural same-clock quantum lift

On \(L^2(\mathbb R)\), let

\[
\widehat H=\frac12\left(-\frac{d^2}{dx^2}+x^2\right),
\qquad Q_\theta=e^{-i\theta\widehat H}.
\]

On the standard oscillator domain, \(\widehat H\) is self-adjoint.  Its
Hermite basis satisfies

\[
\widehat Hh_j=\left(j+\frac12\right)h_j,
\qquad
Q_\theta h_j=e^{-i\theta(j+1/2)}h_j.
\]

The operator family is defined for physical real time \(\theta\in\mathbb R\).
Since every \(j+1/2\) is half-integral,

\[
Q_{\theta+2\pi}=-Q_\theta,
\qquad Q_{\theta+4\pi}=Q_\theta.
\]

Thus this metaplectic lift is genuinely \(4\pi\)-periodic and only
projectively \(2\pi\)-periodic; it is not a single-valued unitary family on
\(\mathbb R/(2\pi\mathbb Z)\).  No global phase is discarded.  If the exact
real-time representative satisfies \(\theta/(2\pi)=a/b\) in lowest terms,
then its spectrum is

\[
e^{-i\pi a/b}\{e^{-2\pi i a r/b}:0\le r<b\},
\]

namely \(b\) rotated roots, each of infinite multiplicity.  Replacing
\(a\) by \(a+b\), which advances physical time by \(2\pi\), multiplies the
operator by \(-1\); replacing it by \(a+2b\) returns the operator exactly.

With \(\widehat p=-i\,d/dx\), the exact Egorov identities are

\[
Q_\theta^*\widehat qQ_\theta
=\widehat q\cos\theta+\widehat p\sin\theta,
\qquad
Q_\theta^*\widehat pQ_\theta
=-\widehat q\sin\theta+\widehat p\cos\theta.
\]

Complex conjugation gives \(KQ_\theta K=Q_\theta^{-1}\).  The unitary
\(Q_\theta\) is noncompact on an infinite-dimensional Hilbert space, belongs
to no finite Schatten class, and has no ordinary trace-class Fredholm
determinant.

### Proof

The Hermite equations diagonalize the functional calculus of
\(\widehat H\).  Substitution in the Hermite phases proves the stated
\(2\pi\) sign and \(4\pi\) return, including the dependence on the exact
real-time rational representative.  On the Schwartz core,
\([\widehat H,\widehat q]=-i\widehat p\) and
\([\widehat H,\widehat p]=i\widehat q\).  The Heisenberg equations therefore
integrate to the displayed rotation, using exactly the classical time
\(\theta\).  Conjugation fixes \(\widehat q\), negates \(\widehat p\), and
commutes with \(\widehat H\), which reverses the unitary phase.  Finally, the
Hermite images remain an orthonormal sequence, excluding compactness and all
finite Schatten classes. \(\square\)

For \(t>0\), \(e^{-t\widehat H}\) is a trace-class heat operator.  It uses
imaginary time, not the physical strobe clock.  Wick rotation, heat damping,
and Hermite truncation therefore define different objects and cannot be used
as determinants of \(T_\theta\), \(U_\theta\), or \(Q_\theta\).

## Route boundary

The strict tuple is

`(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`;
overall `ROUTE_A_REJECTED`.  The A4 theorem cannot repair A0--A3.  No target
zero or prime table, arithmetic local datum, Euler factor, root number,
automorphy object, target divisor, functional equation, counting law,
Hilbert--Pólya operator, or Route-B authorization enters this package.
