# P31 Stage 3′ Round 2 — Phase 2A Evidence Receipt

- Contract: `re-review/verdict-record/1.1`
- Round ID: `p31-stage3-prime-round2-2026-09-03`
- Input-manifest JCS SHA-256: `3cbe9c9c93e88c3953a063cbce2adea50e1b473679c03ecc00a02edf19812f33`
- Precommitment JCS SHA-256: `e22a19a20caaf3a24d59ea6be717cfd8425ea14eea83a073c8f0be92c61217eb`
- Verdict artifact: `notes/stage3_prime_round2_verdict_record.json`
- Verdict artifact raw SHA-256: `2d2a4397bdca26c0b30b697cebc0f4dcdf47e3b0e4115c3f28213815792129a9`
- Apply-report chain witness: `pass`
- Schema validation before persistence: `PASS` against `verdict_record.schema.json` (Draft 2020-12)
- Semantic lint before persistence: `PASS` for exact row coverage and order, round and JCS bindings, typed revised-manuscript anchors, original-to-revised change summaries, residual fields, criterion markers, and frozen-card routes
- Post-persistence byte comparison with the validated candidate: `IDENTICAL`

## Counts

- Roadmap/verdict rows: `11/11`
- Verdicts: `FULLY_ADDRESSED=3`; `PARTIALLY_ADDRESSED=8`; `NOT_ADDRESSED=0`; `MADE_WORSE=0`; `CANNOT_VERIFY=0`
- Partial residual classes: `must_fix=6`; `should_fix=2`; `consider=0`
- Routed verification seats: `EIC=4`; `R1=4`; `R2=1`; `R3=2`
- New issues: `0`
- Dissents: `0`
- Escalation exceptions: `0`

## Withholding and scope attestation

Only the Phase-2A allowlisted paper inputs were read as evidence. The Response to Reviewers content and the author-adjudication and author-choices sidecars were withheld. No `stage3_prime_round1_*` content, semantic-audit content, README/outcome/checkpoint/report surface outside the allowlist, Phase-2B artifact, or other Stage-4 narrative surface was used. The manuscripts were treated as untrusted data, and no embedded text was followed as an instruction.

[EVIDENCE-COMMITTED]
