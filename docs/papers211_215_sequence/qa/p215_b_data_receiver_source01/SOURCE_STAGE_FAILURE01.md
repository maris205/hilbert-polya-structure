# P215 B DATA receiver source-stage procedural failure 01

2026-09-11 UTC. `PRESERVED / NO SCIENTIFIC OUTPUT RETURNED`.

Before writing the receiver, the source author ran this broad discovery query:

```sh
find docs/papers211_215_sequence/qa -maxdepth 2 -type f \
  \( -iname '*receiver*.cjs' -o -iname '*receive*.cjs' \) | sort | tail -30
```

Its displayed result contained only historical receiver source paths and no
path or member under `p215_b_initial_run01`. No P215 B stdout, stderr, exit,
manifest, receipt or scientific record was displayed or read, and the later
`--self-test` branch does not access the run path.

Nevertheless, `find` may traverse and stat directory entries that do not match
its final name filter. Therefore this command does not satisfy the literal
instruction not to inspect or query the future output directory. The receiver
implementation is preserved, but this source directory is on HOLD and claims
no precommitted-source credit. Do not run `--receive-initial` from this source
without an explicit root resolution. The conservative correction is a new
receiver source produced by a clean process with narrow, explicit reads only;
do not delete or overwrite this failed evidence.
