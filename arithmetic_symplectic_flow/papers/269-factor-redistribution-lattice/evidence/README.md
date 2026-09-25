# Evidence and reproducibility — FRL01

**Candidate ID:** `ANG-20260919-FRL01`  
**Status:** `FULL REVERSIBLE OWNER; ALL-INTEGER TRANSPORT PACKETS — STOP / FORK`.

## Inputs and ownership

- [Version-1 candidate card and appended outcome](../candidate-card.md)
- [Full mathematical record](../paper.md)
- [Claim ledger](../claim-ledger.md)
- [Definition-level scouting and admission decisions](scout-record.md)
- [Independent bounded review](independent-review.md)

The proof uses only the card's displayed divisor-permutation definitions,
finite-support arithmetic and the explicit orbit decomposition of a
discrete bijection. Earlier packages are architecture comparisons, not
theorem inputs. No external source-expansion campaign, numerical orbit
census, target data, parameter fitting or scientific background process
was used. The five control rows are exact hand calculations; the infinite
claims have proofs separate from those examples.

The source scout supplied the first three control rows after freeze.
The separate reviewer started with the raw card and no root draft,
derived the same decisive family independently, and supplied the general
odd-composite control before manuscript comparison. Root checked it and
integrated it. The final review binds the final manuscript, not every
navigation file. All work is AI-assisted same-family model work, not
external peer review or a correctness certificate.

## Frozen byte identities

The original definition card, before its appended outcome, had SHA-256

```text
f0b72da9f95047d19a2d851a934d4ec601285e729cfc0c00f08420e5eb994d08
```

The final paper supplied for bounded review has SHA-256

```text
599ccc57cd88c1db86e33cb245b67272dae6bfb0e6aed8e4a82d629217502dfb
```

The review led to one clarity correction: the unchanged swap-control
rows are explicitly the first two table rows, at even site 0, not the
odd singleton rows. The disclosure also explicitly identifies the
reviewer's contribution to the odd-composite contrast. No mathematical
definition or claimed result changed in these editorial corrections.

## Reproducible document checks

From the arithmetic_symplectic_flow directory, the preservation check is:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/269-factor-redistribution-lattice')
card = (pkg / 'candidate-card.md').read_bytes()
prefix = card.split(b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    'f0b72da9f95047d19a2d851a934d4ec601285e729cfc0c00f08420e5eb994d08')
assert hashlib.sha256((pkg / 'paper.md').read_bytes()).hexdigest() == (
    '599ccc57cd88c1db86e33cb245b67272dae6bfb0e6aed8e4a82d629217502dfb')
print('PASS: original card prefix and final paper hash')
```

Local Markdown target checks cover every Markdown file in this package,
plus the newly added 269 links in the two registries. External HTTP(S)
and fragment-only links are excluded from filesystem checks. Exact ID
and current status are checked in the card, paper, claim ledger, package
README, this evidence index and both registries. Whitespace is checked
directly for these new files because an ordinary Git diff does not
include untracked files. The changed-path command is:

```bash
git diff --check -- readme.md papers/README.md papers/269-factor-redistribution-lattice
```

These checks establish document consistency only, not proof validity or
global periodic completeness. No old paper, Route mirror, Phase-I source,
numerical artifact or paused 241/242 package is changed by this work.
No staging, commit, deletion, upload, PDF or publication is performed.
The programme goal remains active independently of this candidate stop.

## Recorded verification results — 2026-09-19

The frozen-prefix and final-paper hash check passed. The final reviewer
file has SHA-256
`0ed7f1414fae6d8d2d93e66d62ae37a5b75e1e387ff770f7bc93f31ef73cae22`;
its binding to the final paper digest above was checked. All three
bounded review checkpoints are complete, with the sole clarity item
resolved and no outstanding mathematical revision request.

The final scoped document check returned:

```text
Package Markdown files: 7
Local links checked, including the new registry links: 33
Broken local targets: 0
Exact candidate-ID/status checks: 7
New-file line-hygiene issues: 0
Final review hash and manuscript binding: PASS
```

The displayed changed-path git diff --check exited 0 with no output.
This appended receipt changes no mathematical input or link; its own
line hygiene is checked after appending. No unchanged proof or scientific
calculation is rerun merely for the receipt.
