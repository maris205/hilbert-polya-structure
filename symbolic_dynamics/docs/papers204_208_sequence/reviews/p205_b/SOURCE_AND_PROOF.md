# P205 manuscript Review B: deductive and source attacks

Reviewer `/root/batch197_lzk_gate`, 2026-09-05 UTC. Scientific input is
`papers/205-conflict-triggered-cyclic-increments/frozen_round1/`, pinned by
[INPUT_PINS.sha256](INPUT_PINS.sha256). This is a new nonauthor manuscript
review, not the candidate gate, Review A, an external referee, or a proof
authorship contribution. No paper text was changed or supplied by B.

## Independence and actual read boundary

I read the complete frozen manuscript, all eight TeX/bibliography files,
PROOF_PACKAGE, claim/source/plan/narrative records, lifecycle and author
execution/build descriptions. The frozen author implementation, its
canonical and raw run files were **hashed only**, never read, imported or
executed. I read A's REPORT and accepted DELTA to establish the lifecycle,
not A's code/canonical or the candidate gate's code/canonical. Author/root
are P205's mathematical/manuscript contributors; A is the distinct
`/root/batch197_fosp_gate` process. I did not scout or gate CCI.

B's [verify.py](verify.py) was written from the literal rule and independently
chosen representations: Boolean total-weight walk layers; Kosaraju strongly
connected components and reverse breadth-first distances; subsets of **old
conflict edges**. No priority-queue arrival simulation, Floyd distances,
zero-indegree peeling, advancing-mask enumeration or held-set enumeration
is used. The only explicit selected-vertex examples are three fixed negative
controls; static P4 independent sets are a separate eight-set boundary test.

The project research workflow, proof-writer, research-review and compilation
skills organized the proof/source/build obligations. The requested current
model, local process separation and owned output directory control over
provider/upload defaults. No external review API, specialist contact or
manuscript upload was used. All four team slots were occupied; no third
process's assessment is implied.

## 1. Construct the entire trajectory before simulating it

Let `d(v)` be the initial-colour nonnegative directed distance in the paper;
take `d(v)=infinity` outside seeded components. Shortest walks can have
cycles deleted, so finite minima are attained. Every zero-weight edge is
initially monochromatic, and both endpoints are seeds. In particular, an
edge entering a nonseed cannot have weight zero.

Define, without referring to actual activation times,

`z_v(t) = x_v + max(0,t-d(v)) mod q`,

with the added term zero at infinite distance. I verify directly that the
conflict indicator in `z(t)` is exactly `1[t >= d(v)]`.

**Before the proposed time.** Fix `t<d(v)`. If a neighbor `u` also satisfies
`t<d(u)`, both candidate colours are initial colours. Equality would make
`v` a seed, a contradiction. Otherwise `d(u)<=t` is finite. If the two
candidate colours were equal, the nonnegative integer `t-d(u)` would be
congruent to `w_x(u,v)` modulo `q`, hence at least that least nonnegative
residue. The shortest-path inequality would give

`d(v) <= d(u)+w_x(u,v) <= t`,

again a contradiction. This also excludes an infinite-distance vertex's
having an active neighbor: that edge would give it a finite route.

**From the proposed time onward.** If `v` is a seed, one initially equal
neighbor is also a distance-zero seed, and their two `z` coordinates remain
equal. For a nonseed of finite distance, choose a minimum seed route and
its last edge `u -> v`. Its prefix is minimum as well, so

`d(v)=d(u)+w_x(u,v)`.

The last weight is strictly positive, as noted above. Therefore `d(u)<d(v)`.
For all `t>=d(v)`, subtracting the two candidate colours yields

`z_v(t)-z_u(t) = x_v-x_u-d(v)+d(u) = 0 mod q`.

So `v` has a same-coloured neighbor at every such time. This proves the
indicator identity for all vertices and integer times, not just a cutoff.
It implies `z(t+1)=F(z(t))` and `z(0)=x`. Uniqueness of iteration proves
the all-time coordinate formula and the exact first-conflict times.

This is a direct trajectory-certificate proof. It does not start with
irreversible activation and backtrack actual first events as the author
does, nor use A's event queue. It independently confirms the manuscript
proof's delicate zero-weight, simultaneous-first-event and infinity cases.
The colour is still its initial value at the first conflict time; its first
increment caused by that conflict is the update to the next time. The
negative control `(0,0,1)` on P3 distinguishes these two times.

## 2. Core, exact entrance and sharp all-parameter clock

All vertices of each seeded component have finite `d`; no seedless
component moves. At `h=max finite d`, every seeded component advances
globally and every seedless component is proper and fixed. Thus `F^h(x)`
is periodic. A same-colour edge persists because its endpoints advance
together, so the active set is monotone. At a time before `h` it will gain
a vertex later; a periodic orbit cannot have that strict future gain. This
proves least entrance, not merely an upper bound. Conversely a state with
each component either proper or entirely active immediately has the stated
periodic action. Any advancing coordinate forces a return time divisible by
`q`, so every nonfixed recurrent orbit has exact period `q`, even when
mixed with fixed components and isolates. Empty graphs and the empty
carrier are included.

A seeded component contains two distinct seeds. Delete cycles and truncate
at the last seed of a shortest route to any nonseed. This leaves at most
`n-2` edges, each of weight at most `q-1`; all finite distances obey the
claimed bound. No nonseed can coexist with a seed edge at `n<=2`. On the
specified path with first colours `0,0` and successive differences `-1`,
the only initial seed edge is the first one, all later forward weights are
`q-1`, and the unique simple route attains `(q-1)(n-2)`. Backtracking never
reduces weight; its two opposite nonzero weights sum to `q`. This proves
sharpness for every stated `n,q`, without extrapolating the finite tests.

The checker constructs the complete literal functional graph, finds SCCs
in two DFS passes, identifies nontrivial SCCs and singleton self-loops, and
propagates depths and eventual periods backwards. Its distance computation
instead forms the Boolean coefficients `R_t` of all seed walks by total
weight, with same-time zero-edge closure. A simple-route bound
`(q-1)(n-1)`, deliberately not the theorem's sharp `n-2`, is its horizon.
Every state's literal iterates through `h+2q+1` and exact activation bits
are compared, in addition to SCC depths and periods. The all-time theorem
rests on the preceding proof, not the finite window.

## 3. Eliminate old conflict EDGES to audit the inverse

Fix a target `y`, and introduce an unknown set `C` of old equal-colour
edges, not a vertex mask. Every endpoint of an edge in `C` advanced; its
other endpoint advanced too. Such an edge therefore remains equal in `y`:
necessarily `C` is a subset of `E(H_y)`. Define `A=endpoints(C)` and
reconstruct `x=y-1_A`. This is a genuine source exactly when, on **every**
edge of `G`, old equality occurs if and only if that edge belongs to `C`.
If this holds, the literal old active set is exactly `A`, so `F(x)=y`.
Conversely every actual source supplies its unique full equality-edge set
`C` and is recovered. Thus edge-consistent solutions biject with sources.

Eliminating `C` from those edge constraints recovers precisely the paper's
three conditions; this verifies necessity and sufficiency independently.

| Target-edge/endpoint case | Consequence of exact old-edge consistency |
|---|---|
| Edge in `H_y`, both outside `A` | Old equality would activate them: forbidden. Thus `A` covers `H_y`. |
| Edge in `H_y`, both in `A` | Old equality holds, so the edge must be in `C`. Thus `C=E(H_y[A])`. |
| Edge in `H_y`, one endpoint in `A` | Old colours differ by one, so it is not in `C`. |
| Nonmonochromatic target edge, both in or both out | Their common shift preserves inequality, so it is not in `C`. |
| Nonmonochromatic edge `u` out, `v` in | Old equality is equivalent to `y_v=y_u+1`; such an incoming arc is forbidden. |

The remaining equation `A=endpoints(C)` with `C=E(H_y[A])` says exactly
that every selected vertex has an internal `H_y` neighbor. Isolates are
therefore forced out. The incoming-arc prohibition is predecessor closure,
including chains by transitivity. Empty `A` is permitted when the target
has no equal edge. Distinct `A` give distinct sources because the two
allowed coordinate shifts are distinct modulo `q>=3`; two edge solutions
with one `A` cannot differ because `C=E(H_y[A])`. This also explains the
checker's injectivity test on reconstructed source encodings.

There is no assertion of polynomial-time recognition/counting, independent
per-vertex choices, or all-time inverse enumeration. The checker enumerates
all `C subset E(H_y)`, applies the **literal old equality test**, and
compares the whole source set against reverse buckets of the complete
literal function, including empty fibres. Cardinality agreement alone is
not the oracle. Removing any of the three conditions admits a false source;
three concrete witnesses and their wrong literal images are in the actual
canonical output.

## 4. Static support and transfer of every equality case

The inequality `|F^-1(y)| <= T(H_y)` drops predecessor closure only.
Constant targets have no predecessor arcs, giving equality. I independently
checked the paper's connected-nonstar argument: a longest path of length
at most two forces a connected graph of at least four vertices to be a
star; otherwise P4 is a (not necessarily induced) subgraph. Connectedness
supplies a P4-to-outside edge at order at least five. P4 has eight
independent sets, with respective vertex-containment counts `3,2,2,3`.
The additional edge excludes at least `2*2^(k-5)` of the relaxed choices,
so `T(H)<=7*2^(k-4)<2^(k-1)-1`. The strict inequality begins at `k=5`,
not `k=4`; the six connected four-vertex graphs are handled separately
with counts `7,4,6,5,6,5`. They are exhaustive and their edge-set counts
are reproduced independently. No induced-P4 assumption is smuggled in.

Component products and the forced exclusion of isolates give the strict
disconnected cases. At order three, the triangle count four beats the path
count three; a disconnected graph has count one. At order at most two the
map itself is a permutation. Hence the stated static upper bounds and
all equality graphs are valid. For a dynamically extremal target, equality
forces `H_y` to be a **spanning connected** star/triangle. Its equal-colour
edges force `y` constant globally. Now `H_y=G`, excluding any extra
nonmonochromatic edge in the original graph. Conversely constant targets
on those exact graphs attain the bound. This last transfer is necessary;
the static extremum alone would not classify dynamical equality pairs.

The elementary static lemma is fully proved but receives zero independent
novelty credit. The finite static census stops at order five, with larger
star checks through fourteen; no all-six-vertex graph audit is claimed.

## 5. Direct primary sources: actual context and limits

The four manuscript DOI records were fetched afresh by ordinary HTTPS
content negotiation (`Accept: application/x-bibtex`), all with child exit
zero, and are retained under [sources/](sources/). The initially mistyped
reviewer query `10.1109/INFOCOM.2009.5062046` returned 404/exit 22; it is
not the manuscript DOI and is not a manuscript finding. The correct DOI
below succeeded. Abbreviated author names and the missing Gravner page
range in those metadata records are completed by the actual primary PDFs,
not treated as discrepancies.

- **Motskin, Roughgarden, Skraba and Guibas (2009).** Read title, Section
  II-A and Algorithm 1 in the nine-page [author PDF](https://www.timroughgarden.algorithmsilluminated.org/papers/desync.pdf).
  The information model permits the current colour and a conflict bit,
  hence contains the deterministic local choice in P205. The displayed
  algorithm resamples randomly. Model ownership and conflict detection are
  fully deducted; no randomized convergence bound transfers to permanent
  CCI conflicts. [Correct DOI](https://doi.org/10.1109/INFCOM.2009.5062165)
  confirms INFOCOM 2009, 2383–2391. A local PDF download returned 406;
  browser primary-page access succeeded and was read. No successful local
  Motskin PDF archive is claimed.
- **Gravner, Lyu and Sivakoff (2018).** Read title/journal header and
  Sections 1–2 through the initial edge 1-form/path-integral comparison,
  including the ordinary CCA/GHM rules and Lemma 1 in the
  [author-hosted journal PDF](https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf).
  CCA tests for a successor colour, not equality. Its 3-colour lift uses
  signed increments and maxima of path integrals under a time/length
  constraint. P205 instead uses nonnegative initial residue waiting costs,
  seed-set minima and clocks that permanently start on equality. On K2 a
  constant colouring is fixed for CCA but moves in a q-cycle for CCI. The
  familiar path/lift methods receive no credit. This is not a theorem
  excluding enriched factors or every possible conjugacy, nor a claim of
  reading the entire 34-page proof. [DOI](https://doi.org/10.1214/17-AAP1350).
- **Fernau, Fomin, Philip and Saurabh (2015).** Read title/footer, the
  t-total-cover definition on PDF page two and parameterized-algorithm
  framing in the [author-hosted journal PDF](https://fedorvf.github.io/articles/2015/2015f.pdf).
  Requiring all selected connected components to have at least two
  vertices is exactly the no-isolated-selected-vertex condition. This
  counting object is prior, including the earlier conference work cited
  there; P205 explicitly states its empty/isolate conventions. Neither a
  new cover object nor a new general counting algorithm survives as a
  contribution. [DOI](https://doi.org/10.1016/j.tcs.2014.10.035).
- **Molinero, Riquelme and Serna (2018).** Read the cover/title metadata,
  Section 2's definition context, Lemma 2.3, Theorem 2.4 sketch and
  Corollary 2.5, and the subsequent related-results/references text in the
  seven-page [UPC final draft](https://upcommons.upc.edu/bitstreams/331d37a2-b15a-44a0-9de1-85a36f5f6d7b/download).
  The negated condition is read on the complement `V\X` appearing in
  Lemma 2.3: every selected vertex has a selected neighbor. General
  total-cover counting complexity is already treated. Corollary 2.5
  supports P205's bounded complexity citation, without importing an
  algorithm for its extra predecessor constraint. Browser download failed;
  ordinary public curl download succeeded without credentials. The locator
  is PDF page six including the cover, not an independently verified
  typeset page 201. [DOI](https://doi.org/10.1016/j.endm.2018.06.034).

The three local PDF hashes are:

| Snapshot | SHA256 |
|---|---|
| `sources/Gravner2018.pdf` | `b77521e5f1d84aac5cfbe86b97d532550f3a4fd0f1aae2544d39cddbc8f3005c` |
| `sources/Fernau2015.pdf` | `9468ba79295aa2f8ae7ebbc5699b725bd5c140c4d349f8db9cdbb6f6f994ce71` |
| `sources/Molinero2018.pdf` | `50768214c2cfa283667fff4a04d23f6dfd2c75e7d9fc8772dfe533fbe8be4b93` |

A fresh additional search located Marsan, Sablik and Törmä's 2026
*A Perturbed Cellular Automaton with Two Phase Transitions for the
Ergodicity*. I opened the [publisher's primary article](https://link.springer.com/article/10.1007/s10955-025-03564-0)
and read its introduction and Section 3's literal counter/arrow rule. The
counter layer without arrows advances everywhere every round; arrows
propagate right and reset/synchronize counters, and the full alphabet has
an additional Gács layer. It is not equality-triggered CCI on arbitrary
finite graphs. The matching search phrase did not expose a literal-map or
full-theorem adapter. I did not audit its entire ergodicity proof. This
additional source is not silently added to the frozen bibliography.

Fresh searches also used `cellular automaton "same color" "increment"
graph`, `deterministic "conflict detection" "cyclic" coloring`, and
`"cyclic" "total vertex covers"`. They produced no additional supported
full owner/adapter. Search non-hits are not global originality evidence.

## 6. Internal full-adapter attacks and what survives

I inspected the actual named manuscript equations and theorem contexts,
not their verifiers: P118 setup/multipartite quotient and recurrence
sections; all of P164's manuscript; P202's rule, inverse/run/temporal
sections; and the complete old Bellman THEOREM_SPIKE. Their exact pins are
recorded below. These are bounded relevant reads, not claims to re-review
every historical artifact.

| Candidate identification | Literal deduction and obstruction |
|---|---|
| P118 synchronous mex | Its output is a least absent neighbor colour, regardless of equality; its complete-multipartite recurrence has only periods 1 and 2. Already on K2 a monochromatic source has a CCI q-cycle, q>=3. A same-carrier conjugacy to that mex family cannot preserve this cycle length. Mex/graph-colouring vocabulary does not supply CCI's coordinate clock or inverse. |
| P164 equality feedback | Its coordinate is the binary equality bit, not the old colour plus the conflict bit. The first image is binary and the dyadic tail is affine Rule 102 with a unique fixed recurrent point. CCI retains colour phases and has q-cycles; its first image is not binary. The literal equality observation is deducted, but this binary tail is not a conjugate/complete adapter. |
| P202 ternary ordered reset | Its directed right-neighbor order/reset rule sends every 0 to 1 and has powers-of-two one-step fibres. A proper CCI colouring is fixed, and a constant target on the four-vertex CCI star has fibre 7. Thus the exact P202 inverse cannot be transferred by a permutation conjugacy, which preserves fibre sizes. Global advance on some recurrent states is only shared background. |
| Old graph Bellman spike | Its fixed map is `T(x)_v=min(x_v,min_{u~v}(x_u+1))`; all orbits become fixed and its weights are graph-distance units. CCI is not this map: it has q-cycles and source-dependent residue costs. Distance computation is a zero-credit Bellman primitive, but an orbit-specific encoding using the already-solved CCI distances is not a prior state-space conjugacy and does not transport target preimages. |

The distinction is not merely a different cutoff or coordinate label. On
P3, the sources `(0,0,1)` and `(0,0,2)` at q=3 have the same initial
conflict endpoints yet activation vectors `(0,0,1)` and `(0,0,2)`.
The seed/equality mask alone does not close the clock. Also the P3 targets
`(0,1,1)` and `(0,2,2)` have identical monochromatic graph H but fibre
sizes zero and one: total covers of H alone do not decode the target;
the directed target relation matters. The canonical evaluates both tests.

These explicit obstructions defeat the proposed direct/full transfers;
they do **not** exclude arbitrary enlarged state spaces, restrictions,
time changes or future adapters. Generic shortest paths, irreversible
activation, conflict-bit models, binary reconstruction, total-cover
objects/counting and elementary independent-set bounds all receive zero
ownership credit. After those deductions, the narrow residual is the
literal CCI rule's all-time source-colour clock plus the separate
target-colour inverse and sharp dynamical equality transfer. No inspected
source supplied that full conjunction. This is sufficient for the scoped
internal review, not an external priority certificate.

Historical original pins (workspace-relative):

| File | SHA256 |
|---|---|
| `papers/118-synchronous-mex-multipartite-dynamics/main.tex` | `9433fc69d5e8d4cc5e508e1f893c3f155d197eb6ebac9e7e874bde7d49676082` |
| `papers/164-cyclic-equality-feedback/main.tex` | `6a589c778137cb6e039f7a01710e7264686c6952321f0494ee3c992bfcda4218` |
| `papers/202-ternary-ordered-reset/main.tex` | `bcb24151784b52a27d846dd564ab6a0b438381e617575e6064c698f69683fa1a` |
| `docs/papers197_201_sequence/scouting/root_graph_bellman/THEOREM_SPIKE.md` | `b4e093c44b41a7a8a09c00d202c2bc9d45bc3f05f177d54958e65546552cedd4` |

Conclusion: all stated all-parameter proofs withstand these attacks;
the inverse is target-resolved and the extrema include their equality
classification. Retain only that bounded conjunction, with
`OWNER_AMBER / HOLD_EXTERNAL`. No manuscript repair is requested by B.
