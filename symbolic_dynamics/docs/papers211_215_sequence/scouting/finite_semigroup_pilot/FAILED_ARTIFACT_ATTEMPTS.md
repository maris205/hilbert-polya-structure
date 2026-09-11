# Preserved post-pilot artifact failures

These are author-authored observations of actual interactive failures, not
native stdout/stderr receipts manufactured after the event. Original files
remain unchanged. Neither command below invoked the scientific producer.

## First frozen artifact audit

Command: `/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/scouting/finite_semigroup_pilot/lock/audit.py audit`.
It stopped at frozen `lock/audit.py` line 113 with:

```text
AssertionError: ('unfrozen observed runtime file', '/usr/lib/locale/C.utf8/LC_CTYPE')
```

The original interactive traceback was observed, but this first invocation was
not separately captured into native stdout/stderr/exit files. The later
`postrun_diagnostic_v2/AUDIT_RECAPTURE_NATIVE_RECEIPT.json` identifies a NEW
read-only invocation, not a retrospective receipt for the first one. The
original strict audit checks sequentially and stops at the first missing path.

## First posthoc diagnostic implementation

Command: `/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/scouting/finite_semigroup_pilot/artifact_closeout.py collect`.
The interactive process returned exit 1 at line 130 with:

```text
AssertionError: launcher discrepancy differs from preserved failure
```

That script incorrectly expected that the first missing path was the only
missing path. It had created the empty `postrun_diagnostic/` directory but
failed before writing a diagnosis or launching the frozen artifact audit.
Thus it made zero new scientific invocations and zero artifact-audit
subprocess invocations. Its source is retained unchanged as
`artifact_closeout.py`. This prose is not a native receipt for that failure.

A subsequent complete, read-only comparison of the original receipt against
the original pre-execution pin list found two launcher-only missing paths:

1. `/usr/lib/locale/C.utf8/LC_CTYPE` — 353616 bytes,
   SHA-256 `e4b5576b19e40be5923b0eb864750d35944404bb0a92aa68d1a9b96110c52120`.
2. `/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache` — 27002 bytes,
   SHA-256 `a8af5639c6f7d2cf9c39f5b4166a3ad8c08a4ee2af1fc82ff67c10d045e615f6`.

The scientific child and the preflight import probe each have zero observed
runtime files outside the recorded prelock. This is only an observed-set
comparison, not certification that their dependencies were exhaustively
enumerated. `artifact_closeout_v2.py` records the complete two-path finding;
it does not add either file to old pins, alter frozen code, rerun science,
or change the original strict audit's failure into a pass.
