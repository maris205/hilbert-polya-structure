# True-twin projection — bounded primary-owner audit

**Search date:** 2026-09-03  
**External state:** `HOLD_EXTERNAL`  
**Decision:** `KILL_DIRECT_COPOINT_SPECIES_AND_INTERNAL_TWIN_QUOTIENT`

This is a bounded subtraction ledger, not a systematic review, novelty claim,
priority claim, or freedom-to-operate opinion.

## 1. Query families

The primary-source search used spelling and complement variants of:

```text
true-twin-free graph enumeration
equal closed neighborhoods quotient graph
co-point-determining graph enumeration
point-determining graph clique substitution
graph blow-up true twin classes
enumeration mating-type graphs Read
modular decomposition twins quotient substitution
point-determining graphs by number of edges
weighted co-point-determining graph polynomial
partition lattice Mobius graph enumeration
```

Search-result snippets were used only to locate records.  Mathematical
subtraction below relies on opened primary text, author-hosted full text, or
publisher metadata.

## 2. Direct owner: Gessel--Li

Ira M. Gessel and Ji Li, “Enumeration of Point-Determining Graphs,”
*Journal of Combinatorial Theory, Series A* **118** (2011), 591--612,
DOI [10.1016/j.jcta.2010.03.009](https://doi.org/10.1016/j.jcta.2010.03.009).

- [Publisher record](https://www.sciencedirect.com/science/article/pii/S0097316510000592)
- [Primary arXiv text](https://arxiv.org/abs/0705.0042)
- [Author-hosted PDF](https://people.brandeis.edu/~gessel/homepage/papers/pd.pdf)

Verified details from the primary text:

1. It defines point-determining graphs by distinct open neighborhoods.
2. It defines their complements, the co-point-determining graphs, equivalently
   as graphs whose distinct vertices have distinct closed neighborhoods.
3. Its Theorem 2.2 proves
   `G=P o E_+=Q o K_+` for all graphs `G`, point-determining `P`, nonempty
   edgeless graphs `E_+`, co-point-determining `Q`, and nonempty complete
   graphs `K_+`.
4. The proof forms the neighborhood-equality classes, defines the uniform
   quotient adjacency, and proves the converse substitution.
5. It explicitly uses these species identities to enumerate labelled and
   unlabelled point/co-point-determining graphs.

### Exact subtraction

For the candidate, vertices with equal closed neighborhoods are precisely the
`K_+` fibres in `G=Q o K_+`.  Replacing the quotient record by the cluster
graph on those fibres changes the output representation but not the canonical
decomposition.  Therefore the following receive zero credit:

- existence and uniqueness of the true-twin partition;
- completeness of each class and uniform cross-class adjacency;
- the co-point-determining quotient;
- the assertion that every source is a clique blow-up of this quotient;
- the unweighted prescribed-target fibre size `q_k`; and
- the mass identity obtained by summing over set partitions.

The literal idempotent `tau` does not appear to be the named map in the paper,
but `tau^2=tau` follows immediately after encoding the already-defined classes
as a cluster graph.  It has no residual temporal content.

## 3. Earlier enumeration owner

Ronald C. Read, *The Enumeration of Mating-Type Graphs*, University of
Waterloo report CORR 89-38 (1989), theoretically enumerates graphs with no two
equal open neighborhoods.
[Primary scan](https://oeis.org/A006023/a006023.pdf)

Gessel--Li explicitly credits Read's reduction and enumeration.  Complementing
transfers the total enumeration to distinct closed neighborhoods.  The later
Gessel--Li theorem is the cleaner direct owner for this candidate; Read is
retained as an earlier-control source, not used to overstate exact weighted
ownership.

## 4. Modular decomposition and substitution control

Michel Habib and Christophe Paul, “A survey of the algorithmic aspects of
modular decomposition,” *Computer Science Review* **4** (2010), 41--59,
DOI [10.1016/j.cosrev.2010.01.001](https://doi.org/10.1016/j.cosrev.2010.01.001),
describes a module as a vertex set sharing the same external neighborhood and
records the mature terminology `modular decomposition`, `substitution
decomposition`, and `X-join decomposition`.

- [Publisher record](https://www.sciencedirect.com/science/article/pii/S157401371000002X)
- [Primary preprint](https://arxiv.org/abs/0912.1457)

A true-twin class is a clique module of this kind.  Generic module, quotient,
substitution, and blow-up language therefore receives zero credit.  Modular
decomposition is a broader framework rather than the exact enumerative owner;
Gessel--Li remains decisive.

## 5. Möbius-inversion control

Gian-Carlo Rota, “On the Foundations of Combinatorial Theory I: Theory of
Möbius Functions,” *Zeitschrift für Wahrscheinlichkeitstheorie und Verwandte
Gebiete* **2** (1964), 340--368, DOI
[10.1007/BF00531932](https://doi.org/10.1007/BF00531932).
[Primary full text](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/rota1.pdf)

This is the foundational owner for incidence-algebra Möbius inversion.  The
partition-lattice value

```text
mu(0hat,Gamma)=product_C (-1)^{|C|-1}(|C|-1)!
```

and inversion of “the true-twin relation contains `Gamma`” are standard
ingredients.  The candidate receives credit only for correctly attaching the
edge weights `binom(S_C,2)` and `S_C S_D` to this inversion.

## 6. Weighted-formula non-hit and ceiling

The search did not locate an inspected primary source stating verbatim

```text
sum_Gamma mu(0hat,Gamma)
 z^{sum_C binom(S_C,2)} product_{C<D}(1+z^{S_C S_D})
```

for arbitrary prescribed positive clique sizes.  Gessel--Li use species and
associated series, but the inspected theorem does not display this exact
original-edge-weighted, every-size-vector polynomial.

This is only a bounded non-hit.  It cannot be promoted to novelty because:

1. the positive counterpart is simply the edge-weight enumerator of the
   already-owned co-point quotient with vertex weights `s_i`;
2. the displayed alternating formula is one standard partition-lattice
   inversion of that decomposition; and
3. searches by edge polynomial terminology are incomplete and older tables or
   multivariate-species treatments may contain equivalent refinements.

The permissible factual ceiling is: “the formula was independently derived
and no verbatim match was found in this bounded pass.”

## 7. Requested internal controls

| control | common surface | separation / consequence |
|---|---|---|
| P118 | graph carrier, multipartite/block quotient, block-size-sensitive labelled fibres | Literal mex update differs, but fibre packaging is occupied. |
| P127 | graph/matrix carrier, idempotent projection branch, codomain-wide fibres | Literal algebra differs; projection-plus-fibre is not new architecture. |
| P143 | quotient object and inclusion--exclusion every-target fibre | Strong proof-architecture collision despite Boolean-relation rather than simple-graph carrier. |
| P152 | finite graph dynamics | Stochastic triad dynamics is technically separate; only broad category proximity. |

### Decisive prior scouting collisions

- `docs/papers112_116_sequence/scouting/COMBINATORIAL_SCOUT.md`, candidate
  `C9`, already considered merging weighted open/closed twin classes and
  retaining the quotient.  It was killed as direct twin-reduction/modular-
  decomposition ownership.
- `docs/papers157_161_sequence/scouting/combinatorial/SCOUT.md`, candidate
  `GQT`, considered equal-open-neighborhood quotienting and killed it as
  `KILL_DIRECT_TWIN_QUOTIENT`, explicitly citing `C9`.

The current map keeps the partition as a cluster graph rather than returning
the co-point quotient.  Its weighted fibre is cleaner than those brief scout
records, but it does not cross the already-recorded mechanism firewall.

## 8. Same-batch audit

The closest visible same-batch architecture is
`scouting/outdegree_residue_clustering`: it sends a labelled digraph to a
cluster graph determined by a vertex statistic and derives every cluster-
target fibre as a block-size-sensitive formula.  The source statistic and
formula are different, so this is not a literal collision.  It is a strong
portfolio collision in output type and theorem packaging.

Other current survivors based on stochastic intersections or cyclic-word
feedback have no graph-twin proof transfer.  Their separation cannot rescue a
candidate already directly owned externally and killed internally twice.

## 9. Final owner/value ruling

**`KILL_DIRECT_COPOINT_SPECIES_AND_INTERNAL_TWIN_QUOTIENT`.**

The weighted polynomial is valid and was not located verbatim, but all of its
objects and its positive quotient interpretation are supplied by
`G=Q o K_+`; only the prescribed-size edge marker and one Möbius evaluation
remain.  That residual is below the two-axis paper threshold.  Maintain
`HOLD_EXTERNAL`, preserve the negative evidence, and make no novelty claim.
