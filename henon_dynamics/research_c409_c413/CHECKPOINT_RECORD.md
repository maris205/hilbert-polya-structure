# Research-checkpoint preservation record

2026-09-06. This is a research/scouting snapshot, **not a paper release**.
The batch has four unnumbered research-ready contracts, two mathematically
valid companion notes excluded from the paper count, zero new manuscripts
or PDFs, and zero formal Route-A evaluations. C409–C413 is incomplete.

## Verified research inputs

The coordinator's substantive reviews are linked from [README.md](README.md).
They record the actual proof scope, independent calculations and source
limits. The full proof statements are preserved, including the rejected
notes; rejection does not delete useful or correct mathematics.

The two independent Hénon finite-complement checkers actually ran under
Python 3.12.3 with exit status 0 and compared complete periodic point sets,
using full bounding-rectangle graphs and Boolean transitive closure.
The commands and detailed results are recorded in
[REVIEW_INTEGER_HENON_ROOT.md](REVIEW_INTEGER_HENON_ROOT.md).
Their checked hashes are:

```text
d8c6c2cf7492461d428fc988b3a773d13c99c47cd6d0e64ca468237c7fd35943  root_integer_henon_check.py
08676ceb5f17db7b702c053b15eb31c79a1393d061d6592548e34d725dfc9914  root_integer_henon_odd_check.py
```

Author diagnostics have separate bounded receipts and limitations, linked
from the README. The final closure edits concern source attribution,
exposition and selection/accounting, not the mathematics or executable
inputs. Completed unchanged tests are reused, not described as new runs.
No old sealed package was retested.

There is no PDF build receipt because no paper was drafted. There are no
manufactured training experiments, numeric Route-A passes, paper outlines
counted as manuscripts, or external peer-review claims.

## Exact snapshot policy

The checkpoint tree is `henon_dynamics/research_c409_c413/` only. It is
preserved with two generated text artifacts:

- [PAYLOAD_LEDGER.txt](PAYLOAD_LEDGER.txt) lists every actual payload file,
  excluding itself and the manifest.
- [MANIFEST.sha256](MANIFEST.sha256) hashes every payload plus the ledger,
  excluding the manifest itself.

Before sealing, a local-link/status audit examines the actual closure
documents and explicitly distinguishes reserved manifest/ledger targets
from unexpected missing files. After sealing, read-only checks must verify
both all digests and exact member-set equality: actual files equal the
ledger plus the two list files, and equal manifest members plus the
manifest. Symlinks, special files, unexpected members and duplicates are
not allowed in this snapshot. No new release program is introduced, so
there is no new release-code failure-path test to report.

The final read-only membership/digest receipt is deliberately recorded
outside this self-hashed tree, in the newest section of
[CURRENT_RESEARCH_STATE.md](../CURRENT_RESEARCH_STATE.md). This avoids
changing a hashed receipt merely to insert its own final digest. The two
list links are reserved until the actual sealing step has completed;
the external current-state receipt decides whether that step has passed.
Hashes establish byte identity and member inclusion, not mathematics.

## Integration boundary

The starting Git object was
`b9eb720eeb5aa590d784b08ef20ffbac896165b5`. Integration may stage only this
new research tree and its current-state entry. No C-number registry is
updated because there is no formal numbered admission or evaluation.

Before synchronization, inspect any remote advancement for overlap with
these paths and with repository/evaluator instructions. Preserve the old
179/93-file round2/round3 snapshots and all eight inherited untracked
directories. No force push, new remote, journal submission, public
announcement or third-party manuscript upload is authorized here.

The commit carrying this snapshot is identified by the subject
`Preserve C409-C413 four-contract research checkpoint` and the actual
Git object. Final synchronization is checked against both tracking refs
and the real remote `main` ref, not assumed from a successful local commit.
Its actual outcome belongs in the current-state closeout and user handoff;
this protocol description alone is not a claim that synchronization ran.

## Continuation boundary

Continue C409–C413 by finding an independently substantial fifth question;
do not relabel either valid companion note as a fifth paper. Reuse accepted
proof/check receipts unless their inputs change or a concrete new issue
arises. Only after five contracts pass should paper numbering, writing,
formal evaluation, PDF verification and paper release begin.
