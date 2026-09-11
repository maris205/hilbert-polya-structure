# Final five-paper private synchronization — bounded scope plan only

Status: PLAN_ONLY / NOT_FROZEN / NOT_EXECUTED. Prepared while root's actual
P210 OUT02 build is running. This document does not assert a successful build,
a page view, P210 acceptance, exact-five acceptance or any new synchronization.

The research workflow requires root to finish the actual terminal obligations,
preserve the previous controls, update the batch index and then the recovery
index before freezing a final synchronization selection. This plan writes only
README.md and SCOPE.json. It does not capture/hash moving terminal files, copy
paper or host-map payloads, execute Git writes, or create another audit layer.

## Repository roles and configuration

Use the already accepted bare destination
`/root/symbolic-dynamics-private-sync-accepted-20260907.git`, previously
observed at commit `36e7b365b35f454d6fa94d6674746eafde314872`, tree
`57efe318eda9575fa785463358cacf9efc2dd3cd`. These are observations to revalidate,
not a guarantee of the remote ref at future execution. Bare worktree status is
N/A; check its actual tree/index/ref roles instead of calling it clean.

The original mirror `/root/autodl-tmp/hilbert-polya-structure` stays at its
separately observed `a380d24718fec4ef27365f44e96fb7ffa2b0fd10` role. Its stale
or dirty worktree/index must not supply a final staging baseline. Do not clean,
reset, copy over or otherwise mutate it. The rejected `1f028072…` capture is
historical Round0 evidence, not today's final source.

The accepted bare repository has no own origin configuration. The actual
[preliminary role record](../P210_FINAL_SYNC_PRELIMINARY_ROLE_READ.actual.json)
preserves the first missing-include failure and corrected actual remote query:
session 32791 → 5bc57f / exit 0, remote main then equal to 36e7b365. Each future
Git command in this destination must retain the documented per-command prefix:

```text
git -C /root/symbolic-dynamics-private-sync-accepted-20260907.git
  -c include.path=/root/autodl-tmp/hilbert-polya-structure/.git/config
  -c core.bare=true -c core.fsmonitor=false -c gc.auto=0
```

This is a command-layout illustration, not an executed shell script. No config
write, credential copy, fetch, stage, commit or push occurs in this task.

## Candidate scope and exact mapping

All following mappings are identity mappings at the repository root; do not
add the older historical `symbolic_dynamics/` prefix.

| Workspace-relative root = Git-relative root | Role |
|---|---|
| SYMBOLIC_DYNAMICS_STATE.md | Final root recovery index |
| docs/papers204_208_sequence | Complete batch records, subject to the explicit exclusion below |
| papers/205-conflict-triggered-cyclic-increments | Retained P205 |
| papers/207-upper-neighbor-rank-dynamics | Retained P207 |
| papers/208-original-snapshot-triangulation-sweeps | Retained P208 |
| papers/209-ordered-fibre-threading | Retained P209 |
| papers/210-weakly-increasing-run-aggregation | Retained P210; final artifacts still require closure |
| papers/204-previous-smaller-distance-feedback | Preserve manuscript-A rejection |
| papers/206-ternary-cyclic-record-feedback | Preserve manuscript-A rejection |

These are selection boundaries, not a blind recursive-add instruction.
Within them, select complete current packages: manuscript/scientific inputs,
canonical outputs, accepted reviews and deltas, physical frozen rounds,
prepared/failed/accepted QA, root native records, historical control snapshots,
scouting and rejection evidence, terminal artifacts and the eventual actual
five-paper gate. Preserve each selected nonself manifest and every referent;
do not select passing reports while dropping their failures or ignored data.
Reuse unchanged verified baseline objects and preserve unrelated tree entries.
There is no authorized implicit deletion.

The exact final producer paths, package count and path/SHA/byte/mode/OID list
cannot be frozen until root has received actual completed terminal/five-gate
outputs and refreshed controls. SCOPE.json specifies this future selection
algorithm; it deliberately contains no fabricated final pin map.

Links to out-of-workspace checkpoint evidence or runtime host files do not
automatically authorize bringing those filesystem trees into Git. Keep their
local archival limitation explicit. Any additional bounded evidence mapping
must be named by root; do not pretend it is included by these nine roots.

## Entire old oversized package remains local-only

Exclude the complete directory
`docs/papers204_208_sequence/qa/p209_completion_private_checkpoint`,
including its manifest and small files: 306 files / 1,169,593,078 bytes in the
earlier census, zero paths in accepted HEAD. Its two gzip streams are each
567,977,587 bytes and caused the actual earlier GH001 rejection. The exact
306-path historical disclosure is
[already preserved](../p210_checkpoint_remote_size_revision_01/P210_REMOTE_SIZE_CHECKPOINT_SCOPE.json).
Do not silently reintroduce it through the broad batch root or upload a partial
package. All local original bytes, failed Git records and rejected commit remain.

Use a conservative 100,000,000-byte new-object blocking threshold in the future
preflight; this is a planning guard, not a claim about current hosting policy.
If another selected object crosses it, stop before staging/push and disclose
its exact role/size. No deletion, clipping, splitting, LFS/new service,
force-push or history rewrite is part of this plan.

## Capacity and bounded future execution

The earlier read-only metadata census (actual native 90ba43 / exit 0) observed
2,950 pathnames absent from HEAD, totaling 432,487,455 apparent bytes. This is
not a content diff and is already temporally behind terminal execution. It
observed 577,437,696 free workspace bytes versus 15,722,483,712 under /root;
neither is a present capacity guarantee. The largest nonexcluded file was
47,524,589 bytes and was already in HEAD. SCOPE.json retains the small original
root/count/size observations and exact two historical read-only Git commands.
No new Git query or live-output scan was run for this plan.

After closure, prefer verified baseline blob reuse and a fresh task-specific
temporary index, importing only explicitly frozen new/changed files. Do not
copy the multi-GB batch/paper tree onto the nearly full workspace mount, use
the original mirror's index, duplicate large host maps, or log another complete
multi-GB cat-file object-body stream. Verify selected object bytes and manifest
closure with bounded streaming/per-object checks and retain genuine small
native command/exit/evidence records.

Root must first: receive P210 build/outer closure; actually view all six final
pages; close artifact/lifecycle reception; receive the exact-five gate for
P205/P207/P208/P209/P210; preserve and refresh controls; settle/freeze all
selected outputs; then recheck capacity, sizes, scope, refs and real remote.
Only afterward does root or its newly bounded executor implement staging,
commit and normal push. Remote advancement requires overlap inspection and a
normal resolution, never force. A receipt is written only after the real ref
exists and cannot claim to be inside its own reported commit.

Preparation-only scope remains OWNER_AMBER / HOLD_EXTERNAL.
