# P210 Round0 private checkpoint — preparation only

2026-09-07 UTC. **PREPARED_ONLY / ROOT_REVIEW_AND_EXPLICIT_EXECUTION_REQUIRED**.
No clone, materializing copy, staging, commit, fetch or push was executed by
this preparation. The source workspace and original mirror remain unchanged.
All writes are confined to this new preparation directory. No manuscript
review, scientific replay, build, page view or acceptance is claimed here.

The project symbolic-dynamics workflow determined the exact mirror mapping,
frozen scope, preserved failures and separate real-remote verification. Its
research phase gates were not changed or replaced by Git diagnostics.

## Exact proposed scope

The immutable [scope](preparation_01/SCOPE.json), SHA256
`bf8e4f358cb175374eec840d02894beecbeda722e6b9e559dc75ee899d49eb0e`,
selects **2,318 files: 2,314 additions and four modifications, zero deletions**.
They total **1,410,484,831 source payload bytes**. Source-relative and Git-root-
relative paths are identical for every selected file; the legacy
`symbolic_dynamics/` prefix is not introduced.

- [Compact exact target map](preparation_01/SELECTED_PATHS.tsv): change, byte
  length, SHA256, Git blob SHA1 and complete path for every selected file.
- [Executable target map](preparation_01/SELECTED_PATHS.json): additionally
  records old mode/object identity for each of the four modifications.
- [Complete expected Git blob map](preparation_01/EXPECTED_BLOBS.json): all
  2,318 selected keys, not just representative artifacts.

The selected packages contain **25 original named manifests / 2,229 payload
rows**, their 25 manifest files, and 64 exact extra records. Complete physical
nonself-manifest coverage and every source SHA256 passed; the final static
validator made a second full source-hash pass. The expected map contains
1,096 unique Git blob identities / 658,584,369 unique payload bytes.

| Included completed boundary | Exact role |
| --- | --- |
| P210 whole-paper 987-payload manifest, including physical Round0 493 and unchanged author evidence | Root-accepted Round0 only; no manuscript A acceptance |
| MNA root strict pair, source reading, original receiver, preparation and actual execution records | Already accepted admission evidence; original gate remains in a380d247 |
| Six P205/P207 fresh strict pairs and accepted four-build supplement | Includes both failed original receiver/diagnosis and the separate accepted revision |
| Prior a380d247 execution package and root reception | Actual historical execution evidence is not in its own named a380d247 commit; it is selected here for the next checkpoint |
| P210 admission/Round0 control snapshots and 64 exact top-level extras | Historical roles preserved; four currently stable live controls are byte-pinned |

The four modified paths are `SYMBOLIC_DYNAMICS_STATE.md`, the batch
`PIPELINE_STATE.md`, `FINAL_THEOREM_CONTRACTS.md` and `GIT_SYNC_RECEIPT.md`.
The executor first physically snapshots their exact approved source bytes
onto overlay, then copies from those snapshots. It aborts on any source
hash/mode drift before or after copying. A subsequent root A/delta/Round1
milestone requires an explicit new scope, not silent use of changing controls.

Excluded explicitly: all P210 A initial/strict/original/delta work; all
P208/P209 reuse preparation/execution/revision work; the unfinished five-paper
terminal preparation; any newly created directories; this preparation and
the executor's future output. The initial A now underway/completed elsewhere
does not expand this frozen Round0 scope. No A/Round1/B, fifth completion,
new scout or new batch is implied. `OWNER_AMBER / HOLD_EXTERNAL` remains.

Exactly **180 ignored TeX evidence files** occur in the selection. Their
complete explicit list is in SCOPE.json and the original native ignore
result. The proposed executor requires root approval of exactly that list
and uses force-add only for those files. It never force-adds a directory,
force-pushes, resets, removes, overwrites a prior worktree file or cleans up.

## Actual read-only Git and transport results

Original mirror: `/root/autodl-tmp/hilbert-polya-structure`.
Workspace: `/root/autodl-tmp/symbolic_dynamics` (not a Git repository).

The actual baseline HEAD and original `origin/main` are both
`a380d24718fec4ef27365f44e96fb7ffa2b0fd10`, tree
`9cedcdbde3ee647a1bc60b56afcfe7c63e05c466`. Full porcelain status is empty,
and divergence is 0/0. The final original-config SHA256 is
`4b442474607b266ca02a5d09925c4656075aa175019d27eb0b97912e78a0a5e5`.
No replace ref was found. These observations do not claim that the new
2,318 files are already in Git.

The first real remote query failed with an SSH `github.com:22` connection
timeout. The original [failed native command](diagnostics_01/command_010.actual.json),
full stdout/stderr and unchanged failed launcher source remain. The launcher
stopped on that native exit 128; it did not reach its later operations.
The separate [bounded normal SSH retry](preparation_01/command_009.actual.json)
succeeded and confirmed the exact baseline. A further
[strict-known-host SSH query](validation_01/command_005.actual.json) also
succeeded, again returning that exact ref. No port-443 alternative, global
SSH/Git change or weakened host verification was needed.

All native read-only Git commands have complete argv, raw stdout/stderr,
actual exits and explicit environment overrides in their respective
directories. Inherited environment values and credential values were not
enumerated. Remote commands name `origin`; no bare remote URL is displayed
in this handoff. The tool display of prepare.py's large JSON summary was
truncated; the full pre-existing SCOPE.json and native ignore file preserve
the complete data. That display is not used as evidence of a successful
sync or as the canonical target map.

No file named `GIT_SYNC_LOG` was found in either data root. The controlling
mapping is the actual `HISTORY_AND_CAVEATS.md` Git path table, the batch
`GIT_SYNC_RECEIPT.md` and the accepted a380d247 executor/receipt. A missing
filename was not replaced with an invented log.

## Storage and supplementary mirror decision

Both proposed destinations are absent, and their parent `/root` is verified
as overlay, a different device from the md0/XFS source and original mirror.

| Storage item | Actual/proposed bytes |
| --- | ---: |
| Initial free md0 space | 903,876,608 |
| Initial free overlay space | 19,589,816,320 |
| Original mirror `.git` apparent bytes | 860,052,675 |
| Prior a380 execution directory apparent bytes | 1,169,626,015 |
| Exact selected source payload | 1,410,484,831 |
| Conservative overlay reservation | 5,305,196,317 |

Proposed supplementary mirror:
`/root/symbolic-dynamics-private-sync-20260907`.
Proposed execution evidence:
`/root/symbolic-dynamics-private-sync-evidence-20260907`.

The executor proposes `clone --shared --no-checkout --origin source-mirror`
from the read-only original mirror, with an empty hook/template directory.
It then loads the baseline index without checking out historical files,
sets skip-worktree on all unselected baseline paths, and materializes only
the 2,318 explicit selected paths. This is a sparse worktree implemented
with explicit index flags, not a whole tracked-worktree duplicate.
The original mirror's files, index, refs and configuration are never changed.

The supplementary object database deliberately has the absolute read-only
alternate `/root/autodl-tmp/hilbert-polya-structure/.git/objects`. Its local
usability therefore depends on retaining that original object store.
No repack/dissociation, history movement, deletion, cleanup or symlink-based
relocation is proposed. After a successful normal push, the actual private
remote independently contains the reachable new commit and objects; do not
equate the local alternate dependency with remote backup completeness.

The private `origin` is read through an explicit **command-scoped, read-only
include** of the original mirror's `.git/config`. No secret-bearing remote
URL is manually copied or printed. Worktree location, nonbare mode, disabled
hooks, disabled fsmonitor/auto-GC, no signing and no automatic CRLF conversion
are explicitly overridden only for commands in the supplementary clone.
The original config is pinned and must remain unchanged. No global settings
are edited. The root approval must acknowledge this dependency explicitly.

No network clone is needed: the verified private remote and read-only local
source share the exact same baseline. If that baseline changes before
execution, the preflight stops; root must inspect overlap and prepare normal
integration separately. There is no automatic merge or force path.

## Proposed execution and verification gates

The [389-line executor](execute.py), SHA256
`8d42285eeebcfc23c145da9b0bf6bb8b82b2db1f04533f5d73c145665f4cdcba`,
is **not executed or runtime-tested**. Static syntax/contract validation is
not a claim that clone/stage/commit/push has succeeded. Root must read the
complete source and scope, decide whether this exact conservative milestone
is still wanted, and separately supply affirmative approval.

Phases are single-use and strictly ordered: `preflight`, `clone`, `copy`,
`stage`, `commit`, `push`. Each consumes the preceding successful phase
receipt and binds the same scope/executor hashes. A failure remains on disk
and stops further work; no phase is automatically retried or overwritten.

Root's approval JSON must use status
`ROOT_APPROVED_EXACT_P210_ROUND0_OVERLAY_CHECKPOINT` and contain:

- `scope_sha256` and `executor_sha256` equal to the exact pins above;
- `supplementary_clone` and `overlay_execution_evidence` equal to the two
  explicit overlay paths;
- `approved_phases` equal to the six ordered phase names above;
- `allow_exact_ignored_paths` equal to the full 180-path SCOPE.json list;
- `allow_original_mirror_alternates_readonly`,
  `allow_readonly_original_config_include` and
  `allow_two_unique_blob_lossless_gzip_captures`, all explicitly `true`.

No approval file is supplied by this preparer. A caller would pass its
root-authored absolute approval path to `execute.py <phase> --approval <path>`.
No phase should be called until the root has actually read and approved it.

Stage verification requires the exact A/M path map, no deletion or unrelated
change, complete named-package path/mode/object coverage, and full actual
Git blob byte length/SHA256/computed SHA1 checks. Each unique object is read
once per stage/commit audit; every path separately maps to its correct key.
The 658,584,369-byte unique payload stream is retained twice as complete
lossless gzip native output on overlay, with full native framing/digests and
a separate streaming decompression check. No multi-GB uncompressed archive
or whole-repository object stream is materialized. The 5.305 GB reservation
covers selected worktree bytes, new Git objects, both bounded compressed
streams, outgoing packing/headroom and small logs/index files. Actual free
space is checked again before cloning; gzip savings are not assumed.

The commit must be an ordinary one-parent child of a380d247 and have exactly
the inspected staged tree. Push is a normal explicit `origin` main refspec,
preceded by a fresh exact-baseline remote query. Actual post-push `ls-remote`,
new-clone tracking fetch, 0/0 and clean sparse status are required. The
original mirror intentionally stays at a380d247 and is checked unchanged
again; a later root handoff must document that split instead of falsely
calling the historical mirror current.

This preparation and future overlay execution receipts are not inside their
own proposed checkpoint. Root may archive this sealed preparation later only
through a separate exact noncircular amendment/next checkpoint. Root then
records the real resulting commit and new path/ref mappings, updates the
batch index followed by stream state, and retains `HOLD_EXTERNAL` throughout.

## Final preparation evidence

[Static validation and final current-state checks](validation_01/RESULT.actual.json)
passed: all 2,318 source hashes rechecked, four script sources parsed/compiled
without executing their phase code during validation, original mirror clean,
strict remote match, and both overlay targets still absent. `diagnose.py`,
`prepare.py` and `validate.py` were separately run for their read-only tasks;
the per-source syntax-only entries describe the validation step, not a denial
of those earlier diagnostic executions. `execute.py` was never run.

The final `SHA256SUMS` is a complete nonself preparation seal. The final seal
identity is reported after creation, outside itself. Root acceptance of this
preparation and any later actual synchronization remain separate obligations.
