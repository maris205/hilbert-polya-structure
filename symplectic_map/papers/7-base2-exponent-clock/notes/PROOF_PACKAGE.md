# Proof Package

Status: `PROVABLE_AS_STATED_WITH_OPEN_EQUALITY_RESIDUE`.

## Theorem A: local sharp-boundary lemma

Let \(F\) be a complete non-Archimedean field of characteristic zero and
residue characteristic two.  Let \(f(z)=z^2+c\) with \(0<|c|<1\).  Every
finite exact period-\(n\ge2\) point \(z\) satisfies \(|f^j(z)|=1\) for all
\(j\), and

\[
|(f^n)'(z)|=|2|^n.
\]

### Proof

If \(|z|>1\), then \(|f(z)|=|z|^2>|z|\), and the orbit cannot be periodic.
Thus every periodic point lies in the closed unit disk.  If one point of a
cycle lies in the open unit disk, then every forward point does because
\(|c|<1\).  For two distinct points \(x,y\) in that disk,

\[
|f(x)-f(y)|=|x-y|\,|x+y|<|x-y|.
\]

Applying this strict inequality around a nontrivial finite cycle contradicts
the equality of the initial and final distance.  Hence an exact cycle of
period at least two lies on the unit circle.  The chain rule gives

\[
(f^n)'(z)=2^n\prod_{j=0}^{n-1}f^j(z),
\]

whose norm is \(|2|^n\).  This proves Theorem A.

## Theorem B: frozen arithmetic corollary

Let \(u\) be a root of \(Q(U)=U^3-2U^2+2U-2\) and let
\(g(z)=z^2-u\).  Let \(C\) be a finite exact period-\(n\ge2\) cycle, let
\(L\) contain its coordinates, and let \(w\) be any place of \(L\) over the
unique place of \(K=\mathbb Q(u)\) above two.  Then every point of \(C\) is a
\(w\)-unit and

\[
w(\Lambda_C)=n\,w(2).
\]

If \(\Lambda_C\in\mathbb Q\), then

\[
v_2(\Lambda_C)=n,
\qquad \Lambda_C=2^n m\quad(m\in2\mathbb Z+1).
\]

### Proof

The polynomial \(Q\) is 2-Eisenstein.  Hence the completion
\(K_u/\mathbb Q_2\) is totally ramified of degree three, \(u\) is a
uniformizer, and \(|u|<1\).  Apply Theorem A after embedding the cycle field
in a completed algebraic closure.  If the multiplier is rational, the global
derivative-content theorem from Batch-01 Paper 2 gives
\(\Lambda_C/2^n\in\mathbb Z\).  Exact local valuation says this integer has
2-adic valuation zero, hence is odd.

An independent cross-check uses Rivera--Letelier's strict inequality theorem:
strictly larger rational 2-adic valuation would force the cycle to attract a
critical point.  Here \(\infty\) is fixed and

\[
0\mapsto-u\mapsto a=u^2-u\mapsto-a\mapsto-a,
\]

so neither critical point can be attracted to a distinct finite exact
period-\(n\ge2\) cycle.

## Lemma C: Frobenius--Hensel norm model

Write \(K_u\) for the completion at \((u)\).  The Eisenstein relation gives

\[
2=\frac{u^3}{u^2-u+1},\qquad v_u(2)=3.
\]

Let \(K_{u,n}/K_u\) be the unramified extension of degree \(n\), with
arithmetic Frobenius \(\sigma\).  Reduction gives

\[
g^n(X)-X\equiv X^{2^n}-X\pmod u,
\]

whose derivative is \(-1\).  Hensel uniqueness therefore associates each
\(\alpha\in\mathbb F_{2^n}\) to a unique periodic lift \(z_\alpha\).  The
\(2^n\) distinct residue classes yield \(2^n\) distinct lifts and exhaust the
degree-\(2^n\) polynomial \(g^n-X\).  If \(\alpha\) has exact Frobenius
degree \(d\mid n\), applying Hensel uniqueness to both \(g^d-X\) and
\(g^n-X\) shows that its lift has exact dynamical period \(d\).  Moreover,

\[
\sigma(z_\alpha)=g(z_\alpha).
\]

Exact dynamical period equals the Frobenius degree of \(\alpha\).  For exact
degree \(n\),

\[
B_C=\prod_{j=0}^{n-1}g^j(z_\alpha)
=N_{K_{u,n}/K_u}(z_\alpha).
\]

## Lemma D: mod-2 two-coefficient obstruction

In

\[
\mathcal O_{K_{u,n}}/(2)\simeq
\mathbb F_{2^n}[u]/(u^3)
\]

Hensel uniqueness and \(\sigma(z)=z^2-u\) give

\[
z_\alpha\equiv\alpha+u+u^2\pmod2.
\]

For \(\alpha_j=\alpha^{2^j}\), let \(e_k\) be the elementary symmetric
functions of \(\alpha_0,\ldots,\alpha_{n-1}\).  Since their product is one,

\[
B_C\equiv
1+e_{n-1}u+(e_{n-1}+e_{n-2})u^2\pmod2.
\]

Thus \(B_C=\pm1\) requires

\[
e_{n-1}=e_{n-2}=0.
\]

The relevant irreducible polynomials are

\[
T^2+T+1,\qquad T^3+T+1,\qquad T^3+T^2+1.
\]

Their indicated two coefficients cannot both vanish, so
\(\Lambda_C\ne\pm2^n\) for \(n=2,3\).  The obstruction is not all-period:
the irreducible degree-four polynomial \(T^4+T^3+1\) has the required two
low-order coefficients zero, while its irreducible reciprocal
\(T^4+T+1\) has the corresponding two highest nonleading coefficients zero.
Thus an exact degree-four Frobenius orbit passes the necessary filter.

## Lemma E: cycle-polynomial identity

For one exact cycle define \(P_C(X)=\prod_j(X-z_j)\).  Then

\[
P_C(g(X))=(-1)^nP_C(X)P_C(-X).
\]

With \(a=u^2-u\) and fixed point \(-a\), every \(n\ge2\) cycle satisfies
\(P_C(a)=(-1)^n\).  If additionally \(B_C=\varepsilon\in\{\pm1\}\), then

\[
P_C(-u)=P_C(u)=P_C(a)=(-1)^n,
\qquad P_C(0)=(-1)^n\varepsilon.
\]

These are necessary conditions only.  The single-cycle polynomial need not
lie in \(K[X]\), and no degree-independent contradiction is inferred.

## Repeat-closed boundary

Locally \(B_C\in K_u\).  The only roots of unity in the totally ramified
odd-degree extension \(K_u/\mathbb Q_2\) are \(\pm1\): the residue field has
no nontrivial odd-order torsion, while nontrivial higher 2-power roots of
unity require even local degree.  Consequently, if for some repetition
\(r\ge1\) the \(g^{nr}\) return multiplier of the original exact
period-\(n\) orbit is rational and has absolute value \(2^{nr}\), then
\(B_C^r=\pm1\), hence already \(B_C=\pm1\).  This does not reclassify the
point as exact period \(nr\), and it does not apply to a modulus-only
repetition without rationality.

## Exact open boundary

No argument above proves \(B_C\ne\pm1\) for every \(n\ge4\).  A finite
resultant or gcd ledger is not a substitute.  The all-period equality status
is therefore `OPEN`.
