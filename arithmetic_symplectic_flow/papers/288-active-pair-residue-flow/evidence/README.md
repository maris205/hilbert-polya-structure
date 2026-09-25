# Evidence — active-pair partial residue owner

Candidate ID: `ANG-20260920-APR01`.
Status: `OWNED ACTIVE-SOURCE PRIME PACKETS; NATURALNESS OPEN — SCOPED ADVANCE / FORK`.

## Definition freeze and source identity

The original [version-1 card](../candidate-card.md) has SHA-256

    1459ec2252afe8d84736c986ac4f572104bc4c6b0d3031672ac780a1f03fc3d4

The unchanged proposal came from [287's separate scout record](../../287-nonlinear-two-seed-residue-flow/evidence/scout-record.md),
whose bound SHA-256 is

    a397bd941d601dc70975dec53e6c45e408c8e5cb348d914076f91790c475f544

That record was UNTESTED and supplied no theorem. The present full
partial owner is newly proved. All a,b>=2, every K² seed, terminal
state, missing incoming root, actual branch and finite preimage remain.

The [manuscript](../paper.md) supplied after the raw-card review has
SHA-256

    b20fa7e047eabcb036e95b60a6a2255f60bb11419ef9d588df7c5d86d86c78b8

## Exact methods and controls

Methods: clopen residue-domain analysis; branch inversion; Borel joint
Haar shear/scale law; partial-tail composition and actual synchronous
refinement; nonnegative cyclic integer sums; all-period integer-matrix
determinants; full isotropy conjugation; and finite inverse-word accounting.

The fixed terminal/missing-root controls (4,2), (3,2), (2,4) are exact
checks, not a numerical sample supporting the global claims. Three
separate witness controls are frozen as v=0, v=1 and v(b)=w(b+1),
each with its own partial domain. Their complete packet classifications
follow from their own nonnegative cyclic sum, matrix and branch laws.

There is no scientific code, numerical orbit run, finite modulus/prime
cutoff, precision parameter, parameter tuning, prime table or target-zero
data. Witness evaluation cost and physical IMAGE time are distinguished.
No finite check stands in for the all-state/all-period proof.

## Review provenance and handoff

The [internal review](independent-review.md) begins from the frozen card
before reading the paper, then compares the entire proof and challenges
the final scope. A separate [control contribution](source-controls.md)
comes from the original proposal author and is disclosed as author-side
work, not independent review. Native agents share model/context; neither
role establishes external peer review, formal verification or independent
error guarantees. ARS workflow and AI assistance are disclosed.

The [claim ledger](../claim-ledger.md) records the scoped T0/T1/T2 advance,
naturalness OPEN, full coarse topology OPEN, T3 NOT SUPPLIED / NOT
PURSUED, classical A0/A1/A2 NOT APPLICABLE, formal UNASSIGNED and
Route B NOT INVOKED. No analytic object is inferred from the prime ledger.

Only the new package and concise registry overviews are written. Old
packages and source mirrors stay unchanged; 241/242 paused; programme
active. No PDF, LaTeX, commit, upload or external publication occurs.

## Verification receipt — 2026-09-20

The root ran a read-only Python check over the seven package Markdown
files, plus the two newly added registry links in root readme.md and
papers/README.md. Result: **39 package-local links + 2 new registry
links resolved; 7 primary ID/status records matched; 4 hash locks
matched; 0 issues**. UTF-8 decoding, final newline, NUL/tab absence
and trailing-space lengths (zero or the Markdown hard-break pair)
were also checked on every package file.

The primary ID/status inputs were paper.md, candidate-card.md,
claim-ledger.md, package README.md, evidence/README.md and the two
registries. Exact expected values were ANG-20260920-APR01 and
OWNED ACTIVE-SOURCE PRIME PACKETS; NATURALNESS OPEN — SCOPED ADVANCE / FORK.
The hash locks were the original card prefix, unchanged manuscript,
completed review and original 287 proposal. The prefix was obtained
by byte-splitting the appended card at the first newline followed by
`## Appended audit outcome`; its hash equals the original freeze above.

Stable artifact receipts:

| Artifact | Lines | SHA-256 |
|---|---:|---|
| paper.md | 355 | b20fa7e047eabcb036e95b60a6a2255f60bb11419ef9d588df7c5d86d86c78b8 |
| candidate-card.md including appended outcome | 213 | cb48100913138d23d66b89e91c0502e5920337cc0c9969f31d33d9cf441fdc78 |
| evidence/independent-review.md | 144 | 42090ebdb50b19d187a044787259cbb615916f2f051763839793d9bb32b01611 |

The exact whitespace command, run from this workspace root, was:

```sh
git diff --check -- readme.md papers/README.md papers/288-active-pair-residue-flow
```

It exited zero with no output. Because untracked files are not covered
by that command, the separate Python content check explicitly included
every new package Markdown file. The source-proposal SHA-256 still
matches a397bd941d601dc70975dec53e6c45e408c8e5cb348d914076f91790c475f544.
Results were returned in the session and recorded here; no numerical
experiment output or generated verification script exists. These are
artifact-integrity checks, not a proof verifier. This receipt adds no
new link or mathematical claim; only the receipt's content/whitespace
and the changed Git diff need the final targeted recheck.
