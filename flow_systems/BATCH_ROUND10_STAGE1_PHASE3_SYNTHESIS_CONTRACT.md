# Round 10 Papers 29–33 — Stage 1 Phase-3 synthesis contract

Date frozen: **2026-09-02 UTC**  
Scope: **ARS Stage 1 Phase 3 evidence synthesis and Devil's Advocate Checkpoint 2 only**

## Authority and phase fence

The scholar's exact UTF-8 response `确认` authorizes Papers 29–33 to leave the
Phase-2 checkpoint and enter Phase 3. The raw event is stored at
`BATCH_ROUND10_STAGE1_PHASE3_AUTHORIZATION_20260902.txt`; its SHA-256 is
`f449b78edf3805c05f297591a9593158d475b87f289b39f69c3f6eb813889ebe`.

This authority permits only cross-source synthesis of the already closed
Phase-2 corpora, one independent Devil's Advocate Checkpoint-2 pass per paper,
bounded corrections to Phase-3 artifacts, and checkpoint/audit bookkeeping.
It does **not** authorize new literature retrieval, scientific computation,
canonical-result refresh, novelty proof, formal manuscript Claim Registry
registration, manuscript drafting, a formal Route-A tuple, Route-A promotion,
or Route-B invocation.

## Frozen inputs

Each synthesis pass consumes, without widening, the paper's exact:

- `notes/stage1_phase1_rq_brief.md`;
- `notes/stage1_phase1_methodology_blueprint.md`;
- `notes/stage1_phase2_annotated_bibliography.md`;
- `notes/stage1_phase2_source_inventory.tsv`;
- `notes/stage1_phase2_source_verification.md` and `.tsv`;
- `notes/stage1_phase2_checkpoint.md`; and
- inherited object, clock, owner/repetition, normalization, cutoff, control,
  failure-state, and Route boundaries in `notes/pipeline_state.md`.

The controlling roadmaps remain `skills/route-a-evaluator.md` and
`skills/route-b-evaluator.md`. Literature compatibility is not Route credit.

## Required Phase-3 artifacts per paper

1. `notes/stage1_phase3_claim_intent_manifest.json`, emitted before synthesis
   prose and conforming to ARS `claim_intent_manifest/1.0`. This is a synthesis
   precommitment only, not formal project claim registration. It must contain
   no experiment IDs because no experiment is authorized.
2. `notes/stage1_phase3_literature_matrix.tsv`, containing every closed-corpus
   source ID exactly once and recording its theme, admissible contribution,
   stronger excluded claim, compatibility role, and unresolved locator limit.
3. `notes/stage1_phase3_synthesis.md`, with 3–7 themes, consensus, debates,
   contradictions/tensions, research gaps, methodology recommendations,
   theoretical implications, and one concrete paper-specific Phase-3 advance.
4. A bounded cross-paper tension inventory inside the Contradictions section.
   It is a candidate-edge heuristic, not an exhaustive pairwise comparison;
   every edge remains `scholar_confirmation: pending`.
5. `notes/stage1_phase3_devils_advocate.md`, produced by a seat different from
   the synthesis seat, followed when necessary by a resolution and independent
   recheck.
6. `notes/stage1_phase3_checkpoint.md`, issued only after all critical issues
   are resolved or the paper is explicitly stopped.

## Citation and claim-strength rules

- Every substantive cross-source statement must name visible author/year and
  carry `<!--ref:SOURCE_ID--><!--anchor:...-->`.
- An exact page/section anchor may be used only when the frozen corpus records
  it. Otherwise use `anchor:none` and keep the statement at metadata,
  abstract, or verification-ledger scope.
- `VERIFIED` proves source identity/metadata under Phase 2; it does not by
  itself prove every theorem-level interpretation.
- `PLAUSIBLE`, background-only, preprint, correction-bound, and
  applicability-limited records retain those limits.
- Search non-detection may identify a corpus gap but may never be called a
  novelty proof, impossibility theorem, or exhaustive-literature result.
- No synthesis statement may imply that a project-specific algorithm,
  certificate, numerical experiment, determinant, uniform tail, or Route
  layer has been executed when it has not.

## Independent Devil's Advocate Checkpoint 2

The DA pass tests at minimum:

1. source-ID coverage and citation-to-inventory validity;
2. theme/gap/debate/methodology/theoretical-implication completeness;
3. contradiction and correction-companion handling;
4. theorem-hypothesis and object/clock/owner compatibility;
5. overclaim, novelty inflation, evidence-grade inflation, and logical
   fallacies;
6. preservation of each immutable dynamical restriction and negative result;
7. leakage into computation, formal Route evaluation, Route B, or manuscript
   drafting; and
8. whether the proposed next executable obligations are genuinely licensed by
   the verified corpus.

Any `CRITICAL` finding blocks the Phase-3 checkpoint until bounded correction
and recheck. `MAJOR` findings require correction unless they are documented as
an explicit fail-closed limitation. Minor observations remain visible.

## Allowed Phase-3 dispositions

```text
PHASE3_SYNTHESIS_READY
PHASE3_SYNTHESIS_READY_WITH_WARNINGS
PHASE3_SYNTHESIS_INSUFFICIENT
PHASE3_INTEGRITY_BLOCK
```

These dispositions answer whether the evidence synthesis is fit to inform the
next Stage-1 research decision. They do not assign novelty, prove a scientific
claim, or authorize later work.

## Batch invariants

```text
SCIENTIFIC_COMPUTATION=NOT_RUN
CANONICAL_RESULTS_REFRESH=NOT_RUN
FORMAL_PROJECT_CLAIM_REGISTRATION=0/5
FORMAL_ROUTE_A_TUPLES=0/5
POSITIVE_ARITHMETIC_A2=0/5
ROUTE_B_INVOCATIONS=0/5
MANUSCRIPT_DRAFTING=NOT_AUTHORIZED
```
