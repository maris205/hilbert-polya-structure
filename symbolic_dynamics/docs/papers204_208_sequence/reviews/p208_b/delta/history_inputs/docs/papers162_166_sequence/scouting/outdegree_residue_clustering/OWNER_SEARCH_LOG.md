# DRC3 bounded owner and collision audit

Date: 2026-09-03 UTC  
Decision: **`KILL_OWNER_THIN_PORTFOLIO_COLLISION`**  
External status: **`HOLD_EXTERNAL`**

## Scope and method

The search was run against the literal ingredients, not the proposed title:

1. form outdegree classes (and outdegree-congruence classes) of a digraph;
2. replace each class by a complete bidirected component;
3. iterate the resulting degree/equivalence graph;
4. merge set-partition blocks with congruent cardinalities; and
5. count inverse images by prescribed row-sum residues.

Queries included:

```text
"vertices of the same degree" "graph operator" graph
"degree modulo" partition vertices graph
"outdegree" "modulo 3" digraph partition
graph transformation "same degree" vertices adjacent
"degree equivalence graph" modulo
"iterated degree equivalence graph"
"outdegree equivalence graph"
integer partition dynamics merge parts congruent modulo
set partition merge blocks congruent size modulo
```

Search hits were checked at publisher or author primary records/full text when
available.  A search non-hit is not evidence of novelty, priority, or owner
clearance.

## Direct construction owner

R. Rajendra, P. Siva Kota Reddy, and K. V. Madhusudhan, “Degree
equivalence graph of a graph,” *TWMS Journal of Applied and Engineering
Mathematics* 10 (2020), 411–414:

- [publisher record](https://dergipark.org.tr/en/pub/twmsjaem/article/761738)
- [primary full text](https://dergipark.org.tr/en/download/article-file/1181256)

The paper defines two vertices to be adjacent in the new graph exactly when
they have equal degree in the old graph and proves that the result is a
disjoint union of complete graphs on the degree-equivalence classes
(Proposition 2.1).  DRC3 changes three details—outdegree instead of degree,
congruence modulo three instead of equality, and two opposite arcs instead of
one undirected edge—but it uses exactly this equivalence-class-to-cliques
template.  Consequently the first-collapse mechanism and “cluster graph”
description receive **zero contribution credit**.  This source does not study
the DRC3 modular iterate or its inverse fibres, so it is not claimed to own
the full displayed theorem.

## Strong thematic but non-direct primary sources

- Asaf Ferber, Liam Hardiman, and Michael Krivelevich,
  [“On subgraphs with degrees of prescribed residues in the random graph”](https://doi.org/10.1002/rsa.21137),
  *Random Structures & Algorithms* 63 (2023), 192–214.  This is direct
  background for degree-residue classes and distributions, but it studies
  induced subgraphs of random undirected graphs, not an equivalence-graph
  operator or its iteration.
- Brian Alspach,
  [“Degree frequencies in digraphs and tournaments”](https://doi.org/10.1002/jgt.3190020307),
  *Journal of Graph Theory* 2 (1978), 241–247.  It treats the frequencies of
  specified in/outdegrees and vertex frequency partitions.  It does not form
  the DRC3 target or iterate it.
- Xueyi Huang, Qiongxiang Huang, and Lu Lu,
  [“Construction of graphs with exactly k main eigenvalues”](https://doi.org/10.1016/j.laa.2015.08.013),
  *Linear Algebra and its Applications* 486 (2015), 204–218.  Its equitable
  partitions and divisors are not DRC3: the original outdegree-residue cells
  need not be equitable in the source digraph, and DRC3 replaces rather than
  quotients the graph.
- Shalom Eliahou and Martin J. Erickson,
  [“Mutually describing multisets and integer partitions”](https://doi.org/10.1016/j.disc.2012.11.014),
  *Discrete Mathematics* 313 (2013), 422–433, is already recorded by the
  internal EQC audit as a plausible direct owner for multiplicity-driven
  integer-partition dynamics.  DRC3's map is residue-coagulation, not their
  displayed multiplicity map, but this source reinforces the owner risk of
  treating a shallow block-size map as an unowned temporal axis.

The bounded search did **not** locate a primary source for the exact
outdegree-modulo-three, complete-bidirected operator or the exact map “merge
all blocks whose sizes are congruent modulo three.”  This is only a bounded
non-hit and carries no positive novelty conclusion.

## Internal P1–P161 collision audit

| occupied item | overlap | verdict |
|---|---|---|
| P112, tournament score-upset reversal | current outdegrees partition vertices into score classes | Not a literal collision: P112 reorients tournament arcs and follows a strict refinement tree.  Still, outdegree-defined synchronous graph dynamics is occupied. |
| P118, synchronous mex on complete multipartite graphs | one round collapses a labelled state to a part quotient; part sizes survive in exact fibres; a shallow quotient theorem yields all depth/basin layers | **Strongest architecture collision.**  DRC3 is formally different, but its theorem package is a smaller instance of the same collapse/quotient/weighted-fibre architecture. |
| P127, odd-outdegree transpose dynamics | binary adjacency matrices, a row/outdegree residue statistic, complete codomain fibres, shallow recurrence | Not conjugate: P127 is looped, parity-affine, and has periods 1/2/4.  It nevertheless occupies the closest carrier/statistic/fibre lane. |
| P159, parallel odd-vertex pruning | a degree residue drives a deterministic graph map and exact census | Separated: P159 changes the vertex set and its inverse uses incidence rank.  This is not the decisive collision. |
| P110, cyclic shift–join partitions | deterministic monotone coarsening of labelled set partitions with exact depth/basins | DRC3's post-collapse map is another partition coarsening, but much shallower and with no independent orbit geometry. |
| permanent EQC kill | simultaneously merge all equal-cardinality blocks; quotient to an integer-partition map | **Near-literal proof-engine collision.**  Replacing equality of sizes by equality modulo three changes the map, but makes the quotient smaller and the temporal proof only a three-residue case split. |

The comparison used the frozen paper-local theorem contracts and the
P137–P141 permanent-kill statement that synchronous equal-size set-partition
merging is an occupied multiplicity-coagulation mechanism.

## Subtraction and owner decision

Assign zero credit to:

- equivalence classes becoming disjoint complete (bi)directed blocks;
- the static degree/frequency partition and cluster-graph language;
- elementary roots-of-unity filtering of binomial coefficients;
- the standard labelled-set-partition EGF; and
- generic multinomial summation once the three row residues are fixed.

What remains is correct: the exceptional depth-three residue pattern, the
modulo-dependent sharp height, and its weighting by the one-step fibre.  But
the temporal mechanism is a six-pattern case analysis on at most three
blocks, while the fibre/census axis is one independent-row multinomial
calculation.  It does not survive the combined P118/P127/EQC portfolio gate
as a paper-sized conjunction.

**Decision: `KILL_OWNER_THIN_PORTFOLIO_COLLISION`.**  No DRC3 paper or reserve
slot is authorized.  Re-entry would require a genuinely parameter-uniform
modulus-`q` temporal theorem with nontrivial all-time target-resolved structure and a
fresh proof-engine firewall against EQC/P118/P127; merely replacing `3` by
another fixed modulus does not qualify.
