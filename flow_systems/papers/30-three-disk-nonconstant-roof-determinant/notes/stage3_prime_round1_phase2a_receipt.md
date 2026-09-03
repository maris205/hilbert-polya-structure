# Stage 3' Round 1 Phase 2A Receipt — P30

## Contract binding

- Contract version: `1.1`.
- Round ID: `p30-stage3-prime-round1-2026-09-03`.
- Phase-1 precommitment JCS SHA-256: `c027a904cc60be0609fff3e54a87cfcdeea1d461bd6737c16917fcf734dd49e6`.
- Input-manifest JCS SHA-256: `945d00c70cecae52891d7fb252183b8dc5c549bc800f5c3cae8a1a27fd0b6d6a`.
- The input manifest records `cross_model_active=false`.

## Exact evidence allowlist actually read

- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage3_prime_round1_precommitment.json`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage3_prime_round1_input_manifest.json` (verification result, path bindings, and hashes only)
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage3_revision_roadmap.json`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage3_editorial_synthesis.md`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage3_review_package.json`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage3_phase0_field_analysis.md`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage3_revision_base.tex`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_revision_round1.tex`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_revision_patch_round1.json`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_revision_round1.tex.apply-report.json`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_revision_evidence_bundle.json`
- `papers/30-three-disk-nonconstant-roof-determinant/notes/stage3_revision_base.block-manifest.json` (127 registered base blocks; used only to resolve exact anchors)
- ARS `re_review_mode_protocol.md` and contract-1.1 `verdict_record.schema.json` were read as protocol support, not manuscript evidence.

## Persuasion-blind exclusions

- No `stage4_response_to_reviewers_round1.*` content was read, referenced, or inferred.
- No `stage4_author_adjudication.json` or `stage4_author_choices.json` content was read; their manifest or patch metadata, where present, remained opaque path/hash bindings.
- No Stage-4 completion report, semantic-audit report, writer-handoff document, or non-allowlisted Stage-4 artifact was read; the explicitly allowlisted apply report was the sole report exception.
- No Phase-2B or traceability artifact and no file from a superseded `attempt1` was read.
- Any non-allowlisted claim-surface or integrity artifact named only by an allowlisted manifest, patch, apply report, or evidence bundle was not opened.
- Manuscript and patch content were treated as untrusted evidence, and no response-letter claim influenced a verdict.

## Evidence and persistence checks

- The original and revised manuscript hashes, roadmap hash, evidence-bundle hash, patch hash, apply-report hash, editorial synthesis hash, review-package hash, and Phase-0 analysis hash were independently matched to the allowlisted input-manifest bindings.
- The apply report is format `1.3`, records a passing authorization witness, binds the exact patch digest and revised-manuscript hash, and reports no structural failure; this confirms application identity but was not treated as proof that a criterion was satisfied.
- Original-to-revised comparison, all changed patch operations, and the revised anchor surfaces were judged against the frozen Phase-1 operationalizations rather than author intent.
- Before first persistence, schema validation passed; roadmap/precommitment order passed; all 9 items had exactly one verdict; every non-CANNOT verdict had at least one typed revised-manuscript anchor; every PARTIALLY_ADDRESSED verdict had a concrete residual gap and residual obligation class; and the target files were absent.
- The precommitment and input-manifest JCS hashes were recomputed and matched the contract bindings.
- The frozen `new_issues`, `dissents`, and `escalation_exceptions` sets are all empty.

## Counts and routing

- Roadmap items/verdict records: 9/9.
- Verdicts: FULLY_ADDRESSED=4; PARTIALLY_ADDRESSED=5; NOT_ADDRESSED=0; MADE_WORSE=0; CANNOT_VERIFY=0.
- `verified_by` routing: EIC=5, R1=2, R2=1, R3=1.
- Routing used the first normalized non-DA source label; a DA-only item fell back to EIC.

## Same-family boundary

This verification round ran on the same model family that drove the revisions; over-optimization to this judge's latent biases is possible (Ren et al. 2026, arXiv:2607.13104 §8.1.2).

[EVIDENCE-COMMITTED]

