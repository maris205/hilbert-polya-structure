# HCS-C60 exact replay code

Status: `PREFREEZE MACHINE CANDIDATE / NO_REFRESH / NOT_RELEASED`.

This directory is a prefreeze release-integration candidate for the fixed
13-source C60 boundary.  The hardened exact-I/O, backend-preflight,
rollback-atomic promotion, self-excluding manifest, runner, and hostile-test
components have been ported from the released C59 machinery.  The C60
producer and checker remain independently written integration inputs.  Their
candidate SOURCE_STABLE bytes are now sealed as
`0b0dda0eddf0f5ec483cd34ae2c8c285d22b47886d231a126a5849a5162e179b`
and
`49b94955cf96862aaefabd5a5988c52b41975e8716a155e1f2ee33af55c7fd46`.
A pristine non-authoritative shadow replay passed both actual CLIs and the
independent source/G0/artifact/full-payload fixture.  These observations do
not authorize an official refresh, repository application, or release.

The intended theorem backends are fixed to:

- miniconda Python 3.12.3 with python-flint 0.9.0, SymPy 1.14.0,
  NetworkX 3.5, and jsonschema 4.25.0; and
- GAP 4.11.1 with TomLib 1.2.9, SmallGrp 1.4.1, and CTblLib 1.3.1.

No additional computer-algebra backend is part of C60.  In particular, PARI
and Singular are not inherited dependencies.

For a fully assembled disposable exact13 tree, `./run_all.sh` with no
arguments performs a nonmutating live replay.  A deliberate machine-tuple
refresh requires
`./run_all.sh --refresh-prefreeze --evidence-dir DIR`, where `DIR` contains
exactly `c60_group_evidence.json` and `c60_resolvent_evidence.json`.  Refresh
must promote exactly six files as one rollback-safe group: those two evidence
carriers, schema, certificate, independent check report, and the final
self-excluding scoped manifest.  A successful refresh must launch a clean
default replay before it can report success.  **Do not invoke refresh in the
authoritative repository while this status remains
`PREFREEZE MACHINE CANDIDATE / NO_REFRESH`.**

The planned scoped manifest has exactly 20 self-excluding entries: 13 code
files, two result prose files, and five promoted result files other than the
manifest.  The exact live code/results inventory has 21 entries.  Unknown
regular files, directories, symlinks, FIFOs, hardlinks, stale stages, or
foreign locks fail closed.

Promotion is persistently directory-fd bound.  The result parent, active
stage, transaction directory, and lock are rebound by device and inode across
precommit, every replacement and fsync, rollback, cleanup, and lock release.
Leaf seals include link count and ctime.  The runner creates its active stage
through the already-open result-directory fd, requires the exact basename
`.c60-stage-[A-Za-z0-9]{8}`, and compares that identity with the canonical
pathname at each orchestration boundary.  Exit 74 means
`ROLLED_BACK_VERIFIED`; exit 75 means `LIVE_COMMITTED_WITH_DEBRIS`; any other
failed atomic-child status means `LIVE_STATE_UNCERTAIN` and retained recovery
evidence.

This is not a same-UID concurrent-mutator security boundary.  A complete
rename/symlink/restore ABA hidden between `exec` of an external producer child
and that child's first path open remains outside the current interface.  The
trusted-parent contract therefore requires no concurrent pathname mutator
during replay.  Eliminating that launch window would require producer and
checker CLIs that accept and verify inherited directory fds.

The bootstrap trust boundary is also the parent process because the dynamic
loader runs before Bash.  A trusted parent must unset `LD_PRELOAD`,
`LD_LIBRARY_PATH`, `BASH_ENV`, `ENV`, `PYTHONOPTIMIZE`, `PYTHONPATH`,
`PYTHONHOME`, and `PYTHONSAFEPATH` before invoking
`/usr/bin/bash -p ./run_all.sh`; it must also leave the reserved
`C60_TEST_EVIDENCE_DIR` unset.  The runner rejects any surviving variable;
after binding its canonical active stage, it supplies that variable only to
the unittest subprocess.

After a machine tuple is locked and later formal or paper handoff changes the
root documentation, Route, or Batch authority, the locked pre-documentation
tuple becomes historical/frozen.  There is no claim that its producer or
checker will live-replay against subsequently changed documentation.  The
later documentation layer must cite the frozen machine hashes.

The intended semantic firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.  The fixed
30 `scope_nonclaims` leaves must all remain literal Boolean `false`.  This
scaffold makes no official refresh, authoritative promotion, paper, or
release claim.  Its machine payload continues to report
`PASS_PREFREEZE_CODE_RESULTS` and `promotion_authorized=false`.
