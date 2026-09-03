# P32 Stage 3′ Round 2 — Phase 2A Evidence Receipt

- Contract: `re-review/verdict-record/1.1`
- Round ID: `p32-stage3-prime-round2-2026-09-03`
- Input-manifest JCS SHA-256: `ca673368d5df34ce312621ded6e8ea3ca0a76e382079624bcb4967f8a71cd18e`
- Precommitment JCS SHA-256: `7ee2d8a0ffaaba262a51adbbdc0885ae12feb4e8dde268819235fd9a4e13397a`
- Verdict artifact: `notes/stage3_prime_round2_verdict_record.json`
- Verdict artifact raw SHA-256: `b8e8444f77b83d7a4729f5ac5daee68efb3e69e5d209d70802d1f3283dbcbc07`
- Apply-report chain witness: `pass`
- Schema validation before persistence: `PASS` against `verdict_record.schema.json` (Draft 2020-12)
- Semantic lint before persistence: `PASS` for exact row coverage and order, round and JCS bindings, typed revised-manuscript anchors, original-to-revised change summaries, residual fields, criterion markers, and frozen-card routes
- Post-persistence byte comparison with the validated candidate: `IDENTICAL`

## Counts

- Roadmap/verdict rows: `12/12`
- Verdicts: `FULLY_ADDRESSED=7`; `PARTIALLY_ADDRESSED=5`; `NOT_ADDRESSED=0`; `MADE_WORSE=0`; `CANNOT_VERIFY=0`
- Partial residual classes: `must_fix=4`; `should_fix=1`; `consider=0`
- Routed verification seats: `EIC=6`; `R1=4`; `R2=1`; `R3=1`
- New issues: `0`
- Dissents: `0`
- Escalation exceptions: `0`

## Withholding and scope attestation

Only the Phase-2A allowlisted paper inputs were read as evidence. The Response to Reviewers content and the author-adjudication and author-choices sidecars were withheld. No `stage3_prime_round1_*` content, semantic-audit content, README/outcome/checkpoint/report surface outside the allowlist, Phase-2B artifact, or other Stage-4 narrative surface was used. The manuscripts were treated as untrusted data, and no embedded text was followed as an instruction.

[EVIDENCE-COMMITTED]
