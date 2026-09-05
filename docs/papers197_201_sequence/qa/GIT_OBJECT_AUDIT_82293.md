# Fixed-commit Git-object audit: 82293 / 8190

Date: 2026-09-05 UTC. Status: **SCOPED_GIT_OBJECT_BYTES_PASS**, with the
pre-existing MCT intermediate-code pin caveat explicitly preserved below.
This is a mechanical archive check, not a mathematics review, new paper
acceptance, proof replay, source-clearance certificate or five-paper completion.
The auditing process authored P202 and co-contributed MCT/P203; it does not
claim independent scientific certification of either paper.

## Exact objects and method

- Mirror: `/root/autodl-tmp/hilbert-polya-structure`.
- Workspace: `/root/autodl-tmp/symbolic_dynamics`.
- Fixed merge: `82293de4105ccc0139acc288a26278261b3426a2`.
- Fixed research parent: `8190c0499bd5edc19e97c7a8d2331076a8df5cb0`.
- Other parent: `697518b6db90458f86f7916fbf397b8ad5ef2372`.
- Common base: `908069ac646c281941788b49e09c0671bf8be0b8`.

The auditor enumerated fixed trees with `git ls-tree -r -z`, retrieved actual
blob bytes with `git cat-file --batch`, and directly compared those bytes with
each workspace file. It did not compare two filesystem copies. Git mode/type/OID
comparisons separately establish equality between the two specified checkpoint
trees in scope. Inventories include every recursive regular file, all nested
manifests, frozen rounds, PDFs, code, logs and visual-QA payloads; none were
silently excluded. No symlinks were found in the checked scope.

## Actual byte and manifest results

| Scope | Files compared |
|---|---:|
| P197 complete current paper package | 82 |
| P199 complete current paper package | 141 |
| P200 complete current paper package | 117 |
| P202 complete current paper package | 185 |
| P197 A / B complete review packages | 23 / 32 |
| P199 A / B complete review packages | 25 / 28 |
| P200 A / B complete review packages | 28 / 28 |
| P202 A / B complete review packages | 44 / 41 |
| MCT scout / temporal / Stage1 / pin supplement | 10 / 11 / 13 / 13 |
| All six breadth-snapshot directories | 15 |
| Current breadth index, reconciliation, LFCTR correction, MCT adjudication | 4 |
| Historical artifact JSON snapshot and paper TSV index | 2 |
| **Unique total** | **842** |

All **39,285,756 bytes** compared equal. Workspace files absent from the fixed
commit: **0**. Committed scoped files absent from the workspace: **0**.
Byte differences: **0**. Scoped mode/type/OID differences between research
parent and merge: **0**.

In addition, all **36 package-local `SHA256SUMS` / `QA_SHA256SUMS` manifests**
were parsed: **1,081 rows** were checked against both the fixed Git blob and
workspace SHA-256, with **0 errors**. Repeated files across nested manifests
are repeated checks, not additional unique-file counts. This statement does
not claim every historical external input-pin document passes.

## Merge isolation, precisely stated

The fixed commit has exactly the two parents listed above. Relative to the
common base, the research parent changes **177 paths**, while the other parent
changes **251 paths**; these changed-path sets are disjoint. Every path in the
251-set is under `henon_dynamics/`.

- Research parent -> merge: **251** changed paths, all `henon_dynamics/`.
- Other parent -> merge: **177** changed paths, none `henon_dynamics/`.
- Comparing full recursive tree entries, the entire non-henon part of the
  merge equals the research parent, and the entire henon subtree equals the
  other parent.

Thus the merge preserves both checked branches without a symbolic overwrite
from the henon branch. It would be incorrect to describe *both* parent-to-merge
diffs as 251 henon files. This check does not certify all historical symbolic
material is synchronized or resolve the documented split-layout/missing-paper
history.

## Breadth and immutable-history checks

The fixed current TSV has **83 records**: **57** current attempts,
**18** historical controls (17 ordinary plus one conjugate control), and
**8** code-only WIP records. The 57 current dispositions are exactly
**5 selected + 3 reserve + 49 kill**. Selected identifiers are
MCT/OR/TCSD/LFAS/FOSP; reserves are ND1/SDD/ZCI. LFCTR retains its row with
historical weight zero and `KILL_EXACT_INTERNAL_Q01`.

All fifteen breadth-snapshot files are byte-backed in both fixed commits.
The nine older snapshot files already present in `908069ac` retain identical
Git objects; the six second-replacement57/provisional58 files are newly
present in this checkpoint, not claimed to have existed in the older one.
In particular the preserved first-replacement54 hashes remain:

- TSV: `18a93958a656615a31a4313845bdffad28a4365d166d06b744a661a9dec165dc`.
- Reconciliation: `c270ee3dcb6761c49b58cbf62176233a36a4be394804152e786a7070cc9e5638`.

The two historical research-state snapshot/index files also retain their
`908069ac` Git objects. These are archive/count checks, not a new adjudication
of the map classifications.

The frozen temporal historical input-pin document was separately spot-checked:
**3 pins match and 1 remains mismatched**, as already documented. Old `probe.py`
pin `7672dea68f66714f1415fec3a507ea06b1ca1beb18c03ac65fc51753f3fea1f7`
differs from the actually archived current author program
`1e40d08722268ab476a8687d1f0204a5dd3f5b2dc6c7046eb0d887c63d36b937`.
The current program and append-only supplement match their Git objects; this
does not recover the missing old program bytes or convert the old pin to PASS.
An initial extra-source lookup using the workspace-relative historical docs
path failed because older material lives beneath `symbolic_dynamics/` in Git;
the subsequent explicit documented-layout lookup matched the expected hash.

## Expected exclusions and observed worktree state

P203's paper and A/B review directories each contain **zero Git files** in
both fixed `82293` and `8190` objects. They are expected exclusions from this
checkpoint. Live counts at the read were paper187, A55, B0; those counts are
time-of-read observations only, not a terminal-state assertion.

Initial preflight found a clean mirror with HEAD and local `origin/main` at
82293. Root then independently created checkpoint `9a394ee2`; the actual
fixed-object comparison process began and ended with clean status at that new
HEAD, while continuing to read **82293/8190**, never floating HEAD. A later
supplemental status showed only root's announced `symbolic_dynamics/README.md`
edit. It was preserved without interference. Local tracking refs are not a new
remote-server verification, and this audit did not fetch or push.

Only this receipt and its new detail file are written by this task. No Git
operation changed state; no accepted paper/review/frozen/canonical/manifest,
central index or previous audit record was edited. No mathematics verifier,
LaTeX build or manuscript review was rerun.

## Durable detail record

`GIT_OBJECT_AUDIT_82293_DETAILS.txt` records all 842 file paths, modes, blob OIDs,
sizes, both SHA-256 values, group inventories, all manifest row counts, both
merge-diff path sets, exact snapshot hashes and historical pin observations.

Detail SHA-256:
`23b276a1df69e9409def0e27bc7d820c86b6aac70b14a305aa8c29687c7e17c9`.
