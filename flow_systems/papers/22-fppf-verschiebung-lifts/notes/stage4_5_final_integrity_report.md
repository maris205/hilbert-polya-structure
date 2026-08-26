# P22 Stage 4.5 final integrity report

Audit closure: **2026-08-25T11:56:46Z**  
Mode: **Stage 4.5 / Mode 2 / final-check**  
Human-facing verdict: **PASS WITH NOTES**  
Schema-5 machine verdict: **`PASS_WITH_CONDITIONS`**  
Checkpoint state: **STAGE 4.5 AUDIT COMPLETE; STAGE 5 ENTRY CLOSED**

The final integrity run found no SERIOUS or MEDIUM issue, no distorted or
unverifiable registered claim, no citation failure, no originality match, and
no recorded claim-strength drift.  It re-observed two MINOR issues frozen by
Stage 3-prime.  Because the pipeline's Stage-5 boundary requires a literal
zero-issue PASS (or the separately recorded exhausted FAIL-loop route), this
report does not dispatch Stage 5.  No manuscript correction was authorized or
made during this audit.

## Exact audit target

| Artifact | SHA-256 | Role |
|---|---|---|
| `paper/manuscript.tex` | `2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2` | Public final-draft source audited in every phase |
| `paper/paper.pdf` | `0ed4af9ef021876efafedf7b2457e3f371cfeb953b82c1773bcea20d8490cb8b` | Promoted Stage-4 PDF |
| `paper/references.bib` | `bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093` | Complete registered bibliography |
| `notes/stage4_revision_round1.tex` | `663ade71e41de81afd376db516ed8f548af3090cf342dd4db052eb212ce3c2d2` | Revision-bundle final-draft authority |
| `notes/stage4_revision_evidence_bundle.json` | `763f9e3cc12a8115f02a0d315dc9c74415448676c341a20e80cc0d292006f0ff` | Complete revision comparison population |
| `notes/stage4_5_input_manifest.json` | `7139194b137f40fbd4184b2f494fa78aeda5d3f6b146e799b96756ae2b79a7f4` | Authorization, frozen issues, and route boundaries |

Deleting only whole-line block-marker comments from the anchored revision
reproduces the public manuscript exactly.  The audit kept the public PDF and
all paper sources byte-identical.

## Verification summary

| Phase | Coverage | Verdict | Fresh result |
|---|---:|---|---|
| A. Reference existence and metadata | 3/3 references | **PASS** | Every registered source was re-opened from scratch; identity, metadata, version state, and locators matched. |
| B. Citation-context fidelity | 21/21 `\cite` commands in 14 paragraph blocks | **PASS** | Zero orphan entries, dangling keys, locator errors, compound-attribution errors, or source-fidelity distortions. |
| C1. Statistical/data accuracy | 0 registered surfaces | **NOT APPLICABLE** | The denominator is genuinely zero for this theoretical paper. |
| C2. Internal consistency | 16 families; 14 clean | **PASS WITH 2 MINOR ISSUES** | The theorem, proof, topology, extension, source-correction, metadata, and public/anchored-source families agree; chronology and materials status remain open. |
| C3. Figure/table fidelity | 0 figures, 0 tables, 0 captions | **NOT APPLICABLE** | No Figure Package or trace entry is required. |
| C4. Experiment provenance | 1/1 declaration; 0 experiment claims | **PASS** | Scholar-supplied `no_experiments_declared` agrees with empty provenance/alignment arrays and manuscript wording. |
| D1. Originality | 37/74 body paragraphs = 50.0% | **NO BLOCKING SIGNAL** | 29 ORIGINAL, 8 COMMON_KNOWLEDGE, and zero PARAPHRASE, CLOSE_MATCH, or VERBATIM rows. |
| D2. Self-reuse | Reliably linked public subset | **LIMITED, NO ACTIONABLE SIGNAL** | No self-reuse match was identified; common-name disambiguation and an incomplete public corpus prevent a `CLEAN` determination. |
| D3. AI-writing heuristics | 6 indicators | **BELOW ALERT THRESHOLD** | One formulaic-transition indicator; this is not an authorship classifier. |
| E. Registered-claim verification | 49/49 claims; 63 evidence rows | **PASS** | 49 VERIFIED, zero MINOR/MAJOR distortion, zero unverifiable/access failure. |
| E4. Scope conformance | 49/49 registered claims | **PASS** | No scope-broadening advisory; the all-index and finite-flat branches are authorized, evidence-backed comparators. |
| E5. Primacy/absence wording | 1 bounded negative search observation | **SUPPORTED WITHIN SEARCH** | The paper records surfaces, queries, cut-off, inclusion rule, and nearest work and expressly disclaims global priority. |
| E6. Claim-strength drift | 13/13 revision operations | **NO RECORDED FINDING** | **None detected by the recorded semantic review.** This is not a deterministic completeness certificate. |

Phase A/B used primary or official records.  Deninger's v1 source remains the
exact cited arXiv object; Deninger--Mellit's formal metadata agrees with the
EMS record; and each cited Stacks Tag remains live.  The source-fidelity PASS
does not claim that external sources prove this manuscript's counterexample or
nonlift theorem.

## Phase E machine receipt

- `claim-registry/1.0`: 49 exact UTF-8 byte-bound rows, all
  `selection_tier=ALL`; SHA-256
  `b5a62ee06844eff8c5f5aeec6fb73090cef998373d73c64917cd9f237cb81954`.
- `claim-registry-coverage/1.0`: build and exact-input replay PASS; SHA-256
  `7da7d0b6c1f1f4696928f6789fda818cac1b75266b253aa0d53d48779b9f0bee`.
- The coverage detector returned 10 mechanical candidates, four exact
  registry-span matches, and a raw `candidate_unregistered_count=6`.  Semantic
  adjudication identified the six raw gaps as two LaTeX macro parameters and
  four incomplete formula/physical-line fragments.  The raw count is retained,
  and `semantic_extraction_coverage=not_machine_detectable` remains mandatory.
- `evidence-row/1.0`: 63 ordered persisted rows covering all 49 distinct
  claims; exact source-map replay PASS; SHA-256
  `492412e025acf88ffbbe44f78379b936e8e0281c35cf5e54f717f610975fa3df`.
- `claim-strength-drift-findings/1.0`: completed, exact draft/bundle bindings,
  and `findings=[]`; SHA-256
  `87dbff3aa4cd7533b18bd26f05bd665cd6dfe875573537a02e2fe0f8b8e797a8`.
- Full Schema-5 machine handoff, including every evidence row:
  `notes/stage4_5_integrity_report.json`; SHA-256
  `f1e2a18e082fe1b226df7ad15b4b405e508b4409f25be06c360d59c7fa37441d`.

The machine handoff was parsed as JSON and replay-validated by the ARS
evidence-row consumer: `PASS: 63 evidence row(s)`.  Evidence rendering remains
paginated at 25 rows per page; this summary does not manually reformat or
truncate the persisted array.

## Originality and self-reuse boundary

The Mode-2 denominator is 74 body paragraphs.  The final sample contains 37
paragraphs, covers every major numbered section, and includes all 12/12 newly
added or substantially replaced Stage-4 body paragraphs.  The three modified
declarations and the modified title/byline metadata block were checked in
addition to the body denominator.

The author-aware screen used exact email/affiliation/ORCID links where
available and excluded ambiguous name-only records.  No current characteristic
fragment matched the reliably linked prior-work subset.  The result is not
labelled `CLEAN`: there is no authoritative complete publication list in the
audit inputs, paywalled or unindexed texts may be absent, and cross-language
reuse is difficult to detect.

> This originality check uses public Web search for heuristic comparison, not
> Turnitin, iThenticate, or publisher similarity software.  It cannot provide a
> reliable global overlap percentage.  Professional similarity screening
> remains recommended before formal submission.

## Seven AI-research failure modes

| Mode | Integrated Stage-4.5 status | Evidence boundary |
|---|---|---|
| 1. Implementation bug passing self-review | `CLEAR` | No implementation, numerical result, or experiment/code-backed claim exists. |
| 2. Hallucinated citation | `CLEAR` | The independent originality subaudit left this outside its task, but the integrated fresh Phase A/B run verified all 3 references and all 21 citation contexts. |
| 3. Hallucinated experimental result | `CLEAR` | Explicit no-experiment declaration; zero empirical/data surfaces. |
| 4. Shortcut reliance | `CLEAR` | No learned model, dataset, performance task, or generalization experiment exists. |
| 5. Bug reframed as novel insight | `CLEAR` | The implementation surface is absent and no surprise narrative was found. |
| 6. Methodology fabrication | `CLEAR` | No experimental Methods/configuration surface exists; this does not certify the mathematical proof. |
| 7. Early frame-lock | `INSUFFICIENT EVIDENCE — WARNING` | Current artifacts establish internal coherence but do not fully reconstruct the author's counterfactual Stage-1 choice. No `SUSPECTED` signal was found. |

There are zero `SUSPECTED` modes.  Mode 7 is one of the protocol's
warning-eligible insufficient-evidence classes and does not create a hard
integrity block.  It remains visible rather than being silently promoted to
`CLEAR`.

## RAISE principles-only compliance

The Schema-12 report is valid and is appended to the Material Passport.
Because this is primary theoretical research rather than evidence synthesis,
RAISE is used only as an ARS principle extension; the result is not a claim of
official RAISE compliance.

| Principle | Recorded status | Main gap |
|---|---|---|
| Human oversight | `fail` | No reviewer count, qualifications, or adjudication procedure is reported. |
| Transparency | `fail` | Tool/model/version, prompt, parameter, and per-stage tool metadata are incomplete. |
| Reproducibility | `fail` | `repro_lock=null`; equivalent configuration/stochasticity archive and public-access closure are absent. |
| Fit for purpose | `fail` | No per-tool rationale, pilot check, validation reference, or task-specific performance evidence is reported. |

Primary-research routing caps these principle results at
`overall_decision=warn`; they are compliance/readiness advisories, not Stage-4.5
SERIOUS or MEDIUM findings.  The compliance artifact SHA-256 is
`1dfd3a71cd164de62057c504e080c5f2be94543cfcfe2e8ac26aff3a4dca4835`.

## Revision-strength and token advisories

The independent E6 review replayed the complete bundle before inspecting all
13 operations.  It recorded no `ADV-E6-*` finding and therefore requires no
author disposition.  The deterministic token checker did emit four
non-gating advisories:

1. B0022: proposition/page/Tag locators and the bounded-search date/window.
2. B0023: formal exact-sequence zeroes, `z_0`, and the target constant `1`.
3. B0092: the explicit theorem bound `N>1`.
4. B0005: affiliation label, street number, and postal code.

Each was semantically inspected against its specific roadmap authorization.
None was converted into a scientific-strength finding or an inferred author
disposition.

## Isolated build and public-artifact integrity

The exact manuscript and bibliography were rebuilt in an isolated temporary
directory with LuaLaTeX, BibTeX, and two final LuaLaTeX passes.  The fresh
output is 13 A4 pages with 21 citation commands and three bibliography entries;
there are zero unresolved citations/references, overfull boxes, missing glyphs,
or fatal errors.  Nine of nine fonts are embedded/subset.  Two pre-existing
underfull notices remain in the manually line-broken Chinese abstract.

The fresh PDF SHA-256 is
`cd01954347c0b29356d3c5c23167211b678118acde96f3b1c5861870a5ace593`.
Binary identity is not expected because PDF build timestamps differ, but the
fresh and promoted `pdftotext -layout` outputs are byte-identical at SHA-256
`070afd082737f6cfa13de4bfec32b30607896e97e8f928ecd2094c8d401eaf0c`.
No build output was promoted during Stage 4.5.

## Open issue list

### MINOR (recommended correction)

| ID | Frozen source | Location | Issue | Required author-side resolution |
|---|---|---|---|---|
| `IL-MINOR-1` | `NEW-1` (`regression`) | Title date and Introduction search record | `Draft of 24 August 2026` coexists with an update completed 25 August 2026. | Synchronize the displayed date or explicitly explain the chronology. |
| `IL-MINOR-2` | `NEW-2` (`previously_missed`) | Data and materials availability | Public-access status is still deferred to later author confirmation. | Supply an explicit author-owned public-availability decision and then finalize the wording. |

Overall issue counts: **SERIOUS 0 / MEDIUM 0 / MINOR 2**.  Neither issue is
upgraded, omitted, or treated as already corrected.  The audit has no authority
to choose the materials-access policy for the author.

## Material Passport receipt

The orchestrator appended the validated Stage-4.5 Schema-12 compliance entry
without overwriting the Stage-2.5 history and updated the passport's current
content binding to the exact audited manuscript.  Current passport:

- `verification_status=VERIFIED`;
- `version_label=p22-stage4.5-verified-with-notes-v1`;
- `integrity_pass_date=2026-08-25T11:56:46Z`;
- `content_hash=2e8a6872eabb512dbd7ef04f5be933717a472c931199b9be509cb654599d4da2`;
- SHA-256
  `004f73185723d519d1c6ab22a4888324856d01554ed8c91efabb0354a4658d7b`.

`VERIFIED` records the exact audit binding.  It does not override the separate
zero-issue Stage-5 entry rule recorded below.

## Governing route-map crosswalk

The two user-designated roadmap files remain the governing route definitions:

- Route A v0.2.0 SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- Route B v0.2.0 SHA-256
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

```text
ROUTE_A_EVALUATION=NOT_TESTABLE
A0_A1_A2_A3_A4_TUPLE=NOT_ASSIGNED
ROUTE_A_ADVANCEMENT=NONE

ROUTE_B_INVOCATION_ALLOWED=false
ROUTE_B_ENTRY_AUTHORIZED=false
ROUTE_B_STATUS=ROUTE_B_NOT_TESTABLE
B1_B2_B3_B4_B5_TUPLE=NOT_ASSIGNED
HILBERT_POLYA_CLAIM_ALLOWED=false

GATE_A=NOT_REACHED
GATE_B=NOT_REACHED
GATE_C=NOT_REACHED
GATE_D=NOT_REACHED
GATE_E=NOT_REACHED
```

This correspondence is deliberate: P22 is a pure algebraic/sheaf-theoretic
obstruction paper and supplies no Route-A dynamical candidate, arithmetic
orbit ledger, determinant convention, or Route-B Hilbert space/operator/domain.
It therefore receives no Route/Gate credit and is not used to rescue or infer a
Route candidate.

## Mandatory checkpoint

Stage 4.5 auditing is complete and stops here.  The current paper is a concrete
13-page research-paper deliverable with a fully replayable integrity record,
but the Stage-5 entry gate remains closed because `IL-MINOR-1` and
`IL-MINOR-2` are open.  The next lawful path is a separately authorized narrow
correction round followed by a fresh Stage-4.5 re-verification.  Until that
authorization is received, there is no manuscript edit, Stage-5 dispatch,
submission, public release, author contact, Git action, cross-model upload, or
Route advancement.
