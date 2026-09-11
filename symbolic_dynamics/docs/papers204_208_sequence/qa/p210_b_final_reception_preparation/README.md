# P210 B final reception — prepared source, not executed

The 768-line [receiver](receive_p210_b_final.py) is bound to the actual final
B package: 441 nonself payloads, seal
`57b7b7919846e3ff5890543f0373439b03cc7f0cf0e896b9db38cd14d5171462`.
Preparation has not executed this receiver or any old writer, receiver,
scientific verifier, native command, build or page-view program.

## Exact source and input contract

[INPUT_BINDINGS.json](INPUT_BINDINGS.json) pins 59 named documentary inputs,
four actual root launch/completion interfaces, three completed new B native
parents, both full phase summaries and the actual final external seal return.
The latter is session 31532, final chunk b8b01c, native exit 0, 2,164 seal
checks; its original call did not explicitly supply workdir or independently
record stderr/process-group data. Those fields are not reconstructed.

The actual B delta inspector (514 lines) and final sealer (144 lines) were
read completely, not imported or executed. Thirteen accepted helper
functions are copied verbatim: eleven from the initial receiver and two
from the strict receiver. [SOURCE_ADAPTATION.json](SOURCE_ADAPTATION.json)
lists the exact functions and source identities.
[SOURCE_FROM_INITIAL_DIFF.diff](SOURCE_FROM_INITIAL_DIFF.diff) contains the
complete source difference from the accepted initial receiver, including all
new final-phase/native/role/runtime/seal helpers and main.
[SOURCE_DIFF.diff](SOURCE_DIFF.diff) contains the complete change after
root's already-read 750-line source; that exact source is retained as
[ROOT_READ_UNBOUND_750.py](history/ROOT_READ_UNBOUND_750.py).

Only the initial B DELTA and SHA256SUMS map to their exact physical
history/initial_before_delta copies. All 407 original payloads remain
preserved, including 406 unchanged in place. Initial REPORT/FINDINGS stay
initial; the actual current findings are separate. Preserved-role pins
are workspace-root-relative, 408 roles including the initial seal.

## What the root receiver will check

The receiver requires the actual final manifest and complete physical
441-payload membership. It rechecks all B original 120,840 rich keys;
reconstructs accepted initial-root 120,840 + 55 and strict-root 3,558 + 75
logical maps; and reconstructs the exact 1,906-key no-change map against
the still-unmodified 1,496-payload pre-Round2 paper.

It checks the full 121,013-key decoded common delta interval, the three
after-only decision/ledger inputs, every recorded role group, actual raw
module/maps samples, independently reconstructed current 40/61 original-B
configuration scopes and 3,121 strict resources / 41 strict configuration
names. Gzip containers are bound separately, not falsely required to be
byte-identical. All current read keys are fully hashed again before return.

It reconstructs all 995 Python comparison operand roles and performs those
complete byte comparisons without calling native cmp. Actual phase
summaries remain 1,978,529 / 1,978,541 checks. All 66 original completed
native records are bound: 63 initial (including two actual native-1
infrastructure failures) plus preservation/before/after. The 29 genuine
local Markdown links use the accepted code-stripping parser. Four prior
root parents and ten strict groups retain their exact recorded roles.

The receiver emits a small exact `current_read_keys_outside_B_common`
map. Convert each B common `resolved/bytes` record to receiver
`real/size`, retaining sha256/symlink; union with those extra records.
This reconstructs the complete actual current read map and its canonical
compact sorted JSON SHA256 without copying a full host ledger again.

Old overwritten, unconsumed PDF states remain historical keys only. No old
A nested host ledger is expanded. Actual B-E1/B-E2, inherited A-E1,
source-access limits, initial-source reconstruction, missing historical
recorder/start evidence and bounded outer runtime observations remain.

## Preparation evidence and root invocation

[STATIC_CHECK.actual.json](STATIC_CHECK.actual.json) and
[STATIC_NATIVE_RETURN.actual.json](STATIC_NATIVE_RETURN.actual.json) record
the AST/data-only preparation check, not a receiver run or host re-audit.
A real earlier AST-only parse found one missing closing brace at line 597.
Its exact source is preserved in
[DRAFT_PARSE_FAILURE_SOURCE.py](history/DRAFT_PARSE_FAILURE_SOURCE.py),
with the actual native traceback in
[DRAFT_PARSE_FAILURE_NATIVE.actual.json](DRAFT_PARSE_FAILURE_NATIVE.actual.json).
The unexecuted source was corrected before final static validation.
A separate historical-key source edge was corrected before execution:
validate the old logical metadata, then compare physical history SHA/size
and its own resolution. Neither correction is called a failed receiver run.

After reading the final complete source, diffs, bindings and preparation
seal, root may invoke the receiver from the workspace, replacing the final
argument with the independently checked preparation seal hash:

```sh
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p210_b_final_reception_preparation/never_created_receiver_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p210_b_final_reception_preparation/receive_p210_b_final.py final-B-actual-only PREPARATION_SHA256
```

Execute before modifying paper lifecycle/whole-manifest or creating Round2.
It writes stdout only and explicitly does not write root acceptance or
claim paper, Round2, terminal or five-paper completion. The preparation
itself claims no receiver PASS. OWNER_AMBER / HOLD_EXTERNAL.
