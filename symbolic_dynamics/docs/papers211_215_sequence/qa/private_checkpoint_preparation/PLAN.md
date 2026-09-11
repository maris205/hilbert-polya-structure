# Closed-scout private checkpoint: preparation only

2026-09-08 UTC. Owner `/root/round211_nonlinear_scout`.
Status: `PREPARED / NO_CAPTURE_STAGE_COMMIT_PUSH_EXECUTED`.
Root must read the complete executor and exact current preview before
authorizing any phase. The standing private-sync authorization does not
turn this preparation assignment into permission to execute its mutations.

## Outcome and repository roles

Prepare a private checkpoint of the 18 closed literal attempts and bounded
NO_FRESH desk, with zero retained/completed new papers and all adverse
findings preserved. This is neither a new scientific run nor a paper PASS.

- Source workspace: `/root/autodl-tmp/symbolic_dynamics`, not a Git worktree.
- Accepted destination: `/root/symbolic-dynamics-private-sync-accepted-20260907.git`.
  Bare `HEAD` names `refs/heads/main`; current baseline
  `cd6066f471631bab7aa544867678578c573c03b1`, tree
  `4d6425878bf347448abeed4e4260fb2013420cc0`.
- Protected original mirror: `/root/autodl-tmp/hilbert-polya-structure`,
  at `a380d24718fec4ef27365f44e96fb7ffa2b0fd10`, clean in the actual
  read-only porcelain query. It is never used as an index or worktree
  destination. The accepted bare's worktree status is **N/A**.
- The bare has no configured remote. Use the actual original-mirror URL
  `git@github.com:maris205/hilbert-polya-structure.git` explicitly for
  every `ls-remote` and normal push. Do not create an `origin` entry.
- Existing author/committer identity is `mariswang / wangliang.f@gmail.com`,
  checked against the baseline commit. Use command-local identity variables;
  do not change Git configuration.

Preparation executes only allowlisted read-only Git queries with optional
locks disabled, plus local artifact reads/writes inside this directory.
It does not repeat root's latest remote query. Capture must make its own
successful explicit-URL remote query before relying on the baseline.

## Exact allowed scope and root decisions

All selected paths are identity-mapped from workspace to Git root:

| Role | Exact selected roots |
|---|---|
| Current controls | `SYMBOLIC_DYNAMICS_STATE.md`; `docs/papers211_215_sequence/PROBLEM_ANCHOR.md`; `docs/papers211_215_sequence/PIPELINE_STATE.md` |
| Closed lanes under `docs/papers211_215_sequence/scouting/` | `combinatorial_lane`, `graph_lane`, `algebra_lane`, `root_zigzag`, `residual_desk`, `set_code_lane`, `nonlinear_lane`, `tree_order_lane` |
| Root evidence | `docs/papers211_215_sequence/scouting/root_reception` |
| Two root-approved older metadata files | `docs/papers204_208_sequence/qa/FIVE_PRIVATE_SYNC_ROOT_INSPECTION.md`; `docs/papers204_208_sequence/qa/FIVE_PRIVATE_SYNC_ROOT_ACCEPTANCE.actual.json` |

Tree/order was initially excluded while active. Root subsequently accepted
its closed packet and explicitly added the exact 20-file sealed lane plus
the new TREE_NONLINEAR root reception. Root then refreshed PIPE followed by
STATE to 18 closed and announced a capture hold on further control edits.

The two older metadata files were explicitly approved as a minimal link
closure: current STATE links the post-push root inspection, which in turn
links the formal acceptance JSON. Both are absent from the baseline commit.
They document that older commit; adding them now never puts them retroactively
inside it. Their recorded historical commands, failures and paths stay intact.

Explicit exclusions remain:

- `scouting/arithmetic_lane`, `scouting/spr_gate`,
  `scouting/spr_root_reception`, and `scouting/transport_lane` under the new batch.
- Old `docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md` and old
  `docs/papers204_208_sequence/PIPELINE_STATE.md`: root declined their refresh.
  Their local versions are later than their baseline versions; this checkpoint
  must preserve the baseline bytes for those unselected keys.
- This preparation directory, all new execution directories and later
  receipts; all other old manuscripts, reviews, failed packets and unrelated
  local changes. The large old P209 execution archive remains local-only.

ROOTS are merely the approved selection boundary. The runnable plan contains
the full exact pathname/mode/byte-length/SHA256/Git-blob-OID inventory.
Any later selected addition, deletion or byte change makes that preview stale;
generate a new numbered preview and obtain renewed root approval. No automatic
directory expansion occurs during capture or later phases.

## Frozen inputs and proportional verification

Eight complete nonself lane manifests are checked. Their explicit inherited
pin lists are verified without copying old papers or runtime installations.
The set/code list's two old live-control keys resolve only to
`root_reception/control_initial13/{SYMBOLIC_DYNAMICS_STATE,PIPELINE_STATE}.md`.
The desk already pins its literal `residual_desk/snapshots/` keys. Both mappings
are recorded in PLAN.json; current control bytes are separate selected keys.
No historical manifest is edited to make a live-control mismatch disappear.

Capture creates a new private `tempfile.mkdtemp` directory under `/root`,
with another unique directory for its isolated index. It freezes **only**
the selected approximately 3.93 MB of bytes and the approved plan/executor.
The snapshot preserves Git executable modes and is re-read against the
approved exact inventory. Live sources are checked before/after copying and
again at the end of capture; subsequent phases exclusively use the frozen
snapshot, so a later source-index update is not silently included.

The entire selected-payload limit is 10,000,000 bytes. Disk capacity is checked
for snapshot, loose objects, a pack and compact native records. No whole
workspace, old batch, repository baseline, host inventory or object-body dump
is copied. Metadata-only `cat-file --batch-check` covers selected objects.

An isolated index begins at the exact baseline tree. Only selected changed
paths are passed to unfiltered `hash-object` and `update-index`. The resulting
tree and selected index records must equal the frozen mode/OID inventory.
An **unfiltered complete baseline-to-new-tree raw diff** must contain exactly
the expected selected additions/modifications, with no deletions, renames or
nonselected entries. This establishes nonselected-tree preservation without
archiving the prior approximately 11 MB complete tree/index streams.

## Four separate phases — not executed here

1. **capture:** verify the exact approved plan/source, existing roles, actual
   remote baseline and no missing selected baseline path; create the bounded
   frozen snapshot and isolated-index location. No Git object/index/ref write.
2. **stage:** initialize only the new isolated index from BASE; write only
   selected changed blobs from frozen files; verify exact index, tree, complete
   diff and selected object type/OID/length metadata. No commit or ref update.
3. **commit:** verify the stage again; create an ordinary one-parent commit
   object with the existing command-local identity. Preserve local main at BASE.
4. **push:** reverify frozen evidence and actual remote BASE; normal non-force
   push of the exact commit to remote main; actually confirm it; only then
   compare-and-swap the accepted bare main from BASE to that commit, followed
   by fresh local/remote confirmation and tree checks.

Every phase requires the exact approved PLAN.json SHA256; phases after capture
also require the actual successful preceding phase-manifest digest. Run the
frozen `executed_source.py` for later phases. No phase follows automatically.
Preparation tokens and future native digests are distinct; none is fabricated.

Example syntax, with real hashes/run path supplied only after root approval:

```text
/usr/bin/python3 -I -S -B checkpoint.py capture --plan /ABS/PREVIEW/PLAN.json --approved-plan-sha256 ACTUAL_APPROVED_HASH
/usr/bin/python3 -I -S -B /root/ACTUAL_RUN/executed_source.py stage --run /root/ACTUAL_RUN --approved-plan-sha256 ACTUAL_APPROVED_HASH --previous-phase-sha256 ACTUAL_CAPTURE_SEAL
```

Commit/push use the corresponding phase names and actual prior seals. These
examples are documentation, not executed commands or synthetic receipts.

## Failure, protection and evidence rules

Each native command stores exact argv, cwd, controlled environment, stdin,
complete stdout/stderr, spawn PID, actual return code and timeout disposition.
Timeouts retain partial streams and terminate the command's own process group;
they do not trigger automatic retries or claim remote success. Failed phases
retain FAILURE.json and every raw command original. No rollback or cleanup
command exists. A used phase/index cannot be overwritten, even after failure.
If a push succeeds remotely but a later confirmation/CAS fails, stop and ask
root to inspect the retained commands and current refs; do not force-push,
reset or silently rerun. A remote advance likewise requires root resolution.

The original mirror's HEAD/config/index/packed-ref roles and the accepted
bare's config/HEAD/default-index roles are protected with exact presence/byte
pins. Command-local config disables hooks, automatic GC/maintenance, prompts
and inherited Git override variables. The explicit SSH command preserves
normal strict host-key checking. This is scoped operational provenance,
not a claim of complete Git/SSH loader hermeticity.

See READONLY_LIMITS.md for initial diagnostic failures and source-read limits.
Pure/static checks do not test Git mutation behavior. This author is not an
independent reviewer of this executor. Root must inspect it before execution.
External status is `OWNER_AMBER / HOLD_EXTERNAL` throughout.
