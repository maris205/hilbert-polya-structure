# Evidence and reproducibility — SYM01

**Screen ID:** `ASFS-SCOUT-20260919-SYM01`  
**Status:** `SYMMETRY-ONLY CLOCK UNIQUENESS REFUTED; NO NEW OWNER — STOP / FORK`.

- [Frozen comparison contract](../candidate-card.md)
- [Exact incidence and clock proof](../paper.md)
- [Claim ledger](../claim-ledger.md)
- [Parallel scouts and source passage check](scout-record.md)
- [Three-checkpoint internal review](independent-review.md)

## Exact inputs and method

The graph, U and W edge weights, root masses and all path/groupoid
conventions are frozen explicitly in the card. Directed incidence
automorphisms are allowed to permute numeric labels and parallel edge
identities; no labels are fixed by hypothesis. The proof uses unique
outgoing hub degrees, the incoming/outgoing degrees of targets, and
the self-loop at H_2. No automorphism-group enumeration is needed.

Rooted probability families are covariant under the induced path action;
the global coproduct measures are invariant. Prefix cylinder products
prove invariance and each owner's image-clock preservation. The
unchanged complete graph ledger is cited from 276, with all transient,
parallel, scan and null paths retained. One p=3 cycle distinguishes
the clocks, but the period comparison is proved for every prime.
This is exact reasoning, not extrapolation from that discriminator.

No numerical input, cutoff, precision, fitting, new weight family,
prime table or zero data is used. The comparison does not adjoin
automorphism arrows, take a new quotient, modify 276 or supply T3.

## Source and readback scope

Root read the exact nearest old cards linked in the scout record.
One primary author-source PDF was checked via browser text at
Proposition 6.1 and Theorem 4.1; the exact citation and limits are
recorded there. This is not a systematic literature or novelty search,
local PDF page-anchor workflow, user-read attestation or a newly
proved geometric result. The symmetry proof itself is elementary
and self-contained apart from the identified same-graph ledger.

## Frozen versions and review

Original version-1 screen card SHA-256:

```text
4ab5c913594ae82e731c40151cb77b3f3756db5a73fee91630a03d8a550a052d
```

Comparison manuscript SHA-256:

```text
c15456f3dde5dfe0fe2ad5e246157fcb002e7056784211cec8f54cc7e1c080cd
```

The native reviewer receives the card before the paper, derives the
symmetry/measure result separately, then compares the manuscript and
performs a final adverse check. The linked report records actual
checkpoint completion and document bindings. Root owns integration;
the reviewer owns that report. ARS determines the freeze-first and
three-checkpoint process, not a mathematical or Route verdict.
Shared model/context lineage is disclosed: internal model review is
not external peer review, formal verification or independent-error
certification. AI assistance was used in research and writing.

## Scoped verification method

After appending the administrative outcome, preserve the original
card prefix through this read-only check:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/277-symmetry-clock-admission-screen')
prefix = (pkg / 'candidate-card.md').read_bytes().split(
    b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    '4ab5c913594ae82e731c40151cb77b3f3756db5a73fee91630a03d8a550a052d')
```

Check local Markdown targets in this package and new 277 registry
links, excluding HTTP(S) and fragment-only references from filesystem
tests. Check the exact screen ID/status in card, paper, ledger,
package README, evidence README and both registries. Validate the
manuscript/review hashes and new-file whitespace directly; ordinary
Git diff omits untracked files. Run:

```bash
git diff --check -- readme.md papers/README.md papers/277-symmetry-clock-admission-screen
```

These checks are document checks, not proofs. All prior candidate
packages, including 276 and paused 241/242, remain unchanged. No
staging, commit, deletion, source/mirror edit, PDF/LaTeX artifact,
publication or external-model transport is part of this screen.

## Recorded verification results — 2026-09-19

All three internal review checkpoints completed without a required
mathematical revision. Root read the full 158-line final report,
whose SHA-256 is
`3e0424f3fc0ec1456c2b1bc1c0323c6f52a4ef92f7a8baca752a489df560df71`.
Its stated review scope excludes independent checking of the other
three scout lanes. The original card prefix and comparison manuscript
remain bound to the hashes above. After the outcome append, the full
card hash is
`d00f9b636c5b62b0ba514183ba7d5f7e472e7bbb7f562221dbb94ddeff93bc82`;
the version-1 input prefix was verified unchanged.

The scoped read-only checker returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 37
Exact screen-ID/status checks: 7
Broken targets / identity / new-file hygiene issues: 0
Original card prefix and final manuscript/review bindings: PASS
```

The changed-path git diff --check exited 0 with no output. This
administrative receipt introduces no scientific input or new link
target; its own line hygiene is checked after appending, without
rerunning unchanged mathematics or source reads. Same-object
comparison intact; no new owner or gate coordinate, formal UNASSIGNED,
B NOT INVOKED; 241/242 paused and programme goal active.
