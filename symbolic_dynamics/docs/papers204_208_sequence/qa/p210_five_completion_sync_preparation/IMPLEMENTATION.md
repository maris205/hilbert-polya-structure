# Single-script implementation — source-only, actual final binding pending

This adds only `sync_five.py` and this implementation note to the already
root-read two-file plan. README.md and SCOPE.json retain their exact original
bytes and historical planning status. The implementation is not executed and
the preparation has no final execution seal yet.

The only intentionally unfinished source dependency is
`completion_binding()`. Before final execution root must bind that small
function to the genuine exact-five root native launch/completion, accepted
result, refreshed batch/root controls and explicitly complete final packages
with their actual schemas and literal pins. It must not turn a caller boolean
or a proposed status into success. In this draft it fails before any output
creation or Git command. No current moving final roots/pins are captured.

## Implemented behavior

`capture` records the actual accepted baseline's entire tree, inventories all
nine explicit live roots excluding the full old 306-file package, and computes
each selected path's SHA256, length, Git blob identity and executable mode.
The complete inventory is immediately repeated. Missing previously tracked
scoped paths are an error, not a deletion. Changed/new paths larger than
100,000,000 bytes fail before any object/index write. Explicit final package
manifests and actual completion/control dependencies must still match.

`stage` uses a fresh task-specific index under the outside-workspace run
directory, initialized from accepted HEAD. Only captured changed paths are sent
to `hash-object -w --no-filters --stdin-paths`; their returned OIDs must match
the previously computed identities. The whole live inventory is checked again
before index updates. Existing unchanged blobs are reused without object-body
capture. NUL-framed explicit index entries, the entire resulting tree and the
entire temporary index must equal baseline plus exactly captured changes;
unrelated paths remain unchanged and no path is deleted. All selected object
types/OIDs/lengths are verified with complete small batch-check output.

`commit` creates and verifies a single-parent commit object for that exact
tree, without advancing local main. The previously documented command-local
identity is reused; no config file is written. Root should retain the existing
identity provenance if changing that identity is ever requested.

`push` first rechecks the frozen scope, committed tree/parent, accepted local
main and actual remote main at 36e7b365. It performs a normal non-force push of
the exact commit to main, observes the real resulting remote ref, and only then
uses a compare-and-swap local-main update from the accepted base. A subsequent
remote/tree check follows. Any failure preserves actual command evidence and
side effects; there is no automatic retry, rollback, deletion or force.

Every Git invocation uses the accepted bare repository and the required
per-command config include/core.bare/fsmonitor/gc flags. Additional
command-local options disable sparse/split indexes, hooks and signing for this
explicit isolated plumbing workflow and carry the existing documented identity.
No Git command uses the original mirror's worktree/index. The old mirror's
config/index/HEAD/refs and the bare configuration/default index are separately
checked unchanged. Bare worktree status is N/A.

The recorder retains exact argv, cwd, sanitized environment, full stdin,
independent full stdout/stderr, original wait result and separate cleanup
outcome for each command. Each command has a new owned process group and
bounded wait/cleanup; unsettled streams are not hashed and no success phase
seal is created after a failure. Original native tool completion of the Python
executor is still root's separate responsibility, not invented by the script.

## Changed-dependency guard and execution order

Every phase revalidates the exact completed-gate/control binding, the original
approved plan/preparation/source, the entire captured selected
pathname/mode/SHA256/length/Git-OID map, and all explicit complete-package
membership. Any change after capture stops the workflow. Previous phase
packages are checked through an exact root-supplied seal and recursive
predecessor-seal chain. The independent index never replaces the bare default
index. Destination/evidence free space is checked against twice the changed
unique-object bytes plus a 1 GiB metadata/pack reserve.

All run artifacts go under a fresh explicit directory of the form
`/root/symbolic-dynamics-private-sync-final-five-N`. Root's separate actual
tool launch/completion records must go outside both the nine captured roots
and already sealed phase subdirectories—for example `RUN/root_native/`.
Adding a root receipt to batch QA between capture and push correctly trips the
source-membership guard; do not weaken the guard to accommodate it.

After actual final binding, complete source reading and sealing, root invokes
the phases explicitly as Python 3.10 -I -S -B with the actual preparation seal.
Later phases additionally take the actual immediately preceding phase seal.
No invocation command containing fabricated seal values is provided here.
A successful push's later QA receipt/state update remains outside its own
reported commit and must say so.

Current checks are AST/data-only. No launcher, executor, gate or Git command
has been executed for this implementation. No worktree/paper/host-map copy,
fetch, stage, object/ref/config write, commit or push has occurred.
OWNER_AMBER / HOLD_EXTERNAL remains.
