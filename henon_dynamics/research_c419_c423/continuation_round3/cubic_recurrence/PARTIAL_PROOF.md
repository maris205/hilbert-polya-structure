# CR2: a proved infinite three-periodic fibre, not the full arithmetic atlas

Date: 2026-09-07 UTC. Current internal author calculation; no independent
review, manuscript admission, formal evaluation, or new C-number is claimed.

## Original claim and status

The [frozen contract](FROZEN_CONTRACTS.md) asks for an explicit,
necessary-and-sufficient classification of the ordinary periodic locus of

$$
M_A(x,y)=\left(y,\frac{Ay}{1+y^2}-x\right),\qquad A\in\mathbb Z,
$$

on **all** $\mathbb Q^2$, for **every** $A$, including singular invariant
fibres and exact least periods. The clock is one application of $M_A$.

**Original-claim status: NOT CURRENTLY JUSTIFIED.** The arguments below
prove specific partial results, not a replacement full theorem. The
unclosed step is stated in Section 8. There is no assertion that the
original classification is impossible or that its global priority is open.

## Assumptions, notation, and proved partial claim

Write

$$
I_A(x,y)=x^2y^2+x^2+y^2-Axy,\qquad
C_{A,K}: I_A(x,y)=K.
$$

Every rational orbit is defined for all positive and negative times because
$1+x^2$ and $1+y^2$ are nonzero over $\mathbb Q$. In particular,

$$
M_A^{-1}(x,y)=\left(\frac{Ax}{1+x^2}-y,x\right).
$$

**Partial theorem.** For $A=-5$, the set

$$
C_{-5,4}(\mathbb Q)
=\{(x,y)\in\mathbb Q^2:x^2y^2+x^2+y^2+5xy=4\}
$$

is infinite, and every one of its points has ordinary least period three
under $M_{-5}$. This map is not globally of finite order. Its invariant
fibre is birational over $\mathbb Q$ to the nonsingular elliptic curve

$$
E:\quad Y^2=X^3-74X^2+1625X.
$$

The infinitude proof uses the classical rational torsion bound and the
single already executed exact finite certificate in Section 6. It is
author computational evidence, not an independent certificate or a new
elliptic-curve theorem.

## Strategy and dependencies

1. Direct algebra proves invariance and a whole-fibre order-three identity.
2. Fixed points are excluded on the chosen fibre, making the period exact.
3. Explicit mutually inverse charts identify a rational open subset with
   an elliptic curve.
4. The exact addition certificate and Mazur's element-order bound show
   that one rational elliptic point has infinite order.
5. Its distinct multiples give infinitely many points on the fibre.

The supplementary singular-fibre calculation in Section 7 locates the
geometric exceptional levels; it does not classify their dynamics.

## 1. Invariance and the exact three-cycle identity

For fixed $y$, write $s=Ay/(1+y^2)$ and $w=s-x$. As a polynomial in $x$,

$$
I_A(x,y)=(1+y^2)x^2-Ayx+y^2.
$$

The substitution $x\mapsto s-x$ preserves this quadratic. Symmetry in
$x,y$ then gives

$$
I_A(y,w)=I_A(w,y)=I_A(x,y).
$$

A second identity, valid wherever $1+y^2\ne0$, is

$$
(1-xy)w+(x+y)
=\frac{y\bigl(I_A(x,y)+A+1\bigr)}{1+y^2}.                 \tag{1}
$$

Indeed, substituting $w=Ay/(1+y^2)-x$ makes the left-hand side

$$
\frac{y\{A(1-xy)+(1+x^2)(1+y^2)\}}{1+y^2},
$$

which is the right-hand side of (1).

Now set $A=-5$ and $I_A=4$. Equation (1) becomes

$$
x+y+w=xyw.                                                \tag{2}
$$

No real point of this fibre has $xy=1$: that equality would give
$I_{-5}=6+x^2+y^2\ge8$, not $4$. Invariance gives the same exclusion
for every consecutive pair. Consequently (2) determines

$$
w=-\frac{x+y}{1-xy}.
$$

Applied to the next pair $(y,w)$, equation (2) determines its next
coordinate as $x$, since $y+w+x=ywx$ and $1-yw\ne0$. Applied once more
it determines the coordinate $y$. Thus

$$
M_{-5}^3(x,y)=(x,y)\qquad\text{for every }(x,y)\in C_{-5,4}(\mathbb Q).
$$

The seed word is explicitly

$$
(1,1/2)\longmapsto(1/2,-3)\longmapsto(-3,1)\longmapsto(1,1/2).
$$

This already disproves an integrality shortcut for nonzero integer $A$.

## 2. The period is three, not merely a divisor of three

A fixed point of $M_{-5}$ must be $(u,u)$ with

$$
2u=-\frac{5u}{1+u^2}.
$$

Hence either $u=0$ or $u^2=-7/2$. The only rational fixed point is
$(0,0)$, whose invariant level is zero. There are no fixed points on
$C_{-5,4}(\mathbb Q)$. Because three is prime, Section 1 therefore proves
least period exactly three for every rational point on the chosen fibre.

## 3. Explicit elliptic charts

On the fibre introduce

$$
v=2(1+x^2)y+5x.
$$

Completing the square in its quadratic equation in $y$ gives

$$
v^2=-4x^4+37x^2+16.                                      \tag{3}
$$

For $x\ne0$, put

$$
u=\frac{v+4}{x^2},\qquad X=8u+37,\qquad Y=8x(u^2+4).
$$

Substitution into (3), followed by division by $x^2$, gives

$$
x^2(u^2+4)=8u+37=X.
$$

It follows that

$$
Y^2=64X(u^2+4)=X\bigl((X-37)^2+256\bigr),
$$

which is the displayed equation of $E$.

Conversely, for a rational point $(X,Y)$ of $E$ with $Y\ne0$, define

$$
x=\frac{8X}{Y},\qquad
v=\frac{X-37}{8}x^2-4,\qquad
y=\frac{v-5x}{2(1+x^2)}.                                  \tag{4}
$$

Here $X\ne0$, since $X=0$ implies $Y=0$ on $E$. The curve equation
implies $x^2(u^2+4)=X$ for $u=(X-37)/8$, so (3) holds. Equation (4)
then satisfies the original quadratic equation defining $C_{-5,4}$.
The factor $1+x^2$ is nonzero over $\mathbb Q$. Substitution recovers
both $X$ and $Y$, so these are mutually inverse rational charts.

The discriminant of the integral Weierstrass equation is

$$
\Delta=16\cdot1625^2\bigl((-74)^2-4\cdot1625\bigr)
       =-2^{14}\cdot1625^2\ne0.
$$

Thus its smooth projective completion, with point at infinity $O$, is
an elliptic curve over $\mathbb Q$. The point

$$
P=(125,1000)\in E(\mathbb Q)
$$

maps by (4) to $(1,1/2)$.

## 4. Infinite order and infinitely many rational three-periodic points

Mazur's rational torsion theorem implies that the order of any torsion
**element** of an elliptic curve over $\mathbb Q$ belongs to
$\{1,2,\ldots,10,12\}$. We use Theorem (7'), printed page 35, of the
[original paper](https://numdam.org/item/PMIHES_1977__47__33_0/), not a
bound of twelve on the cardinality of the whole torsion subgroup.

The frozen exact certificate computes $[n]P$ for $1\le n\le12$ and
verifies that none is $O$; see Section 6. Therefore $P$ is not torsion.
All positive multiples of $P$ are distinct. The only rational point
with $Y=0$ on $E$ is $(0,0)$, since

$$
X\bigl((X-37)^2+256\bigr)=0
$$

has only the rational root $X=0$. That point has order two, so no
nonzero multiple of the infinite-order point $P$ equals it or $O$.
The inverse chart (4) is consequently defined at every positive
multiple of $P$. Its injectivity supplies infinitely many distinct
points of $C_{-5,4}(\mathbb Q)$. Sections 1 and 2 prove that all have
least period three. This proves the partial theorem's infinitude claim.

## 5. This is not a globally finite-order map exception

The origin is fixed and the derivative there is

$$
DM_{-5}(0,0)=\begin{pmatrix}0&1\\-1&-5\end{pmatrix}.
$$

Its eigenvalues are $(-5\pm\sqrt{21})/2$, which are not roots of unity.
If a positive iterate of $M_{-5}$ were the identity rational map, its
derivative at this fixed point would have that same finite-order
property. This contradiction proves that $M_{-5}$ is not globally
of finite order.

For comparison, the exceptional parameter $A=0$ is elementary:
$M_0(x,y)=(y,-x)$, its square is $-(x,y)$, and every nonzero rational
point has least period four. The infinite three-periodic fibre above
shows why merely removing this global order-four exception cannot
rescue a finite-total-periodic-point hypothesis.

## 6. Single-execution exact certificate and its limits

The diagnostic was specified in the frozen contract **before** its only
execution. The program [check_fixed_fibre.py](check_fixed_fibre.py)
uses Python's exact `Fraction` arithmetic, explicit elliptic addition,
and explicit failure exceptions. It has no parameter sweep, point
search, dependency installation, subprocess, network call, or persistent
write. It imports no old research code.

For $E:Y^2=X^3+a_2X^2+a_4X$, the addition used is

$$
\lambda=\frac{Y_2-Y_1}{X_2-X_1},\qquad
X_3=\lambda^2-a_2-X_1-X_2,\qquad
Y_3=-Y_1+\lambda(X_1-X_3),
$$

with tangent slope $(3X_1^2+2a_2X_1+a_4)/(2Y_1)$ when doubling.
Identity and opposite-point cases are treated before division. The
certificate checks the curve equation after every addition. For every
one of the twelve resulting points it also checks (4), the original
fibre equation, the three-step return, and distinctness of the three
orbit points.

Recorded execution, not rerun during preparation of this document:

```text
cwd: /root/autodl-tmp/hilbert-polya-structure
command: python3 -B henon_dynamics/research_c419_c423/continuation_round3/cubic_recurrence/check_fixed_fibre.py
UTC: 2026-09-07T10:51:19.517499+00:00
Python: 3.12.3, Anaconda build, GCC 11.2.0
exit status: 0
status: PASS_FIXED_FIBRE_ONLY
tested multiples: 12
identity multiples: []
inverse-and-exact-period-three checks: 12
full_parameter_atlas_claimed: false
independent_review_claimed: false
script SHA-256:
88be3d20b4eadecc2d14d6c919ee7801872b2a1fe9890f3c36fe77831fc46882
canonical twelve-point-list SHA-256:
9ef47a8432efaef1f357984279d8d3ec7910f26abad04c7786f28f2a94e1c860
```

The first four reported multiples are

| $n$ | $X([n]P)$ | $Y([n]P)$ |
| --- | --- | --- |
| 1 | $125$ | $1000$ |
| 2 | $49$ | $140$ |
| 3 | $10125/361$ | $666000/6859$ |
| 4 | $9409/1225$ | $3968852/42875$ |

The list digest establishes identity of the computed list representation,
not correctness or an independent reconstruction. The twelve checks
become an infinitude proof only together with the stated torsion bound
and the explicit charts. They say nothing about other parameters or
whether this partial result is novel. No second execution was needed.

## 7. Exact geometric singular levels: a locator, not a dynamic atlas

For completeness, the closure of $C_{A,K}$ in
$\mathbb P^1\times\mathbb P^1$ is singular over $\mathbb C$ exactly when

$$
K\in\left\{0,-\frac{(A-2)^2}{4},-\frac{(A+2)^2}{4}\right\}.       \tag{5}
$$

To prove the affine part, let $F=I_A-K$. At a singular point,
$F=F_x=F_y=0$, and

$$
xF_x-yF_y=2(x^2-y^2)=0.
$$

Thus $y=x$ or $y=-x$. The zero solution forces $K=0$ and is singular
there. In the nonzero diagonal case $F_x=0$ gives
$x^2=A/2-1$, and substituting into $F=0$ gives
$K=-(A-2)^2/4$. On the nonzero antidiagonal, it gives
$x^2=-A/2-1$ and $K=-(A+2)^2/4$. Conversely these choices give
singular complex points; when their square roots vanish they reduce
to the already included origin at $K=0$.

There are no additional singular points at infinity. In the chart
$z=1/x$, the equation after multiplication by $z^2$ is

$$
y^2+1+z^2(y^2-K)-Azy=0.
$$

At $z=0$ its points have $y=\pm i$ and its derivative in $y$ is
$2y\ne0$. The other infinity chart has the exchanged calculation.
The double-infinity corner is not on the curve because its local
equation has constant term one. This proves (5).

For $A=-5$, the exceptional levels are $0,-49/4,-9/4$, so the
chosen level $4$ is not singular. Formula (5) has not been used to
claim that all rational points on exceptional components, their
normalizations, or their exact periods have been classified.

## 8. The unclosed global boundary and stop decision

The desired atlas still needs a uniform classification, as $A$ ranges
over all integers and $K$ over rational levels, of the torsion-translation
fibres that actually have rational points. It must identify their exact
translation orders, rational loci, and all exceptional parameters,
and must separately close the singular levels (5). No such complete
parameter/locus argument is supplied here.

The classical QRT reduction to genus-one translations, together with a
rational torsion bound, can produce bounded-order algebraic tests on a
given smooth fibre. That is not an explicit all-parameter rational-point
atlas. A finite list of equations, their numerical sampling, or the
phrase “solve the remaining rational-point conditions” does not prove
their uniform solution. Nor does the finite certificate in Section 6
control a varying family.

The [source audit](SOURCE_AUDIT.md) deducts the invariant, elliptic
translation mechanism, and torsion/division-polynomial machinery from
the proposed increment. The partial theorem is a useful exact failure
of a shortcut, but is a short application of classical structure, not
an independent paper-level closure. The full candidate is stopped at
the frozen unclosed-global-mechanism boundary. There is no new admission,
no third candidate, and no claim concerning target Euler factors,
root numbers, automorphy, or a Hilbert–Pólya correspondence.
