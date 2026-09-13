# Round 10 Stage 4.5 Round 2 — invalidated first authority-chain attempt

Recorded: **2026-09-04**

The first generated input lock and authorization receipt were independently audited and rejected before Stage 4.5 Round-2 execution. They are retained under `*_ATTEMPT1_INVALID.*` names as non-authorizing forensic history and must never be consumed as current authority.

Invalidated artifacts:

- `BATCH_ROUND10_STAGE4_5_ROUND2_INPUT_LOCK_ATTEMPT1_INVALID.json`: SHA-256 `506ad57ea24af8524ff0b32f7bafcd47a7c4565a6b5a6e2a55824c7ae3cd8546`, 42,503 bytes.
- `BATCH_ROUND10_STAGE4_5_ROUND2_AUTHORIZATION_RECEIPT_ATTEMPT1_INVALID.json`: SHA-256 `92ed0c7a827a01e5b311888d6c43024e27eafd8a51bba6c0e21fee67fecc3fe4`, 1,203 bytes.

The failed attempt bound the earlier authorization-record version and omitted required latest-passport/final-audit inputs. Its builder also lacked fail-closed symlink, no-clobber, and pair-publication handling. No paper audit verdict was issued from this chain.

The author event remains unchanged. A corrected authorization record, corrected builder, newly generated no-clobber pair, and fresh independent authority audit are required before execution.
