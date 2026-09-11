# Fresh combinatorial replacement scout

**Route:** A.  **Stage:** Stage-1 replacement discovery.  **External status:**
`HOLD_EXTERNAL`.  **Paper allocation:** none.

This replacement pass tests five new literal finite systems after the first
combinatorial lane returned no gate-clean select.  It does not use matching,
sorting, closure, rowmotion, centroid motion, chip firing, ARC-style run
consolidation, or a cosmetic variant of those mechanisms.  Two systems survive
claim subtraction as paper-sized internal contracts:

- **ELC**, even-level contraction of rooted plane trees; and
- **PKE**, iterated standardized peak extraction on permutations.

FPD initially supplied a clean basin theorem but was killed by direct static
owners.  APL and CCS are negative controls showing that simply pointing a
plane tree does not clear the value gate.

Exact replay is
[`verify_combinatorial_replacement.py`](verify_combinatorial_replacement.py),
with byte-for-byte stdout in [`CANONICAL.txt`](CANONICAL.txt).  The final run
made **3,464,224 assertions and passed**.  The direct-owner and internal
claim subtraction is separate in [`OWNER_AUDIT.md`](OWNER_AUDIT.md).

## 1. Decision ledger

| ID | literal self-map | strongest exact signal | owner/collision after subtraction | decision |
|---|---|---|---|---|
| **ELC** | in a plane tree, erase every odd generation and promote its ordered grandchildren; reset parity and repeat | pointwise clock `ceil(log2(h+1))`; target fibre `y^I/(1-y)^(2m-1)`; algebraic image series | generic contraction, height parity, P114/P115 inputs subtracted; no direct owner found for the conjunction | **SELECT_PAPER_SIZED / PASS_FOCUSED** |
| **PKE** | take all endpoint-inclusive local-maximum values of a permutation, preserve their order, and standardize | all iterate images `P^k(S_n)=union_{m<=ceil(n/2^k)}S_m`; explicit right sections; sharp log clock; target poset fibres | pinnacle sets/orderings heavily owned and credited; no owner found for the repeated transform and iterate-image law | **SELECT_PAPER_SIZED / PASS_REPAIRED** |
| **FPD** | delete the least fixed point and standardize | clock is number of fixed points; each derangement target has binomial basin | Désarménien--Foata directly own derangement reduction; Deutsch--Elizalde meet the smallest-fixed insertion statistic; P105 collision | **KILL_DIRECT_TRANSFER** |
| **APL** | on a plane tree with a marked vertex, move the mark to its parent | exact depth clock and level-polynomial basins | generic parent map; P114 metric/tree boundary; only pointed-species bookkeeping remains | **KILL_CLASSICAL_THIN** |
| **CCS** | advance a marked plane-tree corner by one step around the contour | every component is a cycle of length `2(n-1)` and has a unique inverse | literal cyclic group action on a classical contour tour | **KILL_GROUP_ACTION** |

### Ranking

1. **ELC is the strongest replacement.**  Its inverse unexpectedly collapses
   from a degree-profile product to a two-statistic rational function.  The
   clock and inverse use different proof engines.
2. **PKE also clears the internal two-axis gate after repair.**  Its paper must
   be framed around every-iterate images and explicit sections, not around the
   already mature pinnacle-set literature.
3. **FPD is not a fallback.**  The exact signal is real, but almost every
   theorem is a serialization of the owned derangement reduction.

## 2. ELC: even-level contraction

### 2.1 Carrier and literal map

Let `PT_{<=N}` be the finite disjoint union of rooted plane trees with at most
`N` vertices.  A tree is an ordered list of its child trees.  Define `E` by

```text
E([T_11,...,T_1r1], ... , [T_d1,...,T_drd])
  = [E(T_11),...,E(T_1r1),...,E(T_d1),...,E(T_drd)].
```

In geometric language, retain the root and all even-depth vertices.  Delete
each odd-depth child; its children become consecutive children of their
grandparent, and the original plane order is preserved.  The output has no
more vertices than the input, so this is a literal self-map of `PT_{<=N}`.
The single-vertex tree is fixed.

Example, writing a node as brackets around its ordered children:

```text
[ [[[]],[]], [[],[[]]] ]  --E-->  [ [[]], [], [], [[]] ].
```

This is not leaf pruning: all odd levels disappear simultaneously, including
odd vertices far from the boundary.

### 2.2 Exact early profile and anomaly

For the exact `n`-vertex source stratum, the profile
`(states,image,max tail)` through `n=11` is

```text
(1,1,0), (1,1,1), (2,2,2), (5,3,2), (14,5,3),
(42,9,3), (132,17,3), (429,34,3), (1430,71,4),
(4862,153,4), (16796,338,4).
```

The complete tail censuses include

```text
n=8:  tau 1:1, 2:232, 3:196;
n=9:  tau 1:1, 2:609, 3:819, 4:1;
n=11: tau 1:1, 2:4180, 3:12464, 4:151.
```

The first strong anomaly was not merely logarithmic time.  For every target
tested, thousands of differently grouped source trees collapsed to a fibre
count depending only on the target's vertex count and number of internal
vertices, not its full degree sequence.

### 2.3 All-parameter clock and recurrent theorem

If `h(T)` is ordinary root height, then

```text
h(E(T))=floor(h(T)/2),
h(E^k(T))=floor(h(T)/2^k).
```

Indeed `E^k(T)` retains exactly the vertices whose original depths are
divisible by `2^k`, with nearest retained ancestors joined in contour order.
Therefore

```text
tau(T)=ceil(log2(h(T)+1)).
```

All orbits end at the singleton.  Among trees with `n` vertices,

```text
max tau = ceil(log2 n),
```

and the `n`-vertex path is an explicit witness.  This is pointwise, rather
than only an extremal estimate.

### 2.4 Every-target inverse theorem

Fix a target `U` with `m` vertices and `I=I(U)` internal vertices.  Weight
each deleted odd-level source vertex by `y`.  Then

```text
F_U(y) = sum_{E(T)=U} y^(|T|-|U|)
       = y^I / (1-y)^(2m-1).
```

Consequently the exact number of `n`-vertex predecessors is

```text
[y^(n-m)]F_U(y)
 = binom(n-m-I+2m-2, 2m-2)   if n-m>=I,
 = 0                           otherwise.
```

**Inverse construction.**  At a target vertex with ordered children
`u_1,...,u_d`, the source odd children split this list into consecutive
nonempty blocks; arbitrary empty odd leaves may be inserted in every gap.
For `d>0`, summing over the number of productive blocks gives

```text
sum_{k=1}^d binom(d-1,k-1) y^k/(1-y)^(k+1)
  = y/(1-y)^(d+1).
```

A target leaf contributes `1/(1-y)`.  Multiplying over vertices gives the
numerator `y^I` and denominator exponent
`sum_v(deg(v)+1)=2m-1`.  This proof is local and reversible.

### 2.5 Image theorem

A target appears from the exact `n`-vertex stratum precisely when

```text
|U| + I(U) <= n.
```

Let `H(z)=sum_U z^(|U|+I(U))`.  Splitting off a leaf or an internal root with
a nonempty sequence of children gives

```text
H = z + z^2 H/(1-H).
```

Thus the exact image-count sequence is generated by `H(z)/(1-z)`.  Its first
values are the verified `1,1,2,3,5,9,17,34,71,153,338`.

### 2.6 Proof route, collisions, and decision

The temporal proof is generation arithmetic; the inverse proof is an ordered
block-and-gap species decomposition; the image proof is algebraic species.
The full owner subtraction is in `OWNER_AUDIT.md`.  In short, even/odd level
statistics, generic tree contraction, and generic logarithmic decimation are
zero-credit.  P114's leaf layers and P115's coefficient chains do not supply
the target inverse.

**Exact falsifier.**  The verifier generates all `23,714` plane trees through
11 vertices.  For every source it asserts height halving and the pointwise
clock.  For every possible target and every source size through 11 it compares
the observed fibre with the displayed binomial coefficient, including zero
fibres.  A single wrong gap exponent or missing productive-child factor fails.

**Decision: `SELECT_PAPER_SIZED / PASS_FOCUSED`.**

## 3. PKE: iterated standardized peak extraction

### 3.1 Carrier and literal map

Let `S_{<=N}=disjoint_union_{m=1}^N S_m`, a finite carrier.  For
`pi=pi_1...pi_n`, put `pi_0=pi_{n+1}=0`.  Read, from left to right, all values
`pi_i` satisfying

```text
pi_(i-1) < pi_i > pi_(i+1),
```

and standardize that nonempty subsequence.  Call the resulting permutation
`P(pi)`.  For example,

```text
pi = 4 1 6 2 5 3  -> peak values 4,6,5 -> P(pi)=1 3 2.
```

For `n>1`, no two peak positions are adjacent, so `|P(pi)|<=ceil(n/2)<n`.
The one-letter permutation is the unique fixed state.  This variable-rank
formulation is essential: PKE is a self-map of `S_{<=N}`, not of one `S_n`.

### 3.2 Exact early profile and anomaly

For exact source rank `n`, `(states,image,max tail)` through `n=9` is

```text
(1,1,0), (2,1,1), (6,3,2), (24,3,2), (120,9,3),
(720,9,3), (5040,33,3), (40320,33,3), (362880,153,4).
```

The image sizes are not empirical accidents:

```text
1, 1, 1!+2!, 1!+2!, 1!+2!+3!, ... .
```

The tail censuses at the two largest tested ranks are

```text
n=8: tau 1:128, 2:28512, 3:11680;
n=9: tau 1:256, 2:219664, 3:142800, 4:160.
```

### 3.3 Every-iterate image theorem and sharp clock

For all `n>=1` and `k>=1`,

```text
P^k(S_n) = disjoint_union_{1<=m<=ceil(n/2^k)} S_m,
|P^k(S_n)| = sum_{m<=ceil(n/2^k)} m!.
```

The upper inclusion follows from peak packing.  The reverse inclusion has an
explicit section.  Given `sigma in S_m` and `n>=2m-1`:

1. use the top `m` source values in relative order `sigma`;
2. insert one of `1,...,m-1` between each adjacent pair of high values; and
3. append every remaining low value in decreasing order.

The high values are exactly the peaks, in target order; the terminal descent
creates none.  Repeated minimal odd lifts followed by the available outer
length give a right section for every `k`.  It follows that

```text
max_{pi in S_n} tau(pi)=ceil(log2 n).
```

The verifier constructs sections for every target and every feasible iterate
through source rank 8, rather than checking image cardinality alone.

### 3.4 Target-resolved one-step fibre

Fix `sigma in S_m`.  For a comparison word
`w in {up,down}^{n-1}` having exactly `m` endpoint-inclusive peaks, form the
poset `Q(w,sigma)` on positions `1,...,n`:

- each adjacent comparison of `w` is an order relation; and
- the peak positions are chained in the relative value order `sigma`.

Then

```text
|{pi in S_n : P(pi)=sigma}|
  = sum_{w: peaks(w)=m} e(Q(w,sigma)),
```

where `e(Q)` is the number of linear extensions.  Each source permutation has
a unique comparison word, and assigning ranks is exactly a linear extension,
so this is a bijective atlas, not inclusion-exclusion.

For example, maximal four-peak targets at source rank seven have fibres
ranging from 8 to 15 depending on `sigma`; the target order genuinely matters.
The verifier checks the formula for every target through `n=8`.

### 3.5 Owner subtraction and decision

Pinnacle sets, admissible pinnacle orderings, and static pinnacle enumeration
are directly owned and receive no credit.  The secondary poset formula uses
standard technology and is not the lead novelty claim.  The residual is the
literal repeated transform, all iterate images, explicit all-rank sections,
and their sharp clock.  See `OWNER_AUDIT.md` for the primary papers.

**Exact falsifier.**  All `409,113` permutations through rank nine are tested.
The script checks every source tail, every image rank, every feasible target
section through rank eight, and every target multiplicity against an
independent subset-DP linear-extension calculation.

**Decision: `SELECT_PAPER_SIZED / PASS_REPAIRED`.**

## 4. FPD: least-fixed-point deletion

### 4.1 Map and exact profile

On `S_{<=N}` including the empty permutation, if `pi_i=i`, delete the least
such position/value and reduce all larger positions and values by one.  Fix a
derangement.  For `n=0,...,9`, `(states,image,fixed,max tail)` is

```text
(1,1,1,0), (1,1,0,1), (2,2,1,2), (6,4,2,3),
(24,15,9,4), (120,68,44,5), (720,385,265,6),
(5040,2574,1854,7), (40320,19873,14833,8),
(362880,173816,133496,9).
```

### 4.2 Candidate theorem and inverse

Deleting one fixed point preserves all other singleton cycles.  Therefore

```text
tau(pi)=number of fixed points of pi,
endpoint=the standardized non-singleton-cycle restriction.
```

For every derangement target `delta in S_m`, its basin in exact source rank
`n` has size `binom(n,m)`: choose the labels supporting `delta`, transport it
in increasing order, and make every unused label a singleton cycle.  If an
arbitrary target `rho in S_(n-1)` has least fixed point `j`, its scheduled
one-step indegree from `S_n` is `j`; if it is a derangement, the indegree is
`n`.

### 4.3 Owner and kill

Désarménien--Foata explicitly define the endpoint derangement reduction by
deleting fixed points, while Deutsch--Elizalde's smallest-fixed-point identity
meets the scheduled insertion count.  The least scheduler only serializes
these static facts, and P105 already occupies cycle-component pruning.

**Decision: `KILL_DIRECT_TRANSFER`.**

## 5. APL: ancestor lift of a pointed plane tree

**Map.**  A state is `(T,v)` with a marked vertex address.  If `v` is not the
root, replace it by its parent; fix the root mark.  The underlying plane tree
never changes.

**Profile.**  For exact tree size `n=1,...,11`, the state counts are

```text
1,2,6,20,70,252,924,3432,12870,48620,184756,
```

equal to `n C_(n-1)`.  Maximum tails are `0,1,...,10`; fixed counts are the
Catalan numbers.  At `n=11`, the image contains `92,378` pointed states.

**Theorem / inverse.**  `tau(T,v)=depth(v)`, the unique endpoint is `(T,root)`,
and the basin polynomial is the level profile
`sum_{v in T}u^depth(v)`.  A path gives sharp time `n-1`.

**Collision / decision.**  The map is the defining parent relation of a
rooted tree.  The inverse merely lists children and the basin merely lists
levels; after generic pointed-species and P114 metric subtraction no advance
remains.  **`KILL_CLASSICAL_THIN`**.

## 6. CCS: contour-corner successor

**Map.**  Mark one of the `2(n-1)` corners encountered by the clockwise
contour tour of a nontrivial plane tree and advance it one corner.  Use one
null corner for the singleton tree.

**Profile.**  For `n=1,...,11`, state counts are

```text
1,2,8,30,112,420,1584,6006,22880,87516,335920.
```

Every state is recurrent.  For `n>1`, every orbit has period `2(n-1)` and the
predecessor corner is unique.

**Owner / decision.**  This is a regular cyclic action on a classical contour
tour.  Exact period and inverse are definition-level consequences; it has no
independent temporal or fibre theorem.  **`KILL_GROUP_ACTION`**.

## 7. Exact-evidence boundary

The verifier asserts literal closure of the finite carriers, exact clocks,
fixed/recurrent sets, image ranks, explicit sections, and target fibres.  Its
final lines are

```text
ASSERTIONS=3464224
STATUS=PASS
```

Enumeration is falsification pressure, not proof of the all-parameter
theorems, ownership, or novelty.  The proofs above establish the claimed
formulae independently; `OWNER_AUDIT.md` records bounded searches and explicit
claim subtraction.  No Git operation, external submission, paper-number
assignment, or external message was performed.
