# Evidence and provenance — FBI01

**Candidate ID:** `ANG-20260919-FBI01`  
**Status:** `OWNED NON-ATOMIC PRIME CLOCK; MIXED PRIMITIVE COLLISIONS — STOP / FORK`.

- [Frozen definitions and appended outcome](../candidate-card.md)
- [Full same-object proof](../paper.md)
- [Claim ledger](../claim-ledger.md)
- [Bounded scout dispositions](scout-record.md)
- [Raw-card, manuscript and adverse review](independent-review.md)

## Exact inputs, method and limits

Inputs are the full positive-integer-pair graph, every marked branch
0<=j<gpf(x+y), all rooted infinite paths, and the uniform cylinder
measure. The card fixes prefix arrows from beta-tail to alpha-tail,
the negative log IMAGE Jacobian, the full real extension, and packet
equivalence by actual arrows plus time. No unlisted source states,
paths, marks, lag labels or transient prefixes are suppressed.

Proof uses finite-branching inverse limits, compatible finite measures,
prefix-replacement bisections, Borel measure uniqueness and subgroups
of Z. The least-period degree product gives the entire return-group
rule without enumerating all cycles. Self-loop checks quantify over
all primes, composites and the unit. The two exact finite mixed words
were in the card before their checks: marks 3,1 at (2,3),(3,2), and
four j=0 edges through (7,3),(3,5),(5,2),(2,7).

No scientific program, numerical approximation, optimization, cutoff,
period census or empirical completeness argument was used. The
remaining graph cycles and the coarse topology are not classified.
T3 was not pursued after the mixed-primitive stop. Exact image time
does not establish naturalness of the graph or uniform branch law.

## Bounded primary-source check

On 2026-09-19 root used the public query:

    graph groupoid infinite path prefix replacement bisections locally compact Hausdorff Deaconu Renault local homeomorphism

The primary author-hosted manuscript was read at
[Aidan Sims, Hausdorff étale groupoids and their C*-algebras](https://www.aidansims.com/papers/Sims2017.pdf),
dated 2017-10-31, with arXiv:1710.10897v1 in its source header.
The bounded read covered Examples 2.4.6–2.4.7 and the adjacent étale
definition, checking local-homeomorphism and graph-groupoid vocabulary.
The source uses the opposite graph source/range naming convention.
The paper therefore proves its own outward-path prefix laws explicitly.
No onto-shift assumption, analytic operator theorem or C*-trace is
imported. All arithmetic and image-clock conclusions are proved for
the frozen graph rather than attributed to this reference.

This was browser PDF text, with no local PDF extraction or page-anchor
workflow. Other search hits were not used. It is not a systematic
literature/novelty search, and no user reading is asserted.

## Frozen hashes and review ownership

The initial card, before the appended outcome, has SHA-256

```text
afd7787de56c4fa3e0fb298266aef3d6fcc038ec85eb46776a29705b4f03775c
```

The supplied manuscript has SHA-256

```text
4ca2c45d45f5addecb4905406cf6d81a268d06ee6d65e55a7347a1eceac5419c
```

A separate native worker derived the source, clock and fixed controls
from the raw card before receiving the paper. It then compared the
manuscript and performed the final adverse checkpoint. Its owned
report binds the exact versions reviewed. Shared context/model lineage
is not external peer review, formal verification or a guarantee of
independent errors. Root owns the other files and integration. The
ARS freeze-first and three-checkpoint procedure shaped this workflow;
it did not authorize a Route evaluation or publication.

## Scoped document verification method

From arithmetic_symplectic_flow, check the frozen prefix:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/273-factor-branching-index-flow')
prefix = (pkg / 'candidate-card.md').read_bytes().split(
    b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    'afd7787de56c4fa3e0fb298266aef3d6fcc038ec85eb46776a29705b4f03775c')
```

Check all package local Markdown targets plus the new 273 links in
the two registries; external HTTP(S) and fragment-only links are not
filesystem targets. Compare exact candidate ID and outcome status
in card, paper, ledger, package README, this evidence index and both
registries. Inspect new-file line hygiene directly because untracked
files are not covered by ordinary Git diff. Also run:

```bash
git diff --check -- readme.md papers/README.md papers/273-factor-branching-index-flow
```

These checks verify documents and bindings, not the mathematical
theorems. No previous card, other stream, Phase-I source, Route mirror,
paused 241/242 package, LaTeX/PDF or publication artifact is edited.
No staging, commit, deletion or external-model upload is performed.

## Recorded verification results — 2026-09-19

The separate reviewer completed all three checkpoints with no blocking
error or required manuscript change. Root read the complete 170-line
report. Its final SHA-256 is
`e27ff704f1630f6aef1552c520106c7677740dd0c027d04264789d8397c97da0`.
The review binds the original card and unchanged manuscript hashes
above. The later appended-outcome card has SHA-256
`11263422c5b4475f2d3723c607616f887a2173bca0a5234c4b719d9b48d06796`;
the initial byte prefix was verified unchanged. The review is not
represented as binding this later administrative append.

The scoped read-only document checker returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 35
Exact candidate-ID/status checks: 7
Broken targets / identity / new-file hygiene issues: 0
Original card prefix and final manuscript/review bindings: PASS
```

The changed-path git diff --check exited 0 with no output. This
receipt adds no mathematical input or link target; its own line
hygiene is checked after appending. Unchanged proofs and source
lookups were not rerun for an administrative receipt. Same-object
ledger intact; formal UNASSIGNED, Route B NOT INVOKED. 241/242 remain
paused and the open-ended programme goal remains active.
