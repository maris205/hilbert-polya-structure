# Initial artifact output — exact trailing-LF packaging correction

2026-09-06 UTC. This artifact-only supplement preserves the closed initial
report, its seven-entry manifest, all stopped attempts and every old file.
It corrects the distinction between complete JSON content and exact raw
stdout; no mathematical, build or viewing process is rerun here.

B's actual delta checker discovered that `attempt_03.actual.json` records
147,133 characters from the real tool output, while the saved
`attempt_03.stdout.json` contains 147,134 ASCII bytes and ends in two LFs.
The local patch used to archive that output appended one extra final LF.
Thus the old file is complete untruncated JSON content but is **not** the
byte-exact captured stdout. Any earlier shorthand calling that old saved
file raw stdout must be read with this correction; parsing equivalence
does not establish byte identity.

The original successful tool output was still available in the active
execution record. Its exact 147,133-byte ASCII content has now been saved
separately as [attempt_03.stdout.exact.json](attempt_03.stdout.exact.json),
without changing the old file. A fresh read-only stdout roundtrip compared
the recovered file to that retained actual tool-output string, including
all trailing bytes; it is exactly equal. ASCII validation makes that
comparison byte-preserving. An additional actual byte check established:

```text
old_saved_bytes == exact_captured_bytes + b"\n"
```

The actual roundtrip and byte-check result is recorded in
[PACKAGING_CORRECTION.actual.json](PACKAGING_CORRECTION.actual.json).
The digests and exact sizes are:

| Preserved object | Bytes | SHA-256 |
|---|---:|---|
| Original archived JSON, with extra LF | 147134 | 457e3da885163d5888a95aa165f34e53580a687c63ada34d43f2568cb4ec46aa |
| Recovered exact captured stdout | 147133 | 5f5487bad8a7c11c73b6a6adb251f90bfa365be42ec91d4b6152ed965b334afd |

The parsed JSON objects are also equal, but this is a separate weaker
observation. The actual result still contains P207-B-ART1 as an open
initial-package Minor, with 39,623 checks and 599 point-in-time inputs;
this packaging correction does not turn it into a clean initial PASS.

The preserved `check_initial.attempt_01.py` and `.attempt_02.py` source
snapshots likewise have one transport-added blank final line (two final
LFs). They preserve the executed source content/version, not byte-exact
source-file digests at those earlier failure instants. No historical source
digest was asserted in either actual failure receipt. The final executed
`check_initial.py` itself has its original one final LF and unchanged
recorded hash. All snapshots remain untouched; no broader source-change
claim is made from this packaging detail.

The old `SHA256SUMS` remains the immutable seven-file seal as it existed
before this later supplement. A separate `SUPPLEMENT_PINS.sha256` binds
this clarification and the exact sibling; it does not overwrite or
retroactively expand that historical seal. The actual B delta may now
validate both byte identities explicitly, preserve its own earlier stop,
and document its acceptance or remaining concern. This supplement itself
does not accept B's delta. `OWNER_AMBER / HOLD_EXTERNAL` remains.
