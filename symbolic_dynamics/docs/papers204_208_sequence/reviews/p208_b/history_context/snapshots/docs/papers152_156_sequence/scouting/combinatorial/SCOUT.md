# Combinatorial/geometric Stage-1 scout — P152–P156

**External status:** `HOLD_EXTERNAL`.  **Paper numbering:** unassigned.  This is
an internal breadth scout, not a manuscript, a novelty statement, or release
clearance.  Enumeration below is counterexample pressure only.

## Outcome

Fourteen genuinely different literal systems were owner-screened and tested.
There is **one** possible survivor, `WEX`, and deliberately no second survivor.
`UHC` is the honest runner-up: its geometry, fixed-point classification, and
all-target board formula are clean, but the finite clock has not produced an
all-parameter sharp theorem.  It is therefore a reserve/falsifier target, not a
quota filler.

| rank | handle | literal update | strongest exact signal | verdict |
|---:|---|---|---|---|
| 1 | `WEX` | retain permutation entries `pi_i >= i`, then standardize | exact maxdrop image, explicit right section, every-target Ferrers fibres; Fibonacci size/drop clock under one named proof gate | **`SELECT_INTERNAL_PROOF_GATE`** |
| 2 | `UHC` | take strict upper-hull vertices of `(i,pi_i)`, read heights, standardize | finite fixed-point classification; exact cap-board fibres; tails `0,0,1,2,2,3,3,4,4` | **`RESERVE_NO_SHARP_CLOCK`** |
| 3 | `TFE` | flip the lexicographically first root-frontier diagonal toward a fixed polygon vertex | tail equals missing root diagonals; Catalan-triangle layers | `KILL_DIRECT_FAN_FLIP/P144` |
| 4 | `DSE` | erase the outer `U,D` shell of every primitive Dyck excursion | tail equals height | `KILL_TREE_ROOT_PEEL/P144/P148` |
| 5 | `NCK` | Kreweras complement on noncrossing partitions | complete periods divide `2n` | `KILL_DIRECT_OWNER` |
| 6 | `RSP` | Schützenberger promotion on rectangular SYT | rectangular finite order and cycle census | `KILL_DIRECT_OWNER` |
| 7 | `BPC` | complement a plane partition in its box | involution, volume pairing, fixed-point census | `KILL_DIRECT_OWNER/ONE_STEP` |
| 8 | `LDL` | flip the lexicographically first illegal Delaunay edge | absorbing Delaunay triangulation | `KILL_LAWSON_ALGORITHM` |
| 9 | `LSC` | lexicographically first elementary free-face collapse | exact collapse trace and terminal core | `KILL_DISCRETE_MORSE_OWNER/SCHEDULER_ONLY` |
| 10 | `G2C` | synchronously delete graph vertices of degree below two | exact 2-core and peeling depth | `KILL_CORE_DECOMPOSITION` |
| 11 | `OIR` | rowmotion on ideals of a product of two chains | order divides `a+b`, complete small cycles | `KILL_DIRECT_OWNER` |
| 12 | `PLA` | replace a lattice polygon by the hull of its interior lattice points | rectangle clock `ceil(min(a,b)/2)` | `KILL_ONION/ADJUNCTION_OWNER` |
| 13 | `RSK` | replace a permutation by the bottom-to-top row word of its insertion tableau | idempotent, tableau-resolved image | `KILL_RSK/ONE_STEP` |
| 14 | `MGB` | ordered matroid fundamental-circuit exchange toward the greedy basis | tail equals missing target-basis elements | `KILL_RADO–EDMONDS/PERMANENT_MATROID_EXCLUSION` |

The exact replay covers 180 boxes and 3,998,688 assertions.  The full stdout is
frozen in `CANONICAL.txt`.

## 1. `WEX`: weak-excedance extraction

### Literal map

For `pi=pi_1...pi_n in S_n`, let

```text
W(pi) = std(pi_i : pi_i >= i),
```

where retained entries keep their left-to-right order.  Position one is always
retained, so this is a self-map of `S_{<=N}=disjoint_union_{1<=n<=N} S_n`.
Put

```text
d(sigma)=max_i(i-sigma_i),
```

with `d(id)=0`.  This is the classical maximum-drop statistic; all known static
results about weak excedances or maximum drop receive zero contribution credit.

### Exact early profile

Full enumeration through rank nine gives

```text
max tail:   0,1,2,2,3,3,3,4,4
image size: 1,2,4,8,18,44,120,356,1152
fixed:      exactly id_n at every tested rank.
```

The first sharp witnesses are

```text
w_0 = 1
w_1 = 21
w_2 = 321
w_3 = 54312
w_4 = 87645123
w_5 = 13,12,11,9,10,6,7,8,1,2,3,4,5.
```

Their ranks are `1,2,3,5,8,13`, their maximum drops are
`0,1,2,3,5,8`, and their tails are `0,1,2,3,4,5`.

### Theorem axis A: all-rank image and right section — proved

For `sigma in S_m` and `n>=m`,

```text
sigma in W(S_n)  iff  m+d(sigma) <= n.                    (1)
```

Write the selected source values as `a_1<...<a_m` and their positions as
`p_1<...<p_m`.  Since there are `n-m` unselected values,
`a_j <= n-m+j`.  Weak excedance of the entry representing `sigma_i` gives

```text
i <= p_i <= a_{sigma_i} <= n-m+sigma_i,
```

which proves necessity.  Conversely, for `h=n-m>=d(sigma)`, the explicit
right section

```text
R_n(sigma)=(sigma_1+h,...,sigma_m+h,1,2,...,h)             (2)
```

satisfies `W(R_n(sigma))=sigma`.  Thus the minimum source rank is exactly
`m+d(sigma)`, not just bounded by it.

### Theorem axis B: every-target fibres — proved

Fix `sigma in S_m`, source rank `n`, and `h=n-m`.  For increasing selected
value and position sets

```text
A={a_1<...<a_m},  P={p_1<...<p_m},
```

require `p_i <= a_{sigma_i}`.  Put `B=[n]\A` and
`Q=[n]\P={q_1<...<q_h}`.  The selected assignment is forced, while every
unselected source entry must be deficient.  The number of complement
bijections `B -> Q` is therefore

```text
prod_{j=1}^h ( #{b in B:b<q_j}-(j-1) ),                  (3)
```

interpreted as zero when a factor is nonpositive.  Summing (3) over all
admissible `A,P` is the exact fibre `|W_n^{-1}(sigma)|`.  This is a
target-resolved Ferrers-board matching formula, not merely an aggregate
Eulerian count.  The verifier independently compares (3) with literal source
enumeration for all targets through source rank seven: 6,985 target/rank
checks, including zero fibres.

### Theorem axis C: Fibonacci pointwise clock — proof-gated contract

The intended sharp statement is

```text
tau(pi)>=t  =>  |pi|>=F_{t+2} and d(pi)>=F_{t+1};          (4)
max_{pi in S_n} tau(pi)=max{t:F_{t+2}<=n}.                (5)
```

The section (2) gives equality witnesses recursively:

```text
w_{t+1}=R_{|w_t|+d(w_t)}(w_t).
```

The upper bound has one explicit proof gate, rather than an enumeration claim.

> **Drop-compression lemma.** If `D=d(pi)`, then
> `tau(W(pi)) <= max_{rho in S_D} tau(rho)`, with the right side zero for
> `D=0`.

Once this lemma is proved, (4)–(5) follow simultaneously by induction.  Indeed,
for `q=W(pi)` the exact image theorem gives
`|pi|>=|q|+d(q)`; the compression lemma gives the required lower bound on
`d(pi)`.  The planned proof exposes the permutation plot through the `D` lower
diagonals and compresses its active rank-defect skeleton to `D` points; the
induced skeleton map must semiconjugate all nonidentity `W`-layers.  This is the
only unclosed deductive step.  It is an **exact falsifier**, not a phrase-level
promise: the verifier checks it pointwise for every permutation through rank
nine, in addition to (4).

Accordingly `WEX` may be frozen only after a written proof of the
drop-compression lemma.  Axes A and B do not depend on that lemma and are
already deductive.

### Separation from P149

The shared fact “retain a subsequence and standardize” receives zero credit.
The residual proof engines are different.

| interface | P149 endpoint-peak extraction | `WEX` |
|---|---|---|
| selector | endpoint-inclusive local maxima | absolute diagonal test `pi_i>=i` |
| one-step obstruction | peak packing / alternating slots | target maximum drop `d(sigma)` |
| right section | alternating high/low peak carrier | high-shift target followed by a deficient low tail |
| fibres | zigzag/peak-position constraints and pinnacle subtraction | Ferrers-board deficient completions (3) |
| clock engine | repeated local peak packing | two-resource rank/drop compression with Fibonacci thresholds |

Thus a proof imported from P149 cannot establish (1), (3), or the proposed
drop-compression lemma.  Owner search must nevertheless retain a medium
carrier-level collision warning because both maps live on rank-varying
permutations.

### Owner subtraction and disposition

Ehrenborg–Steingrímsson own excedance-set enumeration.  Chung–Claesson–Dukes–
Graham and Chen–Chen own bounded-maxdrop enumeration and its bubble-sort
connections.  Bergeron owns recent weak-excedance/Bruhat class structure.
These inputs receive zero credit.  The bounded exact-map searches listed in
`OWNER_AUDIT.md` did not retrieve the literal iterated retain-and-standardize
map, its all-rank image (1), or target fibres (3).  A non-hit is not novelty
evidence.

**Verdict:** `SELECT_INTERNAL_PROOF_GATE`.  Residual package if and only if the
clock lemma closes: sharp Fibonacci clock + exact all-rank images/right sections
+ every-target fibres.  Otherwise downgrade to `RESERVE`; do not publish axes A
and B alone merely to fill a slot.

## 2. `UHC`: strict upper-hull extraction

### Literal map and exact profile

Plot `(i,pi_i)`.  Scan left to right with the strict upper monotone-chain rule,
deleting the middle point whenever the cross product is nonnegative (collinear
middle points are deleted).  Read the retained heights and standardize.

Through rank nine:

```text
max tail:   0,0,1,2,2,3,3,4,4
image size: 1,2,4,8,14,22,30,50,84
fixed count:1,2,2,2,0,0,0,0,0.
```

The fixed permutations are `1`; both rank-two permutations;
`132,231`; and `1342,2431`.  A fixed permutation has strictly decreasing
consecutive slopes.  Triangular lower bounds on total ascent and descent rule
out all sufficiently large ranks, with the remaining ranks handled directly.
Every nonfixed step strictly drops rank, so there are no other cycles.

For a target `sigma`, choose prospective hull abscissae `P`, ordinate set `A`,
and require their segment slopes to decrease strictly in the order pattern
`sigma`.  Every unused row/column point must lie on or below the resulting cap.
The complement count is the permanent of that cap board.  Summing over `A,P`
is an exact target-resolved fibre formula and gives an integer-lift image
criterion.

### Why it is not selected

The observed clock has no proved all-parameter formula or equally strong
second temporal axis.  The initial guess `floor(n/2)` was already falsified at
rank ten: the exact maximum there is four, not five.  Static convex/unimodal
permutation realization is also mature and must be subtracted.  A generic
permanent sum plus finite fixed list is below the batch threshold without a
sharp clock.

**Verdict:** `RESERVE_NO_SHARP_CLOCK`; no second survivor from this lane.

## 3–14. Kill ledger with exact small data

### `TFE` — root-frontier fanization

In a rooted convex `n`-gon, consecutive current root neighbours `a<b` expose a
frontier diagonal `(a,b)` and its unique opposite triangle vertex `c`.  Flip the
smallest such `c` from `(a,b)` to `(0,c)`.  For `n=3,...,10`, the exact state,
one-step image, and maximum-tail triples are

```text
(1,1,0),(2,1,1),(5,3,2),(14,9,3),(42,28,4),
(132,90,5),(429,297,6),(1430,1001,7).
```

Every step adds one root diagonal, so the tail is exactly the number missing
from the fan; the depth layers are the Catalan root-degree triangle.  This is
precisely the classical flip-to-fan connectivity invariant, and under the
tree/triangulation dictionary it is a directed reassociation neighbour of
P144.  `KILL_DIRECT_FAN_FLIP/P144`.

### `DSE` — Dyck shell erasure

Delete the first `U` and matching final `D` from every primitive excursion and
concatenate the interiors.  Exhaustive Catalan boxes through semilength nine
give maximum tails `0,1,...,9`; pointwise tail is exactly path height.  This is
simultaneous deletion of tree roots, transferring directly from occupied tree
peeling/contraction mechanisms (P114/P144/P148).  `KILL_INTERNAL_TRANSFER`.

### `NCK` — noncrossing Kreweras complement

Represent a noncrossing partition by its block-cycle permutation `p` and map it
to the cycles of `p^{-1}(1 2 ... n)`.  Catalan state counts through `n=7` are
`1,2,5,14,42,132,429`; all observed periods divide `2n`, with complete period
censuses frozen in `CANONICAL.txt`.  Kreweras complementation and its orbits are
the direct subject of the retrieved literature.  `KILL_DIRECT_OWNER`.

### `RSP` — rectangular tableau promotion

Apply jeu-de-taquin promotion to `2 x b` standard Young tableaux.  For
`b=1,2,3,4`, the state/period censuses are

```text
1:{1:1}; 2:{2:2}; 5:{2:2,3:3}; 14:{2:2,4:4,8:8}.
```

Rectangular promotion order and cyclic sieving are directly owned.
`KILL_DIRECT_OWNER`.

### `BPC` — boxed plane-partition complementation

Map `P_{ij}` in an `a x b x c` box to
`c-P_{a+1-i,b+1-j}`.  It is an involution and pairs volumes to `abc`.  Tested
boxes `(1,3,3),(2,2,2),(2,2,3),(2,3,2)` have respectively
`20,20,50,50` states and `0,4,6,6` fixed points.  Complementation and its
symmetry classes are directly owned; the temporal statement is only an
involution.  `KILL_DIRECT_OWNER/ONE_STEP`.

### `LDL` — lex Delaunay legalization

On a fixed generic planar point set, flip the lexicographically first illegal
interior edge.  The integer quadrilateral
`(0,0),(4,0),(5,3),(0,2)` has two triangulations: diagonal `02` feeds the legal
diagonal `13`, which is fixed.  Lawson-style illegal-edge flipping already owns
the algorithm and termination.  `KILL_LAWSON_ALGORITHM`.

### `LSC` — lex elementary collapse

Choose the lexicographically first codimension-one free face and delete its
unique elementary-collapse interval.  Five exact sample complexes have tails
`3,5,0,5,7`; the 3-cycle is a fixed noncollapsible example.  Lex-first/last
collapse strategies and their discrete-Morse behaviour are directly studied;
the scheduler leaves no independent theorem package.  `KILL_DIRECT_OWNER`.

### `G2C` — synchronous 2-core peeling

Delete all vertices of current degree below two and relabel the induced graph.
All labeled graphs through six vertices have maximum tails
`0,1,1,2,2,3,3`; the terminal object is the 2-core.  This is exactly core
decomposition/peeling, an explicit permanent exclusion.  `KILL_DIRECT_OWNER`.

### `OIR` — order-ideal rowmotion

Send an ideal to the ideal generated by the minimal elements of its complement.
For rectangles `(1,4),(2,2),(2,3),(3,3)`, exact state counts are `5,6,10,20`
and all periods divide `a+b`.  Promotion/rowmotion on rectangles is a mature
directly owned action.  `KILL_DIRECT_OWNER`.

### `PLA` — lattice-polygon adjunction

Replace a lattice polygon by the convex hull of its interior lattice points,
with a lower-dimensional hull terminal.  On all axis rectangles with side
lengths at most ten, 100 exact boxes give tail
`ceil(min(a,b)/2)` and maximum five.  This is convex-layer/adjunction peeling,
colliding with the classical onion-decomposition owner surface and root-lane
negative control R06.  `KILL_OWNER/INTERNAL_COLLISION`.

### `RSK` — insertion-tableau row-word canonicalization

Apply RSK insertion and return the bottom-to-top row word of `P`.  It is
idempotent because that reading word reinserts to `P`.  Image counts through
rank seven are `1,2,4,10,26,76,232`.  This is a one-step canonical section of
classical RSK, not a temporal advance.  `KILL_RSK/ONE_STEP`.

### `MGB` — greedy graphic-matroid basis exchange

For a spanning tree of `K_n`, add the smallest missing edge of the lexicographic
target tree and remove the largest nontarget edge in its fundamental cycle.
Each step gains exactly one target edge, so the tail is the number missing.
For `n=2,...,6`, tree counts are `1,3,16,125,1296` and one-step image counts
are `1,1,5,34,307`.  This is the Rado–Edmonds greedy basis theorem written as a
dynamics and also violates the permanent matroid exclusion.  `KILL_DIRECT_OWNER`.

## Replay and limits

- `verify_combinatorial_scout.py` constructs all fourteen literal maps and
  checks the profiles without loading predicted graph tables.
- `CANONICAL.txt` is its exact frozen stdout.
- Computation supplies falsification pressure only.  In particular the WEX
  Fibonacci upper bound is not promoted to a theorem until the named
  drop-compression lemma is written deductively.
- Owner-search non-hits are bounded search results, never novelty, priority,
  authorship, or external-release claims.
- External state remains `HOLD_EXTERNAL`; no paper number is allocated here.
