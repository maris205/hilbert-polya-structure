# Fixed Git-object audit: P203 Round1 / A at 9a394

Date: 2026-09-05 UTC. Status: **SCOPED_GIT_OBJECT_AND_MANIFEST_PASS**,
using the four explicit historical mirror-path mappings below.
This is mechanical archive/QA engineering, not independent mathematics review
or a new acceptance of P203. This process co-contributed the MCT temporal proof
and is not eligible to claim an independent manuscript review of P203.

## Fixed input and actual method

- Commit: `9a394ee2c3ab171ba4341d77c439ba145e247a85`.
- Parent: `82293de4105ccc0139acc288a26278261b3426a2`.
- Mirror: `/root/autodl-tmp/hilbert-polya-structure`.
- Workspace: `/root/autodl-tmp/symbolic_dynamics`.

An actual fresh read-only process enumerated the fixed Git tree, retrieved raw
blobs using `git cat-file --batch`, and compared their complete bytes directly
against workspace files. It then recomputed package-local manifest digests on
both sides, expanded referenced child manifests and compared their union with
the exact recursive file inventory. No comparison used a copied mirror file
in place of a Git object. No verifier, proof check or LaTeX build was run.

## Results

| Scope | Actual files | Byte differences |
|---|---:|---:|
| P203 complete current Round1 paper package | 187 | 0 |
| P203 complete Review A package | 55 | 0 |
| `qa/audit_batch.py` | 1 | 0 |
| `qa/P203_ADAPTER_CHECKS.txt` | 1 | 0 |
| `qa/P203_SCHEMA_ADAPTER_RECEIPT.md` | 1 | 0 |
| **Total** | **245** | **0** |

All **20,981,544 bytes** match. Missing committed files, extra workspace files
within these scopes, and symlinks: **0** each. Frozen Round0/1, revision A,
PDFs, nested QA, source downloads and current-input payloads are included in
the complete paper count; review QA and repair/source metadata are included
in the A count.

The paper's recursive manifest closure covers **187/187** files. Review A's
parent-plus-child manifest closure covers **55/55** files. There are no
uncovered or extraneous entries. **15** parsed local manifests provide
**419** actual row checks; every pinned digest matches both the fixed Git
object and workspace bytes. This is a count of hash checks, including repeated
targets, not additional files or mathematical assertions.

The live, frozen Round0 and frozen Round1 `CURRENT_INPUTS_SHA256SUMS` each
represent their entire physical and Git `current_inputs/` directory:
**11/11** files in each copy, no missing or extra path. These counts were read
from actual inventories, not assumed as an acceptance threshold.

## Review A input pins: exact archived bytes, explicit locations

All **28** lines of Review A's `PINNED_INPUTS.sha256` match their actual fixed
Git blob hashes and current workspace bytes. **24** inputs have identical
workspace-root-relative and Git-root-relative paths. The remaining four use
the pre-existing split historical layout:

| Workspace-root-relative input | Actual Git path in 9a394 |
|---|---|
| `docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md` | `symbolic_dynamics/docs/papers147_151_sequence/scouting/combinatorial/SCOUT.md` |
| `papers/112-tournament-score-upset-reversal/main.tex` | `symbolic_dynamics/papers/112-tournament-score-upset-reversal/main.tex` |
| `papers/123-odd-component-complementation/main.tex` | `symbolic_dynamics/papers/123-odd-component-complementation/main.tex` |
| `papers/152-triad-dynamics-triangular-books/main.tex` | `symbolic_dynamics/papers/152-triad-dynamics-triangular-books/main.tex` |

The first strict extra-pin pass actually stopped at row23 with an assertion
because the unprefixed Git-root path does not exist. A diagnostic fixed-tree
lookup established the four locations above. A fresh complete pass then
checked their raw archived bytes using only these explicit mappings and
passed all 28 pins. No frozen pin or archive path was edited. Consequently,
this report does **not** claim that the workspace-relative pin list can be
run from the Git mirror root without layout adaptation.

The 28 references are input checks, some outside the 245 primary files and
some already counted there. They are not added blindly to the unique-file
total. Their paths, blob OIDs and all three digests are in the detail record.

## Exclusions and non-mutation

`reviews/p203_b/` contains **0 files in this fixed commit**. It had 20 live
files at the time of the read; that active lane was excluded and is not
represented as accepted or backed up by 9a394. The checkpoint is Round1/A,
not Round2, P203 terminal acceptance or five-paper completion.

Before and after the successful process, HEAD and local `origin/main` were
9a394. The only dirty mirror file was root's announced
`symbolic_dynamics/README.md`; its SHA-256 stayed
`d2c8d1604fc177322066cee7d486db659cba5475a4ca185500871a338eb5245a`.
It was not changed or reverted. These local-ref observations are not a new
network check of the remote server; this task performed no fetch or push.

Only this new receipt and its independent detail file were written. The
preceding 82293 receipt/details, accepted paper/review/frozen/canonical files,
manifests, central state and all Git state were left unchanged.

## Durable details

`GIT_OBJECT_AUDIT_9A394_R1_DETAILS.txt` contains all 245 file paths, modes,
sizes, blob OIDs, both byte digests, complete manifest checks and coverage,
all 28 input-pin checks, path mappings and actual before/after observations.

Detail SHA-256:
`665e79fdf9de1e32651baa14cdd3ef06ae0b5334cb8d65b8738662921bb45d95`.
