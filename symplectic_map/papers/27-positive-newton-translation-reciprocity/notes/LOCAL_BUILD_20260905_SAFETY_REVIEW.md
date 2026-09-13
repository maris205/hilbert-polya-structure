# Paper27 local-build safety review

Decision: FAIL
Reviewed SHA256: 9638c09a43e0c2dc32d6f8b2792be17fc5a8859ac6e59c6e8d7d22b69222b76c

Date: 2026-09-05. This is a bounded, independent prebuild code-safety review, not a mathematical review, completed-build acceptance, or release decision.

## Scope and method

Read the complete `LOCAL_BUILD_20260905.py` (611 lines), `LOCAL_BUILD_20260905_PLAN.md`, and `BUILD_RECOVERY_REASSESSMENT_20260905.md`. The latter documents the user's approval of the simple, fresh-directory local workflow. Assumed one writer and a nonadversarial local host; did not require distributed execution, automatic crash recovery, or arbitrary-crash liveness.

No build/evidence path was accessed, including existence checks. `--build` and `--preflight` were not run. Executed `python3 -B .../LOCAL_BUILD_20260905.py --self-test`: `SELF_TEST_PASS`, 2 positive and 11 negative cases. Also exercised the actual `run_command` function with an entirely in-memory fake subprocess and intercepted writes/signals; this launched no subprocess and performed no build/evidence I/O. This review note is the reviewer's sole file write.

## Blocking finding

**B1 — A live child is not cleaned up when command communication is interrupted or the timeout cleanup itself raises.** `run_command`, lines 248–261, starts a separate-session process but has no encompassing `try/finally` to terminate/reap it and close its output pipes on exceptional exits. In particular, `KeyboardInterrupt` during `communicate(timeout=190)` is not handled there. It reaches the build-level `except BaseException` at lines 599–603, which writes `FAIL_PRESERVED_NO_RETRY` and re-raises while the child can remain alive and continue modifying the fresh root. A normal terminal interrupt need not reach that child because `start_new_session=True` is set at line 250. This is an ordinary cancellation path, not an adversarial race or arbitrary-crash recovery requirement.

The pure fake-process test made `communicate` raise `KeyboardInterrupt` and observed exactly these calls:

```text
write SYNTHETIC.intent.json
communicate(timeout=190)
KeyboardInterrupt propagated
no killpg / terminate / kill / wait call
```

The same missing enclosing cleanup also leaves `os.killpg` exit races (`ProcessLookupError` at lines 256 or 260) and a further `TimeoutExpired` at line 261 outside a cleanup guarantee. On these paths there is no explicit closing of the two pipe objects or assured child reaping before return from the command helper.

Required correction before execution: give every successfully created child an exception-safe cleanup path that performs bounded termination/escalation as needed, tolerates an already-exited process/group, reaps the child when possible, and closes both output pipes. Preserve the original exception/partial evidence and retain no-retry behavior. Add a pure fake-process regression for cancellation and the signaling/timeout failure paths; ordinary successful and nonzero/timeout receipts must remain truthful. No new Host/Runner protocol is needed.

## Checks without additional blockers

- Lines 19–22, 467–475, and 583–594 confine explicit build destinations to the three reviewed new namespaces and their descendants; there is no old-namespace scan, reuse, deletion, rename, or fallback-suffix branch.
- Lines 98–175 use non-following ancestor opens, exclusive directory creation, and `O_EXCL | O_NOFOLLOW` file creation. Existing target names stop rather than being reused. File verification checks regular-file status and single-link identity. Root 1 is only attempted after root 0 passes.
- Lines 45–48 and 244–250 use fixed argument vectors, no shell invocation, `-no-shell-escape`, empty stdin, closed inherited descriptors, and resource limits. No network operation or package installation appears in the reviewed code. The subprocess-lifecycle defect above is the exception to otherwise explicit timeout handling.
- Lines 479–510 preserve per-step bindings, snapshots, and manifests; lines 514–539 compare the intended outputs with a narrowly declared recorder-root normalization. Lines 506–508 and 536–539 correctly leave warning disposition and final independent review pending rather than asserting release-grade acceptance.
- Lines 570–582 gate execution on a hash-bound independent PASS before touching a build pathname. Failure handling has no retry or cleanup/deletion of generated artifacts. `--self-test` uses synthetic data and exits before bindings or build-path operations.

The present FAIL is solely for B1 against the exact SHA256 above. It does not reclassify any old failure, change the user's authorization, or claim an actual build has run.
