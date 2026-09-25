# Evidence and provenance — PDI01

**Candidate ID:** `ANG-20260919-PDI01`  
**Status:** `REVERSIBLE ARITHMETIC SOURCE; EXACT-COBOUNDARY CLOCK — STOP / FORK`.

- [Frozen definitions and appended outcome](../candidate-card.md)
- [Exact proof record](../paper.md)
- [Claim scopes](../claim-ledger.md)
- [Three-lane admission dispositions](scout-record.md)
- [Separate raw-card / manuscript / adverse review](independent-review.md)

## Exact method and limits

Inputs are all positive integer pairs, power-divisibility parity,
coordinate exchange, atomic mass 1/(ab), every iterate arrow and the
card's image-Jacobian/time-return conventions. Integer cancellation
proves reversibility and the all-integer three-cycle family. Singleton
measure identities determine every pointwise Jacobian. The global
coordinate change v=u−log(ab) classifies all physical returns without
enumerating all base cycles. No finite census, modulus cutoff, period
bound, numerical precision, experiment or parameter tuning was used.

The general control has explicit finite-positive atom and partial-
bijection hypotheses. It is not a classification of non-atomic clocks,
noninvertible correspondences or independently defined algebraic index
cocycles. Full base periodic classification remains OPEN; no such
classification is needed to prove zero clock on every actual return.

## Bounded primary-source check

On 2026-09-19 the root used these two public queries:

    Maharam extension coboundary cocycle nonsingular transformation lecture notes author
    "Ergodic Theory: Nonsingular Transformations" Danilenko Silva arxiv

The author-hosted PDF at web.williams.edu/Mathematics/csilva/
NonsingularET_Apr.pdf was not accessible through the browser. That
failure was retained; a search snippet was not substituted for a read.
The primary author manuscript was then read at
[arXiv:0803.2424v3](https://arxiv.org/pdf/0803.2424v3), dated 2022-07-28,
by Alexandre I. Danilenko and Cesar E. Silva.

The bounded read covered the defining derivative convention in Section
2.1 and the logarithmic extension commuting with translation in Section
5.2. This checks standard terminology and sign ancestry only. No
non-atomic ergodic-type theorem, associated-flow classification or
operator result is applied to our countable atomic object. The proof
in the paper independently fixes the image convention on singletons.

The PDF was read through browser text; no local PDF or locally extracted
page anchor was used. This is not a systematic literature or novelty
search. No claim is made that the user personally read this source.
Other search hits were not imported into the proof record.

## Frozen inputs and separate review

The initial card, before its appended outcome, has SHA-256

```text
088e64e21d89034ba04e8e647d287520a7eff724bb2629bcf287f32ee05017fd
```

The manuscript supplied for the bounded comparison has SHA-256

```text
8f0a8d4843fe983a93441fde41db2c304435fc0def89957c98856333b9a81bc5
```

A separate native worker read the raw card and sent independent
derivations before receiving the manuscript. It then compared the
actual paper and performed the final adverse checkpoint. Its owned
review binds the final version. Shared conversation context and model
lineage preclude calling this external peer review, formal proof
verification or evidence of independent errors. Root owns all other
package files and integration.

## Document verification method

From arithmetic_symplectic_flow, verify the frozen byte prefix:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/272-power-divisibility-index-clock')
prefix = (pkg / 'candidate-card.md').read_bytes().split(
    b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    '088e64e21d89034ba04e8e647d287520a7eff724bb2629bcf287f32ee05017fd')
```

Check all local Markdown targets in this package plus new 272 links in
the two registries, excluding external HTTP(S) and fragment-only links
from filesystem checks. Compare exact ID/status across the card, paper,
ledger, package README, this index and both registries. Inspect new-file
line hygiene directly because ordinary Git diff omits untracked files.
Use this additional scoped whitespace check:

```bash
git diff --check -- readme.md papers/README.md papers/272-power-divisibility-index-clock
```

The QA is document consistency, not mathematical proof. Old cards,
other streams, Phase-I materials, frozen Route mirrors and paused
241/242 remain unchanged. No staging, commit, deletion, PDF generation,
publication, scientific run or external-model upload occurred.

## Recorded verification results — 2026-09-19

The reviewer completed all three checkpoints with no required
manuscript change, and root read the complete report. Its final hash is
`bed85813387a37c978519f3daa609450a6bf1fdb870d0d50ecfbeea151b32baf`.
The report binds the original card and unchanged manuscript hashes
listed above. After root appended the matching outcome, the card hash
became `c93a06b516818753aa4074635d732da7953fc4e044a514db56050ab2e431e1a9`;
the initial byte prefix was checked unchanged. The review does not
claim to bind this later administrative card hash.

The scoped read-only document checker returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 36
Exact candidate-ID/status checks: 7
Broken targets / identity / new-file hygiene issues: 0
Original card prefix and final manuscript/review bindings: PASS
```

The changed-path git diff --check exited 0 with no output. This receipt
adds no mathematical input or link target; its own line hygiene is
checked after appending. No unchanged science, source lookup or proof
was rerun for another administrative receipt.
