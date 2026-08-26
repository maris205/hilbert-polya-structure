# Paper 12 Phase-2 bounded novelty and nearest-precedent search

Search cutoff: **2026-08-15**  
`last_searched_at`: **2026-08-15T03:48:00+08:00**  
Search mode: preregistered exact-family search plus seeded-comparator
verification and one-hop backward/forward chaining  
Verdict ceiling: **SUPPORTED_WITHIN_SEARCH**

## 1. Authorization and exact-byte receipt

The search was opened by the Phase-1 final gate and executed against the
following exact bytes:

| locked artifact | SHA-256 |
|---|---|
| `notes/phase1_final_gate.md` | `fc327245bf5653b18f21f782f4783a2ad0b606340c5f5e7da6516d0514cac72c` |
| `notes/research_protocol.md` | `9213d6e27505c09dbfc24899a15dcca9670e897e754fe40efbc9c1ae7248f434` |
| `notes/candidate_lock.md` | `f0878aaf97e44041460b05c59acd5b5a45fd6d1bef2d7042e3ad273de5320d1c` |
| `notes/pipeline_state.md` | `9a3c2dbf85a4f2f9a8ebe82a6b8ad82b79379bb7bd5245bbe03e9a39a2200e05` |

This report performs a bounded novelty/nearest-precedent comparison only. It
does not prove a Paper-12 target, certify the Deninger packet corollary,
inspect another Phase-2 report, or authorize Phase 3, a Route verdict, or
manuscript release.

## 2. Question and direct-precedent rule

The search question was whether a prior source supplies the exact Paper-12
package, rather than one of its standard ingredients. A record counts as a
**direct precedent** only if one source/theorem package satisfies all four
conditions below:

1. **D1 — same owner/domain:** the relevant nonempty inherited-indiscrete
   real action groupoid (and, for the arithmetic application, the exact
   Deninger fixed-orbit or fixed-prime packet owner), with the normalized
   real-time marking where asserted;
2. **D2 — full unnormalized nerve:** the globally continuous, all-degree,
   unnormalized nerve cochain complex at the locked coefficient and domain
   strength, not merely degree one, normalized cochains, a derived theory,
   or a locally compact/Hausdorff/étale replacement;
3. **D3 — marked isotropy image:** representative-independent restriction
   of the marked cohomology class to isotropy and its image, with the source
   normalization kept explicit; and
4. **D4 — morphism boundary:** the strict/positive-scaled/unmarked
   distinction, its exact covariance/non-descent boundary, and the normalized
   strict quotient functor where claimed.

The test is conjunctive: `D1 AND D2 AND D3 AND D4`. A familiar bar complex,
a standard stabilizer quotient, or a cocycle-preserving isomorphism does not
become a direct precedent by being combined post hoc with unrelated sources.

## 3. Exact query families and screening rule

The locked query families were run without adding a new topical family:

```text
Q1  "continuous cohomology" groupoid (nerve OR composable tuples)
Q2  "continuous cochains" "action groupoid" indiscrete
Q3  "trivial coefficient bundle" groupoid cohomology
Q4  groupoid cocycle isotropy (restriction OR period group)
Q5  "cocycle-preserving" "groupoid isomorphism"
Q6  graded groupoid cocycle scaling
Q7  "R/LZ" "action groupoid" cohomology
Q8  Deninger (cocycle OR cohomology OR isotropy OR "marked period")
Q9  "rational Witt" ("groupoid cohomology" OR cocycle)
```

For interfaces with their own Boolean grammar, only syntax was translated:
arXiv used fielded `all:` clauses and zbMATH used its documented `|` operator
for `OR`. Crossref received each exact string through `query.bibliographic`;
Google Scholar received each exact string through `q`. No synonym family was
introduced.

Records were included in the comparison ledger when a title/abstract or
seeded primary record overlapped at least one locked comparison class and
had independently resolvable bibliographic metadata. They were excluded from
the direct-precedent pool when they concerned a different sense of
“cochain,” an algebraic rather than topological groupoid, only twists or
operator algebras, a different owner/domain, only degree one, or no
independently identifiable scholarly record. Zero exact-family hits were
never treated as proof of novelty.

## 4. Endpoint execution and degradation ledger

An entry `reported total / returned` records what the interface itself
reported and what was actually screened. Endpoint totals are not comparable
across services. Crossref's bibliographic parser, in particular, ignored
much of the phrase/Boolean specificity and produced extremely broad totals.

| endpoint | Q1 through Q9: reported total / returned | execution and degradation |
|---|---|---|
| arXiv API | `0/0, 0/0, 0/0, 2/2, 0/0, 0/0, 0/0, 26/26, 0/0` | HTTP 200. All 28 family hits were retrieved because each nonzero family was below the 50-record cap. The seeded `1807.06400v4` comparator was verified separately because its metadata does not satisfy the extra Q8/Q9 conjuncts. |
| Crossref REST | `590323/5, 833798/5, 147806/5, 1318451/5, 86154/5, 146239/5, 501709/5, 311276/5, 144400/5` | HTTP 200. Forty-five result slots were screened. Totals are noisy recall counts, not exact-phrase counts; no negative inference was drawn from ranking. Exact DOI lookups were then used for seeded records. |
| OpenAlex REST | `unavailable` for Q1--Q9 | Nine attempts returned no result payload. The inspected response was HTTP 429, `Insufficient budget`, with zero daily budget and a reset delay. No count was recorded as zero. |
| Semantic Scholar Graph API | `unavailable` for Q1--Q9 | Q1--Q5 and Q7--Q9 returned HTTP 429. Q6 produced one transient HTTP 200 status-only response, but the payload retry returned HTTP 429; therefore no exported total or record set is claimed for Q6. |
| zbMATH Open REST | `1/1, 0/0, 0/0, 0/0, 0/0, 0/0, 0/0, 112/5, 0/0` | HTTP 200 for hits and the API's `status_code=404`/“No results found” response for empty searches. These counts use the documented `|` translation. Submitting literal `OR` tokens gave empty responses for all nine and was logged as a parser mismatch, not a second search. |
| MathSciNet | `unavailable` | The publication-search request returned HTTP 302 to the LibLynx institutional-access selector. No authenticated session was available; counts were not inferred from web-index snippets. zbMATH supplied the accessible mathematics-index endpoint. |
| Google Scholar | `71/10, total omitted/0, total omitted/1, 1560/10, 4/4, 710/10, total omitted/0, 1560/10, 10/10` | Reproducible direct query URLs initially returned HTTP 200 without a challenge; 55 displayed slots were screened. Q2 and Q7 displayed no records but printed no total, and Q3 displayed one record but printed no total. A later “Cited by” navigation triggered a robot challenge, so that forward edge was marked degraded rather than empty. |
| publisher and journal pages | not a corpus-total interface | DOI landing pages at Cambridge Core, EMS Press, Oxford Academic, ScienceDirect, Springer, and arXiv abstract pages were used to verify titles, domains, abstracts, dates, and available reference lists. |
| author/institution pages | not a corpus-total interface | Deninger's University of Münster record, Wockel's publication list, Farsi's CU Experts profile, and the MPG.PuRe record for Blanco--Uribe--Waldorf were checked as manifestation cross-links. |

Across the four interfaces that returned ranked family records, **134
displayed result slots** were screened before cross-endpoint deduplication
(arXiv 28, Crossref 45, zbMATH 6, Scholar 55). This is a workload count, not
a count of unique works. Seeded comparators and one-hop chain records were
screened separately. OpenAlex, Semantic Scholar, and MathSciNet contribute
no false zero to that number.

## 5. Included-source ledger

“Included” means retained as a nearest-class comparator, not that its
hypotheses or convention have been imported into Paper 12.

| ID | source and primary locator | comparison class | include reason and boundary |
|---|---|---|---|
| I01 | K. A. Mackenzie, [*Rigid cohomology of topological groupoids*](https://www.cambridge.org/core/journals/journal-of-the-australian-mathematical-society/article/rigid-cohomology-of-topological-groupoids/E6F26A7B330EB996D3D8AF982BA18DA5), 1978, DOI `10.1017/S1446788700011794` | topological-groupoid cohomology; vertex/isotropy groups | The publisher abstract gives a cohomology theory for locally trivial, locally compact topological groupoids with vector-bundle coefficients and identifies it with vertex-group cohomology. Its domain and derived/module construction do not match the inherited-indiscrete owner or the marked package. |
| I02 | J. Blanco, B. Uribe, K. Waldorf, [*Pontrjagin duality on multiplicative gerbes*](https://ems.press/journals/jncg/articles/12586094), 2023, DOI `10.4171/JNCG/528`, §§2.3--2.4 | continuous simplicial/nerve cochains; topological-group cohomology | The cited sections explicitly discuss continuous cochains on a simplicial space and the nerve of a one-object topological group under paracompact/compactly generated and coefficient hypotheses. This is a convention comparator, not the Paper-12 action-groupoid owner or marking theorem. |
| I03 | C. Farsi, L. Huang, A. Kumjian, J. Packer, [*Cocycles on groupoids arising from* `N^k`-*actions*](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/cocycles-on-groupoids-arising-from-mathbb-nkactions/B70BFA05CEAB5475C63CAA49C539F323), 2022, DOI `10.1017/etds.2021.69`, Definition 3.7 | continuous groupoid 1-cocycles and coboundaries | Definition 3.7 matches the standard degree-one statement “continuous groupoid homomorphism,” and the paper classifies 1-cocycles for étale groupoids from commuting local homeomorphisms on compact Hausdorff spaces. It is not an all-degree inherited-indiscrete result. |
| I04 | M. Fuchssteiner, C. Wockel, [*Topological Group Cohomology with Loop Contractible Coefficients*](https://arxiv.org/abs/1110.2977), published DOI `10.1016/j.topol.2012.04.006` | globally versus locally continuous topological-group cochains | This compares continuous group cochains with cochains continuous near the identity for topological groups and loop-contractible coefficients. It supplies a convention/domain comparison for the time group, not groupoid marking or isotropy recovery. |
| I05 | F. Wagemann, C. Wockel, [*A Cocycle Model for Topological and Lie Group Cohomology*](https://arxiv.org/abs/1110.3304), published DOI `10.1090/S0002-9947-2014-06107-2` | topological-group cohomology models | This later related model distinguishes globally continuous and locally continuous group cohomology. It remains a one-object group result with coefficient/hypothesis qualifications. |
| I06 | J. Lackman, [*Cohomology of Lie Groupoid Modules and the Generalized van Est Map*](https://academic.oup.com/imrn/article-abstract/2022/15/11484/6224268), DOI `10.1093/imrn/rnab027` | Lie-groupoid modules and sheaf cohomology | This treats smooth/holomorphic Lie groupoids, sheaves, and generalized modules. It is close to the module vocabulary but not the locked globally continuous trivial-bundle nerve complex. |
| I07 | V. Deaconu, M. Ionescu, [*Cohomology of ample groupoids*](https://arxiv.org/abs/2501.00166), v3 (2025) | ample-groupoid module/cohomology comparison | This introduces a flat-resolution complex for ample groupoids and compares it with continuous cocycle cohomology. “Ample” and the chosen resolution do not match the non-Hausdorff inherited-indiscrete owner or the four-part package. |
| I08 | T. M. Carlsen, E. Ruiz, A. Sims, M. Tomforde, [*Reconstruction of groupoids and C*-rigidity of dynamical systems*](https://arxiv.org/abs/1711.01052), Adv. Math. 390 (2021), DOI `10.1016/j.aim.2021.107923` | graded groupoids and grading-preserving isomorphisms | This gives a strong nearest analogue for strict preservation of a discrete-group grading on second-countable locally compact Hausdorff étale groupoids. It does not provide positive real rescaling, the unmarked countercategory, or the period image. |
| I09 | B. Steinberg, [*Diagonal-preserving isomorphisms of étale groupoid algebras*](https://arxiv.org/abs/1711.01903), DOI `10.1016/j.jalgebra.2018.10.024` | groupoid reconstruction/isomorphism | This was retained because Q5/Q6 ranked the graded/diagonal-preserving isomorphism literature. Its owner is an étale groupoid algebra and it contains neither the cochain package nor marked period covariance. |
| I10 | B. Armstrong, N. Brownlowe, A. Sims, [*Simplicity of twisted C*-algebras of Deaconu--Renault groupoids*](https://arxiv.org/abs/2109.02583), DOI `10.4171/JNCG/527` | isotropy restriction/quotient adjacent work | This forward-chain record studies continuous circle-valued 2-cocycles and the quotient by interior isotropy. It is useful to separate standard isotropy/twist operations from the locked real 1-class image. |
| I11 | C. Deninger, [*Dynamical systems for arithmetic schemes*](https://arxiv.org/abs/1807.06400), exact `1807.06400v4`; publisher DOI `10.1016/j.indag.2024.05.007` | rational-Witt dynamical owner | The primary abstract constructs rational-Witt real dynamical systems and relates periodic orbits to closed points. It is the seeded owner source, not a source for a Paper-12 groupoid cohomology, marking category, or quotient functor. |
| I12 | [*Homogeneous space*](https://encyclopediaofmath.org/wiki/Homogeneous_space) and [*Topological group*](https://encyclopediaofmath.org/wiki/Topological_group), Encyclopedia of Mathematics | homogeneous quotient recovery | These record the standard set-level identification of a transitive orbit with `G/H` and the quotient topology on a topological-group coset space. They do not identify a cohomological marked image or prove the Paper-12 one-sided topology/functorial ceiling. |
| I13 | Papers 9--11 as summarized in locked `research_protocol.md`, §§1 and 11 | internal prior use | Only the locked delta was used: Paper 9 owns the inherited topology, Paper 10 the actual/standard quotient direction, and Paper 11 the arrow-level time factorization. No sibling Phase-2 report was opened. None is recorded there as owning the all-degree marked package. |

## 6. Representative exclusion ledger

| query/route | representative record | exclusion reason |
|---|---|---|
| arXiv Q4 | *A twist over a minimal étale groupoid that is topologically nontrivial over the interior of the isotropy*, `2312.08683` | A twist/continuous 2-cocycle restriction problem on a Hausdorff étale groupoid, not the real marked 1-class or all-degree complex. |
| arXiv Q4 | *KMS states on the C*-algebras of Fell bundles over groupoids*, `1708.00629` | Operator-algebra/KMS target; no exact cohomology/marking package. |
| Crossref Q1/Q7 | *Strongly groupoid graded rings and cohomology* and algebraic groupoid-extension results | “Groupoid graded” is algebraic and not the topological action-groupoid owner. |
| Crossref Q2 | *Mass continuous cochains are differential forms* | “Continuous cochains” has a geometric-measure meaning unrelated to the nerve complex. |
| Scholar Q1 | *Four equivalent versions of nonabelian gerbes*, Haefliger/differentiable-cohomology records, and stack-cohomology records | Adjacent simplicial/sheaf theories, but not the locked owner, coefficient convention, or marked period boundary. |
| Scholar Q3 | *Recoverable-Support Geometry and Response Visibility: Descent, Holonomy Intertwiners, and the Premetric G1 Handoff* | One displayed result, but no independently verified public mathematical manifestation matching the target; excluded from precedent credit. |
| Scholar Q5/Q6 | *Groupoid Models of C*-algebras and Gelfand Duality*, Steinberg-algebra reconstruction, hyperbolic-groupoid, and twisted-K-theory records | Retained only the resolvable graded-isomorphism comparators I08--I09; the remaining records concern algebra reconstruction, metrics, or twists and lack D2--D4. |
| Scholar/arXiv Q8 | older Deninger cohomology, determinant, foliation, and zeta-function records | The name/keyword conjunction is broad. None of the 26 title/metadata records returned by arXiv Q8 is the seeded rational-Witt marked groupoid package; `1807.06400v4` was instead checked directly. |
| Scholar Q9 | trace forms, Galois realizations, motivic classes, modular surfaces, and other rational-Witt-adjacent results | Wrong owner and no groupoid cocycle/cohomology package. |
| Q2 and Q7 zero-display pages | no displayed record | Logged as search outcomes only. They do not support a novelty conclusion by themselves. |

## 7. Backward and forward chaining

Backward chaining used publisher/arXiv reference lists or Crossref reference
metadata. Forward chaining used Crossref `is-referenced-by-count`, zbMATH's
`rft:` reference-text search, and author/publisher cross-links. Counts are
endpoint snapshots and are explicitly not completeness claims.

| seed | backward screen | forward screen through cutoff | relevance result |
|---|---|---|---|
| Mackenzie 1978 | Publisher page lists 14 references; the nearest antecedents are Hochschild--Mostow on topological/Lie-group cohomology, Higgins on discrete groupoids, and Moore on locally compact group extensions/cohomology. | Crossref: 5; Scholar exact-record page displayed 8 before its cited-by challenge; zbMATH `rft:`: 4. The relevant descendant screened was Huebschmann, *Equivariant cohomology over Lie groupoids and Lie--Rinehart algebras* (2009), a locally trivial Lie-groupoid/derived de Rham theory. | Confirms a substantial groupoid-cohomology lineage, but no descendant in the bounded chain joined D1--D4. |
| Blanco--Uribe--Waldorf 2023 | §§2.3--2.4 lead backward to Segal--Mitchison and continuous/topological-group cohomology models. Crossref exported zero references for this DOI; that is missing metadata, not a source claim of zero bibliography. | Crossref: 0; zbMATH `rft:`: 1, which was the source record itself. | Strong convention comparator for continuous simplicial cochains, not a direct action-groupoid precedent. |
| Farsi--Huang--Kumjian--Packer 2022 | Crossref exports 34 references; the paper's stated lineage is Deaconu--Renault groupoids, continuous cocycles, Ruelle operators, and KMS states. | Crossref: 0; CU Experts displayed citation count 1; zbMATH `rft:`: 1, Armstrong--Brownlowe--Sims on twisted Deaconu--Renault groupoids. | Forward record concerns circle-valued 2-cocycles and isotropy quotient structure, not the marked real 1-class package. |
| Fuchssteiner--Wockel 2012 | Crossref exports 18 references concerning competing topological-group cohomology models and coefficient conditions. | Crossref: 1; zbMATH `rft:`: 0. Wockel's author list identifies the related later Wagemann--Wockel cocycle model. | Nearest topological-group comparison only. |
| Lackman 2022 | Crossref exports 24 references in the Lie-groupoid module/van Est lineage. | Crossref: 1; zbMATH `rft:`: 1, Lackman's 2026 *A Geometric Definition of the Integral and Applications*, which uses pair-groupoid cochains/van Est. | Still a smooth/Lie or pair-groupoid theory, not D1--D4. |
| Steinberg 2019 | Crossref exports 40 references in étale-groupoid algebra reconstruction. | Crossref: 20; zbMATH `rft:`: 22, with the first five screened (projections/diagonal homomorphisms, Leavitt path algebras, chain conditions, twists, and simplicity). | Dense forward lineage for algebra-preserving isomorphisms, but not cohomological clock scaling or period recovery. |
| Deninger `1807.06400v4` / publisher DOI | Crossref exports 40 references; the primary arXiv/publisher record is the rational-Witt dynamical construction. | Crossref: 2; zbMATH `rft:`: 3. The titles and metadata of all 26 arXiv Q8 results were screened; they concern arithmetic/foliated cohomology, determinants, and zeta analogies rather than the exact marked action-groupoid package. | Establishes the application owner and nearby arithmetic literature, not a direct precedent for Paper 12. |

Google Scholar's cited-by navigation became non-reproducible after the exact
family pass because it returned a robot challenge. No citing-work title or
count was silently filled from that blocked page. Crossref and zbMATH
coverage can omit references/citations, so their zeros were not interpreted
as absence.

## 8. Nearest-precedent matrix

`Partial` means that a source supplies a recognizable analogue but fails the
locked strength. It does not satisfy that direct-precedent condition.

| nearest class | nearest source(s) | D1 same owner/domain | D2 full locked unnormalized nerve | D3 marked isotropy image | D4 strict/scaled/unmarked boundary | direct precedent? |
|---|---|---:|---:|---:|---:|---:|
| continuous nerve/simplicial cochains | I02 Blanco--Uribe--Waldorf | No | Partial: continuous cochains on simplicial spaces/topological-group nerve under different hypotheses | No | No | **No** |
| topological-group cohomology | I04 Fuchssteiner--Wockel; I05 Wagemann--Wockel | No: one-object topological groups | Partial: globally/local continuous group complexes, not the action-groupoid owner | No | No | **No** |
| topological-groupoid modules/cohomology | I01 Mackenzie; I06 Lackman; I07 Deaconu--Ionescu | No: locally trivial locally compact, Lie, or ample domains | Partial: derived/sheaf/flat-resolution theories rather than the exact global nerve complex | Partial only in vertex/module language | No | **No** |
| continuous 1-cocycles | I03 Farsi et al. | No: compact Hausdorff, étale `N^k` action groupoids | Degree one only | Partial: restriction to an isotropy subgroup is available at cocycle level, but no locked class-image theorem | No | **No** |
| cocycle-preserving/graded isomorphisms | I08 Carlsen et al.; I09 Steinberg | No: étale/C*- or algebraic reconstruction domain | No | No | Partial: strict grading preservation analogue, without positive scaling and unmarked non-descent package | **No** |
| isotropy restriction | I01, I03, I10 | No | No single source supplies D2 | Partial: vertex groups or restricted 2-cocycles, not `Per_x([b])` with source-normalized `[c]` | No | **No** |
| homogeneous quotient recovery | I12 standard `G/H` background | Only the generic set/topological-group fact, not the cohomological owner | No | No: `H` is a given stabilizer, not a recovered marked-class image | Partial: unbased quotient standard, but no normalized strict functor, basepoint-change law, or one-sided inherited topology result | **No** |
| Deninger and Papers 9--11 | I11 Deninger; I13 locked internal delta | Application owner only; generic theorem not owned there | Partial: Paper 11 is recorded only at arrow degree, not all nerve degrees | Partial: Deninger/Paper 9 own stabilizer/topology, not representative-independent marked cohomology restriction | No prior strict/scaled/unmarked categories recorded | **No** |

No screened source passed all four columns. The closest single external
precedent is Mackenzie for topological-groupoid cohomology/vertex reduction;
the closest exact degree-one convention is Farsi et al.; the closest nerve
cochain convention is Blanco--Uribe--Waldorf; and the closest morphism
analogue is graded-groupoid reconstruction. Each misses multiple required
components and has a different owner/domain.

## 9. Bounded verdict and standalone implication

**Verdict: `SUPPORTED_WITHIN_SEARCH`.**

Within the preregistered query families, seeded comparators, endpoint
degradations, and one-hop chains executed through the 2026-08-15 cutoff, no
direct precedent satisfying `D1 AND D2 AND D3 AND D4` was identified. This is
a bounded search statement, not an assertion of absolute novelty, priority,
or exhaustive literature coverage.

**Standalone implication:** the novelty branch, by itself, does **not** force
`NOTE_OR_MERGE` on the “direct matching precedent” condition. It also does
**not** authorize `STANDALONE_PASS`. The latter remains contingent on all
locked mathematical/source obligations, including the all-degree theorem,
same-object marked-period recovery, the source-verified `PACKET_COROLLARY`,
the strict/scaled/unmarked theorem, the normalized quotient functor,
controls, independent review, and later release gates. An `ORBIT_ONLY`
source result, a routine-collapse finding, or a failed later gate can still
force `NOTE_OR_MERGE` under the protocol.

Machine-readable summary:

```text
NOVELTY_VERDICT=SUPPORTED_WITHIN_SEARCH
DIRECT_PRECEDENT_FOUND=false
NOTE_OR_MERGE_DIRECT_PRECEDENT_TRIGGER=false
STANDALONE_PASS_AUTHORIZED=false
PHASE3_AUTHORIZED=false
SEARCH_CUTOFF=2026-08-15
LAST_SEARCHED_AT=2026-08-15T03:48:00+08:00
```

## 10. Retention and limitations

- No new PDF was retained. No source file, cache, bibliography database, or
  sibling report was created or modified; the only written artifact from
  this task is this Markdown report.
- OpenAlex exhausted its anonymous daily budget; Semantic Scholar was
  rate-limited; MathSciNet required institutional authentication; and
  Scholar's cited-by edge later presented a robot challenge.
- Crossref totals were highly nonspecific, zbMATH and Crossref citation
  metadata were incomplete for some records, and publisher indexing varies.
- The exact English query families may miss differently worded or non-English
  work. The seeded comparator and one-hop chain reduce but do not eliminate
  that limitation.
- Abstract/landing-page screening can distinguish domains and package
  components but is not a substitute for the Phase-3 direct proofs or a
  source-strength audit of every theorem statement.
