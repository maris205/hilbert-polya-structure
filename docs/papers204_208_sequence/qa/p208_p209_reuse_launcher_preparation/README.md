# One native P208/P209 reuse-checker launch

Preparation only. Neither this launcher nor the checker has been executed.
Root must read the complete launcher, verify this four-payload preparation's
seal and physical membership, and retain the actual outer native command,
exit, stdout and stderr. This package does not itself certify an actual run.

The only child is the exact sealed `p208_p209_reuse_preparation/inspect.py`,
executed directly with system Python. No old or checker Python code is
imported, bootstrapped or executed inside the launcher process. No science,
build, renderer or page-view command is run. The checker preparation remains
unchanged at seal `8fc25ed0775c40e38ec8e006eae53f5d762f92a3496bda6349872a46c6adacfc`.

## Exact future launch

From cwd `/root/autodl-tmp/symbolic_dynamics`, after replacing only the final
placeholder by the independently verified SHA-256 of this preparation's
`SHA256SUMS`, root's actual native command has this shape:

```text
/usr/bin/env -i PATH=/usr/bin:/bin LANG=C.UTF-8 LC_ALL=C.UTF-8 TZ=UTC /usr/bin/python3.10 -I -S -B -X pycache_prefix=/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p208_p209_reuse_01/unused_launcher_cache /root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/qa/p208_p209_reuse_launcher_preparation/launcher.py launch-current-p208-p209 LAUNCHER_PREPARATION_SHA256SUMS_DIGEST
```

Output is fixed to the fresh physical `qa/p208_p209_reuse_01/`. Existing output
is refused; there is no overwrite, retry or alternate-mode option. The child
has the same exact four-variable environment and cwd, but the distinct absent
`unused_checker_cache` prefix. Its complete argv is pinned in the source and
saved before spawning. Both parent and child use `-I -S -B`; parent additionally
requires the exact isolated system search path. Mismatching inherited
environment values are never recorded. Parent observation records the actual
four-variable environment only after verifying it is exactly the allowed one.

## Actual evidence produced by a future run

- Parent launch intent, child pre-spawn intent, immediately persisted spawned
  PID/owned process-group identity, and native completion/cleanup facts.
- Complete separate raw `checker.stdout` and `checker.stderr`; stdout is the
  full original checker JSON result, not a truncated or normalized substitute.
- Physical copies of the exact launcher and checker source bytes, plus the
  complete checker-preparation five-payload/six-file keys, own-preparation
  keys, and all 128 fixed checker-input keys before and after.
- Full source-only system-stdlib, bounded shared-library-root, configuration
  and observed-parent input keys before and after. Configuration presence,
  nested entry membership, resolution and symlink state are retained. The
  two new known-input ledgers use lossless gzip with exact JSON/compressed
  byte counts and hashes; no historical host trees or large original ledgers
  are copied.
- Actual early/late parent module and raw file-backed-map observations, and
  the first and last successful child `/proc/PID/maps` samples. Sampling is
  every 0.25 seconds while the child is observed alive; only first/last raw
  samples are retained, with successful-sample count and all sampling errors.
  They may be the same single sample for a short-lived child. Retained sample
  files must lie in the known before-key; no continuous tracing is claimed.

The native timeout is 600 seconds after spawning. Cleanup uses only the
group created by `Popen(start_new_session=True)`: TERM, bounded grace, KILL
if still present, bounded disappearance probes, and leader reap. Actual
group-absence probes are retained. Signal/probe/reap uncertainty prohibits
settled stream hashes and a final seal. Required cleanup signals, timeout,
nonzero exit, malformed JSON or failed input/observation closure prohibit
PASS even if the process group is subsequently settled.

SIGINT/SIGTERM become recorded interruptions; during the narrow spawn/handle
publication interval they are deferred until the actual PID is available for
cleanup. Default handling is restored before exit. SIGKILL, machine failure
or an unreturned process handle cannot be claimed safely settled: preserve
the actual outer failure and existing evidence, and do not infer a PASS.

Once group disappearance is confirmed, a normal or failed attempt can seal
its own small physical output package. After-read errors are retained per
path when possible; they do not erase the original before-key or raw streams.
An unsettled attempt instead records `UNCLOSED_NO_SETTLED_HASHES_OR_SEAL` and
does not hash potentially changing streams or create `SHA256SUMS`.

Launcher success is
`PASS_NATIVE_READ_ONLY_REUSE_LAUNCH_NOT_BATCH_ACCEPTANCE`; it also requires
actual child exit zero and the checker's exact read-only-reuse status.
Failed settled attempts are `FAIL_PRESERVED`. Preserve any failed output and
ask root to choose the next explicitly reviewed fresh attempt, not overwrite
`reuse_01`. The final launcher stdout is a compact receipt pointer; it cannot
replace root's actual native exit record or reading the full child output.

This is a documentary reuse launch, not a new mathematical execution, build,
visual inspection or batch acceptance. Known-file and sampled-observation
closure is not historical OS/kernel reconstruction. `HOLD_EXTERNAL` remains.

`PROVENANCE.json` discloses the original source patterns used. The independent
static desk reviewed the initial draft only; `STATIC_CHECK.json` distinguishes
that review, implemented corrections, and final main-agent static checks.
