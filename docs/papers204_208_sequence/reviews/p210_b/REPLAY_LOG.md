# B actual replay and reusable interface

Scientific interface: run `/usr/bin/python3.10 -I -S -B verify.py` with
`PARAMETERS.json` beside that script. There are no scientific positional
arguments, seeds or hidden data files. The fixed parameters list exactly
N=1,...,12. For strict source-only startup also pass
`-X pycache_prefix=ABSOLUTE_NEW_ABSENT_DIRECTORY` before the script.
Do not use `-O`, site/dist packages or an existing bytecode cache.

Every inner command uses only this explicitly supplied environment:

```text
PATH=/usr/bin:/bin
LANG=C.UTF-8
LC_ALL=C.UTF-8
TZ=UTC
```

No inherited environment values, HOME assignment, credential file or
`/proc/environ` were recorded. `/proc/self/maps` and owned `/proc/*/stat`
observations have the narrower disclosed roles below.

## Executed commands

The exact full argv, cwd, safe environment, prestart epoch/nanoseconds,
numeric native return, end time, owned PID/session/group settlement and
full raw stdout/stderr bindings are in each `ATTEMPT.json`/`RESULT.json`.
These are actual subprocess records, not commands reconstructed from a log.

| Evidence | Actual result |
|---|---|
| `native/produce01` and `produce01/commands/run_1` | Native 0; one actual full stdout, 51,129 checks. Canonical adopted by exact byte copy, not normalization. |
| `native/pair01` and `pair01/commands/run_1`, `run_2` | Parent and both scientific children native 0; 51,129 checks each. |
| `pair01/commands/cmp_pair`, `cmp_1_canonical`, `cmp_2_canonical` | All three actual `/usr/bin/cmp` commands native 0, full empty raw streams retained. |
| `native/compare01` | Native 0; full post-commitment semantic adapter output, 198,189 checks. It reads the three canonicals and their declared role pins, never imports author/A code. |
| `native/pdf_cmp01` | Native 0, actual PDF byte comparison. |
| `native/view_bind01` | Native 0; binds already actual page observations, does not itself view pages. |
| `native/audit01` / `native/audit02` | Initial historical-control role error native 1 retained; corrected evidence audit native 0. |

For each science run the actual child argv is system Python with
`-I -S -B -X pycache_prefix=<new absent path>`, then the local
`tools/runtime_probe.py`, copied `source/verify.py` and the runtime-record
destination. The probe supplies `sys.argv=[target]` to the standalone source.
The instrumentation driver itself also uses `-I -S -B` and a separate absent
cache prefix. Source/canonical copies were made into absent run directories.

`produce01` had 3,651 source/runtime file keys. `pair01` had 3,653, including
both canonical copies and all 509 original Round1 input pins. Both have 40
configuration/presence keys, and identical decoded before/after full-byte
file keys and configuration/membership records (gzip container bytes need
not match). Driver and child cache prefixes remained
absent. Source-only stdlib, interpreter, shared libraries, loader, locale,
gconv and declared configuration resource keys are retained, not host-tree
copies. `REPLAY_KEYS.json` identifies the gzip ledgers and observations for
root's independent replay.

## Coverage and nonclaims

The observed Python import/open audit starts after installing the hook;
before/after maps and complete module file paths complement the resource-key
snapshots. All existing observed reads/module/maps paths were in those keys;
no `.pyc`, `.pyo`, site-packages or dist-packages was observed in a scientific
child. This is bounded Python observation, not a continuous OS or startup
trace. The outer native transport launchers originally used `-I -S -B`
without a separate cache prefix; their start-source hashes and full native
streams are retained, but source-only startup/module coverage is claimed
only for the inner driver and scientific children. The later audit transport
does use its own absent cache prefix. Nothing here retrospectively changes
the original launch.

The final evidence audit fully re-read current dependency bytes, checked
all recorded before/after ledgers, 62 completed command bindings and 515
complete byte comparisons. Its own in-flight stdout/result were deliberately
not included in that count; their completed binding is checked by the final
seal audit. No numeric success token substitutes for a missing native result.
Historical A/root commands were inspected as preserved evidence, not rerun
by this reviewer. Root's forthcoming fresh pair remains a separate gate.
