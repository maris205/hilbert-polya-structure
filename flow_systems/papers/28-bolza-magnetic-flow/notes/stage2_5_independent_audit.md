# Paper 28 — independent Stage 2.5 integrity audit

Audit date: 2026-08-29 (UTC)  
Mode: ARS-Codex Stage 2.5, Mode 1 pre-review, read-only independent pass  
Audited draft: `paper/manuscript.tex`, SHA-256 `864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7`  
Audited bibliography: `paper/references.bib`, SHA-256 `42474f492f261e97883f7b8e0577fc7a42ce58db7e084f456d92045b5788d284`  

## Verdict

**FAIL — three blocking correction items.** The mathematical/numerical claim surfaces checked in this pass are supported, all nine citation contexts are faithful, and the originality sample is clean. The gate nevertheless cannot pass because two BibTeX records have author/subject metadata mismatches and the package has no post-#260 ARS experiment-intake declaration/provenance block.

Stable provisional findings:

| ID | Severity | Surface | Determination | Required correction |
|---|---|---|---|---|
| `P28-IL-SERIOUS-1` | SERIOUS | `Nazarenko2013` in `references.bib` | **MISMATCH**: the official record gives author `A. V. Nazarenko` (submission name `Andrey Nazarenko`) and subject `math-ph`; the entry expands the name as `Aleksandr V.` and says `primaryclass = hep-th`. | Use the source-safe author form `Nazarenko, A. V.` and `primaryclass = {math-ph}`. |
| `P28-IL-SERIOUS-2` | SERIOUS | `AigonDupuyEtAl2005` in `references.bib` | **MISMATCH**: three given names are wrong. Official DOI metadata gives Aline Aigon-Dupuy, Peter Buser, Michel Cibils, Alfred F. Künzle, Frank Steiner; the entry says Annick, Maria, and Andreas F. | Replace the author field with the five official names. |
| `P28-IL-MEDIUM-1` | MEDIUM / structural blocker | Phase C4 experiment disclosure | No Material Passport, `experiment_intake_declaration`, or `experiment_provenance[]` was found for Paper 28, although the manuscript reports an author-run finite enumeration and replay. Under the post-#260 fail-closed rule, absence is a structural **FAIL**. | Add a schema-valid declaration with `status: experiments_declared` and provenance entries binding the Round-8 builder, tests, source locks, results, negative results, and known limitations. |

No manuscript or artifact was edited in this audit.

## Coverage summary

| Phase | Population | Audited | Result |
|---|---:|---:|---|
| A — reference existence/metadata | 6 BibTeX entries | 6/6 (100%) | 4 VERIFIED; 2 MISMATCH |
| A3 — ghost citations | 6 entries; 9 citation contexts | 6/6 and 9/9 | no orphan or dangling citation |
| B — citation context | 9 contexts | 9/9 (100%; minimum was 30%) | 9 faithful contexts |
| C — numerical/data surfaces | 10 registered surface families | 10/10 (100%) | internally consistent and artifact-backed |
| C4 — experiment provenance | 1 computational evidence package expected | 0 declaration/provenance packages | structural FAIL |
| D — body-paragraph originality | 72 prose paragraphs | 28/72 (38.9%; minimum was 30%) | 26 ORIGINAL; 2 COMMON_KNOWLEDGE; 0 close/verbatim |
| E — stable claim registry | 85 claims: 78 HIGH-IMPACT, 3 RANDOM, 4 NOT-SELECTED | 81/81 selected claims; 84 evidence tuples | contract PASS; 84 tuple verdicts VERIFIED, with anchorless-excerpt limitation |
| AI-research failure modes | 7 modes | 7/7 | Mode 2 SUSPECTED; other six CLEAR |

## Phase A — six-reference audit

Every row below records the exact query used, an authoritative primary/official locator, and a field-by-field result. `MISMATCH` is not softened to an uncertain or partial pass.

### A1. `Nazarenko2013` — MISMATCH

- Exact query: `"Two-Parametric Hyperbolic Octagons and Reduced Teichmüller Space in Genus Two" Nazarenko 2013 arXiv 1301.5446`
- Official record: <https://arxiv.org/abs/1301.5446v1>; DOI/DataCite: <https://doi.org/10.48550/arXiv.1301.5446>
- Field results: author **MISMATCH** (`A. V. Nazarenko`; arXiv submission history says `Andrey Nazarenko`, not `Aleksandr V.`); title VERIFIED; year VERIFIED (2013); eprint VERIFIED (`1301.5446`); archive prefix VERIFIED; primary class **MISMATCH** (official `math-ph`, entry `hep-th`); DOI VERIFIED; URL VERIFIED.
- Official content also confirms submission on 23 January 2013, 12 pages, four figures, and the genus-two two-parameter octagon abstract.
- Finding: `P28-IL-SERIOUS-1`.

### A2. `Takeuchi1975` — VERIFIED

- Exact query: `"A Characterization of Arithmetic Fuchsian Groups" Kisao Takeuchi 1975 DOI 10.2969/jmsj/02740600`
- Official record: <https://www.jstage.jst.go.jp/article/jmath1948/27/4/27_4_600/_article>
- Field results: author VERIFIED (Kisao Takeuchi); title VERIFIED; journal VERIFIED; volume VERIFIED (27); issue VERIFIED (4); pages VERIFIED (600–612); year VERIFIED (1975); DOI VERIFIED; URL VERIFIED.
- The official page records a 2006 correction to the formatting/numbering of the article's own reference list; it does not change this article's metadata or Theorem 1.

### A3. `AigonDupuyEtAl2005` — MISMATCH

- Exact query: `"Hyperbolic Octagons and Teichmüller Space in Genus 2" 10.1063/1.1850177`
- Official DOI: <https://doi.org/10.1063/1.1850177>; DOI-deposit metadata: <https://api.crossref.org/works/10.1063%2F1.1850177>; institutional record: <https://infoscience.epfl.ch/entities/publication/eb38a039-e625-41a3-a9a6-4fb5a81f7d7d>
- Field results: author **MISMATCH** (official: Aline Aigon-Dupuy; Peter Buser; Michel Cibils; Alfred F. Künzle; Frank Steiner; entry: Annick, Peter, Maria, Andreas F., Frank); title VERIFIED; journal VERIFIED; volume VERIFIED (46); issue VERIFIED (3); article number VERIFIED (`033513`); year VERIFIED (2005); DOI VERIFIED; URL VERIFIED.
- Finding: `P28-IL-SERIOUS-2`.

### A4. `Voight2009` — VERIFIED

- Exact query: `"Computing Fundamental Domains for Fuchsian Groups" John Voight 2009 10.5802/jtnb.683`
- Official record: <https://jtnb.centre-mersenne.org/articles/10.5802/jtnb.683/>; official PDF: <https://jtnb.centre-mersenne.org/item/10.5802/jtnb.683.pdf>
- Field results: author VERIFIED; title VERIFIED; journal VERIFIED; volume VERIFIED (21); issue VERIFIED (2); pages VERIFIED (467–489); year VERIFIED (2009); DOI VERIFIED; URL VERIFIED.

### A5. `DespreEtAl2023` — VERIFIED

- Exact query: `site:drops.dagstuhl.de "Computing a Dirichlet Domain for a Hyperbolic Surface" Despré Kolbe Parlier Teillaud 2023`
- Official record and supplied BibTeX: <https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.SoCG.2023.27>
- Field results: all four authors VERIFIED; title VERIFIED; booktitle VERIFIED; series VERIFIED; volume VERIFIED (258); pages VERIFIED (27:1–27:15); year VERIFIED (2023); publisher VERIFIED; DOI VERIFIED; URL VERIFIED.

### A6. `Popescu2024` — VERIFIED

- Exact query: `site:link.springer.com/chapter/10.1007/978-3-031-51959-8_16 "A Simple and Self-Contained Proof" Popescu`
- Official book/TOC: <https://link.springer.com/book/10.1007/978-3-031-51959-8>; official chapter DOI: <https://doi.org/10.1007/978-3-031-51959-8_16>; author version: <https://arxiv.org/abs/2306.14352>
- Field results: author VERIFIED; title VERIFIED; book title VERIFIED; pages VERIFIED (349–366); book year VERIFIED (© 2024); publisher VERIFIED (Birkhäuser); DOI VERIFIED; URL VERIFIED; author-version note VERIFIED.

### Exact suggested BibTeX replacement strings

These are correction proposals only; this read-only audit does not edit the
bibliography.  Initials are deliberately retained for Nazarenko because the
official author display is `A. V. Nazarenko`, while the submission-history
name is `Andrey Nazarenko`.

For `Nazarenko2013`, replace the two mismatched fields with exactly:

```bibtex
  author        = {Nazarenko, A. V.},
  primaryclass  = {math-ph},
```

For `AigonDupuyEtAl2005`, replace the author field with exactly:

```bibtex
  author  = {Aigon-Dupuy, Aline and Buser, Peter and Cibils, Michel and K{\"u}nzle, Alfred F. and Steiner, Frank},
```

## Phase B — citation-context audit (9/9)

Phase A metadata failures remain blocking even where the cited content is faithful.

| Context | TeX locator | Source locator | Context verdict | Evidence |
|---|---|---|---|---|
| `Nazarenko2013` | L132–140 | eqs. (10)–(18) | VERIFIED | Official arXiv PDF gives the admissible parameter domain, `b=(sqrt(2)a cos(alpha-π/4))^-1`, relator, explicit `g0,g1`, and rotated `g2,g3`; this supports the family/input statement. |
| `AigonDupuyEtAl2005` | L139–141 | abstract | VERIFIED | The abstract is explicitly about geometric octagon models of genus-two Teichmüller space. The author-field mismatch is a separate Phase A failure. |
| `Nazarenko2013` | L239–243 | eqs. (10)–(18) | VERIFIED | Substitution `a=u`, `alpha-π/4=0` reproduces the displayed `N`, `g0`, `g1`, rotations, alternating radii, and eight-factor relation. |
| `Popescu2024` | L317–324 | Cor. 3.2 | VERIFIED | The official author-version text states that `exp(alpha)` is transcendental for every nonzero algebraic `alpha`; applying `alpha=-1/5` is exact. |
| `Takeuchi1975` | L326–334 | Thm. 1, condition (I) | VERIFIED | The official PDF requires the trace field to be a finite-degree algebraic number field and traces to be algebraic integers for an arithmetic cofinite Fuchsian group. |
| `Voight2009` | L345–353 | §§1–4 | VERIFIED | The official paper assumes exact generators in `SL_2(K)` for a number field, treats arithmetic Fuchsian groups/quaternion orders, and develops exact fundamental-domain/reduction algorithms. |
| `DespreEtAl2023` | L348–353 | §§2–3 | VERIFIED | The official abstract/PDF takes a closed orientable hyperbolic surface represented by a fundamental polygon with side pairings and computes an explicit Dirichlet domain. |
| `Nazarenko2013` | L355–361 | eqs. (10)–(18) | VERIFIED | Faithful family/input attribution; the manuscript expressly withholds project-derived systole credit from the source. |
| `AigonDupuyEtAl2005` | L357–361 | abstract | VERIFIED | Faithful family-level corroboration only; no systole/certificate result is attributed to it. |

Citation-format check: `natbib` is consistently configured as numerical `numbers,sort&compress` with `plainnat`; all six bibliography entries are cited and all nine cite commands resolve.

## Phase C — every numerical/data surface

The numerical/data denominator is 10 surface families, chosen to cover every scientific number, finite count, digest, and execution-status assertion in the body. All 10 were traced; there is no untraced statistical claim.

| Surface | TeX locator | Exact local evidence | Result |
|---|---|---|---|
| Input `u=e^-1/10`, `x=e^-1/5`, `Delta`, alternating radius `b`, four matrices, relator | L208–243 | `results/round7_nonarithmetic_control_matrices.json`; Round-8 builder exact inverse/relator guards; official Nazarenko equations | VERIFIED |
| Radius claims `u^4>1/2`, displayed `u^4` and `u/tanh(3/2)` enclosures, `D_F<3` | L288–307 | `proof_guards.vertex_radius_order` and `.fundamental_polygon_radius` in `results/round8_control_finite_ball_certificate.json` | VERIFIED |
| Transcendental trace equation and nonarithmetic conclusion | L311–334 | direct polynomial rearrangement; Popescu Cor. 3.2; Takeuchi Thm. 1 | VERIFIED |
| Exact normal form, denominator parity, equality/inverse/relator predicates, Taylor order 24 | L377–494 | builder implementation and unit tests; `proof_guards.all_pass=true`; sign-order histograms | VERIFIED |
| Frozen cutoff `21/10`; recentered bound `<81/10`; tile radius `<111/10`; `cosh(111/20)^2` interval and guard 20000 | L503–562, L607–614 | certificate proof guards; independent recomputation gave `16543.290045872232000529962843... < 20000` | VERIFIED |
| Candidate formula, witness `g0*g3`, `ell*<21/10`, 69-digit decimal, primitivity | L629–693 | `exact_systole.*` certificate fields; exact-zero witness polynomial; independent decimal recomputation | VERIFIED |
| Included 18,533; nonidentity 18,532; rejected 108,616; max depth 11; strict 18,388; equality 144; below 0; no cap | L762–770 | `finite_completeness.*` and `exact_systole.*`; `1 + 18,388 + 144 = 18,533` | VERIFIED |
| Depth histogram `1,8,56,392,1632,3976,5104,4168,2260,752,176,8`; order-24/order-0 sign totals | L774–783 | artifact histograms; independent sum = 18,533 | VERIFIED |
| Included/rejected/certificate/freeze/core/tree SHA-256 values | L785–807 | live `sha256sum`; receipt; double fresh replay | VERIFIED |
| Negative execution/scope flags and Route-A tuple | L825–883, L912–938 | validation JSON and receipt: both censuses/comparison/A2 false; Route B false; target data false | VERIFIED |

### Independent execution evidence

- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s code -p 'test_*.py' -v`: **104/104 passed**, exit 0.
- `PYTHONDONTWRITEBYTECODE=1 ./experiments/reproduce_round8.sh`: exit 0; its Round-8 suite reports **24 passed**, runs the builder twice, and returns identical tree hashes `c30beebdd2e832d9375f55f1eab700868b7b967dfb5ee43fcecc0ba5f60919ac`.
- Live hashes matched the receipt for the certificate, source matrix, validation JSON, builder, Round-8 tests, and reproducer (6/6).
- Independent high-precision display checks reproduced `u`, `u^4`, `tanh(3/2)`, `cosh(111/20)^2`, the candidate cosh, `cosh(21/20)`, and the stated systole decimal. These decimal checks corroborate display text; the proof still rests on exact fraction/polynomial guards.

### C3 and C4

There is no figure. The single standalone results table has no Figure Package trace, which is a trace-unavailable **PASS WITH NOTES** advisory under C3; its cells were nevertheless checked directly against the JSON certificate above.

**C4 boundary (required verbatim):** "This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS."

The local scripts, tests, receipts, and exact artifacts are strong substantive provenance, but they are not a schema-valid ARS Material Passport. With no positive proof that this package predates #260, the fail-closed post-#260 rule applies. This is `P28-IL-MEDIUM-1`.

## Phase D — paragraph originality

Paragraph denominator: **72** English prose blocks from numbered Introduction through Conclusion (L120–938), split on blank lines; headings, display-only blocks, tables, lists, and blocks with fewer than 20 prose tokens were excluded. Sample: **28/72 = 38.9%**, covering every major section. Search fragments below are 8–12 consecutive words after deterministic de-TeX/punctuation normalization. Each was searched in quotation marks; fuzzy results were also inspected. No exact source match was found.

| # | TeX locator | Recorded 8–12-word search fragment | Grade |
|---:|---|---|---|
| 1 | L122–130 | `Its definition is short but an exact determination from a polygonal presentation` | ORIGINAL |
| 2 | L132–141 | `This article resolves both parts for one explicit member of the genus-two` | ORIGINAL |
| 3 | L157–166 | `all group elements are reduced to canonical polynomial matrix states` | ORIGINAL |
| 4 | L245–252 | `By the polygon construction the quotient is a closed oriented hyperbolic surface` | COMMON_KNOWLEDGE |
| 5 | L256–265 | `It binds four kinds of input that should not be conflated` | ORIGINAL |
| 6 | L276–284 | `There are also two deliberately separate evidentiary layers` | ORIGINAL |
| 7 | L311–324 | `nonarithmetic in the title can be verified without a decimal trace test` | ORIGINAL |
| 8 | L326–334 | `Takeuchi's characterization requires the invariant trace field of an arithmetic cofinite` | ORIGINAL |
| 9 | L345–353 | `Algorithms for exact or certified work with Fuchsian groups have several nearby` | ORIGINAL |
| 10 | L355–361 | `Independent work on geodesic octagons and genus-two Teichmüller space supplies` | ORIGINAL |
| 11 | L363–370 | `The present scope is deliberately narrower than a surface-to-surface comparison` | ORIGINAL |
| 12 | L393–398 | `the implementation cancels a common factor from all four numerator entries` | ORIGINAL |
| 13 | L459–464 | `The representation is exact but not claimed to be an optimal normal` | ORIGINAL |
| 14 | L499–501 | `The search must contain at least one representative of every short conjugacy` | ORIGINAL |
| 15 | L524–535 | `List in order the tiles whose interiors the segment crosses` | ORIGINAL |
| 16 | L570–579 | `A closed hyperbolic ball is compact so it contains only finitely` | COMMON_KNOWLEDGE |
| 17 | L598–605 | `The crossed-tile sequence then manufactures a generator path` | ORIGINAL |
| 18 | L616–622 | `Every generator edge from every included state is classified` | ORIGINAL |
| 19 | L674–679 | `There are 18 388 strict positive signs and 144 exact zero polynomials` | ORIGINAL |
| 20 | L708–712 | `This distinction prevents the most tempting overinterpretation of the certificate` | ORIGINAL |
| 21 | L719–723 | `Every proof decision branch in the implementation uses Python standard library` | ORIGINAL |
| 22 | L815–823 | `A successful replay has more obligations than reproducing the headline number` | ORIGINAL |
| 23 | L847–858 | `a bounded word search could miss a short conjugate represented` | ORIGINAL |
| 24 | L869–883 | `the result should be read as a control-side infrastructure theorem` | ORIGINAL |
| 25 | L893–897 | `The theorem concerns one fixed parameter Although the normal form construction` | ORIGINAL |
| 26 | L912–916 | `the work is a control surface theorem not evidence of a magnetic` | ORIGINAL |
| 27 | L920–931 | `The lower bound is global because a geometric tile-chain theorem places` | ORIGINAL |
| 28 | L933–938 | `The central methodological outcome is the separation of geometry exact algebra` | ORIGINAL |

Summary: ORIGINAL 26 (92.9% of sample); COMMON_KNOWLEDGE 2 (7.1%); PARAPHRASE 0; CLOSE_MATCH 0; VERBATIM 0.

D3 AI-writing-characteristic screen: one of six indicators was weakly present—deliberate parallel organization in L157–166 and L845–858. The manuscript is highly specific, does not over-hedge, integrates citations at explicit claim boundaries, and varies its proof/expository rhythm. **1/6 is below the two-indicator alert threshold.** This is a heuristic style check, not an authorship determination; the manuscript already discloses Codex assistance.

> This originality verification uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 38.9%, and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.

## Phase E — stable claim-registry contract

### Supersession notice

The earlier manual **6/6 high-impact** table is **SUPERSEDED and is not Stage
2.5 gate evidence**.  A selection bug had failed to classify most numerical,
causal, methods-critical, and headline claims as high impact.  The stable
registry now contains **85 claims: 78 HIGH-IMPACT, 3 RANDOM, and 4
NOT-SELECTED**.  The selected denominator is therefore **81/81 claims**, not
6/6.

Stable sidecars bound to the audited manuscript SHA-256
`864d2f6ce0f76245d4d4237ba2981b3e82fc8e31f7991f1f331817f7c028aec7`:

| Sidecar | SHA-256 | Stable result |
|---|---|---|
| `stage2_5_claim_registry.json` | `031e04aae854667ba03e4b39d8df28fa61391264ab7f8c1fee55d6d6a3514f07` | 85 claims: H78/R3/N4; 81 selected |
| `stage2_5_claim_registry_coverage.json` | `312bd9883bd4a15993ce40702e696e125e1ba550b762204a9c9956b76fd2b35a` | 5 mechanical candidates; 0 gaps; official replay PASS |
| `stage2_5_evidence_rows.json` | `31c68cf97a63af5709c7c48883b3df1765449bb47b3efe0cc8fff89872c4cc3f` | 84 exact tuple rows for all 81 selected claims; official validator PASS |
| `stage2_5_claim_strength_drift_findings.json` | `c5a134885af90e327aa32f6112eab32cc9d1288df2409be85b897a93596a92a9` | schema PASS; `skipped_no_revision_evidence` |

The 81 selected claims expand to 84 evidence tuples because six
source-bearing claims contain nine reference tuples.  All 84 rows have
claim-level verdict `VERIFIED`; tier, claim text, locator, tuple membership,
and registry hashes are consistent, with no failed or inflated row.  The
contract therefore **PASSES** structurally and its verdict ledger is
internally consistent.

Important limitation: all 84 evidence rows have `excerpt.state = anchorless`.
Consequently the sidecar alone does **not** independently prove the semantic
truth of 84 claims or preserve primary-source quotations.  Semantic support
comes from the complete Phase B citation-context audit, the 10/10 Phase C
surface-family audit, the written proof chain, and the frozen artifacts/live
replay above.  The anchorless receipts should be upgraded to source-bound
excerpts if the submission workflow requires the evidence rows themselves to
be independently auditable.

### Source-bearing claims: nine tuple locator/excerpt candidates

Each excerpt candidate below is at most 25 words.  Repeated claims point to a
single candidate rather than duplicating source text.  These candidates are
recorded here only; the read-only audit does not mutate
`stage2_5_evidence_rows.json`.

| Claim | Reference tuple | Official/author source locator | Short original-text candidate |
|---|---|---|---|
| `P28-E1-004` | `Nazarenko2013` | author version, arXiv:1301.5446v1, PDF p. 3, discussion before eq. (7) | N-A: “we choose a pair (a, α) as independent real variables” |
| `P28-E1-004` | `AigonDupuyEtAl2005` | DOI `10.1063/1.1850177`, publisher abstract; EPFL official record | A-A: “special emphasis on their construction by geodesic octagons” |
| `P28-E1-010` | `Nazarenko2013` | author version, PDF pp. 4–5, eqs. (10)–(18), especially eqs. (16)–(18) | N-B: “The remaining generators are simply obtained by rotations” |
| `P28-E1-020` | `Popescu2024` | official chapter DOI `10.1007/978-3-031-51959-8_16`; author version arXiv:2306.14352, Cor. 3.2, PDF p. 16 | P-A: “For any nonzero algebraic number α, e^α is a transcendental number.” |
| `P28-E1-021` | `Takeuchi1975` | official J-STAGE PDF p. 601, Thm. 1, condition (I) | T-A: “Then k1 is an algebraic number field of finite degree” |
| `P28-E1-023` | `Voight2009` | official Centre Mersenne PDF p. 467, Introduction | V-A: “we assume that Γ is specified by a finite set of generators” |
| `P28-E1-023` | `DespreEtAl2023` | official DROPS PDF p. 27:2, Thm. 1 | D-A: “Let S be a closed orientable hyperbolic surface of genus g given by a fundamental polygon” |
| `P28-E1-024` | `Nazarenko2013` | same official locator as N-A, with construction continued through eqs. (10)–(18) | reuse candidate N-A |
| `P28-E1-024` | `AigonDupuyEtAl2005` | same official DOI/abstract locator as A-A | reuse candidate A-A |

The new Phase E contract does not cure the two Phase A metadata failures or
the Phase C4 structural failure.

## Seven AI-research failure modes

| Mode | Status | Evidence |
|---|---|---|
| 1. Implementation bug passing self-review | **CLEAR** | 104 historical tests passed; 24 Round-8 tests passed; exact predicates are failure-closed; independent double build is byte-identical; no unresolved interval/resource cap/failed relation. |
| 2. Hallucinated citation | **SUSPECTED — BLOCKING** | All six works exist, but two records contain serious author/subject metadata errors (`P28-IL-SERIOUS-1/2`). |
| 3. Hallucinated experimental result | **CLEAR** | Every reported numerical result and digest resolves to the committed certificate/validation/receipt; live replay reproduced the result tree. |
| 4. Shortcut reliance | **CLEAR** | This is an exact theorem/enumeration, not a predictive benchmark. The manuscript explicitly attacks word-cap, float-hash, tolerance, target-tuning, and owner-count shortcuts. |
| 5. Bug reframed as novel insight | **CLEAR** | No surprise/counterintuitive narrative is used; the main result is derived from a symbolic theorem plus a replayed exact finite classification. |
| 6. Methodology fabrication | **CLEAR** | Methods L719–739 correspond to the actual builder/reproducer and config constants; source and code hashes match. The separate missing-passport disclosure defect remains `P28-IL-MEDIUM-1`. |
| 7. Early frame-lock | **CLEAR** | The paper narrows itself to a control-surface prerequisite, records negative Route-A scope, and does not promote the result to the planned magnetic/A2 comparison. |

Because Mode 2 is SUSPECTED, the seven-mode gate blocks independently of the ordinary Phase A verdict.

## Correction and re-verification order

1. Correct `Nazarenko2013` and `AigonDupuyEtAl2005` exactly as stated in `P28-IL-SERIOUS-1/2`; rebuild the PDF and re-run the six-entry Phase A field comparison.
2. Add the Material Passport declaration/provenance package required by `P28-IL-MEDIUM-1`; lint it and re-run C4 against every experiment-backed claim.
3. Re-run ghost-citation, PDF-reference-page, and all seven failure-mode checks on the corrected artifact. The mathematical/numerical and originality surfaces need not be rewritten on the evidence found here, but any changed prose must re-enter the relevant sampling/claim checks.
