# Breadth and kill ledger: ten literal deterministic systems

**Scope:** P197--P201 internal graph/matching lane.  **External state:**
`HOLD_EXTERNAL`.  Each row is one literal map, not a parameter choice.  All
schedulers, ties, and hold branches are part of the definition.

## Ranked outcome

| rank | ID | carrier and complete update | exact pilot fingerprint | proof spike | decision |
|---:|---|---|---|---|---|
| 1 | `CMM` | For odd `n=2m+1`, take a matching of the labelled cycle.  If it has at least three monomers, let `a` be the least-labelled monomer and `b` the next monomer clockwise; flip the unique alternating arc from `a` to `b`.  If it has one monomer `a`, flip the first two clockwise edges, moving the monomer to `a+2`.  These cases exhaust the carrier. | Exhaustive odd `n=3..21`.  At `n=21`: 24,476 states, image 9,351, one 21-cycle, maximum tail 10, unique maximum fibre 56. | Exact deficiency clock and all depth layers; one recurrent `n`-cycle; every-target triangular fibre; Lucas image; unique fibre maximum. | **`PROVISIONAL_AMBER_HOSTILE_GATE`**, the sole recommendation.  Not sorting, closure, equal-size coagulation, or a graph power; P90/GCM/AP1 proof-transfer risk remains serious. |
| 2 | `LGB` | Root a labelled tree at `0`.  If a leaf of depth at least two exists, move the least-labelled such leaf from its parent to its grandparent.  Otherwise hold. | All rooted trees through `n=8`; at `n=8`: 262,144 states, image 144,495, one fixed star, maximum tail 21, unique maximum fibre 43. | Point clock is total excess depth; rooted-tree `q`-EGF/recurrence gives every layer; complete sibling-pair inverse atlas; sharp paths and star fibre. | **`RESERVE_ONLY`**.  Literal separation is real, but P114/P148/RLR/tree-lift machinery and proximity to P195 make the lane too crowded for a freeze. |
| 3 | `LAP` | On a matching of the path `P_n`, take its two least unmatched vertices and flip their unique alternating interval; if fewer than two vertices are unmatched, hold. | All states through `n=18`; at `n=18`: 4,181 states, image 1,597, one fixed perfect matching, maximum tail 9, unique maximum fibre 46. | Tail `floor(n/2)-|M|`; binomial matching layers; exact first-monomer triangular fibres and Fibonacci image. | **`KILL_BEHIND_CMM_AP1_GCM`**.  It is the fixed-core precursor of `CMM`, and the remaining clock is the classical augmenting-path deficiency clock. |
| 4 | `LDF` | On a labelled simple graph, find the lexicographically least nonedge whose endpoints have an old common neighbour, add that one edge, and otherwise hold. | All graphs through `n=6`; at `n=6`: 32,768 states, image 15,593, 203 fixed graphs, maximum tail 10, unique maximum fibre 16. | Tail is the number of missing edges inside the initial connected components; fixed graphs are cluster graphs; deepest states are the `n^(n-2)` trees; every target has an admissible deleted-edge atlas. | **`KILL_GRAPH_SQUARE_CLOSURE`**.  This is graph-square/component-clique closure serialized by a lexicographic scheduler. |
| 5 | `LSL` | Root a labelled tree at `0`.  Choose the least-labelled vertex of depth at least two, delete its parent edge, attach it directly to the root, and otherwise hold.  The whole descendant subtree travels with the chosen vertex. | All rooted trees through `n=8`; at `n=8`: 262,144 states, image 48,729, one fixed star, maximum tail 6, unique maximum fibre 43. | Tail `n-1-deg(0)`; depth-`d` population `binom(n-2,d)(n-1)^d` from Prüfer words. | **`KILL_CANONICAL_BASIS_SORT`**.  Adding a missing star-basis edge and deleting the fundamental-path edge is a greedy graphic-matroid normalization/root-degree countdown. |
| 6 | `FCM` | Write a permutation in minimum-first canonical cycles ordered by increasing minima.  If at least two cycles occur, concatenate the first two cycle words into one cycle and retain the rest; otherwise hold. | Through `S_8`; at `n=8`: image 20,160, fixed 5,040, maximum tail 7, unique maximum fibre 8. | Tail is cycle count minus one; unsigned-Stirling depth layers; all long cycles fixed. | **`KILL_MCJ_PM1`**.  This is the serial first-block version of the already killed `MCJ`/`PM1` cut--join and flattened-cycle engine. |
| 7 | `LVR` | For `pi in S_n`, put `c_i=#{j>i:pi_j<pi_i}` and replace `pi_i` by the stable rank of `(c_i,i)`.  The position breaks all ties. | Through `S_8`; at `n=8`: image 5,335, fixed 1,430, maximum tail 6, unique maximum fibre 83. | Catalan fixed locus and sharp `n-2` clock appear. | **`KILL_EXACT_CONJUGACY_S01`**.  Reversing the right Lehmer code turns the update exactly into strict-earlier-rank iteration, the frozen direct-owner kill. |
| 8 | `CASR` | For `pi in S_n`, put `s_i=pi_i+pi_(i+1 mod n)` and replace each position by the stable rank of `(s_i,i)`. | Through `S_8`; at ranks `3..8`, period sets are `{6},{8},{10},{6,12},{14},{8,16}` and maximum tails are `0,1,5,11,24,33`; at `n=8`, image 10,083 and maximum fibre 54. | An explicit `2n` orbit exists, but neither the transient clock nor arbitrary-target inequalities close uniformly. | **`KILL_DIRECT_SCOUT_REPLAY`**.  Literal `Q01_ASR` and its atlas failure were already frozen in the P172--P176 scout. |
| 9 | `OTP` | Simultaneously retain an old edge `uv` iff `|N(u) intersect N(v)|` is odd; all other old edges are deleted. | All graphs through `n=6`; at `n=6`: image 799, fixed 187, maximum tail 3, maximum fibre 6,560. | Edge deletion is monotone, but fixed graphs and fibres are coupled cubic parity constraints. | **`KILL_C20_DIRECT`**.  The identical odd-triangle edge-pruning map already appears as `C20/OTP`. |
| 10 | `OTC` | Let `S` be the vertices incident with an odd number of old triangles and Seidel-switch the cut `delta(S)`; if the cut is empty the state holds automatically. | All graphs through `n=6`; at `n=6`: image 14,676, fixed 7,356, periods `1,2,4`, maximum tail 3, maximum fibre 20. | Small ranks do not support one period or inverse theorem. | **`KILL_X02_DIRECT`**.  The identical odd-triangle cut switch was already frozen as `X02`, with the same tails and periods. |

The denominator is ten.  `CMM` and `LAP` are counted separately because one
has an odd-cycle rotor and no fixed point while the other has a fixed maximum
matching core; nevertheless `LAP` is killed behind the strictly stronger
`CMM` rather than proposed as a second slot.

## Exact pilot ledger

For `CMM`, the rows `(n, states, image, recurrent, max tail, max fibre)` are

```text
(3, 4, 3, 3, 1, 2)
(5, 11, 6, 5, 2, 4)
(7, 29, 13, 7, 3, 7)
(9, 76, 31, 9, 4, 11)
(11, 199, 78, 11, 5, 16)
(13, 521, 201, 13, 6, 22)
(15, 1364, 523, 15, 7, 29)
(17, 3571, 1366, 17, 8, 37)
(19, 9349, 3573, 19, 9, 46)
(21, 24476, 9351, 21, 10, 56)
```

The verifier also exhausts `LAP` through `n=18`, every permutation through
`S_8` for each of `FCM/CASR/LVR`, all 32,768 graphs on six vertices for each
of `OTP/OTC/LDF`, and all 262,144 rooted labelled trees at `n=8` for each of
`LGB/LSL`.  Its `2,508,857` assertions include closure, complete functional
graphs, target indegrees, boundary ranks, formula comparisons, and direct
conjugacy/replay controls.

## Proof spikes for the two top rows

### `CMM`

Consecutive monomers on an odd-cycle matching are separated by an odd number
of edges, and the intervening path is forced alternating.  The selected flip
therefore removes exactly two monomers and raises matching size by one.  At
maximum size the unique monomer moves by `+2`; since the cycle length is odd,
the `n` maximum matchings form one `n`-cycle.

If a target's least monomer is `u`, its vertices before `u` contain exactly
`floor(u/2)` forced consecutive dimers (with the parity determined by whether
the wrap edge is used).  A transient predecessor is uniquely a nonempty
contiguous interval of those dimers.  This yields a triangular number, not a
generic existence proof.  `CMM_THEOREM_CONTRACT.md` gives the complete formula.

### `LGB`

Moving one leaf to its grandparent lowers

```text
sum_(v != 0) (depth(v)-1)
```

by exactly one.  The only zero is the rooted star.  Rooted paths with root at
an endpoint maximize the statistic and give `(n-1)!` deepest states.  For a
target, reverse one step by choosing a target leaf `v` and a sibling `p`, then
reattaching `v` below `p`; the least-eligible-leaf condition is a target-local
inequality.  This is mathematically complete, but its entire environment is a
crowded labelled-tree surgery/species lane, hence reserve rather than promote.

## Final funnel

```text
10 literal maps
  1 provisional amber recommendation: CMM
  1 reserve only: LGB
  2 mechanism kills: LAP, LDF
  1 canonical-basis sorting kill: LSL
  5 direct/conjugate historical kills: FCM, LVR, CASR, OTP, OTC
```

