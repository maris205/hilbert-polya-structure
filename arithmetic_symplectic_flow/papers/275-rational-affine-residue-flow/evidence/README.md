# Evidence and provenance — RAF01

**Candidate ID:** `ANG-20260919-RAF01`  
**Status:** `OWNED AFFINE INDEX; NO PRIMITIVE RETURN PACKETS — STOP / FORK`.

- [Frozen source and appended outcome](../candidate-card.md)
- [Complete proof](../paper.md)
- [Claim ledger](../claim-ledger.md)
- [Three bounded scout dispositions](scout-record.md)
- [Separate three-checkpoint review](independent-review.md)

## Exact method and limits

Inputs are the full inverse-limit ring X, normalized additive Haar
measure, algebraic localization B, every rational affine label with
positive multiplier, all admissible domains, and the frozen image-
clock/time/packet conventions. The proof derives integer torsion
cancellation, Q intersect X, full congruence domains, Borel image
scaling and all fixed states. It does not assume a topology on B or
import a different adelic quotient. Only X and the explicit domain
charts are used for the groupoid topology.

The return test uses every rational multiplier in each stabilizer,
not just q=p. The zero extension orbit is the precommitted topology
control, not a new orbit search. All null integer states stay in the
full source. No numerical run, approximation, modulus cutoff,
optimization or census was used. Naturalness OPEN; T3 NOT SUPPLIED /
NOT PURSUED. There is no operator or target-spectral claim.

## Bounded external-source check

The affine proof is self-contained. On 2026-09-19 root directly read
[Kim–Krieger–Postolache–Szeto, Hénon maps with many rational periodic points](https://arxiv.org/html/2412.01668v1),
Section 2.2, Lemma 3.8 and the start of Section 4, for the external
Hénon control only.
The HTML labels the source arXiv:2412.01668v1, 2024-12-02, while
its displayed manuscript date is 2026-08-24. Both observations are
retained; no publication-date or novelty inference is made from them.

This bounded HTML read supports no RAF01 theorem or new lineage.
No periods were computed, local PDF used, systematic review conducted
or user-read attestation implied.

## Frozen hashes and internal review

The initial card, before the appended outcome, has SHA-256

```text
c932e3e53c88bbf541c8f41e5734319b245bd6d0b2b2e27caf5d9f08d35b5602
```

The manuscript supplied for comparison has SHA-256

```text
235f8c4c297a471d60056a3e49e7321e99e29e8eacc12b366d6209d5921cd3e0
```

The reviewer derived the raw-card domain, clock and stabilizer results
before receiving the manuscript, then compared it and performed the
final adverse checkpoint. ARS freeze-first/three-checkpoint practice
shaped the work, not its authorization. Shared context/model lineage
is disclosed; internal model review is not external peer review,
formal verification or independent-error certification. Root owns
all integration files; the reviewer owns its separate report.

## Scoped document verification method

From arithmetic_symplectic_flow, check the preserved initial prefix:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/275-rational-affine-residue-flow')
prefix = (pkg / 'candidate-card.md').read_bytes().split(
    b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    'c932e3e53c88bbf541c8f41e5734319b245bd6d0b2b2e27caf5d9f08d35b5602')
```

Check all package Markdown targets and new 275 registry links; omit
external HTTP(S) and fragment-only links from filesystem checks.
Check the exact candidate ID and outcome status in card, paper,
ledger, package README, this index and both registries. Inspect new
files' whitespace directly because untracked files are not covered
by ordinary Git diff. Also run:

```bash
git diff --check -- readme.md papers/README.md papers/275-rational-affine-residue-flow
```

These are document/binding checks, not mathematical proof. Earlier
candidates, other streams, Phase-I materials, frozen Route mirrors
and paused 241/242 are unchanged. No stage, commit, deletion,
PDF/LaTeX, publication or external-model upload is performed.

## Recorded verification results — 2026-09-19

All three internal checkpoints completed with no required manuscript
change. Root read the entire 168-line report. Its final SHA-256 is
`e7a9cf7b42b3bec4c22254ce1a1ee129fab06264cac9201dc84ba57208650027`.
The report binds the initial card and unchanged manuscript above.
After the matching outcome append, the card hash became
`8bca9bdf3ea9fe611dae764bbb6f2f48ef638b496ce72c20d22bcea7fa07b666`;
its original byte prefix was verified unchanged. The review does not
claim to bind this later administrative card hash.

The scoped read-only checker returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 36
Exact candidate-ID/status checks: 7
Broken targets / identity / new-file hygiene issues: 0
Original card prefix and final manuscript/review bindings: PASS
```

The changed-path git diff --check exited 0 without output. This
receipt changes no mathematical input or link target; its own line
hygiene is checked after appending. Unchanged science and source
reads were not rerun for a receipt. Same-object ledger intact;
formal UNASSIGNED, Route B NOT INVOKED; 241/242 paused, goal active.
