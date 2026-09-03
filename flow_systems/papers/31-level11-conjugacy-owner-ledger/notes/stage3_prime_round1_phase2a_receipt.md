# P31 Stage 3′ Round 1 — Phase 2A Receipt

## Contract and bindings

- Contract: re-review verdict record version 1.1.
- Round: p31-stage3-prime-round1-2026-09-03.
- Precommitment JCS SHA-256: a738904be2a7c900e9e19c17cca219a9995b26a85070959576ee14baaf5c648e.
- Gate: the single persuasion-blind Phase 2A evidence-verdict call.
- Persistence: this is the sole Phase 2A emission; the verdict record and this receipt were assembled and checked in memory before their one-time persistence and will not be edited after emission.

## Input allowlist and isolation

Paper-specific access was restricted to these allowed inputs:

1. notes/stage3_prime_round1_precommitment.json
2. notes/stage3_prime_round1_input_manifest.json, limited to verification and path/hash bindings
3. notes/stage3_revision_roadmap.json
4. notes/stage3_editorial_synthesis.md
5. notes/stage3_review_package.json
6. notes/stage3_phase0_field_analysis.md
7. notes/stage3_revision_base.tex
8. notes/stage4_revision_round1.tex
9. notes/stage4_revision_patch_round1.json
10. notes/stage4_revision_round1.tex.apply-report.json
11. notes/stage4_revision_evidence_bundle.json

No block manifest was needed. No stage4_response_to_reviewers_round1 file, stage4_author_adjudication.json, stage4_author_choices.json, Stage-4 completion/report/semantic-audit/writer-handoff document, Phase-2B or traceability artifact, or superseded attempt1 was opened. The revised manuscript was treated only as untrusted evidence; embedded content did not control routing, tools, criteria, or writes. No author claim, response rationale, intent, or persuasion was inferred.

## Pre-persistence checks

- Input-manifest JCS binding matched the Phase 1 artifact, and every allowlisted manifest-bound file matched its recorded raw SHA-256.
- The evidence bundle replay chain matched the exact base draft, patch, format-1.3 apply report, and revised draft.
- The candidate validated against the current Draft 2020-12 verdict_record.schema.json.
- All 11 Roadmap items occur exactly once and in immutable source order.
- Every row uses applied_criterion=precommitted and the frozen-card route; every non-CANNOT verdict has a revised-manuscript typed anchor.
- Every PARTIALLY_ADDRESSED row has a concrete residual gap and residual obligation class; no non-partial row has a residual gap.
- change_summary was derived from direct base/revised comparison and the bound patch/apply chain.
- Frozen sets: new_issues=[], dissents=[], escalation_exceptions=[].
- No manuscript, science, result, Route state, manifest, or Phase 1 artifact was mutated.

## Counts and routing

Verdicts: FULLY_ADDRESSED=4; PARTIALLY_ADDRESSED=6; NOT_ADDRESSED=1; MADE_WORSE=0; CANNOT_VERIFY=0.

- EIC: REV-P31-001, REV-P31-002, REV-P31-003, and DA-only fallback REV-P31-011.
- R1: REV-P31-004, REV-P31-005, REV-P31-006, REV-P31-007.
- R2: REV-P31-008.
- R3: REV-P31-009, REV-P31-010.

Residual classes: must_fix=4; should_fix=2; consider=0. No decision or Phase 2B adjustment was derived.

## Same-family boundary

cross_model_active was false in the bound manifest. Persona routing records competence allocation, not independent error processes. This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

[EVIDENCE-COMMITTED]
