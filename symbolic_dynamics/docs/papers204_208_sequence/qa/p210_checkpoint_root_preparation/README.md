# P210 private-checkpoint final receiver preparation

This package prepares one root-only read-only receiver. It creates no Git
commit, push, configuration change, stage, source copy, cleanup, mathematical
replay or manuscript review. `HOLD_EXTERNAL` remains in force.

The project workflow requires an independent artifact-level receiver and
preservation of original evidence. The [single receiver](receive.py) therefore
implements its own manifest, full native-stream, tree-path and Git-blob
parsers. It does not call any preparation/execution artifact verifier.
The only reused code is the already accepted, SHA-pinned 175-line process
recorder, used solely for new bounded read-only Git commands and their owned
process-group settlement.

## Fixed scope and preserved failures

The old approved scope is still SHA256
`bf8e4f358cb175374eec840d02894beecbeda722e6b9e559dc75ee899d49eb0e`:
2,318 selected paths, 2,314 additions, four modifications, no deletion;
25 complete manifests / 2,229 manifest rows. The four live control files,
their physical copy-phase snapshots, all source/overlay selected files and
the P210 package remain at the old checkpoint's exact hashes. Later A/reuse,
Round1, receiver output, synchronization receipt updates and new science are
not silently included in that commit.

All original preparation and both separately sealed revision preparations
are retained. The original native stage timeout is preserved as `TIMEOUT`,
not invented as an integer Git exit. Its missing historical process-group
settlement is not reconstructed. The later commit identity failure retains
actual native exit 128 and its recorded clean owned-group settlement.
All 266 original failure/preparation pins and 118 accepted-stage/identity
failure pins are rechecked. The exact recoverably preserved lock and both
failed temporary objects retain their bytes, location roles, inode/device,
mode and mtime. No deletion or lock move occurs in this receiver.

## Checks performed only when root actually executes

The receiver checks complete sealed preparation membership, every archived
phase file, all native command exit/status/raw-output hashes, all eight
phase command sequences and their approval/executor bindings. It also checks
preparation diagnostic native records, including the failed remote probe
and actual source-diff exit 1, without relabelling those failures as success.
The root lock-move command is received as a historical actual action; it is
never rerun.

Both retained native gzip captures are read in full and actually compared
byte-for-byte. If those **compressed bytes are identical**, the receiver
independently decompresses one complete capture and labels the second's
equality basis explicitly. If not identical, it independently decompresses
both. Each decoded object is checked for exact frame/header, payload size,
SHA256 and Git blob SHA1, final newline and EOF. All 1,096 unique objects /
658,584,369 payload bytes map to the complete 2,318-path staged/committed
trees. No representative sampling or new object-body capture occurs.

Fresh native read-only Git checks cover actual HEAD, single parent, tree,
both named full tree maps, complete changed-path map against the base,
current index equivalence, absence of unmerged paths, all 1,096 actual object
headers, actual commit author/committer identity, current remote ref,
tracking ref, 0/0 and clean overlay status. The original mirror must still
have unchanged config/refs/status at
`a380d24718fec4ef27365f44e96fb7ffa2b0fd10`. No fetch, commit, push, add,
write-tree, config write or Git cleanup is permitted by the receiver's native
command allowlist. Native queries have a 45-second bound and at-most-30-second
heartbeats. The total receiver is finite, with no retry or polling loop.

The source/overlay selected-file keys and all preserved inputs are rechecked
at the end. The new output is exclusively
`/root/symbolic-dynamics-private-sync-evidence-20260907/root_receiver_01`.
Only small native query streams, JSON reception results and a nonself output
seal are created. No raw multi-gigabyte stream is copied onto the source
filesystem. A failure receives a separate immutable failure file; the script
does not clean up or automatically retry.

## Finalization and root handoff

The [83-line metadata finalizer](finalize_inputs.py) is run only after root
reports actual successful `push_revision_02` completion. It creates fixed
`INPUT_PINS.json` and `INPUT_BINDING.json`, binding the actual commit/tree,
all preparation/phase physical membership, exact contemporaneous root
checkpoint receipts and the receiver source hash. Future root receipts and
receiver output are excluded, avoiding circular or self-including inputs.
It parses/compiles both sources, but does not import or run the receiver,
decompress objects, or issue any Git command. `FINALIZATION.actual.json`
describes preparation, never a completed reception.

Root must read the complete final source and verify the externally reported
complete nonself `SHA256SUMS` before invoking the receiver. Run from
`/root/autodl-tmp/symbolic_dynamics` under the same minimal environment:

```
env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C PYTHONDONTWRITEBYTECODE=1 \
  /usr/bin/python3 -B docs/papers204_208_sequence/qa/p210_checkpoint_root_preparation/receive.py \
  --seal-sha256 ROOT_VERIFIED_FINAL_SEAL
```

The literal placeholder is not an approval or an executable seal value.
Use a short outer tool yield, then poll at no more than 30-second intervals
while giving concise updates. The preparer does not perform that root
execution. Only the actual receiver's `RESULT.actual.json` may establish
the reception PASS; preparation alone cannot do so.
