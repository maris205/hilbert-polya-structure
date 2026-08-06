# R058 Hyperbolic Survivor and Filament Replication Analysis

**Completed:** 2026-08-02
**Frozen protocol:** bdd851ac14fb5cbe89ce4592b4f0e9f6cbe4fa4b76778530a2e19e7e0f1dd6f3
**Decision:** C1 theorem PASS; C2 graph replication PASS; independent checker PASS
**Evidence levels:** exact covering/cone theorem plus locked exact finite-grid replication

## 1. Main outcome

R058 closes the main logical gap left by R054--R057. The finite graph is no
longer asked to manufacture a common orbit witness. Six exact h-set
coverings, ten exact forbidden transitions, and strict two-sided cone
bounds certify a nonempty compact uniformly hyperbolic survivor subset.
Its itinerary map is a continuous surjection onto the frozen four-state
subshift, so

\[
h_{\rm top}(H_6|_\Lambda)\ge\log\varphi
\approx 0.481211825.
\]

This is a semiconjugacy and entropy lower bound, not a conjugacy, entropy
equality, or Markov-partition claim.

The separate nine-grid true-positive replication also passes every frozen
gate. Its three multilevel lineages reproduce near-one-dimensional node
growth, shrinking physical area, approximately one-half descendant
coverage, and the exact six-transition symbolic skeleton.

## 2. Exact theorem certificate

| Quantity | Exact value | Decision |
|---|---:|---|
| Allowed coverings | 6 | PASS |
| Forbidden transitions excluded | 10 | PASS |
| Minimum exit margin | 1/48 | PASS |
| Minimum entry margin | 1/128 | PASS |
| Forward cone slope bound | 25088/95079 | < 1/2 |
| Backward cone slope bound | 15129/45388 | < 1/2 |
| Forward expansion squared | 597529/62720 | > 1 |
| Backward expansion squared | 2627641/302580 | > 1 |
| Spectral radius | (1+sqrt(5))/2 | exact |

## 3. Raw locked configuration table

| Configuration | Offset | Kmax | Active cells | Positive edges | Canonical positive SCC | Lineage SCC |
|---|---:|---:|---:|---:|---:|---:|
| n112_d0 | 0 | 31 | 2909 | 36500 | 568 | 568 |
| n224_d0 | 0 | 31 | 12133 | 146080 | 1190 | 1150 |
| n448_d0 | 0 | 31 | 49489 | 584480 | 2461 | 2358 |
| n113_dp1_12 | 1/12 | 37 | 2964 | 37176 | 576 | 576 |
| n226_dp1_6 | 1/6 | 43 | 12352 | 148693 | 1194 | 1154 |
| n452_dp1_3 | 1/3 | 62 | 50400 | 594869 | 2560 | 2453 |
| n113_dm1_12 | -1/12 | 37 | 2969 | 37164 | 562 | 562 |
| n226_dm1_6 | -1/6 | 43 | 12344 | 148715 | 1215 | 1175 |
| n452_dm1_3 | -1/3 | 62 | 50391 | 594847 | 2445 | 2388 |

All nine cap counts are zero. The two finest shifted grids reach
uncapped K=62, leaving only two subdivisions of headroom under the
frozen cap of 64, but their exact integrity checks still pass.

## 4. Multilevel lineage replication

| Chain | Lineage sizes | Exact areas | 4x exponent d | Area exponent d-2 | Coverages | Decision |
|---|---|---|---:|---:|---|---|
| centered | 568 -> 1150 -> 2358 | 0.073726 -> 0.037317 -> 0.019129 | 1.026800 | -0.973200 | 0.506162 / 0.512609 | PASS |
| positive_phase | 576 -> 1154 -> 2453 | 0.073447 -> 0.036787 -> 0.019549 | 1.045203 | -0.954797 | 0.500868 / 0.531412 | PASS |
| negative_phase | 562 -> 1175 -> 2388 | 0.071662 -> 0.037457 -> 0.019031 | 1.043580 | -0.956420 | 0.522687 / 0.508085 | PASS |

Aggregate replication:

- mean lineage exponent: 1.038528;
- R056 positive-SCC slope: 1.038202;
- mean difference from R056: +0.000326;
- mean physical-area exponent: -0.961472;
- six-step coverage mean/median: 0.513637/0.510347;
- coverage range: 0.500868--0.531412.

The mean R058 exponent differs from the R056 positive slope by only
about 0.00033. This is a strong deterministic replication of the
selected filament-compatible scaling model. It is still not a
dimension theorem or graph-limit statement.

The lineage is intentionally not replaced by the largest child SCC.
At the middle levels it retains about 96.6%--96.7% of the canonical
largest-SCC size; at the finest levels it retains about
95.8%--97.7%. Thus the pass is not caused by silent branch switching.

## 5. Symbolic bridge

| Finest configuration | State cell counts (--,-+,+-,++) | Observed transitions | Extra transitions |
|---|---|---:|---:|
| n448_d0 | 216,160,160,106 | 6 / 6 | 0 |
| n452_dp1_3 | 226,183,183,112 | 6 / 6 | 0 |
| n452_dm1_3 | 230,162,162,110 | 6 / 6 | 0 |

Every finest lineage contains all four h-set states and realizes
exactly the six certified transitions, with no forbidden state
transition. This is a useful finite-grid bridge to the exact
survivor, but C1 remains proved by covering relations rather than by
this incidence observation.

## 6. Finest-grid phase overlap

| Pair | Geometric Jaccard | Intersection / first | Intersection / second |
|---|---:|---:|---:|
| centered vs positive_phase | 0.724958 | 0.849780 | 0.831522 |
| centered vs negative_phase | 0.711797 | 0.829507 | 0.833778 |
| positive_phase vs negative_phase | 0.634369 | 0.766001 | 0.786851 |

The Jaccard range is 0.634369--0.724958, with median 0.711797. Phase dependence remains
visible, but a large common geometry survives.

## 7. Independent checker

- complete microgrids: 6,497 source-target pairs;
- frozen held-out source sweeps: 288 sources and 25,591,104 source-target pairs;
- all nine NPZ schemas and hashes independently reloaded;
- all six complete and matched-support projections independently rebuilt;
- three multilevel lineages and three symbolic bridges independently rebuilt;
- theorem matrix and cone fractions independently recomputed;
- final checker decision: True.

## 8. Difference from the frozen expectation

1. C1 is stronger than the previous finite-grid hope. R058 now has an
   actual compact uniformly hyperbolic survivor and entropy lower
   bound, not merely persistent SCCs.
2. C2 lands almost exactly on the R056 selected positive scaling:
   mean d=1.038528 versus 1.038202.
3. All six descendant coverages lie between 0.5009 and 0.5314,
   slightly above but fully compatible with the frozen half-core
   hypothesis.
4. The symbolic bridge is cleaner than minimally required: every
   finest lineage has all six allowed transitions and zero extras.
5. The no-cap stress remains genuine: K=62 is close to 64, but no
   cap or post-freeze repair was needed.

## 9. Scope boundary

R058 proves a conservative hyperbolic subset at a=6. It does not prove
that the full Hénon horseshoe, the whole finite-grid filament, or the
open transfer operator is represented by these four h-sets. It does
not establish graph convergence, operator convergence, a zeta
identity, a Riemann-zero relation, RH, or a Hilbert--Pólya operator.

## 10. Recommended next runs

1. Classify the existing exact period-1--12 a=6 orbit catalog by the
   four h-sets and compare certified symbolic words with trace(A^n).
2. Freeze an interval search for wider rational h-sets or a richer
   transition graph, aiming to raise the entropy lower bound without
   weakening cone margins.
3. Build one operator and one cycle expansion restricted to the
   certified survivor, removing the old ambiguity about the common
   dynamical domain.

## 11. Artifacts

- research/refine-logs/R058_HYPERBOLIC_FILAMENT_PROTOCOL.json;
- research/refine-logs/R058_HYPERBOLIC_FILAMENT_MANIFEST.md;
- R058_COVERING_DERIVATION.md (SHA-256 `5006e6e2d3d1e75382b495be9ec52d6fdf6b90442320b7f3457f9746a00f3e13`);
- R058_COVERING_PROOF.md (SHA-256 `c73188a079df87c93812f1dd5d90e0110a68d8f91780fea22bd779d40f4f59fe`);
- research/refine-logs/R058_HYPERBOLIC_THEOREM_AUDIT.md;
- scripts/audit_hyperbolic_covering_r058.py;
- scripts/audit_hyperbolic_filament_r058.py;
- scripts/check_hyperbolic_filament_r058.py;
- results/hyperbolic_covering_r058.json;
- results/hyperbolic_filament_r058.json and CSV;
- results/hyperbolic_filament_r058_edges/*.npz;
- results/hyperbolic_filament_independent_check_r058.json;
- results/hyperbolic_filament_analysis_r058.json.
