# P209 final lifecycle root-inspector preparation

Preparation only. The preparer authored the lifecycle adaptation and revision04;
this is documentary infrastructure, not independent mathematics/manuscript review,
actual execution of this inspector, or final acceptance. Root must inspect the
complete source and invoke it after the actual lifecycle and sealing commands pass.

`inspect.py` imports only the standard library. Its sole subprocess is native
`/usr/bin/cmp`, invoked only during root's future run with full command, streams,
exit and input-before/after records printed in the result. It never imports or
executes any old auditor/helper, scientific code, builder or viewer, and performs
no artifact writes. Root must retain its full native invocation/output/exit.

The two full ledgers are reopened twice, all original host resolutions twice,
all 50 recorded manifests, the complete current 8231-payload paper, all 1534 old
local links and every new lifecycle link. Exactly two old-paper physical copies
substitute in the original ledger; prior 94 named link roles remain original
documentary data and do not add any ledger alias. Current lifecycle-ledger paths
have no substitutions. Exact one-line paper-seal replacement, immutable author
status/adoption, original 46-payload package, seven pre-update payloads, native
five-payload lifecycle attempt, both runtime samples, full declared resources,
final receipt/report pins and complete final nonself inventory are checked.

Root invocation (replace both uppercase values only with the actual sealing
result, not a prediction; leave attempt fixed):

```sh
env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B docs/papers204_208_sequence/qa/p209_lifecycle_root_preparation/inspect.py --attempt lifecycle_01 --expected-manifest-sha256 ACTUAL_FINAL_SHA256 --expected-payloads ACTUAL_FINAL_PAYLOADS
```

`INPUT_PINS.json` fixes immutable source, gate and preservation originals.
`STATIC_CHECK.json` records only AST/compile inspection, not target execution.
The four nonself preparation payloads are sealed by `SHA256SUMS`. No actual
inspector/lifecycle/science/build/view command was launched by this preparation.
HOLD_EXTERNAL and OWNER_AMBER remain in force; this is P209 only.
