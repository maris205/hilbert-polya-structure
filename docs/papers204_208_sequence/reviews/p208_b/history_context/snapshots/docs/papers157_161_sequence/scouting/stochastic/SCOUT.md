# Stochastic/graph/spatial Stage-1 breadth scout — P157–P161 intake

**Date:** 2026-09-02 UTC  
**Route:** A, Stage 1  
**External status:** `HOLD_EXTERNAL`  
**Paper assignment:** none

## Outcome first

This lane tested **19 genuinely different literal stochastic, graph, or
spatial dynamics**.  The count is by update rule, not by changing parameters.
Every row below was actually run in exact integer or rational arithmetic.

Two candidates are recommended as owner-thin inputs to the joint Stage-1
selection:

1. **`CIC` — random cut-intersection collapse.**  Intersect `K_n` with fresh
   fair vertex cuts.  After `t` epochs, vertices carry `t`-bit histories and an
   edge survives exactly between complementary histories.  This gives an exact
   absorption CDF and a labelled every-target fibre formula for disjoint unions
   of complete bipartite components.  Status:
   **`SURVIVE_OWNER_THIN / HOLD_EXTERNAL`**.
2. **`RCR` — random anchored-rectangle contraction.**  Sample a uniform cell
   of the current lattice rectangle and keep the origin-anchored subrectangle
   ending there.  Its coordinates are independent uniform-descending chains;
   the one-dimensional absorption PGF factors explicitly, the rectangle clock
   is their maximum, and every transient level has a closed Green kernel.
   Status: **`SURVIVE_OWNER_THIN / HOLD_EXTERNAL`**.

One further candidate is mathematically strong but owner-risky:

- **`PMI` — repeated perfect-matching intersection.**  Factorial moments and
  binomial inversion give the complete common-edge law and exact residual-
  matching fibres.  Direct literature owns the `t=2` derangement boundary,
  common-edge questions, and the matching association scheme.  Status:
  **`SURVIVE_OWNER_AMBER / HOLD_EXTERNAL`**, conditional on a stronger Stage-2
  subtraction.

`RII`, fixed-window intersection on a path, is an owner-thin **reserve**.  Its
signal is exact, but its proof is discrete sample-range inclusion–exclusion and
it shares the intersection engine with `CIC` and `PMI`.  The other fifteen
systems are killed now.  No weak system was promoted to fill a quota.

## Exact executable contract

[`verify_stochastic_scout.py`](verify_stochastic_scout.py) is deterministic and
uses only the Python standard library, integers, and `fractions.Fraction`.  It
has no floating-point arithmetic, pseudorandom sampling, seed, timestamp,
third-party package, or network access.  The frozen stdout is
[`CANONICAL.txt`](CANONICAL.txt).

From this directory, the exact cold-run contract is:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_stochastic_scout.py > /tmp/stochastic_scout.out
cmp -s CANONICAL.txt /tmp/stochastic_scout.out
```

The script constructs literal small states and compares them with independent
formula, recurrence, symmetry, inclusion–exclusion, aggregation, permutation,
or fibre calculations.  Exhaustive enumeration is used only as falsification
pressure.  A `PASS` line proves neither an all-parameter theorem nor novelty.

## Nineteen-system exact ledger

The “theorem silhouette” column is a prospective deductive target, not a claim
that finite computation proves it.  The “second axis” is deliberately kept
separate from the principal temporal statement.

| ID | literal carrier and update | exact small-case signature | possible all-parameter temporal theorem | independent second axis | closest P1–P156 collision | decision |
|---|---|---|---|---|---|---|
| `CIC` | Carrier: labelled edges of `K_n`.  Draw an iid fair `0/1` label at every vertex and replace the current edge set by its intersection with that cut. | `n=4,t=3`: edge-count multiplicities `{0:1880,1:1440,2:720,3:32,4:24}` among 4,096 cut histories; exact `K_{2,1}+I` labelled fibre `48`. | Exact `P(T<=t)` from antipodal-code avoidance; finite exponential/inclusion–exclusion tail and absorption almost surely. | Classify every positive-time image as disjoint complete bipartite components plus isolates and count every labelled target fibre. | P143 Boolean-row coding and P145 cut-vector vertex pushes are algebraically nearby, but neither intersects fresh cuts nor has complement-code fibres. | **`SURVIVE_OWNER_THIN`** |
| `PMI` | Carrier: edges of `K_{2n}`.  Draw iid uniform perfect matchings and retain their cumulative intersection. | `K_6,t=3`: 15 matchings, 3,375 histories, common-edge multiplicities `{0:3000,1:360,3:15}`. | Complete all-`n,t` law by factorial moments and binomial inversion; rational absorption mean for `n>=2`. | Exact number of histories whose intersection is any fixed labelled `j`-matching; conditional uniformity over residual matchings. | Permanent generic-matching exclusion and P62–P81 random-graph lane; external matching-derangement owners are the main collision. | **`SURVIVE_OWNER_AMBER`** |
| `RII` | Carrier: lattice intervals in an `n`-vertex path.  Intersect with an iid uniform interval of fixed length `ell`. | `n=7,ell=3,t=3`: intersection lengths `{0:60,1:36,2:24,3:5}` over 125 histories. | Exact absorption CDF and mean as a finite sum of powers of the sampled-start range. | Every nonempty target interval has a position-independent fibre count determined by its length. | P82–P101 renewal/avoidance interfaces are nearby; the decisive engine is classical discrete sample range, not an occupied literal map. | **`RESERVE_OWNER_THIN`** |
| `PLI` | Carrier: points of `PG(2,q)`.  Intersect the current point set with an iid uniform projective line. | At `t=3`, size counts are `{0:168,1:168,3:7}` for `q=2` and `{0:1404,1:780,4:13}` for `q=3`. | For every prime power `q`, exact line/point/empty probabilities at every `t`. | Uniform point fibres and exact concurrent-line history counts. | Direct finite-field rank/incidence theory and the finite-plane carrier of P153. | **`KILL_OWNER_RANK`** |
| `OKC` | Carrier: two positive populations `(a,b)`.  Decrement `a` with probability `b/(a+b)` and `b` with probability `a/(a+b)` until an axis. | From `(3,3)`, survivor-count law `{1:11/60,2:11/30,3:9/20}`. | Exact exit-side/survivor distribution and absorption moments. | Sharp dependence on initial imbalance. | P151 first-passage interface; more decisively, this is literally the externally owned OK Corral urn. | **`KILL_DIRECT_OWNER`** |
| `CUG` | Carrier: subgraphs of `K_n`.  Union the current graph with an iid fair vertex cut. | `n=4,t=3`: edge counts `{0:8,3:224,4:168,5:2016,6:1680}`; complete count `1680=(8)_4`. | Completion CDF `(2^t)_n/2^{tn}` and exact birthday-type mean. | State is the complete multipartite graph of equal-history classes; a target with `r` blocks has `(2^t)_r` fibres. | P143 Boolean rows, P145 cut-vector pushes, and the permanent partition-refinement kill. | **`KILL_BIRTHDAY_REFINEMENT`** |
| `STI` | Carrier: edges of `K_n`.  Intersect iid uniform Cayley spanning trees. | `K_4,t=2`: 16 trees and common-edge counts `{0:12,1:120,2:108,3:16}`. | Full common-forest law from Cayley forest-extension moments and binomial inversion. | Refine by residual forest component sizes and exact fixed-forest fibres. | P146/random-forest deletion interface and the permanent random-forest kill; an external paper directly studies intersections of random spanning trees. | **`KILL_DIRECT_OWNER_ENGINE`** |
| `RSA` | Carrier: occupancy masks of a path.  Uniformly choose an available adjacent empty pair, occupy both sites, and stop when jammed. | On `P_7`, terminal dimer count is `{2:1/9,3:8/9}` across 5 terminal masks. | Standard all-length random-sequential-adsorption recurrence/PGF. | Exact terminal maximal-matching support and endpoint masses. | P141 threshold random-greedy MIS and the permanent greedy-matching exclusion. | **`KILL_CLASSICAL_RSA`** |
| `KGT` | Carrier: self-avoiding paths in `K_{a,b,c}`.  From the current endpoint choose a uniform unvisited neighbour; stop at a dead end. | In `K_{2,2,3}` from part 0, terminal length law `{5:1/40,6:79/360,7:34/45}`. | Only a multivariate finite-state recurrence was stable; no crisp closed all-parameter clock emerged. | Terminal part and visited part-count vector. | P151 unequal-spider first passage and the permanent generic-walk wrapper kill. | **`KILL_WEAK_SILHOUETTE`** |
| `ALE` | Carrier: nonnegative loads on a path.  Choose a uniform adjacent pair with gap at least 2 and replace it by the two floor/ceiling averages, orienting odd totals fairly. | From `(4,0,3,0)`, clock law `{2:7/12,3:1/8,4:7/24}` with 5 terminal state/clock pairs. | Quadratic energy strictly decreases and gives a finite deterministic bound, but no exact general clock law appeared. | Classify locally balanced terminal configurations at fixed mass. | P148 level contraction and P62–P81 sandpile/load-balancing interfaces. | **`KILL_WEAK_TEMPORAL_AXIS`** |
| `HFC` | Carrier: origin-anchored faces of the Boolean cube.  Sample a uniform vertex of the current face and replace the face by the smallest face containing it and the origin. | `d=4,t=3`: face dimensions `{0:2401,1:1372,2:294,3:28,4:1}`. | `D_t ~ Binomial(d,2^{-t})`; exact absorption CDF `(1-2^{-t})^d`. | Every target `k`-face has the same explicit history fibre. | P143 Boolean-lattice machinery and P148 contraction; generic independent-coordinate product. | **`KILL_BOOLEAN_PRODUCT`** |
| `TAS` | Carrier: a binary word.  Choose a uniform active adjacent inversion `10` and swap it to `01`. | `110100` has clock 8, Ferrers shape `(3,3,2)`, and 42 complete histories. | Clock equals inversion number pathwise. | History count is the standard Young-tableau hook formula for the inversion Ferrers shape. | P82–P83 Fredkin/Rule-184 lane and the permanent hook/linear-extension exclusion. | **`KILL_TASEP_HOOK`** |
| `ARC` | Carrier: covered subsets of a cycle.  Union with an iid uniform cyclic arc of fixed length. | On `C_7` with length 3 at `t=3`, covered sizes `{3:7,4:42,5:84,6:126,7:84}`; full-cover count 84. | Exact subset-inclusion–exclusion formula for the cover-time CDF. | Transfer/automaton count of every target covered set. | P130 chord/cycle geometry and P82–P101 coverage/avoidance mechanisms. | **`KILL_COVERAGE_ENGINE`** |
| `CEC` | Carrier: cyclic connected-block partitions.  Uniformly erase one remaining original cycle bond and merge its adjacent blocks. | `C_6,k=3`: ordered-history block profiles `{(1,1,4):36,(1,2,3):72,(2,2,2):12}`. | Fixed absorption clock `n-1`; after `k` steps the erased bond set is uniform. | Exact cyclic-composition endpoint and history fibres. | P148 level contraction plus the permanent adjacent-coalescence exclusion. | **`KILL_OCCUPIED_COALESCENCE`** |
| `PHG` | Carrier: intervals containing a fixed start vertex in a path.  Sample a uniform vertex and replace the state by its interval hull with the sample. | `n=7,start=3,t=3`: 16 targets; full-hull count 36. | `P(T<=t)=1-2((n-1)/n)^t+((n-2)/n)^t` for an interior start. | Exact every-target interval fibre from sample minimum/maximum. | P151 first-passage/endpoint emphasis and the classical sample-range engine. | **`KILL_SAMPLE_RANGE`** |
| `BPC` | Carrier: infected subsets of a cycle.  Add one uniform uninfected seed, then close deterministically under threshold 2. | On `C_7`, required seed count `{4:17/45,5:26/45,6:2/45}`. | Possible all-`n` law through cyclic zero-gap avoidance in a uniform seed order. | Exact terminal closure fibres and minimal contagious seed configurations. | P62–P81 cellular automata and P141 threshold MIS; generic bootstrap closure is also a permanent kill. | **`KILL_BOOTSTRAP_CLOSURE`** |
| `PSD` | Carrier: induced subposets of a fixed DAG.  Uniformly delete a current source and record the deletion order. | A five-point DAG has 10 extensions with probability multiplicities `{1/12:4,1/24:4,1/4:2}`. | Fixed clock `n`; path probability is the product of reciprocal active-source counts. | Complete endpoint history support is the set of linear extensions. | Permanent generic hook/linear-extension exclusion; close in proof engine to P144's reassociation histories. | **`KILL_LINEAR_EXTENSIONS`** |
| `RCD` | Carrier: cells of a rectangle with live row/column labels.  Uniformly delete a live row or column and stop when one family is exhausted. | From `3x2`, axis-survivor law `{C1:3/10,C2:1/5,C3:1/10,R1:3/10,R2:1/10}`. | Negative-hypergeometric absorption clock and exit-side law. | Exact labelled histories for every survivor count. | P82–P101 renewal/exposure interfaces and P151 first-passage wrapper; generic quota race. | **`KILL_QUOTA_EXPOSURE`** |
| `RCR` | Carrier: anchored lattice rectangles `[1,a] x [1,b]`.  Pick a uniform current cell `(i,j)` and replace the state by `[1,i] x [1,j]`. | From `4x3` at `t=4`, absorption probability `3360875/4478976`; for the one-dimensional chain from 5, mean `37/12` and Green row to levels `2..5` is `(1,1/2,1/3,5/4)`. | Coordinate absorption PGF `z(n-1)!/prod_{k=2}^n(k-z)`; rectangle clock is the maximum of two independent coordinate clocks. | Closed level Green kernel and a factorized exact transition atlas on every subrectangle. | P101 random synchronization and P148 level contraction are nearest, but neither uses uniform anchored subrectangles or this transform/Green conjunction. | **`SURVIVE_OWNER_THIN`** |

## Strong candidate `CIC`: cut-intersection collapse

### Literal dynamics

Fix `n>=2`, start from `G_0=K_n`, and at epoch `s` draw independent fair
bits `b_s(v)` at every labelled vertex.  Let `C_s` be the complete bipartite
cut graph with edge `uv` exactly when `b_s(u) != b_s(v)`, and set

```text
G_t = G_(t-1) intersection C_t.
```

Let `T=min{t>=1:E(G_t)=empty}`.  The edge set only decreases, so the empty
graph is absorbing.

### Prospective all-parameter temporal theorem

Give vertex `v` its history word
`c_t(v)=(b_1(v),...,b_t(v))`.  Then, pathwise,

```text
uv in E(G_t)  iff  c_t(u) = complement(c_t(v)).               (CIC.1)
```

For `t>=1`, put `R=2^(t-1)` and define

```text
A_R(n) = sum_(j=0)^R (-1)^(R-j) binom(R,j) 2^j j^n.          (CIC.2)
```

There are `R` antipodal pairs of codewords.  `A_R(n)` counts labelled word
assignments using no pair on both sides; equivalently it is
`n![x^n](2 exp(x)-1)^R`.  Thus the candidate theorem is

```text
P(T<=t) = A_(2^(t-1))(n) / 2^(tn).                            (CIC.3)
```

The union bound `P(T>t)<=binom(n,2)2^(-t)` supplies absorption almost surely
and an immediate finite mean bound.  Formula (CIC.3), not that bound, is the
sharp temporal object.

### Independent structural/fibre axis

By (CIC.1), every nontrivial connected component of `G_t` is a complete
bipartite graph carried by one antipodal code pair; unmatched code classes are
isolates.  Conversely a labelled disjoint union of `r` nontrivial complete
bipartite components and `z` isolates is attainable exactly when `r<=R` and
either `z=0` or `r<R`.  The second condition is necessary because isolates
cannot reuse a code pair already occupied by a nontrivial component.

For a fixed labelled target `H` of that form, its exact history fibre is

```text
|(G_t)^(-1)(H)| = (R)_r 2^r A_(R-r)(z).                       (CIC.4)
```

The factors choose and orient one antipodal pair per connected component; the
remaining isolate codes must avoid complementary pairs.  In particular,
`A_0(z)=0` for `z>0`, so the formula records the missing `r=R,z>0` boundary
without an exception.  A target outside the stated graph class, or outside the
corrected attainability range, has fibre zero.  This is genuinely separate
from the empty-state clock: it is a complete labelled image and inverse
theorem.

The pilot checks all 4,096 histories at `n=4,t=3`, the complete edge-count
profile, (CIC.3), and the nontrivial fibre (CIC.4) for labelled
`K_{2,1}+I`.

### Collision and owner boundary

P143 uses Boolean row inclusion and labelled poset fibres; P145 uses a fixed
cut-vector group action on orientations.  `CIC` instead samples fresh cuts and
retains the intersection of their edge sets.  Its graph components arise from
**complementary full histories**, not row containment, push orbits, spectra, or
component orders.  Those distinctions must be rechecked in a formal collision
firewall if it advances.

The bounded public search found biclique coverings and random intersection
graphs, but no direct owner of (CIC.1)–(CIC.4).  Graph cuts, binary codes,
bicliques, and inclusion–exclusion receive zero credit.  The non-hit is only
`OWNER_THIN`; it is not novelty.  See
[`OWNER_SEARCH_LOG.md`](OWNER_SEARCH_LOG.md).

**Recommendation:** advance to the cross-lane shortlist, anonymously and
under `HOLD_EXTERNAL`.

## Strong candidate `RCR`: anchored-rectangle contraction

### Literal dynamics

For integers `a,b>=1`, let the state be the lattice rectangle
`[1,A_t] x [1,B_t]`, initially `(A_0,B_0)=(a,b)`.  Given `(A_t,B_t)`, choose a
cell `(I,J)` uniformly from the current rectangle and put

```text
(A_(t+1),B_(t+1)) = (I,J).
```

The state `(1,1)` is absorbing.  Because a uniform cell has independent
uniform coordinates, the two coordinate chains are independent at every
time.  This is a literal spatial contraction, not a product imposed after the
fact.

### Prospective all-parameter temporal theorem

Let `H_n` be the first time the one-dimensional chain `X -> Uniform{1,...,X}`
started at `n` hits 1.  First-step decomposition gives, for `n>=2`,

```text
g_n(z) = E[z^H_n] = z(n-1)! / product_(k=2)^n (k-z).          (RCR.1)
```

Equivalently, `H_n` is a sum of one positive-geometric and `n-2`
zero-based geometric variables read from the factors of (RCR.1), and

```text
E H_n = 1 + H_(n-1)                                           (RCR.2)
```

where the rightmost `H_(n-1)` denotes the harmonic number.  If `T_(a,b)` is
the rectangle absorption time, independence gives the complete CDF

```text
P(T_(a,b)<=t) = P(H_a<=t) P(H_b<=t),
T_(a,b) = max(H_a,H_b) in distribution.                       (RCR.3)
```

Thus the two-dimensional clock is explicit through two finite rational PGFs,
without enumerating rectangles.

### Independent occupation/structural axis

For `n,k>=2`, let `G(n,k)` be the expected number of visits to level `k`
before absorption, counting time zero.  A separate hitting-and-dwell argument
gives

```text
G(n,k) = 0          if n<k,
         k/(k-1)    if n=k,
         1/(k-1)    if n>k.                                  (RCR.4)
```

Indeed, from any `n>k` the probability ever to hit `k` is `1/k`, and once at
`k` the geometric dwell has mean `k/(k-1)`.  In addition, the full rectangle
transition atlas factorizes:

```text
P_(a,b)^t((i,j)) = P_a^t(i) P_b^t(j).                         (RCR.5)
```

Equations (RCR.4)–(RCR.5) are occupation and spatial-state results rather than
another statement of the terminal clock.

The pilot independently builds the two-dimensional exact kernel and the two
one-dimensional kernels at `(a,b,t)=(4,3,4)`, checks their complete product
law, and verifies the Green row from `n=5`.

### Collision and owner boundary

P148 contracts levels in a different combinatorial carrier, and P101 concerns
random synchronization.  `RCR` has neither an equivalence-class merger nor a
random-function semigroup; its state is a nested spatial rectangle and its
clock comes from coordinatewise uniform descent.  Generic product-chain and
absorbing-Markov-chain algebra receives zero credit.

The bounded search located a broad paper on decreasing Markov-chain absorption
asymptotics, but no direct anchored-rectangle process or exact
(RCR.1)–(RCR.5) conjunction.  The self-loops also require care when importing
strict-decrease results.  This is an unresolved bounded non-hit, not novelty.

**Recommendation:** advance to the cross-lane shortlist, anonymously and
under `HOLD_EXTERNAL`; Stage 2 must search random descent, leader election,
record minima, and nested-rectangle terminology.

## Conditional candidate `PMI`: repeated matching intersection

Let `M=(2n-1)!!` be the number of perfect matchings of `K_{2n}` and let
`K_t` be the number of edges common to `t` iid uniform perfect matchings.
Write

```text
N_k = (2n)!/[2^k k! (2n-2k)!],
c_k = (2n-2k-1)!!.
```

Counting a fixed `k`-edge partial matching inside all `t` samples gives the
factorial-moment identity

```text
sum_j binom(j,k) #{histories with K_t=j} = N_k c_k^t.         (PMI.1)
```

Binomial inversion therefore yields the complete law

```text
P(K_t=j) = M^(-t) sum_(k=j)^n
           (-1)^(k-j) binom(k,j) N_k c_k^t.                  (PMI.2)
```

For `n>=2`, summing the finite exponential survival law also gives a rational
closed form for `E T`, where `T` is the first empty cumulative intersection.
For a fixed labelled `j`-matching `F`, the number of histories with exact
intersection `F` is the empty-intersection count for `t` matchings on the
remaining `2(n-j)` vertices, hence depends only on `j`.  This is the intended
independent fibre theorem.

The issue is ownership, not mathematics.  Matching derangements own the
`t=2` boundary, and matching association schemes own the pair-relation
geometry.  Stage 2 must show that (PMI.1)–(PMI.2) plus the repeated-intersection
fibre is more than a routine `t`-power extension.  Until then it is
`OWNER_AMBER`, not owner-thin.

## Reserve `RII`: fixed-window intersection

Let `m=n-ell+1` possible windows have starts `0,...,m-1`.  After `t` samples,
the intersection length is `ell-D` if the start range `D=max-min` is smaller
than `ell`, and is zero otherwise.  The number of `t`-tuples with exact range
`d` is

```text
m                                                    if d=0,
(m-d)[(d+1)^t - 2d^t + (d-1)^t]                    if d>=1. (RII.1)
```

Under `m>=ell+1`, summing (RII.1) over `d<ell` gives the exact survival law
and a finite-power expression for the mean.  For each fixed nonempty target
interval, remove the factor `(m-d)` from (RII.1): the remaining bracket is its
exact history fibre.  The theorem pair is clean, but the sample-range engine
is classical and overlaps the other intersection candidates.  `RII` therefore
remains a replacement reserve only.

## Kill rationale and breadth conclusion

The fifteen kills fail for different reasons:

- `PLI`, `OKC`, `STI`, `RSA`, and `TAS` have direct or plainly classical
  owners for the decisive carrier/update/proof engine.
- `CUG`, `HFC`, `CEC`, `BPC`, `PSD`, and `RCD` reduce to permanently excluded
  birthday/refinement, Boolean product, coalescence, closure, linear-extension,
  or quota/exposure mechanisms.
- `KGT` and `ALE` have exact small cases but no sufficiently sharp
  all-parameter temporal theorem.
- `ARC` has only generic coverage inclusion–exclusion/transfer machinery.
- `PHG` is an exact but cosmetic sample-minimum/maximum wrapper.

The breadth pass therefore did its intended job: it did not spend the whole
round patching one weak chain.  It tested graph intersection, matching
intersection, spatial interval intersection, finite geometry, an urn death
chain, cut-union growth, tree intersection, dimer adsorption, kinetic
self-avoidance, load equalization, face contraction, exclusion sorting, cyclic
coverage, edge contraction, hull growth, bootstrap closure, poset deletion,
row/column deletion, and anchored rectangle contraction.

## Handoff

- Recommend `CIC` and `RCR` as the two owner-thin cross-lane candidates.
- Carry `PMI` only as owner-amber and `RII` only as an owner-thin reserve.
- Advance at most one of `CIC`, `PMI`, and `RII` unless a later collision audit
  proves separation of their dominant intersection/inclusion–exclusion engine.
- Assign no paper number at this stage.
- Preserve `HOLD_EXTERNAL`.  No source non-hit or verifier pass authorizes
  posting, attribution, priority language, publicity, or submission.
