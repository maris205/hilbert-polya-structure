# Sixteenth author deductions and disposition

Author: `/root/sixteenth_finite_scout`. These are author proofs, not an
independent candidate review. Literal maps and the immutable 26-box ceiling
are in INTAKE.md. Source and exact historical limits are in
SOURCE_AND_COLLISION.md. No number or reserve is assigned.

## Status and dependency map

The statements explicitly proved below are **PROVABLE AS STATED**. A full
CNL all-length temporal theorem and an LRG all-shape temporal/inverse pair
are **NOT CURRENTLY JUSTIFIED**. Finite observations are separately labelled.

1. CNL uses only rotation orbits, characteristic-two cyclic differences,
   and a canonical-section injection. The augmentation and static orbit
   mechanisms are deducted through P178 and the classical background.
2. D2LC first uses P200's generic least-active-involution argument, then a
   finite four-vertex add/remove case analysis. Its inverse bound follows
   from the least active target vertex and its two neighbours. Section 4
   explicitly tests whether the sharper constants escape that template.
3. LRG has only carrier/content and one-dimensional statements here.
4. LIR is inversion sorting; LMH's sharp clock is directly source-owned;
   KFR is an oriented classical Knuth rewrite with a finite lexical order.

## 1. CNL: true partial results, not an all-length temporal atlas

Let $S$ be left rotation on $\mathbb F_2^n$, and let $m(w)$ be the least
rotation. The map is $F(w)=w+m(w)$.

### 1.1 Fixed points and a power-of-two nilpotency bound

Every output has even Hamming weight, since rotation preserves the sum
of coordinates in $\mathbb F_2$. If $F(w)=w$, then $m(w)=0$, and therefore
$w=0$. Thus zero is the unique fixed point, for every $n\ge1$.

For $n=2^a$, put $N=I+S$. The characteristic-two binomial identity gives
$N^n=I+S^n=0$. For any $0\le k<n$, $I+S^k$ is divisible by $N$ as a
polynomial in $S$ (for $k=0$ it is zero). At any epoch the selected least
rotation is $S^kw$ for some such $k$. Consequently
$$F(N^t\mathbb F_2^n)\subseteq N^{t+1}\mathbb F_2^n,$$
regardless of how the direction is selected. It follows that $F^n=0$.
This handles $n=1$, where the whole map is zero. It proves a bound, not a
sharp all-$a$ clock. The same state-selected augmentation-filtration
argument is already explicit in P178. No new temporal credit is assigned
merely for changing the selector from an anchored value to a minimum rotation.

For odd $n\ge3$, the bounded pilot's nonzero cycles cannot be dismissed as
an arithmetic artifact. If a nonconstant word starts with one, its least
rotation starts with zero, so its first bit stays one. After the first
step its weight is even, hence it cannot be the all-one word at odd $n$.
It can never reach zero; finiteness and the unique-fixed-point result force
a nontrivial cycle in its future. This proves existence of a nontrivial
recurrent component for every odd $n\ge3$, but does not classify periods,
components or maximal entrance times. The literal $n=11$ twenty-cycle and
44-step tail are preserved in CANONICAL.json.

### 1.2 Exact fibre expression and unique maximum: canonical-section template

Let $\mathcal R_n$ contain exactly the least word of each rotation orbit.
For every target $y$,
$$F^{-1}(y)=\{y+r:r\in\mathcal R_n,\ m(y+r)=r\}.$$
Indeed any source $w$ determines $r=m(w)$ and $w=y+r$; conversely every
accepted $r$ gives that source. Distinct representatives give distinct
sources. Hence every fibre has size at most $|\mathcal R_n|$. For $y=0$
all representatives succeed. If $y\ne0$, the representative $r=0$ fails:
$m(y)=0$ would imply $y=0$. Thus zero is the **unique** maximal target.

The maximum equals the classical binary-necklace count
$$|\mathcal R_n|=\frac1n\sum_{k=0}^{n-1}2^{\gcd(n,k)}.
$$
To verify the displayed count without importing an uninspected theorem,
count pairs $(w,k)$ with $S^kw=w$. A rotation $k$ partitions the coordinates
into $\gcd(n,k)$ cycles, each freely assigned a bit. Each rotation orbit
contributes exactly $n$ such pairs by the orbit–stabilizer identity, proving
the formula, including $n=1$.

This entire maximum mechanism holds for any chosen section $c$ of a finite
equivalence relation inside an abelian group under the map $x\mapsto x-c([x])$:
there is at most one source per equivalence class, and the zero target has
one per class. A singleton zero class makes the maximum unique. Thus even
the all-target maximum here is a generic section-subtraction result, not a
second map-specific mechanism. CNL is **NO_PROMOTION / HOLD_GLOBAL_TEMPORAL**;
the power-of-two bound and the correct maximum do not create a reserve.

## 2. D2LC: complete all-parameter temporal and inverse theorem

Assume a labelled simple graph $G$ on $\{0,\ldots,n-1\}$, $n\ge1$.
Let $A(G)=\{v:d_G(v)=2\}$. If nonempty write $p=\min A(G)$,
$N_G(p)=\{a,b\}$, and $G^v$ for local complementation at a degree-two
vertex $v$. It toggles the one edge between its two neighbours. Let
$$\epsilon_v(G)=\begin{cases}+1,&\text{the neighbours of }v\text{ are nonadjacent},\\
-1,&\text{they are adjacent}.\end{cases}$$
Only the two neighbour degrees change, each by $\epsilon_v(G)$.

### 2.1 Fixed and recurrent states: the deducted generic part

If $A(G)=\varnothing$, $G$ is fixed. Otherwise $G^p\ne G$ and $p$ remains
degree two, because no incident edge of $p$ is changed. Thus a nonfixed
state never maps to a fixed state and $\min A(G^p)\le p$.
If equality holds, the next move toggles the same edge back, and $G$ has
exact period two. If strict inequality holds, no orbit can return to $G$,
because selected labels never increase. Therefore every recurrent state
is either a fixed degree-two-free graph or a two-cycle, and a nonfixed
graph is recurrent exactly when
$$\{h\in\{a,b\}:h<p,\ d_G(h)=2-\epsilon_p(G)\}=\varnothing.\tag{D1}$$
This is exactly P200's least-active-involution proof with a different
active predicate. Neither the recurrent test nor a crude $n-1$ descent
bound escapes that old mechanism.

### 2.2 Exact entry time, with all boundary cases

If $A(G)=\varnothing$ or (D1) holds, $\tau(G)=0$.
Otherwise let $q=\min A(G^p)<p$, and let $r$ be the other neighbour of
$p$ in $G$. Then $q\in\{a,b\}$. The following rule is complete:

* If $\epsilon_p(G)=+1$, then $\tau(G)=1$.
* If $\epsilon_p(G)=-1$, then $q$ has degree three in $G$, with neighbours
  $p,r,s$ for a unique $s\notin\{p,q,r\}$. In this case
  $$\tau(G)=\begin{cases}2,&s<q\text{ and }d_G(s)=1,\\1,&\text{otherwise}.\end{cases}\tag{D2}$$

Proof for the addition case: $q$ had degree one and sole neighbour $p$.
After adding $qr$, its neighbours are $p,r$. The next move deletes $pr$.
This changes $p$ from degree two to one and restores $r$ to its original
degree. If that original degree was two, $r\ge p>q$ because $p$ was the
original minimum. No label below $q$ becomes active; $q$ stays minimum.
Thus $G^p$ is recurrent and the original strict descent makes $\tau(G)=1$.

Proof for the deletion case: initially $p,q,r$ form a triangle, and $q$
has the unique extra neighbour $s$. After deleting $qr$, pivot $q$ has
neighbours $p,s$. Vertex $p$ initially had only neighbours $q,r$, so $ps$
is absent. The second move therefore adds $ps$. It raises $p$ from degree
two to three and raises $s$ by one; no other degree changes. The only way
to create a new minimum below $q$ is exactly $s<q$ and $d_G(s)=1$.
If this does not happen, the pivot at the next epoch remains $q$, and
$G^p$ was recurrent, giving $\tau=1$.

If it happens, $s$ originally had sole neighbour $q$, and now has neighbours
$p,q$. The third move deletes $pq$. It lowers $q$ to degree one and
$p$ to degree two. Both labels exceed $s$, so no earlier active vertex is
created. The pivot stays $s$ and the state after two steps is recurrent.
Both preceding pivot drops were strict, so its first entrance time is
exactly two. This proves (D2), not just an upper bound.

For $n=1,2$, no degree-two vertex exists and the maximum tail is zero.
For $n=3$, a pivot neighbour cannot have degree three, so the maximum is
one, attained by edges $02,12$. For every $n\ge4$, the four-vertex graph
with edges $01,12,13,23$ and all other vertices isolated has the pivot
sequence $2,1,0,0,\ldots$ and exact entry time two. Thus the uniform sharp
maximum is $0,0,1,2,2,\ldots$ for $n=1,2,3,4,5,\ldots$.

### 2.3 Every target predecessor without forward iteration

Fix an arbitrary target $H$.
If $A(H)=\varnothing$, its only predecessor is itself: an active pivot
survives its own move, so a nonfixed source cannot map here.

Otherwise let $u=\min A(H)$. Every source has some active pivot $v$ which
is still degree two in $H$, and the source must be $H^v$. If $v\ne u$,
then $v>u$, while $u$ must be inactive in the source. Its degree can have
changed only if $u\in N_H(v)$, equivalently $v\in N_H(u)$. Hence only
$$V_H=A(H)\cap(\{u\}\cup N_H(u))\tag{D3}$$
can supply inverse pivots. There are at most three.

For $v\in V_H$, let $N_H(v)=\{c,d\}$ and $\epsilon=\epsilon_v(H)$.
The source $H^v$ is accepted exactly when both conditions hold:

1. no $h<v$ outside $\{c,d\}$ has $d_H(h)=2$;
2. for $h\in\{c,d\}$ with $h<v$, $d_H(h)\ne2-\epsilon$.

These conditions compute source degrees directly from the target; they
do not execute the forward selector on a candidate source. They are
necessary and sufficient for $v$ to be its least degree-two vertex.
Every accepted candidate really maps to $H$, because local complementation
is an involution. Two accepted pivots cannot produce the same source,
which has only one least degree-two vertex. This is an exact all-target
inverse formula, including empty fibres.

### 2.4 Uniform fibre maximum and every equality target

For $n=1,2$, every fibre is one. For every $n\ge3$, the maximum fibre
is three. A target has three predecessors **if and only if** it contains
an isolated triangle $T$ and every degree-two vertex outside $T$ has
label greater than $\max T$.

Proof of necessity: a three-parent target must have all three potential
pivots in (D3) accepted. Write $N_H(u)=\{a,b\}$ with $a<b$. Both $a,b$
must have degree two and $u<a<b$. If $a,b$ were nonadjacent, the move at
$b$ would toggle an edge involving $u$ and its other neighbour, not $a$.
Vertex $a$ would remain degree two with label $a<b$, so $H^b$ could not
have least pivot $b$. Thus $a,b$ are adjacent; all three triangle vertices
have degree two, so this triangle is isolated. For the pivot $b$ to be
admissible, no external degree-two vertex can have label below $b$.

For sufficiency, complementing at any of the three vertices deletes the
opposite triangle edge. Its other two vertices then have degree one, the
pivot has degree two, and every external active vertex comes after it.
All three inverses are accepted. Such targets exist at every $n\ge3$ by
adjoining isolated vertices to one triangle. The same argument shows the
triangle in an equality target is uniquely determined as the component
containing the least active target vertex. No closed global census of
graphs avoiding degree two is asserted.

## 3. D2LC value audit: why the sharper constants are still a local shell

The theorem above is correct all-parameter mathematics. That alone does
not prove a materially new two-axis contribution. The old P200 source is
read at its original definition and recurrent proof; only its **generic**
priority-involution part transfers. There is no claimed conjugacy between
all D2LC graphs and all binary rectangle matrices, no claimed transfer of
P200's width-sensitive sharp clock, and no import of its inverse maximum.

Nevertheless D2LC's residual is confined to bounded local data:

* The only changed edges over any trajectory are inside at most four
  vertices: the initial pivot $p$, its two neighbours $q,r$, and, only in
  the deletion case with a smaller new pivot, the unique extra neighbour
  $s$ of $q$. The entire add case is a three-vertex wedge/triangle toggle.
  The only two-step transient is the four-vertex triangle-with-leaf
  pattern in Section 2.2, with a prescribed decreasing label chain.
* Outside this set all edges stay fixed, and all outside degrees stay
  fixed. Because the initial pivot was minimum and subsequent pivots only
  decrease, an initially outside active vertex never becomes the chosen
  pivot. The inside behaviour is determined by the internal edges, the
  relative label order, and the **fixed** residual degrees contributed by
  outside edges. Recording each residual degree as $0,1,2,\ge3$ suffices
  for testing degree two. Thus an orbit is a lift of a finite decorated
  local machine with at most six variable edge bits; the ambient graph
  contributes passive boundary data, not an unbounded dynamic interaction.
* This is an orbitwise frozen-environment lift, **not** a global fixed
  three-vertex quotient: the initial graph chooses the four labels, their
  outside degree contributions matter, and recomputing that chosen set at
  a later state can drop a formerly relevant vertex. An unmarked global
  three-vertex semiconjugacy is not claimed. The displayed frozen support
  and degree data are sufficient for every actual forward trajectory.
* The inverse bound is also generic: for a least-active local operation
  which can deactivate the least target vertex only from an adjacent
  active pivot, all predecessors lie at that vertex or its neighbours.
  The present active predicate fixes its degree at two, making the bound
  three automatic. Equality checks only whether those three local choices
  form an isolated triangle and whether an earlier outside active label
  blocks a choice. It does not create an independent large-graph fibre
  mechanism; passive graph counting would only decorate the same gadget.

**Author recommendation: NO_PROMOTION / KILL_BOUNDED_LOCAL_PRIORITY_GADGET.**
The sharp constants improve the crude generic bound numerically, but both
are exhausted by a fixed four-vertex forward case split and a three-choice
local inverse. Enlarging $n$ adds passive environments, not new coupled
temporal or inverse structure. This is an author value recommendation;
root has not accepted it and no independent gate is invented.

## 4. LRG: no all-size idempotence claim

Each row rotation and each column rotation preserves the number of ones,
and the literal composition preserves the full finite carrier. If $r=1$,
the map is simply least cyclic rotation and hence idempotent. If $c=1$,
it is greatest cyclic rotation and hence idempotent. These arguments
include the $1\times1$ identity map. They do not apply to general shapes.

All eight original boxes, including $3\times4$, happened to be idempotent.
This is only a finite observation. It proves neither that the composition
of two canonicalizers is always idempotent, nor an all-shape inverse
formula. Whole-row/column sorting from old D11_DLX is a different literal,
so its theorem cannot fill the gap. **NO_PROMOTION / HOLD_ALL_SHAPE_PROOF**;
no fourth pilot or larger matrix is silently added.

## 5. Desk-only LIR, LMH and KFR

### 5.1 LIR: complete elementary convergence, absent separate residual

For a permutation $w$, write $I(w)=\#\{i<j:w_i>w_j\}$. Swapping two
positions $i<j$ with values $a<b$ increases $I$ by
$$1+2\#\{i<k<j:a<w_k<b\}.$$
To check this, the pair $(i,j)$ contributes one, every intermediate value
strictly between $a,b$ contributes two, values outside that interval give
net zero, and all positions outside $[i,j]$ see the same two values.
An increasing selected subsequence can be reversed by successively
swapping its outermost as-yet-unswapped positions. At each swap their
current values remain in increasing order; the inner selected values have
not been moved. Every swap increases $I$, and at least one swap occurs
whenever the LIS has length at least two. Thus every nonfixed step
increases $I$; the only fixed/recurrent permutation is $n,n-1,\ldots,1$,
and the entrance time is at most $\binom n2-I(w)$.

For any target, one can try each position tuple, reverse it, and accept
exactly when it is the reconstructed source's lex-first longest increasing
subsequence. This is a tautological admissible-selection inverse, not a
separate target theorem. The inversion-potential mechanism is the same
killed sorting shell as C01_DRF, with the inequality direction reversed.
No sharp global time or fibre extremum is proved. **NO_PROMOTION /
KILL_SORTING_POTENTIAL_ONLY**. No numerical run was needed.

### 5.2 LMH: exact primary owner, not a fresh theorem

Every LMH step is precisely a placement-and-shift operation. The primary
Elizalde–Winkler Section 5 explicitly supplies both the universal maximum
$2^{n-1}-1$ and the attaining permutation $2,3,\ldots,n,1$ under exactly
the leftmost-misplaced scheduler. Thus its sharp temporal axis is fully
owned, not merely bounded by a related algorithm. For $n=1$ it is the
identity. At any $n$, a fixed permutation must be the identity, since a
nonidentity has a legal changed placement.

Every one-step predecessor is reconstructed by choosing a value currently
at home in the target and displacing it to another position, plus the
identity loop when applicable; retain precisely those displacements whose
removed value occurs at the leftmost misplaced source position. This is
the source's classical reverse placement operation with the declared
selector restriction. No separate global inverse extremum is supplied.
**NO_PROMOTION / KILL_DIRECT_TEMPORAL_OWNER**, without a pilot.

### 5.3 KFR: explicit oriented rewrite, not a confluence theorem

On the alphabet $0<1<2$, the complete lex-increasing elementary rules are
$$010\to100,\quad020\to200,\quad021\to201,\quad121\to211,$$
$$101\to110,\quad102\to120,\quad202\to220,\quad212\to221.$$
They follow by substituting the three letters into the two displayed
Knuth inequalities. Each preserves length and letter multiplicities,
and strictly increases the whole word lexicographically. Hence every
orbit terminates; every recurrent state is a fixed word avoiding exactly
these eight length-three left-hand sides. The coarse bound $3^n-1$ on
changed steps is just the cardinality of the finite lexical order.

The selected Knuth move preserves the insertion tableau by the classical
Knuth relation theorem stated in the inspected primary Section 2.3.
No confluence or unique terminal word within an insertion class follows
from termination. For an exact but generic one-step inverse, reverse each
possible right-hand side at a position, then retain the candidates whose
first left-hand-side occurrence is that position; include a fixed target's
self-loop. Finite-pattern language recognition and this local inverse
enumeration do not add a separate residual mechanism. **NO_PROMOTION /
KILL_ORDERED_KNUTH_REWRITE_SHELL**. No numerical run was made.

## 6. Evidence boundaries

The main standalone producer executes only CNL/D2LC/LRG on the 26 intake
boxes, with complete canonical stdout and two actual isolated processes.
The D2LC theorem sidecar, if executed, rechecks only the same six graph
boxes and is author theorem pressure, not six new boxes or a fourth map.
The immutable original producer, failed source accesses and original raw
pair are preserved. No proof here repairs the missing CNL all-length or
LRG all-shape obligations. No independent reviewer, accepted delta, or
paper completion follows from this document.
