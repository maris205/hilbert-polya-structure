# Proof package — P159

## Claim

For parallel deletion of all current odd-degree vertices on simple labelled
graphs carried by arbitrary subsets of `[n]`, prove the sharp stabilization
clock, the target-uniform strict inverse formula, the every-time rank-resolved
fibres, the exact images, and the fixed/depth censuses stated in Theorem 1 of
`main.tex`.

## Status

`PROVABLE AS STATED / ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Assumptions

- `n` is a nonnegative integer and the ambient labels are `[n]`.
- States are finite simple graphs on arbitrary subsets of `[n]`.
- All odd-degree vertices are evaluated in the same current graph and deleted
  simultaneously; the next state is the induced graph on survivors.
- Counts are labelled.  No quotient by graph isomorphism is taken.
- Matrix entries are integers and matrix multiplication uses target rows and
  source columns.

## Notation

- `D(G)`: current odd-degree vertex set.
- `F(G)=G[V(G)\D(G)]`: update.
- `rho(G)=|V(G)|`: rank.
- `tau(G)`: first time at an even graph.
- `S`: target vertex set, `|S|=s`.
- `D`: prospective deleted set, `|D|=d>0`.
- `m=s+d`: source rank.
- `B_n(s,m)`: number of strict rank-`m` predecessors of one fixed rank-`s`
  target.
- `C_{n,t}=I+B_n+...+B_n^t`.
- `e_s`: number of even simple graphs on one fixed `s`-set.

## Proof strategy

Separate the forward rank-loss argument from the inverse theorem.  For one
strict inverse, hold the target edges fixed and encode every free edge meeting
the deleted set as a binary variable.  Connected-incidence rank gives both
the consistency parity and the nullity.  Target-independence then licenses
literal matrix powers; deterministic first arrival separates non-even targets
from fixed even targets.  Image and census formulas follow by positivity and
target summation.

## Dependency map

1. Stabilization uses handshaking and strict vertex loss; sharpness uses paths.
2. Strict inverse consistency uses the column space of a connected binary
   incidence matrix.
3. Strict inverse cardinality uses rank–nullity and labelled choice of `D`.
4. Transfer powers use target-independence, nonwaiting strict predecessors,
   and uniqueness of forward intermediates.
5. Images use positive even reverse rank increments.
6. Censuses use the complete-graph incidence kernel and deterministic even
   endpoints.

## Proof

### Step 1. Forward loss, recurrence, and clock

The handshaking lemma gives `|D(G)|` even.  At a non-even state it is positive,
so at least two vertices disappear.  At an even state it is empty, so the
state is fixed.  Strict rank loss rules out all other periodic states and gives

```text
tau(G) <= floor(|V(G)|/2) <= floor(n/2).
```

The path `P_n` has exactly two odd vertices, its endpoints.  One update leaves
`P_(n-2)`, so the path attains the bound.  For `n=0` the only state is empty;
for `n=1` the empty graph and singleton are fixed.  Both clocks are zero.

### Step 2. Normalize one strict inverse

Fix a target `H` on `S` and a nonempty disjoint deleted set `D`.  A predecessor
must retain exactly the edges of `H` inside `S`.  There are

```text
sd + binom(d,2)
```

free edges, namely all edges with at least one endpoint in `D`.  For each
`u in S`, survival requires

```text
sum_{v in D} x_uv = deg_H(u) (mod 2).
```

For each `v in D`, deletion requires

```text
sum_{w != v} x_vw = 1 (mod 2).
```

These conditions are necessary and sufficient: they make every vertex of `S`
even in the source, every vertex of `D` odd, and preserve exactly `H` after
induced deletion.

### Step 3. Consistency and nullity

Let `Q_(S,D)` have vertex set `S union D` and precisely the free edges.  It is
connected for every `d>0`, including the one-vertex case.  Its unoriented
incidence matrix over `F_2` has rank `s+d-1`.  Indeed, a vector in its left
kernel has equal endpoint values along every edge and is therefore constant;
the left kernel has dimension one.

Every incidence column has coordinate sum zero.  Since the column space has
dimension `s+d-1`, it is exactly the even-weight subspace.  The right-side sum
is

```text
sum_{u in S} deg_H(u) + d = d (mod 2).
```

Thus the system is consistent iff `d` is even.  For positive even `d`, the
solution-space dimension is

```text
sd + binom(d,2) - (s+d-1)
 = s(d-1) + binom(d-1,2).
```

The fixed-`D` count is the corresponding power of two.  There are
`binom(n-s,d)` choices of `D`, proving the formula for `B_n(s,s+d)`.  No
target-edge quantity remains, so the count is target-uniform.

### Step 4. Strict and degenerate boundaries

Odd `d` gives no solution.  When `d=0`, the strict problem is absent.  A
same-rank source deletes no vertex, hence is even and fixed; it maps to `H`
iff it equals an even `H`.  This diagonal waiting term belongs to the full
map, not to `B_n`.

At `s=0,d=2` and fixed `D`, the variable graph is `K_2`; the odd equations
force its one edge.  Hence there is one fixed-`D` source and
`B_n(0,2)=binom(n,2)` after label choice.

### Step 5. Matrix orientation and strict chains

Put targets on rows and sources on columns.  Then

```text
(B_n^2)(s,m)=sum_k B_n(s,k) B_n(k,m).
```

For each rank-`k` strict predecessor of a fixed rank-`s` target, the second
factor counts rank-`m` strict predecessors independently of that intermediate
graph's edges.  Every deterministic forward chain has one intermediate state,
so multiplication neither identifies nor repeats chains.

A strict predecessor is non-even because its next deleted set is nonempty and
odd-degree.  It cannot wait.  Induction therefore shows that `B_n^t(s,m)`
counts `t`-step strict inverse chains.  The sentinels

```text
B_4(0,2)=6, B_4(2,0)=0, (B_4^2)(0,4)=24
```

fix the orientation and reject its transpose.

### Step 6. Every-time fibres

If the target `H` is non-even, no forward path ending at it can contain a
waiting step: waiting means an even fixed state, which cannot later leave.
Hence the time-`t` fibre is `B_n^t`.

If `H` is even, a source reaching it after exactly `j<=t` strict steps remains
there for the other epochs.  The first-arrival cases are disjoint, giving
`I+B_n+...+B_n^t`.  At `t=0`, both cases reduce to the identity matrix.

### Step 7. Image criterion

Every reverse strict step adds a positive even number of labels.  A non-even
rank-`s` target can therefore have a time-`t` predecessor only if
`n-s>=2t`.  Under that inequality, choose `t` increments of two; every
corresponding strict-transfer entry is positive, proving sufficiency.  Even
targets are in every image via self-predecessors.  At `t=0`, the identity map
has the full carrier as its image.

### Step 8. Fixed, image, and temporal counts

On a fixed `s`-set, even graphs are the kernel of the incidence map of `K_s`.
For `s>=1` its dimension is `binom(s,2)-(s-1)=binom(s-1,2)`; the `s=0`
boundary also has one graph.  This gives `e_0=e_1=1` and
`e_s=2^binom(s-1,2)` for `s>=2`.

Choosing target labels yields the fixed count.  A state satisfies
`tau(G)<=t` iff its time-`t` image is an even target, so summing the geometric
fibres over all even targets gives the CDF.  Successive CDF differences give
exact shells.  The image formula counts all even targets and adds all non-even
rank-`s` targets exactly when `n-s>=2t`.

Therefore all claims in Theorem 1 follow. ∎

## Corrections or missing assumptions

None.  The hostile pre-paper gate required explicit placement of the `d=0`,
`s=0,d=2`, `n=0,1`, and `t=0` boundaries and the matrix orientation; the
frozen manuscript includes all of them without altering the positive-even
strict formula.

## Open risks

- The direct-owner search is bounded and does not establish priority.
- The theorem package must remain conjunctive; clock or standard parity
  algebra alone is below the retained claim ceiling.
- Any extension to asynchronous, random, directed, multigraph, or unlabelled
  settings requires a new proof rather than a change of notation.
