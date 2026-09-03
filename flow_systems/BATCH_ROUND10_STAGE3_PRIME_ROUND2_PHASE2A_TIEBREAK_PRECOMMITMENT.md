# Round 10 Stage 3′ Round 2 — Phase 2A semantic tie-break precommitment

- Frozen on: 2026-09-03 UTC
- Phase-2A artifacts are already evidence-committed and cannot be rewritten.
- Primary full-row semantic audits are frozen at:
  - `BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_SEMANTIC_AUDIT_P29_P30.json` — SHA-256 `a46fc05948cb147f513c4ce854011aad488875bc9844034332aa8f6ef3648a3b`
  - `BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_SEMANTIC_AUDIT_P31_P32.json` — SHA-256 `bc4a97ca5b051a1658acdae2ee2ca705a144579ae6c93089dbaf489c6d5e4f8d`
  - `BATCH_ROUND10_STAGE3_PRIME_ROUND2_PHASE2A_SEMANTIC_AUDIT_P33.json` — SHA-256 `1fc2e5f957f07eaef2960ffcde810ddde433ba39ebac87cf38c61bfac053bc55`

## Closed disputed set

- P29: `REV-EIC-1`, `REV-DA-2`
- P31: `REV-P31-003`, `REV-P31-006`
- P32: `REV-P32-DA-N1`, `REV-P32-DA-M1`
- P33: `REV-P33-011`

## Arbitration rule fixed before dispatch

Each tie-breaker independently applies the exact committed Phase-1 criterion to
the original and revised manuscript evidence. The tie-breaker receives the item
IDs only; it does not receive the committed Phase-2A verdict, the primary audit
verdict, any Round-1 re-review artifact, any semantic-audit conclusion, the
Response to Reviewers, or the author adjudication sidecar.

For the seven closed disputed rows, the fresh blind tie-break verdict controls
the semantic consolidation. The primary full-row audit controls every other
row. No plurality or averaging is used. A controlling tie-break verdict that
differs from the committed Phase-2A verdict produces
`[RE-REVIEW-ABORT: phase2a_lint_failed]` for that paper; Phase 2A has no retry.
Agreement preserves eligibility for Phase 2B but does not itself issue a
decision.

All tie-break contexts are role-separated but use the same model family and
provider. They are not represented as statistically independent error
processes, and no cross-model verification is claimed.
