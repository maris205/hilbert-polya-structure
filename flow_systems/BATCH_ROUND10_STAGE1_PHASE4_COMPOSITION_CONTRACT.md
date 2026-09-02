# Round 10 Papers 29–33 — Stage 1 Phase-4 composition contract

Date frozen: **2026-09-02 UTC**

Scope: **ARS Stage 1 Phase 4 research-report composition only**

## Authority and interpretation

The scholar's exact UTF-8 response `确认，开始下一轮` authorizes the next gate
disclosed in the Phase-3 checkpoint: Phase 4 composition for Papers 29–33.
The raw event is stored in
`BATCH_ROUND10_STAGE1_PHASE4_AUTHORIZATION_20260902.txt`, SHA-256
`b516a3f1c0b362a77ba7b5963375492d7bab73c746cb458086feb48638739a85`.
“下一轮” therefore means the next research phase for the same five papers, not
a new paper batch.

This authority permits five full research-report drafts, fresh writer-side
claim-intent manifests, deterministic composition audits, paper/batch
checkpoints, README/state bookkeeping, and Git synchronization. It does not
authorize new retrieval, scientific computation, canonical-result refresh,
novelty proof, formal project Claim Registry registration, formal Route-A
evaluation or promotion, Route B, edits to `paper/manuscript.tex` or
`paper/references.bib`, a manuscript PDF, or Phase-5 editorial/ethics/DA
review.

## ARS role and knowledge-isolation rule

The active role is `report_compiler_agent` from
`ars-codex:academic-research-suite`. Every factual or methodological statement
must be traceable to the closed project materials. Parametric knowledge may be
used for language and academic structure only. If the frozen materials do not
support a needed statement, the report must mark `[MATERIAL GAP]`; it may not
fill the gap from memory.

Each compiler consumes, without widening:

- `notes/stage1_phase1_rq_brief.md`;
- `notes/stage1_phase1_methodology_blueprint.md`;
- `notes/stage1_phase2_annotated_bibliography.md`;
- `notes/stage1_phase2_source_inventory.tsv`;
- `notes/stage1_phase2_source_verification.md` and `.tsv`;
- `notes/stage1_phase2_checkpoint.md`;
- `notes/stage1_phase3_literature_matrix.tsv`;
- `notes/stage1_phase3_synthesis.md`;
- the complete Phase-3 DA/resolution/recheck chain applicable to that paper;
- `notes/stage1_phase3_checkpoint.md`; and
- the immutable object, clock, owner/repetition, normalization, cutoff,
  controls, failure states, and Route boundaries in `notes/pipeline_state.md`.

The compiler must not inspect or copy the sibling Phase-3 claim-intent
manifest. It emits a fresh Phase-4 precommitment from the paper-visible
synthesis context, as required by the ARS partial-inversion boundary.

## Required artifacts per paper

1. `notes/stage1_phase4_claim_intent_manifest.json`
   - valid `claim_intent_manifest/1.0`;
   - `emitted_by=report_compiler_agent`;
   - fresh unique manifest ID;
   - emitted before report prose;
   - every `planned_refs` value resolves to the frozen source inventory;
   - no `planned_experiment_ids`, because no experiment is authorized; and
   - global and claim-level negative constraints preserve the paper's exact
     scientific and Route boundaries.
2. `notes/stage1_phase4_research_report.md`
   - 3,000–8,000 whitespace-delimited words excluding the machine ledger;
   - abstract of 150–250 words plus 5–7 keywords;
   - title/author/declarations, introduction and research question;
   - literature/theoretical framework;
   - methodology describing only the executed literature pipeline;
   - findings explicitly typed as evidence-synthesis findings;
   - discussion, theoretical and practical implications;
   - limitations and future work;
   - conclusion and bounded recommendations;
   - reference list containing every cited work and no uncited work;
   - mandatory AI disclosure with the actual metadata/abstract-level
     verification limitation; and
   - report metadata and a closed phase-fence ledger.
3. `notes/stage1_phase4_checkpoint.md`, issued only after deterministic
   validation of the exact manifest/report bytes.

## Citation and reference contract

- Use only source IDs already present in the paper's frozen inventory.
- Every visible author-year citation must be immediately followed by
  `<!--ref:SOURCE_ID--><!--anchor:none:-->`.
- The `none` locator is mandatory here because the frozen Phase-3 corpus does
  not provide report-compiler-safe exact quotation/page/section context. It is
  a visible carried warning, not a verification bypass.
- No direct quotation is permitted.
- A source may support only the contribution allowed by the Phase-3 matrix;
  `PLAUSIBLE`, preprint, correction-bound, background-only, applicability-
  limited, and identity/metadata-only rows retain those limitations.
- Search non-detection is a bounded corpus gap, never novelty or impossibility.
- Each frozen source ID must appear at least once in the report citation layer,
  while the reference list must match the unique cited-ID set exactly.
- Temporal language uses explicit source years or the report date. Deictic
  “latest/current/recent” claims are prohibited.

This is explicit Stage-1 pipeline mode. The standalone ARS no-locator
self-gate therefore does not run; the `anchor:none:` warnings remain in the
draft for the later integrity/review path and prohibit any claim that the
draft has passed locator-level citation compliance.

## Scientific and Route fences

The Phase-4 report may explain a preexecution proof or certificate program but
must not report it as executed. “Findings” means findings of the frozen
evidence synthesis, not new dynamical, arithmetic, numerical, or operator
results.

```text
SOURCE_CORPUS=FROZEN_116_ROWS
SCIENTIFIC_COMPUTATION=NOT_RUN
CANONICAL_RESULTS_REFRESH=NOT_RUN
NOVELTY_ASSESSMENT=NOT_RUN
FORMAL_PROJECT_CLAIM_REGISTRATION=0/5
FORMAL_ROUTE_A_TUPLES=0/5
POSITIVE_ARITHMETIC_A2=0/5
ROUTE_B_INVOCATIONS=0/5
CANONICAL_MANUSCRIPTS_MODIFIED=0/5
CANONICAL_BIBLIOGRAPHIES_MODIFIED=0/5
MANUSCRIPT_DRAFTING=NOT_AUTHORIZED
PHASE_5_REVIEW=NOT_AUTHORIZED
```

The controlling roadmaps remain byte-frozen:

- `skills/route-a-evaluator.md`, SHA-256
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- `skills/route-b-evaluator.md`, SHA-256
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

Literature composition is not Route credit. The eventual manuscript citation
style remains the already confirmed plainnat numerical style; Phase-4
author-year markers are research-report provenance and do not alter LaTeX.

## Allowed Phase-4 dispositions

```text
PHASE4_REPORT_DRAFT_READY
PHASE4_REPORT_DRAFT_READY_WITH_WARNINGS
PHASE4_REPORT_DRAFT_INSUFFICIENT
PHASE4_INTEGRITY_BLOCK
```

The expected warning state is not a waiver: `anchor:none:` locators, bounded
source verification, open certificate gates, and unexecuted science must stay
visible. The only next transition after a valid checkpoint is explicit
scholar confirmation for Phase 5 review.
