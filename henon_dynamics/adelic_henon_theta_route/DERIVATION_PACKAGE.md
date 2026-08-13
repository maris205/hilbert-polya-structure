# Derivation package: adelic Hénon--theta symmetry and the Route-A mother model

## Target

Derive, without prime or zero fitting, a single global quantization of the
integral area-preserving Hénon map and prove that it presents the same
theta/scaling spectral range that carries the Riemann zeta divisor.

The target is deliberately split into two claims:

1. an exact Hénon compatibility theorem;
2. a conditional Hénon-essentiality bridge.

The first is proved here.  The second is the next large research gate.

## Status

`EXACT_MOTHER_COMPATIBILITY_PROVED; SCALING_COVARIANCE_GATE_OPEN`

Evidence labels:

- adelic unitarity: `PROVED`;
- finite spherical-vacuum invariance: `PROVED`;
- rational theta-distribution invariance: `PROVED`;
- equality of Hénon-adapted and standard scaling ranges: `PROVED` under the
  standard Poisson/Connes map and its usual domain;
- same-space compact relative perturbation: `REFUTED`;
- fixed-phase algebraic range-pair quotient bound: `PROVED`;
- conditional projection difference rank at most two: `PROVED` only if both
  images exist as closed subspaces of one Hilbert completion;
- promotion to dynamic two-channel scattering: `REFUTED` as an inference;
- new Hilbert--Pólya proof: `NOT_CLAIMED`;
- Hénon essentiality for the Riemann divisor: `REFUTED` for the vacuum
  channel and `OPEN` for non-vacuum relative channels.

## Invariant Object

Let \(\mathbb A=\mathbb A_{\mathbb Q}\) and let

\[
\psi:\mathbb A/\mathbb Q\longrightarrow\mathbb T
\]

be the standard nontrivial additive character.  The invariant object is the
pair

\[
\left(
L^2(\mathbb A),
\mathcal U_H=\mathcal F_{\mathbb A}\mathcal M_{P_6}
\right),
\qquad
P_6(q)=2q^3-q,
\]

together with the rational theta distribution

\[
\Theta(f)=\sum_{r\in\mathbb Q}f(r).
\]

The classical canonical relation of \(\mathcal U_H\) is exactly the Hénon
map \(H_6\).

## Assumptions

1. The additive Haar measure on \(\mathbb A\) is self-dual for \(\psi\).
2. Fourier transform uses the same sign convention at every place.
3. The adelic Poisson formula holds on \(\mathcal S(\mathbb A)\).
4. The scaling-site periodic-orbit theorem is imported from the audited
   Connes--Consani mother system:
   \(C_p=\mathbb R_+^*/p^{\mathbb Z}\) and \(\ell(C_p)=\log p\).
5. Any use of the Connes absorption spectrum is inherited prior art; it is
   not re-proved by the Hénon calculation.

## Notation

- \(v\): a place of \(\mathbb Q\), finite or archimedean.
- \(\psi_v\): the local component of \(\psi\).
- \(\mathcal F_v\): self-dual local Fourier transform.
- \(e_p=1_{\mathbb Z_p}\): the unramified spherical vector.
- \(I\): inversion on the scaling variable,
  \((IF)(x)=F(x^{-1})\), with the standard half-density convention.
- \(E=E_\times\): the full adelic nonzero-rational theta/scaling map,
  \[
  E_\times(g)(x)=|x|^{1/2}\sum_{r\in\mathbb Q^\times}g(rx).
  \]
  On an even real test function this is twice the positive-integer model
  \(E_+(g)(x)=|x|^{1/2}\sum_{n>0}g(nx)\). The Hénon chirp is not
  parity-preserving, so \(E_+\) is only an even-sector illustration and is
  not used to prove the mother-range identity.
- \(\mathcal S_0\): the usual double-zero Poisson test space.
- \(\mathcal S_H\): its Hénon-chirp pullback.

## Derivation Strategy

The derivation proceeds through four exact interfaces.

1. Recover the classical Hénon map from the generating function.
2. Quantize the generating function place by place and form a restricted
   tensor product.
3. Use the rational triviality of the global additive character to prove
   theta invariance.
4. Pull back the standard Poisson boundary conditions through the Hénon
   chirp and identify the scaling spectral range.

The discarded finite-field Euler product is treated separately by a
zero-accumulation theorem so it cannot be confused with the selected route.

## Derivation Map

\[
\begin{array}{ccccc}
S_6(q,Q)&\Longrightarrow&H_6(q,p)&\Longrightarrow&
\mathcal U_H=\mathcal F\mathcal M_{P_6}
\\
&&&&\Downarrow
\\
&&&\Theta\mathcal U_H=\Theta&
\quad \mathcal U_{H,p}e_p=e_p
\\
&&&&\Downarrow
\\
C_p,\ \ell_p=\log p&&
E\mathcal U_H(\mathcal S_H)=E(\mathcal S_0)&
\quad\text{(separate exact structures).}
\end{array}
\]

## Main Derivation

### 1. Classical map from the phase

Write

\[
S_6(q,Q)=qQ+P_6(q),
\qquad P_6(q)=2q^3-q.
\]

For the type-I convention

\[
p=-\partial_qS_6,
\qquad P=\partial_QS_6,
\]

we obtain

\[
p=-Q-(6q^2-1),
\qquad P=q.
\]

Therefore

\[
(Q,P)=(1-6q^2-p,q)=H_6(q,p).
\]

The Jacobian matrix is

\[
DH_6(q,p)=
\begin{pmatrix}
-12q&-1\\
1&0
\end{pmatrix},
\qquad \det DH_6=1.
\]

More generally, every rational polynomial \(P\) gives the exact symplectic
generalized Hénon map

\[
H_P(q,p)=(-p-P'(q),q).
\]

### 2. Local and global unitarity

At every place \(v\), define

\[
(\mathcal M_{P,v}f)(q)=\psi_v(P_6(q))f(q),
\]

and

\[
(\mathcal F_vf)(Q)=
\int_{\mathbb Q_v}\psi_v(qQ)f(q)\,dq.
\]

Both are unitary on \(L^2(\mathbb Q_v)\).  Hence

\[
\mathcal U_{H,v}=\mathcal F_v\mathcal M_{P,v}
\]

is unitary and has kernel \(\psi_v(S_6(q,Q))\).

For a finite prime \(p\), \(P_6(\mathbb Z_p)\subset\mathbb Z_p\), and the
standard character is trivial on \(\mathbb Z_p\).  Thus

\[
\mathcal M_{P,p}1_{\mathbb Z_p}=1_{\mathbb Z_p}.
\]

Self-duality of \(\mathbb Z_p\) gives

\[
\mathcal F_p1_{\mathbb Z_p}=1_{\mathbb Z_p},
\]

so

\[
\boxed{\mathcal U_{H,p}e_p=e_p.}
\tag{1}
\]

Equation (1) makes the restricted tensor product

\[
\mathcal U_H=\bigotimes_v'\mathcal U_{H,v}
\]

canonical on \(L^2(\mathbb A)\).  This is precisely what was absent from a
direct sum of growing finite-field fibres.

### 3. Exact theta invariance

Let \(g=\mathcal M_{P}f\).  Adelic Poisson summation gives

\[
\Theta(\mathcal U_Hf)
=\Theta(\mathcal Fg)
=\Theta(g).
\]

For every rational \(r\), \(P_6(r)\in\mathbb Q\).  Since the global
character is a character of \(\mathbb A/\mathbb Q\),

\[
\psi(P_6(r))=1.
\]

Consequently,

\[
\Theta(g)
=\sum_{r\in\mathbb Q}\psi(P_6(r))f(r)
=\sum_{r\in\mathbb Q}f(r)
=\Theta(f),
\]

and therefore

\[
\boxed{\Theta\circ\mathcal U_H=\Theta.}
\tag{2}
\]

This calculation works for every \(P\in\mathbb Q[q]\) for which the
restricted tensor product is defined.  Integral \(P\) has no finite bad
places.

### 4. Global repair of the generating-function gauge

For

\[
S'(q,Q)=S(q,Q)+G(Q)-G(q)+C,
\qquad G\in\mathbb Q[q],\ C\in\mathbb Q,
\]

the local kernels obey

\[
\mathcal U'_v
=\psi_v(C)\mathcal M_{G,v}\mathcal U_v\mathcal M_{G,v}^{-1}.
\]

Taking the restricted product gives

\[
\prod_v\psi_v(C)=1,
\]

so the global operator changes only by the endpoint conjugacy

\[
\mathcal U'_H
=\mathcal M_G\mathcal U_H\mathcal M_G^{-1}.
\tag{3}
\]

Thus the absolute constant-phase ambiguity that stopped the real fixed-phase
candidate C05 is absent in the adelic normalization.

### 5. Hénon pullback of the Riemann scaling range

The standard Poisson test space is

\[
\mathcal S_0=
\{g:g(0)=0,\ \widehat g(0)=0\}.
\]

Because \(\widehat g(0)=\int_{\mathbb A}g(x)\,dx\), define

\[
\mathcal S_H=
\left\{f:f(0)=0,\ 
\int_{\mathbb A}\psi(P_6(x))f(x)\,dx=0\right\}.
\]

Multiplication by the chirp is invertible, preserves the value at zero, and
turns the second Hénon condition into \(\widehat g(0)=0\).  Hence

\[
\mathcal M_P:\mathcal S_H\overset{\sim}{\longrightarrow}\mathcal S_0.
\tag{4}
\]

With \(E=E_\times\), the Poisson intertwining identity is

\[
E\mathcal F=I E
\quad\text{on }\mathcal S_0.
\tag{5}
\]

Using (4) and (5),

\[
\begin{aligned}
E\mathcal U_H(\mathcal S_H)
&=E\mathcal F\mathcal M_P(\mathcal S_H)\\
&=I E(\mathcal S_0)\\
&=E\mathcal F(\mathcal S_0)\\
&=E(\mathcal S_0),
\end{aligned}
\tag{6}
\]

where the last equality uses Fourier invariance of \(\mathcal S_0\).

Equation (6) is the exact mother-route theorem: the Hénon-adapted input has
the same scaling spectral range as the standard Poisson input.

### 6. Prime closed orbits and the missing coupling theorem

The scaling site has one primitive periodic orbit \(C_p\) for each rational
prime, with

\[
C_p=\mathbb R_+^*/p^{\mathbb Z},
\qquad \ell(C_p)=\log p.
\]

Separately, equation (1) proves that the finite Hénon unitary fixes the
spherical vacuum.  The scaling mother system itself has

\[
Z_{\mathrm{scale}}(s)
=\prod_p\left(1-e^{-s\ell(C_p)}\right)^{-1}
=\prod_p(1-p^{-s})^{-1}
=\zeta(s)
\tag{7}
\]

for \(\operatorname{Re}s>1\), followed by the standard Tate/Poisson
completion and continuation.

Equation (7) is prior art for the scaling system, not yet a dynamical-zeta
identity for a combined scaling/Hénon system.  No bundle or cocycle has been
constructed whose holonomy around \(C_p\) is \(\mathcal U_{H,p}\).  The
current statement is only formal trivial-vacuum compatibility, and this
missing chronological coupling is a Route-A gate.

### 7. Why the raw finite-field critical-line product is impossible

Let \(U_p\) be any \(p\)-dimensional unitary and write its eigenvalues as
\(e^{i\theta_{p,j}}\).  A local zero of

\[
\det(I-p^{1/2-s}U_p)
\]

has the form

\[
s=\frac12+i\frac{\theta_{p,j}+2\pi k}{\log p}.
\]

Choose \(k\) so \(|\theta_{p,j}+2\pi k|\le\pi\).  For each \(p\), all
\(p\) eigenphases then contribute zeros in

\[
\left|s-\frac12\right|\le\frac{\pi}{\log p}.
\]

As \(p\to\infty\), these zeros accumulate at \(1/2\).  A nonzero
meromorphic function cannot have such an interior zero accumulation point.
Thus local unitarity does not produce an RH candidate; it destroys global
meromorphicity unless an exact cross-prime cancellation is first proved.

### 8. Exact local dilation theorem and the same-space no-go

Fix \(p>3\), normalize \(\operatorname{vol}(\mathbb Z_p)=1\), and put

\[
I_{p,m}=\int_{p^{-m}\mathbb Z_p}\psi_p(2x^3-x)\,dx.
\]

The phase is constant on cosets of \(p^{2m}\mathbb Z_p\).  Thus

\[
I_{p,m}=p^{-2m}S_{p,m},
\]

where

\[
S_{p,m}=\sum_{u\bmod p^{3m}}
\exp\!\left(
2\pi i\frac{2u^3-p^{2m}u}{p^{3m}}
\right).
\tag{8}
\]

Write the highest base-\(p\) digit as
\(u=v+b p^{3m-1}\).  Summation over \(b\bmod p\) vanishes unless

\[
6v^2\equiv0\pmod p.
\]

Since \(p>3\), this forces \(v\equiv0\pmod p\).  Substituting \(v=pw\)
removes three powers of \(p\) from the phase denominator.  One remaining
digit of \(w\) is free, and hence

\[
S_{p,m}=p^2S_{p,m-1},
\qquad S_{p,0}=1.
\tag{9}
\]

Therefore

\[
\boxed{I_{p,m}=1\quad(p>3,\ m\ge0).}
\tag{10}
\]

Let

\[
e_{p,m}=p^{-m/2}1_{p^{-m}\mathbb Z_p}.
\]

These are unit vectors and \(e_{p,m}\rightharpoonup0\).  Equation (10)
gives

\[
\langle e_{p,m},\mathcal M_{P_6}e_{p,m}\rangle=p^{-m},
\]

so

\[
\|(\mathcal M_{P_6}-I)e_{p,m}\|^2=2-2p^{-m}\longrightarrow2.
\tag{11}
\]

A compact operator sends a weakly null bounded sequence to a norm-null
sequence.  Hence

\[
\boxed{\mathcal M_{P_6}-I\text{ is not compact on }L^2(\mathbb Q_p).}
\tag{12}
\]

This closes the naive same-space relative Fredholm route.

### 9. Static fixed-domain range-pair bound

The correct comparison keeps the input domain fixed.  In the adelic
Schwartz space let

\[
V=\{f:f(0)=0\},\qquad
\Lambda_0(f)=\int f(x)\,dx,
\]

and

\[
\Lambda_{-P}(f)=\int\psi(-P_6(x))f(x)\,dx.
\]

Then

\[
\mathcal S_0=V\cap\ker\Lambda_0,
\qquad
\mathcal M_P\mathcal S_0=V\cap\ker\Lambda_{-P}.
\tag{13}
\]

The common subspace

\[
W=V\cap\ker\Lambda_0\cap\ker\Lambda_{-P}
\]

satisfies

\[
\dim(\mathcal S_0/W)\le1,
\qquad
\dim(\mathcal M_P\mathcal S_0/W)\le1.
\tag{14}
\]

Apply the same linear map \(E\mathcal F\) and take closures.  If

\[
R_0=\overline{E\mathcal F(\mathcal S_0)},
\qquad
R_H=\overline{E\mathcal F(\mathcal M_P\mathcal S_0)},
\]

and \(C=\overline{E\mathcal F(W)}\), then both \(R_0/C\) and \(R_H/C\)
have dimension at most one.  Therefore their orthogonal projections, when
defined in the chosen scaling Hilbert completion, obey

\[
\boxed{\operatorname{rank}(P_H-P_0)\le2.}
\tag{15}
\]

This is a static fixed-phase theorem.  It does not imply that scaling
preserves a two-dimensional defect space, nor does it construct wave
operators or a scattering determinant.

### 10. Scaling covariance reopens infinitely many boundary directions

For the half-density dilation

\[
(D_af)(x)=|a|^{1/2}f(ax),
\]

one has

\[
D_a\mathcal M_{P_6}D_a^{-1}=\mathcal M_{P_a},
\qquad P_a(x)=2a^3x^3-ax.
\tag{16}
\]

Thus scaling moves the second boundary functional through

\[
\Lambda_{-P_a}(f)=\int\psi(-P_a(x))f(x)\,dx.
\]

Already at the archimedean place, the kernels

\[
\phi_a(z)=\exp[-2\pi i(2a^3z^3-az)],\qquad a>0,
\]

are linearly independent.  Indeed, a finite relation on the real axis
extends to an entire identity. Along \(z=re^{i\pi/6}\), the term with the
largest \(a\) has unique growth

\[
\exp(4\pi a^3r^3+O(r)),
\]

so its coefficient vanishes; descending induction removes every term.
Consequently

\[
\boxed{
\dim\operatorname{span}\{\Lambda_{-P_a}:a>0\}=\infty
\quad\text{before applying }E.
}
\tag{17}
\]

Equations (15) and (17) are compatible: every single pair has a static rank
bound, while the orbit of those rank-bounded pairs can sweep infinitely many
directions.  A finite dynamical channel now requires a new theorem about the
kernel of \(E\mathcal F\), a renormalized Poisson quotient, or a
crossed-product trace.

### 11. Exact Poisson boundary defect: the possible escape

The full adelic Poisson formula gives more structure than the static rank
count. For

\[
E_\times(g)(x)=|x|^{1/2}\sum_{r\in\mathbb Q^\times}g(rx),
\]

subtracting the zero term on both sides of Poisson summation yields

\[
\boxed{
E_\times(\widehat g)(x)
=E_\times(g)(x^{-1})
+|x|^{-1/2}g(0)-|x|^{1/2}\widehat g(0).
}
\tag{18}
\]

Now take \(g=\mathcal M_{P_a}f\) with \(f(0)=0\). Since \(P_a(0)=0\),

\[
\boxed{
E_\times(\mathcal F\mathcal M_{P_a}f)(x)
=E_\times(\mathcal M_{P_a}f)(x^{-1})
-|x|^{1/2}\Lambda_{P_a}(f).
}
\tag{19}
\]

Thus every fixed scale has only one outgoing Poisson defect *mode*, namely
\(|x|^{1/2}\), even though its coefficient functional
\(\Lambda_{P_a}\) ranges through an infinite-dimensional family. This is
the precise opening left by (17): the pre-Poisson orbit is infinite, but the
Poisson failure of inversion is geometrically rank one at each scale.

There are two important firewalls. First, (17) used the static hyperplane
family \(\Lambda_{-P_a}\), whereas (19) contains
\(\Lambda_{+P_a}\). The two families are separately infinite-dimensional
(by complex conjugation, or the opposite steepest-growth ray), but they are
not identified. Second, \(|x|^{\pm1/2}\) are boundary/asymptotic modes and
are not asserted to be vectors of the current scaling Hilbert completion.
Thus “one output mode” is a distributional Poisson statement, not a bounded
rank-one operator theorem.

Equation (19) does **not** prove that the full images
\(E_\times(\mathcal M_{P_a}f)\) have finite-dimensional orbit, nor that wave
operators or a determinant exist. It identifies the only plausible
compression mechanism: package the coefficient family as a cocycle over
the scaling action and ask whether its Mellin transform defines a
determinant-class boundary anomaly.

### 12. Current Route-A verdict and promotion gate

The strict current tuple is

\[
\boxed{
(A1_{\rm WEAK},A2_{\rm FAIL},A3_{\rm PARTIAL},A4_{\rm NATURAL})
}
\]

with overall status ROUTE_A_EXPLORATORY.  The scaling site supplies the prime
clock and inherited analytic structure; the Hénon map supplies the natural
unitary.  These cannot be combined by taking coordinatewise maxima.

The next promotion gate is now singular and explicit. Construct a genuine
scaling-site Hénon bundle/cocycle and prove that a Poisson-renormalized or
crossed-product anomaly determinant \(\Delta_H(s)\) exists. If one proves

\[
\Delta_H(s)\Delta_H(1-s)=1,
\qquad
\Delta_H(s)=e^{g_H(s)}\ne0
\]

with \(g_H\) entire and the same scaling clock, then

\[
D_H(s)=\xi(s)\Delta_H(s)
\]

has exactly the Riemann divisor and one scaling-covariant object carries the
Route-A layers. If the anomaly is a removable coboundary, the construction
is pure transport; if no determinant-class quotient exists or it has extra
zeros or poles, the route is obstructed.

## Remarks and Interpretation

1. Equation (2) is a nonlinear extension of the usual theta invariance
   calculation, but it is elementary once the adelic normalization is used.
2. The global character is doing real mathematical work: it simultaneously
   synchronizes all local phases and removes the rational constant gauge.
3. Equation (6) is stronger than a finite zero match.  It is an equality of
   ranges before any spectral truncation.
4. The construction supplies one global Hilbert space and one unitary, a
   substantial improvement over C32's varying finite-dimensional fibres.
5. The prime closed orbits are inherited from the scaling site, not generated
   by the real H6 horseshoe. A combined arithmetic Hénon extension remains to
   be constructed.
6. Equations (12), (15), and (17) separate three different statements:
   same-space noncompactness, a static pair bound, and a dynamically
   infinite scaling orbit.
7. Equation (19) supplies the first exact escape mechanism: the infinite
   family enters Poisson inversion through a common outgoing asymptotic
   mode, but determinant class remains open.

## Boundaries and Non-Claims

- No proof of RH is claimed.
- No new proof of the Tate functional equation or the Connes trace formula is
  claimed.
- The inherited scaling determinant is unchanged when the separate cubic
  decoration is removed.
- Theta invariance holds for a broad rational-polynomial family, so it is not
  unique to H6.
- Equality of scaling ranges does not by itself produce a new positive Weil
  form or a self-adjoint operator with discrete Riemann spectrum.
- The raw finite-field local factors are not local factors of the inherited
  scaling zeta.
- The finite-field operator on \(\ell^2(\mathbb F_p)\) and the local
  \(p\)-adic operator on \(L^2(\mathbb Q_p)\) must not be identified.
- The current Route-A tuple is exploratory, not a success verdict.
- Route B remains unauthorized.

## Open Risks

1. **Essentiality risk.** Every certified Riemann factor is presently
   inherited from the scaling mother system.
2. **Coupling risk.** The local Hénon unitary has not been promoted to
   holonomy of a scaling-site cocycle.
3. **Scaling covariance risk.** The boundary orbit is infinite-dimensional
   before Poisson quotienting; a new renormalized or crossed-product theorem
   is required.
4. **Positivity risk.** The Hénon unitary has not yet produced the positive
   form required to turn the absorption realization into an RH proof.
5. **Novelty risk.** The theta calculation may be known in a broader
   automorphic or Braverman--Kazhdan framework even though the explicit Hénon
   package was not found in the bounded search.
6. **Archimedean risk.** A nontrivial Hénon scattering channel may alter the
   gamma factor and introduce an uncontrolled divisor.

The next experiment should construct the scaling-covariant bundle/cocycle
and decide whether the rank-one boundary form in (19), after Mellin or
crossed-product completion, turns (17) into a determinant-class anomaly. It
should not return to prime scans or large finite transfer operators.
