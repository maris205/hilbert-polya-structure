# HCS-C58 exact replay code

This directory implements the source-locked certificate for the filtered
inertia and Artin conductors of the frozen degree-27 line field.  The
producer and checker have separate mathematical call graphs; they share only
the neutral strict-I/O and backend-preflight modules.

The default runner is non-mutating.  A grouped, rollback-safe refresh is
available only through its explicit maintainer flag.  Generated evidence is
canonical JSON (deterministic gzip where applicable), and no absolute scratch
path, runtime, decomposition-Frobenius choice, bad Euler factor, epsilon
factor, or root-number assertion is part of the certificate.

The slow regeneration path for maximal orders is evidence construction, not
the default semantic checker.  The checker rebuilds the certified number
field from the shipped transformed polynomial, exact change of generator,
and maximal integral basis, then independently replays prime decompositions,
different exponents, group filters, ramification laws, conductors, and global
discriminant identities.

The three release backends are fixed by executable hash and version:

- `/usr/bin/python3` for PARI/cypari2;
- `/root/miniconda3/bin/python3` for python-flint, SymPy, and jsonschema;
- `/usr/bin/gap` with the locked TomLib, SmallGrp, and CTblLib 1.3.1 packages
  for the exhaustive labelled-action and character-class filters.

Run `./run_all.sh` with no arguments for a nonmutating replay of the live
package.  A deliberate PREFREEZE refresh requires
`./run_all.sh --refresh-prefreeze --evidence-dir DIR`, where `DIR` contains
exactly `c58_arithmetic_evidence.json.gz` and `c58_group_evidence.json`.
Refresh promotes exactly six files as one rollback-safe group: the two
evidence carriers, schema, certificate, check report, and finally the
self-excluding scoped manifest.  A successful refresh always launches a
second, clean default replay before reporting success.

Promotion authority is directory-fd based: the result parent, active stage,
transaction directory, and lock are rebound by device/inode across
precommit, every replacement and fsync, rollback, cleanup, and lock release.
The manifest reads result leaves through the bound directory descriptor, and
the runner creates the active stage through its persistent result-directory
fd and compares that fd with the required pathname at every orchestration
boundary.  Atomic promotion and manifest writes therefore never redirect
into a substituted directory; an observed parent substitution stops with an
unknown live-state outcome and retained recovery evidence.

The shell boundary is not a defense against a same-UID adversary that performs
a complete rename/symlink/restore ABA wholly between `exec` of an external
producer child and that child's first path open: the producer CLI currently
accepts canonical paths, not inherited directory fds.  The trusted-parent
contract therefore also requires no concurrent pathname mutator during a
release replay.  Closing that remaining launch window would require a future
producer interface that accepts and verifies inherited result/stage fds.

The bootstrap trust boundary is the parent process because the ELF loader
acts before Bash executes this script.  A trusted parent shell must unset
`LD_PRELOAD`, `LD_LIBRARY_PATH`, `BASH_ENV`, `ENV`, `PYTHONOPTIMIZE`,
`PYTHONPATH`, `PYTHONHOME`, and `PYTHONSAFEPATH` before invoking
`/usr/bin/bash -p ./run_all.sh`.  The runner fails closed if any survives; it
does not claim to undo code that a loader constructor already executed.
