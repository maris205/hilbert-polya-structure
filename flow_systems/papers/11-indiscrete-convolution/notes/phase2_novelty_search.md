# Paper 11 Phase-2 bounded exact-precedent / novelty search

Frozen: **2026-08-15 (Asia/Shanghai)**  
`last_searched_at`: **2026-08-15T00:37:14+08:00**  
Search classification: **SUPPORTED_WITHIN_SEARCH**  
Exact-package precedents included: **0**  
New full texts or PDFs retained by this search: **0**

This is a bounded exact-precedent search, not a proof, convention audit,
control run, Route decision, manuscript edit, or claim of absolute priority.
Its only permitted conclusion is that the exact package below was not located
within the documented search. “First,” “unprecedented,” “no prior work,” and
equivalent global formulations remain forbidden.

## 1. Exact novelty unit and mandatory distinctions

A record counted as an **exact included precedent** only if one work, or an
explicitly linked work sequence, treated the following conjunction on the
same object and topology:

1. a fixed actual rational-Witt / finite-kernel Deninger time orbit with its
   inherited nontrivial indiscrete topology, rather than an ordinary circle;
2. the transformation groupoid of that actual orbit and the real-time action;
3. globally continuous functions with open-cover quasi-compact support,
   their convolution/involution, and the collapse to ordinary `C_c(R)`;
4. a separate Hausdorff-open-span diagnostic together with the applicability
   boundary for published non-Hausdorff groupoid conventions;
5. regular representations and full/reduced completions transported from
   the group `R`, without relabelling them as standard groupoid completions;
6. an ordinary standard-circle proxy, including the direction and strict
   image boundary of the actual-to-proxy function map.

The unit is deliberately conjunctive. The following are registered as
**non-novel background or different owners**, even when mathematically close:

- the generic lemma that continuous maps from a nonempty indiscrete space to
  a `T0` target are constant, and its product-space variants;
- Paper 10's collapse of unit-space separated observables;
- Deninger's Section 11 convolution on the pro-discrete group
  `inverse-limit K^times` and its submonoid;
- standard locally Hausdorff or Hausdorff groupoid `C_c` frameworks;
- the ordinary transitive-circle crossed product and Green imprimitivity;
- Paper 9's actual-orbit topology theorem by itself.

Consequently, none of those components alone counts as an exact precedent,
and Paper 11 may not claim novelty for any one of them in isolation.

## 2. Search protocol

### 2.1 Bounds

- **Coverage date:** database inception through 2026-08-15.
- **Search window:** 2026-08-14--2026-08-15, Asia/Shanghai.
- **Document classes:** journal articles, preprints, monographs, proceedings,
  authoritative author copies, DOI/publisher records, and the project's
  already-audited Paper 8--10 source ledgers.
- **Language:** no endpoint language filter was imposed. Exact search terms
  were the English and symbolic terms used by the source literature.
- **Inclusion rule:** same rational-Witt actual orbit/topology plus the exact
  arrow-level analytic and convention/proxy package in Section 1.
- **Exclusion rule:** lexical false positives; generic topology; unit-only
  collapse; different arithmetic spaces; different convolution owners;
  generic groupoid frameworks; and standard-circle proxy results that do not
  treat the actual indiscrete object.
- **Full-text rule:** no candidate PDF would be retained unless an exact
  included precedent required full-text adjudication. No such candidate was
  found. Existing audited local copies were read only to verify the two
  closest arithmetic exclusions and exact locators.
- **Stop rule:** stop when exact-conjunction searches had been run across the
  arXiv API, Crossref, general web discovery, authoritative source endpoints,
  and the inherited project ledgers; the candidate set had stabilized into
  the distinct nearest-precedent buckets below; and no exact candidate
  remained for full-text inclusion. The search is now frozen.

### 2.2 Databases and endpoints

| Endpoint / corpus | Mode | Count semantics and status |
|---|---|---|
| arXiv Export API | exact Boolean and decomposed calibration queries | Numeric `opensearch:totalResults` recorded below; available |
| Crossref Works API | `query.bibliographic`, `rows=1`, top-title calibration | Numeric `total-results` recorded below; lexical candidate-pool counts, not exact-match counts |
| General web search | exact phrases plus source-verification queries | Result-count total was not exposed (`NOT_EXPOSED`); returned records were screened |
| Publisher, DOI, arXiv-record, and author pages | manifestation/source verification | Record verification, not a corpus hit count |
| OpenAlex Works API | planned independent endpoint | `API_DEGRADED`: HTTP 429; `Retry-After: 27071`; no count asserted |
| Semantic Scholar Graph API | planned independent endpoint | `API_DEGRADED`: HTTP 429 “Too Many Requests”; no count asserted |
| zbMATH / MathSciNet discovery | web-indexed discovery attempt | Direct reproducible corpus totals unavailable in this environment; no count asserted and no subscription-completeness claim |
| Local Paper 8--10 audited ledgers | owner and nearest-precedent cross-check | Exact local artifacts, not a bibliographic database |

OpenAlex, Semantic Scholar, zbMATH, and MathSciNet limitations are disclosed
rather than converted into zero hits. The bounded conclusion therefore rests
on the available endpoints and source verification, not on fictional database
coverage.

## 3. Reproducible query and hit ledger

### 3.1 arXiv exact-conjunction queries

The following strings were sent to the arXiv Export API. Counts are
`opensearch:totalResults` at `last_searched_at`.

| ID | Exact `search_query` | Hits | Exact included |
|---|---|---:|---:|
| A1 | `all:Deninger AND all:"rational Witt" AND all:indiscrete AND all:groupoid AND all:convolution` | 0 | 0 |
| A2 | `all:"rational Witt vectors" AND all:"transformation groupoid" AND all:convolution` | 0 | 0 |
| A3 | `all:Deninger AND all:E_f AND all:groupoid AND all:"C*-algebra"` | 0 | 0 |
| A4 | `all:"finite-kernel" AND all:Deninger AND all:orbit AND all:convolution` | 0 | 0 |
| A5 | `all:"global continuous" AND all:"quasi-compact support" AND all:groupoid AND all:convolution` | 0 | 0 |
| A6 | `all:"Hausdorff open" AND all:span AND all:groupoid AND all:convolution` | 0 | 0 |
| A7 | `all:Deninger AND all:"pro-discrete" AND all:convolution` | 0 | 0 |
| A8 | `all:"rational Witt" AND all:"C*(R)" AND all:"crossed product"` | 0 | 0 |
| A9 | `all:Deninger AND all:orbit AND all:"Green imprimitivity"` | 0 | 0 |
| A10 | `all:Deninger AND all:"rational Witt" AND all:groupoid AND all:convolution` | 0 | 0 |

The zero conjunction counts were calibrated against broader queries so that
an endpoint or parser failure was not mistaken for a negative result.

| ID | Exact `search_query` | Hits | Screened result / interpretation |
|---|---|---:|---|
| AC1 | `all:Deninger AND all:"rational Witt"` | 2 | Deninger's arithmetic dynamics article and rational-Witt sheaf article; both ledgered below |
| AC2 | `all:Deninger AND all:groupoid` | 2 | Unrelated lexical/citation hits; neither is a rational-Witt orbit-convolution paper |
| AC3 | `all:Deninger AND all:convolution` | 1 | “Injective convolution operators on ell^infinity(Gamma) are surjective”; unrelated owner |
| AC4 | `ti:"Non-Hausdorff groupoids"` | 8 | Generic non-Hausdorff-groupoid title bucket |
| AC5 | `all:"non-Hausdorff groupoid" AND all:convolution` | 0 | Vocabulary-sensitive negative; not used alone |
| AC6 | `all:"Green imprimitivity" AND all:"C_0(G/H)"` | 0 | Known theorem is verified from the author monograph, so this is only an arXiv-index calibration |
| AC7 | `ti:"Dynamical systems for arithmetic schemes"` | 1 | Exact Deninger title recovered |
| AC8 | `all:"Dynamical systems for arithmetic schemes" AND all:convolution` | 0 | No conjunctive arXiv record |
| AC9 | `all:"Dynamical systems for arithmetic schemes" AND all:groupoid` | 0 | No conjunctive arXiv record |
| AC10 | `all:"Dynamical systems for arithmetic schemes" AND all:"C*-algebra"` | 0 | No conjunctive arXiv record; successful retry after one transient TLS reset |
| AC11 | `all:"Dynamical systems for arithmetic schemes" AND all:indiscrete` | 0 | No conjunctive arXiv record |
| AC12 | `all:"Dynamical systems for arithmetic schemes" AND all:"quasi-compact"` | 0 | No conjunctive arXiv record |
| AC13 | `all:"Dynamical systems for arithmetic schemes" AND all:"transformation groupoid"` | 0 | No conjunctive arXiv record |

These are discovery/index counts. In particular, zero indexed conjunctions
do not prove phrase absence from all literature.

### 3.2 Crossref discovery counts

Each exact string below was sent as `query.bibliographic` with `rows=1`.
Crossref's `total-results` is a broad relevance-pool count, not the number of
exact phrase matches. The top result is recorded to make lexical drift
auditable.

| ID | Exact query | `total-results` | Top returned title | Disposition |
|---|---|---:|---|---|
| C1 | `Deninger rational Witt actual indiscrete orbit transformation groupoid convolution` | 759679 | “Witt vector rings and the relative de Rham Witt complex” | drift; exclude |
| C2 | `"rational Witt vectors" transformation groupoid convolution` | 671694 | “Witt vectors which are rational functions” | drift; exclude |
| C3 | `Deninger E_f orbit groupoid C*-algebra` | 225043 | “Prime groupoid graded rings with applications to partial skew groupoid rings” | drift; exclude |
| C4 | `finite-kernel Deninger orbit convolution` | 520253 | “Figure 6: Convolution kernel operation.” | drift; exclude |
| C5 | `global continuous quasi-compact support groupoid convolution` | 2723796 | “5 Distributions with Compact Support” | drift; exclude |
| C6 | `Hausdorff-open span globally continuous groupoid convolution` | 1504650 | “Examples and Open Questions” | drift; exclude |
| C7 | `Deninger K^x pro-discrete convolution` | 433863 | “Pro Football Was Made for Television” | drift; exclude |
| C8 | `rational Witt transported C*(R) standard circle crossed product` | 913135 | “Orthogonal Polynomials on the Unit Circle with Respect to a Rational Weight Function” | drift; exclude |
| C9 | `Deninger orbit C*(R) Green imprimitivity` | 790692 | “The structure of imprimitivity algebras” | generic theorem bucket; exclude exact |
| C10 | `Deninger rational Witt groupoid convolution 2026` | 6545096 | “Functoriality of bornological groupoid convolution” | generic groupoid bucket; exclude exact |

Crossref therefore supplied candidate discovery and negative calibration but
no exact included precedent. Its large counts must not be reported as large
numbers of close precedents.

### 3.3 General-web exact and source-verification queries

The search provider exposed ranked results but no stable corpus-total field,
so the hit-count entry is `NOT_EXPOSED`, not zero. Returned records were
screened; exact included count was zero for every row.

| ID | Exact query | Provider total | Exact included |
|---|---|---|---:|
| W1 | `"rational Witt" transformation groupoid convolution` | `NOT_EXPOSED` | 0 |
| W2 | `"rational Witt vectors" groupoid C*-algebra convolution` | `NOT_EXPOSED` | 0 |
| W3 | `Deninger E_f orbit transformation groupoid convolution` | `NOT_EXPOSED` | 0 |
| W4 | `"finite-kernel" Deninger orbit groupoid convolution` | `NOT_EXPOSED` | 0 |
| W5 | `Deninger "E_f" groupoid C* convolution` | `NOT_EXPOSED` | 0 |
| W6 | `"actual indiscrete orbit" convolution groupoid` | `NOT_EXPOSED` | 0 |
| W7 | `"global continuous" "quasi-compact support" groupoid convolution` | `NOT_EXPOSED` | 0 |
| W8 | `"Hausdorff open" span "globally continuous" convolution groupoid` | `NOT_EXPOSED` | 0 |
| W9 | `"Dynamical systems for arithmetic schemes" groupoid convolution` | `NOT_EXPOSED` | 0 |
| W10 | `"Dynamical systems for arithmetic schemes" C*-algebra` | `NOT_EXPOSED` | 0 |
| W11 | `"rational Witt" crossed product Deninger` | `NOT_EXPOSED` | 0 |
| W12 | `Deninger rational Witt transformation groupoid 2026` | `NOT_EXPOSED` | 0 |

The following source-verification queries located known generic baselines;
they were not counted as exact precedents:

| ID | Exact query | Verified baseline |
|---|---|---|
| WV1 | `"C_0(G/H)" crossed product "C^*(H)" compact operators` | Williams/Green homogeneous-space theorem |
| WV2 | `transitive transformation groupoid crossed product C*(H) tensor compact operators` | standard transitive-action / imprimitivity bucket |
| WV3 | `Green imprimitivity theorem C0(G/H) crossed product official` | authoritative Williams author copy |
| WV4 | `Deninger rational Witt transformation groupoid 2026` | Deninger and adjacent Morishita records, not the exact package |

## 4. Include / exclude ledger

`EXCLUDE_EXACT` below means “not an exact package precedent.” It does not
mean irrelevant, incorrect, or absent from the eventual bibliography.

| ID | Candidate | Verification level | What it owns | What is missing from the exact unit | Exact-precedent disposition |
|---|---|---|---|---|---|
| N1 | Christopher Deninger, [“Dynamical systems for arithmetic schemes”](https://arxiv.org/abs/1807.06400), journal manifestation *Indagationes Mathematicae* 37(1) (2026), 25--136, [DOI 10.1016/j.indag.2024.05.007](https://doi.org/10.1016/j.indag.2024.05.007) | Existing audited arXiv v4 full text, SHA-256 `edd0bc8c2efb601ed7574e8eceae40e8cde21d0e4b2bc8c4ce7e60d8e1f82a09`; exact Section 11 locators checked | Rational-Witt arithmetic dynamics and source orbit/action material; separately, a pro-discrete group convolution in Section 11 | No actual-orbit transformation groupoid, no global/HOpen convention split, no transported actual completion, no standard-circle strict-image comparison | `NEAREST_ARITHMETIC_BASELINE`; `EXCLUDE_EXACT` |
| N2 | Christopher Deninger, [“Rational Witt vectors and associated sheaves”](https://arxiv.org/abs/2508.05329) | Official arXiv title/abstract/metadata | Adjacent rational-Witt algebraic/sheaf theory | Does not present the exact dynamical arrow-convolution package | `ADJACENT_SOURCE`; `EXCLUDE_EXACT` |
| N3 | Christopher Deninger, [“Primes, knots and periodic orbits”](https://arxiv.org/abs/2301.11643) | Official arXiv record plus inherited audited source ledger | Survey/source lineage for arithmetic dynamical analogies | No exact actual-orbit groupoid and analytic convention package | `SURVEY_BASELINE`; `EXCLUDE_EXACT` |
| N4 | Masanori Morishita, [“Deninger's dynamical systems and Connes--Consani's noncommutative geometry”](https://arxiv.org/abs/2508.15971) | Existing audited v5 full text, SHA-256 `3a5a34165a4bedfefb2c06f43f4e40e416882ae3406a9cd043f6ac12aebb21ae` | Current comparison of rational-Witt/Deninger systems with Connes--Consani adelic spaces | No groupoid/convolution construction on the actual fixed indiscrete orbit and no global/HOpen/transport/proxy package | `NEAREST_CURRENT_ADJACENT`; `EXCLUDE_EXACT` |
| N5 | Paper 9 actual-orbit topology theorem | Exact internal proof/source artifacts inherited by the active protocol | Actual fixed-orbit topology and action/stabilizer ownership | No arrow-level transformation groupoid or convolution/completion theorem | `INTERNAL_SOURCE_OWNER`; `EXCLUDE_EXACT` |
| N6 | Paper 10 unit-collapse theorem, `notes/proof_audit.md`, SHA-256 `efda522ead9efebfc3f59f0688f2dfd3fe63f63ff4efd4377068485d1a4acc3a` | Exact internal proof artifact | Constant separated-target maps and scalar/Borel/operator-observable collapse on the **unit space** | No arrow topology, quasi-compact support, fibre convolution, regular representation, or convention/proxy split | `INTERNAL_NEAREST_THEOREM`; `EXCLUDE_EXACT` |
| N7 | Jean-Louis Tu, [“Non-Hausdorff groupoids, proper actions and K-theory”](https://ems.press/journals/dm/articles/8965109), [DOI 10.4171/DM/178](https://doi.org/10.4171/DM/178) | Existing audited official full text and exact locators | Published locally compact/locally Hausdorff convention, Hausdorff-open `C_c` span, Haar-system domain | Actual Paper-11 unit/arrow space fails the framework's local-Hausdorff compact-neighborhood assumptions | `FRAMEWORK_BASELINE`; `EXCLUDE_EXACT` |
| N8 | Paul S. Muhly and Dana P. Williams, [“Renault's Equivalence Theorem for Groupoid Crossed Products”](https://nyjm.albany.edu/m/2008/3.htm), [arXiv:0707.3566](https://arxiv.org/abs/0707.3566) | Existing audited official full text and exact locators | Accepted Hausdorff-open-span practice and patch convolution under standing hypotheses | Hausdorff unit and local-Hausdorff/local-compact assumptions fail for the actual object | `FRAMEWORK_BASELINE`; `EXCLUDE_EXACT` |
| N9 | Ruy Exel, [“Non-Hausdorff groupoids”](https://arxiv.org/abs/0812.4087) | Existing audited arXiv v3 full text | Étale non-Hausdorff-arrow framework with Hausdorff unit | Actual unit is non-Hausdorff and real-time fibres are not étale | `FRAMEWORK_BOUNDARY`; `EXCLUDE_EXACT` |
| N10 | Alcides Buss, Rohit Holkar, and Ralf Meyer, [“A universal property for groupoid C*-algebras. I”](https://arxiv.org/abs/1612.04963), [DOI 10.1112/plms.12131](https://doi.org/10.1112/plms.12131) | Existing audited final accepted arXiv v2 full text | Hausdorff groupoid universal property and ordinary transformation-groupoid/crossed-product identification | Hausdorff hypotheses fail on the actual groupoid; applies only to the standard proxy | `HAUSDORFF_PROXY_BASELINE`; `EXCLUDE_EXACT` |
| N11 | Dana P. Williams, [*Crossed Products of C*-Algebras*, author draft 3.1](https://math.dartmouth.edu/~dana/cpcsa/draft3.1.pdf) | Existing audited authoritative author copy and exact locators | `C^*(R)`, reduced norm/amenability, Fourier sign, Green's homogeneous-space theorem | These are group and standard-circle proxy results, not actual-groupoid topology or a standard actual completion | `GROUP_AND_PROXY_BASELINE`; `EXCLUDE_EXACT` |
| N12 | Generic indiscrete-space and product-space lemmas | Registered background class; no novelty credit sought | Constancy/factorization facts available without arithmetic input | Does not supply rational-Witt ownership or the exact convention/completion/proxy package | `GENERIC_BACKGROUND`; `EXCLUDE_EXACT` |

### 4.1 Exact adjudication of the two closest arithmetic records

**Deninger Section 11 is a different convolution owner.** In the existing
audited v4 full text, physical pp. 66--67, equation (104) introduces the
pro-discrete inverse-limit group `inverse-limit K^times`; the text proves it
is zero-dimensional and locally compact, chooses Haar measure, and defines
ordinary compact-support group convolution in equation (105). Equation (107)
embeds the submonoid function space, and Lemma 11.1 with equations
(108)--(110) proves the induced non-unital subalgebra. This is a serious
arithmetic convolution precedent, but it is not convolution on
`X_{p,a} rtimes R`. A full-text term screen of that exact PDF returned no
occurrence of `groupoid`, `transformation groupoid`, `crossed product`,
`C*-algebra`, or `indiscrete`. The exclusion is therefore an exact-owner
distinction, not an inference from the title alone.

**Morishita is current and adjacent, but not exact.** The existing audited v5
full text links rational-Witt/Deninger dynamics to Connes--Consani spaces. A
full-text screen returned no `groupoid`, `convolution`, `C*-algebra`, or
`indiscrete`. Its single crossed-product discussion describes the usual
noncommutative adelic quotient, not the fixed actual rational-Witt orbit
groupoid or the global/HOpen split. It remains the nearest current adjacent
comparison, not an exact included precedent.

## 5. Nearest-precedent matrix

| Precedent bucket | Actual rational-Witt fixed orbit/topology | Actual transformation groupoid | Global continuous qc-support convolution | HOpen/applicability split | Transported `C^*(R)` norms | Standard-circle strict proxy boundary |
|---|---|---|---|---|---|---|
| Deninger dynamics + Section 11 | source orbit/action; Section 11 is a different owner | no | different pro-discrete-group convolution only | no | no | no |
| Paper 9 | yes, topology owner | no | no | no | no | no |
| Paper 10 | unit-space generic collapse only | no | no | no | no | no |
| Tu / Muhly--Williams / Exel | no arithmetic owner | generic frameworks only | different function domains and standing hypotheses | yes, as literature convention/boundary | no | no |
| Buss--Holkar--Meyer | no | ordinary Hausdorff transformation groupoids | standard Hausdorff framework | Hausdorff boundary only | generic crossed product | proxy-side only |
| Williams / Green | no | no actual groupoid | ordinary group/crossed-product algebra | no | yes, for `R`/amenable groups | yes, ordinary homogeneous-space proxy |

No row covers the exact conjunction. The apparent proximity results from
combining different owners: arithmetic dynamics from Deninger/Paper 9,
unit-observable collapse from Paper 10, function-space conventions from
Tu/Muhly--Williams, and group/proxy operator theory from Williams/Green.
That synthesis is the only novelty unit supported by this search; the
individual ingredients receive no novelty claim.

## 6. Integrity, acquisition, and bounded conclusion

- **Exact included precedent:** 0.
- **Nearest precedents retained in the ledger:** Deninger Section 11;
  Morishita's current comparison; Paper 9; Paper 10; standard non-Hausdorff
  groupoid frameworks; and Williams/Green group/proxy results.
- **New PDF acquisition:** 0. No search-result PDF was downloaded or retained.
- **Existing full-text use:** only pre-existing audited Deninger and Morishita
  copies were used for the exact arithmetic-owner exclusions; the existing
  Paper-11 framework manifest supplied the standard-source locators.
- **No preflight sidecar was generated:** no new source bytes entered the
  corpus.
- **No phrase-absence generalization:** the two exact-PDF term screens support
  only their corresponding candidate dispositions.

### Permitted conclusion

> As of 2026-08-15, the documented arXiv, Crossref, general-web,
> publisher/DOI/author-record, and inherited-project searches located no
> precedent for the exact conjunction of an actual indiscrete rational-Witt
> orbit transformation groupoid, global continuous quasi-compact-support
> convolution collapse, Hausdorff-open convention split, transported
> `C^*(R)` completions, and strict standard-circle proxy boundary.
> The nearest results divide those components among different objects and
> frameworks. This assessment is **SUPPORTED_WITHIN_SEARCH** only.

This report satisfies the bounded-search documentation requirement only. It
does not establish any `P11-*` theorem, does not certify legal or global
priority, does not by itself authorize Phase 3 or standalone release, and
does not alter any active lock, pipeline state, Route record, or manuscript.

## 7. AI/research-integrity disclosure

The queries, triage, and report drafting were AI-assisted under the ARS deep-
research and source-verification workflow. Endpoint failures, non-exposed hit
counts, inclusion rules, exact candidate dispositions, and wording limits are
reported explicitly. Final scholarly judgment and any future novelty claim
remain the responsibility of the human authors.
