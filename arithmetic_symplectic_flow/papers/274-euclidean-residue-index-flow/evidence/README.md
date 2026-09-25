# Evidence and provenance — ERI01

**Candidate ID:** `ANG-20260919-ERI01`  
**Status:** `OWNED RESIDUE CLOCK; ALL-INTEGER NULL-STRATUM PACKETS — STOP / FORK`.

- [Frozen source and appended outcome](../candidate-card.md)
- [Exact full proof](../paper.md)
- [Claim scopes](../claim-ledger.md)
- [Parallel scout dispositions](scout-record.md)
- [Raw-card / manuscript / adverse review](independent-review.md)

## Inputs and reproducible method

Inputs are every positive integer n, every residue j=0,...,n−1,
the marked gcd update, all infinite paths, all rooted cylinder masses,
and the frozen image-Jacobian/lag/time conventions. The all-zero
unit, prime, 4 and 6 paths were precommitted controls. The analysis
uses strict integer descent to classify paths, compatible finite
probabilities for measure, and prefix replacement for the full clock.
Equal shifted tails, not equal numerical periods, decide packet identity.

The path classification immediately supplies all terminal integers;
it was not obtained by expanding a cycle search after the composite
stop. Pure atomicity is proved together with the null complement,
not inferred from countability alone. The full-support continuous
Jacobian fixes null periodic values, while singleton ratios determine
the clock on the conull positive-atom stratum. Both strata are kept.

No numerical run, approximation, cutoff, optimization, period census
or empirical generalization was used. No T3 object, coarse-space
embedding theorem or ergodic-type classification is supplied. The
graph and uniform measure remain declared choices; naturalness OPEN.

## Bounded primary-source check

On 2026-09-19 root directly reopened the primary author manuscript
[Aidan Sims, Hausdorff étale groupoids and their C*-algebras](https://www.aidansims.com/papers/Sims2017.pdf),
the 2017-10-31 manuscript identified as arXiv:1710.10897v1, and
searched within it for Example 2.4.7. The bounded text read covered
the local-homeomorphism and graph-groupoid examples 2.4.6–2.4.7
and adjacent bisection definition. It checks standard vocabulary
only; the source uses the opposite graph source/range convention.
The paper proves its own outward-path prefix laws and gcd arithmetic.
No C*-algebra, trace or operator result is imported.

This was browser PDF text, not a locally extracted PDF or page-anchor
workflow. No systematic literature/novelty search or user-read mark
is claimed. Nearest repository comparisons are identified in the card
and scouting record; their old mathematical owners remain unchanged.

## Frozen versions and review procedure

The version-1 card, before its appended outcome, has SHA-256

```text
e0e694646b266857f6e3f4e72c93f7add69bd4e7cf0b6fe97cfb442a581d21b6
```

The manuscript supplied for separate comparison has SHA-256

```text
bc69cf70413c8e4a9114a71a56ca4b1b6b4a788b012d9d87498fcc8ba6385afc
```

An independent native invocation first read only the raw card and
derived the path, measure and return results before receiving the
paper. It then compared the manuscript and performed the final
adverse checkpoint. ARS freeze-first and three-checkpoint review
shaped this workflow; they grant no Route or publication permission.
Shared context/model lineage is disclosed: internal model review is
not external peer review, formal proof verification or independent-error
certification. Root owns integration; the reviewer owns its report.

## Scoped document verification

From arithmetic_symplectic_flow, check the frozen byte prefix:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/274-euclidean-residue-index-flow')
prefix = (pkg / 'candidate-card.md').read_bytes().split(
    b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    'e0e694646b266857f6e3f4e72c93f7add69bd4e7cf0b6fe97cfb442a581d21b6')
```

Check local Markdown targets in the package and new 274 links in both
registries, excluding HTTP(S) and fragment-only links from filesystem
checks. Compare exact ID/status in card, paper, ledger, package README,
this evidence index and both registries. Check new-file whitespace
directly, since ordinary Git diff omits untracked files. Also run:

```bash
git diff --check -- readme.md papers/README.md papers/274-euclidean-residue-index-flow
```

Document checks are not mathematical proof. No previous candidate,
Phase-I material, Route mirror, other stream or paused 241/242 package
is modified. No staging, commit, deletion, PDF/LaTeX generation,
publication or external-model transport occurs.

## Recorded verification results — 2026-09-19

All three internal review checkpoints completed with no blocking error
or required manuscript change; root read the entire 165-line report.
The final review SHA-256 is
`e8960d5c1f9bb9eea757994cf5ea079854fee5d462d029ee14600dfe401bdd24`.
It binds the unchanged manuscript and original card listed above.
After the matching administrative outcome was appended, the card
hash became
`38e99382778f68d62b802d75407d570159c1a9f57914a3c79453320c2e37e787`;
the original byte prefix was checked unchanged. The review is not
represented as binding the later appended card hash.

The scoped read-only checker returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 35
Exact candidate-ID/status checks: 7
Broken targets / identity / new-file hygiene issues: 0
Original card prefix and final manuscript/review bindings: PASS
```

The changed-path git diff --check exited 0 with no output. This
receipt adds no new mathematical input or link target; its own line
hygiene is checked after appending. Unchanged science and source reads
are not rerun for an administrative receipt. Same-object ledger intact;
formal UNASSIGNED, Route B NOT INVOKED; 241/242 paused and the
open-ended programme goal remains active.
