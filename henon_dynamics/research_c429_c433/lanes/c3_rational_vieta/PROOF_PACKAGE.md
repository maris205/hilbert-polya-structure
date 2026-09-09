# Rational Vieta: an elliptic obstruction to the integral atlas

## Claim

Let
$$
F_{n,a}(x_1,\ldots,x_n)
=(x_2,\ldots,x_n,x_2\cdots x_n+a-x_1),
\qquad n\ge3,\quad a\in\mathbb Z.
$$
One application is the native time step. Write $\operatorname{Per}_r(F,\mathbb Q)$
for points of exact native least period $r$.

The full positive rational affine-atlas question in
[FROZEN_QUESTION.md](FROZEN_QUESTION.md) is false. More precisely:

1. $\operatorname{Per}_2(F_{5,-1},\mathbb Q)$ is the infinite affine elliptic
   locus
   $$
   \{(u,v,u,v,u):u,v\in\mathbb Q,\ u^2v^2-u-v-1=0\}.
   $$
2. It is not a finite union of rational affine images of rational
   polyhedra, even allowing strict linear inequalities. More strongly,
   its elliptic completion admits no nonconstant rational map from any
   affine space over $\mathbb Q$, so finitely many rational-function
   charts with free rational parameters cannot replace those pieces.
3. It contains zero-free cycles whose denominator exponents at $2$ are
   unbounded. Consequently no fixed rational affine coordinate change
   sends the entire rational periodic set of $F_{5,-1}$ into
   $\mathbb Z_2^5$, and hence none sends it into $\mathbb Z^5$.
4. For every odd $n=2m+1$, the nonzero rational two-period locus has the
   exact denominator-stratum description in Step 2 below.

## Status

**PROVABLE AS STATED** for the four negative/structural assertions above.
The original positive atlas claim is **REFUTED**, not proved after a
denominator cutoff. No claim of a complete nonlinear classification of
all rational periods is made.

## Assumptions and notation

- All coordinates are ordinary rational numbers; no invariant level is
  fixed in the main assertion.
- $v_p$ is the additive valuation with $v_p(p)=1$.
- A rational polyhedron here means a subset of a finite-dimensional
  rational vector space defined by finitely many rational affine linear
  equalities and strict/non-strict inequalities. An allowed chart is its
  image under a rational affine map; parameters have no nonlinear
  constraints. This is more generous than C427's integer linear sets.
- For the stronger consequence, a **free rational-function chart** has
  finitely many coordinate functions in $\mathbb Q(t_1,\ldots,t_r)$,
  evaluated at every rational point of a nonempty rational polyhedron
  where their denominators do not vanish. Equivalently, first take the
  rational affine hull of that polyhedron and a rational map on this
  affine space, defined on a nonempty Zariski open subset; then restrict
  to its polyhedral parameter points. Its image is required to consist
  entirely of points of the labelled exact period. No elliptic equation,
  other nonlinear equation, integer-only condition, or additional
  arithmetic selection rule may be imposed on the free parameters.
  Empty charts contribute nothing and zero-dimensional charts are
  singletons. The proof rules out this stronger chart class as well.
- For odd dimension write $\iota(u,v)=(u,v,u,v,\ldots,u)$ and $s=uv$.
- $K=\sum x_i^2-\prod x_i-a\sum x_i$ is the original invariant.

## Strategy and dependency map

The counterexample is in the zero-free domain, not in an inherited
mixed-zero channel. Native period two gives a plane curve. Its elliptic
model supplies an explicit rational doubling sequence with forced
denominator growth; absence of affine lines then obstructs the atlas.

1. Step 1 uses only the original shift recurrence and its native clock.
2. Step 2 uses the nonarchimedean triangle inequality and unique-minimum
   valuation rule; it does not use C424 integrality.
3. Step 3 is a direct change of variables to a nonsingular cubic.
4. Step 4 uses the classical elliptic tangent law, with the needed
   formulas derived explicitly. Neither a rank oracle nor Lutz--Nagell
   nor an old/new numerical certificate is a proof dependency.
5. Step 5 is elementary polynomial and convexity reasoning for the
   frozen affine-atlas claim. Its stronger rational-function obstruction
   uses the classical Riemann--Hurwitz formula in characteristic zero.
6. Step 6 uses boundedness of a fixed affine image of $\mathbb Z_2^5$.
7. Step 7 checks the original level observable and the cross-level scope.
8. The final structural extension uses the classical genus formula for a
   squarefree hyperelliptic double cover; it is not needed for the
   affine-atlas counterexample or denominator growth.

## Proof

### Step 1. The full native two-period locus

An orbit is a bi-infinite scalar sequence satisfying
$$
x_{i+n}+x_i=\prod_{j=1}^{n-1}x_{i+j}+a.
\tag{1}
$$
If $F^2(P)=P$, shifting two native steps makes the whole scalar sequence
two-periodic: the first $n$ coordinates repeat, and (1) and its inverse
determine all other coordinates. Hence its word alternates $(u,v)$.
When $n=2m+1$, equation (1) is exactly
$$
u+v=(uv)^m+a.\tag{2}
$$
Conversely (2) makes $F$ interchange $\iota(u,v)$ and $\iota(v,u)$.
Their least period is two precisely when $u\ne v$.

For $m=2,a=-1$, equality $u=v$ would give $u^4-2u-1=0$.
A rational root of this monic integer polynomial is an integer dividing
its constant term, hence is $1$ or $-1$; neither is a root. Thus every
rational point of
$$
C:\quad u^2v^2-u-v-1=0\tag{3}
$$
has exact native period two. The two zero-containing pairs are $(0,-1)$
and $(-1,0)$; all points constructed below have no zero.

The explicit pair
$$
(u,v)=(21,-2/9)
$$
satisfies (2), since $(uv)^2-1=196/9-1=187/9=u+v$.
It is zero-free and its coordinate maximum is $21>5=|a|+4$.
Therefore C427's integral zero-free bound is false over $\mathbb Q$.

### Step 2. Exact denominator strata in every odd dimension

Assume $u,v\ne0$ satisfy (2), with $a\in\mathbb Z$ and $m\ge1$.
At a prime $p$, suppose a denominator occurs and order the two valuations
as $\alpha=v_p(u)\le\beta=v_p(v)$, with $\alpha<0$.
If $\alpha=\beta$, then
$$
v_p(u+v-a)\ge\alpha>2m\alpha=v_p((uv)^m),
$$
contradicting (2). If $\alpha<\beta$, the term $u$ is the unique
least-valuation term in $u+v-a$, so
$$
\alpha=m(\alpha+\beta),\qquad
(m-1)\alpha+m\beta=0.
$$
Since $\gcd(m,m-1)=1$, there is an integer $e\ge1$ such that
$$
\{v_p(u),v_p(v)\}=\{-me,(m-1)e\}.\tag{4}
$$
For $m=1$ the second valuation is zero, as (4) states. No division by
$a$ or nonzero-forcing assumption was used.

Consequently there are unique positive coprime integers $B,D$ and
nonzero integers $r,t$ such that
$$
u=\frac{D^{m-1}r}{B^m},\qquad
v=\frac{B^{m-1}t}{D^m},\qquad
\gcd(rt,BD)=1.\tag{5}
$$
Here $B^m$ and $D^m$ are the reduced positive denominators of $u$ and
$v$. Formula (4) proves the prescribed exact numerator exponents at
the other coordinate's denominator primes. Substitution into (2)
gives the exact integer equation
$$
rD^{2m-1}+tB^{2m-1}=(rt)^m+a(BD)^m.\tag{6}
$$
Conversely any data satisfying (5)--(6) give a nonzero rational solution
of (2), with precisely the denominators stated. Remove $u=v$ if exact
period two is required. Equations (5)--(6) are a complete arithmetic
stratification of this stratum, not a claim that finitely many $(B,D)$
suffice and not a solved free-parameter atlas.

### Step 3. The elliptic arithmetic is genuine

For $m=2$ and any integer $a$, put
$$
X=u,\qquad Y=u^2v.
$$
Equation (2) yields
$$
E_a:\quad Y^2-Y=X^3-aX^2.\tag{7}
$$
For $X\ne0$ the inverse is $u=X,v=Y/X^2$. Near $(X,Y)=(0,0)$
it can instead be written
$$
u=X,\qquad v=\frac{X-a}{Y-1},
$$
because $Y(Y-1)=X^2(X-a)$. The latter formula returns $(u,v)=(0,a)$.
Thus the affine curve (2) is isomorphic to the projective cubic $E_a$
with its point at infinity $O$ and the point $(0,1)$ removed.

For nonsingularity, set
$G(X,Y)=Y^2-Y-X^3+aX^2$.
An affine singularity would have $Y=1/2$ and
$X(3X-2a)=0$. The option $X=0$ is incompatible with $G=0$;
the option $X=2a/3$ gives $16a^3=27$, impossible for integer $a$.
At $O=[0:1:0]$, the derivative with respect to $Z$ of
$Y^2Z-YZ^2-X^3+aX^2Z$ equals $1$, so $O$ is nonsingular.
This is a nonsingular plane cubic with rational point $O$, hence an
elliptic curve. Its discriminant is $16a^3-27$.

For $a=-1$ the change $y=-Y$ gives the classical curve
$y^2+y=X^3+X^2$, recorded as LMFDB/Cremona $43.a1/43a1$.
Its established arithmetic is not a newly discovered elliptic curve or
rank theorem. The next step proves exactly the infinitude needed here
without importing database rank or generator claims.

### Step 4. A fully explicit infinite denominator tower

Work on $E_{-1}:Y^2-Y=X^3+X^2$. The rational point
$$
Q_0=(-3/4,-1/8)
$$
lies on it: both sides are $9/64$. If $Q=(X,Y)$ and $2Y-1\ne0$,
the tangent slope and doubled point are
$$
\lambda=\frac{3X^2+2X}{2Y-1},\qquad
X'=\lambda^2-1-2X,\qquad
Y'=1-Y+\lambda(X-X').\tag{8}
$$
Indeed substituting the tangent line in the cubic gives a cubic in its
abscissa, with $X$ as a double root and sum of roots $\lambda^2-1$;
the third root is $X'$. Reflection $Y\mapsto1-Y$ gives the displayed
$Y'$. In particular $Q'=(X',Y')$ is rational and on the same curve.
Since $(2Y-1)^2=4X^3+4X^2+1$, (8) simplifies to
$$
X'=\frac{X^4-2X-1}{4X^3+4X^2+1}.\tag{9}
$$
The numerator identity follows by subtracting
$(1+2X)(4X^3+4X^2+1)$ from $9X^4+12X^3+4X^2$.

Suppose $v_2(X)=-2e$ with integer $e\ge1$. The equation of $E_{-1}$
forces $v_2(Y)=-3e$: the right side has valuation $-6e$, and a
nonnegative valuation of $Y$ would make the left side integral.
Thus $v_2(2Y-1)=1-3e<0$, so the tangent denominator is nonzero.
In (9) the numerator has unique least valuation $-8e$, from $X^4$.
The denominator has unique least valuation $2-6e$, from $4X^3$;
this is less than $2-4e$ and $0$. Hence
$$
v_2(X')=-2e-2.\tag{10}
$$
Starting with $Q_0$ and recursively applying (8), all points $Q_k$
exist and
$$
v_2(X_k)=-2(k+1),\qquad v_2(Y_k)=-3(k+1).
$$
The pairs
$$
u_k=X_k,\qquad v_k=Y_k/X_k^2
$$
therefore satisfy
$$
v_2(u_k)=-2(k+1),\qquad v_2(v_k)=k+1.\tag{11}
$$
They are nonzero, unequal, and pairwise distinct, giving infinitely
many zero-free native two-cycles with unbounded denominator exponents.
The index $k$ enumerates different $F_{5,-1}$-cycles. Elliptic doubling
is an auxiliary construction of points, not an iterate of $F_{5,-1}$
and not a change of its native time unit; every constructed orbit still
has native least period two.
Distinct $k$ cannot represent opposite phases of the same cycle either:
each chosen $u_k$ has negative valuation while $v_k$ has positive
valuation, and the negative valuation changes with $k$.

### Step 5. No finite affine-linear atlas

The curve (3) contains no nonconstant affine line, even over
$\mathbb C$. If
$$
u=u_0+\alpha z,\qquad v=v_0+\beta z
$$
made (3) a polynomial identity in $z$, its coefficient of $z^4$
would be $\alpha^2\beta^2$, so one direction is zero.
If $\alpha=0,\beta\ne0$, the coefficient of $z^2$ forces $u_0=0$,
after which the coefficient of $z$ is $-\beta\ne0$, a contradiction.
The case $\beta=0,\alpha\ne0$ gives the same contradiction with
$u,v$ exchanged. Thus $\alpha=\beta=0$.

Now consider any allowed rational affine-polyhedral chart contained
in (3). If it has two distinct rational image points, choose rational
preimages of those points. All their rational convex combinations
belong to the parameter polyhedron, including in the presence of
strict inequalities. Their images supply infinitely many rational
points of one nonconstant line segment in (3). A degree-at-most-four
polynomial restricted to that line then has infinitely many roots,
so it vanishes identically, contradicting the preceding paragraph.
Every such chart therefore has at most one rational image point.
Finitely many charts cannot cover the infinitely many points from
Step 4.

An exact-period-labelled affine atlas for the entire rational periodic
set would, by keeping its charts labelled two and projecting to the
first two coordinates, provide just such a finite cover of (3).
Therefore the frozen full atlas claim is false. Exact-period labels
are part of the question; this argument does not assert a theorem
about arbitrary unlabelled countable unions.

There is a stronger obstruction that distinguishes this example from
the rationally parameterizable $n=3$ hyperbola. No nonconstant rational
map $\mathbb A^r_{\mathbb Q}\dashrightarrow E_{-1}$ exists, for any
$r\ge1$. If there were one, after restricting to a suitable rational
affine line in its domain it would give a nonconstant rational map
$\mathbb P^1\dashrightarrow E_{-1}$. Such a line exists: a
nonconstant rational coordinate function varies in at least one
variable, and its nonconstancy survives a choice of the remaining
rational coordinates outside the zero sets of finitely many nonzero
coefficient polynomials. A rational map from a nonsingular projective
curve to a projective nonsingular curve extends over its missing
points. The resulting map is a nonconstant finite separable morphism
of smooth projective curves in characteristic zero.
Riemann--Hurwitz would then read
$$
-2=\deg(f)(2\cdot1-2)+\deg(R)=\deg(R)\ge0,
$$
a contradiction. Thus every such rational-function chart is constant.
If free parameters are instead restricted by linear conditions, take
their rational affine hull; rational points of any nonempty relative
open polyhedral region are Zariski dense in that hull, giving the same
rational-map obstruction. To see the compatibility explicitly, all
linear alternating-coordinate relations and equation (3) hold on those
rational parameter points. Clearing the finitely many coordinate
denominators turns them into polynomial identities on the affine hull.
Thus the chart induces a rational map to the curve (3), and then to its
elliptic completion. If the five-coordinate image were nonconstant,
its first two coordinates would be nonconstant because of the
alternating-coordinate identities. The preceding no-map result applies.
A finite collection of these constant charts cannot cover Step 4's
infinite set. This does not preclude
Mordell--Weil descriptions using integer multiplication of group
generators; such descriptions are not fixed rational-function charts
in free rational variables.

### Step 6. No one-time affine denominator normalization

Let $T(z)=Az+c$ with $A\in\mathrm{GL}_5(\mathbb Q_2)$ and
$c\in\mathbb Q_2^5$. There is a finite lower bound on all coordinate
valuations of
$$
T^{-1}(\mathbb Z_2^5)=A^{-1}\mathbb Z_2^5-A^{-1}c,
$$
obtained by taking the minimum of the valuations of the finitely many
matrix and translation coefficients. The family in (11) has no such
bound. It cannot lie in this affine lattice. This proves the claimed
normalization obstruction even over $\mathbb Q_2$, and a fortiori for
any rational affine $T$ and the global integer lattice.

### Step 7. The level observable is not being held fixed

For a pair satisfying (2), direct substitution into the original
invariant, with $s=uv$, gives
$$
\begin{aligned}
K(\iota(u,v))
&=(m+1)u^2+mv^2-us^m-a((m+1)u+mv)\\
&=m s^{2m}+ma s^m-(2m+1)s.\tag{12}
\end{aligned}
$$
The second equality uses $s^m=u+v-a$. For $m=2,a=-1$,
$$
K=2s^4-2s^2-5s.
$$
On the tower (11), $v_2(s)=-(k+1)$, and the three displayed terms
have valuations $1-4(k+1)$, $1-2(k+1)$, and $-(k+1)$.
The first is uniquely least. Thus
$$
v_2(K(\iota(u_k,v_k)))=1-4(k+1).\tag{13}
$$
These are pairwise different rational invariant levels. No assertion
of infinitely many points on one level is made.

In fact, for any fixed odd dimension and fixed $a,D\in\mathbb Q$,
equation (12) permits at most $2m$ values of $s$, and (2) then permits
at most two ordered pairs for each $s$. The rational locus with period
dividing two on $K=D$ has at most $4m$ states, hence at most $2m$
exact native two-cycles. In dimension five this is at most eight
states. This finite-level statement does not bound or enumerate all
levels, and does not imply finiteness of all rational periodic points
on a level at other periods. This completes the main proof. ∎

## Additional structural consequence: the odd-dimensional genus ladder

This is a consequence of the same native period-two reduction, not a
replacement research question or a claimed rational-point algorithm.
For $n=2m+1$, the polynomial coordinate maps
$$
s=uv,\quad w=u-v,\qquad
u=(s^m+a+w)/2,\quad v=(s^m+a-w)/2
$$
are inverse isomorphisms between (2) and
$$
H_{m,a}:\quad w^2=(s^m+a)^2-4s.\tag{14}
$$
For integer $a$ and $m\ge2$ the degree-$2m$ polynomial on the right
is squarefree. A repeated root $s_0$ is nonzero, because a root at
zero requires $a=0$ and then the derivative at zero is $-4$.
The root and derivative equations at $s_0\ne0$ imply
$$
m^2s_0^{2m-1}=1,\qquad a=(2m-1)s_0^m,
$$
and therefore
$$
m^{2m}a^{2m-1}=(2m-1)^{2m-1}.
$$
Any prime divisor of $m$ divides the integer left side but not the
right side, a contradiction. Thus (14) is squarefree.

The smooth projective double cover of $\mathbb P^1_s$ is branched
at exactly the $2m$ finite roots and is unramified at the two points
over infinity. The Riemann--Hurwitz formula gives
$2g-2=-4+2m$, hence $g=m-1$.
Consequently the native two-period strata already exhibit genus one
at $n=5$ and genus at least two at every odd $n\ge7$; their arithmetic
does not reduce to choosing integral unit companions.
No ranks or complete higher-genus rational-point sets are determined.

## Corrections, missing assumptions, and open risks

- The positive rational affine-atlas claim is false, not merely missing
  the C427 maximum argument. Its replacement by unrestricted nonlinear
  arithmetic objects would be a different output contract.
- A finite cover over finitely many denominator pairs $(B,D)$ cannot
  cover the tower (11). A bound depending on one fixed level cannot
  cover the levels (13).
- This proof gives no all-period rational period bound or all-period
  rational enumeration. Individual-point periodicity decidability is
  not refuted; classical general results must be subtracted there.
- No statement that $E_{-1}(\mathbb Q)$ has rank exactly one, nor that
  the displayed doubling orbit exhausts it, is used in the proof.
- The elliptic group-law identities and genus formula are classical.
  The source-system embedding/denominator obstruction is what is being
  investigated for substantive admission; worldwide priority is not
  established by the bounded source search.
- The bare nonaffinity conclusion for the family including $n=3$ also
  follows from the elementary rational extension of C421's period-two
  hyperbola. That observation is subtracted, not advertised as a new
  full-family obstruction. The positive-genus rational-function
  obstruction at $n=5$, the explicit denominator growth, and the
  all-odd-dimensional valuation/genus structure are the increment.
- The proof has been self-checked symbolically, but no independent
  internal review or mathematical execution is claimed in this file.
- No target Euler factor, root number, automorphy, target zero
  correspondence, or Hilbert--Pólya conclusion follows from this
  source arithmetic. Route B is not entered.
