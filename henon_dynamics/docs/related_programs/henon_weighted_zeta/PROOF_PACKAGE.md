# Proof Package

## Claim

Let $a>0$, let $q(x)=a x^2$, and let

$$
H_{a,c}(x,y)=(c-q(x)-y,x).
$$

Let $e_0<\cdots<e_N$ define the common closed cells
$I_r=[e_r,e_{r+1}]$ and product cells $C_{ij}=I_i\times I_j$. Subdivide each
$I_i$ into finitely many positive-width closed slabs, and use the exact range
of $q$ on every slab to construct the forward and inverse axis-aligned outer
rectangles.

Define

$$
S_{jk}=[c-e_{k+1}-e_{j+1},\ c-e_k-e_j].
$$

For each internal boundary $p=e_r$, let $U_p^-$ and $U_p^+$ be the unique
boundary slabs in $I_{r-1}$ and $I_r$, let $Q_p^\pm=q(U_p^\pm)$, and put
$q_p=q(p)$. Define

$$
\omega_p^+=\min(\sup Q_p^-,\sup Q_p^+)-q_p,
\qquad
\omega_p^-=q_p-\max(\inf Q_p^-,\inf Q_p^+),
$$

and, with $\min\varnothing=+\infty$,

$$
\Delta_p^+
=\min_{j,k:\ \inf S_{jk}>q_p}(\inf S_{jk}-q_p),
$$

$$
\Delta_p^-
=\min_{j,k:\ \sup S_{jk}<q_p}(q_p-\sup S_{jk}).
$$

Then the following statements hold.

**Theorem A (closed-edge separation criterion).**

$$
E_{\mathrm{true}}\subseteq E_{\mathrm{mutual}}^{\mathrm{outer}},
$$

and

$$
E_{\mathrm{true}}=E_{\mathrm{mutual}}^{\mathrm{outer}}
$$

if and only if every internal boundary satisfies

$$
\omega_p^+<\Delta_p^+,
\qquad
\omega_p^-<\Delta_p^-.
$$

**Proposition B (positive-area identity).** If positive incidence means
positive two-dimensional Lebesgue measure for the analytic image and strict
positive rectangle overlap for the outer construction, then

$$
E_+^{\mathrm{true}}=E_+^{\mathrm{outer}}
$$

for every finite partition and exact finite slab subdivision above. Mutual
filtering is unnecessary.

**Proposition C (constructive counterexample).** For the centered uniform
$N=60$ partition of $[-R,R]$, with

$$
a=6,\quad c=1,\quad
R=\frac{3190032397181517}{5000000000000000},\quad
\eta=\frac14,
$$

and the frozen adaptive subdivision rule, the mutual outer graph contains
$C_{29,46}\to C_{59,30}$ while the true closed graph does not.

**Corollary D (centered-even adaptive staircase).** Let $N$ be even and use the
centered uniform partition of $[-R,R]$ with width $h=2R/N$. Under the uncapped
adaptive rule

$$
K(a,\eta)=\left\lceil\frac{2ah}{\eta}\right\rceil,
$$

the complete closed graph identity holds if and only if

$$
a\left(\frac h{K(a,\eta)}\right)^2<\Delta_{0,N}^+.
$$

For fixed $a$, the pass indicator can change from pass to fail at most once as
$\eta$ increases. For fixed $\eta$, no analogous monotonicity in $a$ holds in
general because $a/K(a,\eta)^2$ is a sawtooth.

## Status

**PROVABLE AFTER WEAKENING / EXTRA ASSUMPTION.**

The R055--R056-inspired universal claim
$E_{\mathrm{true}}=E_{\mathrm{mutual}}^{\mathrm{outer}}$ is false. Theorem A
is the corrected exact claim. Proposition B survives as a universal statement
within the stated $a>0$, common-partition, exact-range setting.

## Assumptions

- All partition cells and subdivision slabs have positive width.
- Source and target cells use the same one-dimensional partition in both
  coordinates.
- All cells and slabs are closed, so an internal endpoint belongs to both
  adjacent cells or slabs.
- The outer rectangle uses the exact interval $q(U)$, not a rounded
  approximation.
- Forward and inverse outer graphs are constructed with the same cellwise
  subdivision rule. Their subdivision counts may vary by cell.
- $a>0$. This excludes the degenerate case in which $q$ is constant.
- Graph equality is asserted on the complete finite cell graph before active
  restriction.

## Notation

- $C_{ij}\to C_{k\ell}$ denotes a directed forward edge.
- $E_F^{\mathrm{outer}}$ is the forward outer edge set.
- $E_B^{\mathrm{outer}}$ is the inverse outer edge set, oriented in the inverse
  direction.
- The mutual edge set is

  $$
  E_{\mathrm{mutual}}^{\mathrm{outer}}
  =\{(C,D):(C,D)\in E_F^{\mathrm{outer}},\ (D,C)\in E_B^{\mathrm{outer}}\}.
  $$

- $\operatorname{len}$ denotes one-dimensional Lebesgue measure.
- $\operatorname{area}$ denotes two-dimensional Lebesgue measure.

## Proof Strategy

Use direct interval reduction. First eliminate $y$ and show that true
incidence is governed by $q(I_i\cap I_\ell)\cap S_{jk}$. Derive the analogous
slab criterion for both map directions. The common partition reduces all
possible discrepancies to two adjacent cells sharing one point. At that point,
interval order gives the exact overshoot-gap condition. For positive edges,
strict overlap eliminates adjacent-cell contacts and reduces both constructions
to the same finite union of quadratic ranges.

## Dependency Map

1. Lemma 1 reduces exact analytic incidence to $S_{jk}$.
2. Lemma 2 reduces forward and inverse outer incidence to slab range tests.
3. Lemma 3 proves true closed incidence is contained in mutual outer incidence.
4. Lemma 4 localizes every possible strict containment to adjacent cells.
5. Lemma 5 proves the boundary overshoot-gap equivalence.
6. Theorem A follows by taking the conjunction over all internal boundaries.
7. Lemmas 6--7 identify analytic and outer positive-area incidence and prove
   Proposition B.
8. Exact rational substitution at $N=60$ proves Proposition C.
9. Monotonicity of $q$ on the two half-lines and the explicit adaptive rule
   prove Corollary D.

## Proof

### Lemma 1: exact analytic incidence

For any source $C_{ij}$ and target $C_{k\ell}$,

$$
C_{ij}\to C_{k\ell}\text{ in }E_{\mathrm{true}}
\iff
q(I_i\cap I_\ell)\cap S_{jk}\ne\varnothing.
\tag{1}
$$

**Proof.** A source point $(x,y)\in I_i\times I_j$ maps into the target if and
only if $x\in I_\ell$ and

$$
e_k\le c-q(x)-y\le e_{k+1}.
$$

For fixed $x$, such a $y\in[e_j,e_{j+1}]$ exists if and only if the two closed
intervals

$$
[e_j,e_{j+1}]
\quad\text{and}\quad
[c-q(x)-e_{k+1},c-q(x)-e_k]
$$

intersect. Their intersection is nonempty exactly when

$$
c-e_{k+1}-e_{j+1}\le q(x)\le c-e_k-e_j,
$$

which is $q(x)\in S_{jk}$. Requiring also $x\in I_i\cap I_\ell$ gives (1).
$\square$

### Lemma 2: exact outer slab criteria

For a forward slab $U\subset I_i$, its exact rectangle meets $C_{k\ell}$ if
and only if

$$
U\cap I_\ell\ne\varnothing,
\qquad
q(U)\cap S_{jk}\ne\varnothing.
\tag{2}
$$

For an inverse slab $V\subset I_\ell$ constructed from target cell
$C_{k\ell}$, its exact inverse rectangle meets $C_{ij}$ if and only if

$$
V\cap I_i\ne\varnothing,
\qquad
q(V)\cap S_{jk}\ne\varnothing.
\tag{3}
$$

**Proof.** Write $q(U)=[m_U,M_U]$. The forward rectangle is

$$
[c-M_U-e_{j+1},c-m_U-e_j]\times U.
$$

Its second coordinate meets $I_\ell$ exactly when the first condition in (2)
holds. Its first coordinate meets $I_k$ exactly when

$$
c-M_U-e_{j+1}\le e_{k+1},
\qquad
c-m_U-e_j\ge e_k.
$$

These inequalities are equivalent to
$M_U\ge\inf S_{jk}$ and $m_U\le\sup S_{jk}$, which say that the two closed
intervals $q(U)$ and $S_{jk}$ intersect.

For the inverse map

$$
H_{a,c}^{-1}(X,Y)=(Y,c-q(Y)-X),
$$

write $q(V)=[m_V,M_V]$. The inverse rectangle from $C_{k\ell}$ is

$$
V\times[c-M_V-e_{k+1},c-m_V-e_k].
$$

The same two inequalities, now for intersection with $I_i\times I_j$, reduce
to $V\cap I_i\ne\varnothing$ and $q(V)\cap S_{jk}\ne\varnothing$. This proves
(2)--(3). $\square$

### Lemma 3: true closed edges survive mutual filtering

$$
E_{\mathrm{true}}\subseteq E_{\mathrm{mutual}}^{\mathrm{outer}}.
\tag{4}
$$

**Proof.** Let $C_{ij}\to C_{k\ell}$ be true. By Lemma 1, there is
$x\in I_i\cap I_\ell$ such that $q(x)\in S_{jk}$. Because the finite closed
slabs cover $I_i$, some forward slab $U\subset I_i$ contains $x$. Then
$x\in U\cap I_\ell$ and $q(x)\in q(U)\cap S_{jk}$, so Lemma 2 gives the
forward outer edge. Likewise, some closed inverse slab $V\subset I_\ell$
contains $x$, and Lemma 2 gives the reverse outer edge from $C_{k\ell}$ to
$C_{ij}$. Thus the edge is mutual. $\square$

### Lemma 4: discrepancy localization

If a mutual outer edge is not a true edge, then $|i-\ell|=1$.

**Proof.** If $|i-\ell|>1$, the closed cells $I_i$ and $I_\ell$ are disjoint.
Every forward slab lies in $I_i$, so no forward slab meets $I_\ell$. Lemma 2
therefore rules out a forward outer edge.

Suppose $i=\ell$. A forward outer edge exists exactly when at least one slab
$U\subset I_i$ satisfies $q(U)\cap S_{jk}\ne\varnothing$. The slab union is
$I_i$, hence

$$
q(I_i)=q\left(\bigcup_U U\right)=\bigcup_U q(U).
$$

Therefore the forward outer edge exists exactly when
$q(I_i)\cap S_{jk}\ne\varnothing$. The same equivalence holds for the reverse
outer edge, and Lemma 1 gives the identical true-edge condition. Thus mutual
and true incidence agree when $i=\ell$.

The only remaining possibility is $|i-\ell|=1$. $\square$

### Lemma 5: one-boundary separation equivalence

Fix an internal boundary $p=e_r$. There is no false mutual edge whose two
coordinate cells meet at $p$ if and only if

$$
\omega_p^+<\Delta_p^+,
\qquad
\omega_p^-<\Delta_p^-.
\tag{5}
$$

**Proof.** The adjacent cells meet only at $p$. Hence Lemma 1 says that a true
edge exists exactly when $q_p\in S_{jk}$.

Among the forward slabs in one adjacent cell, only its boundary slab can meet
the other cell. The same holds for the inverse slabs in the other adjacent
cell. Lemma 2 therefore says that the edge is mutual exactly when

$$
S_{jk}\cap Q_p^-\ne\varnothing,
\qquad
S_{jk}\cap Q_p^+\ne\varnothing.
\tag{6}
$$

Each $Q_p^\pm$ is a closed interval containing $q_p$. If $q_p\notin S_{jk}$,
then the closed interval $S_{jk}$ lies strictly on one side of $q_p$.

First suppose $\inf S_{jk}>q_p$. Condition (6) is equivalent to

$$
\inf S_{jk}\le\sup Q_p^-
\quad\text{and}\quad
\inf S_{jk}\le\sup Q_p^+.
$$

Equivalently,

$$
\inf S_{jk}-q_p
\le
\min(\sup Q_p^-,\sup Q_p^+)-q_p
=\omega_p^+.
\tag{7}
$$

Thus no coefficient interval above $q_p$ produces a false mutual edge exactly
when every eligible distance is strictly larger than $\omega_p^+$, which is
$\omega_p^+<\Delta_p^+$. The strict inequality is necessary because equality
still gives closed endpoint intersection in both parts of (6).

Now suppose $\sup S_{jk}<q_p$. Condition (6) is equivalent to

$$
\sup S_{jk}\ge\inf Q_p^-
\quad\text{and}\quad
\sup S_{jk}\ge\inf Q_p^+,
$$

or

$$
q_p-\sup S_{jk}
\le
q_p-\max(\inf Q_p^-,\inf Q_p^+)
=\omega_p^-.
\tag{8}
$$

The absence of a false interval below $q_p$ is therefore equivalent to
$\omega_p^-<\Delta_p^-$. If no coefficient interval exists on one side, the
corresponding gap is $+\infty$ and that side cannot fail. This proves (5).
$\square$

### Proof of Theorem A

Lemma 3 proves the inclusion. Lemma 4 shows that strict inclusion can arise
only at an internal boundary. Lemma 5 gives a necessary-and-sufficient
condition for absence of strict inclusion at each boundary. Taking the
conjunction over the finite set $\{e_1,\ldots,e_{N-1}\}$ proves Theorem A.
$\square$

### Lemma 6: analytic positive-area criterion

The analytic intersection $H_{a,c}(C_{ij})\cap C_{k\ell}$ has positive area if
and only if

$$
\operatorname{len}(I_i\cap I_\ell)>0
$$

and

$$
\operatorname{len}\bigl(q(I_i\cap I_\ell)\cap S_{jk}\bigr)>0.
\tag{9}
$$

**Proof.** Area preservation lets us measure the preimage subset of $C_{ij}$.
For $x\in J:=I_i\cap I_\ell$, the admissible $y$ interval is

$$
[e_j,e_{j+1}]
\cap[c-q(x)-e_{k+1},c-q(x)-e_k].
$$

It has positive length exactly when $q(x)$ lies in the interior of $S_{jk}$.
By Fubini's theorem, the two-dimensional intersection has positive area if and
only if the set

$$
\{x\in J:q(x)\in\operatorname{int}S_{jk}\}
$$

has positive one-dimensional measure.

If (9) holds, the intersection of the two intervals $q(J)$ and $S_{jk}$
contains a nondegenerate interval. Its intersection with
$\operatorname{int}S_{jk}$ contains a nonempty open interval. The preimage of
that open interval under the continuous function $q$ is a nonempty relatively
open subset of the positive-length interval $J$, hence has positive measure.

Conversely, suppose the displayed preimage set has positive measure. Then $J$
has positive length and contains some $x$ with
$q(x)\in\operatorname{int}S_{jk}$. Because $a>0$, the image $q(J)$ is a
nondegenerate interval. An open neighborhood of $q(x)$ lies in
$\operatorname{int}S_{jk}$; its intersection with the nondegenerate interval
$q(J)$ has positive length, including when $q(x)$ is an endpoint of $q(J)$.
This proves both conditions in (9). $\square$

### Lemma 7: outer positive-area criterion

A forward slab $U\subset I_i$ gives a positive-area rectangle intersection
with $C_{k\ell}$ if and only if

$$
\operatorname{len}(U\cap I_\ell)>0
$$

and

$$
\operatorname{len}(q(U)\cap S_{jk})>0.
\tag{10}
$$

**Proof.** Write $q(U)=[m_U,M_U]$. The two rectangle coordinates are

$$
[c-M_U-e_{j+1},c-m_U-e_j]
\quad\text{and}\quad U.
$$

The second coordinate has strict positive overlap with $I_\ell$ exactly when
the first condition in (10) holds. Strict positive overlap of the first
coordinate with $I_k$ is equivalent to

$$
M_U>\inf S_{jk},
\qquad
m_U<\sup S_{jk}.
$$

Both $q(U)$ and $S_{jk}$ have positive length: $U$ has positive width,
$a>0$, and $S_{jk}$ has length
$(e_{k+1}-e_k)+(e_{j+1}-e_j)>0$. The two strict inequalities are therefore
equivalent to positive length of their intersection. $\square$

### Proof of Proposition B

If a slab satisfies Lemma 7, then $U\subset I_i$ and
$\operatorname{len}(U\cap I_\ell)>0$. Distinct cells in the common partition
have at most a one-point intersection, so $i=\ell$.

For $i=\ell$, every slab has positive-length intersection with $I_i$. Hence a
positive outer edge exists exactly when some slab $U\subset I_i$ satisfies

$$
\operatorname{len}(q(U)\cap S_{jk})>0.
$$

The finite family $q(U)$ covers $q(I_i)$. If each $q(U)\cap S_{jk}$ had zero
length, each would be empty or a singleton, and their finite union could not
cover a positive-length interval in $q(I_i)\cap S_{jk}$. Therefore

$$
\exists U:\operatorname{len}(q(U)\cap S_{jk})>0
\iff
\operatorname{len}(q(I_i)\cap S_{jk})>0.
$$

By Lemma 6, with $I_i\cap I_\ell=I_i$, the right-hand side is exactly analytic
positive-area incidence. Thus the forward positive edge sets agree. Applying
the same argument to $H_{a,c}^{-1}$ proves the backward identity as well.
$\square$

### Proof of Proposition C

Let

$$
w=\frac{2R}{60}
=\frac{1063344132393839}{50000000000000000}.
$$

The cells adjacent to $p=0$ are $I_{29}=[-w,0]$ and $I_{30}=[0,w]$.
For either cell, the frozen rule gives

$$
K=\left\lceil
\frac{2a\,w\,w}{\eta w}
\right\rceil
=\lceil48w\rceil=2.
$$

The two boundary slabs are $[-w/2,0]$ and $[0,w/2]$, so both exact quadratic
ranges equal $[0,A]$, where

$$
A=6\left(\frac w2\right)^2
=\frac{3392102231689218610081815473763}
{5000000000000000000000000000000000}.
$$

For $j=46$ and $k=59$, direct substitution of the uniform-grid endpoints gives

$$
S_{46,59}=
\left[
\frac{22825777489567}{50000000000000000},
\frac{429902808455449}{10000000000000000}
\right].
$$

Its lower endpoint is positive, so $q(0)=0\notin S_{46,59}$. Cross
multiplication gives

$$
\frac{22825777489567}{50000000000000000}<A.
$$

Hence $S_{46,59}$ intersects both boundary ranges $[0,A]$. Lemma 2 gives the
forward outer edge from $C_{29,46}$ to $C_{59,30}$ and the reverse outer edge
from $C_{59,30}$ to $C_{29,46}$. Lemma 1 rules out the true edge because the
two coordinate cells meet only at $x=0$ and $q(0)\notin S_{46,59}$. The mutual
outer edge is therefore a strict false positive. $\square$

### Proof of Corollary D

For a centered even uniform grid, the cells adjacent to $p=0$ are $[-h,0]$
and $[0,h]$. The minimum target-cell width is $h$. On either central cell, the
adaptive numerator is $2ah^2$, hence the uncapped subdivision count is

$$
K(a,\eta)=\left\lceil\frac{2ah^2}{\eta h}\right\rceil
=\left\lceil\frac{2ah}{\eta}\right\rceil.
\tag{11}
$$

The two slabs incident to zero are $[-h/K,0]$ and $[0,h/K]$. Their exact
quadratic ranges are identical:

$$
\left[0,a\left(\frac hK\right)^2\right].
$$

Therefore

$$
\omega_0^+=a\left(\frac hK\right)^2,
\qquad
\omega_0^-=0.
\tag{12}
$$

Now let $p>0$ be any other internal boundary. Both boundary slabs lie in
$[0,\infty)$, where $q$ is increasing. The left slab range has supremum
$q(p)$, while the right slab range has infimum $q(p)$. Their intersection is
the singleton $\{q(p)\}$, so $\omega_p^+=\omega_p^-=0$. If $p<0$, both slabs
lie in $(-\infty,0]$, where $q$ is decreasing, and the same singleton
intersection conclusion holds with the two roles exchanged.

Every noncentral boundary therefore satisfies Theorem A automatically. At
$p=0$, the lower overshoot is zero, so only the upper inequality remains. This
gives

$$
a\left(\frac h{K(a,\eta)}\right)^2<\Delta_{0,N}^+,
$$

which proves the iff statement.

For fixed $a$, the quantity $2ah/\eta$ is nonincreasing in $\eta$, so its
ceiling $K(a,\eta)$ is nonincreasing. Consequently $a h^2/K(a,\eta)^2$ is
nondecreasing, and a strict inequality against the fixed gap
$\Delta_{0,N}^+$ can change from true to false at most once.

For fixed $\eta$, $K(a,\eta)$ is a nondecreasing integer staircase. On an
interval where $K=m$ is constant, $a h^2/m^2$ increases linearly in $a$. At a
jump from $m$ to $m+1$, the denominator increases discontinuously and the
overshoot drops. Therefore monotonicity in $a$ is not guaranteed, and
fail-to-pass re-entry is possible. $\square$

## Corrections or Missing Assumptions

- The original universal closed-edge identity is corrected to Theorem A.
- Exact slab ranges and a common source/target partition are essential.
- Proposition B is stated for $a>0$; the degenerate $a=0$ case is not covered
  by the quadratic-range proof.
- The claims concern complete cell graphs and do not inherit the R054 active
  node restriction.

## Open Risks

- The independent R057 checker verified that the frozen strict positive label
  agrees with Lemmas 6--7 on four complete microgrids and regenerated the exact
  $N=60$ witness without producer helpers.
- Different partitions in the two coordinates, nonclosed conventions, or
  outward-rounded rather than exact ranges require separate statements.
- None of the proofs upgrades finite graph SCCs to dynamically consistent
  invariant objects.
- The frozen production protocol's strict no-cap gate fails on sixteen
  $\delta=\pm3/8$ stresses. This does not alter Theorem A, which allows any
  finite positive-width subdivision, but it prevents an all-frozen-gates-pass
  report for R057.
- Corollary D uses the uncapped adaptive expression. With a finite cap, replace
  $K(a,\eta)$ by the capped count; the center-boundary iff remains valid, while
  the stated parameter monotonicity must be read for that capped staircase.
