# Round 10 Stage 2.5 — Originality and Failure-Mode Reconnaissance (Working)

Audit continuation date: **2026-09-03 UTC**  
Scope: **Papers 29--33, read-only reconnaissance**  
Disposition authority: **none**

## Scope, freezes, and limitations

This sidecar reports manuscript-language triggers, the seven ARS AI-research
failure-mode surfaces, local exact-phrase overlap, and the already frozen
candidate paragraphs for the minimum 30% originality sample. It does not
declare a paper original, clear a final Stage-2.5 gate, infer a scholar's
experiment declaration, alter a manuscript or bibliography, run science, or
evaluate Route A or Route B.

| Frozen/control artifact | SHA-256 |
|---|---|
| `BATCH_ROUND10_STAGE2_5_INPUT_FREEZE.json` | `8da3f9b70f09d0f7555ce3e233eeddb81c7250b726a8871d0f76fa2aa053907e` |
| `BATCH_ROUND10_STAGE2_5_ORIGINALITY_PRECOMMITMENT.json` | `01f7ffb11ad935cb08a2a1017e0599a32647e4b5bfdaabeae7359733a7d49f44` |
| `BATCH_ROUND10_STAGE2_5_EXPERIMENT_INTAKE_REQUEST.md` | `48374f70e9e4780897a95ed519a54ed4259a7209f833dee0128103d53fe21397` |
| deterministic originality tool | `38552118fe2da81ef20c50392be29cfb708726b1538f0e426115f0d716dc5e19` |

The exact-overlap pass is a local deterministic heuristic, supplemented by
bounded WebSearch identity reconnaissance. It is not Turnitin, iThenticate, or
an exhaustive multilingual/paywalled similarity search. The candidate
paragraphs still have `search_status=PENDING_WEBSEARCH` and `verdict=PENDING`
in their frozen sample files.

## Frozen paper and candidate-sample accounting

The sampling denominator is prose from the first numbered section through the
last numbered section before declarations. Eligible paragraphs are
double-newline prose blocks with at least 12 alphabetic words; declarations,
the duplicate Chinese abstract, pure markup, and tables are excluded. The rule
represents every major numbered section, then selects by deterministic SHA-256
rank to `ceil(30%)`.

| Paper | Frozen manuscript SHA-256 | Eligible body paragraphs | Candidate paragraphs | Rate | Candidate artifact SHA-256 |
|---|---|---:|---:|---:|---|
| P29 | `5bee689a055f99819fb6df1f6e992610fe0dea7ebffc87219758116bf06bd034` | 75 | 23 | 30.67% | `21d6b12fb47938c7d71965902eb284c782d7b381b4a0fcb88c95181aa15c1264` |
| P30 | `af270bc06a3f1e00d657fdc875585e3da9ab9b2b7198ad8d096d188a93af9506` | 87 | 27 | 31.03% | `74dc3cdf07421677d8584ea1ae53e56163e931225d28ef7f95e1d074f6a3b7c2` |
| P31 | `6023a33a4679a79c7c6cc8be8cf4345813a564b2fd420770618e7afa9547206a` | 67 | 21 | 31.34% | `ba936f85dbe85917b88e41292ef0f92546c997235dab5acf0e222255af9026f0` |
| P32 | `246545c14b5d7c3e43f7aad8b421b254ded52bf82efc1182b4c4bfe3ef6232c9` | 77 | 24 | 31.17% | `5240fb65f44e021b0e8b1fdb4262b5b2c7b78ad13dcecc7ed4bc7d02dfb7f700` |
| P33 | `b407441c07091ad38fb7e918721d31d2c4e3d897db9a705d92d9ff1f231f96d3` | 68 | 21 | 30.88% | `2da1096385d76947bab31b0f912dd6b25abf9834edabeeb5531b29243c3e58cb` |
| **Batch** | -- | **374** | **116** | **31.02%** | -- |

The five JSON artifacts enumerate every candidate by sample ID, manuscript
line, major section, paragraph SHA-256, and exact search fragment. All major
numbered sections in every paper are represented. These are candidates for
the protocol's external originality check, not completed originality verdicts.

## Own-experiment and own-result language scan

The manuscripts distinguish completed literature/workflow operations from
prospective scientific operations. The following are textual observations;
they do **not** substitute for the scholar declaration requested in the frozen
experiment-intake form.

| Paper | Positive executed-language surface | Explicit scientific nonexecution surface | Reconnaissance reading |
|---|---|---|---|
| P29 | lines 165--171 report the completed bounded literature workflow and its record counts | lines 169 and 181 state that no scientific artifact, experiment, numerical/algebraic computation, formula, quotient ledger, table, or receipt was created; lines 287--290 repeat the availability boundary | Workflow-result language is present; no own scientific experiment/result claim was found. |
| P30 | lines 201--209 report the completed literature workflow and correction bindings | lines 207 and 217 state that no scientific artifact/result or physical/operator/determinant computation was created; lines 346--349 repeat the boundary | Workflow-result language is present; no own scientific experiment/result claim was found. |
| P31 | lines 263--278 identify literature synthesis as the only executed research method | lines 724--729 deny a canonical form, owner partition, pair audit, theorem, computation, or estimand; lines 753--757 and 763--771 deny solver/science output | Workflow-result language is present; no own scientific experiment/result claim was found. |
| P32 | lines 286--322 describe literature and project-record synthesis; lines 335--340 identify logical comparison as the executed analytical operation | lines 335--340 and 779--785 deny experiment, factor/panel/limit computation and scientific result; lines 809--813 and 819--829 repeat the data/AI boundary | Workflow/design-result language is present; no own scientific experiment/result claim was found. |
| P33 | line 29 records `SCIENTIFIC_EXECUTION=NOT_RUN`; lines 198--205 describe the staged literature investigation | lines 205 and 581 deny an experiment, scientific computation/output, census, validator, fixture, or canonical refresh | Workflow/design-result language is present; no own scientific experiment/result claim was found. |

The bibliography-entry counts independently agree with the manuscript source
inventories: P29/P30/P31/P32/P33 = **22/26/22/26/20**. A batch search for
`surprisingly`, `unexpectedly`, `counterintuitively`, `contrary to`,
`we discovered`, `novel insight`, and `novel finding` returned **zero** hits.
These checks reduce textual triggers but cannot establish who executed or did
not execute an experiment. The intake remains a scholar-controlled gate.

## Seven ARS AI-research failure modes

The labels below are reconnaissance labels, not final `CLEAR` dispositions.

| Mode | Reconnaissance finding | Non-final status |
|---:|---|---|
| 1. Implementation bug passing AI self-review | No manuscript reports project scientific code, a solver run, or a computed scientific result. Only literature/workflow counts and design artifacts are represented as executed. No implementation was inspected or run in this task. | `NO_MANUSCRIPT_TRIGGER_FOUND`; implementation-level clearance is not asserted. |
| 2. Hallucinated citation | P33 received a separate 20/20 reference replay and an 18/48 context audit: 19 records verified within bounded/year-variant metadata, P33-S06 conservatively retained as `PLAUSIBLE`, zero ghost records, and 18/18 sampled contexts faithful within stated boundaries. P29--P32 are outside this P33 Phase-A/B sub-audit. | `P33_PASS_WITH_BOUNDARIES`; no batch-wide Mode-2 clearance from this sidecar. |
| 3. Hallucinated experimental result | No own scientific experiment/result assertion was found; the manuscripts repeatedly deny science execution. This is a text scan only and the scholar's experiment declaration is deliberately not inferred. | `NO_MANUSCRIPT_TRIGGER_FOUND`; D7/intake remains pending outside this sidecar. |
| 4. Shortcut reliance | No trained model, benchmark, performance metric, finite scientific panel result, or optimization result is reported. Prospective finite panels and scores are framed as forbidden or future work. | `NOT_APPLICABLE_TO_REPORTED_SCIENCE`; no future implementation clearance. |
| 5. Implementation bug reframed as novel insight | The surprise/novelty trigger scan returned zero; each paper expressly limits its contribution to synthesis or design and denies a scientific finding. | `NO_MANUSCRIPT_TRIGGER_FOUND`; no code-level inference. |
| 6. Methodology fabrication | The executed methods are described as literature synthesis/revision operations; their source totals match the five current bibliographies (22/26/22/26/20). No scientific method is represented as executed. | `NO_SCIENCE_METHOD_TRIGGER_FOUND`; full provenance replay remains outside this reconnaissance. |
| 7. Frame-lock at an early pipeline stage | The texts expose rather than conceal their locked frames and failure states. P33 expressly records the target/control cutoff asymmetry and systolic confounding; P31/P32 state their formal objects and Route tuple remain unresolved. | `DISCLOSED_LIMITATION_FOUND`; this is not a substantive Route or scientific adequacy verdict. |

No `SUSPECTED` trigger was found by this bounded manuscript-language scan.
That statement must not be promoted into a final seven-mode clearance without
the remaining source, provenance, originality, and scholar-controlled checks.

## Cross-paper exact-phrase reuse

The deterministic body scan compared all ten Round-10 paper pairs at an
eight-normalized-word reporting threshold.

| Pair | Maximum exact run | Human reconnaissance classification |
|---|---:|---|
| P29--P30 | 18 words | Repeated frozen-artifact/review-workflow list; project-specific provenance boilerplate, not a substantive mathematical result. Retain for transparency. |
| P29--P31 | 10 words | Mandatory Route-A status language. |
| P29--P32 | 10 words | Mandatory Route-A status language. |
| P31--P32 | 16 words | Mandatory Route-A/positive-A2/Route-B status language. |
| remaining 6 Round-10 pairs | 5--7 words | Below the eight-word reporting threshold. |

No pair reaches the plagiarism protocol's 20-word exact-body-run warning
threshold. Declarations were excluded from the scientific-body denominator;
when inspected separately, they contain long common funding, ethics,
availability, accountability, and AI-disclosure templates. Those repeated
declarations should be treated as standardized disclosure text, not silently
counted as original scientific prose.

The local prior-corpus scan compared the five Round-10 manuscripts against 21
earlier local manuscripts (**105 pairs**). All were below the eight-word
reporting threshold (maximum runs in the frozen report are 3--5 words). A
secondary local PDF reconnaissance of the author's supplied prior-work folder
found only short affiliation/header matches at roughly 12--16 words after body
boundaries were considered, not a substantive body match.

## Author-identity and prior-work targets for the required external check

A bounded exact-email/author WebSearch identified the following plausible
Liang Wang prior-work targets for the protocol's self-reuse dimension:

- [The emergence of prime distribution from low-dimensional deterministic chaos](https://www.tandfonline.com/doi/full/10.1080/27684830.2026.2684334), DOI `10.1080/27684830.2026.2684334`; the publisher surface matches the project author affiliation/email and exposes ORCID `0000-0001-9006-6924`.
- [Spectral Isomorphism between Renormalization Flow in Non-Autonomous Quadratic Maps and Riemann Zeros](https://assets-eu.researchsquare.com/files/rs-9024307/v1_covered_a1136c72-f4ab-4752-a0b8-7690b3aea3bc.pdf), Research Square manuscript surface returned by the identity query.
- [A Transfer-Operator Framework for the Collatz Map](https://doi.org/10.20944/preprints202603.1652.v1), DOI `10.20944/preprints202603.1652.v1`.

These URLs are search targets, not proof that every item is an author-owned
publication or that semantic self-reuse is absent. Identity and passage-level
comparison require human classification. The first publication is also
present in the supplied local prior-work corpus, where the deterministic body
overlap scan found no eight-word Round-10 match.

## Working disposition

- originality candidate coverage is frozen at **116/374 = 31.02%**, with all
  major numbered sections covered and exact candidate locators stored in five
  hash-bound JSON sidecars;
- no 20-word exact scientific-body reuse warning was found among Round-10
  papers or the 21-manuscript local comparison corpus;
- no own scientific experiment/result claim or surprise-to-novelty trigger was
  found in the five manuscripts, while executed literature/workflow language
  is visible and bounded;
- P33 citation integrity is handled in its dedicated Phase-A/B sidecar;
- scholar experiment declaration, 116 candidate WebSearch classifications,
  professional-detector coverage, P29--P32 citation integrity, and final
  seven-mode adjudication remain outside this working reconnaissance.

No manuscript, BibTeX database, PDF, state file, README, roadmap, or canonical
result was modified by this reconnaissance.
