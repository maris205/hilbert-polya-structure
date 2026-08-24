# Theorem package — HCS-C126

## Definition

Let

\[
 f(x)=T_3(x)=4x^3-3x,
 \qquad F(x,y)=\left(f(x),\frac14y+x\right).
\]

For \(n\ge1\), write \(m=3^n\).

## Theorem 1 — complete all-period fixed-point atlas

For every \(n\ge1\),

\[
 f^n=T_m.
\]

Moreover, \(T_m(x)-x\) has exactly \(m\) distinct real roots.  Each root has
one and only one fiber coordinate that closes under \(F^n\).  Consequently

\[
 \#\operatorname{Fix}(F^n)=3^n.
\]

### Proof

The identity follows inductively from \(T_a(T_b(x))=T_{ab}(x)\), itself
immediate after setting \(x=\cos\theta\).

The equation \(T_m(x)=x\), with \(x=\cos\theta\) and
\(0\le\theta\le\pi\), is \(\cos(m\theta)=\cos\theta\).  Its two families are

\[
 \cos\frac{2\pi k}{m-1},\quad 0\le k\le\frac{m-1}{2},
 \qquad
 \cos\frac{2\pi k}{m+1},\quad 0\le k\le\frac{m+1}{2}.
\]

Each family is injective in the displayed range.  Because
\(\gcd(m-1,m+1)=2\), their intersection is precisely \(\{1,-1\}\).  The
union therefore contains

\[
 \frac{m+1}{2}+\frac{m+3}{2}-2=m
\]

points.  This equals the degree of \(T_m-x\).  At an interior root,

\[
 T_m'(x)=m\frac{\sin(m\theta)}{\sin\theta}=\pm m,
\]

whereas \(T_m'(\pm1)=m^2\).  Thus \((T_m-x)'\ne0\) at every root, proving
both completeness and simplicity.

Iteration of the affine fiber gives

\[
 y_n=4^{-n}y+\sum_{j=0}^{n-1}4^{-(n-1-j)}T_{3^j}(x).
\]

Since \(1-4^{-n}\ne0\), the closing coordinate is uniquely

\[
 y_*(x,n)=\frac{\sum_{j=0}^{n-1}4^{-(n-1-j)}T_{3^j}(x)}{1-4^{-n}}.
\]

If the base point has least period \(p\mid n\), its unique \(F^p\)-closing
coordinate is already fixed by \(F^n\); uniqueness shows that the two formulas
agree.  Because projection to the base cannot reduce period, the least period
is preserved.  This completes the proof.

## Corollary 2 — primitive orbits and zeta

Let \(E_n\) be the number of exact-period points and \(P_n\) the number of
primitive orbits.  Then

\[
 E_n=\sum_{d\mid n}\mu(d)3^{n/d},
 \qquad
 P_n=\frac1n\sum_{d\mid n}\mu(d)3^{n/d}.
\]

The orbit-owned Artin–Mazur zeta is

\[
 \zeta_F(z)
 =\exp\left(\sum_{n\ge1}3^n\frac{z^n}{n}\right)
 =\frac1{1-3z}
 =\prod_{\gamma\ \mathrm{primitive}}
   (1-z^{p_\gamma})^{-1}
\]

in the defining disk \(|z|<1/3\), with the rational expression giving its
meromorphic continuation.

## Theorem 3 — all-period stability and orientation

At a fixed point of \(F^n\),

\[
 DF^n=
 \begin{pmatrix}
 T_m'(x)&0\\
 c_n(x)&4^{-n}
 \end{pmatrix},
 \qquad
 c_n(x)=\sum_{j=0}^{n-1}4^{-(n-1-j)}(T_{3^j})'(x).
\]

There are two endpoint points with unstable multiplier \(m^2\),
\((m-3)/2\) interior points with multiplier \(+m\), and \((m-1)/2\)
interior points with multiplier \(-m\).  Every point is a hyperbolic saddle,
and

\[
 \det(I-DF^n)=(1-T_m'(x))(1-4^{-n})\ne0.
\]

The positive and negative unstable-orientation counts are
\((m+1)/2\) and \((m-1)/2\), respectively.

If \(\gamma\) is primitive of period \(p\), with unstable multiplier
\(\alpha_\gamma\), its \(r\)-fold repetition has eigenvalues
\(\alpha_\gamma^r\) and \(4^{-pr}\), hence

\[
 \det(I-DF^{pr})=(1-\alpha_\gamma^r)(1-4^{-pr}),
 \qquad
 \operatorname{or}(\gamma^r)=\operatorname{sgn}(\alpha_\gamma)^r.
\]

For \(p>1\), \(\alpha_\gamma=\pm3^p\).  At period one the two endpoint
orbits have multiplier \(9\), while the central orbit has multiplier \(-3\).
The negative-orientation counts satisfy

\[
 \frac{3^n-1}{2}
 =\sum_{\substack{p\mid n\\n/p\ \mathrm{odd}}}E_p^-.
\]

Möbius inversion over odd quotient divisors therefore gives

\[
 E_n^-=\frac12\sum_{\substack{d\mid n\\d\ \mathrm{odd}}}
 \mu(d)(3^{n/d}-1),
\]

so \(P_n^-=E_n^-/n\) and \(P_n^+=P_n-P_n^-\).

## Proposition 4 — exact negative controls

1. For \(F_1(x,y)=(T_3(x),y+x)\), the period-one closing equation is
   \(x=0\).  Thus \(x=0\) carries an entire fixed line, while \(x=\pm1\)
   has no closing fiber.  The stable determinant factor is \(1-1=0\).
2. For \(g(x)=4x^3-2x\),

   \[
   g^2(x)-x=x(2x-1)^3(2x+1)^3(4x^2-3).
   \]

   It has only five distinct real roots rather than nine.  The points
   \(\pm1/2\) form a neutral two-cycle, and

   \[
   g^2(x)-T_9(x)=x(192x^6-240x^4+80x^2-5)\ne0.
   \]

Both controls therefore destroy named hypotheses or conclusions rather than
merely perturbing a numerical score.

## Progress and boundary

Prior dynamics-variant papers repeatedly supplied finite word ledgers or one
low-period monodromy, while the global Fock owner had only a trivial recurrent
base.  C126 closes a different gate: a single nontrivial source now owns a
complete all-period real atlas, exact primitive counts, its Artin–Mazur zeta,
and stability/orientation/repetition laws.  It does *not* construct a weighted
nuclear transfer operator or compare a divisor with a target.  The strict
verdict is therefore

```text
(A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
route_b_invocation_allowed = false
```
