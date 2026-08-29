# Batch Round 9 — Stage 2.5 cross-paper self-overlap audit

Audit date: 2026-08-29 (UTC)  
Mode: ARS-Codex Stage 2.5, Phase D supplementary author-corpus screen  
Author identity searched: Liang Wang; `wangliang.f@gmail.com`; ORCID `0000-0001-9006-6924`  
Local corpus: Papers 24--28, frozen Round-9 manuscripts  

## Determination

**PASS WITH NOTES for the self-overlap question only.** Across all ten local
paper pairs, no exact run of eight or more words of substantive body prose was
found.  The only local exact runs at that threshold are a controlled Route-A
status taxonomy.  Full-file comparison additionally finds repeated funding,
conflict, ethics, CRediT, data-availability, and AI-assistance language; these
are classified as **legitimate standardized administrative boilerplate**, not
scientific-text reuse.  A full-text comparison against the 22 publicly
available PDFs in the author's ORCID-bound Zenodo corpus found no substantive
eight-word match.  Three Zenodo PDFs shared only bare axis/index sequences such
as `1 2 3 4 5 6 7 8`, which are numerical table matter rather than prose.

**Potentially undisclosed recycled substantive prose: NOT DETECTED in the
bounded corpus.** This is a provisional screening determination, not a
professional similarity certificate.  It does not cure any paper-specific
Stage 2.5 failure.  In particular, Paper 28 remains separately blocked by two
BibTeX metadata mismatches and the missing post-#260 experiment-intake
declaration recorded in its independent audit.

Stable provisional findings:

| ID | Severity | Determination |
|---|---|---|
| `R9-SO-CLEAR-1` | CLEAR | Exhaustive normalized eight-word comparison of 10/10 local body pairs found zero substantive-prose runs. |
| `R9-SO-CLEAR-2` | CLEAR | The only exact local mathematical overlap is the project-controlled Route-A status tuple/taxonomy; it is not claimed as new prose. |
| `R9-SO-MINOR-1` | MINOR / non-blocking | P24--P25 and P26--P27 contain long exact declaration blocks (maxima 98 and 100 normalized words). They are administrative boilerplate, clearly outside the scientific body. |
| `R9-SO-CLEAR-3` | CLEAR | 22/22 ORCID-bound Zenodo PDFs and two older official arXiv PDFs produced no substantive exact eight-word body match with P24--P28. |
| `R9-SO-CLEAR-4` | CLEAR | Exact-title searches for all five manuscripts found no exact public publication surface. |
| `R9-SO-LIMIT-1` | LIMITATION | Web indexing and PDF extraction cannot cover private, paywalled, unindexed, or differently rendered text; professional duplicate checking remains required before submission. |

There is no gray-zone pass in this report: every detected overlap is assigned
to one of three explicit classes--administrative template, controlled
formula/taxonomy, or bare numerical sequence--and the residual category of
potential undisclosed substantive reuse is empty.

## Local corpus and denominator

The scientific-body boundary is `Introduction` through the last numbered
section before declarations.  Comments, TeX commands, punctuation, and case
were normalized; the screen then exhaustively intersected contiguous word
ngrams.  Displayed mathematics was normalized and compared separately.  The
body denominator is **24,396 normalized words across five manuscripts and all
10/10 unordered paper pairs**.

| Paper | Short title | Manuscript SHA-256 | Normalized body words |
|---|---|---|---:|
| P24 | Bianchi holonomy / first-jet separation | `e43ba0f77332b79df4d84346dcb6e3041c20f4bdded5a91f42caac348ea9fd11` | 4,557 |
| P25 | Three-disk unit-roof non-transfer | `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb` | 4,681 |
| P26 | Level-11 newform-period taxonomy | `00a21246f496b12f98389522d762ad6c4e10683e0eb21163b881d7b035f9c2fe` | 4,742 |
| P27 | Congruence/homology tower obstruction | `c2809011a722b81732952d889f194549adea58875b605dbafe58ada93de9b4b9` | 4,537 |
| P28 | Exact genus-two octagon systole certificate | `864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7` | 5,879 |

## Exhaustive local body comparison (10/10 pairs)

`<8` means that the pair shares no exact normalized run at the eight-word
screening threshold.  A reported maximum does not by itself imply prose reuse;
each positive was inspected in its TeX context.

| Pair | Maximum exact run | Context | Final class |
|---|---:|---|---|
| P24--P25 | `<8` | none | no detected overlap |
| P24--P26 | 13 words | `a 1 weak a 2 fail a 3 fail a 4 fail with` inside Route-A assessment | controlled taxonomy |
| P24--P27 | 10 words | Route-A layer/status sequence | controlled taxonomy |
| P24--P28 | 12 words | Route-A layer/status sequence | controlled taxonomy |
| P25--P26 | `<8` | none | no detected overlap |
| P25--P27 | `<8` | none | no detected overlap |
| P25--P28 | `<8` | none | no detected overlap |
| P26--P27 | 10 words | Route-A layer/status sequence | controlled taxonomy |
| P26--P28 | 15 words | normalized tuple `(A0_WEAK_ARITHMETIC_RELATION,A1_WEAK,A2_FAIL,A3_FAIL,A4_FAIL)` | exact shared formula / controlled taxonomy |
| P27--P28 | 9 words | Route-A layer/status sequence | controlled taxonomy |

Scientific-prose result: **0 substantive exact runs of at least eight words in
10/10 pairs**.  The P26--P28 tuple is the only identical normalized displayed
formula across the corpus.  It is an explicit project-wide status vocabulary,
not a theorem, derivation, datum, or source-specific result.

## Declaration and common-method separation

The full manuscripts were compared a second time so that exclusion of the
declarations from the scientific body could not conceal repeated text.

| Surface | Exact-overlap observation | Classification |
|---|---|---|
| P24--P25 declarations | maximum 98-word normalized run spanning standard funding, conflict, contributions, ethics, and AI-disclosure language | legitimate standardized administrative boilerplate; `R9-SO-MINOR-1` |
| P26--P27 declarations | maximum 100-word normalized run spanning ethics, contributions, conflict, funding, and AI disclosure | legitimate standardized administrative boilerplate; `R9-SO-MINOR-1` |
| P24/P25--P28 declarations | 23-word contribution-role sequence and short ethics phrases | standardized CRediT/ethics vocabulary |
| Other declaration pairs | contribution-role sequences up to 16 words | standardized CRediT vocabulary |
| Route-A tuple | exact P26--P28 formula and shorter cross-pair status sequences | controlled project taxonomy, explicitly labeled in every manuscript |
| Reproducibility language | shared concepts--deterministic Python, source locks, hashes, tests, owner boundaries--but no exact eight-word substantive run | common method, independently worded |
| Domain vocabulary | geodesic flow, primitive owner, determinant, control, and claim-boundary terms | common technical language |

The declaration repetition is non-blocking because it is visibly segregated,
contains no scientific finding, and uses conventional roles and compliance
statements.  A journal-specific template may replace it later without changing
the self-overlap result.

## Paraphrase-oriented paragraph check

Exact matching was supplemented by TF--IDF paragraph comparison.  The highest
cross-paper scores were inspected rather than automatically passed.

| Pair and locators | Cosine score | Shared idea | Determination |
|---|---:|---|---|
| P24 L392 / P25 L385 | 0.361 | an operator/spectral omission boundary | common project claim-boundary method; no eight-word run |
| P24 L358 / P25 L350 | 0.234 | repository/replay inventory | common reproducibility method; no eight-word run |
| P24 L400 / P25 L391 | 0.169 | evidence that would change the verdict | common falsification structure; no eight-word run |
| P24 L90 / P27 L102 | 0.200 | standard unit-speed geodesic-flow setting | common domain definition; no eight-word run |
| P26 L438 / P27 L72 | 0.177 | Route-A layer/status interpretation | controlled taxonomy; no unlabelled prose reuse |
| P26 L411 / P27 L383 | 0.144 | deterministic Python/hash certificate | common method; no eight-word run |

None of these pairs preserves a distinctive result, derivation, example, or
expository sequence.  Therefore none is classified as disguised recycling.

## Author-identity and public-surface search

The homonym risk was controlled by searching the exact email and then the
publisher-confirmed ORCID.  Exact queries included:

- `"wangliang.f@gmail.com"`
- `"Liang Wang" "School of Artificial Intelligence and Automation" "Huazhong University of Science and Technology"`
- `"Liang Wang" "Luoyu Road 1037" mathematics`
- `"0000-0001-9006-6924"`
- each exact P24--P28 title in quotation marks

Identity anchors include the publisher page for [The emergence of prime
distribution from low-dimensional deterministic chaos](https://www.tandfonline.com/doi/full/10.1080/27684830.2026.2684334),
which gives the same email, HUST affiliation, and ORCID; the official arXiv
record for [Describe Prime number gaps pattern by Logistic
mapping](https://arxiv.org/abs/1306.3626); the official publisher page for
[Translate gene sequence into gene ontology terms based on statistical
machine translation](https://f1000research.com/articles/2-231/v1); and the
publisher PDF for [How to Build a DNA Search Engine like
Google?](https://www.hilarispublisher.com/open-access/how-to-build-a-dna-search-engine-like-google-jcsb.1000081.pdf).
The biological/NLP records confirm identity but are thematically distinct.

The mathematically adjacent surfaces were not assumed to be unrelated.  The
screen used the official Zenodo API query
`creators.orcid:0000-0001-9006-6924`, retrieved 22/22 public records as of the
audit date, extracted one public PDF from every record, and compared each
full text with all five local scientific bodies.

### ORCID-bound Zenodo full-text denominator (22/22 PDFs)

| Record | Public title | Exact P24--P28 eight-word result |
|---|---|---|
| [21720147](https://zenodo.org/records/21720147) | Boundary-Aligned Ulam Approximation and Grid Leakage in a Cyclic Postcritically Finite Quadratic Map | none |
| [21712436](https://zenodo.org/records/21712436) | Periodic-Orbit Collapse in B-Admissible Shifts | none |
| [20711935](https://zenodo.org/records/20711935) | A Sequential Birkhoff Theorem for Slow Logarithmic Drift | none |
| [20565112](https://zenodo.org/records/20565112) | The Emergence of Prime Distribution from Low-Dimensional Deterministic Chaos | none |
| [20463341](https://zenodo.org/records/20463341) | Transient Chaos and Topological Bounds in Prime Dynamics | P28 only: four overlapping numeric windows inside `1 2 ... 11`; no prose |
| [19995437](https://zenodo.org/records/19995437) | Unitarity Enables Grokking | P28 only: five overlapping numeric windows inside `0 1 ... 11`; no prose |
| [19682685](https://zenodo.org/records/19682685) | Differentiable Discrete Symplectic Cosmology | P28 only: four overlapping numeric windows inside `1 2 ... 11`; no prose |
| [19677694](https://zenodo.org/records/19677694) | Spectral Analysis of the Transfer Operator in the Period-3 Logistic Sandbox | none |
| [19657875](https://zenodo.org/records/19657875) | An Empirical Logarithmic Relation Between Gravitational and Electromagnetic Coupling Constants | none |
| [19455383](https://zenodo.org/records/19455383) | Physical Emergence of Riemann Zeros in Dissipative Chaotic Circuits | none |
| [19429778](https://zenodo.org/records/19429778) | Discrete Symplectic Cosmology | none |
| [19218674](https://zenodo.org/records/19218674) | Cosmological Evolution as a Non-autonomous Dynamical System | none |
| [19135531](https://zenodo.org/records/19135531) | Ab Initio Quantum Emulation of the Riemann Zeros | none |
| [19084735](https://zenodo.org/records/19084735) | The Physical Topology of Riemann Zeros | none |
| [19045440](https://zenodo.org/records/19045440) | Spectral Isomorphism between Renormalization Flow and Riemann Zeros | none |
| [18596290](https://zenodo.org/records/18596290) | The Riemann Standard Model | none |
| [18535934](https://zenodo.org/records/18535934) | Riemann Zero Truncation in Physical Systems | none |
| [18493585](https://zenodo.org/records/18493585) | The Relaxation of Cosmic Expansion | none |
| [18459475](https://zenodo.org/records/18459475) | Cosmological Evolution as a Non-autonomous Chaotic System | none |
| [17926196](https://zenodo.org/records/17926196) | OpenSciEval | none |
| [17926116](https://zenodo.org/records/17926116) | OpenSciEval Scientific Creativity Evaluation Guide | none |
| [17832139](https://zenodo.org/records/17832139) | Humanity's Final Conjecture | none |

Result: 19 PDFs have zero exact eight-word matches; three have only bare
numeric-sequence matches.  The journal article in the 20565112 deposit and
the directly Hilbert--Pólya-oriented Zenodo papers therefore do not contain
detectable recycled P24--P28 body prose at the chosen threshold.

Two older official arXiv PDFs were additionally screened in full:
[arXiv:1306.3626](https://arxiv.org/abs/1306.3626) and
[arXiv:1006.4114](https://arxiv.org/abs/1006.4114).  Each produced **0 exact
eight-word matches for each of P24, P25, P26, P27, and P28**.

Exact-title searches returned no exact publication surface for any of P24--P28.
General quoted-fragment searching used 40 fragments: 28/72 P28 paragraphs
(recorded individually in the P28 audit) plus three distinctive conclusion
fragments from each of P24--P27 (12 additional fragments).  No exact external
source match was found.  The 12 additional recorded fragments were:

| Paper | Recorded quoted fragments |
|---|---|
| P24 | `Normalized trace divisibility at Gaussian level three is exact but universal`; `The first jet has clean owner-compatible laws and improves finite separation`; `The next meaningful step is a source-derived ideal-valued refinement` |
| P25 | `An exact symbolic determinant does not become a physical-flow determinant`; `period-two and period-three mean flight lengths differ`; `The next viable physical step is a genuinely nonconstant-roof operator` |
| P26 | `The level-11 newform time change has a clean arithmetic period coordinate`; `Exact Schreier homology turns this failure into a complete finite theorem`; `The resulting paper-level contribution is an exact taxonomy and non-implication theorem` |
| P27 | `Residual towers erase same-owner periodicity in two compatible senses`; `The four-quadrant theorem isolates those two costs exactly`; `Because the recovered identity is finite-panel and generic` |

## Seven AI-research failure modes — batch overlay

This table evaluates the overlap-screen execution.  Paper-specific citation
and experiment-disclosure findings retain their own verdicts.

| Mode | Status | Evidence |
|---|---|---|
| 1. Implementation bug passing self-review | **CLEAR** | Local pairwise results were checked by maximal-run and eight-gram views; web PDFs were extracted individually and denominators reconcile (10 pairs, 22 Zenodo PDFs, two arXiv PDFs). |
| 2. Hallucinated citation | **SUSPECTED at aggregate Stage 2.5, not caused by overlap** | Public author surfaces resolve, but Paper 28 independently has two serious BibTeX metadata mismatches. This keeps the aggregate gate blocked. |
| 3. Hallucinated experimental result | **CLEAR for this screen** | Counts and examples are direct outputs of the frozen local texts and official public PDFs; no scientific result is inferred from similarity scores. |
| 4. Shortcut reliance | **CLEAR** | The local comparison is exhaustive at the declared threshold; exact, formula, declaration, semantic-paragraph, exact-title, author-identity, and public-full-text surfaces were all inspected. |
| 5. Bug reframed as novel insight | **CLEAR** | Numeric-sequence hits and template blocks were explicitly downgraded rather than presented as substantive discoveries. |
| 6. Methodology fabrication | **CLEAR for overlap method** | The report states normalization, denominators, thresholds, official corpus, exceptions, and limitations. Paper 28's missing experiment-intake declaration remains a separate structural failure. |
| 7. Early frame-lock | **CLEAR** | The screen tested both expected boilerplate and adverse same-author mathematical corpora, including directly related Hilbert--Pólya/prime-dynamics surfaces found after the initial email search. |

Mode 2 remains SUSPECTED at the aggregate level because of Paper 28, even
though the self-overlap-specific verdict is PASS WITH NOTES.

## Phase D limitation disclaimer

> This originality verification uses WebSearch for heuristic comparison and
> is not professional plagiarism detection software (such as Turnitin /
> iThenticate). Coverage is limited to publicly searchable literature. The
> local P24--P28 exact eight-word comparison was exhaustive across all ten
> pairs; the author-corpus full-text comparison covered 22/22 ORCID-bound
> Zenodo PDFs and two older arXiv PDFs; general-web checking used 40 quoted
> fragments. Private, paywalled, unindexed, image-only, and differently
> rendered sources may be missed. These results serve as preliminary
> screening; it is recommended to use professional plagiarism detection tools
> for complete duplicate checking before formal submission.

## Handoff

No substantive prose correction is required on the evidence found here.
Before submission, retain the existing AI-assistance declarations, apply the
target journal's own declaration template if it differs, and run a professional
similarity report over the final PDFs.  If a later revision imports text,
figures, data, or conclusions from an earlier Liang Wang publication, that
material must be re-screened and the related work cited explicitly.
