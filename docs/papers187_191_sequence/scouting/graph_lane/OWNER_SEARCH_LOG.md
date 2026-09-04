# Bounded owner-search log

Search date: **2026-09-04 UTC**.  Scope: the two survivors only.  The purpose
was to locate a direct owner of the *literal update and its theorem package*,
not to assemble general related work.  Five semantic batches of four web
queries were run; returned title/abstract/snippet candidates were screened,
and a small set of primary or authoritative records was opened.  Four further
exact-title/DOI queries checked bibliographic metadata.  The search then
stopped at **24 queries total**.  No citation-network, MathSciNet/zbMATH,
full-text corpus, or exhaustive historical search was performed.

## Exact queries

### G01 TRC (8)

1. `site:arxiv.org Ferrers matrix row compression transpose conjugate partition dynamics binary matrix`
2. `site:doi.org Ferrers relation row sums conjugate partition binary matrix transformation`
3. `"row compression" binary matrix Ferrers transpose`
4. `"left justified" binary matrix row sums Ferrers matrix transpose`
5. `site:arxiv.org "Ferrers relation" adjacency matrix rows`
6. `site:doi.org "Ferrers relation" binary matrix row sums`
7. `site:oeis.org number of partitions inside n by n square central binomial coefficient`
8. `site:oeis.org self-conjugate partitions inside n by n square 2^n`

### G02 ECSC (12)

1. `site:arxiv.org graph operation merge connected components equal size complete graph iteration`
2. `site:mathworld.wolfram.com connected graph enumeration labeled connected graphs generating function`
3. `"equal-sized components" graph merge operation`
4. `"components of equal size" graph operation complete`
5. `site:arxiv.org graph dynamics "component sizes" merge`
6. `site:doi.org graph transformation "equal component size" merge`
7. `site:arxiv.org labeled cluster graphs set partitions connected graph components cliques enumeration`
8. `site:doi.org "cluster graph" "disjoint union of cliques"`
9. `mathematics "merge equal parts" partition iteration`
10. `combinatorics "combine equal parts" integer partition dynamics`
11. `"merge equal-sized blocks" set partition dynamics`
12. `"merge all equal" parts partition algorithm`

### Bibliographic validation only (4)

1. `doi 10.1016/j.disc.2012.11.027 author`
2. `doi 10.1016/j.disc.2021.112755 author`
3. `doi 10.1016/j.disc.2015.10.010 authors`
4. `doi 10.1016/j.disopt.2010.09.006 authors`

## Screened authoritative/primary hits

### G01 adjacency

| Record | What it owns | Relation to the spike |
|---|---|---|
| Jeffrey W. Miller, [“Reduced criteria for degree sequences”](https://doi.org/10.1016/j.disc.2012.11.027), *Discrete Mathematics* (2013) | Binary matrices with prescribed row sums, conjugate sequences, and Ferrers maximal matrices. | Direct ownership of core vocabulary and line-sum/Ferrers facts; the returned record did not state the repeated map `A -> (row-compress A)^T`. |
| Martin Koutecky and Shmuel Onn, [“Uniform and Monotone Line Sum Optimization”](https://arxiv.org/abs/2011.09932) | Monotone binary matrices and row/column-sum conjugation/majorization. | Adjacent structural owner; no exact functional graph was visible in the returned record. |
| A. K. Kwasniewski, [“Cobweb Posets and KoDAG Digraphs ...”](https://arxiv.org/abs/0812.4066) | Ferrers digraphs/relations and adjacency matrices. | Owns nearby relational representation, not the literal TRC scheduler in the screened text. |
| Ashok Kumar Das, Sandip Das, and Malay Sen, [“Forbidden substructure for interval digraphs/bigraphs”](https://doi.org/10.1016/j.disc.2015.10.010) | Ferrers matrices/bigraphs and Ferrers dimension. | Confirms that the image class is established territory; not an all-time iteration hit. |
| M. D. Barrus, [“The principal Erdos–Gallai differences of a degree sequence”](https://doi.org/10.1016/j.disc.2021.112755) | Corrected Ferrers diagrams and transposition in degree-sequence analysis. | Close operation-level vocabulary, but the screened record did not identify the exact TRC map or its fibres. |
| [OEIS A063746](https://oeis.org/A063746) and [OEIS A000984](https://oeis.org/A000984) | Counts of partitions fitting in an `n x n` box and central binomial coefficients. | Authoritative count cross-checks only; sequence agreement is not ownership clearance. |

### G02 adjacency

| Record | What it owns | Relation to the spike |
|---|---|---|
| Darij Grinberg, [*Enumerative Combinatorics class notes*, Example 3.7.2](https://www.cip.ifi.lmu.de/~grinberg/t/19fco/n/n-temp.pdf) | The Glaisher bijection via repeatedly merging **two** equal integer parts until distinct. | Serious nearby owner.  It is not the simultaneous `m_s`-way rule: for example three copies become `2s,s` there but `3s` here.  This distinction requires external assessment. |
| Michael R. Fellows, Jiong Guo, Christian Komusiewicz, Rolf Niedermeier, and Johannes Uhlmann, [“Graph-based data clustering with overlaps”](https://doi.org/10.1016/j.disopt.2010.09.006) | Cluster graphs as vertex-disjoint unions of cliques and cluster editing. | Owns the target graph class, but its optimization/editing problem is not the deterministic equal-component-size merger. |
| Frank Simon, Peter Tittmann, and Martin Trinks, [“Counting Connected Set Partitions of Graphs”](https://arxiv.org/abs/1005.1726) | Connected set partitions and their enumeration. | Adjacent to the connected-graph decoration in the fibre formula, not a hit on the ECSC dynamics. |
| [Wolfram MathWorld, “Connected Graph”](https://mathworld.wolfram.com/ConnectedGraph.html) and its linked OEIS A001187 | Counts `c_s` of connected labelled simple graphs. | Authoritative numerical cross-check for a factor in the fibre formula, not a direct owner. |

The searches also returned balanced graph partitioning/forest sampling,
critical random-graph component-size distributions, generic cluster deletion,
and unrelated uses of “row compression” or “merge equal”.  They were screened
out because they do not apply the literal update.

## Owner decision and limits

- **G01 TRC: `OWNER_AMBER / HOLD_EXTERNAL`.**  Standard Ferrers/conjugation
  machinery is unquestionably owned.  Within this bounded search, no returned
  record stated the exact iteration together with its depth layers and
  time-one/time-two all-target fibres.  That sentence records a search outcome,
  **not novelty**.
- **G02 ECSC: `OWNER_AMBER / HOLD_EXTERNAL`.**  Glaisher merging and cluster
  graphs are close enough that independent expert review is mandatory.  The
  simultaneous all-multiplicity scheduler and connected-decorated fibres were
  not identified in the returned records.  Again, non-identification is **not
  evidence of novelty**.

No survivor is cleared for public novelty language, paper-number allocation,
submission, or external circulation.  A later owner review must search by
formula and update semantics, include citation chasing, and explicitly decide
whether G02 is merely a dressed partition-merging process.
