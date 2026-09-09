# Adler singular-fibre classification: independent hand proof

## Claim and status

**PROVABLE AS STATED for the assigned singular-fibre statements below.**
The full NL424-3 all-fibre problem is not declared solved or admitted.
The original map and domain are fixed in [SCOPE.md](SCOPE.md).

Every level cubic is geometrically reduced and smooth at its three
points at infinity. Its complete geometric reducibility criterion is
given in Step 2. On each geometrically irreducible singular level:

- the unique singular point is rational, native-regular, and fixed;
- an explicit rational normalization has native action $M$ below;
- its smooth native rational periodic points have common least period
  $2$, $3$, $4$ or $6$ exactly in the respective finite-order cases;
- otherwise the singular point is the only native rational periodic point.

The bound $6$ is attained. Nodes and cusps, split or nonsplit tangent
directions, and coincident parameters are included. No normalization
point or pole is silently counted as an ordinary native point.

## Assumptions and notation

Use the rational parameters $t,a,b,\gamma$ and the cubic $C$ in
[SCOPE.md](SCOPE.md). Its projective closure is
$$
\overline C:\quad
F(U,V,Z)=UV(tZ-U-V)+aUZ^2+bVZ^2+\gamma Z^3=0.
$$
Whenever the level is geometrically irreducible and singular, denote
its singular point in pair-sum coordinates by $(r,s,k)$, where
$k=t-r-s$. In particular, this $s$ is a singular coordinate, not the
original level value $S_0$.

Write
$$
A=k-r-s,\qquad q(z)=-s+Az-rz^2,\qquad
\Delta=A^2-4rs=(r+k-s)^2-4rk.
$$
The parameter $z$ belongs to $\mathbb P^1$, with infinity allowed.
An equation such as $z=\alpha/\delta$ denotes the projective point
$[\alpha:\delta]$ when $\delta=0$.

## Strategy and dependencies

The proof uses the squarefree leading form, elementary line substitution,
projection through the singular point, and direct substitution in the
two Adler factors. Finite projective orders over $\mathbb Q$ are derived
from an eigenvalue ratio; no torsion theorem for elliptic curves is used.
The native domain is checked at **both** factors and for all forward
and backward ticks. Reducible and smooth levels remain with their
assigned reviewers.

## Proof

### Step 1. Reducedness and infinity

The degree-three homogeneous part of the affine polynomial is
$-uv(u+v)$, a product of three distinct linear forms over
$\overline{\mathbb Q}$. If a nonconstant polynomial factor occurred
with multiplicity at least two, its highest homogeneous part would
also occur with multiplicity at least two in this leading form.
This is impossible. Thus every affine cubic is geometrically reduced.
The projective equation has no component $Z=0$, so its closure is
reduced as well.

At infinity the three points are
$$
P_u=[1:0:0],\quad P_v=[0:1:0],\quad P_w=[1:-1:0].
$$
The partials in $U,V$ there are those of $-UV(U+V)$.
At $P_u$, $F_V=-1$; at $P_v$, $F_U=-1$; at $P_w$,
$F_U=F_V=1$. All three points are smooth, for every parameter value.

### Step 2. Exact reducibility criterion

A reducible cubic over an algebraically closed field has a linear
factor. Its leading linear form must divide $uv(u+v)$; hence its
affine line is $u=\rho$, $v=\rho$ or $u+v=\rho$ for some scalar $\rho$.
No line at infinity is a component by Step 1.

On $u=\rho$ the polynomial is
$$
-\rho v^2+\bigl(\rho(t-\rho)+b\bigr)v+a\rho+\gamma.
$$
It vanishes identically precisely when $\rho=0$, $b=0$, $\gamma=0$.
On $v=\rho$ the same coefficient comparison gives
$\rho=0$, $a=0$, $\gamma=0$.
On $u+v=\rho$, substitute $v=\rho-u$ to obtain
$$
-(t-\rho)u^2+\bigl(\rho(t-\rho)+a-b\bigr)u+b\rho+\gamma.
$$
Identical vanishing is equivalent to $\rho=t$, $a=b$,
$\gamma=-bt$. Therefore:
$$
\boxed{\quad
C\text{ geometrically reducible}\iff
(b=\gamma=0)\ \text{or}\ (a=\gamma=0)\
\text{or}\ (a=b,\ \gamma=-bt).
\quad}
$$
The corresponding linear components are $u=0$, $v=0$ and $w=0$.
Every such line is rational. All three conditions are sufficient by
the substitutions just given.

Consequently pairwise distinct $\beta_1,\beta_2,\beta_3$ force every
level to be geometrically irreducible. Parameter coincidence is
necessary, but not by itself sufficient, for reducibility: the indicated
level equation is also required. For all parameters equal, reducibility
occurs exactly at $\gamma=0$, giving the three distinct lines $uvw=0$.
This result classifies the factorization boundary, not the dynamics
on the reducible components.

### Step 3. The unique singular point and its native regularity

Assume now that $\overline C$ is geometrically irreducible and singular.
It has at most one geometric singular point. Indeed, the line through
two distinct singular points would meet the cubic with multiplicity at
least two at each: restriction of the cubic to that line would have
two double roots although its degree is at most three. It would
therefore vanish identically, producing a linear component. This
contradicts geometric irreducibility.

The singular point is affine by Step 1 and rational: its unique
geometric position is preserved by every automorphism of
$\overline{\mathbb Q}/\mathbb Q$. Denote it by $(r,s,k)$ as above.
The equations $F=F_u=F_v=0$ give
$$
a=s(r-k),\qquad b=r(s-k),\qquad
\gamma=rs(k-r-s).                                      \tag{1}
$$
All of $r,s,k$ are nonzero. If $r=0$, then $b=\gamma=0$;
if $s=0$, then $a=\gamma=0$; if $k=0$, then
$a=b=rs$ and $\gamma=-bt$. Each case contradicts Step 2.

Conversely, every triple $r,s,k\in\mathbb Q^\times$ defines an
irreducible singular level by $t=r+s+k$ and (1). The point $(r,s)$
is singular by substitution. None of the reducibility conditions
can hold: if $b=0$, then $s=k$ and $\gamma=-r^2s\ne0$; if $a=0$,
then $r=k$ and $\gamma=-rs^2\ne0$; if $a=b$, then $r=s$ and
$\gamma+bt=-rk^2\ne0$. Thus (1), with nonzero rational coordinates,
also parametrizes all the singular irreducible cases. An arbitrary
$\beta_2\in\mathbb Q$ then recovers
$\beta_1=\beta_2+b$, $\beta_3=\beta_2+a$ and
$h=\beta_2t-\gamma$.

The first Adler difference is $b=\beta_1-\beta_2$.
At the singular point its two-site denominator is $u=r\ne0$, and
$b/r=s-k$. The first factor fixes the point. For the second difference,
$$
\beta_1-\beta_3=b-a=k(s-r),
$$
the denominator is $w=k\ne0$, and again the factor fixes the point.
Both inverses do so too. Hence the singular point belongs to the full
native two-sided regular domain and has least period $1$. In original
coordinates it is
$$
\left(\frac{r+k-s}{2},\frac{r+s-k}{2},\frac{s+k-r}{2}\right).
$$
This conclusion includes a rational node with nonrational branches.

### Step 4. Explicit normalization and singular type

Translate $u=r+U_0$, $v=s+V_0$. Using (1), the cubic equation becomes
$$
-sU_0^2+(k-r-s)U_0V_0-rV_0^2-U_0V_0(U_0+V_0)=0.
$$
For a line $V_0=zU_0$ through the singular point, its remaining
intersection with the cubic is
$$
U_0=\frac{q(z)}{z(z+1)},\qquad V_0=\frac{q(z)}{z+1}.
$$
Thus the normalization map $\nu:\mathbb P^1\to\overline C$ is
$$
\boxed{
u(z)=\frac{(k-s)z-s}{z(z+1)},\quad
v(z)=\frac{z(k-r-rz)}{z+1},\quad
w(z)=\frac{(z+1)(rz+s)}z.}                              \tag{2}
$$
These formulas sum to $t=r+s+k$.

To see explicitly that the projective map has no missing point, put
$z=Y/X$. Its homogeneous coordinates in the $(u,v)$ projective plane are
$$
\bigl[((k-s)Y-sX)X^2:\ Y^2((k-r)X-rY):\ XY(X+Y)\bigr].
$$
They have no common zero, since $rsk\ne0$. The three parameters
$0,-1,\infty$ map to the three distinct points at infinity.
Away from the singular point, the inverse parameter is
$z=(v-s)/(u-r)$; a finite point with $u=r$ has $v=s$, by the
translated equation and $r\ne0$. The morphism is birational and its
smooth source is the normalization. In particular, rational smooth
affine points correspond bijectively to rational parameters excluding
infinity parameters and the preimages of the singular point.

Those singular preimages are precisely $q(z)=0$.
They are disjoint from $0,-1,\infty$, since
$q(0)=-s$, $q(-1)=-k$ and the leading coefficient is $-r$.
If $\Delta\ne0$, there are two distinct tangent directions and the
singularity is a node. If $\Delta=0$, the double root $z_0$ is neither
$0$ nor $-1$; locally $U_0$ has order two in $z-z_0$, while
$V_0-z_0U_0=(z-z_0)U_0$ has order three. This is a cusp.
No smoothness or splitting assumption on a tangent direction is hidden.

### Step 5. The native Möbius action

On pair-sum coordinates the first factor is
$$
(u,v,w)\longmapsto(u,w+b/u,v-b/u),
$$
with cancellation to the swap formula when $b=0$.
In translated slope coordinates, direct substitution in (2) gives
$$
M_{12}(z)=\frac{s(z+1)}{(k-s)z-s}.
$$
For example the two slopes at fixed $U_0$ obey
$z+z'=(A-U_0)/(r+U_0)$, so
$$
z'=\frac{A-rz-(1+z)U_0}{r+U_0}
=\frac{s}{z\,u(z)}.
$$
This equals the displayed $M_{12}$.

The second factor sends
$$
(u,v,w)\longmapsto(v-(b-a)/w,u+(b-a)/w,w).
$$
Substituting $b-a=k(s-r)$ and (2) gives
$$
M_{13}(z)=\frac{s}{rz}.
$$
For completeness the numerator and denominator of the transformed
slope reduce respectively to $s(z+1)^2/z$ and $r(z+1)^2$,
after writing $w=(z+1)(rz+s)/z$.

These identities hold on a dense open subset and hence define the
induced maps everywhere on the normalization. Their matrices have
determinants $-sk$ and $-rs$, both nonzero. The ordered **native**
transfer, without any parameter permutation or root-clock substitution,
therefore induces
$$
\boxed{
M(z)=M_{13}(M_{12}(z))
=\frac{(k-s)z-s}{r(z+1)},\qquad
\mathsf M=\begin{pmatrix}k-s&-s\\r&r\end{pmatrix}.}       \tag{3}
$$
Its determinant is $rk$ and its trace is $r+k-s$.
It is not the identity in $\mathrm{PGL}_2$, because $r,s\ne0$.
Its fixed-point equation is exactly $q(z)=0$, so it preserves each
normalization branch above the singular point.

### Step 6. Exact ordinary native domain

Let $H_0=\{0,-1,\infty\}$. These are exactly the normalization
parameters at projective infinity, not ordinary affine points.
For finite smooth affine points:

- if $b\ne0$, the first factor fails exactly when
  $u(z)=0$, at $z=s/(k-s)=M^{-1}(0)$;
- if $b-a\ne0$, the second factor fails exactly when
  its intermediate denominator $v-b/u$ vanishes.

To check the second condition without a hidden cancellation, substitute
(2) to obtain
$$
v-\frac bu=
\frac{kz\bigl((r+k-s)z+(r-s)\bigr)}
{(z+1)((k-s)z-s)}.                                    \tag{4}
$$
After excluding the infinity parameters and the first-factor pole,
its only possible additional zero is
$z=(s-r)/(r+k-s)=M^{-1}(-1)$.
Also $M^{-1}(\infty)=-1$.

If $b=0$, then $s=k$ and the formal extra first-factor parameter
$s/(k-s)$ is $\infty$, already excluded. If $b-a=0$, then $s=r$
and its formal extra second-factor parameter is $0$, already excluded.
Thus equal-parameter cancellations create no spurious deletions.
The full one-tick bad set on the normalization is precisely
$H_0\cup M^{-1}H_0$.

Since the two Adler factors are involutions on their regular domains,
requiring this condition at every integer iterate also verifies all
intermediate inverse operations. Therefore the exact smooth native
rational domain is
$$
\boxed{
\nu\!\left(\mathbb P^1(\mathbb Q)\setminus
\left(\{q=0\}\cup\bigcup_{j\in\mathbb Z}M^jH_0\right)\right).}             \tag{5}
$$
Here $\{q=0\}$ means its rational members when intersecting with
$\mathbb P^1(\mathbb Q)$. Add the unique ordinary singular point from
Step 3 separately. The singular preimages are fixed by $M$ and do
not meet $H_0$, so they are not hidden pole orbits.

Formula (5) specifies the entire two-sided native domain, not merely
the regular locus of a simplified transfer expression. It is infinite
orbit exclusion for an infinite-order $M$, but becomes a finite check
for each possible periodic smooth case below.

### Step 7. Complete periodic classification and maximum period

Set
$$
\eta=\frac{(r+k-s)^2}{rk}.
$$
The finite projective orders of the nonidentity matrix (3) are exactly
$$
\begin{array}{c|cccc}
\eta&0&1&2&3\\ \hline
\operatorname{ord}(M)&2&3&4&6.
\end{array}                                                       \tag{6}
$$
Here is a direct derivation over $\mathbb Q$. A finite nonidentity
projective-order matrix in characteristic zero is diagonalizable,
with eigenvalue ratio a root of unity $\zeta\ne1$. Then
$\eta=2+\zeta+\zeta^{-1}$. The number $\zeta+\zeta^{-1}$ is both
rational and an algebraic integer, so it is an integer; its absolute
value is at most two. The value $2$ would give $\zeta=1$ and is
excluded. The remaining values $-2,-1,0,1$ give orders $2,3,4,6$.
Conversely, each value in (6) yields that eigenvalue ratio and
distinct eigenvalues, so the indicated projective order follows.

If $\Delta=0$, then $\eta=4$ and the nonidentity matrix has a repeated
eigenvalue. Its nonzero nilpotent Jordan part persists under every
positive power in characteristic zero, so it has infinite order.
In particular every cuspidal case is included in the infinite-order
alternative.

For a diagonalizable infinite-order projective map, a periodic
parameter must be one of its two eigenlines: otherwise periodicity
would force an eigenvalue ratio to be a root of unity. For a
nonidentity parabolic map, conjugation to $z\mapsto z+1$ shows that
only its unique fixed parameter is periodic. In both cases the fixed
parameters are exactly $\{q=0\}$ and represent the singular point.
There are therefore no smooth native periodic points when $M$ has
infinite order.

If $M$ has finite order $m$ from (6), every parameter outside
$\{q=0\}$ has least period $m$: a smaller positive power fixing a
noneigenline would have to be scalar, contrary to minimality of $m$.
The complete ordinary periodic-point list on this singular level is
the singular fixed point, together with
$$
\boxed{
\nu\!\left(\mathbb P^1(\mathbb Q)\setminus
\left(\{q=0\}\cup\bigcup_{j=0}^{m-1}M^jH_0\right)\right),
\quad\text{each of least period }m.}                                \tag{7}
$$
Its original coordinates are recovered without ambiguity by
$$
(x_1,x_2,x_3)=
\left(\frac{u+w-v}{2},\frac{u+v-w}{2},\frac{v+w-u}{2}\right).
$$
Only finitely many rational parameters are removed in (7), so each
finite-order case contains infinitely many rational native smooth
periodic points.

### Step 8. A hand-checked sharp period-six example

Take $r=1$, $s=7$, $k=3$. Then $t=11$, $a=-14$, $b=4$,
$\gamma=-35$, corresponding to
$$
\beta=(4,0,-14),\qquad (S_0,h)=(11/2,35).
$$
The parameters are pairwise distinct, so the level is geometrically
irreducible by Step 2. The singular relations (1) hold, and
$\eta=3$, so $M(z)=(-4z-7)/(z+1)$ has projective order six.
The rational parameter $z=1$ has the explicit orbit
$$
1,\ -11/2,\ -10/3,\ -19/7,\ -9/4,\ -8/5,\ 1.
$$
None is $0,-1,\infty$, so (5) verifies all forward and inverse
factorwise regularity. Also $q(1)\ne0$, so this is a smooth ordinary
orbit, with least period six. Formula (2) gives the starting original
point $(5,-21/2,11)$. This is a finite hand substitution, not a
parameter census or mathematical program.

## Source and admission boundary

The reductions here are explicit elementary algebra, supplied as a
mathematical branch check rather than a worldwide novelty claim.
Existing Adler integrability and normalization/Möbius mechanisms remain
classical inputs to subtract in any paper assessment. No external theorem
about elliptic translation, a flex origin or rational elliptic torsion
was imported.

The reducible line/conic dynamics and all smooth invariant levels are
outside this assigned proof package. Their absence prevents this
document alone from closing the original all-fibre NL424-3 question.
No target Euler factor, root number, automorphy, zero/divisor
correspondence or Hilbert–Pólya realization is established.

## Verification status

The formulas were derived and checked by hand against the exact two
ordered factors, including both equal-parameter cancellations.
An additional current-team nonauthor hand check of Steps 4–7 and the
Step 8 example found no concrete error; its scope and boundary checks
are recorded in [READ_ONLY_CHECK.md](READ_ONLY_CHECK.md).
No numerical or symbolic program was run. This remains an independent
working proof package for coordinator scrutiny, not a formal evaluation
or author acceptance of an admitted contract.
