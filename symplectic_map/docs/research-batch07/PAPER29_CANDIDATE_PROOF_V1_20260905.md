# Paper29 candidate proof V1: collision-stratified rational first integrals

Date: 2026-09-05. Author-side proof package, not a candidate acceptance or a
publication lock. No Paper29 project directory is opened by this document.
The exact result below is proposed for independent correctness, value and
literature review. The ambient degree formula and the absence of periodic
curves on the quotient are not claimed as new contributions.

## Claim and status

**Author feasibility status: PROVABLE AS STATED. Independent review: PENDING.**

Let $r\ge3$, let $f,g\in\mathbb C[t]$ be nonconstant, and put
$$
Q=\prod_{i=1}^r q_i,\quad P=\prod_{i=1}^r p_i,\quad
x_i=q_ip_i,\quad c_i=x_i-x_r\ (i<r),\quad c_r=0.
$$
Define polynomial symplectomorphisms of $\mathbb A^{2r}$ by
$$
S_f(q,p)=\left(q_i,p_i+f'(Q)\prod_{j\ne i}q_j\right)_{i=1}^r,
\qquad
T_g(q,p)=\left(q_i+g'(P)\prod_{j\ne i}p_j,p_i\right)_{i=1}^r,
\qquad F=T_g\circ S_f.
$$
The plus signs are part of the definition. With the convention
$\omega=\sum_i dq_i\wedge dp_i$ and the usual Poisson bracket, these
are Hamiltonian shears with appropriate opposite Hamiltonian signs.

The proposed main theorem is the following conjunction.

1. For every positive integer $N$,
   $$
   \mathbb C(q,p)^{F^N}=\mathbb C(c_1,\ldots,c_{r-1}),\qquad
   \mathbb C[q,p]^{F^N}=\mathbb C[c_1,\ldots,c_{r-1}].
   $$
2. For an arbitrary fixed $c\in\mathbb C^{r-1}$, let
   $$
   M_c=\operatorname{Spec}
   \mathbb C[x,q_1,p_1,\ldots,q_r,p_r]/(q_ip_i-x-c_i)_{i=1}^r.
   $$
   Partition $\{1,\ldots,r\}$ into blocks $I_1,\ldots,I_s$ according to
   equality of $c_i$, and choose a representative $i_a$ of each block.
   For every $N\ge1$,
   $$
   \mathbb C(M_c)^{F^N}
   =\mathbb C\left(q_i/q_{i_a}:i\in I_a\setminus\{i_a\},\ 1\le a\le s\right),
   \qquad \operatorname{trdeg}_{\mathbb C}=r-s.
   $$
   The displayed ratios are algebraically independent generators of a
   function field, not regular functions on the entire fiber. Nonetheless,
   $$
   \mathbb C[M_c]^{F^N}=\mathbb C
   $$
   on every fiber, including the singular collision fibers.
3. Therefore the maximum number of algebraically independent rational first
   integrals of $F^N$ on the full phase space is exactly $r-1$. In particular
   no iterate has $r$ algebraically independent rational commuting first
   integrals. This is a rational algebraic statement only, not an analytic,
   meromorphic or real smooth nonintegrability theorem.

The fixed-fiber answer changes exactly on the collision partition of the
momentum values. Choice of representatives changes only the displayed
transcendence basis, not the field.

## Assumptions and anti-claims

The assumptions are complex characteristic-zero coefficients, $r\ge3$, and
nonconstant $f,g$. There is no generic-coefficient hypothesis and no
restriction on lower coefficients or on multiplicities among the fixed
values $c_i$. Results on all positive powers use the same fixed map.

The proof does not classify maps with arbitrary support, does not assert
that every momentum fiber is a torus torsor, and does not infer a global
first integral by specializing or unspecializing a fiber formula. No
periodic-orbit counting, Riemann determinant, spectral quantization, real
topological entropy or positive-characteristic assertion is made.

## Strategy and dependency map

The noncollision case is not sufficient: a collision destroys factoriality
of the original fiber and introduces new rational functions. The proof first
extracts precisely the visible within-block ratios, then changes to a
different affine model over their function field. This model is factorial.
Its quotient uses the **entire diagonalizable group**, which can be
disconnected; taking only its identity component changes the invariant ring.

The dependencies are:

1. A monomial normal form gives integral momentum fibers and their function
   fields (Lemma 1).
2. Every quotient surface has no periodic affine algebraic curve (Lemma 2).
   This conclusion is already covered in a more general loxodromic setting
   by Abboud; the direct proof here avoids a projective dynamical-degree
   comparison and is included for self-contained verification, not novelty.
3. A distinct-root affine model is a UFD with constant units (Lemma 3).
4. Its full, possibly disconnected diagonalizable quotient has one orbit per
   geometric fiber, with finite stabilizers (Lemma 4).
5. A rational fixed function on the factorial model yields weight
   eigenfunctions whose zero sets would descend to periodic curves
   (Lemma 5).
6. Collision-block reduction applies Lemmas 2--5 to classify every original
   momentum fiber (Theorem 6).
7. Base-field descent gives the full phase-space field. A polynomial section
   and the monomial normal form determine the two regular fixed rings
   (Theorems 7--8).

All computations below are symbolic proofs. No finite numerical or CAS
search is a dependency.

## Lemma 1. Integral fibers and exact coordinates

For any field $k$ and any $d_1,\ldots,d_s\in k$, the ring
$$
R_d=k[x,u_1,v_1,\ldots,u_s,v_s]/(u_av_a-x-d_a)_{a=1}^s
$$
is an integral domain. It embeds into $k[x,u_1^{\pm1},\ldots,u_s^{\pm1}]$
by $v_a=(x+d_a)/u_a$. Its fraction field is $k(x,u_1,\ldots,u_s)$.

To prove injectivity, reduce every monomial so that for each $a$ it contains
either a positive power of $u_a$, a positive power of $v_a$, or neither, but
not both. The relations are monic reductions of distinct products $u_av_a$;
reductions on different indices commute, so this gives a unique spanning
normal form over $k[x]$. For a resulting exponent difference
$m=(m_a)\in\mathbb Z^s$, the image has the form
$$
u^m\prod_a(x+d_a)^{\max(-m_a,0)}.
$$
Different $m$ give different Laurent monomials, and the multiplying
polynomial is nonzero. Thus these normal-form monomials are linearly
independent over $k[x]$. This proves the embedding and all the assertions.

For $M_c$, the chart where every $q_i$ is nonzero is therefore dense and has
coordinates $(x,q_1,\ldots,q_r)$, with $p_i=(x+c_i)/q_i$.

The same normal form before fixing the $c_i$ makes
$\mathbb C[q,p]$ a free module over $\mathbb C[x_1,\ldots,x_r]$.
Changing coordinates to $(x,c_1,\ldots,c_{r-1})$ shows that the momentum map
is flat. It has the polynomial section $q_i=1$, $p_r=0$, $p_i=c_i$ for
$i<r$, so it is surjective. Lemma 1 holds after any extension of the residue
field and proves geometric integrality of every fiber. These structural
facts are background for the fixed-field theorem, not separate novelty
claims.

## Lemma 2. A self-contained no-periodic-curve ingredient

Let $k$ be algebraically closed of characteristic zero, let $h\in k[x]$
have degree $r\ge3$, and write $D_h=\{QP=h(x)\}$. Define
$$
\sigma_f(Q,P,x)=
\left(Q,\ P+\frac{h(x+Qf'(Q))-h(x)}Q,\ x+Qf'(Q)\right),
$$
$$
\tau_g(Q,P,x)=
\left(Q+\frac{h(x+Pg'(P))-h(x)}P,\ P,\ x+Pg'(P)\right).
$$
Both displayed difference quotients are polynomials. The inverses use
$-f$ and $-g$. Put $\phi=\tau_g\sigma_f$,
$d=\deg f$, $e=\deg g$, $A=rd-1$, $B=re-1$, and $L=AB>1$.
Then no irreducible affine curve on $D_h$ is periodic under $\phi$.

Suppose a curve $C$ were fixed by $\phi^N$. Its function field has a
nonsingular projective model $\overline C$. The normalization of the affine
curve is the complement of finitely many points in $\overline C$; an
automorphism of the affine curve lifts to its normalization and extends to
$\overline C$. It therefore permutes these finitely many points. At least
one coordinate function is nonconstant, hence has a pole at one of them.

At such a place $v$, put $a=-v(Q)$, $b=-v(P)$ and $z=-v(x)$; an
identically zero coordinate is assigned $-\infty$. At least one of
$a,b,z$ is positive. If $z>0$, the degree of $h$ gives $a+b=rz$, and
$r\ge3$ implies $a>z$ or $b>z$. If $z\le0$, one of $a,b$ is positive.
Thus at least one of the following strict cones applies:
$$
\mathcal Q:\ a>\max(z,0),\qquad
\mathcal P:\ b>\max(z,0).
$$
In $\mathcal Q$, the first shear gives pole orders
$z_1=da$, $b_1=(rd-1)a=Aa$. The second gives
$z_2=eAa$, $a_2=(re-1)Aa=La$. Indeed $Aa>da$ because
$(r-1)d-1>0$, and $La>eAa$ because $(r-1)e-1>0$.
The maximum in each addition is strict, so the leading terms cannot cancel.
The final triple remains in $\mathcal Q$.

In $\mathcal P$, apply $\phi^{-1}=\sigma_{-f}\tau_{-g}$ instead. The
first phase gives $z_1=eb$, $a_1=Bb$; the second gives
$z_2=dBb$, $b_2=Lb$. The inequalities just verified, with $d$ and $e$
interchanged, keep the triple in $\mathcal P$.

Consequently either $Q\circ\phi^{Nk}$ or $P\circ\phi^{-Nk}$ has pole
order growing as $L^{Nk}$ at the selected original place. But pullback by
the automorphism of $\overline C$ permutes the finite set of pole orders of
that fixed coordinate function at the points at infinity. This is a
contradiction. A coordinate that was identically zero causes no exception:
the selected cone uses a nonzero coordinate, and the first strict update
gives the new nonzero functions whose orders are computed above.

This proves the claim for singular as well as smooth $D_h$. It does not
exclude fixed points or periodic boundary curves on a projective
compactification.

## Lemma 3. Factorial distinct-value model

Assume now that the $d_a$ in Lemma 1 are pairwise distinct. For any
characteristic-zero field $k$, $R_d$ is a UFD and $R_d^*=k^*$.

Localizing all $u_a$ gives the Laurent polynomial ring from Lemma 1, a UFD.
Moreover
$$
R_d/(u_a)\cong k[v_a,u_b^{\pm1}:b\ne a].
$$
In fact $x=-d_a$ in this quotient and
$u_bv_b=d_b-d_a\ne0$ for $b\ne a$. Thus each $u_a$ is prime.
The Noetherian domain $R_d$ admits factorization into irreducibles.
Nagata's criterion for factoriality, in precisely this prime-element
localization form, proves that $R_d$ is a UFD. The applicable reference is
[Stacks Project, Lemma 10.120.7, tag 0AFU](https://stacks.math.columbia.edu/tag/0afu).

Any unit becomes $\alpha\prod_a u_a^{m_a}$ in the Laurent ring, with
$\alpha\in k^*$. In the UFD $R_d$, its order at every prime $u_a$ is
zero. The elements $u_b$ for $b\ne a$ are nonzero in $R_d/(u_a)$, so
these orders are exactly $m_a$. Hence all $m_a=0$.

The case $s=1$ is included: $R_d=k[u_1,v_1]$ after eliminating $x$.

## Lemma 4. The full diagonalizable quotient, including torsion

Let $n_1,\ldots,n_s$ be positive integers of sum $r\ge3$, let $Z\in k^*$,
and retain pairwise distinct $d_a$. Put
$$
Q=Z\prod_a u_a^{n_a},\qquad P=Z^{-1}\prod_a v_a^{n_a},\qquad
h(x)=\prod_a(x+d_a)^{n_a}.
$$
Over an algebraically closed characteristic-zero field, consider
$$
H=\ker\left((\mathbb G_m)^s\longrightarrow\mathbb G_m,
\ (t_a)\longmapsto\prod_a t_a^{n_a}\right)
$$
acting by $(u_a,v_a)\mapsto(t_au_a,t_a^{-1}v_a)$. The group is
diagonalizable with character group $\mathbb Z^s/\mathbb Z(n_1,\ldots,n_s)$.
It has dimension $s-1$ and has a finite component group when
$\gcd(n_a)>1$. Its invariant ring is exactly
$$
R_d^H=k[Q,P,x]/(QP-h(x)).
$$

Here is the invariant-ring verification, including nonsaturated weights.
The normal-form Laurent exponent vector from Lemma 1 has trivial
$H$-character exactly when it is an **integer** multiple of $(n_a)$.
For a nonnegative multiple its monomial is a power of $Q$ times a
polynomial in $x$, and for a negative multiple it is a power of $P$ times
a polynomial in $x$. The relation displayed above is the only relation by
the Laurent embedding. Replacing $(n_a)$ by its primitive version would
give a different invariant ring and is not allowed in this argument.

Every geometric fiber of $\pi:\operatorname{Spec}R_d\to D_h$ is one
$H$-orbit. If $Q\ne0$, all $u_a$ are nonzero, and the ratios of two
points' $u_a$ coordinates give an element of $H$; the $v_a$ then follow
from the relations. The case $P\ne0$ uses $v_a$ in the same way.
If $Q=P=0$, then $x=-d_b$ for one unique $b$. All pairs indexed by
$a\ne b$ are nonzero, while $u_b=v_b=0$. After specifying $t_a$ for
$a\ne b$, the equation for $t_b^{n_b}$ has a solution in the algebraic
closure. The stabilizer is $\mu_{n_b}$. In particular every fiber has
dimension $s-1$, including the case $s=1$ where this is a finite quotient.

This is a geometric quotient with possibly finite stabilizers, not
generally a torsor. It is a different affine model from a collided original
momentum fiber, whose quotient can have nonclosed orbits.

Define automorphisms on this model by
$$
\widetilde S:\quad u_a'=u_a,\quad
v_a'=v_a+Qf'(Q)/u_a,\quad x'=x+Qf'(Q),
$$
$$
\widetilde T:\quad v_a'=v_a,\quad
u_a'=u_a+Pg'(P)/v_a,\quad x'=x+Pg'(P).
$$
All quotients in these formulas are polynomials since $n_a\ge1$.
The relations are preserved; inverse maps use the negative increments.
Both commute with $H$, and their quotient is exactly $\sigma_f,\tau_g$
from Lemma 2. No claim that these coordinates have the original unweighted
symplectic form is needed.

## Lemma 5. Fixed-field descent on the factorial model

Let $k$ be algebraically closed of characteristic zero and use the data of
Lemmas 3--4. For $\widetilde F=\widetilde T\widetilde S$ and every $N\ge1$,
$$
k(\operatorname{Spec}R_d)^{\widetilde F^N}=k.
$$

Write an invariant rational function as $a/b$ with coprime $a,b\in R_d$.
Because $\widetilde F^N$ is an automorphism, its pullbacks of $a,b$ remain
coprime. Equality of the two reduced fractions in a UFD gives
$$
\widetilde F^{N*}a=\lambda a,\qquad
\widetilde F^{N*}b=\lambda b,\qquad \lambda\in R_d^*=k^*.
$$
The diagonalizable group gives a finite character decomposition of each
element of its coordinate ring; commuting with the group preserves each
character space, including torsion characters. Thus every nonzero weight
component $a_\chi$ satisfies the same eigenfunction equation.

If $a_\chi$ is a nonunit, its zero set is nonempty and has pure codimension
one: factor $a_\chi$ in the UFD, where each prime factor defines a prime
divisor. The entire zero set is $H$-stable and is fixed by
$\widetilde F^N$. Lemma 4 says it is saturated by quotient fibers, all of
dimension $s-1$. Its image (or the closure of that image) is consequently
a nonempty union of curves in the two-dimensional quotient, not a point
or the whole surface. The quotient is an affine diagonalizable-group
quotient, so an invariant closed set has closed image; alternatively,
fiber dimension and closure give the same one-dimensional conclusion.
Equivariance makes that finite union invariant under $\phi^N$.
At least one of its irreducible curve components is therefore periodic,
contradicting Lemma 2.

It is unnecessary, and when $H$ is disconnected potentially incorrect, to
claim that each irreducible factor of $a_\chi$ is $H$-stable. The argument
uses the entire weight zero set before passing to curve components.

Every nonzero weight component is thus a unit, hence a constant by Lemma 3.
It follows that $a$ is a constant; the same applies to $b$. This proves
the fixed-field assertion. The identical weight argument also proves
that every nonzero polynomial eigenfunction on this model is constant and
its scalar eigenvalue is $1$.

For a nonclosed characteristic-zero field $K$ containing the data, apply
the proof after extension to $\overline K$. The fraction field
$K(x,u_1,\ldots,u_s)$ is purely transcendental over $K$, so $K$ is
relatively algebraically closed in it. Intersection with the constant
field $\overline K$ gives precisely $K$. Thus the assertion descends.

## Theorem 6. Every collision fiber

On $M_c$, within a block $I_a$ every $x_i$ equals $x+d_a$. The first
shear fixes all $q_i$. The second, applied after the first, multiplies
every $q_i$ in that block by the same rational factor
$$
\frac{x''+d_a}{x'+d_a},
$$
where $x'$ and $x''$ are the successive common scalar coordinates. Hence
$z_i=q_i/q_{i_a}$ is a rational first integral of each shear and of $F$.
This equality is an identity of function fields and does not assert that
the factor is defined everywhere in the affine chart.

Let $n_a=|I_a|$, let
$Z=\prod_a\prod_{i\in I_a\setminus\{i_a\}}z_i$, and let $K=\mathbb C(z_i)$.
On the dense $q$-chart set $u_a=q_{i_a}$ and $v_a=p_{i_a}$.
Then
$$
q_i=z_i u_a,\quad p_i=z_i^{-1}v_a\quad(i\in I_a),\qquad
u_av_a=x+d_a,
$$
with $z_{i_a}=1$. Thus
$$
\mathbb C(M_c)=K(x,u_1,\ldots,u_s),\qquad
Q=Z\prod_a u_a^{n_a},\quad P=Z^{-1}\prod_a v_a^{n_a}.
$$
These are birational coordinates, so all the $z_i$ are algebraically
independent and there are $r-s$ of them. The original shear formulas in
these coordinates are exactly $\widetilde S,\widetilde T$ of Lemma 4.
Lemma 5 over $K$ therefore proves
$$
\mathbb C(M_c)^{F^N}=K
$$
for every $N\ge1$. All collision partitions, including the one-block and
all-singleton cases, have been handled in the same argument.

## Theorem 7. Global fixed field and polynomial ring

First $c_i$ is invariant: multiplication by $q_i$ during $S_f$ adds
$Qf'(Q)$ to every $x_i$, and multiplication by the new $p_i$ during $T_g$
adds $Pg'(P)$ to every resulting $x_i$. Their differences remain fixed.

Let $K_0=\mathbb C(c_1,\ldots,c_{r-1})$. Algebraic independence of these
coordinates follows from the section in Lemma 1. The generic momentum
fiber has pairwise distinct values $c_i$ in $K_0$, including $c_r=0$.
The distinct-value case of Lemma 5 gives its fixed field $K_0$. Moreover
$$
\mathbb C(q,p)=K_0(x,q_1,\ldots,q_r).
$$
This proves the global field equality for each $N$.

If a global polynomial is invariant, it is a rational function of $c$ by
that field equality. Write $b(c)H(q,p)=a(c)$ with $a,b\in\mathbb C[c]$
and $b\ne0$. Restriction to $q_i=1$, $p_r=0$, $p_i=c_i$ gives the
same equality with $H$ replaced by a polynomial in $c$. Hence $a/b$ is
polynomial. The reverse inclusion was proved by the direct momentum
calculation. This proves the polynomial-ring equality without requiring
unique factorization on a singular special fiber.

## Theorem 8. Regular functions do not jump with the rational field

Take an arbitrary fixed $c$ and a regular invariant $H\in\mathbb C[M_c]$.
Theorem 6 puts it in $\mathbb C(z_i)$, while localization at $Q$ puts it
in $\mathbb C[x,q_1^{\pm1},\ldots,q_r^{\pm1}]$. The coordinate $x$
is algebraically independent of the $q_i$, and $H$ is a rational function
of the latter alone. Uniqueness of polynomial expansion in $x$ therefore
shows that $H$ is a Laurent polynomial in the $q_i$ with constant
coefficients.

It is unchanged by simultaneously scaling all $q_i$ in any one block.
Consequently every Laurent monomial $q^m$ with nonzero coefficient has
$\sum_{i\in I_a}m_i=0$ for every $a$. Lemma 1 shows that, for $q^m$ to
occur in a regular function, its coefficient as a Laurent monomial must
be divisible in $\mathbb C[x]$ by
$$
\prod_i(x+c_i)^{\max(-m_i,0)}.
$$
This follows for the entire coefficient at $q^m$, not just for a chosen
presentation: normal forms with that exponent vector are a free
$\mathbb C[x]$-multiple of exactly the displayed factor. A nonzero
constant can be divisible by this polynomial only if every $m_i\ge0$.
The block-sum conditions then force every $m_i=0$. Thus $H$ is constant.
This proves $\mathbb C[M_c]^{F^N}=\mathbb C$ for every $c,N$.

## Consequences, boundaries, and exact counterexamples

The global $r-1$ momenta Poisson commute because the $q_ip_i$ do. The
fixed-field equality rules out $r$ algebraically independent rational
integrals even before the additional requirement that they commute.
It also rules out gaining a new global rational integral by passing to any
positive iterate. This is the precise nonintegrability consequence.

If all $c_i$ are distinct, the fixed fiber has no nonconstant rational
integral. If all are equal, then because $c_r=0$ they all vanish; the
fixed field has the $r-1$ generators $q_i/q_r$. Intermediate partitions
give exactly $r-s$ generators. These rational functions are not regular
on the whole fiber, as Theorem 8 demonstrates.

The following failures delimit the assumptions rather than suggest their
automatic removal.

- In characteristic $p$, choosing $f(t)=g(t)=t^p$ makes both shears the
  identity. Characteristic zero cannot be silently dropped.
- If $f$ or $g$ is constant, there is only one effective shear, which
  preserves an entire coordinate block. Nonconstancy is essential.
- For $r=2$ and $f(t)=g(t)=t$, the map is linear. On the coordinate pair
  $(q_1,p_2)$ it is $(q_1,p_2)\mapsto(2q_1+p_2,q_1+p_2)$, and
  $q_1^2-q_1p_2-p_2^2$ is invariant. It is not a function of the single
  momentum difference: on $c_1=0$ with $q_2=p_1=0$ it remains
  nonconstant. Thus the stated classification fails in dimension four.
- With $r\ge3$, replacing $f(Q)$ by $f(Q)+q_1$ adds $q_1$ to the
  first momentum difference in the first phase. Product support is a
  substantive restriction, not harmless notation.
- A collided original $M_c$ is not replaced by a torsor without a
  birational change and a base-field extension. The weighted model in
  Lemma 4 deliberately retains the full finite component group.

For contextual comparison only, if $d=\deg f$, $e=\deg g$ then
$$
\deg F^k=[(rd-1)(re-1)]^k\quad(k\ge1).
$$
Every $q_i$ has that degree and every $p_i$ has degree
$(rd-1)[(rd-1)(re-1)]^{k-1}$. This follows by strict degree comparison
between a nonzero leading product and the carried coordinate. It is an
absorbed degree-growth calculation, not the proposed headline.

## Novelty deductions and open risks

The no-periodic-curve conclusion is already supplied much more generally
by Marc Abboud, *On the dynamics of endomorphisms of affine surfaces*,
arXiv:2311.18381v3, Proposition 13.20; independent literature review has
checked the 2026-06-17 version. The shears on $D_h$ and the categorical
quotient language belong to established Danielewski/hypertoric theory.
Nagata's UFD criterion and the character decomposition of a diagonalizable
group are established tools. Their direct proofs above do not create
novelty. The only proposed research headline is the exact global and
all-fiber first-integral classification, including the distinction between
rational and regular integrals under momentum collisions.

Independent reviewers must still assess whether that classification is
already a known consequence in the literature and whether its remaining
value supports a standalone paper. The author proof has not received a
formal independent PASS. Priority, exhaustiveness and publication
readiness are not claimed.

The most important adversarial checks are: constant-field descent;
nonsaturated character lattices and the one-block finite-group case;
dimension and nonemptiness of weight zero-set images; the distinction
between original collided fibers and the distinct-value affine model;
normal-form divisibility in Theorem 8; and zero coordinate functions at
infinity in Lemma 2.
