# Findings and retained boundaries

Verdict: no established blocking source defect in the declared exact finite,
root-owned regular-artifact workflow. This is not an unconditional operational
PASS. All five boundaries below must accompany any root source reception.
Line numbers refer only to checkpoint.py SHA256
4851f2c1c39335c1d0f0de270c2d3ae9637a96991425a7cd1891e32da6f9b0d5.

## F1 — Bootstrap and effective SSH no-write policy are external prerequisites

Source 268–280 fixes only a bounded set of Git/SSH settings. Source 387–409
checks selected executable/repository roles; binding 533–542 pins receipt
originals and compares roles. It does not inspect or semantically certify all
SSH configuration, include files, hooks/commands, agent behavior, loaders or
other runtime dependencies. Imports already occurred before main's checks.
The contract explicitly requires prior independent runtime/startup reception
and disclaims full hermetic runtime closure.

In particular StrictHostKeyChecking=yes is not by itself a proof that
known_hosts cannot change: OpenSSH's separate UpdateHostKeys mechanism can
accept post-authentication server keys and write UserKnownHostsFile, and may
be enabled by default. See [OpenSSH UpdateHostKeys](https://man.openbsd.org/ssh_config#UpdateHostKeys).
The actual host's settings were not read here. Root must establish the
effective no-write conditions, including relevant SSH side effects, in the
separate fresh gate. If that evidence is absent or incompatible, operation is
blocked. This is not evidence that the current host is misconfigured, nor
permission to edit host configuration. A source delta to change SSH options
would require separate review rather than silent substitution.

## F2 — The 50-second bound is not a Python read, memory or whole-phase bound

blob 109–128 performs stream.read() without a size argument. It verifies the
whole key afterward; it does not compare expected per-file length against
lstat size before allocating/reading. Stale oversized regular content can
therefore consume time or memory before mismatch refusal. Inventory and the
capture loop have no whole-phase deadline. Native communicate 326 has a
50-second timeout, with the specified bounded handling; its output is buffered
in memory, not streamed continuously into the preopened evidence files.
Process creation and evidence/fsync operations are not covered by that timeout.

The source never claims those stronger bounds, and the accepted protocol's
guard is explicitly native-command-only. This is a material operational
limitation, not a tested passing resource bound or demonstrated scope escape.
Root must not translate LIMIT/MIN_FREE/timeout literals into measured capacity,
reserved storage, bounded peak memory, a capture deadline or a successful run.
The official [Python subprocess documentation](https://docs.python.org/3/library/subprocess.html#subprocess.Popen.communicate)
corroborates EOF/exit behavior and in-memory buffering.

## F3 — Failures before the phase try may lack a phase FAILURE.json

execute 583–635 performs binding/source/plan/inventory/capacity checks,
creates and prints the new run, writes run metadata, checks prior seals and
index ownership, then creates the phase directory before its try block.
A failure during that early portion can leave a printed partial run or a
partial local metadata directory but no phase FAILURE.json. A failure before
mkdtemp can leave no run at all. This follows directly from the source; it was
not induced as a test.

Root's actual enclosing tool request and every actual return/error must be
preserved even when no phase-local report exists. Absence of FAILURE.json is
not success, and no retry/cleanup permission is implied. The source does not
issue a success result on this branch.

## F4 — Phase completeness is regular-file plus alias completeness, not all-entry isolation

complete_manifest 496–509 enumerates p.is_file(), excludes every symlink and
hashes every named regular manifest file. It does not separately reject every
FIFO/socket/device entry or repeat a final directory census after all reads.
Frozen global census 252–255 similarly checks selected regular files and
aliases; declared live/frozen group members are explicitly required regular.

Thus it supports the contract's finite, exclusively root-owned regular
product attachment, not a theorem of hostile concurrent-filesystem or
all-entry completeness. Root must receive and preserve that exclusive finite
capture through the successor checks. If automatic rejection of every
nonregular phase entry or a stable after-census is newly required, this exact
source does not implement that stronger condition; a distinct source delta
is needed. No unexpected entry or concurrent adversary was observed here.

## F5 — Native, local-object, remote and root-product outcomes are different

A command needs actual zero exit, EOF, no timeout and no exception. Signal
group identity is derived from requested new-session ownership, not an
invented sampled process-group observation. If a leader is already reaped,
the source does not invent continuing ownership to kill arbitrary descendants.
Missing pipe EOF remains unknown; no full process-tree/escaped-writer
termination proof is supplied.

Stage may leave index/objects on failure; commit may leave an unreferenced
object; ordinary push may change remote before the subsequent observation,
local CAS or late root reception fails. FAILURE.json conservatively reports
possible partial Git/remote state. No rollback/retry/cleanup is implemented.
A returned native phase result still has phase_seal null; a root receipt and
actual enclosing product originals must precede the nonself phase manifest.
The four operation and reception gates cannot be collapsed into one wrapper
exit, one manifest hash or a source audit verdict.

