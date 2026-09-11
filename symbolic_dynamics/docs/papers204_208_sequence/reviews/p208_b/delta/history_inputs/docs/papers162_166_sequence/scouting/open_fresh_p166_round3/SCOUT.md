# P166 replacement discovery round 3 — exact scout

**Outcome:** `KILL_ALL`  
**Lifecycle:** `HOLD_EXTERNAL`  
**Scope:** six literal systems in five carrier classes; no paper draft and no
Git action.

## 1. Protocol and exact-control boundary

The round began from literal update rules, not desired theorem statements.
For each system the verifier constructs the finite carrier, applies the rule
directly, detects its functional-graph shape or Markov kernel, and only then
checks derived formulas.  It imports no project module.

The exact ranges are:

| system | exhaustive range | interfaces checked |
|---|---:|---|
| `PLP` | all permutations through `S_8` | transitions, identity core, pointwise depth, depth CDF recurrence, sharp shell, one-step fibres |
| `UZD` | every modulus `2<=m<=80` | unit/nonunit runs, all iterates and every-time fibres through time `2m`, core and maximum depth |
| `SCQ` | all two-letter automata through four states | repeated quotient trajectories, terminal injectivity, depth and endpoint rank |
| `RHR` | all `82,500` full binary trees through eleven internal nodes | transitions, tail/period, every-target roots, sharp maximum tail |
| `RMR` | all perfect matchings through twelve labelled vertices | every marked transition, component-profile kernel, CDF/expectation, image and target fibres |
| `OST` | all `23,714` rooted plane trees through eleven vertices | transitions, depth, size bound, every feasible target-minimal fibre for `t<=3`, local recurrence and sharp sources |

The frozen verifier reports `2,515,415` assertions after the final replay.
Enumeration is a falsifier, not a proof or a novelty certificate.

## 2. `PLP`: parallel cyclic-peak pruning

### Literal map

Write a permutation as disjoint directed cycles.  In every cycle of length at
least three, simultaneously remove every entry larger than both cyclic
neighbours, reconnect the surviving entries in their old cyclic order, and
make each removed entry fixed.  In a 2-cycle remove its larger entry.  Fixed
points stay fixed.

### Exact clock and census

The identity is the unique recurrent point.  Rotate a nontrivial cycle so its
minimum is first and cut immediately after that minimum.  Successive deletion
rounds are the leaf layers of the min-Cartesian tree of the remaining linear
word.

Let `a(k,h)` count permutations of `k` labels whose min-Cartesian tree has at
most `h` levels.  Then

```text
a(0,h)=1,
a(k,0)=0                    (k>0),
a(k,h)=sum_{j=0}^{k-1} C(k-1,j) a(j,h-1)a(k-1-j,h-1).
```

If `F(n,t)` is the number of permutations absorbed by time `t`, decomposition
at the cycle containing the smallest label gives

```text
F(0,t)=1,
F(n,t)=sum_{m=1}^n C(n-1,m-1) a(m-1,t) F(n-m,t).
```

Consequently the maximum depth is `n-1`, and the depth-`n-1` shell has
`2^(n-2)` elements for `n>=2` (with the evident singleton boundaries at
`n=0,1`).  The verifier checks the full CDF, not only the maximum.

At `n=8` the exact depth counts are

```text
1, 763, 7812, 14496, 11712, 4608, 864, 64.
```

### Gate

This has a real temporal axis but fails separation.  Cyclic peaks and their
enumeration are established permutation statistics, the recurrence is the
standard Cartesian-tree split, P105 already occupies simultaneous
permutation-cycle pruning with full layers and fibres, and P149 occupies
iterated peak extraction.  No second target-resolved theorem survives those
subtractions.  Decision: **`KILL_INTERNAL_P105_P149`**.

## 3. `UZD`: unit/zero-divisor directed residue walk

### Literal map

For `m>=2`, on `Z/mZ` set

```text
T_m(x)=x-1  if gcd(x,m)=1,
T_m(x)=x+1  otherwise.
```

This is state dependent and is neither a power map nor a valuation map.

### Complete functional graph

Read the cyclic binary word indicating units.  For every `0 -> 1` boundary,
let `z` be the last nonunit, let `alpha` be the length of its backward
nonunit run, and let `beta` be the length of the forward unit run starting at
`z+1`.  The pair `(z,z+1)` is an attracting 2-cycle.  Its arms are

```text
z-j       (0<=j<alpha),
z+1+j     (0<=j<beta).
```

A point with arm coordinate `(side,j)` reaches the boundary in exactly `j`
steps and then alternates.  Explicitly, before arrival its coordinate is
`j-t`; afterwards parity determines `z` versus `z+1`.  Therefore every
time-`t` fibre is the disjoint count of arm coordinates satisfying that
formula, and

```text
maximum depth = max_boundaries(max(alpha,beta)-1).
```

The cases `m=2` and powers of two are handled: all points are recurrent when
the unit indicator alternates.

### Gate

Once the unit indicator has been exposed, every theorem above holds for an
arbitrary cyclic binary landscape oriented left on 1 and right on 0.  The
number theory supplies only the classical gaps between reduced residues (the
Jacobsthal-function neighbourhood); the inverse formula is coordinate
bookkeeping.  Decision: **`KILL_DESIGNED_BINARY_LANDSCAPE`**.

## 4. `SCQ`: synchronizing-collision quotient

### Literal map

A state is a complete deterministic two-letter automaton together with its
current partition of the original labelled states.  Generate the least
transition congruence containing every pair that collides under either
letter, quotient the automaton by it, and repeat.

### Exact temporal result

The map strictly decreases the number of quotient states unless both letters
are injective.  Hence the fixed states are precisely permutation automata and
the depth is at most `n-1`.  Equality is realized when both letters are the
map `i -> max(i-1,0)`, because exactly one new block is lost per round.

For all `65,536` two-letter maps on four states the depth distribution is

```text
depth 0:   576
depth 1: 54496
depth 2: 10032
depth 3:   432.
```

### Gate

Least congruences, quotients, and permutation automata are standard algebraic
automata constructions.  More importantly, an inverse target asks for all
automata whose generated collision congruence closes to a prescribed
partition; it did not factor by target blocks in the pilot.  Thus the only
uniform theorem is generic rank coarsening.  Decision:
**`KILL_STANDARD_QUOTIENT_NO_INVERSE_AXIS`**.

## 5. `RHR`: root-heavy rotations

### Literal map

For a plane full binary tree `(L,R)`, write `|L|,|R|` for internal-node
counts.  If `|L|>|R|+1`, make the right rotation

```text
((A,B),R) -> (A,(B,R)).
```

If `|R|>|L|+1`, use the mirror left rotation; otherwise fix the tree.

### Functional graph and exact inverse

Every orbit has period one or two.  Induction down the exposed heavy spine
shows that its preperiod is at most `floor((n-1)/2)`, and alternating comb
witnesses attain the bound.

A target `(L,R)` has at most three predecessors:

1. itself, exactly when `abs(|L|-|R|)<=1`;
2. `((L,B),C)` when `R=(B,C)` and that candidate is left-heavy enough to
   rotate to the target;
3. `(A,(B,R))` when `L=(A,B)` and that candidate is right-heavy enough to
   rotate to the target.

These candidates are mutually distinct and exhaustive because a source move
is one root rotation.  At eleven internal nodes the maximum fibre is three,
the maximum tail five and the maximum period two.

### Gate

The move is a Tamari cover and the heavy-child condition is a standard
weight-balancing motif.  Internally, P144 already claims a deterministic
Tamari/comb scheduler together with a sharp clock and target-local inverse
description.  The different scheduler does not create a portfolio-separated
paper.  Decision: **`KILL_INTERNAL_P144_ROTATION`**.

## 6. `RMR`: stochastic reference-matching repair

### Literal kernel

Fix the reference perfect matching
`R={{0,1},{2,3},...,{2m-2,2m-1}}`.  From a perfect matching `M`, choose one
reference edge `{a,b}` uniformly.  If it is in `M`, hold.  Otherwise, if
`M` contains `{a,x}` and `{b,y}`, replace these two edges by `{a,b}` and
`{x,y}`.

The union `R union M` is a collection of alternating even cycles.  Let
`lambda` be the partition of `m` formed by their half-lengths and let `m_1`
be its number of singleton parts.  Marking an edge in a part `k>=2` changes

```text
k -> 1 + (k-1),
```

whereas a singleton mark holds.  Thus exactly `m-length(lambda)` accepted
repairs remain, with sharp maximum `m-1`.  The deepest shell has

```text
2^(m-1)(m-1)!
```

matchings.

### All-time and every-target axes

Let `Surj(t,r)=sum_{j=0}^r (-1)^j C(r,j)(r-j)^t`.  For
`lambda=(k_1,...,k_s)`, absorption by time `t` means that at least `k_i-1`
labels from each original component have been selected.  Therefore

```text
P_lambda(tau<=t)
 = m^(-t) sum_{r_i in {k_i-1,k_i}}
     (product_i C(k_i,r_i)) Surj(t,sum_i r_i).
```

The exact expectation recursion is

```text
E(1^m)=0,
E(lambda)=
  [m + sum_{k>=2} k m_k E(lambda with k replaced by 1,k-1)]/(m-m_1).
```

For the one-component start, `E((m))=m sum_{k=2}^m 1/k`, and this is the
largest expectation among profiles.

For a target matching `N`, let `f=|N intersect R|`.  Then

```text
N is in the one-step image iff f>0,
# distinct one-step sources = 0                         if f=0,
                              1+f(2m-f-1)              if f>0,
# marked source/edge histories = f(2m-1).
```

The overlap correction in the distinct-source formula is essential: breaking
two fixed reference edges can give the same source with either edge marked.
The image size is

```text
sum_{j=1}^m (-1)^(j+1) C(m,j) (2(m-j)-1)!!.
```

All formulas include `m=1` and `t=0`.

### Gate

Contract every reference edge.  An alternating component becomes a signed
cycle, and an accepted repair removes the selected element from that cycle
and makes it a singleton.  Conditional on acceptance this is exactly `S06`
cycle erosion from the P147--P151 stochastic kill ledger; choosing from all
reference edges merely inserts null scans.  Perfect-matching flip and switch
literature also owns the ambient 4-cycle surgery.  Decision:
**`KILL_INTERNAL_S06_CYCLE_EROSION`**.

## 7. `OST`: odd-subtree contraction — priority hostile gate

### Literal map

Let `T` be a rooted plane tree.  Compute every current fringe-subtree size.
Simultaneously contract each nonroot vertex whose fringe size is odd;
surviving descendants attach to the nearest surviving ancestor, retaining
plane order.  The root is never contracted.  Denote the map by `O` on the
finite carrier `PT_{<=N}`.

### All-time size law and sharp clock

Every nonroot vertex that survives one round requires a disjoint block of at
least two vertices in its source.  Iterating the block argument gives

```text
O^t(T)=U, |U|=m  =>  |T| >= 1+2^t(m-1).                 (OST.1)
```

The inverse construction below is positive for every target, so equality is
attainable for every `U`.  Consequently the root is the unique recurrent
state and

```text
max_{|T|<=N} depth(T)=ceil(log2 N),
```

with the `N=1` value zero.  The smallest carrier size admitting depth `h` is
`1+2^(h-1)`.

### Target-resolved minimal fibres

Put

```text
c_0=1,
c_t=product_{j=1}^t (2^j-1)^(2^(t-j)),
D_t=2^(t+1)-2.
```

For a nonroot target vertex of outdegree `d`, let `f_t(d)` count its local
minimal inverse gadgets.  Direct separation at the child block containing
the first surviving branch gives

```text
f_0(d)=1,
f_t(d)=sum_{k=0}^d (d-k+1) f_{t-1}(d-k+1) f_{t-1}(k).
```

Thus, with `F_t(z)=sum_{d>=0} f_t(d)z^d`,

```text
F_t=F_{t-1} F'_{t-1}
   =c_t/(1-z)^(2^(t+1)-1),
f_t(d)=c_t C(d+D_t,D_t).
```

The exact number of size-minimal sources of an arbitrary target `U` is

```text
E_t(U)=c_t^(m-1)
       product_{v != root} C(deg_U(v)+D_t,D_t).          (OST.2)
```

It is positive, completing the sharpness/surjectivity assertion in (OST.1).
Summing (OST.2) over all `m`-vertex plane targets and applying Lagrange
inversion gives, for `m>=2`,

```text
sum_{|U|=m} E_t(U)
 = c_t^(m-1)/(m-1) C(2^(t+1)(m-1),m-2),                (OST.3)
```

with value one at `m=1`.  Finally, among trees at the smallest size
`1+2^(h-1)` having depth `h`, the exact count is `c_(h-1)`.  The first four
values are `1,1,3,63`.

The verifier checks the local recurrence through `t=5,d=20`, every feasible
instance of (OST.2)--(OST.3) through eleven source vertices for `t<=3`, and
all depth shells through eleven vertices.  This is the strongest mathematical
signal in the round.

### Hostile internal gate

No bounded primary search located the literal fringe-parity selector or
(OST.2).  That non-hit gives no credit.  P148 is nevertheless decisive:

| interface | P148 | `OST` |
|---|---|---|
| finite carrier | `PT_{<=N}` | `PT_{<=N}` |
| move | contract selected vertices and promote ordered children | same |
| selector | odd current depth | odd current fringe size |
| recurrent core | singleton | singleton |
| sharp extremal clock | `ceil(log2 N)` | `ceil(log2 N)` |
| scored inverse engine | product of local target-degree factors | product of local target-degree factors |
| global extraction | plane-tree generating functions | Lagrange extraction over plane trees |

The selector and exact factors differ, so this is not literal identity.  But
the present gate explicitly forbids a P1--P165 proof-silhouette collision.
P148's accepted residual is already ordered contraction plus target-resolved
inverse/image algebra after its direct outward-contraction owner is
subtracted.  `OST` cannot score that same conjunction again.  Decision:
**`KILL_INTERNAL_P148_SILHOUETTE`**.

## 8. Final decision

All six literal systems are mathematically consistent on the tested ranges.
`RMR` and `OST` each possess more than two formal theorem axes, but both fail
the permanent internal gate.  The other four fail earlier owner/value gates.
The round therefore freezes **`KILL_ALL / HOLD_EXTERNAL`**, without a P166
contract.
