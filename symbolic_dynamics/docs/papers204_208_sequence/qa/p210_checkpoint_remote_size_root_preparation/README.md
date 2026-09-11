# P210 captured-source / bare-checkpoint receiver

This is preparation for one root-only read-only final reception, not an
executed receiver or a checkpoint PASS. The earlier unsealed receiver draft
is preserved unused. No Git write, scientific replay, manuscript review,
source copy, deletion, external upload or new bulk object capture occurs in
this preparation. `HOLD_EXTERNAL` remains unchanged.

The project workflow requires independent artifact reception after actual
execution, with failures preserved and source roles stated exactly. The
[single 421-line receiver](receive.py) implements its own manifest, native
record, tree/path and complete object-stream parsing. Its only reused helper
is the accepted, SHA-pinned 175-line process recorder for bounded new
read-only Git commands, not any executor's artifact-verification logic.

## Scope and three distinct repository roles

| Repository | Required role |
| --- | --- |
| `/root/autodl-tmp/hilbert-polya-structure` | Original mirror remains unchanged at `a380d247…` |
| `/root/symbolic-dynamics-private-sync-20260907` | Immutable captured old source and rejected commit `1f028072…`, tree `a26e19ee…`; all 2,318 original selected files stay physical |
| `/root/symbolic-dynamics-private-sync-accepted-20260907.git` | New small bare repository; accepted new commit must have sole parent `a380d247…`, never the rejected commit |

The moving live workspace's manuscript/control files are not read as old
checkpoint inputs. The four captured old controls and their physical
copy-phase snapshots are checked at their exact old keys. Current live
P210 Round1, review work and central-index updates are outside this captured
checkpoint. The receiver reads local preparation/receipt metadata separately;
that is not a claim of frozen live scientific inputs.

Exactly 306 files (305 payloads plus seal) in the prior P209 execution
package, totaling 1,169,593,078 bytes, remain locally preserved but are
excluded from the new remote tree. The exact exclusion disclosure is an
additional selected blob. The new tree has 2,013 selected changes: 2,009
additions, four modifications, no deletion. There are 24 retained complete
package manifests / 1,924 rows. All 25 original captured manifests / 2,229
rows are still received locally, including the omitted package. Historical
links into omitted execution evidence are not silently rewritten; this is
not a claim that those excluded bytes were pushed remotely.

## Actual checks on root execution

The receiver binds all four sealed preparations, all original/revised
execution files, exact contemporaneous root receipts, both new bare phases
and relevant small bare control files. The 266 original failure pins, 118
identity-revision pins and 624 corrective-preservation pins are rechecked.
The original timeout remains `TIMEOUT`, the identity failure remains native
128, and the actual GH001 push failure remains native 1. Raw streams and
recorded settlement fields are verified without inventing a historical
process-group record for the original timeout. The exact recovered lock and
both failed temporary objects retain their full file keys and locations.

Both original complete native gzip captures are actually read and compared
byte-for-byte. If compressed bytes are identical, one full independent
decompression is performed and the second's equality basis is explicitly
labelled. Otherwise both are independently decompressed. Every one of the
1,096 old unique objects / 658,584,369 payload bytes is checked for exact
header/frame, SHA256, Git blob SHA1, size, delimiter and EOF. The new bare
tree's retained old object keys must occur in that verified capture; the
single new disclosure body is separately read from Git and compared with
its exact source bytes. No new large object-body stream is generated.

Fresh read-only Git queries verify the new bare repository identity, actual
HEAD, sole parent, complete tree and changed-path maps, exact current index,
no unmerged entries, all 964 new selected object headers / 69,914,981 bytes,
new disclosure body, actual author/committer identity, current remote main,
tracking main and 0/0. The largest selected blob remains 6,471,668 bytes.
The new bare worktree/status is explicitly **N/A**; no `git status` is run
there or misreported as clean. Original-mirror and immutable-capsule status,
refs, config and index checks retain their distinct non-bare roles.

Captured selected files and all input pins are rechecked at the end. The
output is exclusively
`/root/symbolic-dynamics-private-sync-evidence-20260907/remote_size_revision_01/root_receiver_01`.
It contains only small native-query streams, reception metadata and a
complete nonself seal. On failure, a new immutable failure file is retained;
there is no automatic retry or cleanup. Native commands have a 45-second
bound and at-most-30-second heartbeats with owned-group settlement.

## Finalization and handoff

The [95-line metadata finalizer](finalize_inputs.py) runs only after root
reports the actual new bare push PASS. It fixes the actual new commit/tree,
native phase counts, complete physical input membership, exact current root
checkpoint receipts and source hashes in `INPUT_BINDING.json` and
`INPUT_PINS.json`. Future receiver output and future root receipts are not
absorbed into those inputs. The resulting `FINALIZATION.actual.json` is a
preparation result, not an executed receiver. The finalizer only hashes and
parses/compiles source, checks the complete native-operation allowlist and
rejects bare worktree-status calls; it performs no Git query or receiver
import/execution.

Root has now actually reported successful new bare build (35 native
commands) and push (26), with commit
`36e7b365b35f454d6fa94d6674746eafde314872`, tree
`57efe318eda9575fa785463358cacf9efc2dd3cd`, sole parent `a380d247…`, actual
remote confirmation and 0/0. Final preparation binds those existing results;
it does not substitute for the pending independent receiver execution.

Root must read the complete final sources and verify the separately reported
complete nonself preparation seal. Then, from the workspace root, root may
run the receiver using the sanitized system-Python launcher and the actual
verified seal:

```
env -i PATH=/usr/bin:/bin LANG=C LC_ALL=C PYTHONDONTWRITEBYTECODE=1 \
  /usr/bin/python3 -B docs/papers204_208_sequence/qa/p210_checkpoint_remote_size_root_preparation/receive.py \
  --seal-sha256 ROOT_VERIFIED_FINAL_SEAL
```

The placeholder is not an approval or valid seal. Use a short outer tool
yield and poll at intervals no longer than 30 seconds while giving concise
updates. Only the actual receiver `RESULT.actual.json` can establish the
final reception PASS. Preparation alone never implies successful remote
synchronization, acceptance of current live work, or five-paper completion.
