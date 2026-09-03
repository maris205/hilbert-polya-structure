# P33 Round-3 Phase-2A semantic-audit attempt 1 — boundary incident

- Disposition: `INVALID_BOUNDARY_TAINTED`; excluded from the semantic gate.
- Invalid artifact: `BATCH_ROUND10_STAGE3_PRIME_ROUND3_PHASE2A_SEMANTIC_AUDIT_P33_INVALID_ATTEMPT1.json`.
- Preserved raw SHA-256: `5610fc9d4ee43a2a6c45cd2105c97823c4d56684994b4a8bb0fb151a8b322ec9`.
- Incident: before receiving the exact P33 paper base path, the audit context ran one broad `**/*P33*` filename glob. It enumerated names of prior P33 audit artifacts, but opened no prior artifact and exposed no prior finding content.
- Conservative ruling: artifact filenames can carry outcome hints, so this context does not satisfy the precommitted fresh-context/blind-input boundary. Its semantic finding is non-controlling and must not determine whether a tie-break is opened.
- Preservation: the committed P33 Phase-2A verdict record remains unchanged at raw SHA-256 `b3774ced6ee2f8114b699e814ad959041b3881f1f8c85ffa9786b117b5d67fa1`.
- Remedy: one replacement primary semantic audit is dispatched in a genuinely fresh context with the exact paper base path supplied initially. This is replacement of an invalid audit-side execution, not a retry or rewrite of the no-retry Phase-2A verdict.

This incident grants no Response-to-Reviewers exposure, Phase 2B authority, manuscript/bibliography/result write, scientific execution, or Route credit.
