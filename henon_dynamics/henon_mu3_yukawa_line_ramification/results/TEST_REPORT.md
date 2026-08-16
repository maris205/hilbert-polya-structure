# HCS-C58 test report

Status: `PREFREEZE_SCAFFOLD_TESTS_PASS`.

The canonical release-scaffold suite contains 45 tests and passed from an
external working directory under unoptimized Python with bytecode generation
disabled.  All transaction fixtures and hostile filesystem objects were
created under temporary directories; this audit did not run refresh, write an
official manifest, or promote any result.

The suite fixes the 14-file code allowlist, the six promoted result names,
the 21-entry self-excluding scoped manifest, and the 22-entry live
code/results inventory.  It rejects extra files and even empty directories in
either scoped directory, as well as symlinks, FIFOs, hardlinks, stale stages,
foreign locks, cross-location sources, stage inode replacement, and manifest
write-boundary substitution.  The atomic promoter persistently binds the
result, stage, and transaction directories by descriptor/device/inode.  Two
benign hostile fixtures rename the result parent and substitute a symlink at
precommit and immediately after the first replacement: the foreign directory
is never touched, the precommit live preimages remain exact, and the
post-replacement case is classified unknown with lock/transaction evidence
retained.  The manifest has an independent result-parent substitution test,
and the shell runner creates its stage through that persistent fd before
rechecking the pathname at every orchestration boundary.  A separate shell
probe performs a result-parent rename/symlink/restore ABA around fd-relative
stage creation and proves that the stage lands only in the bound result
directory while the foreign directory remains byte-exact.  This does not
claim protection against a same-UID ABA hidden wholly between external-child
`exec` and the producer's first canonical-path open; until that producer
interface accepts inherited directory fds, the release trust contract
requires absence of a concurrent pathname mutator.

The six-target rollback transaction is tested after every replacement for
absent, existing, and mixed preimages (18 injected failures).  Tests require
exact byte, mode, and nanosecond-mtime restoration; fd-stable source and
backup snapshots; directory durability after rename; identity-bound cleanup;
and distinct exit 74 `ROLLED_BACK_VERIFIED`, exit 75
`COMMITTED_WITH_DEBRIS`, and all-other-status `LIVE_STATE_UNCERTAIN`
outcomes.  The runner retains an unclassified stage and requires a clean
nonmutating replay after any successful refresh.

Producer/checker separation is checked both statically and semantically.  A
shared local-evidence/no-child sentinel fixture invokes the real producer `build_payload` and
checker `expected_payload`; strict deep equality and semantic diff count zero
are mandatory.  The same fixture now executes the complete core mutation
rebound, rejects all seven hostile semantic mutations, and statically binds
the tame degree-36 row mutation to `tame_theta36_local_rows` while forbidding
the retired `theta36_local_rows` leaf.  The suite also fixes the 15 top-level payload keys, exact
scope and nonresult firewalls, theta-at-precision-40 authority, delta
nondependency, and the absence of decomposition-Frobenius, bad-Euler,
epsilon-factor, root-number, automorphy, and Artin-holomorphy claims.  The
v2 targeted gates additionally bind all four surviving p=3
decomposition/inertia pairs and their deep-C3 normality/actions, the complete
order-two ToM/character-class map, PARI `nf_get_sign`/`polsturm` carriers,
the 900/950/1000 Krasner/separation/multiplyback authority rows, and the
six-boolean reflection Hensel bridge.  The
checker PARI scratch directory must use the hidden
`.c58-checker-pari-` prefix inside the already verified common stage parent;
an unbound default temporary directory is rejected by static contract.  The
request bytes, stable fingerprint, device, inode, link count, size, mode,
mtime, and ctime are rebound after the PARI child.  A hostile same-byte,
same-mode, same-mtime inode substitution is rejected in a direct helper test.

Backend gates cover only the fixed PARI/cypari2 Python, FLINT/SymPy Python,
and GAP/TomLib/SmallGrp/CTblLib executables, including exact CTblLib version
`1.3.1`.  The privileged Bash bootstrap rejects
optimized Python, import-path injection, `BASH_ENV`, and loader-variable
presence while documenting that loader constructors execute before the
script body.
