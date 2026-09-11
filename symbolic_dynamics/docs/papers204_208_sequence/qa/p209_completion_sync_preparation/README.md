# Read-only P209-completion private-checkpoint plan

2026-09-07 UTC. This is a fixed exact-path planning snapshot, **not a copy,
stage, commit, push, merge, scientific check or admission**. Root owns every
subsequent Git/mirror/central action. `HOLD_EXTERNAL` remains unchanged.

## Result and evidence

[SCOPE.json](SCOPE.json), 874,363 bytes, SHA-256
`77c68f6061275210c12ecd66a029bae25af1e29449431e86ca71df5f24243b3b`,
freezes **1,473 selected paths**, each with exact workspace/mirror-relative
path, SHA-256, byte length, expected Git blob SHA-1, and observed baseline role.
There are **1,467 absent paths and six existing differences**, no ignored
selected paths and no planned deletion. No glob is a selection authority.

The complete verification scope is **19 exact named manifests / 12,474 payload
rows**, plus their 19 manifest files and **53 exact additional files**:
**12,546 expected Git blob keys**. Of these, 11,073 already match both HEAD and
mirror bytes. All 12,546 source paths and 11,079 existing mirror paths were
rehashed before/after; absent mirror targets stayed absent.

The first actual planner run passed **242,333 documentary predicates**.
[ATTEMPT_01.actual_tool_return.json](ATTEMPT_01.actual_tool_return.json)
preserves the native start/completion. [READONLY_GIT.actual.json](READONLY_GIT.actual.json)
preserves all nine actual read-only subprocess returns. The full NUL-separated
baseline tree output is [BASELINE_TREE.stdout.raw](BASELINE_TREE.stdout.raw),
1,538,919 bytes, SHA-256
`a700f78bae1478d068f454a6bcff967364fdb92661531e3b9d2358a933ecf7df`.
It is actual metadata output, not a prose reconstruction or a truncated display.
`git check-ignore` genuinely returned 1 with empty output: no selected path was
ignored. That normal nonmatch return was retained.

The planner source is [build_selection.py](build_selection.py), 241 lines,
SHA-256 `2759d6a7c858b93bc1c6399ae9ad3ad0c212968b4bc9f77c792cb78ea9b892bd`.
It writes only new plan artifacts here. All Git calls use
`GIT_OPTIONAL_LOCKS=0`; none fetches or mutates the index, worktree, objects or refs.
It is a one-shot generator, not a sync script; do not rerun it into this sealed
directory. Root should use a separate execution script and separate receipts.

## Exact baseline and mapping

The actual prior checkpoint record
`qa/GIT_OBJECT_P209_ARTIFACT_CORRECTIONS_4BC38B63.json` was read in full.
Its three exact selection/copy/staged-tree receipt pins match and are selected
for archival because they are not yet in the named baseline.

Before and after the plan, local HEAD and the already-fetched origin/main were
both `4bc38b63e7e0bbfd5365c08e5635ebc7ac9af953`, tree
`97ba076a187703d76197c310cd8f6caeb07db8ec`; divergence was 0/0 and full mirror
status was empty. No new fetch or independent network query was made here.

The documented workspace `/root/autodl-tmp/symbolic_dynamics` is not a Git
repository. Every exact selected path maps identically below the mirror root
`/root/autodl-tmp/hilbert-polya-structure`; **no legacy `symbolic_dynamics/`
prefix** is inserted for these scoped P209/current-batch/state paths. The
baseline's actual Git blobs support the mapping for existing paths.

## Included packages and limits

[CONFIG.json](CONFIG.json) and SCOPE freeze all full digests/counts, including:

- P209 complete 8,231-row paper manifest; accepted A 1,342 and B 1,472 seals.
- Final artifact 62, revisions03/04 47/136, lifecycle-root preparation four,
  and pre-completion central snapshot six.
- Scouts37–41: 73 / 156 / 130 / 155 / 196; QEF correction two and corresponding
  documentary packages 36 / 11 / 96 for scouts38/40/41.
- MNA_GATE 309 and MNA documentary audit ten, plus exactly four original
  MNA root proof/source files checked against their frozen author reference roles.
- Current STATE/PIPE/FINAL_THEOREM_CONTRACTS/Git receipt, P209 final QA,
  root37–41/P209 completion reports/native wrappers/scripts, the actual previous
  Git checkpoint record, and its exact three historical native receipts.

The six changed existing paths are the four current central controls above,
P209 `PAPER_MANIFEST.sha256`, and P209 `ROOT_LIFECYCLE.md`. The accepted A/B
packages require zero copied paths, but all their payloads remain mandatory
Git-blob verification inputs. No paper scientific text was interpreted and no
scientific source or verifier was run; only manifest-directed bytes were hashed.

The recorded MNA status remains **gate GO, root original closure pending,
not admitted**; the ten-payload documentary package is also root-inspection
pending in this snapshot. Active `qa/mna_root_pair_preparation/`,
`qa/root_replays/mna_gate_pair_01/`, future P210, all unrelated stream paths,
and this preparation's own files are excluded. No later MNA result is silently
absorbed, even if it appears while root is inspecting this plan.

## Root execution checklist

1. Read the complete config, 241-line builder, SCOPE and actual returns; verify
   this package's nonself seal.
2. Recheck the same baseline/clean mirror, all named package digests and full
   physical coverage, and every exact additional-file hash. Any subsequent
   central or MNA change needs a separately pinned explicit amendment, not an
   overwrite of this frozen plan.
3. Expand only the exact sealed manifest rows plus exact additional files.
   Their canonical path-to-SHA256 map has 12,546 keys and digest
   `84948b0e94b8462fd9548548e3545c2ccd7afe7f6036c13489cdce5db70c5d3a`;
   its precise JSON encoding is specified in SCOPE. This includes unchanged
   evidence for later Git-object checks, not just the 1,473 changed paths.
4. Copy/stage only the pinned selected bytes using root's own authorized
   script, recheck exact ignore/filter behavior, and reject deletions or
   out-of-scope staged paths. Root may explicitly add this preparation's final
   seal/payload list as a separate non-circular selection.
5. Verify every expected manifest/blob key in the actual staged tree, then
   record real commit/push/remote results. Nothing in this planning package
   claims those future operations or their success.

The project workflow guided the exact mirror mapping, original receipt pins,
change-scoped checks and exclusion of active work. It did not authorize this
lane to perform synchronization or to advance MNA's scientific lifecycle.
