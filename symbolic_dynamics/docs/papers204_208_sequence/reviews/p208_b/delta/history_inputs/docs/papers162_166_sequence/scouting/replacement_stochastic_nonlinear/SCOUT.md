# Replacement stochastic/nonlinear breadth scout

**Date:** 2026-09-03 UTC  
**Scope:** random word/configuration operations, nonlinear finite urns, random
algebraic maps, random graph/poset transformations, and finite-geometry walks  
**Historical boundary:** P1--P161 and all earlier P162--P166 scout/kill ledgers  
**External state:** `HOLD_EXTERNAL`  
**Literal systems exact-tested:** 24  
**Survivors:** 0 (`EMPTY_POOL`)

## Outcome first

This lane returns an honest empty pool.  All 24 kernels are literal finite
Markov systems, not parameter variants of one transition table, and all were
enumerated with exact rational arithmetic.  None passes the requested theorem
threshold.

The hard gate was a genuine compression of history.  A candidate needed a
sufficient statistic or diagonalization that was smaller than the full state
chain and that simultaneously supported:

1. a sharp all-parameter temporal, hitting, or endpoint law;
2. an every-target fibre/history law rather than one selected probability; and
3. an independent recovery, extremal, or deformation theorem.

Only two systems exhibit clean compression.  `W05` is exactly an iid
convolution walk on a cyclic rotation orbit after conditioning on letter
content.  That is a generic finite-group walk and directly collides with the
current adaptive-rotation lane.  `F01` falls in one step onto the linear
hyperplane `P+Q+R=0`, where it is fixed; its uniform fibre is only a linear
projection count.  Several urns have deterministic population clocks, but
their endpoint laws remain path-dependent dynamic programs.  The remaining
kernels have either no tested coarse lumping or only a generic linear/group/
polynomial semigroup reduction.  No candidate is reserved.

The lane does **not** re-enter named coalescents, coupon collection, random
deletion/pruning, TASEP/sorting, random span/rank erosion (`RTI`), random cut
intersection (P158), or any of `NL01`--`NL24`.  In particular, a tempting
random coordinate-sandwich matrix map was rejected before the frozen slate
because it reproduced the killed `NL18` rank-one/power-map engine.

## Exact diagnostic convention

For each representative finite box, the verifier records

```text
S / E / A / supp_4 / pmax_4 / Z / incoming range / L
```

where `S` is the number of states, `E` the number of distinct positive
transition edges, `A` the number of absorbing states, `supp_4` and `pmax_4`
refer to the exact four-step law from the displayed start in the source,
`Z` is the number of targets with zero one-step incoming Markov mass, and `L`
states whether the explicitly coded coarse statistic is strongly lumpable.
Incoming mass is the column sum of the stochastic matrix, not an unweighted
preimage count.

## Twenty-four-system decision ledger

### Random word and configuration operations

| ID | literal carrier and update | exact signature | theorem signal and history test | inverse/owner/internal gate | decision |
|---|---|---|---|---|---|
| `W01/EEI` | binary words of length six; sample `i<j`, and when the endpoint bits agree flip the strict interval `(i,j)` | `64/384/0/16/13231\/50625/0/1..1/0` | Every labelled generator is an involution because it leaves its two guards unchanged, so the kernel is doubly stochastic.  Weight plus cyclic-run count is not lumpable. | One-step incoming mass is identically one, but longer endpoint laws are just walks in an irregular involution graph; no hitting or recovery axis. | `KILL_INVOLUTION_GRAPH_NO_COMPRESSION` |
| `W02/UIR` | ternary words of length five; sample `i<j`, rotate `[i,j]` left iff its endpoint colours differ | `243/1539/3/30/107\/2000/0/3\/5..7\/5/1` | Content is preserved and hence lumpable only as a constant statistic.  Within a content class the active intervals depend on the full arrangement. | Variable incoming mass already rules out a uniform fibre; exact powers require the full content-class matrix. | `KILL_CONFIGURATION_DP_ONLY` |
| `W03/RPE` | binary cyclic words of length seven; sample a site, find its forward maximal run, and echo the run-length parity into the next bit | `128/352/2/14/625\/2401/0/4\/7..4/0` | Neither weight nor `(weight,run count)` is Markov.  Runs can split, merge, or remain unchanged under the same summary. | Endpoint multiplicities are irregular and no monotone clock exists. | `KILL_NO_SUFFICIENT_STATISTIC` |
| `W04/PCR` | ternary cyclic words of length five; a sampled `aba` start triggers rotation by its index plus one, otherwise hold | `243/459/105/2/369\/625/0/2\/5..9\/5/1` | Content and number of `aba` sites are invariant; on each rotation orbit the history is a cyclic convolution with orbit-dependent holding weights. | This is a state-gated rotation action, adjacent to `AQN/HWR/DCR`, with no noninvertible target atlas. | `KILL_ADAPTIVE_ROTATION_ACTION` |
| `W05/MCR` | ternary words of length six; sample a position and rotate by the multiplicity of its colour | `729/1665/3/6/325\/1296/0/1..1/1` | Content freezes the iid increment law.  The verifier independently checks four-step cyclic convolution for content `(3,2,1)`. | Fourier/cyclic convolution gives all endpoints, but all fibres are action-orbit fibres and the kernel is doubly stochastic; it is a random version of the occupied data-dependent rotation mechanism. | `KILL_GENERIC_GROUP_WALK_INTERNAL` |

### Nonlinear urns with state-dependent kernels

| ID | literal carrier and update | exact signature | theorem signal and history test | inverse/owner/internal gate | decision |
|---|---|---|---|---|---|
| `U01/SBE` | two-colour populations of total at most six; remove red or blue with weights `a^2,b^2` | `28/43/1/3/4176\/5525/7/27\/26..3/1` | Total drops by one, so the absorption clock from `(a,b)` is sharply `a+b`. | The sink is deterministic and every nontrivial time-target weight is a path sum with state-dependent denominators; no exchangeability or recovery remains. | `KILL_CLOCK_ONLY` |
| `U02/PCR` | sample an unordered ball pair: `RR->B`, `BB->R`, and `RB->empty` | `28/48/3/2/43\/45/7/1\/15..8\/3/0` | Total drops by one or two and colour difference changes in three incompatible ways.  `(total,difference mod 3)` is not lumpable. | This is a finite reaction-chain DP without an all-parameter hitting or target formula. | `KILL_REACTION_DP_ONLY` |
| `U03/PCG` | below cap six, add red with weight `(a+1)(1+[b odd])` and blue symmetrically | `28/49/7/5/3\/10/1/1\/2..11\/5/0` | Time to the cap is deterministic, but parity feedback destroys exchangeability; `(total,parities)` is not lumpable. | Cap endpoints require the full two-dimensional recurrence and have no independent inverse axis. | `KILL_CAP_CLOCK_NO_ENDPOINT_LAW` |
| `U04/PCE` | sample a pair: like pairs both vanish, while an unlike pair leaves one red | `28/48/3/1/1/8/1\/3..10\/3/0` | Total drops by one or two; even `(total,red parity)` is not Markov. | The tested start collapses by four steps, but the all-start law is an ordinary finite chemical-reaction recursion. | `KILL_SMALL_COLLAPSE_NO_SPINE` |
| `U05/GST` | fixed total six; transfer `gcd(a,b+1)` red balls left-to-right or its blue analogue, with square colour weights | `7/12/0/4/4379\/8450/0/1\/26..8\/5/0` | The fixed-population chain has no monotone statistic; the candidate gcd summary is not lumpable. | Irregular rational endpoint weights and no scalable fibre or recovery law. | `KILL_ENGINEERED_BIRTH_DEATH_NO_AXIS` |

### Random algebraic maps

| ID | literal carrier and update | exact signature | theorem signal and history test | inverse/owner/internal gate | decision |
|---|---|---|---|---|---|
| `A01/CCM` | coefficient triples `(a,b,c)` of monic cubics over `F_3`; uniformly mutate one coordinate to `bc`, `a^2+c`, or `ab` | `27/72/2/10/17\/81/9/1..3/0` | Neither coefficient sum nor zero pattern is sufficient; different mutation orders produce genuinely different polynomial compositions. | Nine targets already have no one-step source, and no symbolic normal form compresses histories. | `KILL_POLYNOMIAL_SEMIGROUP_DP` |
| `A02/RQS` | `F_7`; choose `x->x+x^2` or `x->x-x^2` | `7/13/1/5/1\/2/2/1..2/0` | The two quadratic generators have no common invariant giving a uniform prime-parameter temporal law. | Random polynomial iteration and finite-field functional graphs are owner-dense; exact data are only one small prime. | `KILL_GENERIC_RANDOM_POLYNOMIAL` |
| `A03/RPS` | `F_5^2`; choose `(a,b)->(a,b+ab)` or `(a+ab,b)` | `25/41/9/7/5\/16/1/1\/2..3/0` | Coordinate axes are fixed, but the product is not a sufficient statistic and histories are noncommuting polynomial shears. | One missing target and nonuniform incoming mass offer no every-target formula. | `KILL_POLYNOMIAL_SHEAR_NO_NORMAL_FORM` |
| `A04/RFS` | `F_2[u]/(u^4)`; choose `x->x+u^k x^2`, `k=1,2,3` | `16/36/4/8/16\/81/0/1..1/1` | Frobenius makes every generator `F_2`-linear; valuation is lumpable in the tiny box. | The apparent nonlinear notation collapses to a finite-linear semigroup and a doubly stochastic action, a forbidden mechanism. | `KILL_HIDDEN_FINITE_LINEAR` |
| `A05/RMP` | `M_2(F_3)`; choose `A->A+A^2` or `A->A-A^2` | `81/153/9/3/1\/2/34/1..14/1` | Cayley--Hamilton reduces each branch to a scalar polynomial in `A`; trace/determinant lump, but their transition is still a random polynomial semigroup. | Thirty-four targets have zero incoming mass; generic polynomial-map ownership and P103 adjacency consume the reduction. | `KILL_CAYLEY_HAMILTON_REDUCTION` |

### Random graph and poset transformations

| ID | literal carrier and update | exact signature | theorem signal and history test | inverse/owner/internal gate | decision |
|---|---|---|---|---|---|
| `G01/IWC` | labelled graphs on five vertices; sample a triple and add its missing edge exactly when it is an induced wedge | `1024/3984/52/2/369\/625/0/1\/10..4/0` | Components are invariant and the unique terminal graph is the union of cliques on the initial components.  Active moves add one edge, but raw waiting and admissible histories depend on the whole graph. | This is the `K_3` graph-bootstrap/closure primitive; `(edges,triangles)` is not lumpable and target histories are constrained edge-addition orders. | `KILL_DIRECT_GRAPH_CLOSURE` |
| `G02/XEC` | sample ordered vertices `u,v`; for every outside `w`, set both `uw` and `vw` to the old XOR of those incidences | `1024/9651/1/657/77\/2500/312/4\/5..8/0` | The adjacency update is linear over `F_2` for each scheduler choice, but rank and edge statistics are not sufficient under changing choices. | It is a random finite-linear graph transform with rank-changing shadows near the excluded RTI lane; 312 targets are absent after one step. | `KILL_RANDOM_LINEAR_RANK_SHADOW` |
| `G03/IER` | an induced one-edge triple triggers either cyclic relabelling of its three vertices; other triples hold | `1024/7944/52/30/8659\/80000/0/1..1/1` | Isomorphism type is frozen and the kernel is a walk generated by conditional vertex permutations. | The doubly stochastic target law and lumping by `(edges,triangles)` are group-action facts only; current `EGR` already occupies graph relabelling. | `KILL_CONDITIONAL_RELABEL_WALK` |
| `G04/NPC` | naturally labelled posets on four elements; sample `i<j`, adjoin that comparison, and transitively close | `40/169/1/39/1\/12/1/1\/3..17\/6/0` | The full chain is the unique absorbing state, but rank alone is not Markov and closure cascades retain the entire current relation. | Randomizing a closure frontier adds no theorem beyond poset closure; it collides with current `OPG` and the permanent generic-closure exclusion. | `KILL_STOCHASTIC_CLOSURE` |
| `G05/OCN` | labelled graphs on five vertices; toggle sampled edge `uv` iff `u,v` have an odd number of common neighbours | `1024/5488/46/205/43\/1250/0/1..1/0` | Each labelled toggle is an involution because changing `uv` does not change its common-neighbour count, hence the kernel is doubly stochastic.  Edge/parity summaries are not lumpable. | Longer endpoints are an irregular involution-graph walk, not an absorbing transformation or a target atlas. | `KILL_INVOLUTION_GRAPH_NO_COMPRESSION` |

### Finite-geometry walks

| ID | literal carrier and update | exact signature | theorem signal and history test | inverse/owner/internal gate | decision |
|---|---|---|---|---|---|
| `F01/RMT` | ordered triples of points in `F_3^2`; replace a sampled vertex by the midpoint of the opposite side | `729/2025/81/3/1\/3/648/9..9/1` | In characteristic three, every branch lands on `P+Q+R=0`, and every point of that hyperplane is fixed. | The 81 supported targets have uniform incoming mass nine, but this is exactly a depth-one linear projection; no stochastic or geometric third axis survives. | `KILL_LINEAR_PROJECTION_THIN` |
| `F02/AGS` | ordered affine triangles over `F_3`; move sampled vertex along the opposite side by the oriented-area scalar | `729/1593/297/46/5\/81/0/1..1/1` | Oriented area is lumpable, but within an area stratum the walk remains a full affine action with no hitting law. | Dually stochastic action and generic finite affine-geometry walk; no nontrivial fibre axis. | `KILL_AFFINE_ACTION_ONLY` |
| `F03/RSR` | ordered affine triangles over `F_3`; reflect a sampled vertex in the midpoint of the opposite side | `729/2025/81/9/5\/27/0/1..1/1` | The three reflections are affine involutions and preserve area strata. | This is a generic reflection/group walk with singleton labelled actions and no absorbing clock or inverse atlas. | `KILL_GENERIC_GEOMETRY_WALK` |
| `F04/DRF` | ordered vector pairs over `F_3`; choose one vector and rescale it by the frame determinant | `81/137/25/2/1\/2/40/3\/2..9/1` | Determinant zero collapses a vector, determinant one fixes, and determinant minus one reaches determinant one after a rescaling. | Depth one plus determinant/power bookkeeping is adjacent to P103 and the killed scalar-power family; 40 targets are absent. | `KILL_DETERMINANT_POWER_THIN` |

## Why there is no reserve

`W05` has the cleanest history statistic.  If the word contains `m_a` copies
of colour `a`, one step adds rotation increment `m_a` with probability
`m_a/n`; these increments are iid because content is invariant.  Thus the
time-`t` endpoint law is the `t`-fold convolution of

```text
mu = sum_a (m_a/n) delta_(m_a mod n).
```

Fourier diagonalization on `Z/nZ` is immediate.  But the carrier never leaves
one rotation orbit, the kernel is doubly stochastic, and every inverse claim
is an orbit/action count.  After subtracting cyclic convolution and the
current data-dependent-rotation lane, nothing paper-sized remains.

`F01` has the strongest target formula.  Over `F_3`, the midpoint of `Q,R` is
`-(Q+R)`.  Consequently every branch imposes `P+Q+R=0`, all such triples are
fixed, and every supported target has total incoming mass `9`.  These are the
rank, image, and fibre of a linear retraction.  The stochastic scheduler is
irrelevant after one step, so the mechanism is below threshold.

Deterministic clocks in `U01` and `U03` likewise do not rescue those urns: a
fixed population clock is one axis, while the history weights retain the full
two-coordinate state and no every-target closed form or independent recovery
result emerged.

## Verifier scope and falsification boundary

Run

```bash
PYTHONDONTWRITEBYTECODE=1 python3 \
  docs/papers162_166_sequence/scouting/replacement_stochastic_nonlinear/verify_scout.py
```

The standard-library verifier uses exact `Fraction` arithmetic.  It checks
all stochastic rows and carrier closure, every one-step incoming column,
four-step endpoint laws from frozen representative starts, the stated coarse
lumpability decisions, the exact `W05` convolution identity, the `G01`
one-edge monotonicity, family counts, and boundary states.  It makes **70,508
assertions** and ends in `STATUS PASS`.

These finite checks are counterexample pressure, not proofs of a missing
all-parameter theorem.  A bounded source-search miss is not evidence of
novelty, ownership, priority, or freedom to publish.  The entire lane remains
`HOLD_EXTERNAL`.

## Final gate

```text
EMPTY_POOL
SURVIVORS 0
HOLD_EXTERNAL
```

Re-entry requires a new literal stochastic mechanism with a proved history
normal form and all three theorem axes.  Increasing any of the present boxes,
diagonalizing another generic action walk, or solving another finite transition
matrix numerically is not a re-entry condition.
