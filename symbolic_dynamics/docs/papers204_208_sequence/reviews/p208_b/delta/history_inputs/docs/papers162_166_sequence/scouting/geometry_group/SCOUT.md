# P162--P166 geometry/group/topology breadth scout

**Status:** `EMPTY_POOL / HOLD_EXTERNAL`  
**Scope:** finite geometry, finite-group local structure, finite topology  
**Executable result:** 12 genuinely different literal maps, 12,144 exact
assertions, zero promoted candidates

## Outcome first

This lane does **not** nominate a P162--P166 paper.  Twelve maps were
implemented and checked on exact finite carriers.  Several have clean formulas,
but none passes all three gates simultaneously:

1. a nontrivial all-parameter temporal theorem rather than a one-step
   retraction or a clock supplied by deleting the ambient coordinate;
2. an independent fibre/image/recovery axis;
3. survival after both the P1--P161 mechanism firewall and bounded
   primary-owner subtraction.

The two initially strongest signals were flag trace on finite Grassmannians
(`GG01/FTR`) and affine parallel-uniqueness (`GG10/LPU`).  The former is a
Schubert/coordinate-trace calculation with an imposed ambient clock, close in
proof engine to the occupied subspace and trace lanes.  The latter has a nice
every-target product fibre, but its entire temporal theory is `T^2=T`.  Neither
is paper-sized after subtraction.  Therefore the shortlist is empty rather
than padded with an amber system.

No empty search hit is interpreted as novelty.  Everything remains
`HOLD_EXTERNAL`.

## Historical collision firewall

Before generating the pool, the scout inspected the P1--P161 directory roster,
the sequence occupancy/kill ledgers, and the recent geometry replacement
scouts.  The decisive exclusions were:

- P150 already owns the zero-totalized finite-field Lyness window;
- P154 already owns subgroup normalizer dynamics on dihedral groups;
- P161 already owns the finite-field orthocenter window;
- recent geometry scouts already tested projective Steiner collapse,
  Cremona reciprocation, conic reflection, quadratic inversion, Hurwitz
  pairs, harmonic conjugation, projective polarity, Vieta replacement,
  simplex rotation, promotion, polar duality, and finite-field orthocenter
  variants;
- recent topology scouts already tested simultaneous free-face deletion,
  beat/dominated-point cores, links, mod-two boundary support, and canonical
  elementary collapse;
- permanent portfolio kills exclude generic group actions/walks, classical
  involutions, finite-linear relabellings, QNC, and relabelled
  Lyness/Vieta/orthocenter systems.

Those systems are not counted among the twelve below.  In particular, this
pool contains no random walk, Coxeter/group action, polarity/duality
involution, or linear recurrence.

## Exact executable contract

`verify_scout.py` uses only the Python standard library and no randomness.  It
constructs all subspaces of `F_2^n` through `n=5`, all labelled subgroups of
`S_3` and `S_4`, all labelled posets on three points, all nonempty subsets of
the path/cycle pilots, every subset of the Fano plane, all line subsets of
`AG(2,2)` and `AG(2,3)`, and all 167 labelled simplicial complexes on four
available vertices in the chosen facet representation.  It checks identities,
not merely printed samples.

The frozen run ends with

```text
PASS assertions=12144 systems=12 shortlist=0 status=EMPTY_POOL HOLD_EXTERNAL
```

## Twelve-system ledger

| ID | literal carrier and simultaneous update | exact small-box signature | all-parameter theorem signal | independent axis attempted | owner/internal subtraction | decision |
|---|---|---|---|---|---|---|
| `GG01/FTR` | tagged `U <= F_q^n`; replace it by `U cap F_q^(n-1)` in the shorter coordinate flag | over `F_2`, total subspace counts for `n=0..5` are `1,2,5,16,67,374`; for `(k,t)=(3,2)` the target fibre levels are `5,11,29,89` | `T^t(U)=U cap F_q^(n-t)`; the successive dimension losses are the Schubert pivot word | for fixed `W <= F_q^k`, `|T^{-t}(W)|=sum_r [t choose r]_q q^(r(k-dim W))` | imposed ambient clock; Schubert-cell/coordinate-trace count; close to P109 and the current set-family trace control | `KILL_FLAG_TRACE_OWNER_THIN` |
| `GG02/SRE` | `U` in a nondegenerate `2m`-dimensional symplectic space; send `U` to `rad(U)=U cap U^perp` | `(m,states,fixed,image,max fibre)=(1,5,4,4,2),(2,67,31,31,22)` over `F_2` | `T^2=T`; fixed points are exactly totally isotropic subspaces | fixed census `sum_r [m choose r]_q product_(i<r)(q^(m-i)+1)` and orbit-wise radical fibres | classical symplectic/Witt enumeration; only one dynamical step | `KILL_WITT_RETRACTION_SHALLOW` |
| `GG03/MTE` | triples `(U,V,W)` of subspaces; simultaneously use `(U cap(V+W), V cap(W+U), W cap(U+V))` | for `F_2^3`: 4,096 states, 1,090 images/fixed points, maximum fibre 508 | the map is a retraction in every modular subspace lattice; fixed iff each coordinate lies in the sum of the other two | exact small-rank fibre histograms were computed, but no independent general fibre factorization emerged | lattice meet/join comparator; entire temporal axis collapses to one step | `KILL_MODULAR_RETRACTION_SHALLOW` |
| `GG04/PRC` | `p`-subgroups `P <= G`; replace `P` by `O_p(N_G(P))` | for `(S_4,p=2)`: 20 `p`-subgroups, 7 images, sharp observed height 2, maximum fibre 4 | inflationary; every strict step multiplies order by at least `p`; fixed points are precisely `p`-radical subgroups | conjugacy-equivariant fibres and radical-target counts | the Bouc/radical-subgroup literature directly owns the target class; the update also reuses P154's normalizer primitive | `KILL_DIRECT_P_RADICAL_OWNER` |
| `GG05/OMC` | labelled binary matroids; contract the first ground element and shift labels | for ground sizes `1..4`, representable matroid counts are `2,5,16,66`; at size four the image has 16 states and maximum fibre 9 | terminal after exactly `m` contractions; the `0/1` rank-drop word sums to the original rank | one-step target fibres and recovery of rank from the contraction word | contraction is a defining matroid minor operation; time is only ground-set deletion | `KILL_DIRECT_MATROID_MINOR_THIN` |
| `GG06/RCR` | subsets of a finite Alexandrov space; send `S` to `cl(int(S))` | among the 19 labelled three-point posets, the number of fixed regular-closed sets is 2, 4, or 8 with poset multiplicities 9, 9, 1; maximum fibre 4 | `T^2=T`; fixed points are regular-closed sets | complete finite fibres, but no positive-time axis beyond the retraction | classical closure algebra/Kuratowski regularization | `KILL_CLASSICAL_REGULARIZATION` |
| `GG07/MCS` | nonempty vertex subsets of a finite metric graph; replace by their Chebyshev-center set | on `P_6`: 63 states, 11 images, maximum fibre 21, tail at most 1; on `C_6` there are fixed points and 2-cycles | on `P_n`, the image is the `n` singletons plus `n-1` adjacent pairs and `T^2=T`; unrestricted graphs lose that theorem | midpoint target fibres on paths | graph-center theory owns the geometric primitive; the path restriction is a one-step midpoint extractor and the cycle extension is not monotone | `KILL_CENTER_OWNER_OR_UNSTABLE` |
| `GG08/MFS` | nonempty subsets of a graph metric; keep points maximizing distance to the subset | on `P_6`: 31 images, tail at most 3, one fixed state and 62 states ending in 2-cycles; `C_5,C_6` show the same dominant period-two pattern | exact maximum-empty-interval descriptions exist on paths/cycles, but no robust all-graph temporal theorem survived | image/fibre histograms do not produce target identifiability | antipodal/farthest-set shadow, period-two dominated, unstable under changing the graph family | `KILL_ANTIPODAL_SHADOW_UNSTABLE` |
| `GG09/EPC` | point subsets of `PG(d-1,q)`; retain precisely points whose deletion lowers the represented rank | on the Fano plane: 128 states, 57 images/fixed points, fibre histogram `1^49,5^7,44^1` | `T^2=T`; fixed sets are exactly projectively independent sets | fibres are coloop-decomposition counts/Tutte data | exact matroid coloop extractor; one step and internally adjacent to the matroid lane | `KILL_MATROID_COLOOP_RETRACTION` |
| `GG10/LPU` | line subsets of `AG(2,q)`; in each parallel class retain its line iff the class occupancy is exactly one, otherwise retain none | `q=2`: 64 states, 27 images, max fibre 8; `q=3`: 4,096 states, 256 images, max fibre 625 | `T^2=T`; fixed arrangements use at most one line in each direction | a target with `b` lines has exactly `(2^q-q)^(q+1-b)` sources | product over parallel classes is clean but completely owns the fibre; there is no second temporal axis | `KILL_PARTITION_EXTRACTOR_SHALLOW` |
| `GG11/ELP` | finite simplicial complexes; retain the induced complex on vertices whose link has odd Euler characteristic | on four labels: 167 complexes, 52 images, depth histogram `0:26,1:73,2:68`, maximum fibre 28 | the vertex set only decreases, so height is at most `n`; fixed complexes satisfy the local link-parity predicate | exact image/fibre data at `n=4`, no general target formula | arbitrary local pruning plus Euler-parity support; collides with occupied pruning/parity engines and lacks a second axis | `KILL_LOCAL_PRUNING_ENGINE` |
| `GG12/BPD` | finite simplicial complexes; replace the top-dimensional facets by the ridges contained in exactly one top facet and regenerate the complex | on four labels: 167 complexes, 24 images, depth histogram `0:1,1:34,2:132`, maximum fibre 35 | every nonempty step strictly lowers dimension, hence absorption by dimension plus one | exact boundary-target fibres only in the pilot | free-ridge/boundary primitive is directly classical; clock is dimension deletion and P67/topological pruning are close internal controls | `KILL_BOUNDARY_OWNER_THIN` |

## Proof notes behind the strongest exact checks

### `GG01/FTR`: fibre formula

Let `K=F_q^k`, `V=K direct-sum Q`, `dim Q=t`, and fix `W<=K` of
dimension `d`.  If `U cap K=W`, the projection of `U/W` to `Q` is an
`r`-subspace `A`, and `U/W` is the graph of a unique linear map
`A -> K/W`.  Thus there are `[t choose r]_q q^{r(k-d)}` choices at rank
`r`; summing gives the displayed every-target fibre.  This is exact and was
verified for every target with `k<=3,t<=2`.  It nevertheless packages a
static Schubert-cell decomposition under a forced flag clock.

### `GG03/MTE`: why the apparent descent is only one step

Write `U'=U cap(V+W)` and cyclically.  If `u in U'`, choose `u=v+w` with
`v in V,w in W`.  Then `v=u-w in V cap(U+W)=V'` and
`w=u-v in W cap(U+V)=W'`.  Hence `U' <= V'+W'`, and cyclically, proving
that the image is already fixed.  The exact enumerator caught this
one-step collapse before any longer proof program was opened.

### `GG04/PRC`: why the height signal is real but unavailable

For a `p`-subgroup `P`, normality of `P` in `N_G(P)` gives
`P <= O_p(N_G(P))`.  A strict step increases order by at least `p`, so every
orbit terminates.  The `S_4,p=2` pilot really has height two.  However, the
fixed objects are literally the standard `p`-radical subgroups, and their
homotopy role in the Brown/Bouc complexes is directly studied; P154 also owns
normalizer functional dynamics.  This is an owner hit, not a discovery.

### `GG10/LPU`: exact fibres cannot rescue a one-step system

Each of the `q+1` parallel classes contains `q` lines.  A target-occupied
class forces the unique selected source line.  A target-empty class allows
the empty source or any source subset of size at least two, giving
`1+(2^q-1-q)=2^q-q` choices.  Multiplication proves the formula.  The same
classwise argument also proves `T^2=T`, leaving no separate dynamics.

## Recommendation

Return `EMPTY_POOL` for this lane.  Re-entry should require a genuinely new
update mechanism with a state-dependent clock or nontrivial cycles plus a
separate exact fibre/recovery theorem.  It should not be obtained by adding a
tagged flag to `GG01`, randomizing `GG04`, or decorating any of the one-step
retractions above.

