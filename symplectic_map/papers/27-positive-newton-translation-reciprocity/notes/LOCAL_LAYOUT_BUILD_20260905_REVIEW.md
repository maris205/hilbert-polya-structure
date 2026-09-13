# Paper27 layout build: consumed independent reviews

Reviewed SHA256: a38c05bb7d33e3800ea4ea2aff8d5836a135e5c1ebdfd0d7749c3cd140dad9d5
Decision: PASS

The main orchestrator read the two complete independent reports on 2026-09-05 and rechecked their hashes. This consumes their bounded prebuild decisions; it is not a new independent review or an actual-output acceptance decision.

- `LAYOUT_REPAIR_20260905_REVIEW.md`: independent source/typesetting equivalence PASS; report SHA256 `de400bb88207dfa1d07e2b7ad7701c76fab17ab958d2e811522a1e2ec7aaf623`. Original main `d60ec6611683cafdf822b4cb493040258dc1dd29502363d493f52c3e2deeed3e` and layout main `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8` are bound. Finite full-source reconstruction, mathematical token equivalence and outer table structure all pass.
- `LOCAL_LAYOUT_BUILD_20260905_CONTROL_REVIEW.md`: independent control-delta PASS for the script hash above; report SHA256 `505bf6bd7ed1664a413e23204255bf6acd984a39cb15ad0979812901bbb25d8a`. Acceptance and lifecycle algorithms remain unchanged from the dual-reviewed original local script; only the declared source/path/review-file rebinding and original-main preservation check differ. All 18 regression methods, built-in self-test and read-only preflight passed independently.

Under the user's existing confirmation, one execution of this exact script may now exclusively create `build/layout-20260905-evidence`, then r0 and only upon its acceptance r1 at `build/layout-20260905-r0` and `build/layout-20260905-r1`. None of these targets was accessed before consumption of both reviews. No root reuse, automatic replay, fifth pass, old evidence access, source overwrite, external effect or historical failure reclassification is authorized by this record.

This is bounded compile correction 2/3. Actual zero-overfull, metadata, page counts, two-root determinism, remaining-warning disposition, visual/content review and final integrity remain unproved until separately checked against actual outputs.
