# P132--P136 combinatorial/geometric scouting lane

**Status:** Stage 1 internal scouting only; **HOLD EXTERNAL**.  No paper
number is assigned here, and no novelty, priority, release, or submission
claim is made.

**Search/computation snapshot:** 2026-08-31 UTC.

## 1. Scope and decision rule

This lane deliberately changed carriers often.  It audited permutations,
set partitions, parking functions, chord matchings, labelled graphs, rooted
labelled trees, Ferrers diagrams, fixed-grid polyominoes, and rectangular
lattice paths.  The pool contains **35 literal maps**, not 35 parameter
choices or cosmetic renamings.  Each stated finite phase space was completely
enumerated by `verify_combinatorial_scout.py`; there is no random sample.

The cheap decision rule was stricter than “the orbit plot looks structured.”
A survivor needed an all-size mechanism leading to at least two of: an exact
clock, recurrent census, full endpoint basin, pointwise fibre, or a sharp
extremum.  Generic closure, sorting, graph powers, tree algorithms, canonical
cycle notation, ordinary connected-graph enumeration, and standard parking
functions receive zero contribution credit.  A direct owner or an internal
map collision kills a candidate even when the pilot is beautiful.

The breadth run covers **791,292 parameter-labelled states** and makes
**3,166,328 assertions**.  Four focused controls add **2,047,983 assertions**,
for **5,214,311 assertions total**.  The result is intentionally narrow:

- **PM1: conditional promotion to an independent proof/collision gate**;
- **GR1: high-risk reserve with a complete theorem contract**;
- **33 kills**, including two especially important direct-owner kills, TR1
  and PK1.

Thus the lane returns exactly **two theorem-level candidates**, not a quota
of weak promotions.

## 2. Complete literal-map census

`I/F` is the image/fixed count at the last displayed parameter.  Periods and
maximum tails are the union/maximum over the full stated range.

| ID | Literal phase space and simultaneous update | Exact scope and fingerprint | Assertions | Decision |
|---|---|---:|---:|---|
| **PM1** | Put a permutation in minimum-first cycle notation, order cycles by increasing minima, and concatenate consecutive cycle pairs. | `S_n`, `1<=n<=7`; 5,913 states; periods 1, tail 3; last `I/F=1901/720`. | 23,680 | **PROMOTE CONDITIONALLY.** Logarithmic cycle-count clock, every depth layer, terminal cut fibres, and a unique maximum survive. |
| **PM2** | Use the same canonical cycle list, but merge each pair by alternating entries from the two cycle words. | Same 5,913 states; periods 1, tail 3; last `I/F=1393/720`. | 23,680 | **KILL behind PM1.** Same halving clock, less associative endpoint geometry. |
| **PM3** | In each cycle, keep its minimum first and sort the remaining entries increasingly. | Same 5,913 states; idempotent; last `I/F=877/877`. | 23,680 | **KILL.** One-step canonicalisation on the occupied P105 cycle carrier. |
| **PM4** | Rotate the one-line word until the value 1 is first. | Same 5,913 states; idempotent; last `I/F=720/720`. | 23,680 | **KILL.** Transparent projection, uniform fibre, no temporal residual. |
| **PM5** | Replace a permutation by its inverse iff its inversion number is odd. | Same 5,913 states; periods 1,2, tail 0; last `I/F=5040/2646`. | 23,680 | **KILL.** Statistic-gated classical involution. |
| **PM6** | Reverse the prefix ending at the maximum value. | Same 5,913 states; idempotent; last `I/F=720/720`. | 23,680 | **KILL.** Label-dependent one-step projection. |
| **PM7** | Split the one-line word into maximal increasing runs and reverse the run list. | Same 5,913 states; periods 1,2, tail 1; last `I/F=1653/1`. | 23,680 | **KILL.** Small cycles arise from representation reversal; P117/P122 run-reversal risk and no all-size fibre engine. |
| **SP1** | Order set-partition blocks by minima and union adjacent pairs. | Set partitions through `n=7`; 1,155 states; periods 1, tail 3; last `I/F=65/1`. | 4,648 | **KILL.** Exact dyadic block clock, but direct deterministic coarsening collision with P110 and the portfolio's coalescence lane. |
| **SP2** | Union consecutive triples of canonical blocks. | Same 1,155 states; periods 1, tail 2; last `I/F=17/1`. | 4,648 | **KILL behind SP1.** Base-3 scheduler is not a new mechanism. |
| **SP3** | Simultaneously move the minimum of every nonfirst block into the preceding block. | Same 1,155 states; periods 1, tail 6; last `I/F=203/1`. | 4,648 | **KILL.** Label scheduler dominates; no stable fibre or clock formula. |
| **SP4** | Simultaneously move the maximum of every nonlast block into the following block. | Same 1,155 states; periods 1, tail 10; last `I/F=352/1`. | 4,648 | **KILL.** Longest cheap tail, but counterexample-rich and still an arbitrary block-transfer rule. |
| **SP5** | Pair canonical blocks; merge a pair exactly when its two sizes have equal parity. | Same 1,155 states; periods 1, tail 3; last `I/F=301/136`. | 4,648 | **KILL.** Parity-scheduled coarsening collides with P110/P123. |
| **SP6** | Reflect labels `i -> n+1-i` iff the block count is odd. | Same 1,155 states; periods 1,2, tail 0; last `I/F=877/467`. | 4,648 | **KILL.** Gated relabelling involution. |
| **SP7** | Split every block into its lower and upper halves in sorted label order. | Same 1,155 states; periods 1, tail 3; last `I/F=121/1`. | 4,648 | **KILL INTERNAL.** Its balanced refinement clock is P126's occupied engine on a set-partition carrier. |
| **PK1** | Run the ordinary parking algorithm and replace a preference list by the final spot of each car. | Parking functions through `n=7`; 280,392 states; idempotent; last `I/F=5040/5040`. | 1,121,596 | **KILL DIRECT.** Pinsky 2026 owns the outcome distribution, every fibre product, and unique extrema (up to inverse convention). |
| **MT1** | In every crossing-graph component of a chord matching, cyclically shift the right endpoints among chords ordered by left endpoint. | Matchings through 5 chords; 1,069 states; periods 1, tail 7; last `I/F=384/42`. | 4,296 | **KILL.** Arbitrary endpoint scheduler on P130's exact carrier. |
| **MT2** | Resolve the lexicographically first crossing pair into two separated pairs. | Same 1,069 states; periods 1, tail 5; last `I/F=319/42`. | 4,296 | **KILL DIRECT INTERNAL.** Local uncrossing is zero-credit beside P130's componentwise retraction. |
| **MT3** | Flatten the lexicographically first nested chord pair into separated pairs. | Same 1,069 states; periods 1, tail 6; last `I/F=335/42`. | 4,296 | **KILL.** Tie-broken canonical flattening with no new inverse geometry. |
| **GR1** | Replace a labelled simple graph by its square: join vertices at distance at most two. | All graphs through `n=6`; 33,867 states; periods 1, tail 3; last `I/F=2863/203`. | 135,492 | **RESERVE / theorem-level.** Exact powers, clocks, Bell fixed set, every endpoint basin, and every fixed-target one-step fibre survive, but the core is classically owned. |
| **GR2** | Replace `G` by its third graph power. | Same 33,867 states; periods 1, tail 2; last `I/F=518/203`. | 135,492 | **KILL behind GR1.** Merely changes the logarithm base. |
| **GR3** | Delete every edge contained in a triangle. | Same 33,867 states; idempotent; last `I/F=5789/5789`. | 135,492 | **KILL.** One-step triangle-edge filter. |
| **GR4** | Retain exactly the edges contained in at least one triangle. | Same 33,867 states; idempotent; last `I/F=6115/6115`. | 135,492 | **KILL.** Dual one-step filter, no temporal hierarchy. |
| **GR5** | Delete all bridges simultaneously. | All graphs through `n=5`; 1,099 states; idempotent; last `I/F=314/314`. | 4,416 | **KILL.** Every retained edge already lies on a retained cycle; ordinary core projection. |
| **GR6** | Complement the induced graph on each even-order connected component. | All graphs through `n=5`; 1,099 states; periods 1,2, tail 2; last `I/F=854/769`. | 4,416 | **KILL INTERNAL.** Direct P123 odd/even component-complement silhouette. |
| **GR7** | Add every missing edge whose endpoints are currently at distance exactly three. | All graphs through `n=6`; 33,867 states; periods 1, tail 2; last `I/F=14558/14468`. | 135,492 | **KILL.** Weak monotone closure; no pointwise endpoint/fibre theorem survived. |
| **TR1** | On a rooted labelled tree, replace every parent pointer by its grandparent pointer. | Root fixed at 1, all trees through `n=7`; 18,249 states; periods 1, tail 3; last `I/F=3451/1`. | 73,024 | **KILL DIRECT.** This is classical pointer jumping/tree contraction, despite a complete clock and star-fibre formula. |
| **TR2** | Move the distinguished root through the unique incident component of size greater than `n/2`, if one exists. | Every vertex-rooted labelled tree through `n=7`; 126,126 states; periods 1, tail 3; last `I/F=63217/16807`. | 504,532 | **KILL DIRECT.** Standard centroid descent; the depth is distance to the centroid set. |
| **TR3** | Move the root to the least-labelled neighbor of strictly smaller eccentricity. | Same 126,126 states; periods 1, tail 3; last `I/F=63217/24997`. | 504,532 | **KILL DIRECT.** Standard center descent with an artificial tie rule. |
| **PT1** | Pair adjacent Ferrers columns and replace each pair by one column whose height is their sum. | Integer partitions of weights `1<=n<=25`; 9,295 states; periods 1, tail 5; last `I/F=420/1`. | 37,280 | **KILL INTERNAL.** Exact width-halving clock, but adjacent coarsening is the reverse silhouette of P126 and the carrier is occupied by P113. |
| **PX1** | Fill every gap between the first and last occupied cell in each row. | Connected fixed-grid polyominoes in `2x3,3x3,3x4`; 1,384 states; idempotent; last `I/F=698/698`. | 5,548 | **KILL.** Ordinary row-convex hull. |
| **PX2** | Apply row convexification followed by column convexification. | Same 1,384 states; idempotent on the audited grids; last `I/F=571/571`. | 5,548 | **KILL.** No multi-round anomaly; generic orthogonal closure. |
| **PX3** | If area is odd, fill the bounding rectangle; otherwise fix. | Same 1,384 states; idempotent; last `I/F=582/582`. | 5,548 | **KILL.** Statistic-gated bounding-box projection. |
| **LP1** | In every rectangular E/N path, swap all occurrences `NE -> EN` in parallel. | All boxes with sides at most 5; 912 states; periods 1, tail 9; last `I/F=83/1`. | 3,748 | **KILL INTERNAL.** Parallel bubble/traffic rule; Rule 184 and P090 occupy the mechanism. |
| **LP2** | Reverse the step word iff its area is `1 mod 3`. | Same 912 states; periods 1,2, tail 1; last `I/F=168/168`. | 3,748 | **KILL.** Gated word reversal beside P117/P122. |
| **LP3** | Rotate the word left once while its first step is north; otherwise fix. | Same 912 states; periods 1, tail 5; last `I/F=182/126`. | 3,748 | **KILL.** Cut-dependent prefix stripping with no invariant geometry. |

## 3. Candidate PM1: parallel pairing of canonical permutation cycles

### 3.1 Literal map

For `pi in S_n`, write every cycle starting at its least label and order the
cycles `C_1,...,C_k` by increasing least label.  Define

```text
Phi(pi) = (C_1 C_2)(C_3 C_4)...,
```

where juxtaposition *inside one pair of parentheses* means concatenate the
two cycle words, and an unpaired final cycle is retained.  The first entry of
`C_{2j-1}` is still the minimum of the merged support, so this is a literal,
unambiguous self-map of `S_n`.

### 3.2 Admissible theorem contract

Let `c(pi)` be the number of cycles and let
`[{n \atop k}]` denote the unsigned Stirling number of the first kind.

1. **Exact iterate and clock.**  After `t` rounds, consecutive initial cycles
   are concatenated in blocks of at most `2^t`.  Hence

   ```text
   c(Phi^t(pi)) = ceil(c(pi)/2^t),
   depth(pi) = ceil(log_2 c(pi)).
   ```

   The sharp global depth is `ceil(log_2 n)`.
2. **Complete recurrent and depth census.**  The recurrent set is precisely
   the `(n-1)!` `n`-cycles, all fixed.  Thus the formal finite zeta function
   is `(1-z)^(-(n-1)!)`.  The depth-zero layer has size `(n-1)!`, and for
   `d>=1` the exact layer is

   ```text
   sum_{2^(d-1) < k <= min(2^d,n)} [{n \atop k}].
   ```

3. **Endpoint map.**  The terminal `n`-cycle is obtained by erasing the
   parentheses between the initial canonical cycle words.  This gives a
   nonconstant retraction `E_n:S_n -> {n-cycles}`.
4. **Every terminal fibre.**  If the minimum-first word of a target cycle is
   `w=w_1...w_n`, its fibre is in bijection with cuts of `w` into contiguous
   blocks such that each block begins with its own minimum and the sequence
   of block minima is strictly increasing.  Each admissible cut inserts the
   parentheses of one unique source permutation.
5. **Sharp terminal fibre.**  There are at most `2^(n-1)` cut sets.  Equality
   forces the all-singleton cut to have increasing block minima, hence
   `w=12...n`.  Therefore the increasing `n`-cycle is the unique largest
   terminal target and its basin has size `2^(n-1)`.

The focused control exhausts all **409,113 permutations through `S_9`**.  It
checks the pointwise clock, the Stirling-band depth layers, recurrence, every
terminal fibre accumulated from sources, total mass, and the unique maximum:
**818,271 assertions**.

Two proof routes are available.  The parenthesis route is a direct induction
on rounds and then an admissible-cut bijection.  The group route writes each
pairwise concatenation as a join transposition between two disjoint cycles;
the round scheduler is a binary merge tree.  The first route is cleaner and
does not disguise the label-order dependence.

### 3.3 Counterpressure and owner subtraction

- The map is not conjugacy-equivariant: it depends essentially on the label
  order used to choose and order canonical cycle words.
- Terminal fibre size is not a class function.  At `n=3`, the two target
  3-cycles have fibres 4 and 2 although their cycle types agree.
- There are no nontrivial recurrent periods; the value lies in the transient
  normal form and terminal cut geometry, not in exotic cycles.
- Goulden and Jackson's primary paper,
  [*Transitive Factorisations into Transpositions and Holomorphic Mappings on the Sphere*](https://doi.org/10.1090/S0002-9939-97-03880-X),
  owns the cut--join mechanism: multiplying by a transposition joins two
  disjoint cycles and its join operator counts all such choices.
- Khanna and Loehr,
  [*A Local Framework for Proving Combinatorial Matrix Inversion Theorems*](https://doi.org/10.37236/14164),
  explicitly use canonical cycle notation, cycle compositions, their exact
  enumeration, and composition refinement/coarsening.  All of that is
  zero-credit here.

The bounded search did **not** locate the literal repeated adjacent-pair
scheduler together with its all-iterate Stirling layers and target-wise
admissible-cut terminal fibres.  A search non-hit is not novelty evidence.

**Internal firewall.**  P105 deletes a least label from each cycle and has a
linear longest-cycle clock terminating at the identity; PM1 instead merges
whole cycles, has a logarithmic cycle-count clock, and terminates at many
orientation-sensitive `n`-cycles.  P110 coarsens set partitions by cyclic
shift--join, P121/P129 are stochastic coalescence systems, and P126 refines
integer compositions.  PM1 shares one noun or silhouette with each, but no
single one has its carrier, literal update, endpoint word, and cut fibre.
This is still close enough to require a dedicated hostile collision gate.

**Verdict:** **8.1/10, `PROMOTE_TO_INDEPENDENT_PROOF_AND_COLLISION_GATE`**.
Kill if a direct source owns the repeated scheduler or if the P105/P126
review regards the parenthesis residual as insufficient.

## 4. Candidate GR1: graph-square dynamics

### 4.1 Literal map and complete theorem contract

For a labelled simple graph `G` on `[n]`, let `Phi(G)=G^2`: distinct vertices
are adjacent in `G^2` exactly when their distance in `G` is at most two.
Let `D(G)` be the maximum diameter of a connected component, with isolated
components assigned diameter zero.

1. **Exact iterates.**  Graph distances give
   `(G^a)^b=G^(ab)`, hence `Phi^t(G)=G^(2^t)`.
2. **Endpoint and clock.**  The endpoint `K(G)` completes each connected
   component to a clique, and

   ```text
   depth(G) = 0                         if D(G)<=1,
              ceil(log_2 D(G))          otherwise.
   ```

   The sharp maximum on `[n]` is `ceil(log_2(n-1))`, attained by the path
   for `n>=3`.
3. **Recurrence.**  Fixed points are exactly cluster graphs, one for each set
   partition of `[n]`; there are `B_n`, no other cycles, and the zeta function
   is `(1-z)^(-B_n)`.
4. **Every endpoint basin.**  If a fixed target has clique blocks
   `B_1,...,B_r`, then

   ```text
   |K^(-1)(target)| = product_i c_|B_i|,
   ```

   where `c_m` is the classical number of connected labelled graphs on a
   prescribed `m`-set.
5. **Every fixed-target one-step fibre.**  The one-step fibre is

   ```text
   |Phi^(-1)(target)| = product_i q_|B_i|,
   ```

   where `q_m` counts connected labelled graphs of diameter at most two on a
   prescribed `m`-set.  This follows because squaring preserves components
   and turns a connected component into a clique in one round exactly at
   diameter at most two.
6. **All depth-prefix counts.**  If `c_m^(<=R)` counts connected labelled
   graphs of diameter at most `R`, then the number of states of depth at most
   `t` has exponential generating function

   ```text
   exp(sum_{m>=1} c_m^(<=2^t) z^m/m!).
   ```

   Exact layers are consecutive differences.

The focused pilot exhausts **33,867 graphs through `n=6`** and verifies the
iterate identity, endpoint, pointwise clock, Bell fixed count, every endpoint
basin product, every fixed-target one-step fibre product, and the sharp global
clock: **102,169 assertions**.

### 4.2 Owner subtraction and value ceiling

Owner risk is much higher than for PM1.

- Ross and Harary,
  [*The Square of a Tree*](https://doi.org/10.1002/j.1538-7305.1960.tb03936.x),
  explicitly define `G^2` through Boolean adjacency-matrix squaring and study
  graph square roots.  Graph powers, distance contraction, and completion at
  the diameter are classical and receive zero credit.
- Gilbert,
  [*Enumeration of Labelled Graphs*](https://doi.org/10.4153/CJM-1956-046-2),
  owns the connected-labelled-graph counts and their component decomposition.
  Consequently the factors `c_m`, their recurrence, and the exponential
  formula are zero-credit.
- Square-root recognition and graph-power structure are large mature
  literatures.  The bounded current search found no paper presenting this
  exact finite-functional-graph package, but that absence is weak evidence.

The only residual is the conjunction of the fixed operator with its exact
temporal stratification, pointwise endpoint basins, and pointwise fixed-target
fibres.  Each individual ingredient is elementary once graph powers are
accepted.  Internally, GR1 is not P097 sumset squaring, P106 MIS polarity,
P123 component complementation, or P127 binary-matrix transpose dynamics:
its invariant is graph distance and its endpoint is the component clique
partition.  Nevertheless “a classical power operation repackaged as a finite
dynamics” is a real portfolio-level value risk.

**Verdict:** **7.0/10, `RESERVE_TO_HOSTILE_VALUE_GATE`**.  Promote only if an
independent review judges the all-target basin/fibre conjunction sufficient;
otherwise kill as owner-saturated theorem packaging.

## 5. Direct-owner kills that prevented false promotion

### TR1: parent jumping

The exact control through `n=8` checks 280,393 rooted trees and 560,818
assertions.  It proves computationally that after `t` rounds the parent of
`v` is its ancestor `2^t` levels up, the depth is
`ceil(log_2(height))`, the rooted star is the unique attractor, and its
one-step fibre is

```text
sum_{k=1}^{n-1} binom(n-1,k) k^(n-1-k).
```

This is not a candidate.  Miller and Reif's primary
[*Parallel Tree Contraction Part 1: Fundamentals*](https://www.cs.cmu.edu/~glmiller/Publications/b2hd-MR1-89.html)
and Abrahamson et al.'s
[*A Simple Parallel Tree Contraction Algorithm*](https://doi.org/10.1016/0196-6774(89)90017-5)
place grandparent pointer jumping and logarithmic contraction directly in the
owned algorithmic core.  The star-fibre count alone cannot carry a paper.

### PK1: classical parking outcome

The exact control through `n=7` checks all 280,392 parking functions and
566,725 assertions.  It recovers the product of consecutive occupied spots
immediately to the left of each arriving car, total mass `(n+1)^(n-1)`, and
the unique maximum fibre `n!`.

Pinsky's 2026 primary paper,
[*The Distribution on Permutations Induced by a Random Parking Function*](https://doi.org/10.37236/13842),
defines the same classical outcome map in inverse permutation convention,
gives the explicit product for every outcome, and proves the unique maximum
and minimum.  Harris and Martinez,
[*Parking Functions with a Fixed Set of Lucky Cars*](https://arxiv.org/abs/2410.08057),
further occupy outcome/lucky-set enumeration.  PK1 therefore receives zero
residual credit and is **KILL DIRECT**, despite being the cleanest raw fibre
signal in the pool.

## 6. Portfolio collision firewall

| candidate/family | closest occupied papers | firewall result |
|---|---|---|
| PM1 cycle-pair merge | P105 cycle-minimum pruning; P110 shift--join partitions; P121/P129 coalescence; P126 balanced composition refinement | Conditional separation by whole-cycle merge, logarithmic cycle-count clock, many `n`-cycle endpoints, and label-sensitive cut fibres. Requires hostile gate. |
| GR1 graph square | P097 sumset squaring; P106 MIS polarity; P123 component complement; P127 looped-digraph matrix dynamics | Literal carrier/update and distance proof differ. Main risk is external classical ownership, not direct internal conjugacy. |
| TR1 parent jump | P114 forest peeling; P120 plane-tree mirror; P129 rootward coalescence | Internally distinct, but direct external pointer-jumping owner kills it. |
| PK1 parking outcome | P078 complete-bipartite sandpile translations and the broader chip-firing neighborhood | Carrier differs internally, but Pinsky directly owns the literal target-fibre theorem. |
| SP1--SP7 | P110, P123, P126 | All coarsening/refinement/parity residuals are already occupied or theorem-thin. |
| MT1--MT3 | P130 | Same rooted chord-matching carrier without P130's target-wise inverse geometry; killed. |
| PT1 | P113, P126 | Ferrers carrier plus binary adjacent coarsening fails the joint carrier/mechanism firewall. |
| LP1--LP3 | P090, P117, P122 | Traffic sorting and gated reversal are directly occupied silhouettes. |

Across the five-paper finalist search, PM1 and GR1 must also be compared with
all other lanes on carrier, literal map, recurrent silhouette, proof engine,
and theorem outputs.  A shared logarithmic clock alone is not a collision;
changing only a carrier never cures one.

## 7. Handoff

1. Send **PM1** to a proof spike that formalizes the admissible-cut fibre
   bijection and then to an independent P105/P110/P126 collision review.
2. Send **GR1** only to a hostile value gate.  Its mathematics is exact, but
   the review should be willing to kill it if “all basins plus fixed-target
   fibres” does not clear the classical graph-power ownership ceiling.
3. Do not revive TR1 or PK1 by adding dynamics vocabulary; their principal
   mechanisms/results have direct owners.
4. Preserve **HOLD EXTERNAL** until a separate, current owner/novelty process
   clears whichever candidate survives cross-lane comparison.

Reproduction:

```bash
python docs/papers132_136_sequence/scouting/combinatorial/verify_combinatorial_scout.py
```

The stdout must match `CANONICAL.txt` byte for byte.
