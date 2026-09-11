# Independent artifact audit of checkpoint ff020cec

2026-09-06 06:49 UTC. Auditor: `/root/batch197_lzk_gate`.
Result: **PASS_SCOPED_ARTIFACT_AUDIT**, with no new defect found.
The pre-existing MNC machine role-label defect remains preserved and is
correctly explained by the committed human-readable addendum below.

This is a read-only Git/object/role/link audit, not a mathematical review,
candidate admission, manuscript review or new numerical execution. The
auditor authored MNC's proof package and does not independently review
that science here. Only this new audit file was written; gates, author
packages, central state and Git were not modified. Research-workflow
evidence and role boundaries govern this artifact-only check.

## Ref, ownership and archive boundary

The actual mirror is `/root/autodl-tmp/hilbert-polya-structure`, not the
workspace, which is not a Git repository. Read-only `git show`,
`diff-tree`, `ls-tree`, `rev-parse`, `merge-base`, `rev-list`, `status`
and `ls-remote` were used. The inspected exact commit is

`ff020cec61ee121f7d9c77e349faa2d5c7e9e1fc`.

Its sole parent is `ae2fdc72c865a61369ef74d03d5b266a94ace86d`.
The parent's 21 changed paths are all under `henon_dynamics/`, and
`merge-base --is-ancestor` exited zero. This is consistent with the
recorded disjoint fast-forward; no fetch, merge or push was performed
by this auditor. A fresh `ls-remote --heads origin main` returned the
exact checkpoint SHA above. Local HEAD matched it, ahead/behind against
`origin/main` was `0 0`, and mirror status was empty before and after.

`diff-tree --no-commit-id --name-only -r` gives exactly **169 changed
files**. Every path is either the root recovery state or under
`docs/papers204_208_sequence/`; no foreign-stream change appears.

| Changed scope | Files |
|---|---:|
| Root state and two batch indexes/receipts | 3 |
| QA helper and prior object-audit files | 3 |
| Root combined author-inspection note | 1 |
| Root CPRM boundary evidence | 5 |
| Root MNC author replay evidence | 15 |
| Root MNC independent-producer replay evidence | 16 |
| Root UGR author replay evidence | 15 |
| Closed seventh geometry package | 15 |
| Closed MNC author package (`CONTRAST_PROOF_WORK`) | 26 |
| Closed MNC nonauthor candidate gate | 30 |
| Closed UGR author package | 28 |
| Remaining word-local arithmetic/boundary/disposition files | 12 |
| Total | 169 |

The complete tree at this ref contains no `UGR_GATE/`,
`HVD_PROOF_WORK/`, `finite_structures_eighth/` or `__pycache__/` paths.
Thus the active-work exclusions in the
[root sync receipt](../GIT_SYNC_RECEIPT.md) are correct. Later UGR gate
closure and possible admission are not attributed to this historical ref.
The FF020CEC post-push object receipt is itself absent from that commit,
as the current receipt explicitly discloses. The historical root state
still reports the preceding push; the current post-push receipt/state
is not misrepresented as self-included in the commit it records.

## Fresh Git-object checks, not fresh mathematical checks

After reading `check_named_git_manifests.py` completely, this auditor
actually ran its read-only check on the exact ref and the same four
explicit manifests named in
[the root object receipt](GIT_OBJECT_CANDIDATES_FF020CEC.json).
It exited zero: **95 entries, zero missing or mismatched objects**.
Independent tree-versus-manifest set comparison additionally checked
coverage for these four packages, beyond that helper's stated scope:

| Package | Nonself hash entries | Actual Git files including manifest | Missing / unlisted nonself |
|---|---:|---:|---:|
| UGR author | 27 | 28 | 0 / 0 |
| MNC author | 25 | 26 | 0 / 0 |
| MNC gate | 29 | 30 | 0 / 0 |
| Seventh geometry | 14 | 15 | 0 / 0 |
| Total | 95 | 99 | 0 / 0 |

This confirms directory-relative package object closure, not portability
of workspace-root-relative/absolute input pins and not mathematical
correctness. The original helper correctly disclaims path-set coverage;
the extra coverage result above belongs to this audit, not retroactively
to its earlier receipt. All four original manifests remain unchanged.

## Source/output roles and the known label defect

The actual reusable root harness source, all three root machine receipts,
their explicit producer paths, and archived Git source/stdout objects
were checked. For each pair, the pinned producer matches its Git blob,
both stored stdout hashes/sizes match the blobs, the two complete archived
stdout byte strings equal their corresponding canonical, the original
recorded child/comparator exits are zero, package before/after snapshots
agree, and all archived child/comparator stderr streams are empty.

| Root receipt directory | Actual producer | Original assertions per execution | Correct role |
|---|---|---:|---|
| `mnc_author` | `CONTRAST_PROOF_WORK/verify_mnc.py` | 356,509 | Root replay of author code |
| `ugr_author` | `UGR_PROOF_WORK/verify_ugr.py` | 33,321 | Root replay of author code |
| `mnc_gate` | `MNC_GATE/verify.py` | 293,461 | Root replay of the nonauthor gate producer |

These assertion totals are read from preserved execution evidence;
**no producer was rerun in this audit**. The archived `mnc_gate` machine
receipt still has the harness's hard-coded `AUTHOR_PRODUCER` kind.
The [committed correction](root_replays/mnc_gate/RECEIPT.md) explicitly
identifies the actual independent gate producer and preserves the wrong
original label. It also says that root, an MNC contributor, is not a
third independent reviewer. The
[root disposition](../scouting/word_local/MNC_ROOT_DISPOSITION.md)
links that correction and retains MNC-V1 Critical/open and NO_ADMISSION.
The [combined author inspection](root_replays/RANK_CONTRAST_AUTHOR_INSPECTION.md)
likewise excludes independent-review, admission and source-clearance
credit for the author replays.

Thus the known machine-only ambiguity is documented, not a newly repaired
scientific result. Consumers must use the explicit command/source pins
and the role-label addendum, not classify solely by that old `kind` value.
No reviewed status document turns these checks into a third independent
science review, a manuscript acceptance, or five completed current papers.
The checkpoint state says one retained/completed paper and four open
seats; its separately labelled previous completed batch is not conflated
with the active batch. MNC's adverse ledger remains open as intended.

## Workspace links and final boundary

All 23 changed Markdown files were checked in the actual workspace,
including the current root/batch sync statements and new role/disposition
notes. The check resolved **125 non-HTTP local link occurrences** relative
to each document's workspace location: zero missing targets. This
includes the new MNC disposition-to-root-receipt link, root receipt-to-JSON
link, author-pair links and the current sync-to-object-receipt link.
External URLs and fragment/heading correctness were outside this bounded
existence check. Old mirror split-path links were not mistaken for missing
workspace artifacts, and no whole-history link audit is claimed.

No action is required by this audit. Preserve the existing role correction,
active exclusions and post-commit receipt boundary. Continue root's
separate UGR admission/replay work; any future P207 manuscript A must
start from its actual frozen Round0, not from this artifact audit or the
candidate scout inputs. `HOLD_EXTERNAL` remains unchanged.
