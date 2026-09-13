# Paper30 D first probe: the local order at a cubic third resonance

Date: 2026-09-06. Author-only, proof-first bounded probe.
Disposition: BOUNDED_SHORT_RESULT_STOP, not a selected Paper30 candidate.
No manuscript, capacity exception, formal score, numerical experiment, or
Route A/B claim is created by this note.

## Claim

Fix $b\in\mathbb C$ and $c\in\mathbb C^*$. Consider the cubic symplectic map
$$
H_{\tau,b,c}(x,y)=((-1+\tau)x+b x^2+c x^3-y,x).
$$
Let $R=\mathbb C[[\tau]]$, and retain only the local factor at the origin
of the scheme of points fixed by $H_{\tau,b,c}^3$. Denote its finite
$R$-algebra by $B_{b,c}$. Its trace discriminant means the determinant
of the pairing $(u,v)\mapsto\operatorname{Tr}_{B_{b,c}/R}(uv)$, up to an
$R$-unit. It is not the discriminant of the normalized cover.

The exact values are

| Fixed coefficients | Local special-fibre length | Trace-discriminant order | Normalization-discriminant order | $\operatorname{length}_R(\widetilde B/B)$ |
| --- | ---: | ---: | ---: | ---: |
| $b\ne0$, $c\ne0$ | $4$ | $8$ | $0$ | $4$ |
| $b=0$, $c\ne0$ | $13$ | $38$ | $6$ | $16$ |

Both rows have the same degree and the same linear map at $\tau=0$:
$$
DH_{0,b,c}(0)=
\begin{pmatrix}-1&-1\\1&0\end{pmatrix},
\qquad \operatorname{Spec}DH_{0,b,c}(0)=\{\omega,\omega^2\},
$$
where $\omega$ is a primitive cube root of unity.
Thus neither the local length nor the trace-discriminant order is
determined by these linear eigenvalues.

## Status and assumptions

Status: PROVABLE AS STATED by the author proof below; independently
reviewed status is NOT_ASSESSED. The short-stop disposition does not
certify world novelty or any candidate gate.

The coefficient $c$ stays nonzero. The detuning is exactly the displayed
linear parameter $\tau$, with $b,c$ held fixed. Orders are taken with
$v_\tau(\tau)=1$. The local factor includes the origin section as well as
all nearby points of least period three, with their scheme lengths.
It does not include other fixed points away from the origin.

Varying $b$ alone while keeping $\tau=0$ would leave the origin resonant
throughout and would not give the discriminant calculation in this note.
The excluded linear case $b=c=0$ has $H_{0,0,0}^3=\mathrm{id}$ and is not
an isolated local fixed-point scheme.

## Notation, strategy, and dependency map

Set $f_\tau(t)=\tau t+b t^2+c t^3$ and $s=x+y+z$. The cyclic equations are
$$
G_x=f_\tau(x)-s,\quad G_y=f_\tau(y)-s,\quad G_z=f_\tau(z)-s.
\tag{1}
$$
They encode the three-period scheme, not a new unrelated construction:
the recurrence $x_{j+1}+x_{j-1}=(-1+\tau)x_j+b x_j^2+c x_j^3$
is exactly (1). Eliminating the third coordinate identifies the cyclic
scheme with $\operatorname{Fix}(H_{\tau,b,c}^3)$.

The proof uses four steps:

1. Local intersection multiplicity at $\tau=0$ gives ranks $4$ and $13$.
2. An explicit splitting into local generic branches checks reducedness.
3. The finite-flat complete-intersection different formula converts the
   cyclic Jacobian into the trace discriminant.
4. The same branch description gives the normalization and lattice index.

The different formula is standard prior work, not a contribution here.
Its hypotheses and the precise cited result are given in Step 3.

## Proof

### Step 1. The local special fibre and finite flatness

The algebra $Q=R[x,y,z]/(G_x,G_y,G_z)$ is finite free of rank $27$.
Indeed, dividing (1) by $c$ gives monic leading terms $x^3,y^3,z^3$
for any degree-compatible monomial order. Their pairwise coprime leading
monomials imply the Gröbner criterion over $R$; hence the $27$ monomials
$x^i y^j z^k$, $0\leq i,j,k\leq2$, form an $R$-basis.
Because $R$ is complete, the idempotents of $Q/\tau Q$ lift, splitting
$Q$ into finite free local factors. The origin factor is $B_{b,c}$.
Equivalently it is the completion of (1) at $(\tau,x,y,z)$.
This description also proves that it is a relative local complete
intersection: locally three equations of height three in the smooth
three-variable $R$-algebra form a regular sequence.

Suppose first $b\ne0$. At $\tau=0$, the equation $G_x=0$ gives
$$
z=-x-y+b x^2+c x^3.
$$
The other two equations can be replaced by $f_0(y)-f_0(x)=0$ and
$f_0(z)-f_0(x)=0$. Their initial homogeneous forms, up to signs, are
$$
b(x^2-y^2),\qquad b\bigl(x^2-(x+y)^2\bigr).
\tag{2}
$$
They have no common projective zero: the first forces $y=x$ or $y=-x$;
in these two cases the second is $-3b x^2$ or $b x^2$, respectively.
The local intersection multiplicity is therefore the product $2\cdot2=4$.
Here the usual initial-form intersection rule applies because the two
initial forms are a regular sequence. This proves that the local factor
is isolated and has rank $4$.

Now let $b=0$. Eliminate $z=-x-y+c x^3$. Dividing differences by $c$,
the remaining two equations are $y^3-x^3=0$ and $z^3-x^3=0$.
The first factors into the three distinct lines $y=\eta x$,
$\eta\in\{1,\omega,\omega^2\}$. On such a line, the second is
$$
x^3\left[\bigl(-(1+\eta)+c x^2\bigr)^3-1\right].
\tag{3}
$$
For $\eta=1$, the bracket has constant term $-9$ and order $0$.
For $\eta=\omega,\omega^2$, one has $-(1+\eta)=\eta^2$; the constant
term is zero and the coefficient of $x^2$ is $3c\eta^4\ne0$.
Thus the three intersection orders are $3,5,5$.
Additivity of intersection multiplicity over distinct factors gives
$3+5+5=13$. Formula (3) also verifies isolation on every factor,
so the use of that additivity has no common-component exception.

### Step 2. All generic branches in the local factor

The origin is always a section. Its cyclic Jacobian will have nonzero
determinant over $\mathbb C((\tau))$, as computed in Step 3.

For $b\ne0$, seek solutions with two coordinates equal to $t$ and the
third equal to
$$
u=f_\tau(t)-2t=(\tau-2)t+b t^2+c t^3.
$$
After division by $t-u$, the necessary and sufficient remaining equation
for unequal $t,u$ is
$$
\Phi(\tau,t)=\tau+b(t+u)+c(t^2+tu+u^2)=0.
\tag{4}
$$
At $(0,0)$, $\partial_t\Phi=-b\ne0$ and $\partial_\tau\Phi=1$.
The implicit function theorem gives
$$
t=\tau/b+O(\tau^2),\qquad u=-2\tau/b+O(\tau^2).
\tag{5}
$$
The three placements of $u$ give three distinct sections over $R$.
Together with the origin these are four distinct geometric points in
the generic local factor of rank $4$. Consequently they exhaust it,
each point is simple, and the generic algebra is $\mathbb C((\tau))^4$.

For $b=0$ there are two types of nonconstant branches. If $x,y,z$ are
all distinct, they are the three roots of $c t^3+\tau t-s=0$.
Their sum is zero, whereas (1) says that their sum is $s$.
Thus $s=0$, and all such solutions are the six permutations of
$$
(0,r,-r),\qquad r^2=-\tau/c.
\tag{6}
$$
All these branches approach the origin.

For exactly two equal coordinates, write $x=y=t$, $z=u=r_0t$ and
$v=ct^2$. For nonzero $t$ the equations become
$$
r_0=\tau-2+v,\qquad \tau+v(1+r_0+r_0^2)=0.
\tag{7}
$$
The second equation after substituting the first has $v$-derivative $3$
at $(\tau,v)=(0,0)$. Its unique local solution is
$$
v=-\frac{\tau}{3}-\frac{2\tau^2}{9}+O(\tau^3).
\tag{8}
$$
For completeness, substitute $v=A\tau+B\tau^2+O(\tau^3)$ in (7).
The coefficient of $\tau$ is $1+3A$, so $A=-1/3$.
Since $r_0=-2+(1+A)\tau+O(\tau^2)$, the coefficient of $\tau^2$
is $3B-3A(1+A)$, so $B=-2/9$.
The choices $t=\pm\sqrt{v/c}$ and the three placements of $u$ give six
more distinct geometric points. They differ from (6) because precisely
two coordinates are equal. They differ from the origin because $v\ne0$.

When all coordinates equal $t$, their equation is
$t(\tau-3+ct^2)=0$. Its only branch approaching the origin is $t=0$.
We have found $1+6+6=13$ distinct generic geometric points of a rank-$13$
local algebra. They therefore exhaust it and prove generic reducedness.
In both coefficient cases the nonorigin local points have least period
three: a triple fixed by a shift of one position would have all entries
equal, and a divisor of three is either one or three.

### Step 3. Trace discriminant from the different

Put $a_t=f_\tau'(t)=\tau+2bt+3ct^2$. The Jacobian of (1) is
$\operatorname{diag}(a_x,a_y,a_z)-\boldsymbol1\boldsymbol1^{\mathsf T}$,
so its determinant is exactly
$$
J=a_xa_ya_z-a_xa_y-a_ya_z-a_za_x.
\tag{9}
$$
For a finite flat, generically étale local complete intersection, the
different is generated by this Jacobian; in local duality terms there
is a generator $\lambda$ of $\operatorname{Hom}_R(B,R)$ as a $B$-module
such that $\operatorname{Tr}(w)=\lambda(Jw)$, up to a unit multiplying
$J$. This is the complete-intersection different formula, specifically
[Stacks, Lemmas 49.12.2–49.12.4](https://stacks.math.columbia.edu/tag/0BWB).
The required finite flatness and complete-intersection property were
verified in Step 1, and generic étaleness in Step 2.

To spell out the discriminant consequence, take an $R$-basis of $B$.
The matrix of $(u,v)\mapsto\lambda(uv)$ is invertible over $R$, since
$\lambda$ generates the dual module. The trace Gram matrix is its
product with the matrix of multiplication by $J$, up to an invertible
change. Its determinant thus differs from $\operatorname{Norm}_{B/R}(J)$
by a unit. We may compute its valuation by summing the valuations of
$J$ at the generic geometric points, counted once each.

At the origin, (9) is $\tau^2(\tau-3)$, of order $2$.
For the three branches (5), one has
$a_t=3\tau+O(\tau^2)$ and $a_u=-3\tau+O(\tau^2)$.
Consequently
$$
J=a_t^2a_u-a_t^2-2a_ta_u=9\tau^2+O(\tau^3),
$$
of order $2$. This gives the first discriminant order $2+3\cdot2=8$.

For $b=0$, at every point (6) the three values of $a$ are
$\tau,-2\tau,-2\tau$. Their pairwise products sum to zero, so
$J=4\tau^3$, exactly. At the six points (7), (8) gives
$$
a_t=\tau+3v=-\frac23\tau^2+O(\tau^3),\qquad
a_u=\tau+3vr_0^2=-3\tau+O(\tau^2).
$$
It follows that
$$
J=a_t^2a_u-a_t^2-2a_ta_u=-4\tau^3+O(\tau^4).
$$
These twelve geometric points each contribute order $3$.
The total is therefore $2+12\cdot3=38$. All leading coefficients used
here are nonzero, as also required for generic reducedness.

### Step 4. Normalization and the index of the original algebra

Because $B$ is torsion free and its generic fibre is reduced, $B$ itself
is reduced. It embeds into the normalization of its generic algebra.
For $b\ne0$, Step 2 gives $\widetilde B=R^4$, whose trace discriminant
is a unit.

For $b=0$, the six points (6) form three conjugate pairs under
$\sqrt{\tau}\mapsto-\sqrt{\tau}$, one pair for each location of the zero.
The six points (7) form three more pairs, one for each location of the
unequal entry. In (8), $v/c$ has order one, so each pair has generic
field $\mathbb C((\sqrt{\tau}))$. The origin contributes $R$.
Thus, as an $R$-algebra,
$$
\widetilde B\simeq R\times\mathbb C[[w]]^6,\qquad \tau=w^2
$$
after unit changes of the individual $w$ coordinates. Each quadratic
factor has trace discriminant $4\tau$, as follows directly from its
basis $1,w$. The total normalization-discriminant order is $6$.

Finally, two full $R$-lattices $B\subseteq\widetilde B$ in the same
generic algebra satisfy
$$
v_\tau(\operatorname{disc}B)
=v_\tau(\operatorname{disc}\widetilde B)
2\operatorname{length}_R(\widetilde B/B).
$$
Indeed, a basis inclusion matrix changes the trace Gram determinant
by the square of its determinant, whose valuation is that quotient
length by Smith normal form over the DVR $R$.
The two lengths are $(8-0)/2=4$ and $(38-6)/2=16$.
This proves every entry of the table. $\square$

## Prior work, noncollision, and bounded disposition

This is not a new discovery of a degenerate cubic $1{:}3$ resonance.
The primary article by Dullin and Meiss, *Generalized Hénon maps:
the cubic diffeomorphisms of the plane*, Physica D 143 (2000), 262–289,
studies low-period bifurcations of exactly the conservative cubic family.
Its publisher abstract and introduction were directly read:
[publisher](https://www.sciencedirect.com/science/article/pii/S0167278900001056).
Its complete paywalled body was not read in this probe.

Gonchenko, Kazakov, Samylina and Shykhmamedov, *On 1:3 resonance under
reversible perturbations of conservative cubic Hénon maps*, explicitly
identify this central-symmetry degeneracy and the four three-periodic
orbits. The arXiv abstract, introduction and relevant discussion were
directly read, including the attribution to Dullin–Meiss:
[arXiv 2105.01360](https://arxiv.org/abs/2105.01360).
Publication metadata was verified at the authors' institutional
[repository](https://diposit.ub.edu/items/f741b221-9eb7-48ba-8519-d72820e59672):
Regular and Chaotic Dynamics 27 (2022), 198–216.
These are strong direct deductions. Complex scheme lengths and the
local order's trace discriminant are not asserted to be the article's
stated theorem, but recounting the orbit bifurcation is not new.

The bounded search also covered fixed-point/Dold indices, local
multiplicity, different/discriminant terminology, and 2025–2026 queries.
It did not locate a directly stated $8/38$ local-order formula. This is
not proof of absence, and no novelty score is awarded. The branch
description makes this formula a short algebraic refinement, not by
itself evidence for the required independent long paper.

Local noncollision: Papers12, 13, 15 and 18 concern residue separation,
primitive covers, multiplier fibres or marked boundary coordinates;
Paper29 concerns filtered polynomial cohomology. This calculation is a
different local object, but noncollision alone does not imply sufficient
research value or substantive capacity.

Per the proof-writer skill, the finite parameter slice and distinction
between an order and its normalization have been kept explicit.
Per the novelty-check/research-lit skills, the directly overlapping
strong-resonance theory is deducted. No external GPT-5.4 MCP review
was available or performed; no fallback review is being impersonated.
No formula here has yet received a separate mathematical review.

## Open risks and stopping boundary

- No classification for arbitrary resonant germs or all root orders is
  proved; the displayed two coefficient strata are one cubic slice.
- No general multi-parameter discriminant or divisor multiplicity is
  claimed. A different, especially tangent, detuning changes the order.
- The full algebra's discriminant is not the normalized cover's
  ramification discriminant; the difference is quantitatively real here.
- Novelty and candidate capacity are NOT_ASSESSED; this is a short
  author result retained without a formal project or paper count.
- Do not append additional low-degree tables or unrelated old results
  to make this stopped probe appear to meet the 22-page lower bound.
