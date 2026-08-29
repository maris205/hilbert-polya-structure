# Paper 26 — Stage 2.5 independent integrity audit

Audit date: 2026-08-29 UTC  
Auditor role: independent read-only integrity reviewer  
Audited draft: `paper/manuscript.tex` (480 lines) and `paper/references.bib` (5 entries)  
Protocol: ARS-Codex Stage 2.5 pre-review, Phases A–E and all seven AI-research failure modes

## Current Round-9 disposition — supersedes the historical audit state below

**ARS Stage 2.5 verdict: PASS AT MANDATORY CHECKPOINT. Stage 3 is not authorized.** The scholar-owned experiment-intake declaration is now present in the material passport, the provenance inventory is populated from existing Round-2--Round-8 artifacts, and the direct experiment-claim alignment audit is clean. Advancement remains paused at the mandatory checkpoint pending explicit authorization.

| Current Round-9 surface | Coverage | Current result |
|---|---:|---|
| Reference verification | 5/5 references | VERIFIED |
| Phase-E selected claims | 68/68 distinct claims | VERIFIED; 0 distortion or unverifiable verdicts |
| Selected evidence tuples | 70/70 tuples | structurally closed; all 70 carriers are anchorless, an advisory limitation |
| Experiment provenance | 7/7 evidenced Round-2--Round-8 packages | declared and mapped to existing artifacts |
| Direct experiment-claim alignment | 17/17 claims | ALIGNED; 0 contradiction, unsupported, or ambiguous verdicts |

The former blocker `P26-S25-F001`, the open-finding count, and the FAIL-CLOSED conclusion retained below describe the pre-declaration snapshot and are **superseded**. The anchorless-row condition remains advisory because the independent semantic audit checked every selected claim against its manuscript proof chain, exact artifacts/tests where applicable, official source-context audit where applicable, and stated limitations. The scientific Route-A state is unchanged by this integrity-gate update.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

## Historical decision and counts — superseded

> The following FAIL-CLOSED decision and all later references to an absent declaration, open `P26-S25-F001`, blocking Mode 6 verdict, or unresolved stage gate are retained as the dated pre-declaration audit record. They do not govern the current Round-9 disposition above.

**Stage 2.5 verdict: FAIL-CLOSED — structural provenance gate only.** The reference, citation-context, exact-artifact, originality-screen, and current full selected-population claim-evidence checks are clean. The fail-closed blocker is `P26-S25-F001`: the scholar-owned `experiment_intake_declaration` is absent. An agent must not infer or fabricate that declaration from tests or receipts.

| Surface | Coverage | Result |
|---|---:|---|
| BibTeX existence/metadata/hallucination | 5/5 entries (100%) | 5 VERIFIED; 0 SUSPECTED; 0 DOI misdirection |
| In-text citation contexts | 5/5 contexts (100%) | 5 VERIFIED; 0 contradicted/overstretched |
| Registered numerical/data claim families | 14/14 (100%) | all reproduce from exact local artifacts |
| Body-paragraph originality screen | 21/65 (32.3%) | 21 CLEAR; 0 actionable overlap |
| Claim registry | 72 claims | 0 mechanically uncovered candidates; semantic extraction completeness remains `not_machine_detectable` |
| Historical Phase-E sample | 4/4 high-impact + 7 random = 11/11 | all VERIFIED in the initial snapshot; **superseded for current counts** |
| Current Phase-E semantic audit | 68/68 selected distinct claims; 70/70 selected tuples | all VERIFIED; semantic clean; 70/70 anchorless rows are advisory only |
| Tests | 74 historical + Round-8 18/18 | all pass; Round-8 two-build tree byte-identical |
| Open provisional findings | 1 | one structural C4 blocker; no content-integrity finding |

## Phase A — 100% reference verification

Every populated BibTeX field was checked. `VERIFIED` means the field agrees with the linked publisher, journal platform, official database, or DOI metadata. No `MISMATCH` or `NOT_FOUND` field remains.

| Key; exact query | Authoritative primary/official record | Field-by-field result | Hallucination scan |
|---|---|---|---|
| `manin1972`; `"Parabolic Points and Zeta-Functions of Modular Curves" "10.1070/IM1972v006n01ABEH001867" official` | [MathNet journal record](https://www.mathnet.ru/eng/im2290), including the official 46-page English PDF | author VERIFIED; title VERIFIED; journal VERIFIED; year VERIFIED; volume VERIFIED; number VERIFIED; pages VERIFIED; DOI VERIFIED; URL VERIFIED | VERIFIED; no title/author/venue/conflation/phantom-support or DOI-misdirection signal |
| `merel1991`; `"Opérateurs de Hecke pour Gamma_0(N) et fractions continues" "10.5802/aif.1264"` | [Annales de l'Institut Fourier / Centre Mersenne](https://aif.centre-mersenne.org/articles/10.5802/aif.1264/) | author VERIFIED; title VERIFIED; journal VERIFIED; year VERIFIED; volume VERIFIED; number VERIFIED; pages VERIFIED; DOI VERIFIED; URL VERIFIED | VERIFIED; none of TF/PAC/IH/PH/SH/DOI-misdirection |
| `ruelle1976`; `"Zeta-Functions for Expanding Maps and Anosov Flows" "10.1007/BF01403069"` | [Springer publisher record](https://link.springer.com/article/10.1007/BF01403069) | author VERIFIED; title VERIFIED; journal VERIFIED; year VERIFIED; volume VERIFIED; number VERIFIED; pages VERIFIED; DOI VERIFIED; URL VERIFIED | VERIFIED; no hallucination indicator |
| `fried1986`; `"The Zeta Functions of Ruelle and Selberg. I" "10.24033/asens.1515"` | [Numdam journal record and full text](https://www.numdam.org/articles/10.24033/asens.1515/) | author VERIFIED; title VERIFIED; journal VERIFIED; year VERIFIED; series VERIFIED; volume VERIFIED; number VERIFIED; pages VERIFIED; DOI VERIFIED; URL VERIFIED | VERIFIED; no hallucination indicator |
| `lmfdb112aa`; `site:lmfdb.org "Newform orbit 11.2.a.a" eta` plus exact label lookup | [Official LMFDB orbit](https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/11/2/a/a/) and [official API record](https://www.lmfdb.org/api/mf_newforms/?label=11.2.a.a&_format=json) | corporate author VERIFIED; title/label VERIFIED; snapshot year VERIFIED; `LMFDB` venue VERIFIED; URL VERIFIED; access note VERIFIED | VERIFIED; official page gives level 11, weight 2, trivial character, dimension 1, coefficient field Q, q-expansion, and the eta quotient |

Reference-status total: **5 VERIFIED / 0 SUSPECTED / 0 unresolved**. All DOI strings resolve to the same works named in the entries.

## Phase B — citation-context verification

All five contexts were inspected, exceeding the 30% minimum.

| Context | Manuscript locator | Source locator checked | Verdict |
|---|---|---|---|
| Level-11 normalized newform, one-dimensional newspace, rational field, q-expansion, eta quotient | L86–L88 | LMFDB Properties, Newform invariants, q-expansion, eta-quotient sections | VERIFIED |
| Modular-symbol integrals as homological periods | L95–L97 | Manin, official English PDF pp. 19–25, especially §1 homology classes and integration | VERIFIED |
| Hecke action on relative homology in the projective-line model | L141–L143 | Merel, Introduction and §§1–2, official PDF pp. 519–526 | VERIFIED |
| Zeta functions for expanding maps/Anosov flows organized through periodic-orbit dynamics | L146–L148 | Ruelle publisher record/abstract and article scope | VERIFIED; manuscript makes only the broad historical claim |
| Prime periodic orbits distinguished from finite covers/iterates | L146, L149–L150 | Fried §2, official full text pp. 496–502 | VERIFIED |

Context total: **5/5 VERIFIED (100%)**. No citation is used to support the paper's new finite taxonomy; those claims instead point to exact local proof/artifact evidence.

## Phase C — every numerical/data surface

The unit-test command ran with bytecode writes disabled. It passed **74/74** historical tests. The verify-default Round-8 script passed **18/18**, generated two isolated trees, found them byte-identical, and returned tree SHA-256 `cc36c1f952c9ce89050996f4bb4c9905571f9ef09a0d7115be8a985e02a5621d`.

| ID | Manuscript surface | Exact local cross-check | Result |
|---|---|---|---|
| P26-C-01 | L36, L47, L61, L81–L88: level 11, weight 2, unique normalized orbit, rational field, eta quotient and coefficients | official LMFDB orbit/API and q-expansion | VERIFIED |
| P26-C-02 | L47, L71, L364: 11 sources, primes `{2,3,5,7,13}`, 55 word/prime groups, 138 owner instances | independent CSV recount: 11, 5, 55, 138 | VERIFIED |
| P26-C-03 | L47, L366–L386: instance split 2 full kernels, 2 projection-only kernels, 134 nonkernels; per-prime totals 18/22/30/30/38 | `round8_exact_instance_taxonomy_ledger.csv`; mutually exclusive count is 138, with all four kernels at p=5 | VERIFIED |
| P26-C-04 | L47, L395–L397: each primary law passes 4/fails 51 of 55; control fails 55 | independent recount of 165 group/law rows | VERIFIED |
| P26-C-05 | L308, L399–L401: failure mechanisms | exact flags give `a_p`: 51 degree-one+nonunit failures; `a_p^2`: 47 double plus 4 nonunit-only; control: 51 double plus 4 degree-one-only | VERIFIED |
| P26-C-06 | L208, L251: all registered outputs primitive, root exponent 1 | all 138 rows: rebuilt owner true, determinant 1, c mod 11 = 0, primitive true, root exponent 1 | VERIFIED |
| P26-C-07 | L298, L331, L345: all 11 source coordinates k are nonzero | 11 distinct source words; k values are ±1 or ±2, never 0 | VERIFIED |
| P26-C-08 | L316–L328: 12 cosets, 24 arcs, 35 relation rows, rank 21, dimensions 3/2/1 | `round7_exact_homology_model.json`, exact rational tests, and Round-8 verifier | VERIFIED |
| P26-C-09 | L331–L352: exact rational period ratios, rational square sums, exact kernel tests | all 138 ratios and 165 moment rows serialized exactly; zero decisions use rational coordinates, not floats | VERIFIED |
| P26-C-10 | L393: four p=5 degree-5 kernel words and their 2+2 split | exact instance ledger word/prime/degree/classification filter | VERIFIED |
| P26-C-11 | L411–L422: locked input/source SHA-256 values | direct `sha256sum`: cycle ledger `f906…0662`, moment ledger `f95e…edea`, builder `3bb9…582b`, tests `9c0c…391b`, script `3e32…94d3`, freeze `2831…bc8d` | VERIFIED |
| P26-C-12 | L424: 138 instance rows, 165 group/law rows, 165 numerical-verdict agreements, max residual `1.9895196601282805e-13` | independent CSV recount and maximum calculation | VERIFIED |
| P26-C-13 | L426–L428: 18 tests, two isolated four-file trees, exact tree hash | live verify-default replay | VERIFIED |
| P26-C-14 | L438–L447: no prime-target/Riemann-zero data; no A2/root-count run; Route B closed | every 138 row flag is false; `round8_summary.json` and receipt agree | VERIFIED |

Experiment/provenance boundary: **This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.**

## Phase D — originality heuristic

Universe definition: 65 English prose blocks from Introduction through Conclusion, containing at least 20 lexical words, excluding front matter, Chinese summary, declarations, references, and math-only/table-only blocks. The sample contains 21 blocks (32.3%), covers every major section, and uses exact quoted WebSearch fragments of 8–12 words.

| ID | Line / section | Exact search fragment | Originality verdict |
|---|---|---|---|
| P26-D-01 | L61 / Introduction | “Arithmetic surfaces offer a natural place to ask how algebraic correspondences interact” | CLEAR — no exact match observed |
| P26-D-02 | L69 / Introduction | “The Hecke correspondence acts on a cycle by producing a finite sum” | CLEAR — no exact match observed |
| P26-D-03 | L73 / Introduction | “The conclusion is an obstruction, not a positive determinant construction” | CLEAR — no exact match observed |
| P26-D-04 | L95 / Mathematical setting | “The classical modular-symbol framework identifies such integrals with homological periods” | CLEAR — no exact match observed |
| P26-D-05 | L123 / Mathematical setting | “determines an oriented quotient loop by projecting an oriented segment” | CLEAR — no exact match observed |
| P26-D-06 | L141 / Related work | “places weight-two periods in the homology of modular curves” | CLEAR — no exact match observed |
| P26-D-07 | L146 / Related work | “separated prime periodic orbits from their iterates in comparing Ruelle” | CLEAR — no exact match observed |
| P26-D-08 | L202 / Hecke ownership | “The theorem is sum-valued. It does not send one primitive orbit” | CLEAR — no exact match observed |
| P26-D-09 | L208 / Hecke ownership | “The second integer is the primitive-root exponent of” | CLEAR — no exact match observed |
| P26-D-10 | L210 / Hecke ownership | “These distinctions explain why a correct linear equality in homology” | CLEAR — no exact match observed |
| P26-D-11 | L222 / Zeta variations | “Every assertion below is exact for a finite owner family” | CLEAR — no exact match observed |
| P26-D-12 | L274 / Zeta variations | “The obstruction is algebraic before any root-finding experiment is contemplated” | CLEAR — no exact match observed |
| P26-D-13 | L296 / Zeta variations | “quantifier is what exposes this rigidity. For a single numerical value” | CLEAR — no exact match observed |
| P26-D-14 | L345 / Schreier classifier | “all real periods are scalar multiples of the single compact” | CLEAR — no exact match observed |
| P26-D-15 | L356 / Schreier classifier | “The two kernel labels answer different questions. A full complex-period” | CLEAR — no exact match observed |
| P26-D-16 | L360 / Finite taxonomy | “This hierarchy also clarifies what the enumeration proves. Exhausting” | CLEAR — no exact match observed |
| P26-D-17 | L393 / Finite taxonomy | “The four kernels all occur at p=5 and cycle degree five” | CLEAR — no exact match observed |
| P26-D-18 | L432 / Reproducibility | “The certificate is layered so that each conclusion can be audited” | CLEAR — no exact match observed |
| P26-D-19 | L447 / Adversarial controls | “Two proves-too-much controls are decisive. First, every compactly extending” | CLEAR — no exact match observed |
| P26-D-20 | L451 / Limitations | “The taxonomy is complete only for the frozen output multiset” | CLEAR — no exact match observed |
| P26-D-21 | L457 / Conclusion | “The level-11 newform time change has a clean arithmetic period coordinate” | CLEAR — no exact match observed |

Required limitation disclaimer: **This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 32.3%, and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.**

## Phase E — claim verification and sidecars

### Authoritative stable-selection result

- [`stage2_5_phase_e_semantic_audit.md`](stage2_5_phase_e_semantic_audit.md) is the authoritative current Phase-E semantic audit.
- `notes/stage2_5_claim_registry.json`: 72 registered claims; 65 HIGH-IMPACT, 3 RANDOM, 0 TOP-UP, and 4 NOT-SELECTED.
- `notes/stage2_5_claim_registry_coverage.json`: 4 mechanical candidates, 0 unregistered.
- Selected distinct claims: **68/68 VERIFIED**; 0 distortion and 0 unverifiable verdicts.
- Selected tuples: **70/70 present, unique, and VERIFIED**. The tuple count exceeds the distinct-claim count because the three source-bearing claims expand to five `(claim_id, ref_slug)` tuples.
- All **70/70** persisted rows have `anchor.kind = none` and `excerpt.state = anchorless`. This is the non-gating advisory `P26-E-ADV-ANCHORLESS-1`: it limits source-excerpt replay from the receipt but does not alter the independently supported claim verdicts.
- Mechanical coverage reports zero bounded candidate gaps, while `semantic_extraction_coverage` remains `not_machine_detectable`; completeness is established only for the stable selected registry population.
- `notes/stage2_5_claim_strength_drift_findings.json`: no drift finding; status `skipped_no_revision_evidence`, appropriate because no revision-evidence bundle was supplied.

### Superseded initial snapshot retained for audit history

The earlier Phase-E pass recorded **4/4 high-impact + 7 random = 11/11 VERIFIED** and rendered the following four headline rows. That 11/11 selection and its former tier totals are retained only as historical trajectory; they are **superseded** by the 68/68-claim, 70/70-tuple audit above and must not be quoted as the current Phase-E denominator.

| Claim ID | Exact claim / TeX locator | Evidence | Verdict |
|---|---|---|---|
| P26-E1-002 | Abstract bundle: exact owner distinction, parity/moment criterion, 138-instance 2/2/134 split, primary 51/55 failures, control 55/55 failure, bounded non-global conclusion; L46–L47 | written theorems; exact instance/group ledgers; summary; receipt; LMFDB for the setup | VERIFIED |
| P26-E1-053 | Exhaustive taxonomy: 138 = 2 full kernels + 2 projection-only + 134 nonkernels, none unresolved; L366–L368 | independent recount of all 138 locked instance rows; exact classifier tests | VERIFIED |
| P26-E1-057 | Group verdicts: each primary law 4 passes/51 failures of 55; four p=5 kernel survivors; control fails 55; L395–L397 | independent recount of all 165 group/law rows | VERIFIED |
| P26-E1-072 | Conclusion: cycle-pushforward ownership defeats the tested primitive-Euler interpretation; finite exact taxonomy only; global determinant/Hilbert–Pólya claim excluded; L457 | Theorems at L169–L200, L253–L272, L330–L352, L366–L401; Route flags and limitations | VERIFIED |

## Seven AI-research failure modes

| Mode | Concrete evidence | Verdict |
|---|---|---|
| 1. Implementation bugs | 74 historical tests, Round-8 18/18, exact integer/rational arithmetic, tamper-rejection tests, source locks, two byte-identical trees | CLEAR |
| 2. Hallucinated citations | 5/5 entries and 5/5 contexts independently verified through official records/full text | CLEAR |
| 3. Hallucinated results | every headline count independently recomputed from 138/165 rows; hashes and replay agree | CLEAR |
| 4. Research shortcuts / cherry-picking | population and laws were frozen before classification; all rows are exhausted; negative control retained; no target/zero data used | CLEAR |
| 5. Bug-as-insight storytelling | manuscript calls the result a bounded finite obstruction, separates exact proof from numerical cross-check, and reports survivors/failures mechanistically | CLEAR |
| 6. Methodology fabrication | code, tests, ledgers, receipts and narrative agree, but no scholar-owned `experiment_intake_declaration` exists | **INSUFFICIENT EVIDENCE — BLOCKING** (`P26-S25-F001`) |
| 7. Frame lock / overclaim | Route A layers, proves-too-much controls, non-deduplicated multiset boundary, convergence exclusions, and next obligation are explicit | CLEAR |

## Stable provisional findings

| Finding ID | Severity/status | Evidence | Required disposition |
|---|---|---|---|
| `P26-S25-F001` | BLOCKING / OPEN | Repository-wide exact search finds no `experiment_intake_declaration`; deterministic receipts cannot substitute for a scholar attestation | Scholar supplies the intake declaration in the material passport/pipeline record; rerun C4/Mode 6. The agent must not author it on the scholar's behalf. |
| `P26-S25-C001` | CLOSED | Claim registry, coverage, evidence-row, drift, and semantic-audit artifacts now exist; current Phase E is 68/68 claims and 70/70 tuples VERIFIED, with 0 mechanically unregistered candidates | `CLOSED_BY_CURRENT_STAGE2_5_ARTIFACT`; no action |

**Historical conclusion (superseded):** Content-integrity conclusion: **clean**, including the authoritative current Phase-E selected population. Stage-gate conclusion: **FAIL-CLOSED until `P26-S25-F001` is scholar-resolved and C4/Mode 6 are rechecked**.
