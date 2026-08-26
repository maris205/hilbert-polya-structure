# Paper 15R reproduction entry

`reproduce.sh` is the sole eventual entry source.  It is a POSIX shell prefix
followed by one byte-bounded embedded Python coordinator.  In the current
source profile, the shell emits exactly `E_POSSESSION_UNAVAILABLE` with status
1 before resolving a path, changing directory, starting Python, creating an
endpoint, or probing the platform.  `CURRENT_RUN_PROFILE_ACCEPTED=false` and
`PROFILE_HASH_IS_EVIDENCE=false` are intentional: source presence and the
frozen HC digest cannot authorize execution.

The embedded `successor_execution_gate_entry(acceptance)` callgraph root accepts
only an exact frozen `ExternalProfileAcceptance` object owned and validated by
a separate successor execution-governance gate before the profile window.  It
binds the exact HC digest, one exact window class, independent gate digest,
lease identity, revocation epoch, and an unrevoked state.  P, L, and G validate
the inherited object before their first governed action.  No environment
variable, path, FD, socket self-test, euid check, or source toggle can construct
that object.  The named root is an external future-governance interface, not a
currently authorized top-level branch: only a later gate may separately
authorize its invocation mechanism.  The current entry passes `None`, the shell
remains fixed false, and no current source path is run-ready.

The runner is intentionally restricted to native Linux x86_64, LP64,
little-endian operation on a trusted, non-Byzantine kernel and the byte-bounded
checked-in sources.  The future execution environment must provide delegated
cgroup v2 and unprivileged nested user, mount, and PID namespaces with the exact
UAPI operations required by the design.  Missing, denied, ambiguous, partial,
or non-unique possession evidence terminates once as
`E_POSSESSION_UNAVAILABLE`; there is no fallback, retry, process-moving
substitute, pathname-stat substitute, or compatibility protocol.

## Process and capability ownership

The shell resolves the physical repository/package/entry identities and then
execs Python so the same process becomes P.  P remains in the initial user,
mount, PID, and cgroup namespaces, is single-threaded and a child subreaper,
normalizes every catchable signal disposition to the default, blocks exactly
the handled set into one signalfd path, and exclusively owns entropy,
cgroup mutation, retained `/proc` roots, pidfds, FD 5 peers, authentication,
D-M2 audits, and the mirror ledgers.  P never receives a capability for a
private generation root or package lock pathname.

After external acceptance, P creates L atomically in the guardian cgroup with the exact 88-byte `clone3`
ABI, `CLONE_NEWUSER|CLONE_PIDFD|CLONE_INTO_CGROUP`, and the exact U1 maps
`65534 65534 1`.  L retains only its bootstrap endpoint and setup FD 10/11,
drops to outer UID/GID 65534 with empty capabilities and groups, creates U2 with
the exact maps `0 65534 1`, unshares the private mount and child PID namespaces,
and performs its sole later clone to create G as inner PID 1.  P pidfd-reaps L.

G is a single-threaded inner PID-1 subreaper, outer 65534 and inner 0.  It owns
the private mount propagation, tmpfs `/tmp`, private proc, abstract
`SOCK_SEQPACKET` package lock, root/lock/member capabilities, object ledgers,
all worker creation, RPC, drain, waitid reap, and capability-relative cleanup.
Every target, requester, generator, holder, or actor is a direct G child born
atomically in the workers cgroup.  A trusted first-instruction stub closes the
inherited actual EP_G alias before any other descriptor operation, then closes
the cgroup FD, installs the final descriptor set and seccomp boundary, and
crosses `SANITIZED -> ADMIT -> SOURCE_READY -> START`.

The only descriptor-state contracts are:

```text
STDIO_BARRIER                    {0,1,2,8}       -> {0,1,2,8}       -> {0,1,2}
STDIO_SOURCE_BARRIER             {0,1,2,3,8}     -> {0,1,2,8}       -> {0,1,2}
STDIO_SOURCE_ROOT_BARRIER        {0,1,2,3,8,9}   -> {0,1,2,8,9}     -> {0,1,2,9}
STDIO_SOURCE_RPC_AUDIT_BARRIER   {0,1,2,3,4,5,8} -> {0,1,2,4,5,8}   -> {0,1,2,4,5}
```

FDs 0/1/2 are unique EOF/stdout/stderr pipes; FD 3 is the exact read-only
source; FD 4 is a child-unique RPC seqpacket; FD 5 is the P-owned authenticated
audit seqpacket; FD 8 is the unique admission barrier; FD 9 is a duplicate of a
registered generation-root capability.  FD 6, FD 7, and every unregistered
descriptor are closed.  Setup FD 10/11 never reaches a worker.

## v14 endpoint boundary and execution fence

The actual endpoints are the one `accept()` result owned by P (EP_P) and the
one `connect()` result owned by G (EP_G); there is no handoff, duplicate, or
alternate pair.  Each endpoint receives the exact one-instruction accept-all
cBPF, `SO_LOCK_FILTER`, three EPERM negative probes, and two raw readbacks.
Their seven-item local receipts HP/HG and P's four-item reciprocal holder
matrix HM feed MECH and the five-line actual-endpoint contract H.  The exact
41-item, 2928-byte hook/custody profile has digest
`1d2c38d460a280b7a4555f6ec0df0be2f81bf3ee5b05ecf8c554295a21cd8cb1`;
it narrows a future deployment model but supplies no runtime evidence.

G completes its local drop and HG before epoch-2 `CGROUP_PROBE_REAPED`.  After
L is pidfd-reaped, P proves sole-G placement and a close-first denial child,
then freezes HP/HM before `LAUNCHER_REAPED`.  The only boundary sequence is the
revised `PRIVILEGE_DROP_RELEASE` (RE), `GUARDIAN_READY` (YE),
`GUARDIAN_READY_ACK` (AE), and `BOOTSTRAP_SEALED` (SS).  C14 has six coordinates
`(RE,YE,AE,SS,E_PG,E_GP)`, exactly 15 closed rows, and 17 independently computed
raw failure predicates.  Buffer construction, parse success, or a private
state transition never sets a coordinate.

SS is committed by the actual complete Seal enqueue.  G may create the package
lock, root, suite child, generator, verifier, or any governed write only after
that same exact framed Seal also returns in full from the actual EP_G send; the
immutable `V14SealFence` is the sole argument to `run_after_preflight`.  P's
later exact Seal receipt closes the live audit window but is not write
authority.  A post-enqueue/pre-return G death is row-15 audit success with no
live execution.

## Fail-before-write and transaction

Before binding the package lock or creating any candidate/result root, the
reachable main path proves the scalar syscall/structure ABI; exact U1/U2 and
private mount/PID/proc state; cgroup delegation, atomic membership,
freeze/thaw/kill/ECHILD/empty removal; retained-dirfd `openat2` and
`renameat2` exchange/replacement behavior; credentialed AF_UNIX seqpacket EOF;
two simultaneous reciprocal and crossed Unix-diag pairs; and final nested
pidfd-getfd possession under D-M2.  D-M2 has exactly ENTER, ACK, EXIT, and
EXIT_ACK, uses only FD4/FD5/FD8 and PREFLIGHT_PROBE/RUNTIME_CHILD, reuses each
registered child pidfd, retains exactly four child/G proc capabilities across
both snapshots, audits every snapshot-fixed G socket candidate, and preserves
the fixed 21-tag `P15R-FD-AUDIT-TRANSCRIPT-v6` schedule.  Success and failure
share one reverse close/EBADF tag-18 unwind; ABORT and MISSING tags retain the
first failure.  Multi-slot phases are always FD8, FD4, FD5; only epoch-1 uses
`PREFLIGHT_PROBE`, while epoch-2 and all other children use `RUNTIME_CHILD`.
The same retained pidfd is audited at registration, SOURCE_READY, each
audited-RPC running reference, and each frozen reference while FD4/FD5 remains
live.  G consumes the matching one-use phase/slot sequence before ACK.  P's
single long-lived `/proc` root is an exact O_RDONLY directory capability with
an identity/CLOEXEC ledger opened before the workers-cgroup handoff can release
G's first probe; each row uses four fresh `openat` directory
capabilities, and each exact ten-field pidfd ledger moves
RETURNED→VALIDATED→CLOSED_PROVED.  Tag 21 is recomputed from the two snapshots,
fresh peer fstat, every acquired-FD close state, and the live G-holder count;
it is not a literal assertion.  The exact P signal mask and all catchable
dispositions are revalidated at every allocation-barrier entry and after the
matching EXIT_ACK.  Any ambiguous close leaves G quiesced and sends no EXIT;
top-level containment closes each retained child pidfd exactly once and moves
its mirror and ten-field ledger to `CLOSED_PROVED` only after whole-tree exit
and reap are proved.  If reap containment is incomplete, every still-retained
pidfd remains open through P exit, its ledger becomes
`AMBIGUOUS_CRASH_ONLY`, and no exact terminal receipt is permitted.

Before Seal, `GuardianWorkers.spawn` admits only the exact child-1/child-2
cgroup-probe budget.  After the exact Seal full-return fence, the same local
spawn gate rejects every probe and requires the identical endpoint-bound fence
for every normal clone.  G then binds the exact abstract lock and runs the
remaining frozen registry: checked-in verify-only, canonical A
generate-plus-verify, canonical B generate-plus-verify, all nine checked/A,
A/B, and checked/B byte comparisons, then the top 173-test requester.  Package
methods create independent full synthetic repositories and reply only after
method freeze, `FROZEN_NOREFS`, capability cleanup, cleanup commit, and thaw.

V14 failures stop both carrier admission and governed work.  Once P has the
HP/HM no-alternate-reader ceiling, it may become the sole authenticated
survivor only after the retained G pidfd has been killed/reaped by containment.
It drains the actual EP_P to exact EOF, preserves the failure-time raw frame
separately from that terminal EOF, closes EP_P with immediate EBADF, and only
then freezes C14/Q/raw17.  Every terminal-drained carrier and retained
endpoint-bound full-return receipt is reconciled before classification.  In
particular, an exact queued Seal advances SS and produces the immutable row-15
success audit even when G died before its send returned; it never produces a
failure row or a Seal fence.  The seventeen raw predicates are separately
derived from typed packet, direction, length, grammar, session, identity,
cgroup, attestation, state, EOF/deadline/crash, and errno evidence before the
precedence winner is selected.  Canonical `LAUNCHER_REAPED` is retained only as
the carrier-chain predecessor, never as the next-carrier candidate or an old-form
extra; only an additional actual enqueue can set its direction-owned E bit.
The terminal reader retains every datagram—including zero-data ancillary
records, positive prefixes, truncation flags, ancillary violations, malformed
bytes, unknown forms, and recognizable wrong-direction old forms—safely closes
any received rights, and continues until a clean data-empty, ancillary-empty,
flag-zero exact EOF.  A row-15 terminal audit also requires that exact EOF and
the unbroken holder ceiling.  Each observation freezes its event-time carrier
prefix: a pre-cut out-of-slot old form sets its actual direction E bit, while a
post-cut observation moves only to downstream secondary evidence and cannot
change C14 or raw17.  The canonical Launcher is excluded by predecessor event
identity, so a second byte-identical Launcher remains an actual duplicate/E
observation.  `DUPLICATE` requires exact bytes matching a retained
current-bootstrap predecessor (or a repeated exact observed frame); `REPLAY`
requires an independently retained authenticated consumed coordinate, so a
mere wrong-session field never guesses replay and the current one-shot process
has no such prior-coordinate evidence; and
`REORDERED` requires a later carrier index rather than merely a nonexpected
form.  Launcher identity is never compared to the guardian coordinate.
`WRONG_ATTESTATION` is independently derived by exact comparison with each
available expected/canonical carrier frame.  A future carrier with no retained
preimage oracle proves only the independently supported order/state failures;
neither attestation failure nor an unavailable historical identity is guessed.
`MISSING` is independently true whenever the next
carrier remains uncommitted at the reconciled checkpoint, even when EOF, crash,
timeout, malformed, or another losing bit is also true.  A failure before
HP/HM, an ambiguous pidfd/endpoint close, a live producer, missing EOF, or a
failure while completing terminal reconciliation remains an explicitly
unreconciled `exact_row_claimed=false` tombstone and does not claim one of the
fourteen exact failure rows.  Once the holder ceiling exists, no provisional
tombstone is created unless later terminal evidence becomes ambiguous;
successful exact freeze replaces the terminal context with the single failure
or row-15 receipt.

The v9/v14 wire intentionally carries P's Release attestation and G's HG as
lowercase digest commitments, not their owner-local raw preimages.  Under the
frozen HC model P and G are trusted non-Byzantine owners: G authenticates and
causally binds P's exact Release digest, while P binds G's HG digest into
MECH/H and the Ready/ACK/Seal chains.  The peer cannot recompute the absent raw
owner-local preimage, and this source does not present that trust-bound digest
join as independent peer-side mechanical evidence.

FD 5 and P-G authentication use closed exact datagrams/frames.  P owns globally
monotone audit handles and per-endpoint serials.  A single immutable
`AUDITED_SPAWN` byte object travels FD5 to P and FD4 to G; G reports those exact
bytes to P and waits for confirmation before reservation or clone.  Rich spawn
results bind the authorization coordinates, original outer hash, target,
method, purpose, handle, child, status, both complete stream byte/chunk/hash
receipts, and an independently recomputed capability hash before one-time
consumption.  The v8 success
suffix requires `FINALIZED_ACK`, terminal receipt, clean FD5 EOF, validated
requester reap, byte-equal child-reap acknowledgement, and auth-reap
reconciliation.  Only then may global FINAL freeze, kill, reap, prove
`populated 0`, clean each registered object, close the workers capability in
the last cleanup result, close the abstract lock, and emit the single `EXIT`.
EOF, crash, SIGKILL, missing objects, path drift, or incomplete cleanup is never
interpreted as success.

## Current state

This README describes a static source contract, not observed platform
behavior.  During the third remediation-authoring attempt, no wrapper,
preflight, generator, verifier, suite, namespace, cgroup, endpoint, lock, or
cleanup path was run.  `CURRENT_RUNTIME_ATTESTATION_PRESENT=false` and
`CURRENT_EXECUTION_AUTHORITY=false`; a later independent gate must first accept
and pin the exact HC/window contract before any execution receipt can exist.
