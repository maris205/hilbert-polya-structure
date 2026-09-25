# Evidence and provenance — PIR01

**Candidate ID:** `ANG-20260919-PIR01`  
**Status:** `OWNED HAAR INDEX; NO PRIMITIVE RETURN PACKETS — STOP / FORK`.

- [Frozen definitions and appended outcome](../candidate-card.md)
- [Exact mathematical record](../paper.md)
- [Claim scopes](../claim-ledger.md)
- [Bounded scout dispositions](scout-record.md)
- [Independent raw-card and manuscript review](independent-review.md)

## Method and scientific evidence boundary

All return statements are exact for every profinite state. The proof
uses integer-multiplication injectivity, the clopen residue cylinders,
Borel measure uniqueness on their generating algebra, rational partial
actions and the displayed return equation. No finite modulus cutoff,
period census, floating-point evaluation, parameter search or numerical
approximation supplies the complete classification.

The groupoid arrow and object topologies, fixed-object isotropy, time
stabilizers and coarse quotient topology are checked separately. No
operator or equilibrium-state result is imported as a point-orbit claim.
There is no new geometric owner after the first-gate failure.

## Bounded primary-source identity check

Date: 2026-09-19. One public search query was used:

    Bost Connes groupoid positive rationals action profinite integers partial action Haar measure Laca Raeburn

The main source read was
[Sergey Neshveyev, arXiv:math/0002141v1](https://arxiv.org/pdf/math/0002141),
the opening finite-adele definitions, rational multiplication and time
character, with the measure-scaling convention immediately following.
This identifies standard ancestry and the image/pushforward sign
distinction. No ergodicity or KMS theorem is a proof input here.

The second source was the author abstract of
[Marcelo Laca, arXiv:math/9911135](https://arxiv.org/abs/math/9911135),
used only to confirm the existing rational-action dilation background.
It was not a full-paper read or a theorem application. Neither source
is claimed as human-read, a new construction by this project, or proof
of a natural sieve-to-geodesic correspondence.

The first source was read through the browser's PDF text; no local PDF
was created or used for page-anchor evidence. The source record does
not rely on a locally extracted PDF or an unperformed structural check.
The packet proof in the paper is self-contained under its frozen
definitions. This bounded lookup is not a systematic literature review.

## Frozen-input identities

The version-1 card, before its appended outcome, has SHA-256

```text
d721774b7af8546f52fe5d87b5178efb9281e282dc4653ab78ca7de86faba488
```

The manuscript initially supplied for final bounded comparison has SHA-256

```text
6619e9ff0d68eab5b6407d639531b7dd787dc818ffdd26b6cef07a181cd3ef64
```

A separate native worker first read the raw card, independently derived
the owner, index and full return classification, and only then read the
root manuscript. The final review binds its actual manuscript version.
Same-family model review and shared project context do not establish
independent errors, external peer review or mathematical certification.
Root owns navigation and administrative QA, not the reviewer's file.

## Document verification method

From arithmetic_symplectic_flow, preserve the original card by checking
the byte prefix before the appended result:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/270-profinite-index-return')
raw = (pkg / 'candidate-card.md').read_bytes()
prefix = raw.split(b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    'd721774b7af8546f52fe5d87b5178efb9281e282dc4653ab78ca7de86faba488')
print('PASS: original card prefix preserved')
```

Check every local Markdown target in this package and the new 270 links
in the two registries, excluding external HTTP(S) and fragment-only
targets from filesystem validation. Check the exact ID and status in
paper, card, ledger, package README, this index and both registries.
Directly check new-file whitespace, since ordinary Git diff does not
cover untracked files. The changed-path command is:

```bash
git diff --check -- readme.md papers/README.md papers/270-profinite-index-return
```

These checks establish document consistency only. No older paper,
Phase-I material, frozen Route mirror, numerical artifact or paused
241/242 package was edited. No staging, commit, deletion, publication,
PDF generation or external-model transport was performed.

## Recorded verification results — 2026-09-19

The original card prefix and unchanged manuscript hash above both passed
their byte-identity checks. The independent review completed all three
checkpoints with no requested manuscript revision. Its final SHA-256 is
`27c1911c5000f92bbd1f84a9eed50286429bcfd1b26593d0e2ad57bcc42dbd52`;
the file and its binding to the displayed final paper hash were checked.

The final scoped document check returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 33
Broken local targets: 0
Exact candidate-ID/status checks: 7
New-file line-hygiene issues: 0
Final review hash and manuscript binding: PASS
```

The changed-path git diff --check exited 0 with no output. This receipt
adds no link or mathematical input; its own line hygiene is checked
after appending. No unchanged proof or source lookup is repeated merely
to obtain another receipt.
