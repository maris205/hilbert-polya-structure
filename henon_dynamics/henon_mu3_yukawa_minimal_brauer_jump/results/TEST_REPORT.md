# HCS-C57 test report

The canonical release test suite covers strict JSON and 100,000-digit integer
parsing, deterministic gzip enforcement, exact C56/source/evidence inventory
rebinding, backend byte/version gates, producer/checker call-graph separation,
all eight theorem gates G0--G7, scalar-leaf and structural mutation rebound,
and the complete nonclaim firewall.

The 33-test canonical suite includes a fixed nine-target rollback-atomic
transaction.  Tests
inject a failure after each of the nine replacements for absent, existing and
mixed preimages; verify byte hash, size, mode and nanosecond mtime restoration;
require post-rename directory durability; bind staged and backup identities;
and reject missing, substituted or extra transaction entries, symlinks, FIFOs,
hardlinks, cross-filesystem requests, stale output, foreign lock replacement
and non-active stage directories.  It also tests short lock writes, fd-bound
mtime-before-fsync ordering, final-stage snapshot mutation, manifest-stage
replacement at the write boundary, and a hostile `BASH_ENV` bootstrap.  The scoped
manifest has exactly 28 self-excluded entries and the live code/results
inventory has exactly 29 entries including the manifest.

The default runner is nonmutating and checks byte, mode, mtime and inode snapshots.
It rejects optimized Python and import-path injection, runs from an external
working directory, suppresses bytecode generation, and never authorizes paper
or release promotion.  Its explicit `STAGED_VERIFIED`, `LIVE_COMMITTED`, and
`RELEASE_VERIFIED` states distinguish rollback-safe failures from the separate
`COMMITTED_WITH_DEBRIS`/`POSTCOMMIT_INCOMPLETE` outcomes that must not be retried.
Only atomic exit 74 is accepted as `ROLLED_BACK_VERIFIED`; every other nonzero
status, including 129/137/143 or a parent-shell signal while promotion is
active, becomes `LIVE_STATE_UNCERTAIN` and preserves the stage for recovery.
Because the dynamic loader runs before Bash, tests and documentation separately
enforce the trusted-parent requirement that `LD_PRELOAD` and `LD_LIBRARY_PATH`
be unset before exec; the runner detects their presence without claiming it can
reverse a pre-body loader constructor.
