# Evidence and provenance — UIR01

**Candidate ID:** `ANG-20260919-UIR01`  
**Status:** `OWNED LOG-PRIME RETURNS; CONTINUUM PACKET MULTIPLICITY — STOP / FORK`.

- [Frozen definitions and appended outcome](../candidate-card.md)
- [Full mathematical record](../paper.md)
- [Claim scopes](../claim-ledger.md)
- [Bounded scout dispositions](scout-record.md)
- [Separate raw-card and manuscript review](independent-review.md)

## Method and evidence boundary

Exact inputs are the full inverse-limit ring X, its entire multiplicative
unit group U, all rational partial arrows, additive Haar probability,
its quotient pushforward, and the card's full packet convention.
The method is direct proof: Chinese remainder coordinates, exact unit
orbits, residue-cylinder measure uniqueness, saturated Borel preimages,
valuation return equations, and finite-modification orbit equivalence.
There is no modulus cutoff, period bound, numerical precision setting,
parameter scan or scientific executable. The continuum multiplicity
is proved by an explicit binary-sequence injection into tail classes,
not inferred from a large finite orbit table.

The source interface preserves all finite-divisibility predicates but
not original residue phase/order/chronology. Naturalness is OPEN. The
measure-null return strata, nontrivial base isotropy, trivial extension
isotropy and coarse non-T1 topology are all retained and distinguished.
An abstract cyclic time orbit is not promoted to a Hausdorff embedded
circle. No ordinary Euler product, trace or T3 operator was pursued.

## Bounded primary-source check

On 2026-09-19 the scout and root separately checked the public HTML of
[Connes and Consani, Knots, Primes and the adele class space, arXiv:2401.08401v1](https://arxiv.org/html/2401.08401v1).
The selected scope is Sections 1–2: the compact-unit quotient, canonical
C_p and the definition of its representative set F. Other finite
components of F are units; the source then takes rational saturation.
This identifies the canonical scope without claiming it exhausts the
full-tail owner of the present card. No theorem from that paper's trace,
étale, semilocal or C*-algebra discussions is a proof input here.

This was a bounded known-owner source check, not a systematic literature
review, novelty search or operator-import campaign. The main agent
opened and read the relevant HTML directly; no local PDF was downloaded,
extracted, generated or used for page evidence. Local 005/024/146/270
were read only for the particular identity/multiplicity collision.
Their cards and results were not revised by this paper.

## Frozen-input and review identities

The version-1 card, before the appended result section, has SHA-256

```text
52c8ffe25a607dc99fea2b5fcd4391256c008584a08a8de8cd560bb1dfe1fa34
```

The initial manuscript supplied for comparison has SHA-256

```text
3cae9e8a9a05e41f2d62947732ae1f621561b5afd877e64f96b4d7dc36d6f9f3
```

A separate native worker first read the raw card and independently
derived the full quotient, measure law, return groups and tail
multiplicity before receiving the root manuscript. Its owned review
file records three checkpoints and binds the actual reviewed version.
Shared context and same-family model review do not establish independent
errors, external peer review or mathematical certification. Root owns
the paper and integration, not the independent-review file.

## Document verification method

From arithmetic_symplectic_flow, verify the original card byte prefix:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/271-unit-quotient-return-multiplicity')
prefix = (pkg / 'candidate-card.md').read_bytes().split(
    b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    '52c8ffe25a607dc99fea2b5fcd4391256c008584a08a8de8cd560bb1dfe1fa34')
```

Check local Markdown targets in the package and new 271 links in both
registries, excluding external HTTP(S) and fragment-only targets from
filesystem checks. Check the exact candidate ID and status in the card,
paper, claim ledger, package README, this index and both registries.
Check all new files directly for line hygiene because ordinary Git
diff does not cover untracked files. The scoped Git command is:

```bash
git diff --check -- readme.md papers/README.md papers/271-unit-quotient-return-multiplicity
```

These checks establish document consistency only. No older proof,
Phase-I source, frozen Route mirror, numeric artifact or paused 241/242
package was edited. No staging, commit, deletion, publication or
external-model transport occurred.

## Recorded verification results — 2026-09-19

The separate review completed all three checkpoints with no required
manuscript change. Root read the complete final report. The paper hash
above remained unchanged; the current card hash is
`33222fff843780aa12abeee291a594f6be2ea853f161b9831a342fd9e9924e7c`,
and its original byte prefix matches the frozen input hash above.
The final review hash is
`bf972732854da9f95212662c1e7c84f2eb484fae88bd70f36abf085ba06d43df`.
Both final manuscript/card bindings were checked against that report.

The scoped read-only document checker returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 34
Exact candidate-ID/status checks: 7
Broken targets / identity / new-file hygiene issues: 0
Initial card prefix and final review bindings: PASS
```

The changed-path git diff --check exited 0 with no output. This appended
receipt changes no mathematical input, link target or reviewed artifact;
its own line hygiene is checked after appending. No unchanged scientific
proof or source lookup is repeated to obtain an additional receipt.
