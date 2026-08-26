# Paper 22 — fppf and finite-flat Verschiebung lifts

## Current status

- Stage: **Stage 6 PROCESS SUMMARY in progress; Chinese record delivered;
  terminal acknowledgement pending**.
- Current checkpoint: the scholar selected Chinese first, requested this
  conclusion synopsis, and entered Stage 6.  The 1,653-word Markdown record and
  its 14-page A4 PDF include the complete stage history, iteration statistics,
  whole-pipeline Collaboration Depth advisory, AI self-reflection, and the
  final collaboration-quality evaluation.  Stage 6 is not marked complete
  until the scholar explicitly accepts the delivered record.
- Working title: *A Descent Obstruction to Verschiebung Lifts on fppf and
  Finite-Flat Sites*.
- Primary owner: a universe-small absolute `NoethAffSch` site in Deninger's
  sense, the exact sheaf epimorphism `omega`, and the additive operation
  `V_N`.
- Final package: **seven sections, continuous two-round revision evidence,
  reproducible 13-page PDF**.

## 结论概要

对每个 `N>1`，论文在 Deninger 意义下的 universe-small absolute
`NoethAffSch` 上，利用有限自由根覆盖 `k[x] -> k[s]`、`x -> s^N`，构造了
Verschiebung 局部前像无法下降的显式障碍。因此，`V_N` 在 fppf site 上不存在
通过 `omega` 的加性 sheaf lift；有限平坦 site 的非存在性由独立的
site-specific 论证得到。等价地，对扩张 `e:0->K->Z->W->0`，不存在
`u:K->K` 使 `u_*e=V_N^*e`。`N=1` 的恒等 lift 是严格对照。

该有限平坦反例还表明 Deninger v1 Corollary 4.6 的 sectionwise
Dedekind-ring 等式按原文表述需要修正；Propositions 4.3、4.5 与
Corollary 4.7 不受该结论否定。

## Main result

For every `N>1`, the locally forced root-factorization preimage of
`V_N([x])` fails descent on a finite-free cover. Hence no additive lift
through `omega` exists on the fppf site. The finite-flat result is proved
separately with its own domain-refinement check. For the actual extension
`e:0->K->Z->W->0`, no endomorphism `u:K->K` satisfies
`u_*e=V_N^*e`. The `N=1` identity is the control.

The finite-flat witness also shows that the sectionwise Dedekind-ring
assertion in Corollary 4.6 of Deninger's version-1 preprint does not hold as
stated. Proposition 4.3 remains the sheaf-epimorphism input; Proposition 4.5,
together with the Dedekind-domain refinement, supplies injectivity.

## Manuscript and audits

- [compiled paper](paper/paper.pdf)
- [LaTeX source](paper/manuscript.tex)
- [bibliography](paper/references.bib)
- [Phase-3 proof ledger](notes/phase3_all_index_nonlift_theorem.md)
- [independent proof/source audit](notes/stage2_independent_proof_source_audit.md)
- [writer contract report](notes/phase4_writer_contract_report.md)
- [Round-2 evaluator ACCEPT report](notes/phase6b_evaluator_report_round2.md)
- [citation and abstract report](notes/stage2_citation_abstract_report.md)
- [build report and hashes](notes/stage2_build_report.md)
- [Stage-2.5 integrity report](notes/stage2_5_integrity_report.md)
- [Stage-2.5 corrected build and hashes](notes/stage2_5_build_report.md)
- [claim registry and evidence coverage](notes/stage2_5_claim_registry_coverage_adjudication.md)
- [verified Material Passport](notes/material_passport.json)
- [experiment-intake closure receipt](notes/stage2_5_experiment_intake_closure.md)
- [exact roadmap crosswalk](notes/composition_blueprint.md)
- [Stage-4 completion report](notes/stage4_completion_report.md)
- [Stage-4 Response to Reviewers](notes/stage4_response_to_reviewers_round1.md)
- [Stage-4 revision-evidence bundle](notes/stage4_revision_evidence_bundle.json)
- [Stage-4 revised-paper build report](notes/stage4_build_report.md)
- [Stage-3-prime verification review](notes/stage3prime_verification_review.md)
- [Stage-3-prime traceability sidecar](notes/stage3prime_phase2b_traceability.json)
- [Stage-3-prime completion report](notes/stage3prime_completion_report.md)
- [Stage-4.5 final integrity report](notes/stage4_5_final_integrity_report.md)
- [Stage-4.5 Schema-5 machine handoff](notes/stage4_5_integrity_report.json)
- [Stage-4.5 reference/citation audit](notes/stage4_5_reference_citation_audit.md)
- [Stage-4.5 originality/failure-mode audit](notes/stage4_5_originality_failure_mode_audit.md)
- [Stage-4.5 Round-2 exact PASS report](notes/stage4_5_round2_final_integrity_report.md)
- [Stage-4.5 Round-2 Schema-5 machine handoff](notes/stage4_5_round2_integrity_report.json)
- [Stage-4.5 Round-2 reference/citation audit](notes/stage4_5_round2_reference_citation_audit.md)
- [Stage-4.5 Round-2 Phase-C audit](notes/stage4_5_round2_phase_c_internal_consistency_audit.md)
- [Stage-4.5 Round-2 originality/failure-mode audit](notes/stage4_5_round2_originality_failure_mode_audit.md)
- [Stage-4.5 Round-2 E6 audit](notes/stage4_5_round2_e6_semantic_audit.md)
- [Stage-4.5 Round-2 route crosswalk](notes/stage4_5_round2_route_crosswalk.md)
- [Stage-5 entry checkpoint](notes/stage4_5_round2_stage5_entry_checkpoint.md)
- [Stage-5 entry decision](notes/stage5_entry_decision_20260826.md)
- [Stage-5 input manifest](notes/stage5_input_manifest.json)
- [Stage-5 content preflight](notes/stage5_content_preflight.md)
- [Stage-5 final paper package](stage5_finalization/README.md)
- [Stage-5 finalization report](notes/stage5_finalization_report.md)
- [Stage-5 final manifest](notes/stage5_final_manifest.json)
- [Stage-5 FULL completion checkpoint](notes/stage5_completion_checkpoint.md)
- [Stage-5 provenance summary](stage5_finalization/provenance_summary.md)
- [Stage-5 package-verifier report](stage5_finalization/submission_verification_report.json)
- [Stage-6 中文流程记录（Markdown）](notes/stage6_process_record/paper_creation_process.md)
- [Stage-6 中文流程记录（PDF）](notes/stage6_process_record/paper_creation_process_zh.pdf)
- [Stage-6 process-record manifest](notes/stage6_process_record/process_record_manifest.json)
- [whole-pipeline Collaboration Depth advisory](notes/stage6_process_record/stage6_collaboration_depth_advisory.md)
- [Stage-6 terminal checkpoint](notes/stage6_process_record/stage6_terminal_checkpoint.md)

The respectful source-author note is stored at
[author_contact_draft.md](notes/author_contact_draft.md) and is prominently
marked **UNSENT**. No external contact was made.

## Roadmap disposition

`ROUTE_A_EVALUATION=NOT_TESTABLE`; no A0--A4 tuple and no Route-A
advancement. Route-B invocation and entry authorization are both false;
`ROUTE_B_STATUS=ROUTE_B_NOT_TESTABLE`, and no B1--B5 tuple is assigned.
Gates A--E are not reached. This is a reusable pure-algebra obstruction,
and its sheaf-theoretic word “lift” has no Route-A quantization meaning.

## Gate

Stage 4.5 Round 2 remains exact `PASS` with zero SERIOUS, MEDIUM, or MINOR
issues.  Stage 5 preserved manuscript SHA `e90dd881...58ed` and bibliography
SHA `bd03813...1093`, then produced reproducible final PDF SHA
`e030259...c761a`.  All 13 pages rendered correctly; all fonts are embedded;
21 citation commands and three bibliography entries close without a missing or
orphan key.  The package verifier passes C1/C2 and remains explicitly
`NOT-CHECKED` on B1--B5 because no venue profile was declared.  #660 remains
`not_checked`; #672 remains advisory-unavailable; neither is restated as clean.
Stage 5 is complete and its FULL checkpoint is confirmed by the explicit
Stage-6 entry.  Stage 6 has delivered the Chinese process record and now awaits
terminal acknowledgement.  Git synchronization of the current in-scope
session results is explicitly authorized; submission, public release,
source-author contact, venue-readiness claims, and Route advancement remain
unauthorized.
