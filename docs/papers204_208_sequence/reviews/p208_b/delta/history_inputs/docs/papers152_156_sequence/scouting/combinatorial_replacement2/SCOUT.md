# Combinatorial/geometric replacement-2 breadth scout

**Audit date:** 2026-09-02 UTC.  **External status:** `HOLD_EXTERNAL`.
**Paper status:** no number, no manuscript, no frozen theorem contract, and no
novelty/priority/release claim.  Exact enumeration is counterexample pressure,
not proof.

## Outcome

Ten genuinely different literal systems were tested after the WEX clock gate
failed.  The result is deliberately strict:

```text
paper-sized unconditional survivors = 0
CME = exact image/right-section and every-target fibre axes proved;
      proposed sharp iterated clock remains one explicit proof gate
second survivor = none
```

`CME` is the only theorem-rich candidate.  Its one-step geometry is unusually
clean: the minimum source rank of a target `sigma in S_m` is

```text
mu(sigma)=2m-rlmin(sigma),
```

and every fibre is an exact weighted sum over ordered cycle supports.  The
functional graph through rank ten has the power-of-two silhouette
`0,1,2,2,3,3,3,3,4,4`, with reverse-permutation witnesses at ranks
`1,2,3,5,9,17`.  What is *not* proved is the all-parameter optimization

```text
min{mu(sigma): tau(sigma)=t}=2^t+1.                       (CME-GATE)
```

Consequently this scout freezes only the deductive image/fibre results and
labels the iterated clock `UNFALSIFIED_PROOF_GATE`.  It does not promote CME by
finite pattern recognition.  `PMT` is the honest runner-up, but related
multiplicity/inventory dynamics and the occupied partition firewall subtract
its main mechanism; its observed clock also lacks a closed all-depth solution.

The deterministic replay covers 4,037,913 CME permutation states, ten systems,
and more than twelve million exact assertions.  Its stdout is frozen in
`CANONICAL.txt`.

| rank | ID | literal update | strongest exact signal | verdict |
|---:|---|---|---|---|
| 1 | `CME` | cycles ordered by minima; take their maxima and standardize | `mu=2m-rlmin`; all-target support fibres; power-clock silhouette | **`RESERVE_CLOCK_PROOF_GATE`** |
| 2 | `PMT` | replace an integer partition by the sorted multiplicities of its distinct parts | weighted-rank image threshold and monomial-symmetric fibre GF | `KILL_RELATED_OWNER/PARTITION_FIREWALL` |
| 3 | `FOT` | iterate Foata's first fundamental transformation | bijective periods already reach 23,435 at rank eight | `KILL_DIRECT_MAP/FIBRE_ONE` |
| 4 | `LGT` | replace a graph by its line graph | paths shrink linearly, cycles fix, prolific graphs grow | `KILL_DIRECT_ITERATION_OWNER` |
| 5 | `POD` | take order dual and reverse the natural labels | exact involution on naturally labelled posets | `KILL_ONE_STEP_SYMMETRY` |
| 6 | `HBL` | replace a clutter by its minimal-transversal blocker | exact involution and self-blocking census | `KILL_DIRECT_OWNER` |
| 7 | `SYT` | transpose a standard Young tableau | exact fixed-point-free involution beyond rank one | `KILL_CLASSICAL_ONE_STEP` |
| 8 | `SPR` | reverse ground-set labels in a set partition | exact involution and fixed census through Bell rank nine | `KILL_GROUP_ACTION_THIN` |
| 9 | `NBR` | reflect a binary necklace, modulo rotation | exact dihedral involution and Burnside-type fixed census | `KILL_GROUP_ACTION_THIN` |
| 10 | `SOC` | take orthogonal complement of an `F_2` subspace | exact dimension-reversing involution | `KILL_LINEAR_ALGEBRA_THIN` |

## 1. CME — cycle-maximum extraction

### Literal finite self-map

For `pi in S_n`, forget the cyclic order inside each cycle only after taking
its support.  Write the supports

```text
B_1,...,B_m,       min B_1 < ... < min B_m,
```

and define

```text
C(pi)=std(max B_1,...,max B_m) in S_m.                    (1)
```

The carrier is `S_{<=N}=disjoint_union_{1<=n<=N} S_n`.  The map is not a
cycle-minimum deletion, not Foata's parenthesis-erasing bijection, and not a
local subsequence selector.  The only same-rank fixed point is `id_n`, because
rank is preserved only when every cycle is a singleton.

### Exact early functional graph

Full literal enumeration gives

```text
rank n       1  2  3  4  5  6  7  8  9   10
max tail     0  1  2  2  3  3  3  3  4    4
image size   1  2  4  8 17 39 96 253 706 2074
fixed        1  1  1  1  1  1  1   1   1    1
```

The complete tail censuses, including the three depth-four states at rank nine
and 129 at rank ten, are in `CANONICAL.txt`.  This is a clear anomaly rather
than a smooth generic rank drop.

### Theorem axis A — exact all-rank image and target right section

Let `rlmin(sigma)` be the number of right-to-left minima of
`sigma=sigma_1...sigma_m`.  Then the exact image threshold is

```text
sigma in C(S_n)  iff  n >= mu(sigma),
mu(sigma)=2m-rlmin(sigma).                                (2)
```

Here is a proof independent of enumeration.  In any source, call a cycle
support a singleton when its minimum and maximum use the same ground-set
coordinate.  If support `B_i` is a singleton, then for every `j>i`,

```text
max B_j >= min B_j > min B_i=max B_i.
```

Thus `sigma_i` is a right-to-left minimum.  At most `rlmin(sigma)` supports can
be singletons; every other support needs distinct opener and closer endpoints.
This proves `n>=2m-rlmin(sigma)`.

Conversely make exactly the right-to-left-minimum supports singletons.  Take
two chains of formal endpoints

```text
O_1<...<O_m,            C_1<...<C_m,
```

pair `O_i` with `C_{sigma_i}`, and impose `O_i<C_{sigma_i}` for a nonsingleton
support.  Identify `O_i=C_{sigma_i}` precisely at the right-to-left minima.
These identifications are compatible: if `sigma_i=v` is a right-to-left
minimum, all smaller closer ranks have their paired openers before `i`, while
the identified pairs themselves occur in the same order in both chains.
Hence the quotient precedence relation is acyclic and has a linear extension.
Reading it produces an `O/C/S` endpoint schedule of length
`2m-rlmin(sigma)`, and pairing the endpoints gives the required supports.
Choosing any cyclic order on each support realizes an actual permutation.

Equivalently, the endpoint dynamic program has states `(i,j)`, the numbers of
openers and closers already read.  It permits `O`, permits `C` when the paired
opener is open, and permits `S` when the next opener is paired to the next
closer.  The proof above shows its optimum is exactly (2), not merely an
algorithmic characterization.  Replacing an `S` by separate `O,C` endpoints
and then inserting interior points realizes every larger source rank.  This
also supplies a constructive target right section at every `n>=mu(sigma)`.

The verifier independently compares the literal image with (2) in 145,684
target/source boxes and compares the endpoint DP with the closed form for every
target through rank eight.

### Theorem axis B — every-target fibres

Fix `sigma in S_m` and source rank `n`.  Let `P_n(sigma)` be the ordered set
partitions

```text
(B_1,...,B_m) of [n]
with min B_1<...<min B_m and std(max B_1,...,max B_m)=sigma.
```

For fixed supports, a cycle on `B_i` has exactly `(|B_i|-1)!` cyclic orders.
Therefore

```text
|C_n^{-1}(sigma)| =
  sum_{(B_1,...,B_m) in P_n(sigma)} prod_i (|B_i|-1)!.     (3)
```

This is a target-resolved fibre theorem, including zero fibres.  It can also
be read as a sum over endpoint words `O,C,S,I`: an interior event `I` is
allocated to an open support, and the final allocation receives the same
factorial weight.  Formula (3) is not a crossing/nesting `q`-product; all
static opener/closer and cycle-maxima theory is subtracted.

The replay builds supports from restricted-growth words, weights them by (3),
and compares the complete fibre dictionaries with literal permutations through
source rank eight: 53,218 target checks and 5,295 support terms, with total
weight `n!` in every rank.

### Iteration axis — exact conjecture and exact gap

Put `tau(pi)=min{t:C^t(pi)=id}`.  Direct sum is respected pointwise:

```text
C(alpha direct-sum beta)=C(alpha) direct-sum C(beta),
tau(alpha direct-sum beta)=max(tau(alpha),tau(beta)).       (4)
```

For `r_m=m,m-1,...,1`, the involution

```text
(1,2m-1)(2,2m-2)...(m)
```

maps under `C` to `r_m`.  Hence reverse permutations at ranks
`1,2,3,5,9,17,...` have tails `0,1,2,3,4,5,...`.  Because
`rlmin(r_m)=1`, their minimum source rank is `mu(r_m)=2m-1`.

The desired sharp clock is

```text
min{mu(sigma):tau(sigma)=t}=2^t+1,                        (5)
max_{pi in S_n} tau(pi)=max{t:2^(t-1)+1<=n}.              (6)
```

The reverse chain proves the upper/witness direction of (5).  Formula (2)
reduces the missing lower direction to the concrete optimization

```text
tau(sigma)=t  =>  2|sigma|-rlmin(sigma)>=2^t+1.           (7)
```

This is the sole clock gate.  It survived all permutations through rank ten,
and the minimum values by tail are `1,3,5,9,17` for tails `0,...,4` when tail
zero is read at the singleton base.  No induction proving (7) has been found.
Several attractive pointwise recurrences are false; in particular one cannot
replace the global optimization by a claim that every state doubles the
minimum-source resource of its literal image.  Enumeration is not a repair.

**Clock verdict:** `UNFALSIFIED_PROOF_GATE`, not theorem.  **Deductive frozen
residual:** (2), constructive sections, and (3).  **Candidate verdict:**
`RESERVE_CLOCK_PROOF_GATE`; do not assign a paper number on this audit alone.

### Portfolio and owner firewall

- **P105:** its map preserves `[n]` and surgically fixes the current minimum of
  every cycle, with clock `largest cycle length - 1`.  CME discards cyclic
  order after reading support endpoints, changes rank to the number of cycles,
  and uses an opener/closer precedence proof.  P105's pruning normal form and
  arrow-surgery fibres do not prove (2) or (3).
- **P149:** both carriers contain variable-rank permutations and standardize an
  extracted word; that carrier-level fact receives zero credit.  P149 selects
  endpoint-inclusive local peaks, has a uniform alternating-slot threshold,
  and uses comparison-poset fibres.  CME selects one support maximum per
  disjoint cycle, has the target-dependent threshold `2m-rlmin`, and uses
  ordered-set-partition factorial fibres.
- **External static owners:** ordered cycles by increasing minima, cycle maxima,
  set-partition opener/closer configurations, and fixed-minimum/fixed-maximum
  crossing-nesting enumerations all receive zero contribution credit.  The
  bounded exact-map searches in `OWNER_SEARCH_LOG.md` did not retrieve (1)
  under iteration, (2), or (3).  A non-hit is not novelty evidence.

## 2. PMT — partition-multiplicity transform

For an integer partition `lambda`, let

```text
M(lambda)=sort_desc(multiplicities of its distinct part values).             (8)
```

The only fixed point is `(1)`.  Exact maximum tails for source sizes
`1,...,14` are

```text
0,2,3,4,4,4,5,5,5,5,5,5,5,6,
```

and the first source sizes exhibiting tails `0,...,6` are

```text
1,2,2,3,4,7,14.
```

There is a clean one-step inverse theorem.  For a target
`mu=(mu_1>=...>=mu_k)`, rearrangement gives

```text
rho(mu)=sum_{i=1}^k i mu_i,                               (9)
mu in M(Partitions(n)) iff n>=rho(mu).
```

A minimum section uses part value `i` with multiplicity `mu_i`.  The exact
fibre generating function is the principal specialization of the monomial
symmetric function

```text
sum_n |M_n^{-1}(mu)| z^n = m_mu(z,z^2,z^3,...).           (10)
```

The verifier checks (9)--(10) target by target.  Nevertheless Eliahou and
Erickson directly study mutually describing multisets and a related integer-
partition dynamical system built from multiplicities.  Static multiplicity
partitions are standard, and the portfolio permanently excludes another
partition transform whose main advance is an inverse repartition formula.
After those subtractions the irregular all-depth minimum sequence above is not
a closed temporal theorem.

**Verdict:** `KILL_RELATED_OWNER/PARTITION_FIREWALL`; it is not a backup slot.

## 3. FOT — iterated Foata transformation

Rotate every cycle so its maximum is first, order cycles by these maxima, and
erase parentheses.  This is Foata's classical first fundamental
transformation, now merely iterated.  It is a bijection, so every fibre is one.
Maximum observed periods at ranks one through eight are

```text
1,1,3,7,25,216,963,23435.
```

The huge, irregular period jump is an anomaly but not a tractable sharp clock;
the literal map is directly owned and the second axis is the tautological
inverse of a bijection.  `KILL_DIRECT_MAP/FIBRE_ONE`.

## 4. LGT — iterated line graph

Vertices of `L(G)` are edges of `G`, adjacent when the original edges meet;
unlabelled states are canonically relabelled.  Exact controls give path tail
`tau(P_n)=n` to the empty graph, fixed cycles `L(C_n)=C_n`,
`L(K_{1,3})=K_3`, and `L(K_4)` with six vertices and twelve edges.  The
coexistence of extinction, fixed points, and prolific growth is classical:
van Rooij and Wilf introduced the iterated interchange/line-graph
classification.  `KILL_DIRECT_ITERATION_OWNER`.

## 5. POD — order dual with natural-label reversal

For a naturally labelled poset on `[n]`, reverse every order relation and then
send label `i` to `n+1-i`.  This is an involution.  The state counts through
rank six are `1,2,7,40,357,4824`; fixed counts are
`1,2,3,12,25,172`.  Fibre one and period at most two leave no independent
axis beyond definitional poset duality.  `KILL_ONE_STEP_SYMMETRY`.

## 6. HBL — clutter blocker

For a nonempty clutter, take the clutter of inclusion-minimal hitting sets.
Exact clutter counts on ground-set sizes one through four are
`1,4,18,166`, with `1,2,4,12` self-blocking states.  Blocker duality is an
involution on clutters; Edmonds--Fulkerson and the subsequent blocker
literature directly own this theorem.  `KILL_DIRECT_OWNER`.

## 7. SYT — tableau transpose

Transpose the cells and entries of a standard Young tableau, allowing the
shape to conjugate.  The disjoint union over all shapes has
`1,2,4,10,26,76,232,764,2620` states through rank nine.  Transpose is an
involution, with no fixed tableau beyond the one-cell state.  This is classical
shape conjugation with fibre one, not a dynamical package.
`KILL_CLASSICAL_ONE_STEP`.

## 8. SPR — set-partition reversal

Send every ground label `i` to `n+1-i` and reorder blocks by their new minima.
This involution has fixed counts
`1,2,3,7,12,31,59,164,339` through Bell rank nine.  The complete theorem is a
two-element group action and its Burnside fixed census.  It supplies neither an
absorbing clock nor a nontrivial inverse axis.  `KILL_GROUP_ACTION_THIN`.

## 9. NBR — binary-necklace reflection

Reflect a binary word and take its least cyclic rotation.  Through length
sixteen the state counts end at 4,116 and the reflection-fixed counts end at
384; every orbit has period one or two and every fibre is one.  This is the
standard dihedral action on necklaces, so all Burnside enumeration is owned
group-action material.  `KILL_GROUP_ACTION_THIN`.

## 10. SOC — binary subspace orthogonal complement

For `U<=F_2^d`, set `U -> U^perp` under the standard dot product.  Exact
subspace counts for `d=1,...,5` are `2,5,16,67,374`; self-dual counts are
`0,1,0,3,0`.  Dimension reverses and the map is an involution with fibre one.
This is elementary nondegenerate-bilinear-form duality and falls below the
one-step theorem-size gate.  `KILL_LINEAR_ALGEBRA_THIN`.

## Final kill ledger

| ID | direct-owner subtraction | internal collision | residual after subtraction | final |
|---|---|---|---|---|
| CME | static cycle maxima; ordered minima; opener/closer configurations | P105 cycles, P149 rank-changing standardized extraction | exact target image and fibres; clock open | `RESERVE_CLOCK_PROOF_GATE` |
| PMT | multiplicity/inventory multiset and partition dynamics | permanent partition-transform firewall | one-step image/fibre only | `KILL` |
| FOT | literal Foata transformation | none needed | irregular periods, fibre one | `KILL` |
| LGT | literal iterated line graphs | generic graph-functor firewall | classical classification | `KILL` |
| POD | order duality | relation-duality ceiling | involution only | `KILL` |
| HBL | clutter blocker involution | closure/duality ceiling | involution only | `KILL` |
| SYT | tableau/shape conjugation | generic tableau-formula ceiling | involution only | `KILL` |
| SPR | relabelling action | none | involution only | `KILL` |
| NBR | dihedral necklace action | free-monoid/group-action ceiling | involution only | `KILL` |
| SOC | orthogonal-complement duality | subspace-operation ceiling | involution only | `KILL` |

There is no second survivor and no paper number assigned from this lane.
