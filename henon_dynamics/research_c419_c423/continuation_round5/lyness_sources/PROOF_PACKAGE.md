# LY4 auxiliary: a coarse rational native-period bound

Date: 2026-09-08. Coordinator-authored dependency, not a separate candidate.
The [frozen scope](FROZEN_AUXILIARY_SCOPE.md) is unchanged.

## Claim and status

Let $a\in\mathbb Q$ and let $(x_i)_{i\in\mathbb Z}$ be a periodic sequence
of rational numbers satisfying
$$x_i x_{i+3}=a+x_{i+1}+x_{i+2},\qquad x_i\notin\{0,-1\}.$$
Then its native least period $N$ is at most $48$.

Auxiliary status: **PROVABLE AS STATED**, with explicit classical inputs
below; pending non-author internal review. This does not prove the original
all-integer LY4 atlas or its sharper proposed period exhaustion. The bound is
not claimed optimal, and its classical reduction is not claimed novel.

## Assumptions, notation and classical inputs

All maps are evaluated only along the stated ordinary orbit. Rational formulas
may be used on open neighborhoods of that orbit, but a canceled zero coordinate
does not become an allowed state. Work geometrically over $\overline{\mathbb Q}$
when counting irreducible components and singularities, and explicitly descend
the selected component to $\mathbb Q$ before using rational torsion.

1. The alternating integral $\kappa_i=(x_i+1)(x_{i+2}+1)/x_{i+1}$ and the
   even-subsequence QRT map and invariant are classical:
   [Matsukidaira–Takahashi, §II.1, equations (6)–(14)](https://arxiv.org/html/nlin/0512072).
   The same reduction appears in
   [Cima–Gasull–Mañosa, §3.1, equation (16)](https://arxiv.org/html/0801.4360).
2. A birational map over $K$ of a smooth genus-one curve with a $K$-point
   is an elliptic translation followed by a group automorphism; see
   [Jogia–Roberts–Vivaldi, Theorem 3 and proof, author version pp. 5–6](https://web.maths.unsw.edu.au/~jagr/IntegrabilityRS.pdf).
   Over $\mathbb Q$, the group automorphism is $+1$ or $-1$.
3. Mazur's rational torsion theorem allows element orders
   $$\mathcal M=\{1,2,3,4,5,6,7,8,9,10,12\}.$$
   Credit: [Mazur, *Modular curves and the Eisenstein ideal* (1977)](https://www.numdam.org/item/PMIHES_1977__47__33_0/).
   The theorem is imported, not reproved. Its order list is also explicitly
   recalled in the introduction and §3.2 of
   [Gasull–Mañosa–Xarles](https://arxiv.org/html/1004.5511).
   The present source session accessed that statement and Mazur's metadata;
   retrieval of the original long PDF failed, so no full-reading claim is made.
4. Standard curve facts used explicitly: normalization of a projective reduced
   curve is finite; birational self-maps of smooth projective curves extend to
   automorphisms; a smooth genus-zero curve over $\mathbb Q$ with a rational
   point is $\mathbb P^1_{\mathbb Q}$ (Riemann–Roch for that point).
   The needed arithmetic-genus and singularity estimates are derived below
   from Euler characteristics rather than assumed for a generic fiber.

## Strategy and dependency map

The classical reduction places an even orbit on one fixed biquadratic curve.
At every allowed point the map is locally biregular, so singular points remain
singular and nonsingular points remain nonsingular. The singular set is small.
A nonsingular rational point selects a geometrically irreducible component
defined over $\mathbb Q$. After at most four component steps, its normalization
has a rational automorphism of genus zero or one. The two automorphism bounds
then control the original clock.

1. Steps 1–2: exact plane reduction, invariant identity and local inverses.
2. Step 3: all reduced/nonreduced/reducible fibers, component and singular bounds.
3. Steps 4–5: rational automorphism period bounds.
4. Step 6: component descent, complete case split and native-clock restoration.

## Proof

### 1. Exact even-subsequence reduction

Subtracting the recurrence at adjacent indices gives
$$x_{i+1}(x_{i+4}+1)=x_{i+3}(x_i+1).$$
Consequently $\kappa_{i+2}=\kappa_i$. Put
$$u=\kappa_0\in\mathbb Q^*,\quad g_j=x_{2j},\quad
x_{2j+1}=\frac{(g_j+1)(g_{j+1}+1)}{u}.$$
Eliminating the odd term, or substituting it into two original recurrences,
gives the classical map
$$R(X,Z)=(Z,f(Z)/X),\qquad
f(Z)=\frac{(u+1)Z+au+1}{Z+1}.\tag{1}$$
Here $(X,Z)=(g_j,g_{j+1})$, and the second output is $g_{j+2}$.
In particular $f(g_{j+1})=g_jg_{j+2}\ne0$ at every orbit point.
Thus $f$ is not the identically zero rational function, including at exceptional
parameter values; that impossible case cannot contain the stipulated orbit.

The projection $(x,y,z)\mapsto(x,z)$ on $\{\kappa_0=u\}$ has the inverse
$(X,Z)\mapsto(X,(X+1)(Z+1)/u,Z)$. It conjugates $L_a^2$ along this orbit to
$R$. If $m$ is the least period for $R$, then
$$m=\frac{N}{\gcd(N,2)},\qquad N\le2m.\tag{2}$$
This follows also directly from the formula for the order of the square of a
cyclic permutation and the displayed injective reconstruction. It does not
identify the two clocks without the factor in (2).

### 2. Fixed biquadratic and local biregularity

Set $D=u^2+2u+2+au$ and let
$$\begin{split}
B_h(X,Z)={}&X^2Z^2+(2+u)(X+Z)XZ+(1+u)(X^2+Z^2)\\
&+D(X+Z)+(1+u)(1+au)-hXZ.
\end{split}\tag{3}$$
Choose the rational number $h$ so that $B_h(g_0,g_1)=0$; this is possible
because $g_0g_1\ne0$. Formula (3) is the classical invariant numerator.
For a fixed $Z$, its quadratic coefficient in $X$ is
$$A(Z)=(Z+1)(Z+u+1),$$
and its constant coefficient is
$$C(Z)=(Z+u+1)((u+1)Z+au+1)=A(Z)f(Z).$$
For a quadratic $AX^2+BX+C$ with $C=Af$, substitution of $f/X$ yields
$$A(f/X)^2+Bf/X+C=\frac f{X^2}(AX^2+BX+C).$$
Using symmetry of (3) therefore proves the rational identity
$$B_h(R(X,Z))=\frac{f(Z)}{X^2}B_h(X,Z).\tag{4}$$
This identity still holds at $Z=-u-1$ whenever the orbit is ordinary; no
division by $Z+u+1$ is needed in the verification.

At each orbit point $(X,Z)$, the entries $X,Z,Z+1,f(Z)$ are nonzero.
The map (1) and its inverse
$$R^{-1}(X,Z)=(f(X)/Z,X)$$
are regular on suitable open neighborhoods of that point and its image.
Their compositions are the identity there. In (4) the factor $f(Z)/X^2$
is a unit on such a neighborhood. Hence $R$ induces an isomorphism of the
local curve germs, including their reduced supports. In particular it neither
contracts a component through an orbit point nor changes whether that point
is singular on the reduced curve.

### 3. Component and singularity bounds, without a generic-fiber assumption

Bihomogenize (3) in $\mathbb P^1\times\mathbb P^1$ and take its reduced
geometric support $C$. The coefficient of $X^2Z^2$ is one, so this is not
the zero polynomial. The reduced support has bidegree $(d,e)$ with
$0\le d,e\le2$. Write its geometric irreducible components as
$C_1,\ldots,C_r$ and their normalization genera as $g_1,\ldots,g_r$.
Every component has nonzero effective bidegree, so
$$r\le d+e\le4.\tag{5}$$

The exact sequence for a divisor of bidegree $(d,e)$ is
$$0\longrightarrow\mathcal O(-d,-e)\longrightarrow\mathcal O
\longrightarrow\mathcal O_C\longrightarrow0.$$
Since $\chi(\mathcal O(k,l))=(k+1)(l+1)$ on this surface, it gives
$$p_a(C)=1-\chi(\mathcal O_C)=(d-1)(e-1)\le1.\tag{6}$$
For the normalization $\nu:\widetilde C\to C$, the cokernel of
$\mathcal O_C\to\nu_*\mathcal O_{\widetilde C}$ has length
$\delta=\sum_{P\in C}\delta_P$. The normalization exact sequence gives
$$\delta=p_a(C)+r-1-\sum_{j=1}^r g_j\le r\le4.\tag{7}$$
Each geometric singular point of the reduced curve has $\delta_P\ge1$.
Thus $C$ has at most four geometric singular points. Equations (6)–(7)
also apply to a disconnected reduced support; connectedness was not assumed.

Apply the same arithmetic-genus calculation to one irreducible component
of bidegree $(d_j,e_j)$. If one of its bidegrees is zero, geometric
irreducibility forces it to be a single ruling line, with genus zero.
Otherwise $1\le d_j,e_j\le2$ and
$$0\le g_j\le(d_j-1)(e_j-1)\le1.$$
If $g_j=1$, both degrees equal two. This consumes the entire available
bidegree, so $C=C_j$ is irreducible and (7) forces $\delta=0$. Thus the
genus-one case is precisely a smooth irreducible curve here. All other
normalizations have genus zero. Nonreduced fibers cause no extra cases:
the preceding argument was expressly applied to their reduced support.

### 4. Rational genus-zero automorphisms

Let $T\in\operatorname{PGL}_2(\mathbb Q)$ and suppose a rational point has
least period $s$. If it is fixed, $s=1$. Otherwise a matrix representative
cannot be a nontrivial Jordan block: its positive powers have the same unique
eigenline, which would only give a fixed projective point.

With two distinct eigenvalues $\alpha,\beta$, a non-eigenline can be periodic
only if $\zeta=\alpha/\beta$ is a root of unity, of the same order $s$.
The matrix trace and determinant give
$$\zeta+\zeta^{-1}=
\frac{\operatorname{tr}(T)^2}{\det(T)}-2\in\mathbb Q.$$
This number is an algebraic integer and lies in $[-2,2]$, so it is one of
$-2,-1,0,1,2$. Solving the corresponding quadratic for $\zeta$ shows
$$s\in\{1,2,3,4,6\}.\tag{8}$$
The scalar matrix case is already the identity. This argument concerns the
automorphism of the whole normalized curve and does not use a finite orbit
sample.

### 5. Rational genus-one automorphisms

Let $E/\mathbb Q$ be a smooth genus-one curve with a rational point chosen
as zero. By classical input 2 a rational automorphism is either
$$P\longmapsto P+\Omega\quad\hbox{or}\quad P\longmapsto-P+\Omega,
\qquad\Omega\in E(\mathbb Q).$$
For completeness, the extra order-three/four/six group automorphisms over
an algebraic closure require nonrational roots of unity as their multiplier
on a rational invariant differential. Hence they are not group automorphisms
over $\mathbb Q$. The negative-sign map squares to the identity. For a
translation, periodicity of any point with least period $s$ is equivalent to
the rational point $\Omega$ having exact order $s$. Classical input 3 gives
$$s\in\mathcal M,\qquad s\le12.\tag{9}$$
No assumption that the specialized map is an infinite-order translation has
been used; the finite-order involution case was retained.

### 6. Descent, all orbit cases and restoration of the native clock

Consider the $R$-orbit on the reduced curve $C$ of Step 3.
If one of its points is singular, Step 2 makes every point singular.
Step 3 then gives $m\le4$.

Otherwise every orbit point is nonsingular. At its starting rational point
$P$, there is a unique geometric irreducible component $C_0$. Every Galois
automorphism fixes $P$ and permutes the components, and therefore fixes
$C_0$. Thus $C_0$ is defined over $\mathbb Q$; it is not an arbitrarily
chosen component over an extension field. The unique normalization point
above the smooth rational point $P$ is rational as well.

By Step 2 the map transports the components through the orbit birationally.
Their cycle has a length $r_0\le r\le4$, and $r_0$ divides $m$.
The return $R^{r_0}$ induces a birational self-map of $C_0$ over
$\mathbb Q$, hence an automorphism of its smooth projective normalization.
The normalized point has exact period $m/r_0$: the projection is injective
at all these nonsingular orbit points.

If that normalization has genus zero, its rational point identifies it
with $\mathbb P^1_{\mathbb Q}$. Step 4 gives
$$m=r_0s\le4\cdot6=24.$$
If it has genus one, Step 3 gives $r=r_0=1$ and Step 5 gives $m\le12$.
These cases exhaust all reduced fibers and all orbit points. Thus always
$m\le24$, and (2) yields $N\le48$. $\square$

## Consequence for the original integer question and remaining obligation

For integer $a\ne1$, the fourth-pass complete stratum meeting $-1$ has
period dividing four. For $a=1$, classical global order eight handles the
period bound, although an integral atlas is a separate assertion. Together
with the lemma above, this gives a coarse finite list of possible native
periods for the integer LY4 question, without a height cutoff.

This is **not** a proof that all integer periods outside $a=1$ are at most six.
It also does not parametrize the integral points in each higher-period torsion
stratum, eliminate those strata, give exact all-parameter counts, or close the
original LY4 contract. The QRT reduction and the curve automorphism inputs are
classical. This auxiliary package cannot be counted as a fourth admission.

## Execution and review boundary

No mathematical program or finite census was run for this proof. The invariant
identity is checked by the displayed quadratic substitution. Source retrieval
is documented in the separate source audit. No unchanged old program was
rerun. The argument is offered for non-author internal review, with particular
attention to local germs, reducible/nonreduced fibers, Galois descent and
normalization; it is not a mathematical correctness certificate by assertion.
