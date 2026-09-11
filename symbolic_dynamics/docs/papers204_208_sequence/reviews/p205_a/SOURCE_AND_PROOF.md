# P205 Review A — source contexts and deductive audit

2026-09-05 UTC. Status: **PROVABLE AS STATED / NARROW OWNER-AMBER SCOPE**.
This audits the frozen manuscript's own arguments. No missing lemma was
provided, no theorem was weakened and no manuscript text was authored.
Input and execution provenance are in [REPORT.md](REPORT.md),
[INPUT_PINS.sha256](INPUT_PINS.sha256) and
[SUPPLEMENTARY_INPUTS.sha256](SUPPLEMENTARY_INPUTS.sha256).

## Exact assumptions and dependency map

The literal carrier is $(\mathbb Z/q\mathbb Z)^V$ for a finite simple
undirected graph, $q\ge3$, including $V=\varnothing$. All updates use the
old state; a vertex increments once iff an old neighbor has equal colour.
An isolate never increments. The first conflict time is not the time of
the first changed coordinate. Empty maxima are zero, and empty covers are
allowed. No graph-connectivity or palette-size-versus-degree assumption
is silently introduced.

1. Persistent equal edges imply single activation and the coordinate formula.
2. First meetings plus strictly backward-traced activation events identify
   activation times with the stated directed seed distances.
3. Seed-component exhaustion identifies the exact recurrent core and
   entrance; a seed-avoiding simple path gives the upper bound and the
   displayed path colours give sharpness.
4. Separately, old/target equality in each held/advancing endpoint case gives
   a complete target mask characterization.
5. The established static cover object bounds the fibre; the paper's
   elementary static proof determines equality, and monochromatic
   connectivity transfers it back to the whole graph and target.

The dependencies do not run from temporal distances to the inverse theorem.
There is no external graph-counting theorem being used as an unproved
substitute for Lemma 3.2, nor a finite-experiment extrapolation.

## Temporal proof attack

At first conflict time $a$, a vertex still has its initial colour and only
the update $a\to a+1$ changes it. Thus an already active neighbor at time
$a$ meets a stationary vertex of initial colour difference $r$ at $a+r$,
with $r\in\{0,\ldots,q-1\}$. If that stationary vertex was activated
elsewhere sooner, the edge inequality remains an upper bound. A zero
residue is an initial equal edge, so both endpoints are already seeds.
These facts validate the forward path inequality without assuming a unique
front or changing an oriented residue to its reverse.

For the reverse inequality, a first positive-time conflict cannot have
two newly activated stationary endpoints: their equality would have been
initial. A witness neighbor therefore activated strictly earlier. Its
first meeting with the stationary vertex is the least nonnegative residue
wait; any earlier congruent meeting would contradict the definition of the
first conflict time. Following such witnesses decreases a nonnegative
integer time at every step, reaches time zero, and gives a seed path of
exactly the claimed weight. This also rules out activation in a seedless
component. The manuscript explicitly contains both inequalities and this
termination argument.

At the maximum finite arrival time, every seeded component is fully active
and rotates, while every unseeded component is proper and fixed. A state
earlier on an orbit cannot already be periodic if its monotone active set
will later grow. Thus the stated time is exact entrance, not only an upper
bound. On the recurrent core, any advancing coordinate forces a return
time divisible by $q$; global addition gives period $q$, and an entirely
proper state has period one. Disconnected mixtures cause no additional
period.

A shortest seed-to-nonseed path can be chosen simple and have no other
seed after the start. At least one further seed is therefore omitted, so
it has at most $n-2$ edges. The manuscript's path has only its initial
equal edge seeded and every remaining forward residue is $q-1$. Positive
backtracking cannot create a shorter arrival. The empty graph and
$n\le2$ are correctly separated. No gap is filled by the reviewer's
finite path check.

## Inverse proof attack through held sets

Write $I=V\setminus A$ for the held set and $R=V\setminus I$ for the
advancing set. This is a reviewer representation of the existing theorem,
not a new claim. Its three conditions become:

- $I$ is independent in the target monochromatic graph $H_y$;
- every vertex of $R$ has an $H_y$ neighbor in $R$;
- $I$ is successor-closed in $D_y$.

For both endpoints in $R$, subtracting one preserves target equality and
produces exactly the required old triggering edges. For both endpoints in
$I$, a target equality is an old equality and would contradict holding.
Across $I$ to $R$, old equality occurs exactly on a target successor arc,
which is forbidden by held-set successor closure. These exhaust the
undirected edge cases, so the reconstructed source has advancing set
exactly $R$ and maps to $y$. The target and held set determine the source
uniquely. This checks the manuscript's sufficiency as well as necessity.

The independent checker automatically finds actual counterexamples when
each of these conditions is individually dropped. It compares full
predecessor sets with the literal map, not merely fibre sizes. Its explicit
$q=3$ path timeline $002\to112\to222\to000$ separately checks activation
at time two versus first increment at time three. The $001/002$ pair has
the same initial active set but different next active sets, so merely
discarding colours does not supply an autonomous Boolean flooding map.

## Static support and equality attack

For each connected nonstar of order at least four, the longest-path
argument indeed supplies a four-vertex path as a subgraph, not necessarily
an induced path. When the order is at least five, connectivity supplies
an edge from that path to an outside vertex. There are eight independent
sets on the path, and each chosen path vertex belongs to at least two.
The extra edge excludes at least $2\cdot2^{k-5}$ choices from the
$8\cdot2^{k-4}$ overcount. This verifies the displayed
$7\cdot2^{k-4}<2^{k-1}-1$ for $k\ge5$.

At order four, the connected graphs with three edges are the path and
star; those with four are the cycle and paw; five and six edges give the
diamond and complete graph. Thus the manuscript's six-case list is
exhaustive. Their total-cover counts, independently recomputed using held
complements, are $7,4,6,5,6,5$ in the manuscript's stated order. This
finite boundary calculation is a legitimate part of the proof, not an
assumption about larger graphs.

Total-cover counts multiply over components, with an isolate contributing
one. Two nontrivial components have the strict factor bound written in
the paper. A single smaller component plus isolates also gives strictness,
including the triangle value four. The edgeless count is one. Therefore
the exact static equality classification includes all disconnected cases.

The decoder bounds each fibre by $T(H_y)$ and constant targets attain that
bound. A maximum at $n\ge4$ forces a spanning monochromatic star; at
$n=3$ it forces a triangle. Connectivity makes all target colours equal,
so $H_y=G$ and no extra edge can remain outside the monochromatic graph.
Conversely those targets attain the counts. The single-edge map is a
permutation: unequal states hold, equal states rotate. This covers all
$n\le2$ cases, including the empty state.

## Primary citation contexts actually inspected

The read scopes below are bounded. They do not assert reading all proofs
in the cited papers. Bibliographic metadata and each actual manuscript use
agree; no incorrect “Hosseini 2013” record or unverified journal-page
locator remains in the frozen bibliography.

| Source and readable primary locator | Actual passage / allowed use |
|---|---|
| Motskin, Roughgarden, Skraba and Guibas, *Lightweight Coloring and Desynchronization for Networks*, INFOCOM 2009, 2383–2391, DOI [10.1109/INFCOM.2009.5062165](https://doi.org/10.1109/INFCOM.2009.5062165); [author PDF](https://www.timroughgarden.algorithmsilluminated.org/papers/desync.pdf) and [institutional metadata](https://www.seresearch.qmul.ac.uk/cfcs/publications/2009/) | PDF p. 2, Section II-A and Algorithm 1, with the theorem context on p. 3. The local conflict-bit model permits this rule but the selected source algorithm randomizes on conflict. The draft deducts the model and does not transfer randomized convergence. |
| Gravner, Lyu and Sivakoff, *Limiting behavior of 3-color excitable media on arbitrary graphs*, AAP 28(6), 3324–3357 (2018), DOI [10.1214/17-AAP1350](https://doi.org/10.1214/17-AAP1350); [author journal PDF](https://www.math.ucdavis.edu/~gravner/hidden/clanki/AAP_2018.pdf) | Title/header and Section 1, PDF p. 2 / journal p. 3325, literal GHM/CCA equations; nearby comparison context on p. 3 was also read. The successor-trigger CCA holds on a monochromatic edge, unlike the manuscript rule. The draft asserts that literal separator, not impossibility of all enriched factors. |
| Fernau, Fomin, Philip and Saurabh, *On the parameterized complexity of vertex cover and edge cover with connectivity constraints*, TCS 565, 1–15 (2015), DOI [10.1016/j.tcs.2014.10.035](https://doi.org/10.1016/j.tcs.2014.10.035); [author journal PDF](https://fedorvf.github.io/articles/2015/2015f.pdf) | Title/footer, exact definition on p. 2 and Section 3 framing. At `t=2`, the established cover condition is exactly the no-singleton selected component condition. The object is deducted; CCI's empty/isolate conventions remain explicit. |
| Molinero, Riquelme and Serna, *Satisfaction and Power in Unanimous Majority Influence Decision Models*, ENDM 68, 197–202 (2018), DOI [10.1016/j.endm.2018.06.034](https://doi.org/10.1016/j.endm.2018.06.034); [UPC author final draft](https://upcommons.upc.edu/bitstreams/331d37a2-b15a-44a0-9de1-85a36f5f6d7b/download) | The matching local source snapshot was independently reread: cover/title and Section 2, PDF pp. 5–6, Theorem 2.4 sketch and Corollary 2.5. The corollary establishes total-vertex-cover counting #P-completeness. The draft cites that result and does not promote its earlier open-problem prelude. |

For Molinero et al., the source actually read this round is
[the paper-local snapshot](../../../../papers/205-conflict-triggered-cyclic-increments/source_evidence/molinero2018_author_final.pdf),
SHA256 `50768214c2cfa283667fff4a04d23f6dfd2c75e7d9fc8772dfe533fbe8be4b93`.
Corollary 2.5 is on PDF page six including the warehouse cover (body page
five), not an independently checked typeset page 201. Historical UPC
browser failures remain documented; this review used the actual readable
download without claiming a new browser success. Neither the Fernau nor
Molinero inspected passage supplies the manuscript's dynamical mask closure
or its all-graph/target equality transfer.

## Internal formula-level collision checks

The following primary repository originals were directly reread in their
indicated mathematical scope and pinned in SUPPLEMENTARY_INPUTS.sha256.
No implementation or canonical from them was imported.

| Original | Actual scope and tested separator |
|---|---|
| [P118](../../../../papers/118-synchronous-mex-multipartite-dynamics/main.tex) | Literal open-neighborhood mex, part quotient and Section 4's quotient support/recurrence and graph two-round collapse. Its recurrent periods are at most two, whereas CCI already has a `q≥3` orbit on an edge. A surjective autonomous factor of the former complete finite system cannot create the latter period. |
| [P164](../../../../papers/164-cyclic-equality-feedback/main.tex) | Literal binary equality output, full main theorem and affine nilpotent-tail proof. Its dyadic system is absorbed into a unique fixed point; CCI preserves full colours and has nonfixed `q`-cycles. The source's binary-code fibre atlas is not CCI's target graph constraint. |
| [P202](../../../../papers/202-ternary-ordered-reset/main.tex) | Literal ordered-reset rule and complete time-one decoder/proof. Its nonzero fibres are powers of two. CCI has a four-vertex star/constant-target fibre of seven, which blocks bijective conjugacy to that complete rule. The independent local `01` choices do not supply CCI's coupled target constraints. |
| [Old Bellman spike](../../../papers197_201_sequence/scouting/root_graph_bellman/THEOREM_SPIKE.md) | Entire fixed-height min-envelope contract. Its states all fix; CCI's waits and seeds depend on the initial colours and nonfixed states rotate. A source-dependent shortest-path representation is not an autonomous conjugacy to that fixed height map. The shortest-path primitive receives no novelty credit. |

These are bounded exact adapter tests. A mismatch of a naive representation
does not rule out every possible future enriched factor. No global
nonexistence-of-adapter theorem is asserted.

## Value and source ceiling

The conflict-bit model, irreversible activation as a method, shortest paths,
binary branch reconstruction, total covers, their counting programme and
elementary independent-set bounds all receive zero contribution credit.
After those deductions, the manuscript still proves a literal all-time
coordinate/entrance theorem and a separate target inverse/extremum theorem.
The supporting static calculation is not sold as separately new. The
conjunction is sufficient only for the repository's modest internal note
contract; it is not a certificate of demanding-venue significance or
priority. Exact contrary ownership evidence would reopen the gate.
