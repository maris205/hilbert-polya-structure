# P209 B — exact delta execution and role log

2026-09-07 UTC. Documentary evidence only. The accepted assessment is
[DELTA.md](DELTA.md); the checker explicitly does not write that decision.

## Physical intake

`delta_intake.py` under `launch_delta.py intake delta_intake_01` actually
checked the complete initial 1,298-payload package, copied the original seal
to `INITIAL_REVIEW_SEAL.sha256` and the original UNASSESSED delta to
`INITIAL_DELTA.md`, then copied 15 exact response, instruction and root
inspection inputs to `delta_intake_01/context`. Its complete 29-payload seal
is `5a655c39e3e32d433bd2449635c958980fcb60ef6412cd06719df15300e7fb97`.
The intake did not accept the response. Physical copies retain the consumed
instruction controls even when root later updates live lifecycle files.

## Failed attempt, correction and successful attempt

The original `launch_delta.py check delta_check_01` actually completed its
documentary child with exit 0, then failed with outer exit 1 at the exclusive
create of `ALL_COMMAND_RECORDS.json`. The child's existing file contained
its eight real `cmp` command records. The original scripts and all streams
remain unchanged. `delta_check_01/OUTER_FAILURE.actual.json` is an exact
record of the returned tool failure, not a synthetic process log.
`seal_failed_delta_attempt.py` then performed a separate documentary
post-failure closure: child exit 0, eight comparisons exit 0, wrapper input
maps unchanged, original outer exit 1. Its resulting 64-payload seal is
`6ea48c853dfdf769b1b315d6f55d5b0341e68d6a466e5ae0f95e2a5be2494740`.
No original wrapper receipt was fabricated and that wrapper is not PASS.

`launch_delta_v2.py` uses a separate `WRAPPER_COMMAND_RECORDS.json`.
`check_delta_v2.py` changes only its output/source version roles and adds
mandatory checks of the sealed failed attempt and exact intake originals
(moving STATE/PIPE controls retain their exact physical copies). The actual
ordinary `diff -u` calls both returned 1 because changes exist; their full
concatenated output is `DELTA_ADAPTATION.diff`, SHA-256
`03176a0ca4343e9fd7e4d4431d5ca7a6feba01df33217e4e8a47158bb2f495f2`.
Neither unchanged original script is overwritten.

Successful wrapper invocation, actually completed exit 0:

```text
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p209_b/delta_check_02/never_created_parent_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/reviews/p209_b/launch_delta_v2.py check delta_check_02
```

The wrapper recorded one actual documentary child command, its full
stdout/stderr, actual exit 0, early/late maps and 5,166 equal before/after
input pins. The child recorded 128,227 equal before/after complete consumed
path maps, 32 exact role aliases (all 13 older aliases retained), 8 selected
alias resolutions, recaptured configuration/runtime/TeX inventory and eight
actual comparisons, all exit 0. There are no new mathematical executions,
builds, renders or image views. `DELTA_EVIDENCE_RESULT.json` has SHA-256
`65929ef451d8294840b1455eb5aaef927f2587ee750c7967110002ffee40d5ea`.
The complete 64-payload successful seal is
`8987d60fc57d05379e161d7631a508b325aca6f2edc4f08758065b9208d5d36c`.

The eight comparisons are: root B raw run 1 versus raw run 2; each raw root
run versus original B canonical; live versus frozen Round1 PDF, verifier,
canonical and author manifest; exact response versus its physical intake
copy. This does not compare unlike author/A/B canonical formats as raw data.

## Scope and original preservation

The new root pair was independently inspected as documentary evidence,
including its 85 actual commands, source-only child capsules, unchanged
source adaptations, complete raw outputs and known-input/runtime closure.
The checker imports only unchanged B recording/runtime primitives; it does
not import or execute scientific verifiers, root inspectors or root
recorders. Root's actual code executions remain root executions.

After the successful evidence check and the same reviewer's assessment,
only the current `DELTA.md` role was replaced. `REPORT.md`, `FINDINGS.json`,
all scientific code, canonical, build/view logs, original audit records and
all initial nested packages remain unchanged. Current census is a separate
`CURRENT_FINDINGS.json`. The final complete outer seal supersedes only the
current `SHA256SUMS` role, after the exact old seal was preserved physically.
The original 1,298 entries retain their original logical names: 1,297 at
the same paths and original DELTA through its single named alias.

The project skill caused preservation-before-replacement, exact-response
inspection, full dependency rechecking, explicit failed-attempt retention
and same-reviewer assessment. No broad novelty/source search or proof
extension was needed for this exact no-change response. All original
evidence limits and **OWNER_AMBER / HOLD_EXTERNAL** remain.
