# P69 Stage 2.5 source and search ledger

Audit date: 2026-08-26 (UTC)  
Manuscript: *Orientation-Sensitive Surface-Flat Shifts and Finite-Group Character Data*  
Release state during audit: **HOLD**  
Search cutoff: sources indexed and reachable by 2026-08-26

## 1. Scope and method

This ledger records the reproducible search surface for the Stage 2.5 integrity and
priority audit.  It covers every entry in `references.bib`, every in-text citation
context, the paragraph-overlap sample, and alternate-term searches for each core
claim family.  Queries were issued to a general indexed-web search tool.  Direct
publisher, DOI, arXiv, journal, or author URLs are recorded instead of search-result
URLs.

The reference-verification rule was: search a bibliographic record by exact title,
author, DOI, or identifier; prefer publisher/DOI/arXiv/author-controlled records; and
label a record `NOT_FOUND` only after three materially different queries fail.  All
three records were found exactly, so the three-failure escalation rule was not
invoked.  Search results establish bounded evidence, not global exhaustiveness.

## 2. Phase A — 100% reference verification

### A1. `Klug2025`

Queries:

1. `"Michael R. Klug" "Counting Homomorphisms from Surface Groups to Finite Groups" "10.4153/S0008439524000420"`
2. `site:arxiv.org/abs/2106.11089 "Counting Homomorphisms from Surface Groups to Finite Groups"`
3. `site:cambridge.org/core "Counting Homomorphisms from Surface Groups to Finite Groups" Klug`

Direct evidence:

- Cambridge publisher record: <https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/counting-homomorphisms-from-surface-groups-to-finite-groups/C523AC49DFABB67F60E13A19BBF11F52>
- DOI resolver: <https://doi.org/10.4153/S0008439524000420>
- Publisher PDF: <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/C523AC49DFABB67F60E13A19BBF11F52/S0008439524000420a.pdf/counting-homomorphisms-from-surface-groups-to-finite-groups.pdf>
- arXiv record: <https://arxiv.org/abs/2106.11089>
- Author page: <https://math.uchicago.edu/~michaelklug/>

| BibTeX field | Stored value | Evidence check | Verdict |
|---|---|---|---|
| author | Michael R. Klug | Exact on publisher, arXiv, and author page | VERIFIED |
| title | Counting Homomorphisms from Surface Groups to Finite Groups | Exact on publisher and arXiv | VERIFIED |
| journal | Canadian Mathematical Bulletin | Exact on publisher and arXiv journal reference | VERIFIED |
| volume / issue | 68 / 1 | Exact on publisher | VERIFIED |
| pages | 141–153 | Exact on publisher | VERIFIED |
| year | 2025 | Correct for volume/issue; publisher reports online publication 2024-11-29 | VERIFIED |
| DOI | 10.4153/S0008439524000420 | Resolves to the publisher record | VERIFIED |
| arXiv / class | 2106.11089 / math.GR | Exact on arXiv | VERIFIED |

Record verdict: **VERIFIED**.  Content note: the publisher version numbers the
relevant result as Corollary 1 and the later structural result as Theorem 3.1.  The
paper currently says “following Theorem 3”; that is a minor pinpoint mismatch, not a
formula mismatch.  The nonorientable closed-surface formula used by P69 follows
algebraically from Klug's Corollary 1 after setting the boundary word to the identity.
Klug is a chosen modern normalization source; Klug's own introduction attributes the
classical orientable and nonorientable formulas historically to Mednykh and to
Frobenius–Schur, respectively.

### A2. `CarrollPenland2015`

Queries:

1. `"David Carroll" "Andrew Penland" "Periodic Points on Shifts of Finite Type and Commensurability Invariants of Groups"`
2. `site:nyjm.albany.edu/j/2015/21-36 "Periodic Points on Shifts of Finite Type"`
3. `site:arxiv.org/abs/1502.03195 Carroll Penland`

Direct evidence:

- New York Journal of Mathematics article page: <https://nyjm.albany.edu/j/2015/21-36.html>
- Journal PDF: <https://nyjm.albany.edu/j/2015/21-36v.pdf>
- arXiv record: <https://arxiv.org/abs/1502.03195>

| BibTeX field | Stored value | Evidence check | Verdict |
|---|---|---|---|
| authors | David Carroll; Andrew Penland | Exact on NYJM and arXiv | VERIFIED |
| title | Periodic Points on Shifts of Finite Type and Commensurability Invariants of Groups | Exact | VERIFIED |
| journal | New York Journal of Mathematics | Exact | VERIFIED |
| volume | 21 | Exact | VERIFIED |
| pages | 811–822 | Exact | VERIFIED |
| year | 2015 | Exact | VERIFIED |
| arXiv / class | 1502.03195 / math.GR | Exact on arXiv | VERIFIED |
| URL | NYJM article page | Direct and live | VERIFIED |

Record verdict: **VERIFIED**.

### A3. `CohenGoodmanStrauss2017`

Queries:

1. `"David Bruce Cohen" "Chaim Goodman-Strauss" "Strongly Aperiodic Subshifts on Surface Groups"`
2. `"Strongly Aperiodic Subshifts on Surface Groups" "10.4171/GGD/421"`
3. `site:arxiv.org/abs/1510.06439 "Strongly Aperiodic Subshifts"`

Direct evidence:

- EMS Press publisher record: <https://ems.press/journals/ggd/articles/14944>
- DOI resolver: <https://doi.org/10.4171/GGD/421>
- Publisher full text: <https://ems.press/content/serial-article-files/29842>
- arXiv record: <https://arxiv.org/abs/1510.06439>

| BibTeX field | Stored value | Evidence check | Verdict |
|---|---|---|---|
| authors | David Bruce Cohen; Chaim Goodman-Strauss | Exact on EMS and arXiv | VERIFIED |
| title | Strongly Aperiodic Subshifts on Surface Groups | Exact | VERIFIED |
| journal | Groups, Geometry, and Dynamics | Exact | VERIFIED |
| volume / issue | 11 / 3 | Exact | VERIFIED |
| pages | 1041–1059 | Exact | VERIFIED |
| year | 2017 | Exact | VERIFIED |
| DOI | 10.4171/GGD/421 | Resolves to EMS record | VERIFIED |
| arXiv / primary class | 1510.06439 / math.GR | Exact; math.DS is also listed | VERIFIED |

Record verdict: **VERIFIED**.

### A4. Ghost, dangling, and uncited-record check

Static extraction and compiled-artifact checks gave:

| Surface | Result |
|---|---|
| BibTeX keys in `references.bib` | 3 |
| Distinct keys cited in manuscript | 3 |
| Citation commands/contexts | 5 |
| Keys in `main.aux` citation records | all 3 |
| Keys in `main.aux` bibliography labels | all 3 |
| Undefined citation/reference warnings in `main.log` | none |
| Ghost citations (cited, absent from bibliography) | none |
| Dangling bibliography entries (present, never cited) | none |
| Duplicate keys | none |

Verdict: **PASS**.

## 3. Phase B — 100% citation-context verification

All five citation contexts were checked, exceeding the protocol's 30% floor.

| ID | Manuscript location | Citation and local claim | Source-side evidence | Verdict |
|---|---|---|---|---|
| B01 | `sections/1_introduction.tex:26-28` | Carroll–Penland supplies the general finite-index subgroup / periodic-point setting for group SFTs | NYJM abstract and introduction explicitly relate group subgroups, finite-type shifts, weak/strong periodicity, and commensurability; finite orbit is tied to finite-index stabilizer | VERIFIED |
| B02 | `sections/1_introduction.tex:28-30` | Cohen–Goodman-Strauss shows surface groups support nontrivial finite-type symbolic systems | EMS/arXiv abstract proves a strongly aperiodic SFT for every hyperbolic surface group | VERIFIED |
| B03 | `sections/1_introduction.tex:31-35` | Klug is used as a modern normalization source, not declared the historical owner | Publisher introduction gives the classical attributions and the paper presents a modern treatment | VERIFIED |
| B04 | `sections/2_background.tex:52-58` | Orientable and nonorientable surface-group Hom formulas | Klug Corollary 1 yields the displayed formulas after evaluation at the identity; publisher final uses Theorem 3.1, so “Theorem 3” is an imprecise pinpoint | VERIFIED_WITH_PINPOINT_NOTE |
| B05 | `sections/7_scope_controls.tex:13-20` | Same modern-source / historical-ownership boundary | Consistent with Klug's publisher introduction and Corollary 1 | VERIFIED |

No cited source is made to support P69's new synthesis or inverse theorem.  Conversely,
the cited passages do not contradict their surrounding prose.  Objective correction:
change “Theorem 3” to “Theorem 3.1” in the Klug pinpoint before external release.

## 4. Phase D — paragraph-overlap search

### D1. Census and sample

The normalized manuscript contains 71 narrative paragraph units after excluding
headings, display-only blocks, theorem labels without prose, and table-grid rows.
The audit sampled 22 units, or **30.99%**, and included the abstract plus at least one
paragraph from every numbered major section (Sections 1–8).  Each query is an exact
8–12-word quotation from the manuscript.  “No exact match” means no exact string was
returned by the indexed-web tool; lexical or topic matches were not counted.

| ID | Location | Exact query | Indexed-web result |
|---|---|---|---|
| D01 | `sections/0_abstract.tex:15-16` | `"Finite moment inversion shows that the two spectra jointly determine"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D02 | `sections/1_introduction.tex:4-9` | `"This makes the topology of the corresponding finite covers available"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D03 | `sections/1_introduction.tex:33-35` | `"Those formulas are cited inputs, not contributions of this paper"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D04 | `sections/1_introduction.tex:97-103` | `"The inverse step is a finite exponential-moment problem"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D05 | `sections/2_background.tex:22-27` | `"This criterion will be important because it is the same"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D06 | `sections/2_background.tex:75-80` | `"Convolution of the corresponding class functions diagonalizes in irreducible characters"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D07 | `sections/3_flat_shift.tex:36-46` | `"There are finitely many forbidden patterns on this set"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D08 | `sections/3_flat_shift.tex:90-94` | `"Every connection has a unique based gauge transform whose labels"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D09 | `sections/3_flat_shift.tex:114-119` | `"The full gauge group can have stabilizers governed by centralizers"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D10 | `sections/4_subgroup_counts.tex:7-10` | `"We retain all positive moduli because both parities of the"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D11 | `sections/4_subgroup_counts.tex:44-46` | `"This prevents the orientation comparison from being hidden in unrelated"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D12 | `sections/5_moment_recovery.tex:27-30` | `"The reduced rational function on the right has simple poles"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D13 | `sections/5_moment_recovery.tex:83-86` | `"Distinct degrees give distinct nonzero bases and every coefficient"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D14 | `sections/5_moment_recovery.tex:32-37` | `"When the bases are known, moments with nonnegative indices"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D15 | `sections/5_moment_recovery.tex:164-167` | `"The orientable moments alone cannot distinguish characters of equal degree"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D16 | `sections/6_dihedral_quaternion.tex:17-18` | `"The two-dimensional indicators have opposite signs. This can be checked"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D17 | `sections/6_dihedral_quaternion.tex:69-76` | `"separation holds at every odd level, not only at the first one"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D18 | `sections/7_scope_controls.tex:6-11` | `"The theorem does not assert that this signature determines the"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D19 | `sections/7_scope_controls.tex:79-82` | `"This finite enumeration can detect normalization or parity regressions"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D20 | `sections/7_scope_controls.tex:86-90` | `"That negative search is not a priority result"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D21 | `sections/8_conclusion.tex:4-11` | `"The flat-connection SFT converts finite-index fixed points into raw flat"` | NO_EXACT_MATCH_IN_INDEXED_WEB |
| D22 | `sections/8_conclusion.tex:13-18` | `"Several boundaries are deliberate. The recovered signature is not a"` | NO_EXACT_MATCH_IN_INDEXED_WEB |

Phase D1 verdict: **PASS_WITH_TOOL_LIMITATIONS**.  This is an overlap screen, not an
originality or plagiarism certificate.

### D2. Author-overlap search

`NOT_RUN_AUTHOR_IDENTITIES_UNAVAILABLE`

Anonymous authorship prevents an author-name / prior-work overlap search.  This must
be rerun after the author list is authorized and before external release.

### D3. Tool limitations

The search surface was a general indexed web, not Turnitin, iThenticate, Crossref
Similarity Check, a subscription full-text corpus, or a complete historical archive.
Exact-phrase search can miss paywalled or unindexed documents, OCR failures, TeX/math
normalization, translations, paraphrases, and sources published under different
terminology.  A no-match result therefore means only “not found within this bounded
search.”

## 5. Alternate-term novelty and ownership search

### N1. Lattice gauge / configuration shifts / flat connections

Queries:

1. `"flat connections" "subshift of finite type" finite group`
2. `"lattice gauge theory" "symbolic dynamics" "subshift of finite type"`
3. `"configuration space" flat finite-group connections shift periodic points`
4. `"finite gauge group" subshift flat connections`

Results and nearest neighbors:

- Noah Snyder, *Mednykh's Formula via Lattice Topological Quantum Field Theories*:
  <https://arxiv.org/abs/math/0703073>.  This is a close owner of the lattice/TQFT
  route from surface topology to the Mednykh and Frobenius–Schur counts, but it is not
  a surface-group SFT periodic-spectrum inverse theorem.
- Vladimir Turaev, *Dijkgraaf–Witten invariants of surfaces and projective
  representations of groups*: <https://arxiv.org/abs/0706.0160> and
  <https://doi.org/10.1016/j.geomphys.2007.08.009>.  This is a close finite-gauge /
  edge-label state-sum neighbor, including a nonorientable discussion, but not the
  stated configuration-shift recovery construction.
- Pierre Béaur and Jarkko Kari, *Effective Projections on Group Shifts to Decide
  Properties of Group Cellular Automata*: <https://arxiv.org/abs/2301.11133>.  This
  concerns algebraic group shifts over `Z^d` and cellular-automaton decision problems,
  not flat connections on a surface group.

Outcome: no exact collision found; **medium collision risk** because the finite-gauge
and lattice-state-sum ingredients are established.  P69 must subtract Snyder/Turaev
rather than frame the lattice/flat-connection bridge alone as new.

### N2. Surface-group SFTs / group shifts / finite-index periodicity

Queries:

1. `"surface group" "subshift of finite type" periodic points`
2. `"group shifts" finite-index subgroups periodic points "surface group"`
3. `"surface groups" symbolic dynamics finite type configurations`
4. `"surface group" shift "fixed points" finite-index subgroup`

Results and nearest neighbors:

- Cohen–Goodman-Strauss: <https://ems.press/journals/ggd/articles/14944> and
  <https://arxiv.org/abs/1510.06439>.  Owns strongly aperiodic SFT existence on
  hyperbolic surface groups; it does not give P69's flat-connection fixed-count laws.
- Carroll–Penland: <https://nyjm.albany.edu/j/2015/21-36.html> and
  <https://arxiv.org/abs/1502.03195>.  Owns the general group-SFT / finite-index
  periodicity and commensurability context; it does not recover character indicators.
- Lewis Bowen, *Free Groups in Lattices*: <https://arxiv.org/abs/0802.0185>.  The
  surrounding work discusses surface-group SFT periodic-point phenomena, but not the
  explicit P69 invariant-recovery mechanism.

Outcome: the “surface-group SFT” frame is established prior art.  The residual
candidate is the exact flat-holonomy SFT plus two cover families and joint inverse
statement, not surface symbolic dynamics in isolation.

### N3. Mednykh / Frobenius–Schur surface Hom formulas

Queries:

1. `"Mednykh formula" homomorphisms surface group finite group`
2. `"Frobenius-Schur" nonorientable surface homomorphisms finite group formula`
3. `"counting homomorphisms" surface groups finite groups character degrees indicators`
4. `"Mednykh's formula via lattice" topological quantum field theories`

Results and owners:

- Klug modern account: <https://doi.org/10.4153/S0008439524000420> and
  <https://arxiv.org/abs/2106.11089>.
- Snyder lattice-TQFT proof: <https://arxiv.org/abs/math/0703073>.
- Motohico Mulase and Josephine T. Yu, *A generating function of the number of
  homomorphisms from a surface group into a finite group*:
  <https://arxiv.org/abs/math/0209008>.  It explicitly describes new proofs of the
  classical Frobenius, Schur, and Mednykh formulas.
- Turaev surface Dijkgraaf–Witten account:
  <https://doi.org/10.1016/j.geomphys.2007.08.009>.

Outcome: these formulas are classical inputs.  Klug is the selected modern
normalization source, not the original owner.  P69's theorem-sized mass cannot include
the formulas themselves.

### N4. Orientation-sensitive cover spectra

Queries:

1. `"orientable" "nonorientable" cover periodic spectra group shift`
2. `"orientation-sensitive" periodic points surface group subshift`
3. `"finite-index" surface covers "fixed point counts" subshift`
4. `"orientable covers" "nonorientable covers" symbolic dynamics`

Results and neighbors:

- Turaev's surface state sums distinguish orientability through representation data:
  <https://doi.org/10.1016/j.geomphys.2007.08.009>.
- *Counting the regular coverings of surfaces using the center of a group algebra*
  treats orientable/nonorientable surface-cover enumeration:
  <https://doi.org/10.1016/j.ejc.2004.09.001>.
- Carroll–Penland supplies the periodic/fixed-subgroup setting:
  <https://nyjm.albany.edu/j/2015/21-36.html>.

Outcome: no source located the exact pair of divisibility-directed P69 cover families
and their joint fixed-point inverse signature.  The topology, covering enumeration,
and general periodicity components have prior owners, so this is only a
`NOT_FOUND_WITHIN_BOUNDED_SEARCH` result.

### N5. Character-degree / Frobenius–Schur-indicator moment recovery

Queries:

1. `"Frobenius-Schur indicator" "moment problem" character degrees`
2. `"character degree" Frobenius-Schur indicators recover finite group spectra`
3. `Vandermonde character degrees Frobenius-Schur indicator finite group`
4. `"degree-indicator" multiset finite group Frobenius Schur`
5. `finite group representation zeta function determines character degrees moment sequence`
6. `inverse moments irreducible character degrees finite groups zeta function`
7. `"Frobenius-Schur indicators" surface partition functions recover`
8. `D8 Q8 surface homomorphism counts Frobenius Schur indicator`

Results and nearest neighbors:

- Martin W. Liebeck and Aner Shalev define the finite-group character-degree zeta
  function `sum chi(1)^(-t)` in *Character degrees and random walks in finite groups
  of Lie type*: <https://doi.org/10.1112/S0024611504014935> and the
  <https://www.cambridge.org/core/journals/proceedings-of-the-london-mathematical-society/article/abs/character-degrees-and-random-walks-in-finite-groups-of-lie-type/971082D1033B8B0372ECA3FDEE82F5ED>
  publisher record.  Thus inverse-degree power sums are a standard representation-zeta
  object, though this source does not perform P69's signed indicator reconstruction.
- Klug, Snyder, Mulase–Yu, and Turaev provide the surface-count sequences from which
  such moments arise; direct URLs are listed above.
- The opposite two-dimensional Frobenius–Schur types for `D8` and `Q8` are standard
  representation-theoretic data.  In P69 they function as a separation control, not
  as an independent novelty claim.

Outcome: no exact joint recovery theorem for the multiset
`(degree, Frobenius–Schur indicator)` was located.  The finite Vandermonde inversion
itself is elementary and should not be isolated as a priority claim.  A
representation-zeta citation should be added before release to make the owner
subtraction explicit.

### N6. Exact-combination collision queries

Queries:

1. `"flat-connection SFT" surface group`
2. `"orientation-sensitive recovery" Frobenius Schur periodic`
3. `"fixed-point counts" "Frobenius-Schur indicators" subshift`
4. `"character-degree" indicator "periodic spectra" finite group`

Result: **NOT_FOUND_WITHIN_BOUNDED_SEARCH**.  Returned items were either lexical false
positives or one of the component literatures above.  This is not a worldwide priority
certificate and must not be represented as one.

## 6. Owner subtraction and collision-risk record

| Component | Prior owner / nearest literature | What remains potentially P69-specific |
|---|---|---|
| Surface Hom counts | Mednykh and Frobenius–Schur historically; Klug modern normalization; Snyder/Mulase–Yu/Turaev alternative proofs | Not a P69 contribution |
| Lattice/finite-gauge surface formulation | Snyder and Turaev | Not the flat/gauge bridge by itself |
| Group-SFT finite-index periodicity | Carroll–Penland | Not the subgroup-periodicity framework itself |
| Surface-group SFTs | Cohen–Goodman-Strauss and surrounding surface symbolic dynamics | Not the existence of a surface-group SFT |
| Inverse-degree moments | representation-zeta literature, e.g. Liebeck–Shalev | Not the use of inverse character-degree sums alone |
| Finite moment inversion | elementary Vandermonde/rational-function algebra | Not a standalone novelty claim |
| `D8`/`Q8` FS separation | standard character theory | A proof-regression example only |
| Residual synthesis | exact `N_3` edge-holonomy SFT, explicit orientable/nonorientable divisibility-directed cover families, raw fixed-count identity, and joint recovery of order plus the degree/indicator multiset | Candidate theorem-sized contribution, subject to broader specialist search |

Collision-risk assessment: **MEDIUM**.  The exact synthesis was not found, but every
major ingredient is close to established work and the indexed-web search is not
complete.  Required wording is search-bounded: “no exact collision found in the
recorded queries through 2026-08-26.”  Global priority, specialist clearance, and
publication novelty remain unresolved.

## 7. Ledger disposition

- Existing bibliography metadata: **3/3 VERIFIED; no field mismatch**.
- Citation-context fidelity: **PASS_WITH_ONE_PINPOINT_NOTE**.
- Ghost/dangling citations: **PASS**.
- Paragraph-overlap screen: **PASS_WITH_TOOL_LIMITATIONS**.
- Novelty/priority search: **SEARCH-BOUNDED; MEDIUM COLLISION RISK**.
- Needed before external release: correct Klug “Theorem 3” to “Theorem 3.1”; add and
  discuss Snyder as a lattice-TQFT neighbor; add a representation-zeta source for the
  inverse-degree-moment context; rerun D2 after author identities are authorized.
- External release state: **HOLD**.

