# Primary-source and collision verification — P171

**Checked:** 2026-09-03 UTC  
**Result:** `GREEN_OWNER_THIN / HOLD_EXTERNAL`  
**Scope:** bounded owner search and bibliographic verification, not a novelty
certification.

## Primary sources retained in the paper

### Szpilrajn--Marczewski (1945)

- **Work:** Edward Szpilrajn-Marczewski, “Sur deux propriétés des classes
  d'ensembles,” *Fundamenta Mathematicae* 33(1), 303--307.
- **Primary/catalogue record:** <https://eudml.org/doc/213098>
- **DOI verification:** <https://doi.org/10.4064/fm-33-1-303-307>
- **Owner role:** early set-intersection representation background.
- **Does not establish for this gate:** the self-map's finite orbit clock or
  the ordered fixed-width fibre formula.

### Erdős--Goodman--Pósa (1966)

- **Work:** Paul Erdős, A. W. Goodman, and Louis Pósa, “The Representation of
  a Graph by Set Intersections,” *Canadian Journal of Mathematics* 18,
  106--112.
- **Publisher PDF:**
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C1EC0B9CD0270564F05B5A62301BE20D/S0008414X00040104a.pdf/the-representation-of-a-graph-by-set-intersections.pdf>
- **DOI:** <https://doi.org/10.4153/CJM-1966-014-3>
- **Verified content:** sets represent graph vertices by nonempty
  intersections; Section 2 translates elements of the representing universe
  into complete subgraphs covering the graph.
- **Owner role:** direct owner of intersection representations and the
  edge-clique-cover equivalence used by the image criterion.
- **Does not establish for this gate:** labelled empty/repeated `n`-column
  enumeration or Boolean-Gram iteration.

### Warshall (1962)

- **Work:** Stephen Warshall, “A Theorem on Boolean Matrices,” *Journal of the
  ACM* 9(1), 11--12.
- **DOI/publisher record:** <https://doi.org/10.1145/321105.321107>
- **Verified metadata:** title, author, journal, volume, issue, pages, January
  1962, and DOI.
- **Owner role:** Boolean-matrix transitive closure is classical.  This source
  is not used to claim the particular doubling schedule.

### Kim (1982)

- **Work:** Ki Hang Kim, *Boolean Matrix Theory and Applications*, Pure and
  Applied Mathematics 70, Marcel Dekker, New York, 1982.
- **Catalogue evidence:**
  <https://books.google.com/books/about/Boolean_Matrix_Theory_and_Applications.html?id=UeDuAAAAMAAJ>
- **Verified metadata:** 288 pages; ISBN 0-8247-1788-0 / 978-0-8247-1788-9.
- **Owner role:** general Boolean matrix/relation background only.

### Fitting (2003)

- **Work:** Melvin Fitting, “Bisimulations and Boolean Vectors,” in
  *Advances in Modal Logic*, vol. 4, King's College Publications, 2003,
  97--125.
- **Author-hosted primary PDF:**
  <https://id144254.securedata.net/melvinfitting/bookspapers/pdf/papers/BisimBool.pdf>
- **Proceedings record:** <https://www.aiml.net/volumes/volume4/>
- **Verified content:** Theorem 8 states
  `(AA^T) <= (AA^T)^2 <= (AA^T)^3 <= ...` for Boolean-algebra-valued
  matrices; the following paragraph and Example 9 show arbitrarily long
  strict growth across finite dimensions.
- **Owner role:** strong direct owner of the post-first-image power-growth
  engine.  This forces the entire monotonicity mechanism to zero credit.
- **Gate distinction:** it studies the power chain for a fixed Gram product;
  the checked source does not formulate the literal feedback self-map's
  finite functional graph, source-dependent first-stable time, sharp
  fixed-dimension height, or target fibres.

### Chen--Song--Tao--Zhang (2022)

- **Work:** Sitan Chen, Zhao Song, Runzhou Tao, and Ruizhe Zhang, “Symmetric
  Sparse Boolean Matrix Factorization and Applications,” ITCS 2022,
  LIPIcs 215, Article 46, 25 pages.
- **Publisher record/PDF:**
  <https://doi.org/10.4230/LIPIcs.ITCS.2022.46>
- **Verified content:** the paper explicitly poses `M=WW^T` over the Boolean
  semiring, interprets columns of `W` as a clique cover, and relates exact
  factorization to hypergraph line-graph recovery.
- **Owner role:** direct owner of the symmetric Boolean factorization and
  recovery viewpoint.  The factorization viewpoint earns zero credit.
- **Gate distinction:** its stated problem imposes sparse/random regimes and
  seeks optimization or recovery; it does not give the unrestricted complete
  number of labelled fixed-width factors for every target, and it does not
  study the feedback dynamics.

## Additional hostile owner check

Tao-Ming Wang and Jun-Lin Kuo, “On Intersection Representations and Clique
Partitions of Graphs,” arXiv:0804.4617, explicitly describes the
representation--clique correspondence and enumerates restricted minimum
representations for special line graphs:
<https://arxiv.org/abs/0804.4617>.  This reinforces the subtraction of the
inverse dictionary and representation-counting theme.  Its restrictions
(minimum, simple/antichain/family variants, special graph classes) do not give
the all-target labelled `n`-column formula in the manuscript.

Bounded searches combined the phrases `Boolean Gram`, `AA^T`, `iteration`,
`Boolean powers`, `symmetric Boolean factorization`, `intersection
representation`, `edge clique cover`, `ordered columns`, and `counting
representations`.  The search found the strong owners above but no source
asserting both manuscript axes for the literal self-map.  A search non-hit
has no positive evidentiary weight, and external status therefore remains
`HOLD_EXTERNAL`.

## Internal collision audit

### P127 — parity transpose/outer-product dynamics

- Carrier algebra is `F_2`, not the Boolean semiring.
- Update transposes and adds a rank-one parity correction.
- Recurrent periods are 1, 2, or 4; fibres are margin/parity equations.
- P171 becomes monotone graph squaring after one step and has only fixed
  recurrence; its fibres are ordered clique covers.
- **Decision:** shared transpose/Gram vocabulary, no literal equality or
  proof transfer.

### P143 — Boolean row-inclusion residual

- Update records support containments, so the first image is a preorder.
- Subsequent behavior is a transpose phase with `T^3=T`.
- Fibres are induced order embeddings into a Boolean lattice.
- **Decision:** same broad Boolean-row carrier but neither the Gram
  intersection map, diameter clock, nor clique-cover fibre.

### P163 — complemented shadow dynamics

- Carrier is a family of subsets; update is a complemented lower shadow.
- Temporal depth is controlled by Johnson-kernel shells.
- Boolean relation powers appear only as a proof tool.
- **Decision:** no literal carrier/update collision and no inverse transfer.

## Bibliography hygiene

Every entry in `references.bib` is cited in `main.tex`.  Titles, author lists,
venues, years, pages, volume/issue fields, ISBNs, and DOIs above were checked
against publisher, proceedings, author-hosted, or catalogue records.  No
unverified citation is used to support a theorem claim.

