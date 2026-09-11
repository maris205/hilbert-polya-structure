# Fixed Git-object audit: 79e872 final-artifact checkpoint

Date: 2026-09-05 UTC. Status: **FIXED_SCIENTIFIC_ARCHIVE_PASS**, with exactly
five declared post-checkpoint lifecycle differences and a separately passing
current-manifest hash refresh.

This is mechanical archive/QA engineering, not a new mathematics review,
verifier replay, LaTeX build, visual manuscript review or novelty certificate.
The checking process contributed to P200's proof, authored P202 and
co-contributed P203; it does not claim independent scientific review of those
papers. Root's separately reported full terminal run is not this process.

## Fixed checkpoint and scope

- Commit: `79e8729b5c25bbf3140482f7fd2ece7d32f09b79`.
- Parent: `9a394ee2c3ab171ba4341d77c439ba145e247a85`.
- Mirror: `/root/autodl-tmp/hilbert-polya-structure`.
- Workspace: `/root/autodl-tmp/symbolic_dynamics`.

**79e is the Round2/final-build evidence checkpoint created before the
all-five terminal audit passed, not a five-paper completion commit.** Later
root lifecycle updates are distinguished below; they are not retroactively
attributed to this fixed Git object.

The actual fresh read-only process enumerated fixed trees with
`git ls-tree -r -z`, retrieved raw blobs with `git cat-file --batch`, and
compared complete bytes with each workspace file. It recomputed manifest
digests against both sides and checked exact recursive inventory coverage.
No comparison substituted a filesystem mirror copy for a Git object. An
initial oversized output was truncated; the durable results below come from
the successful fresh compact-output run and its later hash-only supplement.

## Complete file inventories and byte comparisons

| Scope | Files |
|---|---:|
| P197 complete paper package | 82 |
| P199 complete paper package | 141 |
| P200 complete paper package | 117 |
| P202 complete paper package | 185 |
| P203 complete paper package | 260 |
| **Five paper packages** | **785** |
| P197 A/B | 23 / 32 |
| P199 A/B | 25 / 28 |
| P200 A/B | 28 / 28 |
| P202 A/B | 44 / 41 |
| P203 A/B | 55 / 36 |
| **Ten complete review packages** | **340** |
| Two global manifests and four QA scripts | 6 |
| **Total** | **1,131** |

The fixed blobs total **68,366,049 bytes**. Workspace and fixed-Git inventories
agree exactly: missing files **0**, extra files **0**, symlinks **0**.
**1,126 files match byte-for-byte. Exactly five files differ**, all in root's
announced lifecycle refresh below. There is no unexplained scientific,
frozen, review, code, canonical, PDF or final-QA byte difference.

The four QA scripts are `audit_batch.py`, `audit_retained_subset.py`,
`review_cold_build.sh` and `run_final_cold_builds.sh`. Their bytes match the
checkpoint; none was executed as a terminal audit in this task.

## Recursive manifests and final build/visual evidence

All fifteen top package/review manifest closures cover their complete
recursive inventories exactly. Nested `SHA256SUMS` and the historical
top-level `QA_SHA256SUMS` lists were expanded, not merely hashed as opaque
files. **52 manifests, 1,650 rows** were checked against actual fixed Git
blobs, with **zero fixed-Git digest errors**.

Comparing those *old checkpoint manifests* to the subsequently updated
workspace yields four expected target-digest differences: three P203
lifecycle documents and P203's top manifest. These are not reported as
workspace PASS under the old digests. The newly refreshed workspace
manifests are independently checked in the next section.

Each `qa_final/` is exactly **33 files**, including its own manifest:
**165 files total**, all byte-identical to the checkpoint and fully covered.
Each of the ten existing cold-build directories contains 13 archived files.
For each build, `main.tex`, `references.bib` and `main.pdf` equal the current
paper's corresponding scientific bytes. Logs and other build outputs were
included in the raw-object comparison; no new build was performed.

Read-only `pdfinfo` confirms five current four-page PDFs, **20 pages total**.
All **20 existing PNG page images** are archived byte-identically; exact page
names, PNG signatures/dimensions and each visual `SOURCE_PDF.sha256` binding
were checked. This is image-artifact integrity, not a new visual assessment
of the manuscript pages.

## All fifteen frozen rounds and historical preservation

All fifteen actual frozen-round directories are present with their four
required source/bibliography/verifier/canonical files. The **seven historical
core-only freezes** remain in their original form; this task did not invent
internal PDFs or manifests for them. The other **eight full freezes** have
complete nonself manifests and internal PDFs matching their labelled round
PDFs. P199/P200 retain their original `round0_snapshot/` path convention.

All five Round2 source/bibliography/verifier/canonical sets equal the current
paper scientific files, and current PDFs equal their labelled Round2 PDFs.
P203's live and three frozen `current_inputs/` directories each have their
complete **11/11** files represented by the corresponding actual manifest.
Historical pin-list documents inside them were hashed, not recursively run.

Stronger fixed-tree preservation checks also passed:

- The entire earlier four-paper packages, **525 files**, have unchanged
  path/mode/type/blob-OID entries against research commit
  `8190c0499bd5edc19e97c7a8d2331076a8df5cb0`. This includes all their frozen
  source/code/PDF evidence, not merely a selected theorem file.
- P203's complete Round0 and Round1 freezes and their labelled PDFs retain
  their exact `9a394ee2` objects.
- P203 Round1 and Round2 have identical relative inventories and all
  **37 relative file objects** match, consistent with the unchanged B delta.

P203's two historical PDF roles remain distinct:

- Original Round0: `617cea5d4f8b50a9946d05bafc2cfbf6fb01bbe45dab754813b07f4f12cc1167`.
- Current/Round1/Round2: `0738965406c046662618ec999474738c064c363fa66ba587e7b33a377f89b47d`.

Actual read-only text extraction confirms the original lacks `HOLD_EXTERNAL`,
while current/Round1/Round2 contain it. The preserved original was not
silently overwritten or relabelled as the repaired version.

## Review input pins and the two global manifests

All ten review pin-list files match the fixed commit. All **195 input rows**,
representing **150 distinct workspace paths**, match both their pinned hash
and actual archived raw bytes. The documented `symbolic_dynamics/` prefix is
used for older paper/batch-doc inputs; P200 B's absolute workspace paths are
normalized explicitly. No missing or wrong-version historical input was found
in this bounded union.

Reading a historical pin-list *file* does not execute its old dependencies.
In particular this task does not change the preserved temporal **3 PASS /
1 failed old-code pin** or recover the missing intermediate program.

Both fixed global manifests contain exactly the expected five distinct
targets and every digest matches its fixed Git object:

- `CANONICAL_PDF_MANIFEST.sha256` -> the five `main_round2.pdf` files;
  manifest SHA `b65f36f5bf1ea032693ea9f8bec597d07b5af4ce49beff0a32e40085bba0874a`.
- `PACKAGE_MANIFESTS.sha256` -> the five paper `SHA256SUMS` files;
  fixed manifest SHA `088dd47c01d0fd40b15d111c1cfd82bae8826eb92e32e36135cd431761ccbd84`.

## Exact post-checkpoint lifecycle delta and fresh hash closure

Root announced these edits only after its separate terminal run completed.
The fresh fixed-object comparison observed exactly:

1. P203 `README.md`.
2. P203 `PAPER_IMPROVEMENT_STATE.md`.
3. P203 `IMPROVEMENT_LOG.md`.
4. P203 current `SHA256SUMS`.
5. Batch `PACKAGE_MANIFESTS.sha256`.

The first three are lifecycle/completion commentary. Their full before/after
hashes and actual text diffs are in the detail record. The current paper
manifest changes exactly their three target hashes, with no path added or
removed. Its new SHA is
`447459ff4e8c7e54b24a9cf3086565b9ca1906a7752c5b0dffc74906a211c78d`.
A fresh read checked all **259 payload rows** and exact **260-file coverage**;
all pass against current workspace bytes.

The current global package manifest changes exactly the P203 paper-manifest
row. Its new SHA is
`dc784add27d2a9e536bf1041eb90a0405c966c4b22bd6fc73fa22d707d5a23bb`.
The current canonical-PDF global manifest is unchanged. Both current global
lists retain exactly five expected targets and all ten current digest checks
pass. This is a **hash-only refresh**, not another mathematical execution or
an assertion that the new lifecycle bytes were already in fixed79e.

## Non-mutation and durable evidence

The mirror was clean at the actual before/after observations, with HEAD and
local `origin/main` at79e. Lifecycle changes above occurred in the separate
non-Git workspace. No Git state, accepted artifact, frozen version, review,
manifest, central index or earlier audit was edited by this task. Only this
new receipt and its detail file were added. No fetch/push or new remote-server
check occurred, and no all-history synchronization claim follows.

`GIT_OBJECT_AUDIT_79E872_FINAL_ARTIFACTS_DETAILS.txt` records every scoped file's
path/mode/blob-OID/size/hashes, all coverage and manifest results, all fifteen
freezes, cold-build/image records, all195 review pins, both global target sets,
the exact five lifecycle diffs and current hash-refresh results.

Detail SHA-256:
`c40c84867081b97e49d963288f6bea9f87aa7e337037f2980b8183466f9ff806`.
