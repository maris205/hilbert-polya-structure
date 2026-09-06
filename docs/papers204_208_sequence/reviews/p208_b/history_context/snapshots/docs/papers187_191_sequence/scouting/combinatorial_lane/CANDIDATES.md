# P187--P191 combinatorial breadth slate

Status: frozen scouting denominator; no paper number is assigned here.

## Scope and collision rule

The denominator is exactly the 21 systems `C01`--`C21` below.  They span six
literal carriers: permutations, words, set partitions, labelled posets,
compositions, and integer partitions.  The carrier parameter is always
positive.  The last six systems are a replacement pass added after the
central-history audit killed two provisional survivors.  We first compared
the literal updates and proof engines against the P1--P186 directory titles,
the batch historical seed, and the recent combinatorial collision/kill ledgers.
In particular, the occupied neighborhood includes P110, P126, P147,
P167--P169, P176, P179, P181, and P185--P186.  A familiar statistic, a generic
finite-map invariant, or a second presentation of the same update earns no
separation credit.

For a map `F` on a finite carrier, tail means the least `h >= 0` for which
`F^h(x)` is recurrent.  Image and fibres refer to the one-step map unless a
time `t` is displayed.  All displayed pilot counts are exhaustive in the
listed boxes, but are not proofs outside them.

## Permutations

### C01_ACTR -- anchored cycle-tail rotation

- Carrier: `S_n`, exhaustively tested for `1 <= n <= 7`, with labels
  `{0,...,n-1}`.
- Literal update: write each cycle uniquely as
  `(a_0,a_1,...,a_{ell-1})`, where `a_0` is its minimum and
  `pi(a_j)=a_{j+1 mod ell}`.  For `ell >= 3`, replace it by
  `(a_0,a_2,...,a_{ell-1},a_1)`; leave cycles of length one or two unchanged.
  Do this independently in every cycle.
- Small-case signal: at `n=7`, all 5,040 states are recurrent, every fibre has
  size one, there are 232 fixed points, and periods `1,2,3,4,5,6` occur.
- Prospective axes: cycle-length period lcm and fixed-cycle enumeration; there
  is no nontrivial inverse/fibre axis.

### C02_MCP -- minimum-cycle powering

- Carrier: `S_n`, exhaustively tested for `1 <= n <= 7`.
- Literal update: on every old cycle `C`, set
  `F(pi)(x)=pi^(1+min C)(x)` for every `x in C`.  The power may split `C`.
- Small-case signal: at `n=7`, image 3,515, recurrent set 3,327, maximum tail
  two, and recurrent periods `1,2,4`; the largest one-step fibre is 80.
- Prospective axes: arithmetic evolution of cycle lengths and roots of a
  target permutation, with the minimum label coupled to each cycle.

### C03_IPF -- simultaneous interior-peak fall

- Carrier: one-line permutations in `S_n`, exhaustively tested for
  `1 <= n <= 7`.
- Literal update: mark every `i` with `1 <= i <= n-2` satisfying
  `pi_(i-1) < pi_i > pi_(i+1)` in the old word, then simultaneously swap
  `pi_i` and `pi_(i+1)`.  Marked pairs are automatically disjoint.
- Small-case signal: fixed counts are `1,2,4,8,16,32,64`; at `n=7` the map has
  maximum tail nine, exactly two deepest states, image 2,590, and no
  nontrivial recurrence.
- Prospective axes: a descent/energy clock and parallel-swap preimages.

## Words

For `C04`--`C07`, the carrier is `W_n={0,...,n-1}^n`, exhaustively tested for
`1 <= n <= 6`.

### C04_PME -- positional multiplicity echo

- Literal update: if `m_w(a)=#{j:w_j=a}`, set
  `F(w)_i=m_w(w_i)-1` at every old position `i`.
- Small-case signal: at `n=6`, image 150, 82 fixed points, maximum tail three,
  and largest one-step fibre 1,800.  Every orbit is eventually fixed.
- Prospective axes: (i) an exact pointwise clock on the merger dynamics of
  equality-block sizes, including a sharp logarithmic upper bound; (ii) an
  every-target labelled fibre product and image enumeration.  These use
  different data and pass the mathematical two-axis test, but central history
  identifies this as the permanent EQC/equal-cardinality-coagulation kill.

### C05_RLF -- run-length feedback

- Literal update: partition the old word into maximal adjacent constant runs;
  every position in a run of length `r` receives `r-1`.
- Small-case signal: at `n=6`, the image has size 32, there are 14 fixed words,
  maximum tail three, and largest fibre 18,750.
- Prospective axes: binary cut-set image and run-length composition fibres.

### C06_IHC -- interval-hull coverage

- Literal update: for every used symbol `a`, let
  `I_a=[first_w(a),last_w(a)]`; set
  `F(w)_i=#{a:i in I_a}-1`.
- Small-case signal: at `n=6`, image 21, 16 fixed points, maximum tail two,
  and largest fibre 9,276.
- Prospective axes: interval-overlap profiles and realization counts.

### C07_PBD -- strict-prefix bigram diversity

- Literal update: set
  `F(w)_i=|{(w_j,w_(j+1)):0 <= j <= i-2}|`; thus coordinates zero and one
  are zero, and the bigram ending at `i-1` is the newest eligible bigram.
- Small-case signal: at `n=6`, image seven, a unique fixed point, maximum tail
  three, and largest fibre 39,960.
- Prospective axes: first-occurrence times of adjacent pairs and prefix
  realization counts.

## Set partitions

For `C08`--`C11`, the carrier is the set `Pi_n` of set partitions of
`{0,...,n-1}`, exhaustively tested for `1 <= n <= 8`.  Blocks and elements
inside blocks are canonically written in increasing-minimum order.

### C08_PBMP -- parallel block-minimum peeling

- Literal update: replace each nonsingleton block
  `{b_1<...<b_s}` by `{b_1}` and `{b_2,...,b_s}`; leave every singleton
  unchanged, and perform the replacements simultaneously in all old blocks.
- Small-case signal: at `n=8`, image 397, the discrete partition is the unique
  recurrent state, the maximum tail is seven, and the indiscrete partition is
  the unique deepest state.  The largest one-step fibre is 764.
- Prospective axes: (i) an exact pointwise maximum-block clock and restricted
  Bell depth census; (ii) all-time every-target fibres governed by lower-label
  capacity matching plus a restricted Bell factor.  Central history identifies
  the literal map as the orbit-partition factor of P105 cycle-minimum pruning,
  so these axes receive no separation credit.

### C09_CSM -- cyclic-shift meet

- Literal update: let `rho(x)=x+1 mod n`; two labels `x,y` are equivalent in
  `F(pi)` iff both `x~_pi y` and `rho^(-1)x~_pi rho^(-1)y`.  Equivalently,
  `F(pi)=pi meet rho(pi)` in the refinement lattice.
- Small-case signal: at `n=8`, image 612, four fixed partitions, maximum tail
  six, and largest fibre 1,433; there are no nontrivial cycles.
- Prospective axes: the closed meet fold
  `F^t(pi)=meet_{j=0}^t rho^j(pi)` and target refinements.

### C10_MRC -- minima-reservoir collection

- Literal update: collect all old block minima into one block; for every old
  block retain its nonempty set of nonminimum elements as a separate block.
- Small-case signal: at `n=8`, image 1,091, no fixed state, maximum tail nine,
  and recurrent period 12; period spectra fluctuate through `2,6,12`.
- Prospective axes: an incidence permutation on minima/residual roles and
  target decompositions.

### C11_XCM -- crossing-component merge

- Literal update: make a graph on old blocks, joining `A,B` exactly when their
  endpoint intervals properly cross:
  `min A < min B < max A < max B` or the symmetric inequality.  Replace every
  connected component of this graph by the union of its blocks.
- Small-case signal: at `n=8`, image=fixed=1,922 and all other 2,218 states
  have tail one; the largest fibre is 265.
- Prospective axes: characterization of crossing-closed partitions and
  connected crossing-graph assemblies.

## Labelled posets

For `C12`--`C13`, the carrier is every strict partial order `R` on
`{0,...,n-1}`, exhaustively tested for `1 <= n <= 5` (4,231 states at `n=5`).

### C12_RPE -- relational-power erosion

- Literal update: `F(R)=R o R`; thus `x F(R) z` iff some `y` has
  `x R y R z`.
- Small-case signal: at `n=5`, image 631, unique recurrent/fixed antichain,
  maximum tail three, and largest fibre 841.
- Prospective axes: exact logarithmic height clock under repeated relation
  squaring and square-root counts for strict orders.

### C13_CSR -- cyclic-shift relation intersection

- Literal update: with `rho(x)=x+1 mod n`, retain `(x,y)` exactly when both
  `(x,y) in R` and `(rho x,rho y) in R`.
- Small-case signal: at `n=5`, image 431, unique fixed antichain, maximum tail
  four, exactly 20 deepest states, and largest fibre 1,471.
- Prospective axes: a closed shifted-intersection iterate and a cyclic run
  statistic on relation indicators.

## Compositions

The carrier `Comp_N` consists of all ordered positive compositions of `N`.

### C14_EVA -- equal-value aggregation

- Exhaustive box: `1 <= N <= 12`.
- Literal update: scan the old composition left to right.  On the first
  occurrence of each distinct value `v`, output the single part `v*m_v`,
  where `m_v` is its old multiplicity; output nothing on later occurrences.
- Small-case signal: at `N=12`, image 148, 101 fixed compositions, maximum
  tail three, and largest fibre 136.
- Prospective axes: strict loss of repeated values and an every-target divisor
  assignment/first-occurrence word count.

### C15_EHS -- simultaneous even-halving split

- Exhaustive box: `1 <= N <= 14`.
- Literal update: replace every even part `2m` by the adjacent pair `(m,m)`;
  leave every odd part fixed, synchronously over all old parts.
- Small-case signal: at `N=14`, image 889, 377 fixed compositions, maximum
  tail three, and largest fibre 610.  Fixed counts are Fibonacci numbers.
- Prospective axes: exact 2-adic pointwise clock and all-time constant-tile
  preimages.

## Replacement pass

### C16_MGBF -- leftmost-maximum-gap block fission

- Carrier: `Pi_n`, exhaustively tested for `1 <= n <= 9`.
- Literal update: in each old block `B={b_1<...<b_s}` with `s>=2`, locate the
  **leftmost** index `j` maximizing `b_(j+1)-b_j`, and replace `B` by the two
  nonempty blocks `{b_1,...,b_j}` and `{b_(j+1),...,b_s}`.  Split all old
  nonsingleton blocks simultaneously; singletons stay fixed.
- Small-case signal: at `n=9`, image 1,320, unique fixed/recurrent discrete
  partition, maximum tail eight with the indiscrete partition uniquely
  deepest, and largest fibre 2,620.
- Prospective axes: the left-tied maximum-gap Cartesian split tree gives every
  iterate and the exact pointwise clock; independently, every one-step target
  fibre is a restricted matching count in its block-compatibility graph.
- Gate warning: the local split is already a named largest-gap divisive
  clustering operation.  The matching theorem is real but does not buy literal
  update ownership; the final ledger kills it conservatively.

### C17_TRR -- top-row reservoir on integer partitions

- Carrier: integer partitions `lambda=(lambda_1>=...>=lambda_k>0)` of `N`,
  exhaustively tested for `1 <= N <= 25`.
- Literal update: replace `lambda` by
  `(lambda_1+k-1, lambda_2-1,...,lambda_k-1)`, deleting zero parts.
- Small-case signal: at `N=25`, image 383, unique fixed state `(25)`, maximum
  tail 12 with two deepest states, and largest fibre 25.
- Prospective axes: the all-time formula transfers one cell per surviving
  lower row into the top row, so the pointwise clock is `lambda_2`; every
  target has an elementary linear fibre formula.
- Gate warning: this is a Ferrers-layer transfer silhouette already occupied
  by P113's partition dynamics, so easy completeness is not enough.

### C18_MLI -- minimal-layer isolation of labelled posets

- Carrier: all strict partial orders on `{0,...,n-1}`, exhaustively tested for
  `1 <= n <= 5`.
- Literal update: find all current minimal vertices and delete every strict
  comparability whose lower endpoint is one of those vertices, synchronously.
- Small-case signal: at `n=5`, image 931, unique antichain fixed point,
  maximum tail four, and exactly `5!=120` deepest labelled total orders.
- Prospective axes: original down-heights give a closed layer-erasure iterate
  and height clock.  No independent target-root theorem emerged.

### C19_ISE -- interval-span echo on words

- Carrier: `W_n={0,...,n-1}^n`, exhaustively tested for `1 <= n <= 6`.
- Literal update: for every used letter `a`, let `f(a)` and `l(a)` be its first
  and last positions; replace every occurrence of `a` by `l(a)-f(a)`.
- Small-case signal: at `n=6`, image 195, 79 fixed words, maximum tail three,
  largest fibre 720, and no nontrivial recurrence.
- Prospective axes: equality-class interval spans and target realizations; the
  observed shallow clocks do not stabilize into a second theorem axis.

### C20_DRA -- displacement-rank assignment on permutations

- Carrier: `S_n`, exhaustively tested for `1 <= n <= 8`.
- Literal update: at position `i`, form the distinct key
  `(|pi_i-i|,pi_i)` and replace `pi_i` by the zero-based rank of that key among
  all positions in lexicographic order.
- Small-case signal: at `n=8`, image 14,634, 55 fixed states, recurrent periods
  `1,2,4,6`, maximum tail 17, and largest fibre 46.
- Prospective axes: displacement-order patterns and rank-realization fibres.
  The period and tail sequences are already too irregular for an all-size
  theorem spine.

### C21_PDCF -- prefix-divisibility cut filter

- Carrier: positive compositions `a=(a_1,...,a_k)` of `N`, exhaustively tested
  for `1 <= N <= 15`.
- Literal update: write `s_i=a_1+...+a_i`.  For every old internal cut `s_i`,
  retain it exactly when `a_i` divides `s_i`; delete all other old cuts
  simultaneously, and read the resulting coarsened composition.  No new cut
  is inserted.
- Small-case signal: at `N=15`, image 4,906, fixed set 1,763, maximum tail
  `12=N-3`, unique deepest state `(1,2,1,...,1)`, largest fibre 182, and only
  fixed recurrence.  The image sequence through 15 is
  `1,2,4,7,14,23,46,73,146,258,493,801,1602,2453,4906`.
- Prospective axes: monotone cut deletion gives the sharp all-size clock,
  fixed-state path recurrence, and strict extremizer; independently, a
  target-local path DP counts every one-step fibre and decides the image.
- Gate status: sole survivor, `OWNER_AMBER / HOLD_EXTERNAL`; the bounded
  owner search is a non-hit, not a novelty or priority claim.

## Gate summary

The expanded exhaustive pilot records 19 theorem-signal labels, but the gate
counts independent proof axes and subtracts ownership.  `C04_PME` and
`C08_PBMP` are central-history collisions and are killed.  `C16_MGBF` passes
both mathematical axes but is killed on the directly published largest-gap
split engine.  `C17_TRR` and `C15_EHS` are complete but internally
transferable.  Only `C21_PDCF` survives, still `OWNER_AMBER / HOLD_EXTERNAL`.
The exact disposition of all 21 denominator members is frozen in
`KILL_LEDGER.md`.
