# Paper 27 — Stage 2.5 independent integrity audit

Audit date: 2026-08-29 UTC  
Auditor role: independent read-only integrity reviewer  
Audited draft: `paper/manuscript.tex` (465 lines) and `paper/references.bib` (5 entries)  
Protocol: ARS-Codex Stage 2.5 pre-review, Phases A–E and all seven AI-research failure modes

## Current Round-9 disposition — supersedes the historical audit state below

**ARS Stage 2.5 verdict: PASS AT MANDATORY CHECKPOINT. Stage 3 is not authorized.** The scholar-owned experiment-intake declaration is now present in the material passport, the eligible provenance inventory is populated from existing artifacts, and the direct experiment-claim alignment audit is clean. Advancement remains paused at the mandatory checkpoint pending explicit authorization.

| Current Round-9 surface | Coverage | Current result |
|---|---:|---|
| Reference verification | 5/5 references | VERIFIED |
| Phase-E selected claims | 70/70 distinct claims | VERIFIED; 0 distortion or unverifiable verdicts |
| Selected evidence tuples | 71/71 tuples | structurally closed; all 71 carriers are anchorless, an advisory limitation |
| Experiment provenance | 5/5 eligible packages (Rounds 2, 4, 5, 7, and 8) | declared and mapped to existing artifacts |
| Direct experiment-claim alignment | 14/14 claims | ALIGNED; 0 contradiction, unsupported, or ambiguous verdicts |

Round 3 is a literature audit and Round 6 is a source-positioning, human-pending audit. Neither is experiment provenance, and both are deliberately excluded from the five provenance entries and fourteen direct-claim alignments. The former blocker `P27-S25-F001`, the open-finding count, and the FAIL-CLOSED conclusion retained below describe the pre-declaration snapshot and are **superseded**. The anchorless-row condition remains advisory because the independent semantic audit checked every selected claim against its manuscript proof chain, exact artifacts/tests where applicable, official source-context audit where applicable, and stated limitations. The scientific Route-A rejection/Route-B authorization state is unchanged by this integrity-gate update.

This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.

## Historical decision and counts — superseded

> The following FAIL-CLOSED decision and all later references to an absent declaration, open `P27-S25-F001`, blocking Mode 6 verdict, or unresolved stage gate are retained as the dated pre-declaration audit record. They do not govern the current Round-9 disposition above.

**Stage 2.5 verdict: FAIL-CLOSED — structural provenance gate only.** The reference, context, exact-artifact, originality-screen, and current full selected-population claim-evidence checks are clean. The fail-closed blocker is `P27-S25-F001`: the scholar-owned `experiment_intake_declaration` is absent and cannot be reconstructed by an agent from local receipts.

| Surface | Coverage | Result |
|---|---:|---|
| BibTeX existence/metadata/hallucination | 5/5 entries (100%) | 5 VERIFIED; 0 SUSPECTED; 0 DOI misdirection |
| In-text citation contexts | 5/5 contexts (100%) | 5 VERIFIED; 0 contradicted/overstretched |
| Registered numerical/data claim families | 13/13 (100%) | all match exact local proofs/artifacts |
| Body-paragraph originality screen | 21/67 (31.3%) | 20 no-match CLEAR + 1 standard-theorem phrase CLEAR |
| Claim registry | 77 claims | 0 mechanically uncovered candidates; semantic extraction completeness remains `not_machine_detectable` |
| Historical Phase-E sample | 4/4 high-impact + 7 random = 11/11 | all VERIFIED in the initial snapshot; **superseded for current counts** |
| Current Phase-E semantic audit | 70/70 selected distinct claims; 71/71 selected tuples | all VERIFIED; semantic clean; 71/71 anchorless rows are advisory only |
| Tests | 58 historical + Round-8 12/12 | all pass; two isolated Round-8 builds byte-identical |
| Open provisional findings | 1 | one structural C4 blocker; no content-integrity finding |

## Phase A — 100% reference verification

Every populated BibTeX field was checked. `VERIFIED` denotes agreement with the publisher, official journal platform, official arXiv record, or DOI metadata. No `MISMATCH` or `NOT_FOUND` field remains.

| Key; exact query | Authoritative primary/official record | Field-by-field result | Hallucination scan |
|---|---|---|---|
| `martinez2016`; `"Horocycle Flows for Laminations by Hyperbolic Riemann Surfaces and Hedlund's Theorem" "10.3934/jmd.2016.10.113"` | [AIMS Journal of Modern Dynamics](https://www.aimsciences.org/article/doi/10.3934/jmd.2016.10.113) and official arXiv full text 0711.2307 | authors VERIFIED; title VERIFIED; journal VERIFIED; year VERIFIED; volume VERIFIED; pages VERIFIED; DOI VERIFIED; URL VERIFIED | VERIFIED; no TF/PAC/IH/PH/SH/DOI-misdirection |
| `penner2008`; `"Teichmüller Theory of the Punctured Solenoid" "10.1007/s10711-007-9226-9"` | [Springer publisher record](https://link.springer.com/article/10.1007/s10711-007-9226-9) and [official arXiv record](https://arxiv.org/abs/math/0508476) | authors VERIFIED; title VERIFIED; journal VERIFIED; year VERIFIED; volume VERIFIED; number VERIFIED; pages VERIFIED; DOI VERIFIED; URL VERIFIED | VERIFIED; no hallucination indicator |
| `alcalde2026`; `"Horocyclic Trajectories in Hyperbolic Solenoidal Surfaces of Finite Type" "10.4171/GGD/967"` | [EMS Press publisher record](https://ems.press/journals/ggd/articles/14299725) and official arXiv full text 2411.18418v2 | authors VERIFIED; title VERIFIED; journal VERIFIED; year VERIFIED; online-first note VERIFIED; DOI VERIFIED; URL VERIFIED | VERIFIED; no volume/pages are invented in BibTeX |
| `hurder2019`; `"Wild Solenoids" "10.1090/tran/7339" Hurder Lukina` | [AMS DOI article](https://www.ams.org/tran/2019-371-07/S0002-9947-2018-07339-1/) and [official arXiv record](https://arxiv.org/abs/1702.03032) | authors VERIFIED; title VERIFIED; journal VERIFIED; issue-year VERIFIED (online publication in 2018, volume 371 issue 7 in 2019); volume VERIFIED; number VERIFIED; pages VERIFIED; DOI VERIFIED; URL VERIFIED | VERIFIED; date distinction is not a mismatch |
| `nica2013`; `site:arxiv.org/abs/1306.2385 "Linear groups" Nica` | [Official arXiv record](https://arxiv.org/abs/1306.2385) and official PDF | author VERIFIED; title VERIFIED; arXiv venue/identifier VERIFIED; year VERIFIED; eprint VERIFIED; archive prefix VERIFIED; primary class VERIFIED; URL VERIFIED | VERIFIED; no hallucination indicator |

Reference-status total: **5 VERIFIED / 0 SUSPECTED / 0 unresolved**.

## Phase B — citation-context verification

All five contexts were inspected, exceeding the 30% minimum.

| Context | Manuscript locator | Source locator checked | Verdict |
|---|---|---|---|
| Leafwise geodesic/horocycle framework, an explicit no-period example, universal-solenoid simply connected leaves | L76–L78 | Martínez–Matsumoto–Verjovsky §2.2, Example 4, Example 6 in official full text | VERIFIED |
| Punctured solenoid as inverse limit of finite covers, disk leaves | L81–L83 | Penner–Šarić Introduction and Definition 2.1 plus following paragraph | VERIFIED |
| Leafwise geodesic flow, finite-type solenoidal surfaces, inverse limits of regular covers/McCord terminology | L86–L88 | Alcalde et al. Definitions 4, 5, 7 and tower discussion | VERIFIED |
| Group-chain kernel and its identification with the corresponding leaf fundamental group | L91–L93 | Hurder–Lukina Definition 5.5 and following paragraph | VERIFIED |
| Malcev theorem: finitely generated linear groups are residually finite | L94–L96 | Nica official PDF p. 1, displayed theorem and definition | VERIFIED |

Context total: **5/5 VERIFIED (100%)**. The manuscript explicitly credits the general mechanisms as prior and limits novelty to its proof chain and exact owner audits.

## Phase C — every numerical/data surface

The historical unit-test command, run with bytecode writes disabled, passed **58/58**. The verify-default Round-8 script passed **12/12**, built twice, found byte-identical output, and returned core SHA-256 `a1b588724dacb2ab2986326a7a5e1c6aec654c61538c1465e26564357b568b33`.

| ID | Manuscript surface | Exact local cross-check | Result |
|---|---|---|---|
| P27-C-01 | L122–L149: no inverse-limit periodic point; quotient orders divide forward and diverge | complete written normality/residuality proof; group-chain owner quantifiers independently checked | VERIFIED |
| P27-C-02 | L161–L180: factorial principal-congruence chain and projective-sign intersection proof | direct integer congruence argument and 58-test suite | VERIFIED |
| P27-C-03 | L184–L194: three elements, eight moduli, three exact order sequences, 24 rows, 21 transitions | independent CSV recount: moduli `3,6,18,72,360,2160,15120,120960`; sequences exactly match; all 21 divisibility flags true | VERIFIED |
| P27-C-04 | L202–L229: three closed owners, eight levels, factorial lower bounds through 40320 | 24/24 ledger rows; each exact homology order equals the certified lower bound; all full quotient statuses remain `NOT_ENUMERATED_LOWER_BOUND_ONLY` | VERIFIED |
| P27-C-05 | L244–L267: every fixed-owner factor escapes each fixed coefficient prefix | written support proof plus Round-7 exact prefix artifact/tests; no finite replay is used as an asymptotic proof | VERIFIED |
| P27-C-06 | L273–L295: cover degree `N^4`, owner order `N`, primitive lift count `N^3`, period `N ell(g)` for three content-one owners | all 96 quadrant rows satisfy the three exact integer identities; written primitivity proof checked | VERIFIED |
| P27-C-07 | L303–L350: four exact quadrants; 96 owner/level/quadrant rows; 1,248 coefficient rows through degree 12 | independent recount: 3×8×4 = 96; 3×8×4×13 = 1,248; every coefficient row marked exact | VERIFIED |
| P27-C-08 | L354–L375: all-s equality forces `c_N=1/N` and `b_N=1/N^3` | leading-exponent and leading-coefficient proof independently checked | VERIFIED |
| P27-C-09 | L383–L394: freeze, locked Round-5 inputs, validation, and core hashes | direct SHA-256 checks: `88d1…a72`, `0c74…825`, `afdc…c10`; receipt binds core `a1b5…b33` | VERIFIED |
| P27-C-10 | L392–L397: 12 tests and two isolated byte-identical builds | live verify-default Round-8 replay | VERIFIED |
| P27-C-11 | Whole historical computation chain | live discovery run: 58/58 tests pass | VERIFIED |
| P27-C-12 | L411–L425: two distinct Route-A tuples; no prime/zero tables; Route B closed | Round-7/Round-8 summaries and receipts agree; flags remain false | VERIFIED |
| P27-C-13 | L429–L435: diagnostic primitivity and full-residual-order limitations | ledger/status fields preserve loop-only and lower-bound-only semantics; no fabricated full quotient order found | VERIFIED |

Experiment/provenance boundary: **This check verifies disclosure and claim-to-provenance fidelity. It does not judge whether the experiment was correctly designed, run, statistically adequate, or reproducible by ARS.**

## Phase D — originality heuristic

Universe definition: 67 English prose blocks from Introduction through Conclusion with at least 20 lexical words, excluding front matter, declarations, references, and math-only/table-only blocks. The sample contains 21 blocks (31.3%), covers every major section, and uses exact quoted WebSearch fragments of 8–12 words.

| ID | Line / section | Exact search fragment | Originality verdict |
|---|---|---|---|
| P27-D-01 | L62 / Introduction | “Periodic-orbit constructions require an unambiguous owner. This requirement becomes nontrivial” | CLEAR — no exact match observed |
| P27-D-02 | L66 / Introduction | “The first answer is rigid. In a descending normal finite-index tower” | CLEAR — no exact match observed |
| P27-D-03 | L68 / Introduction | “The second answer requires two independent renormalizations. In a pure” | CLEAR — no exact match observed |
| P27-D-04 | L76 / Prior work | “give the standard leafwise flow framework, an explicit compact hyperbolic-lamination” | CLEAR — no exact match observed |
| P27-D-05 | L81 / Prior work | “define the punctured solenoid through finite modular covers and describe” | CLEAR — no exact match observed |
| P27-D-06 | L153 / Residual towers | “uses two quantifier changes that are easy to miss” | CLEAR — no exact match observed |
| P27-D-07 | L155 / Residual towers | “Coherence of the point also matters. A coordinate in the cover” | CLEAR — no exact match observed |
| P27-D-08 | L198 / Congruence specialization | “Direct multiplication can certify the first return but may be expensive” | CLEAR — no exact match observed |
| P27-D-09 | L223 / Cocompact control | “The image of g in integral homology is a vector” | CLEAR — no exact match observed |
| P27-D-10 | L220 / Cocompact control | “finitely generated group has only finitely many subgroups of any fixed index” | CLEAR — exact stock-theorem wording appears in [standard group-theory exposition](https://sites.lsa.umich.edu/lji/wp-content/uploads/sites/1345/2024/08/a-tale-of-two-groups.pdf); non-distinctive mathematical fact, no proprietary phrasing |
| P27-D-11 | L259 / Coefficient escape | “This theorem strengthens the owner firewall. Not only are finite-level geodesics” | CLEAR — no exact match observed |
| P27-D-12 | L263 / Coefficient escape | “Fixed-prefix convergence means that for each D, the coefficients of degrees” | CLEAR — no exact match observed |
| P27-D-13 | L271 / Homology calibrator | “Retain the same marked genus-two surface, but now define the distinct tower” | CLEAR — no exact match observed |
| P27-D-14 | L297 / Homology calibrator | “cannot be described as a renormalization of the residual inverse-limit owner” | CLEAR — no exact match observed |
| P27-D-15 | L331 / Four quadrants | “For Q00 and Q01, the first nonconstant degree is N” | CLEAR — no exact match observed |
| P27-D-16 | L352 / Four quadrants | “This panel identity is exact for every N, including N=1, but exactness” | CLEAR — no exact match observed |
| P27-D-17 | L405 / Computational certificates | “The executable certificate mirrors the proof chain. It first validates” | CLEAR — no exact match observed |
| P27-D-18 | L418 / Route-A analysis | “The pure homology-cover panel is a new candidate with new tower” | CLEAR — no exact match observed |
| P27-D-19 | L429 / Limitations | “The no-period theorem assumes a normal residual tower and one common clock” | CLEAR — no exact match observed |
| P27-D-20 | L431 / Limitations | “The renormalized identity concerns a fixed finite owner panel” | CLEAR — no exact match observed |
| P27-D-21 | L439 / Conclusion | “Residual towers erase same-owner periodicity in two compatible senses” | CLEAR — no exact match observed |

Required limitation disclaimer: **This verification report's originality check (Phase D) uses WebSearch for heuristic comparison and is not professional plagiarism detection software (such as Turnitin / iThenticate). Coverage is limited to publicly searchable literature, with a sampling rate of 31.3%, and there is a risk of missed detection. These results serve as preliminary screening; it is recommended to use professional plagiarism detection tools for complete duplicate checking before formal submission.**

## Phase E — claim verification and sidecars

### Authoritative stable-selection result

- [`stage2_5_phase_e_semantic_audit.md`](stage2_5_phase_e_semantic_audit.md) is the authoritative current Phase-E semantic audit.
- `notes/stage2_5_claim_registry.json`: 77 registered claims; 67 HIGH-IMPACT, 3 RANDOM, 0 TOP-UP, and 7 NOT-SELECTED.
- `notes/stage2_5_claim_registry_coverage.json`: 7 mechanical candidates, 0 unregistered.
- Selected distinct claims: **70/70 VERIFIED**; 0 distortion and 0 unverifiable verdicts.
- Selected tuples: **71/71 present, unique, and VERIFIED**. The tuple count exceeds the distinct-claim count because the four source-bearing claims expand to five `(claim_id, ref_slug)` tuples.
- All **71/71** persisted rows have `anchor.kind = none` and `excerpt.state = anchorless`. This is the non-gating advisory `P27-E-ADV-ANCHORLESS-1`: it limits source-excerpt replay from the receipt but does not alter the independently supported claim verdicts.
- Mechanical coverage reports zero bounded candidate gaps, while `semantic_extraction_coverage` remains `not_machine_detectable`; completeness is established only for the stable selected registry population.
- `notes/stage2_5_claim_strength_drift_findings.json`: no drift finding; status `skipped_no_revision_evidence`, appropriate because no revision-evidence bundle was supplied.

### Superseded initial snapshot retained for audit history

The earlier Phase-E pass recorded **4/4 high-impact + 7 random = 11/11 VERIFIED** and rendered the following four headline rows. That 11/11 selection and its former tier totals are retained only as historical trajectory; they are **superseded** by the 70/70-claim, 71/71-tuple audit above and must not be quoted as the current Phase-E denominator.

| Claim ID | Exact claim / TeX locator | Evidence | Verdict |
|---|---|---|---|
| P27-E1-001 | Abstract bundle: residual-tower no-period/order escape, coefficient-prefix escape, factorial control, exact `N^4/N/N^3/N ell(g)` cover data, four-quadrant result, finite/generic boundary; L47–L48 | complete written proofs; Round-4/5/7/8 ledgers; verify-default replay; receipts | VERIFIED |
| P27-E1-015 | Residual-tower theorem: no periodic point; `o_n(g)` divides `o_{n+1}(g)` and tends to infinity; L122–L129 | direct group proof at L131–L149; normality/residuality hypotheses explicit | VERIFIED |
| P27-E1-052 | Four-quadrant theorem: only simultaneous clock and multiplicity renormalization recovers the base factor at every level; L308–L310 | cover theorem, four symbolic factors, exact coefficients, all 96 quadrant rows | VERIFIED |
| P27-E1-077 | Conclusion: residual owner periodicity/finite panels escape; the separate homology calibrator succeeds only after both interventions; generic finite result gives no A2/Route-B credit; L439 | residual/prefix proofs, exact quadrants, Route summaries, explicit limitations | VERIFIED |

## Seven AI-research failure modes

| Mode | Concrete evidence | Verdict |
|---|---|---|
| 1. Implementation bugs | 58 historical tests, Round-8 12/12, exact integer coefficients, two independent order algorithms, source locks, two byte-identical builds | CLEAR |
| 2. Hallucinated citations | 5/5 entries and 5/5 contexts verified through publisher/official full text | CLEAR |
| 3. Hallucinated results | 24 congruence rows, 24 cocompact rows, 96 quadrant rows and 1,248 coefficient rows independently recounted; hashes/replay agree | CLEAR |
| 4. Research shortcuts / cherry-picking | owner panels and schedules are frozen; four quadrants include both one-intervention failures; nonarithmetic/generic control is explicit; no target data used | CLEAR |
| 5. Bug-as-insight storytelling | finite diagnostics are not extrapolated to asymptotics; full quotient orders/primitivity gaps remain labeled; positive identity is called a calibration | CLEAR |
| 6. Methodology fabrication | code, ledgers, receipts and prose agree, but no scholar-owned `experiment_intake_declaration` exists | **INSUFFICIENT EVIDENCE — BLOCKING** (`P27-S25-F001`) |
| 7. Frame lock / overclaim | distinct residual and homology-cover owners are firewalled; clock/normalization changes are explicit; convergence, growing-panel and A2 limitations are stated | CLEAR |

## Stable provisional findings

| Finding ID | Severity/status | Evidence | Required disposition |
|---|---|---|---|
| `P27-S25-F001` | BLOCKING / OPEN | Repository-wide exact search finds no `experiment_intake_declaration`; deterministic receipts cannot substitute for scholar attestation | Scholar supplies the intake declaration in the material passport/pipeline record; rerun C4/Mode 6. The agent must not author it on the scholar's behalf. |
| `P27-S25-C001` | CLOSED | Claim registry, coverage, evidence-row, drift, and semantic-audit artifacts exist; current Phase E is 70/70 claims and 71/71 tuples VERIFIED, with 0 mechanically unregistered candidates | `CLOSED_BY_CURRENT_STAGE2_5_ARTIFACT`; no action |

**Historical conclusion (superseded):** Content-integrity conclusion: **clean**, including the authoritative current Phase-E selected population. Stage-gate conclusion: **FAIL-CLOSED until `P27-S25-F001` is scholar-resolved and C4/Mode 6 are rechecked**.
