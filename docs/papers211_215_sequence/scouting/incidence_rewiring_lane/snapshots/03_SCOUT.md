# Replacement breadth scout — matchings and incidence systems

**Date:** 2026-09-03 UTC  
**Portfolio boundary:** P1–P161 and every visible P162–P166 scout/kill ledger  
**External state:** `HOLD_EXTERNAL`  
**Literal systems enumerated:** 26  
**Distinct conjugacy classes:** 25 (`S01` and `S06` are complement-conjugate)  
**Decision:** `0 GREEN / 0 AMBER / 26 KILL`

## Outcome first

This lane deliberately returns an empty pool.  Twenty-six deterministic finite
maps were defined literally and exhaustively enumerated, spanning perfect
matchings, relations and bipartite matrices, subsets of incidence/intersection
graphs, rank-alternating incidence systems, ordered set systems, and uniform
hypergraphs.  Even after quotienting the one conjugate duplicate, the run
contains 25 genuinely distinct systems and therefore clears the requested
24-system breadth floor.

One system, `M01 OMD`, produced a striking exact atlas.  Relative to a fixed
perfect matching, its alternating-cycle parts split 2-adically; its target
fibres have an exact product formula; and its largest fibres for `n=1,...,7`
are

```text
1, 3, 7, 25, 81, 331, 1303.
```

It nevertheless fails the hostile gate.  If `F` is the fixed matching and
`M` the state, then

```text
F T^t(M) = (F M)^(2^t).
```

Thus every temporal, image, and fibre claim is a restriction of the generic
permutation power/root problem.  The perfect-matching overlay supplies the
usual coset type, and the fibre product is exactly the cyclewise square-root
formula.  This is a proof-engine owner, not merely a neighbouring title.

The next most complicated maps (`R01 UWS`, `R02 UCN`, `R04 DOM`) have rich
finite signatures but no stable all-parameter invariant, no every-target
formula, and no recoverable deformation.  Promoting such a single-size
anomaly would be quota padding.  The remaining systems are direct Hurwitz
actions, depth-one component/coordinate retractions, elementary incidence
threshold maps, or unstable finite spectra.

No theorem contract is frozen because no candidate reaches amber.

## Firewall applied before ranking

The literal/proof-engine exclusion pass removed or assigned zero credit to:

- the P130 crossing-component matching/planarity interface;
- the P136 random sunflower-transversal lane;
- the P157–P161 blocker, incidence-transpose, partition, and pruning engines;
- `CPE` partition meet-shift, `BQC` quotient/coalescence, `RTI` random
  intersection, and `AQN`/necklace actions;
- generic closure/core/pruning, direct image, coordinatewise products, fixed
  linear maps, LDU/Schur engines, and generic permutation powers/roots;
- graph-line-graph and matching-independent-set translations already present
  in the portfolio; and
- mere relabellings, named construction iterates, and a parameter change of an
  existing system.

The systems below are not random samples.  For each displayed carrier, the
entire state space was enumerated and its full functional graph classified.

## Exact signature convention

Each row reports

```text
N / |image| / maximum positive fibre / cycle lengths / maximum tail depth.
```

Cycle lengths list only the lengths present, not the number of vertices.
`verify_scout.py` and `CANONICAL.txt` retain the full fibre, cycle, and depth
histograms.

## Decision ledger

| ID | literal deterministic update | exact signature | attempted theorem axes | hostile decision |
|---|---|---:|---|---|
| `M01 OMD` | on perfect matchings of `[2n]` with fixed `F`, `T(M)=MFM` | at `n=7`: `135135 / 62685 / 1303 / {1,2,3,4} / 2` | exact iterate, 2-adic clock, every-target fibres/image, all fixed counts | **`KILL_GENERIC_PERMUTATION_SQUARE_ROOT_ENGINE`** |
| `M02 HUR` | ordered matchings `(A,B)->(B,BAB)` | `225 / 225 / 1 / {1,2,3} / 0` | complete temporal action | **`KILL_DIRECT_HURWITZ_ACTION`** |
| `M03 OCP` | keep each `F∪M` component iff its half-size is odd; use `F` elsewhere | `10395 / 3105 / 6331 / {1} / 1` | image and fibres | **`KILL_COMPONENT_RETRACTION_THIN`** |
| `M04 OFL` | keep the unique overlay component containing label `0`; use `F` elsewhere | `10395 / 6331 / 945 / {1} / 1` | image and fibres | **`KILL_POINTED_COMPONENT_RETRACTION_THIN`** |
| `R01 UWS` | Boolean relation: `(i,j)` is on iff there is exactly one selected two-walk `i-k-j` | `512 / 238 / 28 / {1,2,3} / 5` | temporal and fibres sought | **`KILL_NO_PARAMETER_SPINE`** |
| `R02 UCN` | graph: join `i,j` iff they have exactly one common neighbour | `32768 / 10729 / 878 / {1,2} / 10` | long clock signal and fibres sought | **`KILL_COMPLEX_SMALL_SPECTRUM_NO_SPINE`** |
| `R03 URF` | flip a matrix cell iff it lies in exactly one all-one complementary rectangle | `512 / 233 / 46 / {1} / 3` | temporal and target axes sought | **`KILL_UNSTABLE_RECTANGLE_THRESHOLD`** |
| `R04 DOM` | output cell `(i,j)` iff old row degree equals old column degree plus one | `4096 / 466 / 173 / {1,2} / 4` | deformation by dimensions and fibres sought | **`KILL_NO_PARAMETER_SPINE`** |
| `S01 KUN` | subsets of `KG(5,2)`: keep vertices with exactly one selected neighbour | `1024 / 483 / 52 / {1,2} / 5` | temporal and target axes sought | **`KILL_THRESHOLD_GRAPH_NO_SPINE`** |
| `S02 JEX` | subsets of `J(5,2)`: keep vertices with exactly two selected neighbours | `1024 / 253 / 262 / {1,3} / 5` | temporal and target axes sought | **`KILL_THRESHOLD_GRAPH_NO_SPINE`** |
| `S03 FTA` | Fano polarity graph: keep points with exactly one selected polar neighbour | `128 / 57 / 16 / {1} / 4` | finite-geometry deformation sought | **`KILL_POLARITY_THRESHOLD_NO_SPINE`** |
| `S04 PTA` | `PG(2,3)` orthogonal-polarity version of `S03` | `8192 / 1626 / 769 / {1,2} / 4` | `q`-deformation and fibres sought | **`KILL_POLARITY_THRESHOLD_NO_SPINE`** |
| `S05 RMN` | rook graph: keep vertices attaining the minimum positive selected-neighbour count | `512 / 218 / 10 / {1,2} / 4` | rectangular deformation sought | **`KILL_STATE_THRESHOLD_NO_SPINE`** |
| `S06 TIN` | 3-subsets of `[5]`: keep triples meeting exactly one selected triple in one point | `1024 / 483 / 52 / {1,2} / 5` | temporal and target axes sought | **`KILL_CONJUGATE_TO_S01`** |
| `I01 KVE` | alternate subsets of vertices/edges of `K5`; keep opposite objects incident to exactly one selected object | `1056 / 47 / 314 / {2} / 3` | rank-changing clock and fibres sought | **`KILL_INCIDENCE_THRESHOLD_NO_SPINE`** |
| `I02 BLM` | alternate 2- and 3-subsets of `[5]`; keep minimum-positive incidence count | `2048 / 968 / 10 / {2,6} / 5` | six-cycle signal and deformation sought | **`KILL_SMALL_ORBIT_SIGNAL_NO_FORMULA`** |
| `I03 FSC` | alternate Fano points/lines; keep opposite objects incident to exactly two selected objects | `256 / 114 / 16 / {2} / 4` | finite-geometry clock and fibres sought | **`KILL_INCIDENCE_THRESHOLD_NO_SPINE`** |
| `I04 GPM` | alternate `3x3` grid points and row/column lines; keep maximum-positive incidence count | `576 / 100 / 34 / {2} / 3` | rectangular deformation sought | **`KILL_STATE_THRESHOLD_NO_SPINE`** |
| `I05 CVP` | alternate cube vertices/faces; keep opposite objects with prime selected incidence count | `320 / 89 / 44 / {2,4} / 4` | dimensional deformation sought | **`KILL_ARBITRARY_PREDICATE_NO_SPINE`** |
| `I06 TAB` | alternate tetrahedron edges/faces; keep objects incident to all but one selected object | `80 / 24 / 15 / {2} / 3` | simplex-dimension deformation sought | **`KILL_INCIDENCE_THRESHOLD_NO_SPINE`** |
| `O01 PVT` | each ground-element membership column survives iff it occurs in exactly one ordered set | `65536 / 625 / 20736 / {1} / 1` | exact image/fibres | **`KILL_DIRECT_PRODUCT_RETRACTION`** |
| `O02 MCC` | replace each membership column of weight `r` by the first `r` set labels | `65536 / 625 / 1296 / {1} / 1` | exact image/fibres and ordered deformation | **`KILL_COLUMN_COMPRESSION_RETRACTION`** |
| `O03 SOR` | send a nonempty membership column to the singleton indexed by the sum of its old labels | `65536 / 625 / 256 / {1} / 1` | exact target fibres | **`KILL_DIRECT_PRODUCT_RETRACTION`** |
| `O04 RIN` | cyclic interval of the same membership weight, starting after its least selected label | `4096 / 2401 / 16 / {1,3} / 2` | weight deformation and target fibres sought | **`KILL_COLUMNWISE_NECKLACE_ENGINE`** |
| `H01 DDF` | 3-graph: retain an edge iff its three old vertex degrees are pairwise distinct | `1024 / 36 / 324 / {1} / 2` | degree-distribution fibres sought | **`KILL_DEGREE_SUMMARY_COLLAPSE`** |
| `H02 CDF` | 3-graph: retain an edge iff its three old pair-codegrees are pairwise distinct | `1024 / 66 / 304 / {1} / 2` | codegree-distribution fibres sought | **`KILL_CODEGREE_SUMMARY_COLLAPSE`** |

## The one strong negative control: `M01 OMD`

Let `P=FM`.  Because `F` and `M` are fixed-point-free involutions and
`FPF=P^(-1)`,

```text
T(M)=MFM=F P^2,
F T^t(M)=P^(2^t).
```

If the alternating components of `F∪M` have half-sizes
`lambda=(lambda_1,...,lambda_s)`, a part `r=2^a u` with `u` odd becomes
`2^min(t,a)` parts of size `r/2^min(t,a)`.  Therefore

```text
depth(M)  = max_i v_2(lambda_i),
period(M) = lcm_i ord_(u_i)(2).
```

The number of matchings of a fixed overlay profile `lambda ⊢ n` is

```text
n! 2^(n-l(lambda)) / product_r [r^(m_r) m_r!].
```

A target lies in the one-step image iff each even part size has even
multiplicity.  Its fibre factors independently over part sizes.  With `m=m_r`,

```text
r even:  0                                      if m is odd,
         m!/(2^(m/2)(m/2)!) (2r)^(m/2)          if m is even;

r odd:   sum_(j=0)^(floor(m/2))
         m!/((m-2j)! 2^j j!) (2r)^j.
```

Finally, the fixed count of `T^ell` is the profile sum over partitions all of
whose parts divide `2^ell-1`.  The verifier checks all these statements for
every matching through `n=7`, not just profile representatives.

These are mathematically correct and substantial-looking, but the displayed
factorization shows that they are generic power-map and permutation-root
facts on a reversible matching coset.  They receive zero residual credit.

## Boundary and negative-control attacks

- Empty carriers do not occur: matching tests start at `n=1`; relation and
  set-system carriers include the empty state explicitly.
- Every update is asserted to remain in its declared carrier before any graph
  statistic is computed.
- The functional-graph classifier independently verifies indegree mass,
  exhaustive cycle coverage, depth descent, and period inheritance.
- `M01` includes `t=0` in its power identity and checks positive iterates
  beyond twice the matching rank.  It separately checks `ell=1,...,6` fixed
  counts and every target, including `F` and targets with zero fibre.
- `S01` and `S06` having identical signatures triggered a literal conjugacy
  audit: complementing a 2-subset of `[5]` gives a 3-subset and converts
  disjointness to one-point intersection.  They count as one distinct class.
- Tagged incidence carriers include both empty-side states.  All observed
  cycles are even, as demanded by side alternation.
- The three ordered-family systems use 16 membership columns independently;
  their large fibres are therefore a direct-product artefact, not a second
  theorem axis.
- `R02`'s depth 10 is the best unexplained temporal anomaly.  Without a sharp
  formula in `n` or a target-resolved inverse law, it remains a kill.

## Reproducibility

Run from the repository root:

```bash
python3 docs/papers162_166_sequence/scouting/replacement_matchings_incidence/verify_scout.py
```

The frozen run reports `5,103,540` assertions and ends with

```text
DECISIONS 0_GREEN 0_AMBER 26_KILL
M01=KILL_GENERIC_PERMUTATION_SQUARE_ROOT_ENGINE
HOLD_EXTERNAL
STATUS PASS
```

`CANONICAL.txt` is the exact stdout transcript.  The owner log records a
bounded primary-source search; its non-hits are not novelty claims.

Frozen replay receipt:

```text
verify_scout.py SHA256
a204a09676ff5c5decdc7b5e9e313775653f51314d9db82a7bec8c4bad2aa850

CANONICAL.txt SHA256
ae32204f6d97bac186d3f7948404d6b7d2afbdcd397eaa31365c6b3343d9f54e

fresh replay 1 stdout SHA256
ae32204f6d97bac186d3f7948404d6b7d2afbdcd397eaa31365c6b3343d9f54e

fresh replay 2 stdout SHA256
ae32204f6d97bac186d3f7948404d6b7d2afbdcd397eaa31365c6b3343d9f54e

python3 -m py_compile: PASS
```

## Final handoff

```text
SURVIVORS: none
PAPER-SIZED CONTRACTS: none
POOL EFFECT: no addition
EXTERNAL: HOLD_EXTERNAL
```
