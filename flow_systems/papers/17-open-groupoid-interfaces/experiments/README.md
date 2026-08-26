# Paper 17 reproduction entry

`reproduce.sh` is the sole top-level reproduction entry and accepts no
arguments.  It must be invoked only once under the exact implementation gate.

The entry rejects recursion first, validates the deterministic environment
and physical root, classifies an already occupied exact lock path as
concurrent exit 3, scans every other cache/task residue as exit 5, and then
uses one atomic `mkdir` to acquire its lock.  Only a lock acquired by that
successful operation is exempt or cleaned by the process.

The run verifies the checked-in package without changing its metadata or
bytes, creates two distinct fresh generation roots, verifies both, compares
all ten artifacts across all three copies byte-for-byte, runs exactly 180
explicit tests including the 48 semantic and 42 package mutations, and
removes only its two fresh roots and owned lock.  There is no automatic retry.

The package is a finite control envelope, not mathematical or publication
authority.  Route, composition, manuscript, release, archive, Git, and public
synchronization remain outside this entry.
