# P210 remote-size correction — preparation only

**READ_ONLY_PREFLIGHT_PASS / CONTINUATION_NOT_EXECUTED**.
Root's first replacement commit `1f028072dc408a7d4404a7276f22f8666ba81801`
was locally valid, but GitHub actually rejected its push. Native command 010
returned **1 after 196.9 seconds**, without timeout, signals or remaining
process-group members. The remote reported GH001 for a 541.67 MB raw gzip
inside the prior P209 execution package. All failed phase files remain exact.

The project workflow requires separate failure-preserving correction. Root
therefore authorized omitting the **entire** prior execution package from
this new checkpoint only; not deleting it, rewriting the rejected commit,
installing LFS, splitting its raw data or using a new service. The earlier
unsealed `p210_checkpoint_root_preparation` draft remains unused and
superseded; it was never accepted, finalized or executed.

## Exact new scope and captured-source role

The [11-command read-only preflight](inspection_01/RESULT.actual.json)
actually confirmed remote main is still
`a380d24718fec4ef27365f44e96fb7ffa2b0fd10`, inspected all 1,096 actual native
object headers, and hashed all 2,318 captured selected files. Both oversized
original selected paths are inside the excluded package. Every retained
selected blob is smaller than the conservative 100,000,000-byte threshold;
the largest is only **6,471,668 bytes**. Baseline objects are already remote;
the rejected commit will not be an ancestor of the new commit.

| Scope component | Exact value |
| --- | --- |
| Excluded package | `docs/papers204_208_sequence/qa/p209_completion_private_checkpoint` |
| Excluded paths | 306 = 305 payloads + its seal |
| Excluded total bytes | 1,169,593,078 |
| Retained prior paths | 2,012 |
| Added disclosure | `docs/papers204_208_sequence/qa/P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json` |
| New selected paths | 2,013 = 2,009 additions + four modifications |
| Remaining complete package manifests | 24, retaining all other original package membership |

The [disclosure](P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json) includes every exact
excluded path, byte/hash/mode/OID key and reason. Historical references into
that package remain unchanged and locally resolvable; this scoped private
backup is explicitly not a complete remote archive of the omitted execution
bytes. All manuscripts, science, frozen packages and other selected runtime
receipts remain in the approved captured scope. No scientific claim changes.

The authoritative source is now the **immutable first overlay**
`/root/symbolic-dynamics-private-sync-20260907` at rejected HEAD `1f028072…`
and tree `a26e19ee04c7a25fd0b0d00c67df784206baba4c`. Its old four control
versions and old P210 package are physical. The original copy-phase control
snapshots also remain physical inputs. The live workspace may now advance;
this continuation never reads its moving manuscript or control files as
though they were the captured old scope. Source/executor metadata in this
new preparation is separate from those captured scientific inputs.

## Minimal root-only execution

Read the complete [231-line executor](execute.py), SHA256
`6607f1adb9b0013e8c52dcf8460088ec0f7751a08847630e3650b6d795a5b70a`.
It uses only the accepted 175-line process recorder, SHA256
`8ce99e3b7684123c5a04d99d8fa5cee98bd4e8e8b9bca7f7a4dd5dc93b5dde7c`.
No existing executor is modified and no continuation is run by this preparer.

Only two CLI phases exist: `build` and `push`. Their new, exclusive evidence
directories are under
`/root/symbolic-dynamics-private-sync-evidence-20260907/remote_size_revision_01`.

`build` creates the new small bare repository
`/root/symbolic-dynamics-private-sync-accepted-20260907.git`. Read-only object
alternates point to the first overlay and original mirror object stores.
The new index starts at `a380d247…`, then receives only the exact approved
mode/OID/path keys. The one new disclosure blob is written and read back
byte-for-byte. Complete changed-path, selected-tree and actual object-header
checks precede `commit-tree`. The sole parent is **a380**, never the rejected
commit. Main advances normally from that base to the new commit.

`push` consumes only the actual successful build receipt. It rechecks the
tree and unchanged remote base, performs the normal explicit main push,
confirms the actual remote ref, fetches only main's tracking ref, and checks
0/0 and exact index/tree equivalence. No force flag is used. Bare worktree
and worktree status are explicitly **N/A**, not claimed clean or waived as
though there were a checked-out worktree. Tree/index/ref checks remain exact.

Before and after each phase, all **624 historical input pins**, all first
overlay selected files and materialized membership, HEAD/tracking/config/
refs/index, all three failed residue keys and original-mirror bindings are
rechecked. No mutation targets the first overlay or original mirror. There
is no checkout, reset, broad copy, deletion, repack or cleanup. The two old
lossless full native object streams remain available for independent final
reception; no new bulk object-body capture is added.

Native bounds remain 300 seconds, with at-most-30-second heartbeats and
settlement restricted to each newly owned process group. Root should launch
with a short tool yield and poll at intervals no longer than 30 seconds.
Any failure is preserved without automatic retry or cleanup.

## Required separate root approval

| Approval field | Required exact value |
| --- | --- |
| `status` | `ROOT_APPROVED_P210_REMOTE_SIZE_REVISION_01` |
| `executor_sha256` | `6607f1adb9b0013e8c52dcf8460088ec0f7751a08847630e3650b6d795a5b70a` |
| `scope_sha256` | `32df0b5a0c20bba93034a3469ebd3689b5d932b247d6c064c6cbfb518d8a1b3d` |
| `preparation_seal_sha256` | Actual final nonself seal, reported separately after creation |
| `preserved_input_pins_sha256` | `96616b010d8d2d8dfe0b99b060e5c3e2c5e5c61676f7bffa770fb3831352da70` |
| `process_support_sha256` | `8ce99e3b7684123c5a04d99d8fa5cee98bd4e8e8b9bca7f7a4dd5dc93b5dde7c` |
| `new_bare` | `/root/symbolic-dynamics-private-sync-accepted-20260907.git` |
| `new_evidence` | `/root/symbolic-dynamics-private-sync-evidence-20260907/remote_size_revision_01` |
| `captured_source` | `/root/symbolic-dynamics-private-sync-20260907` |
| `rejected_commit_preserved` | `1f028072dc408a7d4404a7276f22f8666ba81801` |
| `approved_phases` | `["build", "push"]` |
| `allow_exact_bare_index_commit_tree_and_normal_ref_updates` | `true` |
| `allow_readonly_object_alternates_and_origin_config_include` | `true` |
| `commit_identity` | `{"user.name":"mariswang","user.email":"wangliang.f@gmail.com"}` |

The exact identity is reused command-locally from root's earlier actual
configured-key read, not written to any config. Root must read and approve
separately. The final seal covers this preparation only, excluding itself.
Static AST/contract checks and preserved-input hashing do not constitute a
runtime test, successful build/push or final receiver PASS. All remain
`HOLD_EXTERNAL`; this is a scoped backup, not five-paper completion.
