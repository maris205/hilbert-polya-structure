# Idea ledger — P166 replacement discovery round 2

**Frozen outcome: `KILL_ALL`; lifecycle: `HOLD_EXTERNAL`.**

The ledger separates full literal enumeration from desk kills.  A desk kill
does not count toward the four newly exact-tested maps in `SCOUT.md`.

## Intake firewall

- Allowed carriers: finite automata, DAGs/posets, abstract complexes/clutters,
  matroids/greedoids/convex geometries.
- Excluded carriers: codes, matrices, permutations, finite-field points and
  word cellular automata.
- Permanent mechanism kills: repeated transitive closure, TC-spanners,
  pointer jumping, Horn/clique filling, generic closure, duality alone, rank
  erosion alone, and standard greedy algorithms.
- Required survivor conjunction: natural self-map + nontrivial all-parameter
  clock/core + all-time image or every-target fibres + boundaries + residual
  theorem mass after owner and P1--P165 subtraction.

## Candidate ledger

| id | literal system | early signal | inverse/image prospect | audit result |
|---|---|---|---|---|
| `A01/PFR` | acyclic orientations; reverse all current sources in parallel | periods already reach 6 on five vertices; tail reaches 3 | every-target roots are source-dominating subsets of target sinks | **exact-tested; `KILL_DIRECT_OWNER`**: Goles--Prisner study the same parallel dynamics |
| `A02/PSE` | strict posets; replace `<` by its relational square | `T^t=R^(2^t)`, logarithmic height clock | arbitrary targets ask for transitive relation roots | **sentinel replay only; prior literal S03 and pointer-jumping kill** |
| `A03/RTC` | DAG relation `R <- R union R^2` | logarithmic reachability-diameter clock | TC-spanner/minimal-root questions | **desk kill**: explicitly excluded repeated transitive closure |
| `A04/LDG` | replace a DAG by its line digraph | vertices of the `t`th iterate are directed paths | line-digraph roots | **desk kill**: not a fixed bounded carrier without orbit tagging; direct line-digraph iteration owner |
| `A05/IPA` | poset of proper intervals, iterated under containment | rank can initially grow; small cases lack monotone clock | interval-poset roots not target-local | **desk kill**: no stable temporal anomaly |
| `C01/USC` | complex `K -> K vee K`, faces are unions of two old faces | exact `2^t`-fold union and depth `ceil(log2 chi(K))` | stable simplex fibres from full-support complex counts | **exact-tested; `KILL_DIRECT_INGREDIENT_AND_P97`** |
| `C02/FNV` | complex to the nerve of its facets | double-nerve collapse toward incidence twins | roots are arbitrary set-system representations | **desk kill**: direct nerve/Dowker incidence plus P143 quotient silhouette |
| `C03/HBL-C` | clutter blocker followed by ground complement | period at most two on support | singleton/bijection fibres | **desk kill**: blocker is a directly owned involution; no transient mass |
| `C04/MPU` | clutter to inclusion-minimal pairwise unions | edge sizes tend to rise on pilots | minimal-union roots are global set-cover constraints | **desk kill**: unstable clocks and generic union closure |
| `C05/SFP` | complex with every current facet deleted | dimension/layer clock | inverse is arbitrary facet insertion | **desk kill**: exact prior `KILL_GENERIC_POSET_PEEL` |
| `M01/ASD` | matroid `M -> si(M)^*` with least-label representatives | simple/cosimple dual core, rank-changing tails | exact product fibre over every cosimple target | **exact-tested; `KILL_STANDARD_SIMPLIFICATION_RANK_EROSION`** |
| `M02/MUS` | independence complex of `M -> M vee M` (matroid union square) | `2^t`-fold matroid union; cover-number clock | matroid-union root problem | **desk kill**: Edmonds matroid partition/union and exact USC specialization |
| `M03/TRD` | matroid truncation, then duality, alternately | rank follows a sawtooth | fibres are erections/truncations | **desk kill**: classical truncation/erection plus rank erosion |
| `M04/CHR` | relax all circuit-hyperplanes simultaneously | typically idempotent or one-step | target roots are relaxation choices | **desk kill**: one-step projection and noncanonical interaction failures |
| `M05/BGR` | greedoid feasible-set rank truncation by one | linear rank clock | extensions are arbitrary feasible antichains | **desk kill**: rank erosion and no target-local inverse |
| `G01/CGP` | convex geometry; delete all extreme points of a closed set | exact extreme layers, sharp maximum `n` | rank-four geometries already show 28 fibre spectra | **exact-tested; `KILL_DIRECT_PEELING_OWNER_THIN`** |
| `G02/MEP` | poset ideals; delete all maximal elements | poset-height clock | cover-subset inverse inclusion--exclusion | **desk kill**: prior `KILL_MAXIMAL_LAYER_OWNER` |
| `G03/AEX` | antimatroid feasible sets; add all currently feasible continuations | closure in at most `n` | roots are prerequisite hypergraphs | **desk kill**: generic closure/Horn forward chaining |

## Why no candidate was promoted

`PFR` has the best one-step inverse axis but a direct paper owns the literal
parallel dynamical system.  `USC` has the cleanest clock, but the exact
operation, its iterated self-product notation, and the controlling chromatic
number are already explicit in the simplicial-complex literature; moreover
its proof engine duplicates P97.  `ASD` has the cleanest every-target product,
but it merely counts loop/parallel extensions under standard simplification.
`CGP` is natural but is literally onion peeling in an abstract convexity and
has no uniform target formula.

No fifth candidate was promoted to compensate.  The lane is intentionally
closed as `KILL_ALL` rather than padded to fill P166.

