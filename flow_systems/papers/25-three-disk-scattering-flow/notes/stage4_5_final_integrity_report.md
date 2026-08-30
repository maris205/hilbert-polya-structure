# Paper 25 Stage 4.5 final integrity report

Audit closure: **2026-08-30T12:39:43Z**  
Mode: **Stage 4.5 / Mode 2 / final-check**  
Human-facing verdict: **HOLD FOR EXACT MINOR BIBLIOGRAPHY CORRECTIONS**  
Schema-5 machine verdict: **`PASS_WITH_CONDITIONS`**  
Checkpoint state: **STAGE 4.5 AUDIT COMPLETE; STAGE 5 ENTRY CLOSED**

The fresh five-phase audit found no SERIOUS or MEDIUM issue, no unsupported
citation context, no distorted or unverifiable registered claim, no
experiment/result mismatch, and no recorded claim-strength drift. It found
four MINOR bibliography controls: two published-erratum disclosures, one issue
number, and one authoritative author-initial normalization. The corrections
do not require a manuscript-claim rewrite, but the zero-issue Stage-5 boundary
means the paper stops at the mandatory correction checkpoint.

No proposed patch was applied. The current draft, canonical manuscript,
bibliography, PDF, canonical results, initial dynamical-system restrictions,
and Route records remain unchanged.

## Exact audit target

| Artifact | SHA-256 | Role |
|---|---|---|
| `notes/stage4_revision_round1.tex` | `39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835` | Sole current Stage-4.5 manuscript target |
| `paper/manuscript.tex` | `283695c485a2a48abfab1ef0fe3d479f597f68f3082e20f4a5a1894ca37baefb` | Frozen canonical manuscript; not promoted |
| `paper/references.bib` | `de776cc0bf16e6c837917f4a289f8c07b8b4f7e9146183b9a9e0e6294db99e6b` | Frozen canonical bibliography |
| `notes/stage4_revision_evidence_bundle.json` | `bf368e5757d30bf182eca18fe574814ecc11e750f5060b528bd1022b68b9fd51` | Complete Stage-4 comparison population |
| `notes/stage4_5_input_manifest.json` | `1e920cc6593fba373f5aa8e158bc0a292d5c0fd59a51f9cfb5c0b22fba6bc0e3` | Audit authority, inputs, populations, and Route boundary |

The generic event `确认，继续下一轮` authorized the fresh audit and preparation
of the next lawful control artifacts. It did not authorize any exact
bibliography correction, Stage-5 dispatch, canonical promotion, result refresh,
or Route mutation.

## Verification summary

| Phase | Coverage | Verdict | Fresh result |
|---|---:|---|---|
| A. Reference existence and metadata | 8/8 references | **PASS WITH 4 MINOR CONTROLS** | All works and identities verified; two errata need disclosure, one issue number and one author field need normalization. |
| B. Citation-context fidelity | 13/13 citation commands | **PASS** | All contexts supported; zero distortion, unverifiable context, dangling key, or orphan entry. |
| C1. Data and numerical accuracy | 8 checked data/result families | **PASS** | 2,241 rows, 747 per geometry, 3 matches and 744 disagreements per geometry, six exact witnesses, 68-file lock, and 75/75 tests replayed. |
| C2. Internal consistency | 18/18 named families | **PASS** | Theorems, exact witnesses, object typing, declarations, experiment scope, and Route boundaries agree. |
| C3. Figure/table fidelity | 0 figures; 2/2 tables | **PASS** | The conceptual taxonomy and all 12 displayed replay cells were traced. |
| C4. Experiment provenance | 1 scholar declaration; 6/6 claims | **PASS WITH BOUNDARY** | All registered experiment claims align; historical provenance remains labelled retrospective and the computation remains validation-only. |
| D1. Originality | 45/74 body paragraphs = 60.8% | **NO BLOCKING SIGNAL** | 38 no-indexed-exact-match and 7 common-knowledge grades; zero paraphrase, close-match, or verbatim findings. |
| D2. Stage-4 changed prose | 17/17 paragraphs | **CHECKED** | Every new or substantially replaced Stage-4 body paragraph was included. |
| E1. Claim Registry | 114/114 `ALL` claims | **PASS FOR FROZEN POPULATION** | Five official mechanical candidates matched exact registry spans; `candidate_unregistered_count=0`. Semantic extraction completeness remains not machine detectable. |
| E. Claim/source verification | 114/114 claims; 127 rows | **PASS** | Every persisted row is source-bound and `VERIFIED`; zero anchorless rows and zero distortions. |
| E6. Claim-strength drift | Complete Stage-4 bundle | **NO RECORDED FINDING** | `findings=[]` in the recorded model-mediated review; this is not a deterministic completeness guarantee. |

## Phase A/B source boundary

All eight bibliography records were rechecked against current DOI metadata and
official publisher, society, repository, or author-hosted primary records.
Reverse update queries were also used for correction status. Both Gaspard--Rice
errata affect formulas or local wording in the source articles, but the three
manuscript contexts use broader determinant/resonance statements and remain
supported. The audit does not treat any external source as proving this
paper's new two-witness theorem, minimax bound, replay, or Route tuple.

The complete source and context ledger is
`notes/stage4_5_reference_citation_audit.md`, SHA-256
`891a027ca49c7e8fbab8244ed4abc8f98630a7ca41b872e814ddb42f44f647b7`.

## Phase C experiment and build replay

The fresh replay read committed carriers rather than copying prose values:

- `results/round8_physical_roof_replay.csv` contains 2,241 data rows: 747 for
  each frozen no-eclipse geometry `d/a=29/5, 6, 31/5`;
- each geometry has three period-two matches and 744 disagreements under its
  period-two-frozen scalar clock;
- `results/round8_exact_roof_witnesses.csv` contains six exact witnesses;
- all three declared Round-8 result hashes match the Stage-4 receipt;
- the current reproducibility lock contains 68 files;
- `bash experiments/reproduce_stage4.sh` passed all 75 tests, reproduced the
  isolated core outputs, reported no canonical-result modification, and
  reported no scientific-value change.

These are deterministic finite-cutoff validation surfaces, not 2,241
statistically independent observations and not an additional proof of roof
noncohomology. The exact theorem rests on the two symmetric orbit witnesses.

A marker-stripped isolated build produced 13 A4 pages with no undefined
citation/reference, missing glyph, fatal error, or overfull box. Consecutive
PDF bytes differ because volatile metadata is embedded, so no byte-reproducible
PDF claim is made. No build output was promoted.

## Phase D originality and self-reuse boundary

The deterministic sample covers 45 of 74 current English body paragraphs,
every major numbered section, all 17 current Stage-4 new or substantially
replaced body paragraphs, all current declaration paragraphs, and the
title/byline/affiliation/email metadata. Quoted 8--12-word characteristic
fragments were screened on the public Web and inspected for actual textual
overlap rather than shared mathematical vocabulary.

The result is a bounded heuristic screen: 38 sampled paragraphs had no indexed
exact match and seven contained common formula-adjacent terminology; zero were
graded paraphrase, close match, or verbatim. Author-aware searches found no
actionable match in the searchable linked subset, but the audit lacks an
authoritative complete publication corpus.

> This is not Turnitin, iThenticate, publisher similarity software, or a
> reliable global-overlap percentage. Professional similarity screening
> remains recommended before formal submission.

## Phase E machine receipt

- `claim-registry/1.0`: 114 exact UTF-8-bound claims, all
  `selection_tier=ALL`; SHA-256
  `9e333277db2225c1e9d68afadb1c55acdb7845a28a72cb896aca8bef0cd8b90b`.
- `claim-registry-coverage/1.0`: five official mechanical candidates, five
  exact full-span matches, zero unregistered candidates; SHA-256
  `d8f9343806bbf42846f204a45a04ad4c7c07ae2eb7af3d5779da0d8b3cf61098`.
- Semantic census: 116 anchored blocks inspected, 29 purely structural blocks
  excluded, and the remaining complete current claim population frozen at 114.
  `semantic_extraction_coverage=not_machine_detectable` remains mandatory.
- `evidence-row/1.0`: 127 persisted, source-bound, `agent_extracted` rows
  covering all 114 claims; 114 use the frozen local artifact chain and 13 use
  current Stage-4.5 citation-audit carriers; SHA-256
  `752504e737d4162dff1e189c878f4c1492054207cbd36752dfc6ff86cacce146`.
- Evidence source map: nine sources; SHA-256
  `2134ef5b70b85d93882a6d9616c7e2d4e9e45566186525b245b096ecfe9bd711`.
- The evidence-row `captured_at` value is a frozen evaluator extraction event,
  not a deterministic build timestamp. Replay validates and reuses the exact
  persisted row bytes; it does not mint a new timestamp and silently rebind
  downstream hashes.
- `claim-strength-drift-findings/1.0`: `status=completed`, exact draft and
  revision-bundle bindings, `findings=[]`; SHA-256
  `f618185110e7264805743072b4f866eb85db1b4eced4e50ed9f755a4572bc644`.
- Full Schema-5 handoff, including all 127 evidence rows:
  `notes/stage4_5_integrity_report.json`; SHA-256
  `e46f58d5d1fcfcb6786fd11b006587f62350965aa35d326cef21fffa05b854e4`.

The official claim-coverage replay and evidence-row/source-map validation pass.
The Stage-4 bundle validator also passes. The deterministic token checker
reports `conserved=false` with four advisories, each semantically attributable
to authorized new citations, numbers, layout/object labels, or environment
pins. The independent E6 review did not convert them into a drift finding.
That semantic empty finding set is not a proof that all possible strength drift
is mechanically detectable.

## Seven AI-research failure modes

| Mode | Integrated status | Boundary |
|---|---|---|
| 1. Implementation bug passes self-review | `CLEAR_AFTER_REPLAY` | 75/75 tests, fail-closed tamper checks, 68-file lock, and isolated rebuilds passed; this does not prove absence of every bug. |
| 2. Hallucinated citation | `CLEAR_CONTEXT_WITH_MINOR_METADATA_HOLD` | 8/8 works and 13/13 contexts verified; four bibliography controls remain open. |
| 3. Hallucinated experimental result | `CLEAR_AFTER_DECLARATION_AND_REPLAY` | 6/6 registered experiment claims align and fresh replay reproduces the declared counts. |
| 4. Shortcut reliance | `CLEAR_WITH_SCOPE_BOUNDARY` | Exact theorem uses two symmetric witnesses; 2,241-row computation is validation-only. |
| 5. Bug reframed as novel insight | `CLEAR` | The theorem-level result is solver-independent and no failed implementation is narrated as the contribution. |
| 6. Methodology fabrication | `CLEAR_FOR_DECLARED_FINITE_REPLAY` | Source, environment, lock, tests, outputs, receipts, and limitations exist; no undeclared global determinant/asymptotic experiment is certified. |
| 7. Early frame-lock | `INSUFFICIENT_EVIDENCE_WARNING` | Alternative objects and negative controls are explicit, but artifacts cannot reconstruct every counterfactual Stage-1 choice. |

There are zero `SUSPECTED` modes. Mode 7 remains a visible warning rather than
being silently promoted to `CLEAR`.

## RAISE principles-only advisory

The Schema-12 compliance extension validates and records
`overall_decision=warn`. It applies RAISE principles only as a transparency
extension to primary mathematical/computational research; it is not a claim of
official RAISE compliance and does not replace the independent integrity gate.

All four principles remain `fail` with material gaps: named qualified human
review/adjudication is not documented; complete historical tool/model/prompt/
parameter metadata is unavailable; retrospective provenance cannot become a
contemporaneous preregistration; and no external task-specific benchmark or
per-tool selection rationale proves full fit for purpose. The validated
artifact is `notes/stage4_5_compliance_report.json`, SHA-256
`3873ec3b2b46c5f0079144c7aba8aecb251336d015ebaf3da89bbd8aa1324154`.

## Open MINOR correction list

| ID | Reference | Exact target/operation | Required narrow correction |
|---|---|---|---|
| `IL-MINOR-1` | `GaspardRice1989Semiclassical` | `B0001/replace_block` | Add published erratum DOI `10.1063/1.457672`. |
| `IL-MINOR-2` | `GaspardRice1989Exact` | `B0002/replace_block` | Add published erratum DOI `10.1063/1.457670`. |
| `IL-MINOR-3` | `Ruelle1976` | `B0006/replace_block` | Add `number = {3}`. |
| `IL-MINOR-4` | `Livsic1972` | `B0008/replace_block` | Normalize the author to `Liv\v{s}ic, A. N.`. |

Overall issue counts: **SERIOUS 0 / MEDIUM 0 / MINOR 4**. Reference existence
and citation support pass; these four rows remain open because exact correction
authority has not been supplied.

Byte-bound control artifacts:

- correction list SHA-256:
  `f25c80eae179acd0f50d948447000f775575a0c962ea9de3627c87d6d9c217c7`;
- exact proposed patch SHA-256:
  `c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc`;
- exact authorization request SHA-256:
  `72743007c76cff3079252f00ba23c64b4aa810f095b743c37552ed7e5567243e`.

The patch schema, base hash, old hashes, targets, correction-list binding, and
structural analysis pass. It touches 4/8 bibliography blocks, ratio `0.5 <
0.6`, with no structural flag. It remains unapplied.

## Material Passport state

The Stage-4.5 passport binds the exact current draft, appends the validated
compliance history, preserves the six experiment ClaimIntents and seven
historical provenance entries, and records the four-MINOR hold. Its state is:

- `verification_status=UNVERIFIED`;
- `version_label=p25-round9-stage4.5-round1-four-minor-hold-v1`;
- `integrity_pass_date` is absent;
- `content_hash=39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835`;
- SHA-256
  `f261c7a68d3b669301195950499fa6c92920078044984837fe2410fe7f171a6e`.

`UNVERIFIED` is an honest gate state, not a finding that the paper's scientific
claims failed. It records that a zero-issue Stage-4.5 pass has not yet been
obtained.

## Governing Route crosswalk

The two user-designated roadmap definitions remain controlling:

- Route A v0.2.0 SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- Route B v0.2.0 SHA-256
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

```text
PHYSICAL_OBJECT=no-eclipse equilateral three-disk scattering flow
FROZEN_GEOMETRIES=d/a in {29/5, 6, 31/5}
PHYSICAL_FLOW_ROUTE_A_TUPLE=UNASSIGNED

SYMBOLIC_CALIBRATOR=separately typed unit-roof q-symbol no-repeat suspension
SYMBOLIC_ROUTE_A_TUPLE=(A0_FAIL,A1_PASS_ANALYTIC,A2_ANALYTIC_DETERMINANT,A3_FAIL,A4_FAIL)
SYMBOLIC_ROUTE_A_OVERALL=ROUTE_A_REJECTED

ROUTE_B_INVOCATION_ALLOWED=false
ROUTE_B_STATUS=UNINVOKED
STAGE4_5_GATE_CREDIT=NONE
HILBERT_POLYA_CLAIM_ALLOWED=false
```

The unit-roof determinant remains a negative analytic calibrator and cannot be
transferred to the physical nonconstant-roof flow. Stage 4.5 improves integrity
traceability only; it does not change A0--A4, invoke Route B, or advance any
Gate A--E milestone.

## Mandatory checkpoint

Stage 4.5 auditing is complete and stops here. The lawful next step is a
separately authorized four-operation bibliography correction, followed by
patch validation/application to the anchored working copy and a fresh Stage
4.5 re-verification. No direct edit of `paper/references.bib`, Stage-5 dispatch,
canonical promotion, result refresh, manuscript-claim rewrite, or Route change
is authorized at this checkpoint.

Exact copy-paste authority is recorded in
`notes/STAGE4_5_INTEGRITY_CORRECTION_AUTHORIZATION_REQUEST.md`:

> 我确认并授权 Paper 25 Stage 4.5 bibliography integrity correction patch，revision patch SHA-256 c135b935ff154a9dd946f1bb9652e514ebae0cf82dc7894149a2b6872bc0cffc；IL-MINOR-1 authorize B0001/replace_block；IL-MINOR-2 authorize B0002/replace_block；IL-MINOR-3 authorize B0006/replace_block；IL-MINOR-4 authorize B0008/replace_block。授权仅限上述 exact patch、targets 与 operations；不授权 collateral edits、claim-strength changes、canonical results refresh、正文修改或 paper/references.bib 在本授权步骤中的直接修改。若 hash/precondition/validator 失败、出现 structural flag 或需超出 scope，停止并请示。
