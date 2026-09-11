# P166 replacement discovery, round 2

**Decision: `KILL_ALL`.  External lifecycle: `HOLD_EXTERNAL`.**

This was a breadth-first search restricted to finite automata/DAG/poset
maps, abstract simplicial complexes and clutters, and
matroid/greedoid/convex-geometry maps.  It did not revisit words, codes,
matrices, permutations, or finite-field point configurations.  Four new
literal maps were exhaustively tested.  A fifth map, strict relation
squaring, was replayed only as a permanent-kill sentinel because the same
literal map already occurs in an earlier scout.

The strict gate required one map to have all of the following after owner
subtraction:

1. a natural, untagged self-map;
2. a nontrivial all-parameter clock and recurrent core;
3. an all-time image theorem or every-target fibre theorem;
4. correct empty/rank-zero/small-ground boundaries; and
5. no P1--P165 proof-silhouette collision.

No candidate meets the conjunction.  In particular, no result below is a
paper contract and no priority inference is made from a bounded search.

## Exact-search envelope

`verify_scout.py` contains independent implementations and generators; it
imports no project code.  The frozen run makes **275,111 assertions**.
Two fresh process-substitution replays both matched `CANONICAL.txt` byte for
byte.  The canonical transcript SHA-256 is
`eed8fefe38a28abfb05a4f9f1746e2d0f10effb02d1295906718cb7b2cd6ecd6`;
the verifier SHA-256 is
`ca5fbe7d4f50c7115d4d53efeae3cf2b0aa2147bca27ae63b47014ca68e53947`.

| code | carrier checked | literal states checked | strongest exact signal | decision |
|---|---:|---:|---|---|
| `PFR` | all acyclic orientations of all simple graphs on `[n]`, `0<=n<=5` | `1,1,3,25,543,29281` by rank | exact every-target one-step fibre; tails and periods enumerated | `KILL_DIRECT_OWNER` |
| `USC` | all abstract complexes on `[n]`, including void, `0<=n<=5` | `2,3,6,20,168,7581` | exact `2^t`-union iterate, sharp logarithmic depth, stable fibres | `KILL_DIRECT_INGREDIENT_AND_P97` |
| `ASD` | all labelled matroids on all subgrounds of `[n]`, `0<=n<=5` | `1,3,10,38,171,967` | exact one-step image and every-target fibre | `KILL_STANDARD_SIMPLIFICATION_RANK_EROSION` |
| `CGP` | all labelled convex geometries on `[n]`, `0<=n<=4` | `1,1,3,22,485` geometries | extreme-layer clock; all `4,468` closed states at rank four | `KILL_DIRECT_PEELING_OWNER_THIN` |
| `PSE` | all labelled posets on `[n]`, `0<=n<=5` | `1,1,3,19,219,4231` | exact power-of-two erosion clock | `PERMANENT_KILL_PRIOR_LITERAL_S03` |

The transition-table hashes in `CANONICAL.txt` bind the actual labelled
tables, not only the displayed aggregate counts.

## 1. PFR: parallel full-source reversal

### Literal map

Fix a labelled simple graph `Gamma`.  A state is an acyclic orientation
`D` of `Gamma`.  Let `S(D)` be all current sources, including isolates.
Reverse every edge incident with a vertex of `S(D)` simultaneously.
Sources are pairwise nonadjacent, so these reversals commute, and the result
is again acyclic.

This is a very natural deterministic self-map.  It initially looked better
than a generic DAG peel because the ground graph and every edge are retained.

### Independently derived target fibre

For a target orientation `H`, write

- `A(H)` for its nonisolated sources;
- `B(H)` for its nonisolated sinks; and
- `N_B(J)` for the union, inside `B(H)`, of the neighbours of vertices in
  `J subseteq A(H)`.

The source set of a root must be the isolates together with a set
`D subseteq B(H)` that dominates every vertex of `A(H)`.  Conversely, every
such `D` gives one root, by reversing the edges at `D` (isolates do nothing).
Thus

```text
|T^{-1}(H)|
  = #{D subseteq B(H) : N(D) contains A(H)}
  = sum_{J subseteq A(H)} (-1)^|J| 2^(|B(H) \ N_B(J)|).
```

In particular, `H` is in the one-step image exactly when every nonisolated
source of `H` has a sink neighbour.  The empty graph has one root.  For
`n=2` all three states have one root; at `n=5` the maximum fibre is `15`.
The verifier obtains the fibre independently both by literal predecessor
enumeration and by the displayed cover count/inclusion--exclusion.

### Temporal attack

The exhaustive functional graphs are not governed merely by DAG height.
At `n=5` they already have tails `0,1,2,3` and periods
`1,2,3,4,5,6`; the complete `(tail,period)` histogram is frozen in
`CANONICAL.txt`.  This destroys the hoped-for simple source-layer rotation
contract.  More decisively, Goles--Prisner (2000) study the same literal
parallel rule: repeatedly reorient all arcs starting at sources, explicitly
as a discrete dynamical system and in connection with chip firing.

The target fibre above is a generic dominating-set inclusion--exclusion on
the source--sink bipartite cut.  It cannot carry a paper after the literal
operator and dynamics are subtracted.

**Decision: `KILL_DIRECT_OWNER`.**

## 2. USC: union-square of an abstract simplicial complex

### Literal map

On a fixed labelled ground set, including complexes that ignore some ground
vertices, put

```text
T(K) = K vee K = {sigma union tau : sigma,tau in K}.
```

The void complex and `{empty}` are distinguished.  Since `K` is hereditary,
`T(K)` is again hereditary.

### Exact iterate, core, and sharp clock

Associativity gives

```text
T^t(K) = vee^(2^t) K,
```

the complex of unions of at most `2^t` old faces.  Let `supp(K)` be the union
of all faces and, for nonempty support, let

```text
chi(K) = min{k : k faces of K cover supp(K)}.
```

Then

```text
T^t(K) = 2^supp(K)  iff  2^t >= chi(K),
depth(K) = ceil(log_2 chi(K)).
```

A hereditary union-closed family is exactly a simplex on its support.
Therefore the recurrent core consists only of the void complex and the
`2^n` support simplices, all fixed.  The maximum depth is
`ceil(log_2 n)` and is attained by the zero-dimensional complex on all `n`
vertices.  This includes the exact `n=0,1` boundaries.

The exhaustive depth histograms are:

```text
n=0: 0:2
n=1: 0:3
n=2: 0:5, 1:1
n=3: 0:9, 1:10, 2:1
n=4: 0:17, 1:120, 2:31
n=5: 0:33, 1:5444, 2:2103, 3:1.
```

### Stable image and fibres

Let `M_s` be the number of complexes on an `s`-set when void is included;
for `s<=5`,

```text
(M_0,...,M_5) = (2,3,6,20,168,7581).
```

The number with full support is

```text
F_s = sum_{j=0}^s (-1)^j binom(s,j) M_(s-j),
```

giving `(F_0,...,F_5)=(2,1,2,9,114,6894)`.  Once
`t>=ceil(log_2 n)`, every target outside the fixed core has fibre zero;
each nonempty support simplex `2^S` has fibre `F_|S|`, while the void complex
and `{empty}` each have fibre one.

This is a complete stable-image theorem, but not the demanded all-time
target theorem.  At intermediate time, deciding `T^t(K)=L` for arbitrary
`L` remains a complex-root problem; only simplex targets reduce to the
cover inequality `chi(K)<=2^t`.

### Owner and collision subtraction

Aharoni--Berger (2006) explicitly define the same product
`C vee D={sigma union tau}` and its `k`-fold self-product, and define the
chromatic number of a complex as the minimum number of faces covering its
ground set.  Thus the displayed clock is the direct iteration of an owned
operation read through an owned parameter.  Internally, P97 has the same
proof silhouette: square an associative set operation, obtain a `2^t`-fold
product, and hit the closure core when a covering/generation number crosses
`2^t`.  The stable fibre is only Dedekind-number inclusion--exclusion.

**Decision: `KILL_DIRECT_INGREDIENT_AND_P97`.**

## 3. ASD: alternating simplification--duality on matroids

### Literal map and labelled convention

To make deletion rank-changing but still finite, the carrier consists of all
matroids whose ground is a subset of `[n]`.  In each nonloop parallel class,
`si(M)` retains its least-labelled member and deletes all other members and
all loops.  Define

```text
T(M) = si(M)^*.
```

### Core and clock bound

Every image is cosimple.  A state is recurrent exactly when it is both simple
and cosimple; on that core, `T` is ordinary duality, so periods divide two.
If an image is not in the core, it is cosimple but nonsimple, hence its next
update strictly decreases ground size.  Only the initial step can preserve
ground size outside the core.  Therefore

```text
depth(M) <= |E(M)| + 1.
```

The bound is safe but not a sharp all-parameter theorem.  The observed
maximum depths for ambient `n=0,...,5` are `0,2,2,3,3,4`, already showing
that ground size alone does not determine the clock.

### Exact image and every-target fibre

Let a target `N` have ground `S subseteq [n]`.  If `N` is not cosimple its
fibre is empty.  Otherwise `N^*` is simple.  A root is obtained by treating
each `e in [n]\S` independently as

1. absent;
2. a loop; or
3. parallel to one of the representatives `s in S` with `s<e`.

The inequality is forced by the least-label representative convention.
Every choice gives a unique matroid and every root arises this way.  Hence

```text
|T^{-1}(N)| = product_{e notin S} (2 + #{s in S : s<e})
```

for cosimple `N`, and zero otherwise.  This also proves that the one-step
image is exactly all cosimple matroids.  It handles `S=empty`: there are
`2^n` roots, one all-loop matroid on each subground.

### Gate failure

The fibre is clean, but its entire structure is only the familiar fact that
matroids with a fixed simplification are loop and parallel extensions of a
simple matroid.  The forward map is explicitly simplification followed by
duality; alternating parallel/series removal is standard
simplification/cosimplification and is a rank-eroding algorithmic primitive.
This is exactly the class the intake rule excludes.  P148 and the permanent
matroid-greedy/rank-erosion kills supply additional portfolio pressure.

**Decision: `KILL_STANDARD_SIMPLIFICATION_RANK_EROSION`.**

## 4. CGP: convex-geometry extreme peeling

### Literal map

Fix a finite convex geometry `(E,cl)` and let its closed sets be the states.
For closed `C`, let

```text
ex(C) = {x in C : C\{x} is closed},
T(C) = C\ex(C).
```

The update stays closed: for each removed extreme `x`, the new set is
contained in the closed set `C\{x}`, so its closure excludes every removed
point and remains inside the new set.

### Exact forward statement and failure of the inverse axis

Every nonempty closed set has an extreme point.  Thus the empty set is the
only recurrent state, the depth is the number of simultaneous extreme
layers, and

```text
depth(C) <= |C| <= n.
```

The maximum `n` is attained by chain convex geometries, where one point is
extreme at each step.  Exhaustive generation of all labelled convex
geometries confirms the counts `1,1,3,22,485` through rank four and all
`4,468` rank-four closed states.

For a target `D`, a putative root `C superseteq D` must satisfy the literal
conditions

```text
C closed;
C\{x} closed for every x in C\D;
C\{d} not closed for every d in D.
```

Across rank-four geometries the verifier already sees 28 different fibre
spectra.  No geometry-uniform target statistic or closed fibre law emerged;
the displayed condition is only a restatement of the update.

Edelman--Jamison own the convex-geometry/antimatroid framework; Ando studies
the extreme-point operator on closure spaces; repeated removal of convex-hull
extreme points is the classical convex-layer/onion-peeling process.
Internally this is the same simultaneous layer deletion silhouette as the
maximal-poset, simplicial-facet, forest-leaf, and odd-vertex pruning lanes.

**Decision: `KILL_DIRECT_PEELING_OWNER_THIN`.**

## 5. PSE sentinel: strict-square erosion of posets

For a strict poset relation `R`, the tempting map `T(R)=R^2` satisfies

```text
T^t(R)=R^(2^t),
depth(R)=ceil(log_2 h(R)),
```

where `h(R)` is the maximum number of elements in a chain; the sole fixed
state is the antichain.  The verifier reconfirms this on all `4,231` labelled
five-point posets.

This is not a round-two candidate.  The literal `R -> R intersect R^2`
(equal to `R^2` on a transitive strict relation) was already frozen as
`S03 / KILL` in the P127--P131 algebraic scout.  It is also exact Boolean
relation powering/pointer jumping, and directed-root inversion is a classical
graph-power problem.

**Decision: `PERMANENT_KILL_PRIOR_LITERAL_S03`.**

## Final gate

| candidate | natural map | all-parameter clock/core | all-time image or every-target fibre | owner-thin after subtraction | result |
|---|---|---|---|---|---|
| PFR | yes | no; direct owner already studies dynamics | one-step every-target fibre | no | kill |
| USC | yes | yes | stable only, not arbitrary-time targets | no; exact operation/parameter + P97 | kill |
| ASD | borderline canonical-label convention | upper bound/core, not sharp clock | one-step every-target fibre | no; standard simplification | kill |
| CGP | yes | tautological layer clock and sharp bound | no | no; classical peeling | kill |

There is therefore no theorem contract to freeze for P166 in this lane.
The correct outcome is **`KILL_ALL / HOLD_EXTERNAL`**.

## Reproduction

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_scout.py
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_scout.py)
cmp -s CANONICAL.txt <(PYTHONDONTWRITEBYTECODE=1 python3 verify_scout.py)
```
