# Round 10 Stage 4.5 Round 2 — audit-validator count correction

Date: 2026-09-05 UTC. Audit-side execution history only; not manuscript-repair authority or a scientific PASS.

## Actual failed full replay

After the exact TEMP9 P30/P31 audit packages were published, the main agent executed `ruby tools/audit_round10_stage4_5_round2.rb`. It exited 1 with 88 passed checks and one failed check:

```text
FAIL P31 S23/S24 passage support remains UNVERIFIABLE: P31 S23/S24 missing component denominator: 10 != 8
Checks passed: 88
ROUND10_STAGE4_5_ROUND2_AUDIT_FAIL
```

The final independent replay and batch-finalization outputs were not created on the strength of this failed run.

## Diagnosis and bounded correction

Two separately executing reviewers and the main agent found the exact ten components: claims `P31-S45R2-E1-008`, `067`, `077`, `079`, and `080`, each paired with `missing_s23_passage` and `missing_s24_passage`. Every component is anchorless and UNVERIFIABLE. The obsolete validator expected eight components and omitted E067 from this one claim-set assertion, although E067 was already in its overall UNVERIFIABLE set.

E067 is the existing broad literature-negative claim. The original semantic-dependency review explicitly required its 15 unavailable S01–S22 passage components plus the two S23/S24 passage components to remain unverifiable. The builder implemented that requirement. There is no duplicate component, new scientific finding, new correction target, or justification for deleting these missing components.

The validator now checks the exact five-by-two claim/component pair set, denominator ten, and unchanged UNVERIFIABLE outcomes. Its other checks are unchanged. The original entire validator is retained at `tools/audit_round10_stage4_5_round2.pre_p31_e067_denominator_fix.79ca4b364a0b.rb`.

| Version | SHA-256 | Bytes |
| --- | --- | ---: |
| Before | `79ca4b364a0bbe7cdbd50b347ba8e7906476d5a00dba4f32fd590638b5d613a5` | 62262 |
| After | `b432c4a7b008f0ebea92590d0bb051fc18239fc315704f4d6ba635c2fe76eafc` | 62689 |

The repair reviewer directly exercised the extracted predicate: the actual ten components passed; deletion of E067's components, duplicate substitution, wrong claim/component pairing, and weakening an EVR verdict to VERIFIED each failed. The old predicate reproduced its eight-versus-ten failure. Ruby syntax passed. Reversing the one changed predicate reconstructed the old validator bytes exactly.

## P30 provenance rebinding

Changing the validator requires rebinding P30 E107's unique `CURRENT_AUTHORIZED_AUDIT_EXECUTION` descriptor to the actual new validator SHA and byte count. The helper `tools/rebind_round10_p30_validator_descriptor.py` performs only that change and propagation through existing current audit-artifact SHA/bytes descriptors. It does not regenerate evidence, change claim text or verdicts, refresh timestamps, modify manuscripts, or rerun science.

A first unpublished helper preview was stopped when its separate code review found that historical archive descriptors also needed exclusion. That issue was corrected before any publication: descriptors carrying `archive_path` are skipped, and the old incident, attempt lineage, and EVR files must remain byte-identical. The reviewed helper SHA is `6ccf09121fcd2268c4e1d1d22d58515b0452178d6c096b99a1999f504cf8adf6`.

The previous TEMP9 package is to be preserved in `papers/30-three-disk-nonconstant-roof-determinant/notes/stage4_5_round2_TEMP9_PRE_VALIDATOR_COUNT_REBIND_archive/`: 42 manifest-bound artifacts plus the manifest and validation receipt. Publication requires a validated preview matching all 23 candidate files exactly. Full root replay must then actually pass before any final PASS audit-package record is emitted.

Reviewers are same-model-family, role-separated agents, not a cross-model panel or a claim of independent error processes. One reviewer previously performed the path-only runtime compatibility repair. All five scientific-integrity FAIL dispositions, the 17-issue / 66-block / one-Bib proposed correction scope, and frozen Route/initial-system boundaries remain unchanged.

## Completed descriptor publication

The revised preview passed the official evidence, coverage, Schema-12, raw-dependency-chain and candidate-manifest checks. A separate reviewer compared the original TEMP9 bytes with the preview: exactly five JSON files and twelve leaf values changed, all existing descriptor `sha256`/`bytes` fields. The only primary change was the one runtime validator descriptor; all other changes were its downstream hashes. EVR, attempt lineage, and the attempt-5 incident remained byte-identical.

The exact preview was then published. All 44 previous manifest-bound artifacts were archived and verified. Post-publication `validate_final` passed, including protected snapshots and the retained attempt-5 archive. P31 was not rewritten.

| Current P30 audit artifact | SHA-256 | Bytes |
| --- | --- | ---: |
| Dependency catalog | `f2c89499f3bcacc037c104582b55cbf5d8c943d2a19e72c49863862430c08d0d` | 2615565 |
| Integrity report | `4962f4265fd5589c88f737900cc0aa898c2a9be44334e31c139f43723c203be4` | 1730386 |
| Receipt | `1c270bba315f203fa068bdc2a943bc87fddcd2e1ec9a9ee69f88bb6652d3b60a` | 1690691 |
| Output manifest | `ef82adeebd08e2b6532f2c84ee997da942a923bee7d2f44f62188b10a7e07919` | 15035 |
| Validation receipt | `2c65d545782df68d3e175c0337814c9acdc4227260553420bd5c922a6f336b86` | 9623 |

## Actual terminal replay

After this publication, the main agent and the separately executing batch reviewer each ran the full root validator successfully: exit 0, 89 checks passed, `ROUND10_STAGE4_5_ROUND2_AUDIT_PASS`. The final independent replay is `BATCH_ROUND10_STAGE4_5_ROUND2_FINAL_INDEPENDENT_REPLAY.json`, SHA-256 `2596f8caa15c91a04f7bb33d69bbc231f0e2154df6d6bc01f1e1db50d304094f`. After freezing that actual digest, finalizer execution completed successfully and emitted the batch audit, report, correction request, mandatory checkpoint and validation receipt. Five scientific FAIL verdicts remain unchanged; this terminal PASS concerns only audit-package coherence.
