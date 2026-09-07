# Combinatorial / graph / order / partition / word-dynamics scout for P112--P116

**Historical provenance:** this is a Stage-1 scouting record.  Post-review
claim and ownership boundaries in each paper-local consolidated
`HOSTILE_REVIEW.md`, `CLAIMS_EVIDENCE.md`, and `FINAL_QA.md` are authoritative.

**Status:** scouting evidence only.  External posting, submission, specialist
contact, priority, authorship, and venue decisions remain **HOLD**.  This file
assigns no final paper number and makes no absolute novelty claim.

**Evidence cutoff:** 2026-08-29.  The P1--P111 tree was read only.  New exact
programs made by this scout have the required `combinatorial_` prefix and live
only under `scouting/code/`.

## 1. Executive decision

Two systems merit passage to a theorem-contract / deeper-owner stage.

1. **GO, owner-gated: synchronous tournament score-upset reversal.**  In a
   labelled tournament, simultaneously correct every result in which a
   lower-outdegree vertex beats a higher-outdegree vertex, retaining ties.
   The first spike found a strict quadratic Lyapunov function, a recursive
   score-class decomposition, a complete fixed-point classification as
   ordered sums of regular tournaments, and an exact fixed-count recurrence.
   The tempting claim that the map is a projection fails first at order six;
   the failure exposes a nontrivial recursive transient rather than destroying
   the system.

2. **CONDITIONAL GO, unusually strict owner subtraction: principal-hook
   partition dynamics.**  Send an integer partition to the partition of the
   lengths of its principal diagonal hooks.  The one-step map, its
   Rogers--Ramanujan image, and its Frobenius-coordinate fibres are classical
   and receive zero credit.  The residual temporal signal is nevertheless
   strong: for every `n>=1`, a first-two-part gap Lyapunov function proves
   that `(n)` is globally absorbing in the finite-time sense and that the
   sharp maximum depth is `floor(n/2)`; exhaustive
   iteration through all partitions of every `n<=35` independently confirms
   strict dominance growth and the nonclosed depth-state-weighted transport
   identity.  No searched source
   stated the iterated transient package, but the background is mature enough
   that a direct temporal owner immediately kills the candidate.

The best reserve is **directed-triangle-support reversal on tournaments**.
Its directed-triangle set grows monotonically, which proves eventual period at
most two.  It cannot coexist with the score-upset system in one diversity
batch, and the triangle-inversion literature is substantial, so it remains a
replacement rather than a third GO.

The multiplicity-profile partition map was downgraded after a direct dynamics
neighbor was found.  Parallel equal-part coagulation, word eroders, KMP-border
descent, record peeling, twin quotienting, pointer doubling, and elementary
poset/partition projections are owner-dominated, theorem-thin, or internally
colliding.

## 2. Read-only P1--P111 collision boundary

The audit used the repository inventory and the frozen firewalls for the
[P92--P96](../../papers92_96_sequence/phase1/SYSTEM_COLLISION_FIREWALL.md),
[P97--P101](../../papers97_101_sequence/phase1/SYSTEM_COLLISION_FIREWALL.md),
[P102--P106](../../papers102_106_sequence/phase1/SYSTEM_COLLISION_FIREWALL.md),
and [P107--P111](../../papers107_111_sequence/phase1/SYSTEM_COLLISION_FIREWALL.md)
rounds, together with the previous
[combinatorial scout](../../papers107_111_sequence/scouting/COMBINATORIAL_SCOUT.md).
The following mechanisms were treated as occupied or expressly excluded:

- the P1--P96 symbolic/SFT/sofic/substitution/S-adic, relation/hom-shift,
  renewal/stack/reset, beta/IET, tree-shift, and cellular-automaton lanes;
- P97 sumset squaring and binary-product closure, P99 sublattice shear,
  P100 least-valuation digit erasure, and P101 random cap--floor
  synchronization;
- P102 group-algebra norm/power dynamics, P103 double adjugation, P104 random
  monomial cocycles, P105 cycle-minimum pruning, and P106 MIS polarity;
- P107 ideal annihilator--power dynamics, P108 capped Fibonacci absorption,
  P109 nilpotent-image subspaces, P110 cyclic partition shift--join, and P111
  positive Heisenberg word area; and
- prior-round kills/reserves including graph powers, rowmotion,
  promotion/0-Hecke and pop-stack sorting, noncrossing closure, blocker
  duality, chordal fill, source-to-sink reversal, lower shadows, odd--even
  comparators, line-graph iteration, cyclic gcd erosion, and degree-parity
  Seidel switching.

The two proposed GO systems clear this internal boundary for different
reasons.  The tournament rule updates edge orientations using global score
classes; its states are not independent sets and its proof is not a Galois
polarity.  The principal-hook map acts on integer partitions of a fixed
integer, preserves total weight, and regroups a Young diagram by diagonal
hooks; it neither joins translated set partitions nor closes a family under a
binary product.  Nevertheless, any replacement in either the tournament or
integer-partition family would have to displace, rather than accompany, the
selected system from that family.

## 3. Candidate ledger (13 explicit self-maps)

Here `P(n)` denotes the integer partitions of `n`, `T_n` the labelled
tournaments on `[n]`, and `W(q,N)` the words over a `q`-letter alphabet of
length at most `N`.

| ID | Finite / controlled phase and exact update | Earliest exact signal | Owner / internal risk | Decision |
|---|---|---|---|---|
| C1 | `T_n`; orient `u-v` from the larger current outdegree to the smaller, retaining the old edge on a tie | strict `sum_v s(v)^2`; recursive score-class refinement; fixed ordered regular sums | mature Copeland/tournament ranking, but no exact temporal hit; distinct from P106 | **GO OWNER-GATED** |
| C2 | `P(n)`; replace a Young diagram by its principal diagonal-hook lengths | image = gap-at-least-two partitions; gap Lyapunov; `(n)` globally absorbing in finite time for `n>=1`; proved sharp depth `floor(n/2)` | principal-hook map and fibres classical; residual iteration not located; low P110 collision | **CONDITIONAL GO** |
| C3 | `T_n`; reverse every arc belonging to at least one directed 3-cycle | cyclic-triple set is monotone, hence eventual period `<=2` | triangle inversion/interchange literature; same tournament slot as C1 | **RESERVE OWNER / BATCH COLLISION** |
| C4 | nonempty `P(<=N)`; replace a partition by the sorted nonzero multiplicities of its distinct parts | `|M(lambda)|=ell(lambda)` and `|M^2(lambda)|=#distinct(lambda)`; unique attractor `(1)` | direct multiset-description dynamics and inventory-sequence owner | **KILL DIRECT** |
| C5 | `P(n)`; replace all `m>=2` equal parts `a` simultaneously by one part `ma` | fixed iff all parts are distinct; a tracked merged mass at least doubles | 2048/equal-pile merging is mature; coarsening/closure flavor too near P110/P97 | **KILL OWNER / INTERNAL** |
| C6 | `W(q,N)`; send a word to its longest proper border, or to the empty word when unbordered | orbit is the KMP failure-link chain; depth is failure-tree height | Knuth--Morris--Pratt owns the state transition as a standard algorithm | **KILL DIRECT** |
| C7 | disjoint union of permutations of sizes `<=N`; delete all left-to-right minima and standardize | peeling depth equals a product-order height / LIS statistic; layer counts come from RSK | patience sorting/RSK direct, plus P105 deletion--standardization collision | **KILL DIRECT / INTERNAL** |
| C8 | `P(<=N)` including empty; remove the first row and first column: `E(lambda)_i=max(lambda_{i+1}-1,0)` | `E^t(lambda)_i=max(lambda_{i+t}-t,0)`; depth is Durfee size | classical Durfee-square decomposition; residual is one-line and thin | **KILL THIN** |
| C9 | weighted simple graphs of total vertex weight `n`; merge every maximal open/closed-twin class and retain the weighted quotient | vertex count strictly falls to the point-determining twin quotient | twin reduction/modular decomposition/color refinement directly own the core | **KILL DIRECT** |
| C10 | rooted functional forests on `[n]`; replace the parent map `f` by `f^2` | `F^t(f)=f^(2^t)`; depth is `ceil(log_2(height))` | pointer jumping and functional-graph power maps direct; P97/P102/P103 power motif | **KILL DIRECT / INTERNAL** |
| C11 | `W(q,N)`; for each letter retain occurrence numbers `1,3,5,...` in their old order | the `t`-th iterate retains ranks `1 mod 2^t`; depth `ceil(log_2 max multiplicity)` | almost literal digit erasure plus word pruning; P100/P105 collision | **KILL INTERNAL** |
| C12 | labelled posets on `[n]`; set `x<_{F(P)}y` iff the longest-chain height of `x` is smaller than that of `y` | one-step projection to an ordinal sum of antichains | standard rank projection and theorem-thin idempotence | **KILL THIN** |
| C13 | clutters on `[n]`; map a clutter to its family of minimal transversals | blocker is an exact involution | classical blocker duality and nearly the same polarity language as P106 | **KILL DIRECT / INTERNAL** |

Candidates C6--C13 were defined precisely enough to falsify their paper value
without spending an enumeration lane: their headline dynamics is already a
named algorithm/theory or collapses in one elementary identity.  Assertion
volume was reserved for C1--C5, where a temporal question survived the first
definition.

## 4. Exact-spike and falsification ledger

All programs use only the Python standard library.  Together they executed
**1,098,971 explicit assertions**.

| Program | Exact scope | Assertions | Surviving statements | Smallest killed overclaim |
|---|---:|---:|---|---|
| [`combinatorial_tournament_score.py`](code/combinatorial_tournament_score.py) | every labelled tournament through `n=6` | 244,904 | Lyapunov growth, score-order refinement, terminal structure, fixed recurrence | projection/idempotence fails first at `n=6`, mask `148`, scores `(2,2,2,2,3,4)` |
| [`combinatorial_diagonal_hooks.py`](code/combinatorial_diagonal_hooks.py) | every partition for each `1<=n<=35`; independent Frobenius fibre DP | 488,741 | weight, conjugation, dominance, gap growth, exact image/fibres, unique fixed point, maximum depth | idempotence fails first at `n=4`, `(2,2)->(3,1)->(4)`; simple deepest-shell boundary guess fails first at `n=16`, `(4^4)` has depth `7`, not `8` |
| [`combinatorial_triangle_support.py`](code/combinatorial_triangle_support.py) | every labelled tournament through `n=6` | 121,855 | cyclic-triple monotonicity, periods `1/2`, fixed count `n!` | global involution fails first at `n=5`, mask `10`, when cyclic triples grow `3->4` |
| [`combinatorial_partition_kills.py`](code/combinatorial_partition_kills.py) | every partition for each `1<=n<=35` for both C4 and C5 | 243,471 | exact profile weight drop; coagulation weight/fixed tests; power-of-two deepest witnesses | coagulation maximum depth is not `floor(log_2 n)`: first failure `n=5`, observed `1` versus `2` |

Representative exact C1 rows are:

| `n` | tournaments | fixed | depth histogram |
|---:|---:|---:|---|
| 4 | 64 | 40 | `{0:40,1:24}` |
| 5 | 1,024 | 264 | `{0:264,1:760}` |
| 6 | 32,768 | 2,048 | `{0:2048,1:26400,2:4320}` |

Representative exact C2 rows are:

| `n` | `p(n)` | one-step image size | maximum depth | deepest states |
|---:|---:|---:|---:|---:|
| 10 | 42 | 6 | 5 | 4 |
| 20 | 627 | 31 | 10 | 29 |
| 30 | 5,604 | 117 | 15 | 145 |
| 35 | 14,883 | 211 | 17 | 914 |

Representative exact C3 rows are:

| `n` | fixed | recurrent points | 2-cycles | depth histogram |
|---:|---:|---:|---:|---|
| 3 | 6 | 8 | 1 | `{0:8}` |
| 4 | 24 | 64 | 20 | `{0:64}` |
| 5 | 120 | 784 | 332 | `{0:784,1:240}` |
| 6 | 720 | 14,048 | 6,664 | `{0:14048,1:16560,2:2160}` |

No theorem below is inferred merely from these rows.  Proven finite identities
and infinite-family proof obligations are separated explicitly.

## 5. C1 -- synchronous tournament score-upset reversal

### 5.1 Exact system and proved structural spikes

For a tournament `T` on `[n]`, write `s_T(v)=d_T^+(v)`.  Define `F_n(T)` by

\[
 u\longrightarrow_{F_n(T)}v
 \quad\Longleftrightarrow\quad
 \begin{cases}
 s_T(u)>s_T(v),&s_T(u)\ne s_T(v),\\
 u\longrightarrow_Tv,&s_T(u)=s_T(v).
 \end{cases}
\]

Thus every score upset is corrected synchronously, while an edge inside a
score tie is retained.

Let `R(T)` be the corrected arcs, oriented in `T` from a lower score `x` to a
higher score `y`, and let `delta_v=s_{F(T)}(v)-s_T(v)`.  Literal expansion gives

\[
 \sum_v s_{F(T)}(v)^2-\sum_v s_T(v)^2
 =2\sum_{(x\to y)\in R(T)}(s_T(y)-s_T(x))
  +\sum_v\delta_v^2>0                                             \tag{C1.1}
\]

whenever `F(T) != T`.  Hence there are no nontrivial cycles.

More structure is visible than the Lyapunov argument alone.  Partition the
vertices into equal-score classes and order those classes by decreasing score.
Then

\[
 F(T)=T[C_1]\oplus T[C_2]\oplus\cdots\oplus T[C_k],                \tag{C1.2}
\]

the ordinal sum of the *unchanged induced subtournaments* on those classes.
The score intervals of successive blocks are disjoint, so all later updates
factor inside the blocks.  Iteration is therefore recursive score-class
refinement, not ordinary sorting.

A tournament is fixed exactly when it is an ordered sum of regular
tournaments.  If `r_j` is the number of labelled regular tournaments on `j`
vertices (`r_j=0` for positive even `j`) and `f_n` is the number of fixed
points, uniqueness of the top block gives

\[
 f_0=1,\qquad
 f_n=\sum_{\substack{1\le j\le n\\j\text{ odd}}}
      \binom nj r_j f_{n-j}.                                      \tag{C1.3}
\]

The exact values `f_1,...,f_6` are `1,2,8,40,264,2048`.  Since all recurrence
is fixed, the finite dynamical zeta function is

\[
                 \zeta_{F_n}(z)=(1-z)^{-f_n}.                     \tag{C1.4}
\]

The first nonprojection is scientifically useful: at `n=6`, mask `148` has
score vector `(2,2,2,2,3,4)` and needs two updates.  Thus (C1.2) really creates
nested score refinement; it is not a disguised one-pass Copeland ranking.

### 5.2 Five-item theorem contract

All five items below are consequences of the proved spike in Section 5.1;
the contract asks for full formalization, not extrapolation from `n<=6`.

1. **Strict Lyapunov theorem.**  Prove the exact energy identity (C1.1) and
   deduce that every periodic point is fixed.
2. **Recursive iterate theorem.**  Prove (C1.2), preservation of strict order
   between old score classes, factorization of every later iterate, and the
   pointwise description by the recursive score-refinement tree.
3. **Uniform absorption theorem.**  Show that after the initial ordinal-sum
   update, every further nonterminal step strictly refines at least one score
   class.  This gives the structural bound `tau(T)<=n-1`, independently of
   the numerical energy range.
4. **Fixed-block census.**  Classify fixed tournaments as unique ordered sums
   of regular blocks and prove (C1.3).  Refined by the number `k` of blocks,
   the exponential generating function is `1/(1-yR(x))`, with the coefficient
   for an odd composition `(j_1,...,j_k)` given by the corresponding labelled
   multinomial product of the `r_{j_i}`.
5. **Periodic census and zeta.**  Combine item 1 with item 4 to prove
   `#Fix(F_n^m)=f_n` for every `m>=1` and hence (C1.4).  This explicitly rules
   out treating the fixed recurrence as evidence for an unproved transient
   enumerator or sharp-depth formula.

### 5.3 Two materially different proof/control routes

**Route A -- ordinal-sum recursion.**  Work with equal-score blocks.  The wins
against all lower blocks give disjoint integer score intervals, so old strict
score order can never collapse.  This proves the recursive decomposition,
the refinement absorption bound, fixed classification, and block-refined
enumeration.

**Route B -- energy and score-sequence geometry.**  Prove convergence from the
quadratic energy (C1.1), then use tournament score-sequence identities to
recover the regularity of an equal-score fixed block.  This route does not
assume the recursive functional-graph conclusion; it independently excludes
cycles and feeds the periodic-point/zeta calculation.

**Independent exact control.**  Bit-coded tournaments are exhaustively
enumerated, while the predicted fixed counts are computed separately from
regular-tournament counts and recurrence (C1.3).  Every transition is checked
for energy growth and strict score-order preservation.  The smallest failure
of idempotence is searched rather than supplied to the script.

### 5.4 Owner and internal-collision gate

Searches for “tournament dynamics reverse every upset edge according to
outdegree,” “orient edge from higher score to lower score iteration,”
“Copeland dynamics tournament edge reversal,” and “score classes tournament
ordinal sum regular” found extensive score-ranking background, including
[Monsuur's characterization of Copeland inconsistency measures](https://doi.org/10.1016/j.ejor.2003.09.032),
but no source in the bounded result set defining `F_n` or proving the temporal
package (C1.1)--(C1.4).  Absence from these queries is not novelty evidence.

Internal risk is controlled but nonzero.  The adaptive global score resembles
ranking, yet the map is not a comparator network, 0-Hecke action, or sorting
projection: regular cyclic blocks remain fixed.  P106 evolves subsets of a
fixed graph by an antitone MIS polarity; C1 evolves every edge of a tournament
and is controlled by score intervals and ordinal sums.  Kill C1 if an exact
score-reversal owner or an equivalent iterative Copeland correction is found.

## 6. C2 -- principal-hook partition dynamics

### 6.1 Exact system and zero-credit classical layer

For `lambda=(lambda_1>=lambda_2>=...)` in `P(n)`, let `d(lambda)` be its
Durfee size and define

\[
 H(\lambda)=\bigl(h_{11}(\lambda),h_{22}(\lambda),\ldots,
 h_{d(\lambda)d(\lambda)}(\lambda)\bigr),\qquad
 h_{ii}=\lambda_i+\lambda'_i-2i+1.                               \tag{C2.1}
\]

The principal diagonal hooks partition the Young diagram, so `H` is a
self-map of `P(n)`.  The parts of `H(lambda)` differ successively by at least
two.  Conversely every such partition is a principal-hook type.  If
`h=(h_1>...>h_r)` has gaps at least two, its exact fibre is

\[
 \#H^{-1}(h)=h_r\prod_{i=1}^{r-1}(h_i-h_{i+1}-1),                \tag{C2.2}
\]

equivalently the number of strict Frobenius arm/leg splittings
`a_i+b_i+1=h_i`.  These facts are owned background and are not proposed as
new.  Gutschwager owns the principal-hook partition object and first-hook
identity (DOI `10.1007/s00026-011-0084-7`).  In particular, the hook-type product formula already appears in
[Goupil, *A product of integer partitions*](https://arxiv.org/abs/0906.3004),
and principal/diagonal-hook statistics have a broad literature, including
[Chern--Yee, *Diagonal hooks and a Schmidt-type partition identity*](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v29i2p10/pdf/).

### 6.2 Residual temporal signal

The first part obeys

\[
              H(\lambda)_1=\lambda_1+\ell(\lambda)-1.           \tag{C2.3}
\]

There is a sharper temporal potential.  Put

\[
      g(\lambda)=\lambda_1-\lambda_2,\qquad \lambda_2:=0
      \text{ when }\ell(\lambda)=1.                              \tag{C2.4}
\]

If the Durfee size is at least two, subtracting the first two diagonal-hook
lengths gives

\[
 g(H(\lambda))-g(\lambda)
   =\ell(\lambda)-\lambda'_2+2
   =m_1(\lambda)+2\ge2,                                         \tag{C2.5}
\]

where `m_1(lambda)` is the number of parts equal to one.  If the Durfee size
is one and `lambda!=(n)`, write `lambda=(a,1^b)` with `b>=1`; then
`H(lambda)=(n)` and the same gap increase is `b+1>=2`.  Thus every nonterminal
step raises `g` by at least two, while `g((n))=n`.  This proves, for every
partition rather than only in the finite lanes,

\[
 \tau(\lambda)\le
 \left\lfloor\frac{n-g(\lambda)}2\right\rfloor
 \le\left\lfloor\frac n2\right\rfloor.                          \tag{C2.6}
\]

For the balanced two-row partition
`lambda=(ceil(n/2),floor(n/2))`, the update is
`H(a,b)=(a+1,b-1)` while `b>=2`, followed by `(n-1,1)->(n)`.
It takes exactly `floor(n/2)` steps, so the global bound in (C2.6) is sharp.

Also `H(lambda)=H(lambda')`, hence `H^t(lambda)=H^t(lambda')` for every
`t>=1`.  Entrance depth is conjugation-invariant except for the unique pair
`(n),(1^n)` when `n>1`, whose depths are respectively zero and one.  This
one-step symmetry is zero-credit diagonal-hook background.  The exhaustive
spike verifies the stronger dominance relation
`H(lambda) >=_dom lambda` through `n=35`.  The gap proof
already gives the unique fixed point `(n)` and full convergence, hence

\[
                    \zeta_{H|P(n)}(z)=(1-z)^{-1}.                \tag{C2.7}
\]

In particular,

\[
                  \max_{\lambda\vdash n}\tau(\lambda)
                  =\left\lfloor\frac n2\right\rfloor.           \tag{C2.8}
\]

The independent fibre DP also yields an exact depth-state-weighted transport
identity.  If
`A_t(n)=\#\{\lambda\vdash n:\tau(\lambda)=t\}`, then `A_0(n)=1`,
`A_1(n)=n-1`, and for
`t>=2`,

\[
 A_t(n)=\sum_{\substack{h\vdash n,\ h_i-h_{i+1}\ge2\\
                         \tau(h)=t-1}}
          h_r\prod_{i<r}(h_i-h_{i+1}-1).                         \tag{C2.9}
\]

Equation (C2.9) exactly reproduces the stored depth histograms, but it is not
a closed scalar recurrence in the numbers `A_t(n)` alone: it retains the
depth of each image state.  A naive
deepest-shell characterization (“two equal top rows and no row of length
one” for even size) survives through `n=15` but fails minimally at
`lambda=(4,4,4,4)` for `n=16`; any proof must use the full iterated hook
geometry.

### 6.3 Historical five-item scouting proposal -- not retained as the frozen contract

The following was the exploratory contract before hostile review.  Items 4
and 5 were not retained, and item 3 was narrowed to a nonclosed,
depth-state-weighted transport identity.  The authoritative residual main
result is only the exact gap increment, pointwise depth bound, and sharp
global depth theorem.

1. **Temporal collapse theorem.**  Treat the classical hook-type facts as
   lemmas, then promote the gap calculation (C2.5) to a formal proof of unique
   attraction, full recurrent classification, and (C2.7).
2. **Sharp depth theorem.**  Formalize (C2.6)--(C2.8), including equality for
   every balanced two-row witness and, if possible, classify equality in the
   pointwise gap bound.
3. **Fibre-weighted layer transport.**  Prove (C2.9), explicitly without
   calling it a closed scalar recurrence, give a finite dynamic program with
   complexity bounds, and tabulate exact layers independently of functional
   orbit enumeration.
4. **Fixed-depth formulas.**  Derive closed generating functions (or eventual
   quasipolynomials) for each fixed transient layer.  The spike already gives
   `A_1(n)=n-1` and `A_2(n)=n-3` in their valid ranges; higher layers must be
   derived, not curve-fit.
5. **Deepest-shell theorem.**  Characterize or recursively enumerate the
   partitions attaining `floor(n/2)`, provide their ordinary generating
   function and asymptotic bounds, and explicitly explain the minimal
   `(4^4)` failure of the first boundary-only guess.

### 6.4 Two materially different proof/control routes

**Route A -- Frobenius coordinates and fibre transfer.**  Split every
principal hook into strict arm and leg sequences.  This proves the classical
kernel (C2.2) and turns temporal layers into the exact weighted transfer
(C2.9).  A transfer-matrix or `q`-series treatment can attack fixed-depth and
deepest-shell enumeration.

**Route B -- first-gap / Ferrers geometry.**  View `H` as regrouping the cells
into nested principal hooks.  Comparing the first two hooks gives the exact
increment (C2.5), proving convergence and sharp depth without fibre
enumeration.  Conjugation symmetry and dominance provide further geometric
control but are not needed to infer the depth theorem from finite data.

**Independent exact control.**  One implementation enumerates all integer
partitions and literal functional orbits.  A separate Frobenius arm/leg DP
counts every one-step fibre and is compared target by target, while image
surjectivity is checked against independently enumerated gap-at-least-two
partitions.  The script actively searches both minimal counterexamples quoted
above.

### 6.5 Owner and internal-collision gate

Queries for “iterate diagonal hook lengths integer partition dynamics,” “map
partition to diagonal hook lengths iteration,” “principal hook partition
iteration,” “hook type partition dynamics,” and an exact
“`lambda_1-lambda_2` principal hook” gap query located the mature one-step
theory but no exact temporal analysis in the bounded result set.  The map
itself is standard enough to be called the *principal hook partition* in the
representation-theory literature; this is the dominant risk, not a footnote.

The residual claim must therefore be limited to the exact gap increment
(C2.5), its pointwise depth bound, and sharp global depth (C2.8).  The map,
image/fibre characterization, absorption, nonclosed layer transport,
conjugation timing, and zeta receive zero or low credit.  A direct source for
that gap/depth package changes the decision to `STOP_DUPLICATE`.  Internally, C2 is separated
from P110: P110 joins translates of an equivalence relation on a labelled
cyclic ground set, whereas C2 preserves integer weight and regroups a Ferrers
diagram; there is no lattice join, cyclic action, or Bell/Möbius basin engine.

## 7. C3 -- directed-triangle-support reversal (reserve)

For a tournament `T`, let `C(T)` be its directed 3-cycles and let `E_C(T)` be
the union of their arcs.  Define

\[
                 Q(T)=T\triangle E_C(T),                         \tag{C3.1}
\]

i.e. reverse every arc lying in at least one directed triangle.  Every old
directed triangle has all three arcs reversed, so it remains directed.  Hence

\[
                    C(T)\subseteq C(Q(T)).                        \tag{C3.2}
\]

Once the finite set `C(T)` stabilizes, the same support is reversed on every
step and `Q^2(T)=T`.  Thus every orbit is eventually fixed or two-periodic.
Fixed points contain no directed triangle and are exactly the `n!` transitive
tournaments.

The smallest failure of a global involution occurs at `n=5`, mask `10`, where
the cyclic-triple count grows from three to four.  That failure creates the
transient problem.  A possible contract would classify stable cyclic-triple
supports, count the 2-cycles, and determine sharp closure time.  The current
data give maximum depths `0,0,1,2` for `n=3,4,5,6`.

Owner risk is material.  Reversing a single directed triangle is the standard
interchange move on fixed-score tournaments; see the modern account in
[*Coxeter Interchange Graphs*](https://doi.org/10.1007/s00026-025-00768-9).
Searches for the simultaneous union-support update found no exact hit, but
triangle inversions and feedback-arc operations are mature.  More
importantly, C3 and C1 share phase space and synchronous edge-reversal
language.  Keep C3 only as a replacement if C1 fails its owner/depth gate.

## 8. Direct-owner kills and reserves

### C4 -- multiplicity profile: direct dynamics neighbor

The map `lambda -> sorted(nonzero multiplicities of lambda)` has clean
double-logarithmic weight contraction and unusually deep minimal examples:
the first orders supporting depths `0,...,7` are
`1,2,2,3,4,7,14,42`.  This signal is not enough.  Eliahou and Erickson's
[*Mutually describing multisets and integer partitions*](https://doi.org/10.1016/j.disc.2012.11.014)
explicitly studies iteration of a multiplicity-description map and a related
integer-partition dynamical system.  The exact formal map would require
full-text comparison, but this is already a direct enough owner neighborhood
to kill C4 before theorem investment.

### C5 -- parallel equal-part coagulation: owner/internal kill

If a part `a` has multiplicity `m`, replace its entire parallel class by the
single part `ma`.  Fixed states are distinct-part partitions and the depth is
at most `floor(log_2 n)` because every followed cluster at least doubles.
Equality is attained uniquely at powers of two by the collision chain
`(2^(k-1),...,2,1,1)`, but the exact-order maximum is nonmonotone: `n=5` is the
first counterexample to equality.  Equal-tile merging is the central mature
2048 mechanism, and the map is a partition coarsening too close in proof shape
to the closure/shift--join firewall.  Kill rather than rebrand a game rule.

### C6--C13 -- immediate kills

- C6 is precisely descent along string failure links; the border chain is an
  implementation of the KMP prefix-function tree.
- C7 repackages Pareto-layer peeling/patience sorting/RSK and repeats P105's
  deletion--standardization architecture.
- C8 is just successive removal of the outer row and column; the Durfee depth
  and its generating function are standard, leaving no residual temporal
  theorem.
- C9 is iterative twin reduction / point-determining quotienting, adjacent to
  modular decomposition and color refinement.
- C10 is pointer jumping `f -> f^2`, a textbook parallel algorithm and another
  occupied power-map functional graph.
- C11 is a base-two occurrence-rank eraser; its exact iterate advertises the
  P100/P105 collision rather than curing it.
- C12 is a one-step rank projection of a poset, too thin even without an owner.
- C13 is classical blocker involution and directly violates the P106 polarity
  firewall.

## 9. Bounded owner-search log

This was an owner search, not a claim of novelty.  The query families and
their consequences were:

| Candidate | Representative queries | Closest located material | Consequence |
|---|---|---|---|
| C1 | `tournament dynamics reverse every upset edge according to outdegree`; `orient edge from higher score vertex to lower score iteration`; `Copeland dynamics tournament edge reversal`; `score classes tournament ordinal sum regular` | Copeland ranking/inconsistency, feedback-arc reversal, classical score sequences | no exact update/package located; **medium owner risk** |
| C2 | `iterate diagonal hook lengths integer partition dynamics`; `principal hook partition iteration`; `hook type partition dynamics`; exact first-gap formula vocabulary | principal-hook partitions, hook-type product fibres, diagonal-hook identities, Rogers--Ramanujan partitions | one-step layer directly owned; temporal delta only; **medium-high risk** |
| C3 | `reverse all arcs contained in directed triangles simultaneously dynamics`; `directed triangles tournament simultaneously reverse arcs` | triangle interchange/inversion and feedback-arc literature | no union-support temporal hit; **medium-high risk** |
| C4 | `map sends a partition to partition of nonzero multiplicities`; `frequency of frequencies integer partition dynamics`; `inventory loops partitions` | Eliahou--Erickson 2013 exact neighboring dynamics | **direct-neighbor kill** |
| C5 | `integer partition merge all equal parts simultaneously`; `parallel equal-size coalescence`; `partition 2048 merge` | equal-pile/2048 and partition-dynamics literature | **mature-mechanism kill** |

Search-result absence is never recorded as `novel`.  For C1 and C2 the next
gate must search MathSciNet/zbMATH/full text by the exact update, not only title
and abstract vocabulary.  C2 in particular should be killed if the principal
hook literature already treats iteration under another name.

## 10. Recommended retention and stop rules

### Retain C1 if and only if

- no exact iterative Copeland/score-correction owner is found;
- the recursive score-class factorization and `n-1` absorption bound survive
  formal review;
- the block-refined fixed census is not already implicit in the closest owner;
  and
- the two proof routes remain genuinely independent.

**Fast stop:** a source defining the same simultaneous edge correction, or a
finding that the regular-block census is standard under another formulation,
reduces C1 to a short note and removes it from the five-paper pool.  No sharp
depth or full transient enumerator is claimed at this scouting gate.

### Retain C2 if and only if

- all one-step hook/image/fibre facts are explicitly credited as classical;
- no temporal owner for repeated principal-hook partitions is found;
- the first-gap proof of (C2.5)--(C2.8) survives formal review; and
- the exact gap increment, pointwise depth bound, and balanced-two-row
  sharpness survive hostile proof review.

**Fast stop:** discovery of an iterated principal-hook paper, a flaw in the
gap calculation, or inability to extract a temporal result beyond the sharp
depth theorem kills the candidate.

### Batch separation certificate

| axis | C1 | C2 |
|---|---|---|
| phase | labelled tournament orientations | integer partitions / Young diagrams |
| update | adaptive global edge reorientation from outdegrees | regroup cells by principal diagonal hooks |
| headline | recursive score classes, regular-block fixed census, transient height | hook-iteration depth and exact transient layers |
| proof engine A | ordinal sums and score intervals | Frobenius fibre transfer |
| proof engine B | quadratic Lyapunov plus Landau score geometry | Ferrers dominance and boundary amortization |

The pair therefore passes the internal diversity test.  They remain anonymous
candidate systems under external **HOLD**; neither is assigned a P112--P116
slot by this scout.
