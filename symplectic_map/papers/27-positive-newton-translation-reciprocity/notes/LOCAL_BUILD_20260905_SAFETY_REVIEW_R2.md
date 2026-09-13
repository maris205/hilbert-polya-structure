# Paper27 local-build safety review — R2

Decision: PASS
Reviewed SHA256: 49fba6fa53a6ecf7f4ebd23b2dca72db2a1079d83437088cf89b0c94e6936a9a

Date: 2026-09-05. This is an independent, targeted prebuild code-safety re-review. The initial `LOCAL_BUILD_20260905_SAFETY_REVIEW.md` FAIL remains unchanged and applies to its earlier script hash. This PASS applies only to the exact revised script hash above, not to an actual build, mathematical completeness, or release-grade acceptance.

## Scope and observations

Read the full revised `LOCAL_BUILD_20260905.py` (680 lines) and full `LOCAL_BUILD_20260905_TEST.py` (176 lines). Re-reviewed the original lifecycle blocker and the additional runtime-binding, log-header, recorder-spelling, and content-suffix changes. Retained the approved single-writer, nonadversarial local-host scope from the initial review; no new Host/Runner, crash-restart, distributed execution, or external-effect requirement was introduced.

No build/evidence path was accessed, including existence checks. No `--build` or `--preflight` was run. All commands used `python3 -B` for the pure tests. Only this fresh R2 note was written during this re-review.

## Resolution of B1

The revised `run_command` (lines 265–328) catches the initial post-launch communication exception and enters cleanup before emitting a terminal command receipt. For incomplete communication, lines 284–309 temporarily ignore a further SIGINT, attempt SIGTERM then SIGKILL with bounded three-second communication waits, tolerate an absent process group, record other signaling/communication errors, and perform a bounded explicit wait when the return code remains unknown. Lines 310–312 close both output pipes after these ordinary cleanup paths.

Lines 315–323 distinguish a real return code from `UNKNOWN`, record stream completeness and cleanup errors, and raise typed `ChildUnreaped` if the child was not reaped. Lines 667–671 map that state to `HOLD_UNREAPED_CHILD_NO_RESTART`, rather than claiming termination or initiating a retry. When cleanup does reap the child, lines 324–325 re-raise the original communication exception. Ordinary nonzero exits and stderr still fail acceptance. This resolves the cancellation, absent-group race, and further-timeout defect reported as B1 for the earlier hash.

This is not a promise of cleanup after SIGKILL of the interpreter, hardware failure, or every imaginable runtime failure. Such a promise is outside the explicitly approved bounded workflow. An unreaped HOLD requires later state inspection and must not be automatically restarted.

## Other changes

- Lines 79–85 and 246–253 bind the explicitly enumerated 17 PyMuPDF runtime files to a fixed hash frame; lines 458 and 528 check it around parsing, and line 643 checks it before any build pathname is touched. These are read-only bindings and do not add output locations or installation/network activity.
- Lines 397–398 exempt only the two exact normal `-file-line-error` administrative header spellings. They do not suppress a header with an appended error message or generally weaken error detection.
- Lines 367–370 admit a single leading `./` spelling before applying the same finite local-name allowlist. `../`, `./../`, and repeated `././` paths remain rejected; raw recorder bytes and the declared cross-root normalization are unchanged.
- Lines 446–447 reject known proof-section/clause/boundary/conclusion anchors after References. This is a useful finite check, not a claim of exhaustive semantic completeness; actual output and mathematical/content review remain separate.
- The exclusive fresh-directory/file creation, fixed three output namespaces, no old-namespace scan/reuse/deletion, fixed shell-free commands, no automatic retry, and pending-independent-review result wording remain intact.

## Test evidence

Executed the complete pure regression suite: **18 test methods passed**. It covers cancellation cleanup, absent-group signaling race, timeout escalation, unreaped HOLD, success, exact diagnostic headers, recorder path spelling, reference/content checks, warning retention, environment shape, and mocked citation consistency. These are synthetic/mocked tests, not real subprocess or PDF/build acceptance tests.

Executed the built-in `--self-test`: **2 positive and 11 negative cases passed**.

Ran two additional in-memory fake-process cases using the reviewed test helper:

1. Initial communication `OSError`, simulated signaling failures, a cleanup communication `OSError`, then successful reaping at return code -9: original exception identity preserved, all three cleanup errors recorded, stream completeness true, both pipes closed.
2. Ordinary return code 7: nonzero status preserved, acceptance rejected, pipes closed, and no unnecessary signal.

Rechecked the script SHA256 after testing; it matched the reviewed hash. No concrete safety blocker remains within this review scope. Actual execution must still use the required hash-bound aggregate prebuild PASS gate, and any generated outputs require the separate independent postbuild review already specified by the plan.
