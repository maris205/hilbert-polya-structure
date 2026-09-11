# Ninth-lane actual execution evidence

2026-09-06 UTC. The two author-code checks are separate from independent
review and from root replay. No run or comparison is inferred from its
digest alone.

## Initial full scout

Invocation from the workspace root:

```bash
python3 -B docs/papers204_208_sequence/scouting/finite_algebra_ninth/record.py
```

Actual launcher completed with exit $0$. Its three child commands, exact
paths, UTC timestamps and status are in
[SUMMARY.json](execution_01/SUMMARY.json) and the per-run receipts.
The child interpreter was `/root/miniconda3/bin/python3`; each command was
`python3 -B execution_01/pilot.py` with the recorded absolute script path
and execution directory. This is a physical source snapshot, not an import
of the live pilot. Runtime environment fixed `LC_ALL=C`, `TZ=UTC`,
`PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1` and removed `PYTHONPATH`/
`PYTHONHOME`. No network or random sampling occurs.

| Run | Actual UTC start–end | Seconds | Exit | Result |
|---|---|---:|---:|---|
| initial run 0 | 07:33:25.659359–07:33:26.276889 | 0.617537 | 0 | 134 boxes, 33,301 states, 116,472 assertions |
| fresh run 1 | 07:33:26.277837–07:33:26.893789 | 0.615973 | 0 | same complete result |
| fresh run 2 | 07:33:26.895106–07:33:27.513779 | 0.618689 | 0 | same complete result |

[CANONICAL.json](CANONICAL.json) is the exclusive-created first stdout,
335,995 bytes, SHA-256
`6e13f54e51997c790008d2375d6f8c1fd1b6a3fa34d2be8577331c5f78911ed9`.
Its record digest is
`66534ce51b3049a5ee274ca6ec6650a6b2c148636ed466db1f6879829e0666ad`.
All three producer stderrs are empty. All three actual `cmp` operations
have exit $0$, empty stdout/stderr, and saved command/status receipts.
The three computational source pins before and after are byte-identical;
the three corresponding source snapshots are retained.

The complete cycle-length, height and fibre histograms, all maximum-fibre
targets, first deepest orbits and literal-comparison witnesses are in the
canonical. No numerical table is represented by a digest alone. Individual
transition arrays are reproducible from the source, and their digests are
additional diagnostics; they were not part of the promised full-stdout
payload.

## QEF static inverse follow-up, same original fields

Invocation:

```bash
python3 -B docs/papers204_208_sequence/scouting/finite_algebra_ninth/record_inverse.py
```

The pre-execution scope is [CORRECTIONS_AND_FOLLOWUP](CORRECTIONS_AND_FOLLOWUP.md).
It fixes the original primes $2,3,5,7,11,13$. The new source uses a
fixed-third-coordinate linear/singular decoder against directly generated
predecessor sets, with no imports or data reads from the first pilot.
[Its actual summary](inverse_execution_01/SUMMARY.json) and receipts record
all three fresh processes and comparisons, using the same runtime controls.

| Run | Actual UTC start–end | Seconds | Exit | Result |
|---|---|---:|---:|---|
| initial run 0 | 07:38:41.911052–07:38:41.986169 | 0.075123 | 0 | 4031 sources and targets, 16,893 checks |
| fresh run 1 | 07:38:41.986387–07:38:42.061918 | 0.075542 | 0 | same complete result |
| fresh run 2 | 07:38:42.062085–07:38:42.138187 | 0.076121 | 0 | same complete result |

[QEF_INVERSE_CANONICAL.json](QEF_INVERSE_CANONICAL.json) is the first
complete stdout, 10,347 bytes, SHA-256
`991dabcacdeef0ced6bbe6f3f6bebfd83d49b732e448318248a07ae2a7b37bf6`.
All producer stderrs are empty and all three actual raw `cmp` results are
zero with empty stdout/stderr. Four computational input pins are identical
before/after, and all four source snapshots exist. Branch/predecessor
digests are diagnostics; the checked exact sets are reconstructed afresh
inside each process, not read from a digest.

## Limitations, failures and seal

The initial historical-comparator label error is preserved and explained
in [the correction](CORRECTIONS_AND_FOLLOWUP.md) and
[source report](SOURCE_AND_COLLISION.md). Corrected historical interpretation
does not alter any frozen numerical output. A read-only summary command
had a syntax error and a lookup for a nonexistent `algebra_third/INTAKE.md`
returned exit $2$; neither was a numerical run or changed a file. The real
old LV definition was read successfully in `PROOF_AND_ADAPTER_NOTES.md`.
No producer/comparison failed. Direct source-access failures are listed in
the source report, without claims of unread evidence.

The recorders exclusive-create all run directories and canonical files;
they refuse overwrite. `seal.py` is an artifact-generation/check helper,
not a new mathematical execution. It records nine historical input pins,
checks both nested complete nonself manifests and all before/after pins,
checks the six raw comparison receipts and current raw byte equalities,
checks local Markdown links, and exclusive-creates a complete top-level
nonself `SHA256SUMS`. Its actual results live in `SEAL_CHECK.json`. Final
root handoff cites only successful completed checks, not this protocol
description alone.
