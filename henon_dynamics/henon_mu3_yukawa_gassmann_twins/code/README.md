# HCS-C59 exact replay code

Status: `PREFREEZE_SCAFFOLD / NOT_RELEASED`.

This directory is the fixed 13-source implementation boundary for the C59
certificate.  The producer and checker reconstruct the same 15-key G0--G7
payload through separate theorem call graphs.  Shared imports are restricted
to strict canonical I/O, stable fingerprints, and deterministic backend
preflight.  The producer may use `c59_group` and `c59_resolvent`; the
checker may use `c59_checker_resolvent` and execute
`c59_checker_group.g`, but it may not import producer theorem helpers.

The only theorem backends are:

- the fixed miniconda Python 3.12.3 with python-flint 0.9.0, SymPy 1.14.0,
  NetworkX 3.5, and jsonschema 4.25.0; and
- GAP 4.11.1 with TomLib 1.2.9, SmallGrp 1.4.1, and CTblLib 1.3.1.

No other computer-algebra backend is part of C59.  In particular, the C58
PARI and Singular lanes are not inherited dependencies.

Run `./run_all.sh` with no arguments for a nonmutating replay of the locked
pre-documentation `PREFREEZE` machine tuple.  A deliberate prefreeze refresh requires
`./run_all.sh --refresh-prefreeze --evidence-dir DIR`, where `DIR`
contains exactly `c59_group_evidence.json` and
`c59_resolvent_evidence.json`.  Refresh promotes exactly six files as one
rollback-safe group: those two immutable evidence carriers, schema,
certificate, independent check report, and finally the self-excluding scoped
manifest.  A successful refresh must launch a clean default replay before it
can report success.

This replay claim is deliberately layered, as in C58.  After the formal and
paper handoff changes the root documentation, Route, or Batch authority, the
verified pre-documentation machine tuple is historical/frozen.  There is no
claim that its producer or checker will live-replay against those changed
documents; their exact formal locks are expected to reject that mixed state.
The later documentation layer must cite the frozen machine hashes rather
than reinterpret a post-handoff runner failure as a machine-result failure.

The scoped manifest has exactly 20 self-excluding entries: 13 code files, two
result prose files, and five promoted result files other than the manifest.
The exact live code/results inventory has 21 entries.  Unknown regular files,
directories, symlinks, FIFOs, hardlinks, stale stages, or foreign locks fail
closed.

Promotion is persistently directory-fd bound.  The result parent, active
stage, transaction directory, and lock are rebound by device and inode across
precommit, every replacement and fsync, rollback, cleanup, and lock release.
The runner creates its active stage through the already-open result-directory
fd and compares that identity with the canonical pathname at every
orchestration boundary.  Exit 74 means `ROLLED_BACK_VERIFIED`; exit 75 means
`LIVE_COMMITTED_WITH_DEBRIS`; any other failed atomic-child status means
`LIVE_STATE_UNCERTAIN` and retained recovery evidence.

This is not a same-UID concurrent-mutator security boundary.  A complete
rename/symlink/restore ABA hidden between `exec` of an external producer
child and that child's first path open remains outside the current interface.
The trusted-parent contract therefore requires no concurrent pathname
mutator during replay.  Eliminating that launch window would require producer
and checker CLIs that accept and verify inherited directory fds.

The bootstrap trust boundary is also the parent process because the dynamic
loader runs before Bash.  A trusted parent must unset `LD_PRELOAD`,
`LD_LIBRARY_PATH`, `BASH_ENV`, `ENV`, `PYTHONOPTIMIZE`,
`PYTHONPATH`, `PYTHONHOME`, and `PYTHONSAFEPATH` before invoking
`/usr/bin/bash -p ./run_all.sh`; it must also leave the reserved
`C59_TEST_EVIDENCE_DIR` unset.  The runner rejects any surviving variable;
after binding its own canonical active stage, it supplies that stage variable
only to the unittest subprocess.  It does not claim to undo code already
executed by a loader constructor.

The resolvent evidence owns its exact schema descriptor in source.  No
scratch path, development schema sidecar, pilot file, runtime, or
certificate-selected arbitrary path is authority.  The canonical invariant
is the scaled integral `eta` in `alpha_i=L*d_i`; the evidence contains
only modular coefficient arrays, not expanded characteristic-zero
coefficients.

All 30 `scope_nonclaims` leaves are literal Boolean `false`.  The semantic
firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.  Machine success does not claim a
paper or release.
