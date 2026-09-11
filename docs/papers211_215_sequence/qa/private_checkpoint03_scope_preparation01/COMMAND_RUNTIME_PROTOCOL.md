# Proposed checkpoint03 command/runtime protocol — not executable authority

No invocation in this document has occurred. The four actual future phases
require four separate root decisions after reception of the preceding phase.
The current source-only preparation has no operative executor. Root must
receive a new complete source whose immutable exact-file mapping replaces
the old roots/BASE/34-count/12MB constants; no old source, failed version or
accepted receipt may be edited.

## Reused protocol and limits

The controlling accepted original is
../root_checkpoint_inspection02/RECEPTION.md. Its actual old executable is
../private_checkpoint_preparation02/checkpoint.py,42,576 bytes, SHA256
4b34a7735121f0fc51a996daca0c26b7d5e282098708aec8b9bb6e6a98b13ff3.
The executed old plan was895,111 bytes, SHA256
7d3408300c1dc7f9d0d69ac6ef0e359fe8b8d65493877cbf01cd0350f5bdd8f6.
Only nine exact old-run boundary files were pinned, not the recursive archive:
see PRIOR_PROTOCOL_LOCAL_ONLY_BOUNDARY.json. They remain local-only.

Use /usr/bin/python3 -I -S -B for the eventual reviewed executor, with
its exact resolved interpreter/source pins recorded before invocation.
Later phases execute the physically frozen executed_source.py, not live source.
The four commands are separate tool calls with actual plan/phase digests;
there is no all-phases, retry, force, delete, pull, reset or cleanup mode.

All Git commands use this fixed argv prefix, followed by the phase-specific
array below, never shell interpolation:

    /usr/bin/git
    --git-dir=/root/symbolic-dynamics-private-sync-accepted-20260907.git
    -c core.hooksPath=/dev/null
    -c core.fsmonitor=false
    -c core.untrackedCache=false
    -c gc.auto=0
    -c maintenance.auto=false
    -c commit.gpgSign=false

The original mirror allows only its explicitly reviewed read-only HEAD,
origin and porcelain-status calls, with optional locks and fsmonitor disabled.
No Git operation is issued in the non-repository workspace root as if it
were a worktree. Never add origin or rewrite either Git configuration.

The isolated child environment is constructed explicitly, not inherited
wholesale: PATH=/usr/bin:/bin, LANG=C, LC_ALL=C, TZ=UTC,
GIT_OPTIONAL_LOCKS=0, GIT_TERMINAL_PROMPT=0, GIT_CONFIG_NOSYSTEM=1,
GIT_CONFIG_GLOBAL=/dev/null. The accepted Git/SSH recipe additionally used
the existing HOME/USER/LOGNAME/SSH_AUTH_SOCK/SSH_AGENT_PID roles when present
and an explicit GIT_SSH_COMMAND:
`/usr/bin/ssh -o BatchMode=yes -o StrictHostKeyChecking=yes -o ConnectTimeout=20 -o ConnectionAttempts=1`.
Do not create/alter credentials, agents, host files, known_hosts or Git config.
Any current authentication/startup change is a new operational boundary.

Only stage/tree checks receive GIT_INDEX_FILE, pointing to a uniquely owned,
initially absent isolated index. Only commit-tree receives command-local
GIT_AUTHOR_NAME/GIT_COMMITTER_NAME=mariswang and both emails
wangliang.f@gmail.com, as verified from the accepted baseline. Existing
system variables are read as existing roles, never repurposed as task paths.

## Native and outer records

Before spawning each native command, create its exclusive ATTEMPT containing
full argv/cwd/exact environment/input bytes/timeouts, and open complete raw
stdout/stderr files. Record spawn success/failure, actual pid and process-group
handling, final native exit or signal, timeout/cancellation and cleanup outcome.
Keep application/native status distinct from wrapper/tool exit. Use a fresh
process group and the accepted50-second per-native-command bound; timeout
preserves failure, signals only that owned group, and waits at most5 seconds
after TERM and3 after KILL. Size feasibility is not a measured execution-time
guarantee. Never retry a partially written index/object phase automatically.

Capture each outer tool request and each actual yielded session/poll/final
return. Yield early (about1 second initially, then bounded polls no longer
than30 seconds) so the root can continue communicating. A yielded process
without a native final exit is UNKNOWN/UNCLOSED, not a success. Missing
actual session/stream/exit evidence blocks the phase seal. Never predict a
future pid, native result, frozen path, tree, commit or phase digest.

Before/after input reading, compare complete exact selected membership,
bytes/SHA256/mode/blob OIDs and unaliased regular-file roles; use opened-fd
and endpoint stat checks in the new executor. Preserve exact complete selected
package manifests and original-location historical mappings. Protected
mirror/bare config, HEAD/default-index/packed-ref/alternate roles and executable
pins must stay unchanged, apart from the separately allowed push-phase
compare-and-swap of bare main. Do not claim complete Git/SSH/ELF/configuration
runtime closure, continuous startup tracing or host hermeticity. This is
private documentary synchronization, not reusable strict scientific evidence.

## Four independently gated phases

In the arrays below BASE is exactly
7d43cb323adf7d27326263b8ce4158d4eefff43a and BASE_TREE exactly
64feab3a9eff397179a6670aff5b1ff7d0595796. NAMES is the sorted final approved
explicit Git-path set. Any added optional bridge requires a new exact plan.
TREE and COMMIT mean only actual successful earlier native outputs.

### 1. Capture — no Git mutation

Root grant binds the exact final plan hash, executor hash, immutable source
mapping, selected size ceiling and phase=capture. Confirm roles with actual
rev-parse/symbolic-ref/remote and clean-mirror status; confirm actual remote:

    ["ls-remote","--exit-code",
     "git@github.com:maris205/hilbert-polya-structure.git","refs/heads/main"]

Require precisely BASE and refs/heads/main. Recheck capacity and every selected
source. Create a new tempfile.mkdtemp-owned run under /root with a narrow
validated prefix and a distinct initially absent isolated-index role.
Exclusively save the approved plan and exact executed source. Exclusively
capture only approved individual input files into their mapped frozen paths,
with raw before/copy/after comparisons and full membership/key checks.
No recursive archive or whole-history copy, Git object, index or ref write.
Freeze/control capture is an action for this separately approved phase only.

The baseline selected metadata array is:

    ["ls-tree","-r","-z","--full-tree",BASE,"--",...NAMES]

Refuse aliases, unsupported modes, omitted selected baseline paths, stale
sources/controls, an existing index or nonzero/unknown native results.
Seal the whole successful capture package. Stop for independent root reception.

### 2. Stage — isolated index and selected objects only

Root grant binds the accepted capture manifest digest and exactly the same
plan/source/run. Recheck base/remote/protected roles and complete frozen inputs.
Require the isolated index still absent. Allowed mutation arrays:

    ["read-tree",BASE]
    ["hash-object","-w","--no-filters","--stdin-paths"]
    ["update-index","-z","--index-info"]
    ["write-tree"]

read-tree sees only the new isolated index. hash-object stdin is the exact
ordered, Git-quoted absolute frozen paths of changed approved files; returned
OIDs must equal independently calculated frozen blob OIDs. update-index stdin
is the exact NUL-terminated mode/SP/OID/TAB/path record for each changed path.
No -A, rm, checkout, clean, default-index staging or whole-worktree operation.

Before success, independently compare all selected tree/index rows and actual
selected blob type/OID/byte lengths, and inspect the **whole** unfiltered diff:

    ["ls-tree","-r","-z","--full-tree",TREE,"--",...NAMES]
    ["ls-files","--stage","-z","--",...NAMES]
    ["diff-tree","--no-commit-id","--raw","-r","-z","--no-renames",BASE_TREE,TREE]
    ["cat-file","--batch-check"]

The last command receives only deduplicated selected OIDs on stdin, not a
whole-baseline object stream. Exact core expectation is8,178 changed paths:
8,176 A and2 M. There may be no deletion, rename, unmerged entry, nonselected
change or filtered content. Native LF/TAB/NUL bytes—not literal backslashes—
must be independently checked. No commit/ref operation occurs. Seal and stop.

### 3. Commit — one ordinary unreferenced commit object

Root grant binds the accepted stage seal. Recheck unchanged frozen payload,
actual TREE, complete raw diff, base/remote and protected roles. The sole
allowed commit mutation is:

    ["commit-tree",TREE,"-p",BASE]

Use the existing command-local identity and a reviewed narrow commit message
accurately saying P211 complete,43 closed attempts, two retained/one complete/
three open seats, exact excluded P212 boundary and HOLD_EXTERNAL. Do not claim
five-paper completion, current P212 manuscript completion or public release.
Verify actual parent, tree and identity using:

    ["rev-list","--parents","-n","1",COMMIT]
    ["rev-parse",COMMIT+"^{tree}"]
    ["show","-s","--format=%an%x00%ae%x00%cn%x00%ce",COMMIT]
    ["cat-file","-p",COMMIT]

Only the small commit record is read; hash it independently. Require one
parent=BASE, exact TREE, no signed/configured extra behavior, and bare main
still BASE. No reference moves. Seal and stop for independent root reception.

### 4. Push — normal private push, then compare-and-swap

Root grant binds the successful commit seal. Recheck the complete prior seal
chain, actual commit/tree/diff, current protected roles/frozen data and fresh
explicit-URL remote=BASE. Only then:

    ["push","--porcelain",
     "git@github.com:maris205/hilbert-polya-structure.git",COMMIT+":refs/heads/main"]
    ["ls-remote","--exit-code",
     "git@github.com:maris205/hilbert-polya-structure.git","refs/heads/main"]
    ["update-ref","refs/heads/main",COMMIT,BASE]

Require actual remote=COMMIT before the CAS. Never force or force-with-lease.
Then separately confirm local main, tree, sole parent, mirror HEAD/clean state,
protected keys and actual remote again. No current-state success is inferred
from a push wrapper alone. If the remote moved but a later check/CAS fails,
preserve that partial external state and report it precisely; no rollback,
retry, merge or alternate-baseline invention. Postpush root reception and a
later additive synchronization receipt are separate from the selected commit.

This plan makes the four gates actionable but does not authorize or execute
any one of them. Every actual future source, plan, binding and phase seal must
be received before the next step.

