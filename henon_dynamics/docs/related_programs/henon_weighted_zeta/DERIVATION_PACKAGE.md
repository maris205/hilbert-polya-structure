# Derivation Package

## Target

Derive the exact finite-grid relation among three incidence graphs for

$$
H_{a,c}(x,y)=(c-a x^2-y,x),\qquad a>0,
$$

on one common closed interval partition:

1. the exact analytic true-image graph;
2. the exact slab-rectangle outer graph;
3. the forward/inverse mutual outer graph.

The immediate target is an exact necessary-and-sufficient condition for

$$
E_{\mathrm{mutual}}^{\mathrm{outer}}=E_{\mathrm{true}}
$$

on a fixed finite partition. A second target is to determine whether the
positive-area identity

$$
E_{+}^{\mathrm{outer}}=E_{+}^{\mathrm{true}}
$$

needs the mutual filter.

A final special-case target is a closed form for centered even uniform grids,
explaining how the adaptive subdivision staircase in $a$ and $\eta$ moves the
exact failure boundary.

## Status

**COHERENT AFTER REFRAMING / EXTRA ASSUMPTION.**

The universal closed-edge identity suggested by R055--R056 is false. It is
replaced by an exact boundary separation criterion. The positive-area identity
survives unchanged under the assumptions below. The centered $N=60$ grid is an
exact constructive counterexample to the universal closed-edge claim.

## Invariant Object

The organizing object is the **finite-grid incidence defect**

$$
D=E_{\mathrm{mutual}}^{\mathrm{outer}}\setminus E_{\mathrm{true}}.
$$

The derivation localizes $D$ to pairs of adjacent coordinate cells and then
expresses its presence entirely through two one-dimensional quantities at each
internal partition boundary:

- a common quadratic slab overshoot $\omega_p^\pm$;
- a coefficient-interval separation gap $\Delta_p^\pm$.

This is a finite combinatorial-geometric object. It is not an invariant set,
a graph limit, or an operator approximation.

## Assumptions

- $a>0$ and $c\in\mathbb R$ are fixed.
- The one-dimensional box is partitioned by
  $e_0<e_1<\cdots<e_N$ into positive-width closed cells
  $I_r=[e_r,e_{r+1}]$.
- Source and target phase-space cells use the same product partition:
  $C_{ij}=I_i\times I_j$.
- Each $I_i$ has a finite subdivision into positive-width closed slabs whose
  union is $I_i$. Different cells may use different subdivision counts.
- Every slab rectangle uses the exact range of $q(x)=a x^2$ on that slab.
- Closed outer incidence includes endpoint contacts.
- Positive outer incidence means strict positive two-dimensional rectangle
  overlap with a target cell.
- True positive incidence means positive two-dimensional Lebesgue measure of
  $H_{a,c}(C_{ij})\cap C_{k\ell}$. For $a>0$, this agrees with the frozen R055
  strict-overlap predicate.
- The derivation concerns complete finite cell graphs before any active-node,
  SCC, or in-box-hull restriction.

## Notation

- $q(x)=a x^2$.
- $C_{ij}=I_i\times I_j$ is a source cell and
  $C_{k\ell}=I_k\times I_\ell$ is a target cell.
- The coefficient interval associated with source-$y$ cell $j$ and target-$x$
  cell $k$ is

  $$
  S_{jk}=[s^-_{jk},s^+_{jk}]
  =[c-e_{k+1}-e_{j+1},\ c-e_k-e_j].
  $$

- $E_{\mathrm{true}}$ denotes exact closed analytic image incidence.
- $E_F^{\mathrm{outer}}$ and $E_B^{\mathrm{outer}}$ denote forward and inverse
  slab-rectangle outer incidence.
- Their mutual filter is

  $$
  E_{\mathrm{mutual}}^{\mathrm{outer}}
  =E_F^{\mathrm{outer}}\cap(E_B^{\mathrm{outer}})^\top.
  $$

- For an internal boundary $p=e_r$, let
  $I^-_p=I_{r-1}$ and $I^+_p=I_r$. Let $U^-_p\subset I^-_p$ and
  $U^+_p\subset I^+_p$ be the unique boundary slabs containing $p$.
- Write $Q_p^-=q(U_p^-)$, $Q_p^+=q(U_p^+)$, and $q_p=q(p)$.
- The common upper and lower overshoots are

  $$
  \omega_p^+=\min(\sup Q_p^-,\sup Q_p^+)-q_p,
  $$

  $$
  \omega_p^-=q_p-\max(\inf Q_p^-,\inf Q_p^+).
  $$

  Both are nonnegative because $q_p\in Q_p^-\cap Q_p^+$.
- With the convention $\min\varnothing=+\infty$, define

  $$
  \Delta_p^+
  =\min_{j,k:\ s^-_{jk}>q_p}(s^-_{jk}-q_p),
  $$

  $$
  \Delta_p^-
  =\min_{j,k:\ s^+_{jk}<q_p}(q_p-s^+_{jk}).
  $$

## Derivation Strategy

Reduce the two-dimensional image-intersection problem to a one-dimensional
quadratic-range test. The common partition then leaves only three possibilities
for $I_i\cap I_\ell$: empty, a full cell, or one shared boundary point. The
first two cases are automatically exact. In the adjacent-cell case, the true
test sees only $q(p)$, while the mutual outer test sees the intersection of the
two boundary-slab ranges. This converts the entire equality question into a
strict overshoot-versus-gap comparison.

## Derivation Map

1. Eliminate the source $y$ variable to obtain the coefficient interval
   $S_{jk}$.
2. Express true closed incidence as
   $q(I_i\cap I_\ell)\cap S_{jk}\ne\varnothing$.
3. Express a forward slab outer edge as
   $U\cap I_\ell\ne\varnothing$ and $q(U)\cap S_{jk}\ne\varnothing$.
4. Apply the same reduction to the inverse map. The inverse test uses the same
   coefficient interval $S_{jk}$.
5. Split into nonadjacent, identical, and adjacent coordinate-cell cases.
6. In the adjacent case, compare $S_{jk}$ with the common boundary-slab range
   above and below $q(p)$.
7. Minimize over the finite family of coefficient intervals to obtain
   $\Delta_p^\pm$ and the global equality criterion.
8. Repeat with strict overlaps to show that positive-area incidence forces
   $i=\ell$ and is therefore exact without mutual filtering.
9. Specialize to a centered even uniform grid, where every noncentral boundary
   has zero common reach and the entire criterion collapses to one scalar
   center-boundary inequality.

## Main Derivation

### Step 1: exact true closed incidence

A point $(x,y)\in C_{ij}$ maps into $C_{k\ell}$ exactly when

$$
x\in I_i\cap I_\ell
$$

and

$$
e_k\le c-q(x)-y\le e_{k+1}
$$

for some $y\in I_j$. The latter feasibility condition is equivalent to

$$
q(x)\in[c-e_{k+1}-e_{j+1},\ c-e_k-e_j]=S_{jk}.
$$

Hence the exact identity

$$
C_{ij}\to C_{k\ell}\text{ in }E_{\mathrm{true}}
\iff
q(I_i\cap I_\ell)\cap S_{jk}\ne\varnothing.
\tag{1}
$$

### Step 2: exact slab outer incidence

Let $U\subset I_i$ be one forward subdivision slab. Its exact rectangle has
second-coordinate interval $U$ and first-coordinate interval

$$
[c-\sup q(U)-e_{j+1},\ c-\inf q(U)-e_j].
$$

This rectangle meets $C_{k\ell}$ under closed semantics exactly when

$$
U\cap I_\ell\ne\varnothing,
\qquad
q(U)\cap S_{jk}\ne\varnothing.
\tag{2}
$$

For the inverse map

$$
H_{a,c}^{-1}(X,Y)=(Y,c-q(Y)-X),
$$

the reverse outer test subdivides $I_\ell$. A reverse slab $V\subset I_\ell$
meets $C_{ij}$ exactly when

$$
V\cap I_i\ne\varnothing,
\qquad
q(V)\cap S_{jk}\ne\varnothing.
\tag{3}
$$

Equations (2)--(3) use the same $S_{jk}$; this is where reversibility enters
the mutual-filter mechanism.

### Step 3: the true graph is always contained in the mutual outer graph

If (1) holds, choose a witness $x\in I_i\cap I_\ell$ with $q(x)\in S_{jk}$.
At least one closed subdivision slab of $I_i$ contains $x$, and at least one
closed subdivision slab of $I_\ell$ contains $x$. Those slabs satisfy (2) and
(3), respectively. Therefore

$$
E_{\mathrm{true}}\subseteq E_{\mathrm{mutual}}^{\mathrm{outer}}.
\tag{4}
$$

This inclusion is exact and does not require a separation condition.

### Step 4: reduction to adjacent coordinate cells

Because $I_i$ and $I_\ell$ belong to the same one-dimensional partition, only
three cases occur.

1. If $|i-\ell|>1$, then $I_i\cap I_\ell=\varnothing$. No forward slab of
   $I_i$ meets $I_\ell$, so neither graph has the edge.
2. If $i=\ell$, the slab ranges cover $q(I_i)$:

   $$
   q(I_i)=\bigcup_{U\subset I_i}q(U).
   $$

   Thus both forward and reverse outer tests are equivalent to
   $q(I_i)\cap S_{jk}\ne\varnothing$, which is exactly (1).
3. If $|i-\ell|=1$, the cells share one boundary point $p$. The true test is

   $$
   q_p\in S_{jk},
   \tag{5}
   $$

   whereas the mutual outer test is

   $$
   S_{jk}\cap Q_p^-\ne\varnothing,
   \qquad
   S_{jk}\cap Q_p^+\ne\varnothing.
   \tag{6}
   $$

Consequently every possible false mutual edge is an adjacent-cell boundary
edge.

### Step 5: common overshoot controls every false mutual edge

Both $Q_p^-$ and $Q_p^+$ are closed intervals containing $q_p$. If
$q_p\notin S_{jk}$, the closed interval $S_{jk}$ lies strictly above or
strictly below $q_p$.

If $S_{jk}$ lies above $q_p$, condition (6) holds exactly when

$$
s^-_{jk}-q_p\le\omega_p^+.
\tag{7}
$$

If $S_{jk}$ lies below $q_p$, condition (6) holds exactly when

$$
q_p-s^+_{jk}\le\omega_p^-.
\tag{8}
$$

Taking the nearest interval on either side gives the boundary criterion

$$
\text{no false mutual edge at }p
\iff
\omega_p^+<\Delta_p^+
\text{ and }
\omega_p^-<\Delta_p^-.
\tag{9}
$$

The inequalities are strict: equality produces a closed endpoint contact in
both outer rectangles while the true image still misses the target.

Combining all internal boundaries yields

$$
E_{\mathrm{mutual}}^{\mathrm{outer}}=E_{\mathrm{true}}
\iff
\forall p\in\{e_1,\ldots,e_{N-1}\},\quad
\omega_p^+<\Delta_p^+,
\quad
\omega_p^-<\Delta_p^-.
\tag{10}
$$

Equation (10) is an exact finite-grid necessary-and-sufficient criterion, not
an asymptotic approximation.

### Step 6: positive-area incidence is exact without the mutual filter

For a slab rectangle to meet $C_{k\ell}$ with positive two-dimensional area,
both coordinate overlaps must have positive length. In particular,
$U\cap I_\ell$ must have positive length. Since $U\subset I_i$ and the cells
belong to one common partition, this forces $i=\ell$.

When $i=\ell$, a slab gives a positive outer edge exactly when

$$
\operatorname{len}(q(U)\cap S_{jk})>0.
$$

There are finitely many slabs and their quadratic ranges cover $q(I_i)$.
Therefore

$$
\exists U:\operatorname{len}(q(U)\cap S_{jk})>0
\iff
\operatorname{len}(q(I_i)\cap S_{jk})>0.
$$

For $a>0$, the right-hand side is equivalent to positive Lebesgue area of the
exact analytic intersection. Hence

$$
E_+^{\mathrm{outer}}=E_+^{\mathrm{true}}
\tag{11}
$$

for every such finite partition and finite exact slab subdivision. No mutual
filter or overshoot-gap condition is needed.

### Step 7: the centered $N=60$ constructive failure

Use the frozen R055--R056 parameters

$$
a=6,\qquad c=1,\qquad
R=\frac{3190032397181517}{5000000000000000},
\qquad \eta=\frac14,
$$

with the centered uniform $N=60$ partition. At the internal boundary $p=0$,
the adjacent cells both use $K=2$ and their boundary slabs have the common
quadratic range

$$
[0,A],\qquad
A=\frac{3392102231689218610081815473763}
{5000000000000000000000000000000000}.
$$

Thus $\omega_0^+=A$. For $j=46$ and $k=59$,

$$
S_{46,59}=
\left[
\frac{22825777489567}{50000000000000000},
\frac{429902808455449}{10000000000000000}
\right].
$$

Its lower endpoint is strictly positive and

$$
\frac{22825777489567}{50000000000000000}<A.
$$

Therefore both boundary-slab ranges meet $S_{46,59}$, but
$q(0)=0\notin S_{46,59}$. The mutual outer graph contains the edge

$$
C_{29,46}\longrightarrow C_{59,30},
$$

while the true closed graph does not. This is an exact touch-only false mutual
edge and disproves the universal identity.

### Step 8: centered-even adaptive staircase

Let $N$ be even and let the centered partition of $[-R,R]$ be uniform with

$$
h=\frac{2R}{N}.
$$

The central cells are $[-h,0]$ and $[0,h]$. Under the uncapped R053 adaptive
rule, both use

$$
K(a,\eta)=\left\lceil\frac{2ah}{\eta}\right\rceil.
\tag{12}
$$

Their boundary slabs are $[-h/K,0]$ and $[0,h/K]$, so

$$
Q_0^-=Q_0^+=\left[0,a\left(\frac hK\right)^2\right],
$$

and hence

$$
\omega_0^+=a\left(\frac hK\right)^2,
\qquad
\omega_0^-=0.
\tag{13}
$$

At every nonzero grid boundary, both incident slabs lie on one monotonicity
half-line of $q(x)=a x^2$. One slab range reaches $q(p)$ only from below and the
other only from above. Their common range is therefore the singleton
$\{q(p)\}$, so both common overshoots vanish.

Let $\Delta_{0,N}^+$ denote the nearest coefficient gap above zero for this
fixed grid. The complete graph criterion (10) reduces exactly to

$$
a\left(\frac{h}{K(a,\eta)}\right)^2<\Delta_{0,N}^+.
\tag{14}
$$

Equivalently, with

$$
\Theta_N=\frac{\Delta_{0,N}^+}{h^2},
$$

the grid passes if and only if

$$
\frac{a}{K(a,\eta)^2}<\Theta_N.
\tag{15}
$$

For fixed $a$, $K(a,\eta)$ is nonincreasing as $\eta$ grows, so the left side
of (15) is nondecreasing. A pass sequence ordered by increasing $\eta$ can
therefore switch from pass to fail at most once.

For fixed $\eta$, $K(a,\eta)$ is a nondecreasing integer staircase in $a$.
Within a plateau, $a/K^2$ increases linearly; when $K$ jumps, $a/K^2$ drops.
Thus the $a$ dependence is a sawtooth and can exhibit fail-to-pass re-entry.
R057S1 observes exactly this distinction: zero nonmonotone eta sequences, but
re-entry for $N=46,92,106$ in the frozen $a$ panel.

## Remarks and Interpretation

- R055--R056 did not reveal a universal theorem; they sampled configurations
  with positive separation headroom. Their zero symmetric differences can now
  be explained by checking (10), rather than treated as unexplained luck.
- False mutual edges are not diffuse rectangle inflation. They are localized
  boundary arithmetic events in which two exact boundary slabs overshoot the
  same side of $q(p)$ far enough to reach a coefficient interval.
- For a centered even grid, $p=0$ is especially vulnerable because both
  adjacent quadratic ranges overshoot upward from the shared minimum. It is
  not the only possible obstruction: shifted boundary slabs can cross the
  critical point, and the general $\omega_p^\pm$ definition covers that case.
- Increasing subdivision resolution weakly shrinks each boundary range and
  therefore cannot increase $\omega_p^\pm$ for a fixed partition. Changing
  $N$, offset, $a$, $c$, or $R$ also moves the coefficient gaps, so exactness
  need not vary monotonically with grid resolution.
- The positive graph is structurally more robust because positive coordinate
  overlap rules out adjacent-cell boundary contacts before quadratic
  overshoot enters.
- On centered even uniform grids, the obstruction is exactly the $p=0$ scalar
  inequality (14), not merely a vague critical-point neighborhood effect.

## Boundaries and Non-Claims

- Equation (10) concerns finite exact cell-incidence graphs only.
- It does not certify an invariant set, an isolating neighborhood, a Markov
  partition, a covering relation, symbolic conjugacy, entropy, or a graph
  limit.
- It does not imply convergence of Ulam, finite-volume, transfer, Koopman, or
  zeta operators.
- A graph path can concatenate existential edge witnesses that do not form one
  dynamically consistent orbit.
- The result has no implication for prime distributions, Riemann zeros, RH,
  or Hilbert--Pólya.

## Open Risks

- The independent R057 checker has now verified the exact R053/R055 endpoint
  conventions, four complete microgrids, the positive-area identity, all
  persisted boundary arithmetic, and every production failure witness without
  importing producer incidence or certificate helpers.
- The positive-area proposition assumes $a>0$. The degenerate linear case
  $a=0$ requires a separate area argument and is outside R057.
- If source and target use different partitions, or if slab ranges are rounded
  rather than exact, the adjacency reduction and criterion must be modified.
- The criterion explains edge equality; it does not by itself explain the SCC
  scaling and filament-like refinement observations from R056.
- Sixteen frozen $\delta=\pm3/8$ production stresses activate the $K=64$ cap,
  so the strict R057 no-cap gate fails even though the capped finite-subdivision
  criterion remains well-defined and independently audited.
