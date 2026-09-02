# Focused owner and collision audit — cut-intersection collapse

## Decision

**OWNER-THIN PASS FOR INTERNAL DEVELOPMENT / HOLD_EXTERNAL.**

This is a bounded search result, not a novelty, absence, or priority finding.
The paper can survive only on the literal conjunction of the repeated-cut
process, exact all-time absorption law, and complete labelled target-fibre
atlas. Every standard ingredient is subtracted.

## Literal fingerprint searched

- carrier: spanning subgraphs of a labelled $K_n$;
- update: intersect the current edge set with a fresh iid fair vertex cut;
- encoding: two vertices remain adjacent exactly when their full binary
  histories are bitwise complements;
- temporal target: exact empty-state CDF at every time;
- structural target: exact labelled fibre of every disjoint union of
  nontrivial complete bipartite components and isolates;
- corrected boundary: $r=R,z>0$ has zero fibre.

Search terms included the literal update and variants using cut-space,
intersection of complete bipartite spanning graphs, antipodal binary labels,
complementary codewords, biclique dimension, separating systems, bipartite
cluster graphs, and random graph processes.

## External citation chain

### Biclique covering and partitioning

P. Erdős and L. Pyber, *Covering a graph by complete bipartite graphs*,
Discrete Mathematics 170 (1997), 249--251,
<https://doi.org/10.1016/S0012-365X(96)00124-0>.

- **Owns/supports:** complete-bipartite edge decompositions are an established
  graph-theoretic object.
- **Does not support:** iid cut intersection, complement-history occupancy,
  an absorption clock, or a fixed labelled target history fibre.
- **Subtraction:** all general biclique-cover motivation receives zero credit.

### Bicluster graph class

J. Guo, F. Hüffner, C. Komusiewicz, and Y. Zhang, *Improved Algorithms for
Bicluster Editing*, TAMC 2008, LNCS 4978, 445--456,
<https://doi.org/10.1007/978-3-540-79228-4_39>.

- **Owns/supports:** a vertex-disjoint union of complete bipartite graphs is a
  standard target class in bicluster editing.
- **Does not support:** why this random intersection process lands there, the
  resource constraint from only $R$ complementary pairs, or any history-fibre
  formula.
- **Subtraction:** the graph-class name and its static recognition receive
  zero credit.

### Random intersection graphs

J. Zhao, O. Yağan, and V. Gligor, *On $k$-connectivity and minimum vertex
degree in random $s$-intersection graphs*, ANALCO 2015, 1--15,
<https://doi.org/10.1137/1.9781611973761.1>; author preprint
<https://arxiv.org/abs/1409.6021>.

- **Owns/supports:** random item assignments as a mature way to generate
  graph edges and asymptotic connectivity questions.
- **Does not support:** CIC's edge rule. Random intersection graphs create an
  edge from shared items; CIC retains an edge from exact full-history
  complementation. The cited work does not study cumulative cut
  intersections, finite-time absorption, or labelled fibres.
- **Subtraction:** generic random-label graph language receives zero credit.

## Bounded direct-owner result

No inspected primary record stated the same random update together with either

\[
\Pr(T\le t)=A_{2^{t-1}}(n)/2^{tn}
\]

or

\[
(R)_r2^rA_{R-r}(z)
\]

for every fixed labelled target. This is only a bounded non-hit. In
particular, search snippets were not treated as evidence, and different
terminology may conceal a direct owner.

## Claim-by-claim subtraction

| ingredient | ownership treatment | residual status |
|---|---|---|
| vertex cuts and cut graphs | standard; zero credit | none |
| binary history words and complementation | definition-level encoding; zero credit | none |
| complete bipartite components / bicluster graphs | externally established class; zero credit | none |
| labelled EGF and inclusion--exclusion | standard enumeration; zero credit | none |
| one-edge survival probability and union bound | elementary; zero credit | only a tail certificate |
| exact all-time empty-state CDF | no direct owner found in bounded pass | retained only inside conjunction |
| corrected every-target fibre, including $r=R,z>0$ | no direct owner found in bounded pass | principal residual |
| labelled image-size EGF with resource boundary | derived corollary | secondary residual |

## Internal collision matrix

| comparator | superficial overlap | decisive separation | proof-transfer verdict |
|---|---|---|---|
| P78, complete-bipartite sandpile translations | complete-bipartite vocabulary | P78 translates recurrent sandpiles on one fixed graph; CIC changes the edge set by fresh random cuts | no state, clock, or fibre proof transfers |
| P143, Boolean row-inclusion residual | Boolean data, labelled fibres, inclusion--exclusion | P143 replaces a relation by row-support inclusion and iterates a cubic retraction; CIC is a decreasing random edge intersection encoded by complementary histories | quotient-poset embeddings do not transfer |
| P145, random vertex-push orientation chain | graph bits, cut vectors, stochastic epochs | P145 reverses orientations inside a fixed affine cut-space orbit and uses folded-hypercube spectra; CIC deletes edges and absorbs | Fourier/product/inverse machinery does not transfer |
| P146, random ear deletion | monotone random graph deletion | P146 selects and deletes an ear under a random-order mechanism; CIC applies a global cut independently at each epoch | deletion-order arguments do not produce complement-code fibres |
| P152, triangular-book triad absorption | finite random graph dynamics and absorption | P152 flips signs on a fixed graph and reduces to a reflected count chain; CIC changes the underlying graph and has many component profiles | Bellman/Chebyshev machinery does not transfer |

The strongest proximity is P143 at the theorem-silhouette level: both have a
Boolean encoding and labelled inverse counts. It is not a literal or
proof-engine collision, but the manuscript must avoid generic claims about
introducing Boolean encodings or inclusion--exclusion fibres.

## Focused correction audit

The broad scout claimed that every valid component graph was attainable once
$R\ge r$. Full target enumeration found the counterexample
$r=R,z>0$. The corrected positive-fibre condition is

\[
r\le R\quad\text{and}\quad(z=0\text{ or }r<R).
\]

The algebraic fibre formula did not require alteration because
$A_0(z)=0$ for $z>0$. The focused verifier tests every labelled graph, not
only observed images, so this boundary is now an executable zero-fibre
obligation.

## Gate conditions for a manuscript

1. Preserve the corrected boundary example explicitly.
2. Cite and subtract the biclique/bicluster and random-intersection
   neighbourhoods.
3. Make no novelty, first, new graph class, or priority claim.
4. Require two independent hostile reviewers to search for a direct owner
   using alternate terminology.
5. Kill or radically narrow the paper if either reviewer finds the literal
   update plus the fibre conjunction in prior work.

Until those conditions close, external status remains **HOLD_EXTERNAL**.
