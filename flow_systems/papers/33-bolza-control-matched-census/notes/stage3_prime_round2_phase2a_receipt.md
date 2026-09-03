# P33 Stage 3′ Round 2 Phase 2A Receipt

- Round: `p33-stage3-prime-round2-2026-09-03`
- Contract: `verdict_record/1.1`
- Committed artifact: `notes/stage3_prime_round2_verdict_record.json`
- Raw artifact SHA-256: `a4487366cca09bd333221a2606443c17ddea9546e27216c8760304d536849939`
- Artifact JCS SHA-256: `e85fb9401fe046d05ba1cb39a078405fb0a7d406a8db096c733d713aaf7dac7e`
- Input-manifest JCS SHA-256: `7250e43866c14e1a0fdbdc08de9eaa420a34520df0fbdad65ab07b16de5f3985` — recomputed and equal to the immutable Phase 1 binding.
- Precommitment JCS SHA-256: `adfe01c13084301ba5e83e7cec39c3312190d0fada37869226f008c7290d0dc2` — recomputed and equal to `precommitment_hash` in the committed verdict record.
- Schema validation: PASS against the current `verdict_record.schema.json`.
- Allowed manifest artifact hashes: PASS for the original manuscript, revised manuscript, roadmap, editorial synthesis, Round-1 findings, frozen configuration cards, revision patch, apply report, and revision-evidence bundle.
- Apply-chain evidence: patch digest matched the paired patch and the current apply report carried `authorization_witness.status: pass`.

## Verdict accounting

- Rows: 13/13, in immutable Phase 1 order.
- `FULLY_ADDRESSED`: 6 — `REV-P33-001`, `REV-P33-004`, `REV-P33-009`, `REV-P33-010`, `REV-P33-011`, `REV-P33-012`.
- `PARTIALLY_ADDRESSED`: 7 — `REV-P33-002`, `REV-P33-003`, `REV-P33-005`, `REV-P33-006`, `REV-P33-007`, `REV-P33-008`, `REV-P33-013`.
- `NOT_ADDRESSED`: 0; `MADE_WORSE`: 0; `CANNOT_VERIFY`: 0.
- Partial residual classes: 6 `must_fix`, 1 `should_fix`, 0 `consider`.
- Routed verification seats: EIC 5, R1 4, R2 2, R3 2. The DA-only row `REV-P33-013` was routed to EIC as required; DA was not used as a verification persona.
- New issues: 0; dissents: 0; escalation exceptions: 0.

## Withholding and independence attestation

Phase 2A was performed persuasion-blind. No response-to-reviewers content, author-adjudication sidecar content, author-choice content, earlier-round Phase 2A verdict, semantic-audit surface, Phase 2B artifact, outcome/checkpoint/report narrative, or other Stage-4 narrative surface was opened, parsed, or used. Pointer and hash carriage metadata for withheld artifacts was visible only where it occurred inside the allowlisted input manifest or revision-evidence bundle; the referenced withheld files themselves were not accessed. No prior verdict or expected count informed the row judgments, and no web, external-model, or cross-model source was used.

All non-`CANNOT_VERIFY` anchors point to exact blocks in `notes/stage4_revision_round1.tex`; every `change_summary` was checked against `notes/stage3_revision_base.tex` and the bound patch/apply evidence. The Phase 1 operationalizations were treated as immutable. The committed verdict record was promoted byte-for-byte from the schema- and lint-validated scratch candidate in one persistence action and was not edited or regenerated afterward.

[EVIDENCE-COMMITTED]
