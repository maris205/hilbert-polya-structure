# HCS-C31 theorem package

## Status vocabulary

- **PROVED:** follows from the inherited exact certificates, explicit
  deductions, and locked theorem interfaces in this package.
- **NUMERICALLY CERTIFIED:** follows from the archived directed-rounding
  computer certificate and its independent checker.
- **NOT CLAIMED:** outside C31's proved scope.

## Frozen notation

\[
H_6(q,p)=(1-6q^2-p,q),
\qquad
DH_6(q,p)=
\begin{pmatrix}-12q&-1\\1&0\end{pmatrix}.
\]

In state order \((--,-+,+-,++)\),

\[
A=
\begin{pmatrix}
1&0&1&0\\
1&0&0&0\\
0&1&0&1\\
0&1&0&0
\end{pmatrix},
\qquad
\varphi=\rho(A)=\frac{1+\sqrt5}{2}.
\]

Let \(\Phi:\Sigma_A\to\Lambda_*\) be the inverse itinerary conjugacy.  Set

\[
r=\frac{123}{112},\qquad
a_0=\frac{112}{123},\qquad
\rho_0=\frac{\sqrt{17}-\sqrt{13}}2.
\]

If \((1,\mu^u(z))\) spans the normalized unstable line, define

\[
\lambda_u(z)=-12q-r\mu^u(z),\qquad
J^u_{\rm ad}=|\lambda_u|,\qquad
\tau_{\rm ad}=\log J^u_{\rm ad}.
\]

## Theorem 1. Exact realized-coordinate range -- **PROVED**

Every \(z_i=(q_i,q_{i-1})\in\Lambda_*\) satisfies

\[
\frac{\sqrt{17}}{12}
\le|q_i|
\le\sqrt{\frac38}=\frac{\sqrt6}{4}.
\]

### Proof

R059 gives

\[
q_i=\varepsilon_i
\sqrt{\frac{1-q_{i-1}-q_{i+1}}6}
\]

and the two radicand ranges

\[
\left[\frac5{18},\frac38\right],
\qquad
\left[\frac{17}{144},\frac{31}{144}\right].
\]

Taking the extreme endpoints proves the claim. \(\square\)

## Theorem 2. Self-consistent invariant slope -- **PROVED**

\[
\sup_{\Lambda_*}|\mu^u|\le a_0\rho_0,
\]

\[
J^u_{\rm ad}\ge
J_*:=\rho_0^{-1}
=\frac{\sqrt{17}+\sqrt{13}}2
=3.864328450540823\ldots ,
\]

and

\[
J^u_{\rm ad}\le
J^*:=3\sqrt6+\rho_0
=7.60724640342637\ldots .
\]

### Proof

The normalized derivative is

\[
D\widehat H_6=
\begin{pmatrix}-12q&-r\\a_0&0\end{pmatrix},
\]

so invariance gives

\[
\mu^u(H_6z)=\frac{a_0}{-12q-r\mu^u(z)}.
\]

Let \(M=\max_{\Lambda_*}|\mu^u|\).  The inherited cone gives \(M\le1/2\).
Theorem 1 implies

\[
M\le\frac{a_0}{\sqrt{17}-rM},
\]

or

\[
rM^2-\sqrt{17}M+a_0\ge0.
\]

The roots are \(a_0\rho_0\) and \(a_0/\rho_0\).  Since
\(M\le1/2<a_0/\rho_0\), the large branch is excluded and
\(M\le a_0\rho_0\).  Hence

\[
J^u_{\rm ad}\ge
\sqrt{17}-r(a_0\rho_0)
=\sqrt{17}-\rho_0
=\rho_0^{-1}.
\]

The upper bound follows from

\[
J^u_{\rm ad}
\le12\sqrt{3/8}+r(a_0\rho_0)
=3\sqrt6+\rho_0.
\qquad\square
\]

## Corollary 2.1. Coarse root bracket -- **PROVED**

There is a unique \(h_*>0\) with

\[
P_{\Sigma_A}(-h_*\tau_{\rm ad}\circ\Phi)=0,
\]

and

\[
\frac{\log\varphi}{\log J^*}
\le h_*
\le\frac{\log\varphi}{\log J_*}.
\]

Numerically,

\[
0.237155154771165\ldots
\le h_*
\le0.355981747990270\ldots .
\]

### Proof

The roof lies in \([\log J_*,\log J^*]\), so

\[
\log\varphi-s\log J^*
\le P(-s\tau_{\rm ad})
\le\log\varphi-s\log J_*.
\]

The positive roof makes pressure strictly decreasing. \(\square\)

## Theorem 3. Adapted/Euclidean coboundary -- **PROVED**

Define

\[
e^u_{\rm ad}(z)
=\left(\frac7{48},\frac{41}{256}\mu^u(z)\right),
\qquad
b_u(z)=\log\|e^u_{\rm ad}(z)\|_2.
\]

Then \(b_u\) is bounded Hölder and

\[
\tau_E^u(z)
:=\log\|DH_6(z)|_{E^u(z)}\|_2
=\tau_{\rm ad}(z)+b_u(H_6z)-b_u(z).
\]

For every \(H_6^nz=z\),

\[
\sum_{j=0}^{n-1}\tau_E^u(H_6^jz)
=\sum_{j=0}^{n-1}\tau_{\rm ad}(H_6^jz)
=\log|\Lambda_u(z,n)|,
\]

and

\[
P(-s\tau_E^u\circ\Phi)
=P(-s\tau_{\rm ad}\circ\Phi).
\]

### Proof

With

\[
S=\operatorname{diag}(7/48,41/256),
\qquad
D\widehat H=S^{-1}DH_6S,
\]

the invariant graph identity is

\[
D\widehat H(z)(1,\mu^u(z))
=\lambda_u(z)(1,\mu^u(H_6z)).
\]

Multiplying by \(S\) gives

\[
DH_6(z)e^u_{\rm ad}(z)
=\lambda_u(z)e^u_{\rm ad}(H_6z).
\]

Normalize, take Euclidean norms, and take logarithms.  Hölder regularity
follows from the Hölder invariant bundle and the nonzero first frame
component.  Periodic telescoping and pressure invariance under coboundaries
give the rest. \(\square\)

## Theorem 4. Local mixing basic set -- **PROVED**

\(\Lambda_*\) is compact, locally maximal, uniformly hyperbolic, and
topologically mixing for the \(C^\infty\) surface diffeomorphism
\(H_6:\mathbb R^2\to\mathbb R^2\).

### Proof

R059 gives compactness, invariance, and conjugacy with \(\Sigma_A\); R058
gives uniform hyperbolicity.  Strict square-root bounds put \(q_i\) in
\(\operatorname{int}X_{\varepsilon_i}\), while

\[
q_{i-1}\in\operatorname{int}X_{\varepsilon_{i-1}}
\subset\operatorname{int}Y_{\varepsilon_{i-1}}.
\]

Thus, for \(N=\bigcup N_{st}\) and \(U=\operatorname{int}N\),

\[
\Lambda_*\subset U,
\qquad
\operatorname{Inv}(U)=\operatorname{Inv}(N)=\Lambda_*.
\]

This is local maximality.  Moreover,

\[
A^4=
\begin{pmatrix}
4&2&2&1\\
2&2&1&1\\
2&1&2&1\\
1&1&1&1
\end{pmatrix}>0,
\]

so \(\Sigma_A\), and hence \(\Lambda_*\), is mixing. \(\square\)

## Theorem 5. Certified cylinder-pressure root -- **NUMERICALLY CERTIFIED**

Use centered length-\(13\) cylinders.  The chronological higher-block graph
has \(714\) length-\(12\) vertices and \(1156\) length-\(13\) edges.

For each edge \(e:u\to v\), the production certificate proves

\[
0<\tau_e^-
\le\tau_{\rm ad}(\Phi x)
\le\tau_e^+
\qquad(x\in[e]).
\]

For \(s\ge0\), define

\[
(L_s^-)_{uv}
=\sum_{e:u\to v}e^{-s\tau_e^+},
\qquad
(L_s^+)_{uv}
=\sum_{e:u\to v}e^{-s\tau_e^-}.
\]

Then

\[
\log\rho(L_s^-)
\le P_{\Sigma_A}(-s\tau_{\rm ad}\circ\Phi)
\le\log\rho(L_s^+).
\]

The outward-rounded Perron certificate gives

\[
\log\rho\!\left(L_{277980/10^6}^-\right)>0,
\qquad
\log\rho\!\left(L_{277987/10^6}^+\right)<0.
\]

Therefore

\[
\boxed{
\frac{277980}{10^6}
<h_*<
\frac{277987}{10^6}
}.
\]

### Proof

For \(s\ge0\),

\[
-s\tau_e^+
\le-s\tau(x)
\le-s\tau_e^-.
\]

Pressure is monotone in a real potential.  The pressure of a locally constant
edge potential is the logarithm of its chronological transfer matrix's Perron
root.  This proves the sandwich.  Positivity of every roof lower bound makes
the pressure strictly decreasing, so the two rational endpoint signs bracket
its unique zero. \(\square\)

## Corollary 5.1. Certified finite-section/pressure comparison -- **NUMERICALLY_CERTIFIED**

\[
\frac{277980}{10^6}
<
0.277982981676189\ldots
<
\frac{277987}{10^6}.
\]

Thus the independently obtained pressure certificate explains the old
positive finite-cycle-section signal to the certified resolution.

This does not prove that the finite cycle sections converge to an infinite
determinant.  Under a standard suspension-zeta continuation theorem, \(h_*\)
is the leading positive-real zeta pole and the inverse determinant has a zero
there.  That continuation is not part of Theorem 5.

The certified root is standard pressure geometry.  Containment makes the old
finite-section value consistent with that explanation at the stated
resolution, not a proof that the two quantities are identical.

## Theorem 6. Absolute instability-trace radius -- **PROVED**

Let

\[
B_n(1)=
\sum_{x\in\operatorname{Fix}(\sigma^n)}
e^{-\tau_n(x)}.
\]

Then

\[
B_n(1)\le\operatorname{tr}(A^n)J_*^{-n},
\]

so

\[
\sum_{n\ge1}\frac{z^n}{n}B_n(1)
\]

converges absolutely for

\[
|z|<
R_{\rm inst}:=\frac{J_*}{\varphi}
=\frac{\sqrt{17}+\sqrt{13}}{1+\sqrt5}
=2.388286326127446\ldots .
\]

At weight \(e^{-s\tau_n}\), the corresponding radius is at least
\(J_*^s/\varphi\) for real \(s\ge0\).

### Scope

This is the instability-weight trace.  It is not the BPS flat trace weighted
by \(|\det(I-DH_6^n)|^{-1}\).  The inherited radius
\((773/224)/\varphi=2.132\ldots\) is valid but weaker.  A separate scalar-BPS
radius near \(1.312\ldots\) concerns another determinant.

## Corollary 6.1. Uniform expansion cannot reach the root -- **PROVED**

At \(z=1\), the expansion majorant alone proves absolute convergence only for

\[
s>\frac{\log\varphi}{\log J_*}
=0.355981747990270\ldots .
\]

The certified interval for \(h_*\) lies below this threshold.  Effective
cylinder pressure, rather than a crude Euler-product majorant, is necessary.

## Theorem 7. Stable angle coboundary -- **PROVED**

Writing the normalized stable line as \((\nu^s,1)\),

\[
\sup|\nu^s|\le r\rho_0.
\]

If \(\alpha\) is the Euclidean stable/unstable angle, then

\[
\sin\alpha(z)
\ge\frac{1-\rho_0^2}{1+\rho_0^2}>0.
\]

With

\[
J_E^s(z)=\|DH_6(z)|_{E^s(z)}\|_2,
\qquad
\tau_E^s=-\log J_E^s,
\qquad
g=\log\sin\alpha,
\]

one has

\[
\tau_E^s=\tau_E^u-g+g\circ H_6.
\]

### Proof

The inverse graph transform gives the self-consistent stable bound exactly as
in Theorem 2.  Physical stable and unstable spanning vectors then give the
angle lower bound.  Finally, \(\det DH_6=1\) implies

\[
J_E^u(z)J_E^s(z)\sin\alpha(H_6z)=\sin\alpha(z),
\]

whose logarithm is the stated coboundary. \(\square\)

## Corollary 7.1. Bowen/Hausdorff interpretation -- **PROVED**

Pesin--Sadovskaya, “Multifractal Analysis of Conformal Axiom A Flows,”
Communications in Mathematical Physics 216 (2001), Remark 4.1 (printed page
284), states the map formula for a \(u\)-conformal diffeomorphism on a locally
maximal hyperbolic set:

\[
\dim_H(U\cap X)=t^u,
\qquad
P_X(f,-t^u\log b^u)=0.
\]

Here \(E^u\) is one-dimensional, hence the Euclidean derivative restricted to
\(E^u\) is conformal.  Theorem 4 gives a locally maximal hyperbolic set, and
Theorem 3 identifies its Euclidean unstable pressure with the certified
adapted pressure.  Therefore, for every appropriate local unstable piece,

\[
\dim_H(\Lambda_*\cap W^u_{\rm loc}(z))=h_*.
\]

Applying the same one-dimensional conformal statement to \(H_6^{-1}\) gives
the stable-slice root.  Theorem 7 shows that this root also equals \(h_*\).
Barreira, *Dimension Theory of Hyperbolic Flows* (Springer, 2013),
Introduction, Theorem 1.2, states that a locally maximal hyperbolic set of a
\(C^1\) surface diffeomorphism with
\(\dim E^s=\dim E^u=1\) has
\(\dim_H\Lambda=t_s+t_u\).  Its statement requires neither global Axiom A nor
a compact ambient surface.  Consequently,

\[
\dim_H\Lambda_*=2h_*,
\]

hence

\[
\frac{555960}{10^6}
<\dim_H\Lambda_*<
\frac{555974}{10^6}.
\]

### Scope audit

McCluskey--Manning's compact-surface/global-Axiom-A formulation is not used to
justify this corollary.  Its official 1985 erratum deletes the bifurcation
section, not its slice-pressure theorem, but neither fact is needed to broaden
its scope.  The exact local interfaces are the two theorem locators above.

## Theorem 8. BPS novelty boundary -- **PROVED BY SOURCE AUDIT**

For this analytic Hénon hyperbolic model, qualitative one-step-to-all-word
pinning, chronological iterated kernels, nuclearity of order zero, and the
flat-trace Fredholm identity are specializations of the classical
Baladi--Pujals--Sambarino framework.

C31 therefore claims none of those generic statements as new.  Potential
novelty begins with useful project-specific tails and the end-to-end certified
Hénon pressure interval.

## Route-A evaluation

The strict result is

~~~text
(A1_WEAK,
 A2_FAIL,
 A3_FAIL,
 A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED
Route B authorized: false
~~~

- **A1 weak:** no prime or von-Mangoldt correspondence.
- **A2 fail:** the full-cylinder pressure certificate is not a
  Fredholm-determinant zero theorem and gives no target spectral law.
- **A3 fail:** no completion, functional equation, critical-line symmetry, or
  global zero count.
- **A4 formal hint:** no self-adjoint Hilbert--Pólya operator.

Separately from Route A:

~~~text
pressure: NUMERICALLY_CERTIFIED
analytic_pressure_implication: PROVED
unstable_slice_dimension: PROVED
total_Hausdorff_dimension: PROVED
~~~

These theorem-ledger labels are not alternative Route-A grades.

The main C31 conclusion is negative for the old spectral narrative: the
certified pressure root supplies an ordinary geometric benchmark containing
the robust finite-section value at the stated resolution, without an equality
or convergence claim.
