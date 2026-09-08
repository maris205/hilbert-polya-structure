# P210 checkpoint stage revision 01 — preparation only

2026-09-07 UTC. **STATIC_PREPARATION_PASS / CONTINUATION_NOT_EXECUTED**.
This preparer only performed read-only diagnosis and wrote this new directory.
No Git mutation, process signal, lock move, stage, commit, fetch, push,
scientific run or manuscript review was executed by this preparer.

The project workflow required preserving the failed attempt, checking the
changed execution dependency and using a separate disclosed revision. The
original preparation and all four original phase directories remain intact.

## Actual failure and complete read-only diagnosis

Root actually completed preflight (12 native commands), clone (19) and exact
copy (10). Original stage then stopped at command 007, ordinary `git add`,
after the recorder's 60-second timeout. That command had 2,138 explicit
nonignored inputs. The 180-file exact ignored add, staged-tree audit, blob
stream checks, commit and push had not started.

The [full original/failure inspection](inspection_01/RESULT.actual.json)
checked all **48 original native records**, original raw streams and input
membership; all 103 original preparation payloads plus its seal; and **266
original input pins**, rechecked after the diagnostic. `TIMEOUT` is the
original recorder's classification, not a captured integer Git exit code.
The failed stdout and stderr are genuinely empty. The original source uses
`subprocess.run` without a new process session and does not record a
process-group settlement; no historical group cleanup is inferred from it.

The 60-second parent deadline cut off unfinished Git object work. No
conversion diagnostic or failed content check was reported. Large temporary
object files are consistent with bulk check-in still underway, but CPU/I/O
profiling was not performed and a specific performance bottleneck is not
claimed as proven.

Eleven fresh read-only Git commands and complete source/overlay hashing found:

- **69,832 index entries**, exactly equal to the full baseline: zero staged
  changes, zero unrelated changes and zero unmerged entries. An unchanged
  index does not mean the failed add made no object-store writes.
- All **2,318 source and overlay files**, each side totaling
  **1,410,484,831 bytes**, still match the original approved hashes.
- Original mirror HEAD, tracking ref, config, full status and refs remain
  unchanged at `a380d24718fec4ef27365f44e96fb7ffa2b0fd10`.
- The index remains 11,362,580 bytes, SHA256
  `ac873c02fd9d7035de07e58b69edb09d01dd222bfdfe61aa669c856f9a80f7e2`.
- Two before/after scoped process snapshots found no matching live Git/SSH/
  pack processes. Additional all-process exact-FD scans found no holder of
  the failed lock or either temporary object file. No environment values
  or unrelated command arguments were recorded.

The exact [failed residues](FAILED_RESIDUE_PINS.actual.json) were measured
read-only and remain evidence, not cleanup targets:

| Residue under the overlay mirror | Bytes | Required disposition |
| --- | ---: | --- |
| `.git/index.lock` | 0 | Exact root-owned recoverable preservation, described below |
| `.git/objects/pack/tmp_pack_58p3V5` | 566,679,063 | Keep at its original path and hash |
| `.git/objects/96/tmp_obj_f76Bfi` | 446,464 | Keep at its original path and hash |

`git count-objects -v` reported 878 loose objects and those two garbage files;
the complete native stdout and warnings remain. Neither object residue is
deleted, moved, normalized or silently excluded from preservation checks.

## Separate actual root lock preservation

After these read-only diagnostics, root independently rechecked two fresh
all-process ownership/FD inventories and the exact stable lock key, then
actually ran `mv --no-clobber --` on only that lock. The live lock is now
absent; the zero bytes, inode 8613190901, device 99, mode 33188 and original
mtime 1788791779973320571 survive at:

`/root/symbolic-dynamics-private-sync-evidence-20260907/stage_revision_01_lock_preservation/index.lock.failed-stage-01`

The actual root receipt is
`/root/symbolic-dynamics-private-sync-evidence-20260907/stage_revision_01_lock_preservation/ROOT_PRESERVATION.actual.json`,
SHA256 `208b59678887f7741403dc3110d0585f10b730ceca94788203d3bc92403fa00e`.
This was a **root action**, not delegated execution by this preparer. The
full root source was read; its actual native exit 0, empty streams, exact
no-clobber argv and seven preservation input pins were checked separately.
Both object residues remain at their original paths. No bytes were deleted.

The proposed continuation contains no lock move/remove operation. It requires
that exact existing root receipt, preserved lock identity and absent live
lock, and refuses any newly observed overlay Git writer. The original stale
lock's old path is not falsely rehashed as though the root move never occurred.

## Exact amended source and scope

Root review entry points:

- [410-line continuation](execute.py), SHA256
  `497db8a936d1080523f9407799d3f9e094275ec18557c30f4307cf4c0babc1f8`.
- [175-line process support](process_support.py), SHA256
  `8ce99e3b7684123c5a04d99d8fa5cee98bd4e8e8b9bca7f7a4dd5dc93b5dde7c`.
- [Complete 360-line original-source delta](validation_01/SOURCE_DELTA.diff)
  and its actual native diff record (exit 1 means different source).
- [Final static and current-input validation](validation_01/RESULT.actual.json).

The prior executor remains at SHA256
`8d42285eeebcfc23c145da9b0bf6bb8b82b2db1f04533f5d73c145665f4cdcba`.
The scope is exactly the original
`bf8e4f358cb175374eec840d02894beecbeda722e6b9e559dc75ee899d49eb0e`:
2,318 paths, 2,314 additions, four modifications, no deletions. No A/reuse
work or new controls are added. P210 paper 987 and the four pinned live
controls must remain unchanged throughout the continuation. The existing
source control snapshots remain physical inputs; nothing is recopied.

Only CLI phases `stage`, `commit`, `push` exist. Their new, single-use output
directories are respectively `stage_revision_01`, `commit_revision_01` and
`push_revision_01` under the existing overlay evidence root. Stage consumes
the actual old `copy/RESULT.actual.json`; later phases consume only the new
successful predecessor. The original `stage/` failure is never overwritten,
renamed or converted into PASS. No clone, read-tree, skip-flag reset, broad
copy, repack, garbage collection, cleanup, deletion or force-push is present.

Before stage, the current staged diff must be an exact subset of intended
path/change/blob/mode keys, with no unrelated or unmerged entry. The actual
current subset is empty. The original ordinary and 180-path force-add lists
are unchanged, and the complete final staged path map is still required.

The native command bound is now **300 seconds**. Each command starts a new
session/process group owned by its launcher. At most 30-second heartbeat
messages let root keep giving updates while the outer execution session is
yielded; root should start with a short tool yield and poll at intervals no
longer than 30 seconds, rather than blocking a tool call for 300 seconds.

On timeout/interruption, signals are restricted to that newly created
PGID/session, never a discovered historical or unrelated process. The code
waits boundedly, escalates only within the owned group if needed, and refuses
to finalize stdout/stderr hashes while any live group member remains. A
successful parent that requires descendant termination is not accepted as
ordinary success. Zombie identities may be recorded; zombies cannot retain
open writing descriptors. If settlement cannot be established, raw files
remain explicitly unfinished instead of receiving final-output hashes.

The exact `cat-file` verifier now uses bounded nonblocking reads with the
same new-session/group settlement rule. It still checks all 2,318 path keys
through **1,096 unique objects / 658,584,369 bytes per audit**, retains two
complete lossless gzip native streams on overlay (stage and committed tree),
and independently rechecks decompressed raw stream identities. No check is
replaced with a summary or a representative-object sample. The source/
manifests, complete tree coverage, ordinary single-parent commit, actual
remote verification, tracking fetch, 0/0 and clean sparse status requirements
remain unchanged. Original mirror config/refs and all failed original bytes
are rechecked before and after each successful continuation phase.

Final observed overlay free space is **17,548,324,864 bytes**. The continuation
reserves **3,049,494,931 additional free bytes** for remaining objects, both
bounded captures, packing/index/log overhead and headroom. Already copied
worktree bytes and preserved failed temporary objects are already charged
against the observed free space. No deletion is proposed to obtain capacity.

## Required root approval, not supplied here

The revised approval status must be
`ROOT_APPROVED_P210_STAGE_REVISION_01_CONTINUATION`. It must retain the exact
overlay mirror/evidence paths, unchanged scope pin, all 180 ignored paths
and the existing three permissions for read-only alternates, read-only
original-config include and two bounded lossless blob captures. New fields:

| Field | Exact required value |
| --- | --- |
| `executor_sha256` | `497db8a936d1080523f9407799d3f9e094275ec18557c30f4307cf4c0babc1f8` |
| `process_support_sha256` | `8ce99e3b7684123c5a04d99d8fa5cee98bd4e8e8b9bca7f7a4dd5dc93b5dde7c` |
| `prior_executor_sha256` | `8d42285eeebcfc23c145da9b0bf6bb8b82b2db1f04533f5d73c145665f4cdcba` |
| `inspection_sha256` | `ed6e9175e3ce3ba92831ae5d622e71fb2e4eceb0f415ec7b983119a60c854176` |
| `residue_pins_sha256` | `d0e499698e4c3902bb36929ee4f193854f3c76e0c55910082e4ea0c72ee364f6` |
| `approved_phases` | `["stage", "commit", "push"]` |
| `allow_owned_new_session_timeout_settlement` | `true` |
| `lock_preservation_receipt` | Exact actual root receipt path above |
| `lock_preservation_receipt_sha256` | `208b59678887f7741403dc3110d0585f10b730ceca94788203d3bc92403fa00e` |

Root must actually read the complete revised sources/diff and issue the
approval separately. This preparation creates neither approval nor phase
output. Static AST/compile/contract checks do not constitute a runtime test
of the new process guard or a successful Git continuation. No new commit or
remote advancement is asserted. All research remains `HOLD_EXTERNAL`.

## Preparation closure

Final validation rechecked 266 original failure/preparation pins, all seven
root preservation pins, both failed object residues, the unchanged baseline
index and all 2,318 source/overlay hashes. New execution directories were
still absent. All five sources were parsed/compiled; the continuation and
process support were not imported or run by validation. Diagnostic helpers
were used only for their read-only current-state functions.

The final `SHA256SUMS` is a complete nonself seal of this preparation only.
Its identity is reported after creation, outside itself. It does not seal
future continuation outputs or silently add this package to the old scope.
