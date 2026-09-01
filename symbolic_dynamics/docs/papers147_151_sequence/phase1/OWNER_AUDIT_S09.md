# Independent direct-owner and claim-subtraction audit — S09

**Audit date:** 2026-09-01 UTC.  **External status:** `HOLD_EXTERNAL`.
**Decision:** `PERMANENT KILL — DIRECT INTERNAL CONJUGACY AND DIRECT GENERAL
PROCESS OWNER`.

## Executive finding

S09 is mathematically correct, but it cannot be frozen for P147–P151.
There are two independent and decisive collisions.

1. **Internal same-map collision.**  Under the standard triangle-hypergraph
   encoding, S09 on the `r`-page triangle book is exactly P136 with sunflower
   core size `c=1`, `m=r` petals, petal sizes `p_i=2`, unit edge rates
   `lambda_i=1`, and recorded hypergraph vertices interpreted as deleted graph
   edges.  P136 proves the more general heterogeneous, weighted,
   vertex-resolved endpoint law and the complete unit-rate selection-count
   law.  Every advertised S09 clock and endpoint formula is a literal
   specialization.  The absorber census, mode, and projected-history formula
   are one-line corollaries of the same representation.
2. **External direct process owner.**  Bar-Yehuda's hypergraph version of the
   Pitt process already selects an unhit hyperedge, selects a random vertex in
   it, adds that vertex to the cover, and removes the constraints it hits.  A
   uniform active-edge scheduler and uniform vertex weights give the S09
   transition after the triangle-hypergraph encoding.  Triangle Edge Deletion
   itself is explicitly reduced to 3-Hitting Set in the primary algorithmic
   literature.

The bounded search did not locate an external paper that prints the graph-book
specialization together with the exact `3^r` endpoint census in S09 notation.
That phrase-level non-hit is immaterial: the literal system and main theorem
conjunction already transfer from P136, and the general update has a direct
external owner.  By the P147–P151 firewall, this is a permanent kill, not a
reserve.

## 1. Audited literal map

Let `B_r` have a common spine edge `z` and private side edges `a_i,b_i` on
page `i`, for `1<=i<=r`.  Its triangles are

```text
Delta_i = {z,a_i,b_i}.
```

S09 repeats the following update while a triangle exists:

1. choose a current triangle uniformly;
2. choose one of its three graph edges uniformly;
3. delete that graph edge;
4. stop when the graph is triangle-free.

The output endpoint can equivalently be recorded by the set `D` of deleted
graph edges, since the final graph is `B_r-D`.

### History convention

There are two different history objects, which must not be conflated.

- A **projected deletion history** records only the successive graph edges
  deleted.  When the common spine is deleted, it forgets which active triangle
  was sampled as the witness.
- A **full sampled-match history** also records that final witness triangle.

The scout's history mass `1/[3^(s+1)(r)_s]` is the first object.  For a fixed
full history, including a specified final witness page, the mass is instead
`1/[3^(s+1)(r)_(s+1)]`.  Summing over the `r-s` possible witnesses recovers
the projected mass.  This convention issue does not rescue an independent
claim.

## 2. Exact same-map conjugacy

For any graph `G`, form its triangle hypergraph

```text
H_Delta(G) = (E(G), { {e_1,e_2,e_3} : e_1,e_2,e_3 form a triangle of G }).
```

Graph edges are hypergraph vertices, and graph triangles are 3-uniform
hyperedges.  If `D` is the set of graph edges already deleted, the current
triangles are exactly the hyperedges disjoint from `D`: edge deletion cannot
create a triangle.  Therefore

```text
choose a current triangle uniformly
+ choose one of its graph edges uniformly
+ delete that graph edge
```

is exactly

```text
choose an unhit hyperedge uniformly
+ choose one of its vertices uniformly
+ add it to the hitting set
+ remove every hyperedge it hits.
```

This is equality of transition kernels, not an analogy or a state quotient.
On `B_r`,

```text
H_Delta(B_r) has edges {z,a_i,b_i}, 1<=i<=r,
```

so it is the 3-uniform sunflower with singleton core `{z}` and disjoint
two-vertex petals `{a_i,b_i}`.

### Direct comparison with occupied P136

| field | S09 | occupied P136 | relation |
|---|---|---|---|
| carrier | `r` triangles sharing graph edge `z` | sunflower with core size `c` and petal sizes `p_i` | `c=1`, `p_i=2`, `m=r` |
| active object | current triangle | unhit hyperedge | identical under `H_Delta` |
| scheduler | uniform current triangle | rate-proportional unhit hyperedge | `lambda_i=1` |
| local mark | uniform graph edge in triangle | uniform vertex in hyperedge | identical |
| state change | delete marked graph edge; all incident triangles vanish | record marked vertex; all hit hyperedges vanish | identical |
| endpoint | deleted-edge set, or remaining graph | recorded transversal | bijective |
| clock | number of graph-edge deletions | number of recorded vertices | identical |

The relevant occupied contract is
`docs/papers132_136_sequence/phase1/FINAL_THEOREM_CONTRACTS.md`, under
“P136 — exact laws for random sunflower transversals.”  The repository's
P147–P151 historical occupancy file already names “sunflower laws” among the
P132–P141 exclusions.  This is precisely that exclusion, not merely a similar
carrier.

## 3. Complete theorem-package transfer

P136 writes

```text
r_i = p_i/(c+p_i),       q_i = c/(c+p_i).
```

The S09 specialization gives `r_i=2/3` and `q_i=1/3` for every page.

### 3.1 Clock law

P136's unit-rate tail formula is

```text
Pr(T>t) = e_t(r_1,...,r_r) / C(r,t).
```

Hence S09 has `Pr(T>t)=(2/3)^t`, and therefore

```text
Pr(T=t) = (2/3)^(t-1)/3,        1<=t<r,
Pr(T=r) = (2/3)^(r-1).
```

The top atom already includes the two mechanisms distinguished by P136:
all `r` petal marks, or `r-1` petal marks followed by a last-page core mark.

### 3.2 Every-target endpoint law

Fix `S subset [r]`, `|S|=s<r`, and fix one private side edge on every page in
`S`.  P136's unit-rate aggregate endpoint formula first gives

```text
pi(S) = (2/3)^s / [3 C(r,s)].
```

Resolving the selected vertex in each two-vertex petal divides by `2^s`.
Since the core has one vertex, the specified S09 endpoint mass is exactly

```text
1 / [3^(s+1) C(r,s)].
```

For a specified choice of one deleted private side on every page, P136's
all-petal vertex-resolved law gives

```text
product_i 1/(c+p_i) = 3^(-r).
```

These are the two advertised S09 endpoint formulas verbatim.

### 3.3 Absorber census and mode

The P136 endpoint classification leaves, for every page, either one of two
private marks before the core mark, no mark before the core mark, or one of
two private marks in the all-petal endpoint.  Consequently S09 has

```text
sum_(s=0)^(r-1) C(r,s)2^s + 2^r = 3^r
```

absorbers.  For `r>=2`, the endpoint `D={z}` has mass `1/3`; every other
core endpoint has denominator at least `3^2 C(r,1)`, and every all-petal
endpoint has mass `3^-r`.  Thus immediate spine deletion is the unique mode.
Both statements are direct corollaries of the already occupied full endpoint
law, not an independent structural axis.

### 3.4 Projected history mass

For a fixed ordered list of `s` resolved pages and fixed selected side edges,
the successive factors are

```text
1/[3r], 1/[3(r-1)], ..., 1/[3(r-s+1)].
```

The aggregate hazard of deleting the common spine next is `1/3`.  Thus the
projected edge-deletion history has mass

```text
1 / [3^(s+1)(r)_s].
```

For a fixed all-page order and fixed private sides, the mass is

```text
1 / [3^r r!].
```

This is exactly the random-order/independent-mark proof engine already used
by P136.  It adds no owner-subtracted theorem axis.

## 4. Direct-owner and nearest-neighbour classification

The categories below are deliberately separated.  “Nearest” is not used as
a euphemism for the direct same-map hits.

| tier | source | owned content | audit consequence |
|---|---|---|---|
| **DIRECT, general same map** | Reuven Bar-Yehuda, [*One for the Price of Two: A Unified Approach for Approximating Covering Problems*](https://csaws.cs.technion.ac.il/~reuven/PDF/Bar98a.pdf), *Algorithmica* 27 (2000), DOI [`10.1007/s004530010009`](https://doi.org/10.1007/s004530010009), Sec. 5.1 and Thm. 6 | the hypergraph Pitt process: choose an unhit edge, choose a random vertex in it, add it to the cover, and remove what it hits; uniform weights give a uniform vertex | the S09 update is owned after the exact triangle-hypergraph encoding; uniform edge choice is a scheduler specialization |
| **DIRECT, internal same map and stronger theorem** | P136, `FINAL_THEOREM_CONTRACTS.md` and its hostile owner gate | weighted heterogeneous sunflower endpoint law, vertex resolution, complete unit-rate clock/PGF/moments, forest product | all principal S09 claims transfer by `c=1,p_i=2,lambda_i=1`; permanent firewall kill |
| **SAME OBJECT / exact reduction** | Gramm, Guo, Hüffner, Niedermeier, [*Automated Generation of Search Tree Algorithms for Hard Graph Modification Problems*](https://fpt.akt.tu-berlin.de/homepage-hueffner/search-trees-algorithmica04.pdf), *Algorithmica* 39 (2004), Sec. 4.1.3 | Triangle Edge Deletion maps graph edges to ground-set elements and each triangle to a 3-set | owns the exact Triangle Edge Deletion `<->` 3-Hitting Set object map used above; its algorithms are deterministic/exact rather than S09's endpoint law |
| **SAME OBJECT, current algorithms** | Censor-Hillel and Khoury, [*On Distributed Computation of the Minimum Triangle Edge Transversal*](https://arxiv.org/abs/2402.13985) | minimum edges whose deletion makes a graph triangle-free; reduction to hypergraph vertex cover; distributed approximation and lower bounds | confirms modern use of the same optimization object, but does not state the S09 chain law |
| **SAME RANDOM LOCAL SCHEMA, rank two** | Gupta, Ligett, McSherry, Roth, Talwar, [*Differentially Private Approximation Algorithms*](https://www.cs.cmu.edu/afs/cs.cmu.edu/Web/People/CompThink/probes/papers/private-optimization.pdf), Sec. 4.1 | explicitly describes the non-private Pitt rule as repeatedly selecting an uncovered graph edge uniformly and including a random endpoint | the 2-uniform ancestor has the same “uniform uncovered constraint + uniform element” skeleton; Bar-Yehuda is the closer hypergraph owner |
| **NEAREST, different deletion amount** | Bohman, Frieze, Lubetzky, [*Random triangle removal*](https://arxiv.org/abs/1203.4223) | select a uniform triangle and delete all three of its edges; analyze the final edge count/time on the complete graph | not the same map: S09 deletes one random edge, not the whole selected triangle |
| **NEAREST framework** | Behr, Danos, Garnier, [*Stochastic mechanics of graph rewriting*](https://nicolasbehr.com/publication/2016-01-01_bdg2016/) | stochastic graph-rewrite rule algebra and Kolmogorov equations | an equal-rate triangle-with-distinguished-edge deletion rule can represent S09's event skeleton; this is a framework-level inference, not a located S09 theorem |
| **NEAREST framework/application** | Mjolsness, [*Explicit Calculation of Structural Commutation Relations for Stochastic and Dynamical Graph Grammar Rule Operators in Biological Morphodynamics*](https://www.frontiersin.org/journals/systems-biology/articles/10.3389/fsysb.2022.898858/full) | local graph rules, matches, propensities, and stochastic rule firing; includes edge-erasure semantics | owns general stochastic rewrite machinery, not the triangle-book endpoint formulas |
| **NEAREST deterministic triangle rewrite** | Kulcsár et al., [*Rapid Prototyping of Topology Control Algorithms by Graph Transformation*](https://eceasst.org/index.php/eceasst/article/view/2144) | graph-transformation implementation of kTC, which marks/deletes a longest edge in qualifying triangles | literal triangle-conditioned edge deletion exists in graph rewriting, but the choice rule and target are deterministic/weighted rather than S09 |
| **SAME CARRIER ONLY** | Mubayi, [*Books Versus Triangles*](https://onlinelibrary.wiley.com/doi/abs/10.1002/jgt.20607) | a book of size `b` is an edge lying in `b` triangles; static extremal results | owns the shared-edge book terminology and carrier, not a deletion chain |

Bar-Yehuda is the direct external process owner.  The graph-rewriting papers
are not promoted above framework/nearest-neighbour status: the audit found no
instance in them that analyzes the uniform one-edge triangle-book chain.
Likewise, the standard random triangle-removal process is genuinely a
different transition kernel and is not the basis of the kill.

## 5. Search protocol and query log

### Sources/databases actually queried

- arXiv title/abstract/full-text records, including current 2024–2026 records;
- SpringerLink/Algorithmica, Elsevier/ScienceDirect, Wiley, Frontiers, and the
  official ECEASST proceedings pages;
- author and institutional repositories at Technion, TU Berlin, CMU, and the
  authors' publication pages;
- exact DOI/title searches and reference chasing from the primary papers.

A general web index was used only to locate records.  Admissible evidence in
this audit is linked to a publisher, arXiv, proceedings, institutional, or
author-hosted source.  ResearchGate snippets and tertiary pages were not used
as claim evidence.

### Representative literal queries

The following query families were run with plural/singular and
hyphenation variants where useful.

```text
"random triangle removal"
"choose a triangle" "delete one" edge random process
"random triangle" "delete an edge" graph process

"triangle edge deletion" randomized algorithm
"triangle edge transversal" randomized greedy
"triangle edge deletion" 3-Hitting Set
"choose an uncovered hyperedge" "uniformly at random"
"random hyperedge" "random element" hitting set approximation
"random endpoint" "uncovered hyperedge"

"stochastic graph rewriting" triangle edge deletion
"probabilistic graph transformation" edge deletion triangle
site:arxiv.org stochastic graph rewriting edge deletion graph
"Rapid Prototyping of Topology Control Algorithms by Graph Transformation"

"book graph" triangle edge deletion
"triangles sharing a common edge" random deletion graph
site:arxiv.org "book graph" triangle removal process
"book graph" edge deletion triangle-free journal

"Pitt algorithm" sunflower hitting set
"random greedy" sunflower "hitting set"
"probabilistic approximation algorithm" sunflower hypergraph vertex cover
"YaleU/DCS/TR-404"
```

### Results by required lane

1. **Random triangle removal:** a strong named neighbour was found, but it
   deletes all three selected-triangle edges and therefore is not same-map.
2. **Triangle edge deletion / hitting-set algorithms:** the exact
   Triangle Edge Deletion-to-3-Hitting-Set reduction and a modern minimum
   triangle edge transversal treatment were found.  This is same-object
   ownership.
3. **Stochastic graph rewriting:** general stochastic rule/match semantics and
   a deterministic triangle-conditioned edge-deletion application were found;
   no exact book endpoint-law paper was located.
4. **Book/shared-edge processes:** primary static book-graph sources were
   found; no primary source located by these queries prints S09's named
   graph-book chain and formulas.
5. **Random cover process:** the direct Bar-Yehuda hypergraph owner and Pitt
   graph ancestor were found.  This lane, together with P136, decides the
   audit.

## 6. Claim subtraction ledger

| proposed S09 material | subtraction | residual credit |
|---|---|---|
| random “active triangle then one edge” update | exactly the hypergraph Pitt step after `H_Delta`; direct Bar-Yehuda owner | **zero** |
| Triangle Edge Deletion/hitting-set interpretation | explicit primary reduction by Gramm et al.; reinforced by current transversal work | **zero** |
| shared-edge book carrier | classical book/sunflower object; already used by P136 | **zero** |
| constant `1/3` spine hazard | `c=1,p_i=2` mark probability in P136 | **zero** |
| truncated-geometric clock | exact specialization of P136's elementary-symmetric tail law | **zero** |
| every-target endpoint masses | exact specialization of P136's vertex-resolved endpoint law | **zero** |
| `3^r` absorber count | immediate count of the already classified P136 endpoints | **transferred corollary; zero independent axis** |
| unique maximum-mass endpoint | immediate comparison inside the specialized P136 law | **transferred corollary; zero independent axis** |
| projected history factorization | random page order plus independent marks, the same P136 proof engine | **elementary transferred corollary** |
| graph-language presentation | a realization of the occupied hypergraph chain | **presentation only** |

### Surviving claim conjunction

Relative to the P1–P146 portfolio, **none survives**.  The strongest sentence
that survives the external phrase search alone would be:

```text
The graph-book realization gives a compact corollary, in graph language, of
the unit-rate singleton-core, two-vertex-petal specialization of the random
sunflower transversal law.
```

That is explicitly below the P147–P151 progress threshold: it is a classical
algorithm restated on a new encoding, and its clock/endpoint conjunction has
already been proved in a stronger occupied system.  It is not paper-scale and
must not receive a paper number.

## 7. Proof skeleton, retained only as audit evidence

The S09 formulas require no new engine beyond the collision.

1. Track the unresolved page set `U` while the spine survives.  The active
   triangles are exactly `U`.
2. Conditional on any nonabsorbing state, a uniform mark is the spine with
   probability `1/3`; otherwise it is one of two private sides and resolves
   the sampled page.
3. Therefore the first `t` choices avoid the spine with probability
   `(2/3)^t`, giving the clock law after truncation at `r`.
4. For a fixed `s`-set of pages and fixed side choices, sum over its `s!`
   possible orders before the first spine mark.  This gives
   `1/[3^(s+1) C(r,s)]`.
5. If no spine is selected, sum the `r!` page orders to obtain `3^-r` for
   each fixed side word.
6. Enumerate the endpoint types and compare their displayed masses to get
   `3^r` and the unique mode.

This proof is precisely the singleton-core/two-petal specialization of P136's
uniform random-order and independent-mark argument.

## 8. Bounded-non-hit limitation

The statement “no external source was located printing the complete S09
graph-book formula package” is only a bounded non-hit as of the audit date.
It is limited by the queried databases, indexed English terminology, exact
phrase choices, and accessible full text.  No exhaustive search of
MathSciNet, zbMATH, Web of Science, Scopus, non-English literature, theses, or
all citation descendants was performed.  Pitt's original Yale TR-404 was not
located as a direct primary full-text record; the rule was checked through
author-hosted primary papers that explicitly reproduce and attribute it.

No novelty, priority, authorship, or release conclusion may be inferred from
that non-hit.  More importantly, the kill does **not** depend on it: the exact
P136 conjugacy is repository-verifiable, and Bar-Yehuda directly owns the
general random hypergraph-cover update.

## 9. Final disposition

```text
S09 = PERMANENT KILL
reason = direct specialization of occupied P136
       + direct Bar-Yehuda hypergraph Pitt-process owner
       + exact Triangle Edge Deletion / 3-Hitting-Set same-object reduction
paper allocation = forbidden
reserve status = no
external status = HOLD_EXTERNAL
```

S09 may be mentioned only as a zero-credit graph realization or sanity-check
corollary of P136.  It cannot supply one of P147–P151, and changing the name,
using graph rather than hypergraph language, or emphasizing the book spine
would be a cosmetic re-encoding barred by the historical firewall.
