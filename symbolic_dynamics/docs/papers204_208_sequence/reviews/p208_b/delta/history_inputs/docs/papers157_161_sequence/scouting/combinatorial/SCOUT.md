# Stage-1 combinatorial / permutation / word / tree breadth scout

**Portfolio boundary:** P1--P156  
**Systems tested:** 18 genuinely different literal finite dynamics  
**External state:** `HOLD_EXTERNAL`  
**Numbering state:** no paper number assigned

## Outcome

Two systems merit a focused theorem-and-owner gate:

1. **`LCP`**, parallel deletion of the whole leftmost-child subtree at every
   plane-tree vertex, has an exact pointwise sibling-bottleneck clock and a
   target-resolved all-time inverse OGF.  It is the strongest candidate.
2. **`PAE`**, parity-agreement extraction on permutations, has even strict
   rank loss, a sharp half-rank clock with an explicit inverse tower, and a
   nontrivial target threshold/fibre problem governed by two coupled binary
   embeddings.  It survives only behind a severe P156/parity-selector
   collision gate.

The next apparent signal, `CCQ`, was killed during owner search: its central
operation is Kreweras's classical noncrossing closure in block-index form.
The remaining 15 systems were killed for a direct owner, a portfolio collision,
or a theorem package that collapsed to an idempotence/deterministic-rank fact.
This is deliberately a breadth result: no weak system was prolonged merely to
fill a slot.

The companion verifier exhausts the declared small carriers, checks literal
closure and the displayed formulas, and freezes 3,703,298 assertions in
[`CANONICAL.txt`](CANONICAL.txt).  Enumeration is counterexample pressure only;
it is not a proof or novelty evidence.

## Ranked ledger

| rank | handle | carrier and literal update | first exact signal | verdict |
|---:|---|---|---|---|
| 1 | `LCP` | plane trees; recursively discard each vertex's first child subtree | exact iterate, sibling-bottleneck clock, every-target inverse OGF | **`SELECT_FOCUSED`** |
| 2 | `PAE` | permutations; retain `pi_i` iff `i=pi_i mod 2`, then standardize | even loss, sharp `floor(n/2)` clock, coupled-parity target threshold | **`SELECT_PROOF_AND_COLLISION_GATE`** |
| 3 | `CCQ` | set partitions; take crossing-graph component RGF | two-step collapse and minimum source `2m-s_1` | **`KILL_DIRECT_OWNER`** |
| 4 | `ILP` | permutations; peel degree `0/1` vertices of the inversion graph | nontrivial shell depths and fixed counts | **`KILL_GENERIC_2_CORE`** |
| 5 | `DFC` | endofunctions; delete all indegree-zero vertices | cyclic core and exact tree-height clock | **`KILL_FUNCTIONAL_CORE_P114`** |
| 6 | `BGS` | integer partitions; deterministic Bulgarian-solitaire move | rich transients and periods | **`KILL_CLASSICAL_OWNER`** |
| 7 | `PPS` | permutations; reverse every maximal descending run | apparent sharp `n-1` pass bound | **`KILL_POP_STACK_OWNER`** |
| 8 | `TSW` | permutations; reverse prefix of length equal to first entry | extremal steps `0,1,2,4,7,10,16,22,30` | **`KILL_NAMED_OWNER_OPEN_EXTREMAL`** |
| 9 | `CBB` | cyclic binary words; cyclic nearest-empty box--ball matching | bijective periodic dynamics with erratic maximum periods | **`KILL_BOX_BALL_OWNER`** |
| 10 | `CSR` | positive compositions; subtract the minimum and delete zeros | clock equals number of distinct parts | **`KILL_EUCLIDEAN_THEOREM_THIN`** |
| 11 | `SSE` | set partitions; erase singleton blocks | one-step closure and explicit fixed locus | **`KILL_IDEMPOTENT_SELECTOR`** |
| 12 | `CPE` | permutations; retain odd cycles and standardize restriction | one-step closure; odd-cycle fixed class | **`KILL_CYCLE_SELECTOR`** |
| 13 | `TUS` | plane trees; suppress every nonroot unary vertex | one-step homeomorphic reduction | **`KILL_TREE_CONTRACTION`** |
| 14 | `ASD` | binary words; delete second copy of shortest-leftmost square | terminal words have length at most three | **`KILL_WORD_REWRITE_THIN`** |
| 15 | `GQT` | simple graphs; quotient equal open-neighborhood classes | one-step point-determining quotient | **`KILL_DIRECT_TWIN_QUOTIENT`** |
| 16 | `TSK` | tournaments; strip the unique sink | exact forced-suffix tail distribution is elementary | **`KILL_TOURNAMENT_COLLISION`** |
| 17 | `PFD` | parking functions; delete first `1`, decrement larger entries | every orbit has deterministic rank clock | **`KILL_SCHEDULE_ONLY`** |
| 18 | `WBS` | binary words; swap the leftmost `10` to `01` | clock is inversion number | **`KILL_COMPARATOR_RULE184`** |

## Detailed system records

### `LCP` -- whole-leftmost-child subtree pruning

- **Carrier.** The disjoint union of rooted plane trees with at most `N`
  vertices.  Recursively write a tree as `T=(T_1,...,T_k)`; the empty tuple is
  the one-vertex tree.
- **Update.** `L(T)=()` when `k=0`, and
  `L(T)=(L(T_2),...,L(T_k))` otherwise.  Thus the whole first-child subtree is
  discarded at every surviving vertex in parallel; this is not leaf peeling.
- **Small exact signature.** State counts for sizes `1..10` are
  `1,1,2,5,14,42,132,429,1430,4862`; distinct one-step image counts are
  `1,1,2,3,5,9,17,34,71,153`; maximum tails are
  `0,1,2,3,4,5,6,7,8,9`.  The verifier checks the iterate and clock formulas on
  every such tree and checks every target through size four, times `1..3`,
  against every source through size nine.
- **Candidate sharp temporal theorem.** If the child indices along the
  root-to-`v` path are `j_1,...,j_d`, let
  `b_T(v)=min(j_1,...,j_d)`.  Then
  `tau(T)=max_{v != root} b_T(v)`, and the size-`n` maximum is exactly `n-1`.
  More strongly, `L^t(T_1,...,T_k)` is
  `(L^t(T_{t+1}),...,L^t(T_k))`.
- **Independent second theorem axis.** For every target tree `U` and every
  time `t`, the complete preimage OGF factors recursively.  This also gives the
  exact minimum source size `|U|+t i(U)`, where `i(U)` is the number of internal
  vertices, and coefficient-level fibres at every larger size.
- **P1--P156 collision.** P114 peels exposed nonroot leaves from labelled
  rooted forests and uses height/Cayley machinery.  P148 deletes odd levels and
  promotes ordered grandchild blocks.  Neither uses sibling indices or deletes
  a whole first-child subtree.  Hackl--Heuberger--Kropf--Prodinger directly own
  adjacent leftmost-leaf/path pruning and inverse-expansion language, so all
  generic tree-pruning credit is subtracted; see `OWNER_SEARCH_LOG.md`.
- **Verdict.** **`SELECT_FOCUSED`**.  Freeze nothing yet; first prove the full
  coefficient statement and run a deeper old-path citation search.

### `PAE` -- parity-agreement extraction

- **Carrier.** `S_0 disjoint-union ... disjoint-union S_N`, including the empty
  permutation.
- **Update.** For `pi in S_n`, retain the entries `pi_i` satisfying
  `i congruent pi_i (mod 2)` in their old order and standardize the resulting
  word.
- **Small exact signature.** Maximum tails for ranks `0..8` are
  `0,0,1,1,2,2,3,3,4`.  Fixed counts are
  `1,1,1,2,4,12,36,144,576`, equal to
  `ceil(n/2)! floor(n/2)!`.  At target rank eight, the exact minimum-rank excess
  distribution is `{0:576, 2:39012, 4:732}`: this is the first rank at which
  the naive claim "every nonfixed target occurs two ranks above" fails.  For
  example, `21354687` first occurs at source rank 12.  The explicit orbit
  `24163857 -> 315264 -> 2413 -> 21 -> empty` has tail four.  A recursive sharp
  tower is checked through even rank 60, together with its odd-rank lift.
- **Candidate sharp temporal theorem.** Every rank loss is even; a nonfixed
  step loses at least two entries.  The fixed points are precisely the
  odd-starting parity-alternating permutations.  Hence
  `tau(pi)<=floor(n/2)`, with equality attainable for every `n` by the explicit
  tower in the theorem contract below.
- **Independent second theorem axis.** Target feasibility is exactly the
  simultaneous embedding of a balanced position-colour word and the
  target-permuted value-colour word into the alternating parity word.  It gives
  an exact minimum source rank and, independently, a factorially weighted
  every-target fibre formula over retained position and value subsets.
- **P1--P156 collision.** This is dangerously close to P156: both select a
  permutation subword by an absolute position/value predicate and standardize.
  P149 supplies the same zero-credit carrier pattern, and the earlier binary
  parity sieve supplies a parity-erasure neighbour.  The residual is the
  balanced two-word embedding obstruction, even loss, nonidentity fixed locus,
  and the rank-eight `+4` anomaly.  Those objects do not occur in P156's
  maximum-drop/Ferrers/Fibonacci theorem, but the permanent parity-selector
  firewall may still control.
- **Verdict.** **`SELECT_PROOF_AND_COLLISION_GATE`**.  Promote only if the exact
  threshold is proved without importing P156's main conjunction and the
  historical firewall is cleared explicitly.

### `CCQ` -- crossing-component quotient

- **Carrier.** Set partitions of `[n]`, `0<=n<=N`, represented by restricted
  growth words.  The blocks, ordered by their least elements, form the vertex
  set of a crossing graph.
- **Update.** Join two block-vertices when the corresponding blocks cross; the
  output is the restricted-growth word of the connected-component partition of
  those ordered block indices.
- **Small exact signature.** Bell carrier counts through `n=10` are
  `1,1,2,5,15,52,203,877,4140,21147,115975`; distinct image counts are
  `1,1,2,3,5,9,17,32,61,118,233`; maximum tails are
  `0,0,1,1,2,2,2,2,2,2,2`.  Every image tested is noncrossing, and the next
  image is discrete.
- **Candidate sharp theorem.** A target `rho` is reachable iff it is
  noncrossing.  If `rho` has `m` entries and `s_1(rho)` singleton blocks, the
  observed and recursively constructible minimum ground-set size is
  `mu(rho)=2m-s_1(rho)`; checked for all targets through `m=5` using sources
  through size ten.
- **Independent second theorem axis.** One could enumerate minimum witnesses
  by connected chord diagrams inside the nesting forest of `rho`, or derive
  full-rank fibres by species substitution.
- **P1--P156 collision.** The image map is block-index notation for the
  connected-component construction in the classical noncrossing closure.
  Kreweras directly owns that operation and its closure theorem.  Generic
  set-partition closure is also permanently excluded.
- **Verdict.** **`KILL_DIRECT_OWNER`**.  The `2m-s_1` residual is not enough to
  relabel an owned closure as a new dynamics.

### `ILP` -- inversion-graph low-degree peeling

- **Carrier.** Permutations of ranks at most `N`; the graph of `pi` has one
  vertex per entry and an edge for each inversion.
- **Update.** Simultaneously delete vertices of current degree at most one and
  standardize the surviving permutation subword.
- **Small exact signature.** For ranks `0..8`, maximum tails are
  `0,1,1,2,2,3,3,4,5`; fixed counts are
  `1,0,0,1,5,31,228,1871,16988`; distinct images number
  `1,1,1,3,9,46,303,2342,20513`.
- **Candidate sharp theorem.** Classify the parallel shell-depth maximum over
  permutation graphs and the extremizing permutations.
- **Independent second theorem axis.** Enumerate permutation graphs with
  minimum degree at least two, refined by the standardized 2-core.
- **P1--P156 collision.** The update is literally the standard parallel
  computation of the graph 2-core, followed by a representation change.
  Generic closure/core machinery is permanently excluded, and P114 is the
  nearest internal peeling paper.
- **Verdict.** **`KILL_GENERIC_2_CORE`** after direct owner hit.

### `DFC` -- indegree-zero pruning of endofunctions

- **Carrier.** All functions `f:[n]->[n]`, for `0<=n<=N`.
- **Update.** Delete every current indegree-zero vertex in parallel, restrict
  `f` to the survivors, and order-relabel them.
- **Small exact signature.** Carrier counts for `n=0..6` are
  `1,1,4,27,256,3125,46656`; fixed counts are `n!`, namely
  `1,1,2,6,24,120,720`; maximum tails are `0,0,1,2,3,4,5`.
- **Candidate sharp theorem.** The terminal state is the cyclic permutation
  core of the functional digraph; the pointwise clock is the largest rooted
  in-tree pruning height and the rank-`n` maximum is `n-1`.
- **Independent second theorem axis.** Refine rooted-functional-digraph species
  by terminal permutation and layer profile to obtain target fibres.
- **P1--P156 collision.** This is the standard cyclic-core extraction of a
  functional graph, using the same leaf-height engine as P114 after reversing
  arrows.  Relabeling does not change that engine.
- **Verdict.** **`KILL_FUNCTIONAL_CORE_P114`**.

### `BGS` -- deterministic Bulgarian solitaire

- **Carrier.** Integer partitions of a fixed total `n`.
- **Update.** Remove one card from every pile, discard empty piles, and add a
  new pile whose size is the old number of piles; sort the parts.
- **Small exact signature.** Partition counts for `n=1..20` are
  `1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231,297,385,490,627`.
  Maximum transient lengths are
  `0,0,2,2,3,6,4,5,7,12,8,8,9,14,20,15,12,13,16,23`.
  The observed eventual-period sets begin
  `{1},{2},{1},{3},{3},{1},{4},{2,4},{4},{1}`.
- **Candidate sharp theorem.** An exact all-`n` description of recurrent
  cycles and maximal transients would be required; the irregular pilot gives
  no new clean formula.
- **Independent second theorem axis.** Basin enumeration by recurrent cycle
  and transient length.
- **P1--P156 collision.** This is the named classical deterministic Bulgarian
  solitaire itself; stochastic Bulgarian variants were already screened in
  the preceding batch.
- **Verdict.** **`KILL_CLASSICAL_OWNER`**.

### `PPS` -- parallel pop-stack sorting

- **Carrier.** `S_n` for fixed `n`.
- **Update.** Reverse every maximal descending run in parallel.
- **Small exact signature.** Maximum pass counts for `n=1..8` are
  `0,1,2,3,4,5,6,7`; one-step image counts are
  `1,1,3,11,49,263,1653,11877`.
- **Candidate sharp theorem.** The observed maximum is `n-1`, with an
  extremizer classification as the natural refinement.
- **Independent second theorem axis.** Exact image or `t`-sortable class
  enumeration.
- **P1--P156 collision.** Pop-stack sorting and its sortable classes are a
  mature direct literature, and push--pop/sorting interfaces are occupied in
  P82--P101 and explicitly listed in earlier scouts.
- **Verdict.** **`KILL_POP_STACK_OWNER`**.

### `TSW` -- TopSwops

- **Carrier.** `S_n` for fixed `n`.
- **Update.** If the first entry is `k>1`, reverse the first `k` entries; states
  beginning with `1` are fixed.
- **Small exact signature.** Maximum steps for `n=1..9` are
  `0,1,2,4,7,10,16,22,30`; the numbers of distinct terminal states are
  `1,1,2,6,24,120,720,5040,40320=(n-1)!`.
- **Candidate sharp theorem.** A closed extremal step formula or new strong
  bounds would be needed; the pilot reproduces the familiar irregular
  TopSwops extremal sequence.
- **Independent second theorem axis.** Refined basin sizes of the `(n-1)!`
  terminal permutations.
- **P1--P156 collision.** This is Conway's named TopSwops process, not a new
  update.  Prefix-reversal dynamics and open extremal values cannot be claimed
  from a small census.
- **Verdict.** **`KILL_NAMED_OWNER_OPEN_EXTREMAL`**.

### `CBB` -- cyclic box--ball matching

- **Carrier.** Labelled cyclic binary words of length `n` with at most
  `floor(n/2)` ones.
- **Update.** Repeatedly pair every cyclically adjacent unmatched `10`, remove
  paired positions from the matching pass, then place a ball at every paired
  zero.  This defines one full cyclic box--ball step.
- **Small exact signature.** Carrier counts for `n=1..12` are
  `1,3,4,11,16,42,64,163,256,638,1024,2510`.  The update is bijective in every
  checked rank; maximum periods are
  `1,2,3,4,5,6,21,16,45,30,77,48`.
- **Candidate sharp theorem.** Maximum orbit period at fixed circumference and
  density.
- **Independent second theorem axis.** Orbit counts refined by soliton content.
- **P1--P156 collision.** The carrier and pairing are standard periodic
  box--ball dynamics; Rule-184/Fredkin traffic interfaces are already occupied.
- **Verdict.** **`KILL_BOX_BALL_OWNER`**.

### `CSR` -- composition subtraction of the minimum

- **Carrier.** Positive compositions of a total `n`, with the empty
  composition as terminal state.
- **Update.** Subtract the smallest part from every part and delete zeros,
  preserving the order of survivors.
- **Small exact signature.** State counts for `n=1..14` are `2^(n-1)`;
  maximum tails are `1,1,2,2,2,3,3,3,3,4,4,4,4,4`.
- **Candidate sharp theorem.** For each state, the clock is exactly the number
  of distinct part values.  Hence the size-`n` maximum is the largest `k` with
  `k(k+1)/2<=n`.
- **Independent second theorem axis.** Count compositions of `n` by their
  number of distinct part sizes and record the ordered survivor chain.
- **P1--P156 collision.** The proof is a one-line ordered Euclidean
  subtraction and overlaps P131's Euclidean/composition territory.  The
  distinct-part enumeration is static and cannot carry a paper alone.
- **Verdict.** **`KILL_EUCLIDEAN_THEOREM_THIN`**.

### `SSE` -- singleton-block erasure

- **Carrier.** Set partitions of `[n]`, represented by restricted-growth
  words, across ranks at most `N`.
- **Update.** Delete all elements whose blocks are singletons and standardize
  the remaining partition.
- **Small exact signature.** Fixed counts for `n=0..9` are
  `1,0,1,1,4,11,41,162,715,3425`; distinct image counts are
  `1,1,2,3,7,18,59,221,936,4361`.  Every image is fixed.
- **Candidate sharp theorem.** The map is an idempotent retraction onto
  partitions with no singleton blocks.
- **Independent second theorem axis.** A target without singleton blocks has
  simple binomial label-insertion fibres; the empty target comes from the
  discrete partition.
- **P1--P156 collision.** This is a one-step selector/closure with static Bell
  enumeration, explicitly below the temporal threshold and within permanent
  generic-partition exclusions.
- **Verdict.** **`KILL_IDEMPOTENT_SELECTOR`**.

### `CPE` -- odd-cycle extraction

- **Carrier.** Permutations of ranks at most `N`.
- **Update.** Retain the union of all odd-length disjoint cycles, restrict the
  permutation to that set, and order-standardize its labels.
- **Small exact signature.** Fixed counts for `n=0..8` are
  `1,1,1,3,9,45,225,1575,11025`; distinct images number
  `1,1,2,4,11,49,236,1624,11261`.  Every image is fixed.
- **Candidate sharp theorem.** The fixed locus is the permutations with only
  odd cycles and the map is idempotent.
- **Independent second theorem axis.** Fibres factor into a chosen retained
  label set, an odd-cycle target, and an arbitrary even-cycle permutation on
  the complement.
- **P1--P156 collision.** P105 already uses permutation-cycle pruning and P155
  extracts one statistic per ordered cycle support.  Changing the selected
  cycle parity yields only a static exponential-formula selector.
- **Verdict.** **`KILL_CYCLE_SELECTOR`**.

### `TUS` -- nonroot unary suppression

- **Carrier.** Rooted plane trees of size at most `N`.
- **Update.** Recursively contract every nonroot vertex having exactly one
  child; the root itself is not contracted.
- **Small exact signature.** Fixed counts for sizes `1..10` are
  `1,1,1,2,4,9,21,51,127,323`; distinct images are
  `1,1,2,4,8,17,38,89,216,539`.  The update is idempotent.
- **Candidate sharp theorem.** Characterize the root-exceptional homeomorphically
  reduced plane trees and their OGF.
- **Independent second theorem axis.** Every target fibre is an ordered family
  of positive unary-chain subdivisions of its nonroot edges.
- **P1--P156 collision.** This is classical unary-chain contraction; P114 and
  P148 already occupy tree reduction, and the one-step nature supplies no new
  temporal theorem.
- **Verdict.** **`KILL_TREE_CONTRACTION`**.

### `ASD` -- deterministic adjacent-square deletion

- **Carrier.** Binary words of lengths at most `N`.
- **Update.** Among factors `XX`, choose minimum `|X|`, break ties by the
  leftmost start, and delete the second copy of `X`.
- **Small exact signature.** Maximum tails for lengths `0..12` are
  `0,0,1,2,3,4,5,6,7,8,9,10,11`; fixed counts are
  `1,2,2,2,0,0,0,0,0,0,0,0,0`.
- **Candidate sharp theorem.** Every terminal binary square-free word has
  length at most three, and the maximum tail is `n-1`, attained by a constant
  word.
- **Independent second theorem axis.** Classify deterministic normal forms and
  fibres under the shortest-leftmost scheduler.
- **P1--P156 collision.** The only temporal result is length descent under a
  chosen rewrite scheduler; word avoidance/rewrite and run interfaces are
  heavily occupied, and generic scheduling is permanently excluded.
- **Verdict.** **`KILL_WORD_REWRITE_THIN`**.

### `GQT` -- equal-open-neighborhood quotient

- **Carrier.** Labelled simple graphs on `[n]`, `0<=n<=N`.
- **Update.** Quotient the equivalence classes of vertices with equal open
  neighborhoods, order classes by least label, and use the induced quotient
  graph.
- **Small exact signature.** State counts for `n=0..6` are
  `1,1,2,8,64,1024,32768`; fixed counts are
  `1,1,1,4,32,588,21476`; distinct images are
  `1,1,2,6,38,626,22102`.  Every image is fixed.
- **Candidate sharp theorem.** This is an idempotent retraction onto
  point-determining graphs.
- **Independent second theorem axis.** Target fibres can be refined by positive
  multiplicities on false-twin classes.
- **P1--P156 collision.** The P112--P116 scout already killed the weighted
  true/false-twin quotient as directly owned by twin reduction and modular
  decomposition.  The present false-twin-only version is strictly weaker.
- **Verdict.** **`KILL_DIRECT_TWIN_QUOTIENT`**.

### `TSK` -- unique-sink stripping in tournaments

- **Carrier.** Labelled tournaments on `[n]`; ranks zero and one are fixed by
  convention.
- **Update.** A tournament has at most one sink.  Delete it if it exists and
  relabel; otherwise fix the state.
- **Small exact signature.** State counts through `n=6` are
  `1,1,2,8,64,1024,32768`; fixed counts are
  `1,1,0,2,32,704,26624`; maximum tails are `0,0,1,2,3,4,5`.
- **Candidate sharp theorem.** The maximum is `n-1`.  More precisely, a tail
  of length `t` is a forced ordered sink suffix attached below a sink-free core,
  giving an elementary exact tail distribution.
- **Independent second theorem axis.** The fixed count for `n>=2` is
  `2^(n choose 2)-n 2^((n-1) choose 2)`, and the suffix decomposition lifts it
  to all tail layers.
- **P1--P156 collision.** P112 already occupies labelled tournament dynamics;
  the present rule has only a forced transitive suffix and no independent deep
  engine.  Carrier reuse plus elementary counting is insufficient.
- **Verdict.** **`KILL_TOURNAMENT_COLLISION`**.

### `PFD` -- first-one deletion on parking functions

- **Carrier.** Classical parking functions of length at most `N`, including
  the empty function.
- **Update.** Delete the first occurrence of `1`; subtract one from every
  remaining entry greater than one.
- **Small exact signature.** State counts for `n=0..6` are
  `1,1,3,16,125,1296,16807=(n+1)^(n-1)` with the usual empty convention.
  Distinct images are `1,1,1,3,16,125,1296`; maximum tails are
  `0,1,2,3,4,5,6`.
- **Candidate sharp theorem.** The update is surjective onto the preceding
  rank, and every state has clock exactly its length.
- **Independent second theorem axis.** Refine one-step fibres by the first-one
  position and the set of entries lifted above one.
- **P1--P156 collision.** Time contains no state information: it is merely the
  forced rank schedule.  The remaining fibre is a standard parking-function
  deletion recurrence.
- **Verdict.** **`KILL_SCHEDULE_ONLY`**.

### `WBS` -- leftmost binary bubble sorting

- **Carrier.** Binary words of a fixed length `n`.
- **Update.** Replace the leftmost occurrence of `10` by `01`; fix a word with
  no such factor.
- **Small exact signature.** Maximum tails for lengths `0..14` are
  `0,0,1,2,4,6,9,12,16,20,25,30,36,42,49`; fixed counts are
  `1,2,3,...,15`.
- **Candidate sharp theorem.** The clock of a word equals its inversion number,
  so the maximum is `floor(n/2) ceil(n/2)`.
- **Independent second theorem axis.** The basin of `0^a1^(n-a)` is the
  corresponding weight layer, with Gaussian-binomial clock refinement.
- **P1--P156 collision.** This is comparator sorting/adjacent exclusion and is
  a sequential presentation of the same inversion engine surrounding
  Rule-184 traffic.  Both are permanent intake kills.
- **Verdict.** **`KILL_COMPARATOR_RULE184`**.

## Exact theorem contracts for the two recommended candidates

### Contract `LCP-A`: all iterates and sharp pointwise clock

Fix `N>=1` and the finite carrier of plane trees with at most `N` vertices.
For a nonroot vertex `v`, write `j_e` for the child index of each edge on its
root path and put `b_T(v)=min_e j_e`.  With `max(empty)=0`, prove for every
`t>=0` and `T=(T_1,...,T_k)` that

```text
L^t(T) = (L^t(T_{t+1}), ..., L^t(T_k)),
tau(T) = max_{v != root} b_T(v).
```

Consequences to include, not replace the theorem: the single vertex is the
only fixed/recurrent state, every nonfixed step strictly loses vertices, and
`max_{|T|=n} tau(T)=n-1`, attained by the `(n-1)`-leaf star.

### Contract `LCP-B`: every-target all-time inverse series

Let

```text
T(z) = sum_{n>=1} Catalan(n-1) z^n = z/(1-T(z)),
P_{t,U}(z) = sum_{V: L^t(V)=U} z^|V|.
```

For every `t>=0`, prove

```text
P_{t,bullet}(z) = z (1 + T(z) + ... + T(z)^t),
P_{t,(U_1,...,U_r)}(z)
    = z T(z)^t product_{a=1}^r P_{t,U_a}(z)       (r>=1).
```

For `t>=1`, derive coefficient positivity exactly at every source size
`n>=|U|+t i(U)`, where `i(U)` is the number of internal vertices.  Report
coefficient fibres, not just aggregate expectations.  Generic plane-tree GF
and expansion-operator facts must be cited/subtracted.

### Contract `PAE-A`: loss, fixed locus, and sharp clock

On `S_0 disjoint-union ... disjoint-union S_N`, define

```text
A(pi) = std(pi_i : i congruent pi_i (mod 2)).
```

Prove for every `pi in S_n`:

1. `n-|A(pi)|` is even.
2. `A(pi)=pi` iff `pi_i congruent i (mod 2)` for every `i`; hence the fixed
   count is `ceil(n/2)! floor(n/2)!`.
3. Every nonfixed step loses at least two entries and
   `max_{pi in S_n} tau(pi)=floor(n/2)`.

For sharpness, use the explicit even tower `E_0=empty`, `E_1=21`.  Given
`E_{r-1}` and `n=2r`:

- if `r` is even, let the retained positions be `1,...,n-2`, the retained
  values be `[n]` without `{n-3,n}`, place them in relative order `E_{r-1}`,
  then put `n,n-3` in positions `n-1,n`;
- if `r` is odd, let the retained positions be
  `1,...,n-4,n-2,n-1`, the retained values be `1,...,n-2`, place them in
  relative order `E_{r-1}`, and put `n` at position `n-3` and `n-1` at
  position `n`.

Prove `A(E_r)=E_{r-1}`.  The odd-rank witness is
`1 direct-sum E_r`, since `A(1 direct-sum pi)=1 direct-sum A(pi)` for even-rank
`pi`.

### Contract `PAE-B`: target threshold and every-target fibres

Fix `sigma in S_m`, `m>=1`.  Encode odd parity by `1`.  For a binary word
`a=(a_1,...,a_m)`, define the minimum alternating-host embedding length

```text
ell(a) = m + #{i<m : a_i=a_{i+1}} + 1[a_1=0].
```

Let `C_m` be the binary words with exactly `ceil(m/2)` ones.  For `c in C_m`,
put `beta_j=c_{sigma^{-1}(j)}` and

```text
M(sigma)  = min_{c in C_m} max(ell(c),ell(beta)),
mu(sigma) = m + 2 ceil((M(sigma)-m)/2).
```

Prove the gap-free same-parity image theorem

```text
sigma in A(S_n)  iff  n>=mu(sigma) and n congruent m (mod 2).
```

The empty target has `mu(empty)=0` and occurs only from even ranks.

For the fibre theorem, write retained positions and values as
`I=(p_1<...<p_m)` and `V=(v_1<...<v_m)`.  Sum over pairs satisfying
`p_i congruent v_{sigma_i} (mod 2)` and the complement-balance conditions

```text
a := # odd positions outside I = # even values outside V,
b := # even positions outside I = # odd values outside V.
```

Prove

```text
|A_n^{-1}(sigma)| = sum_{compatible (I,V)} a! b!.
```

The threshold proof must explicitly show that `ell` is both necessary and
sufficient and that adding two unused host coordinates preserves feasibility.
The fibre reconstruction must be bijective, including `m=0`, `n=m`, and empty
factorial boundaries.

## Recommendation and next gate

- Advance **`LCP` first** to a focused proof/owner audit.  Its two theorem axes
  are already exact and visibly independent: a pointwise temporal clock and a
  target-resolved inverse series.
- Advance **`PAE` second**, but as a collision-gated proof spike rather than a
  freeze.  The all-rank target theorem is worth proving precisely because the
  rank-eight anomaly falsifies the tempting simple threshold.  If the proof is
  merely P156 with colours substituted for inequalities, kill it immediately.
- Do not revive `CCQ` unless the update is changed substantially; its central
  closure is directly owned.

No candidate here is assigned a paper number, no manuscript has been drafted,
and all external activity remains `HOLD_EXTERNAL`.

## Reproduction

From the repository root:

```bash
python -B docs/papers157_161_sequence/scouting/combinatorial/verify_combinatorial_scout.py
```

The stdout must match `CANONICAL.txt` byte for byte.  The verifier uses only the
Python standard library and fixes every enumeration order explicitly.
