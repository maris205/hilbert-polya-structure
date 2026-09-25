# Evidence and reproducibility — SGC01

**Candidate ID:** `ANG-20260920-SGC01`  
**Status:** `OWNED ARITHMETIC CARRY CLOCK; EXTRA PRIME-TWO PACKET — STOP / FORK`.

- [Frozen card](../candidate-card.md)
- [Full mathematical record](../paper.md)
- [Claim ledger](../claim-ledger.md)
- [Architecture admission and two non-admitted lanes](scout-record.md)
- [Three-checkpoint internal review](independent-review.md)

## Inputs, method and scientific outputs

All inputs are the three frozen residue branches, every modulus n>=2,
the full profinite integer seed, normalized rootwise additive Haar,
the complete retained-lag T-tail relation, and the real extension
derived from its Borel IMAGE clock. No prime table, Riemann-zero
data, von Mangoldt weight, selected seed or fitted parameter enters.

The exact proof method is compatible residue division, Borel Haar
scaling, inverse affine branch composition on restricted clopen
domains, modulus descent, the equation (n^r−1)x=b and an elementary
integer successor/carry descent. The smallest discriminator is the
actual fixed point (2,1) versus the actual cycle (2,2)<->(2,3).
One carry in each gives equal least time, not the same primitive.
The full classification is proved, not inferred from this example.

SOURCE-OFF and PREDICATE are separate exact controls with all states
retained. Noninteger periodic-itinerary fibres, negative/zero seeds,
restricted GCD images and nonclosed extension orbits are additional
ownership controls. The manuscript's outputs are mathematical
arguments; no orbit census, scientific numerical script, cutoff,
precision setting or generated numerical artifact was used.

## Primary source and prior-work scope

The bounded primary-source browser check read
[Sims, Examples 2.3.7 and 2.4.6](https://www.aidansims.com/papers/Sims2017.pdf)
on local-homeomorphism groupoids and their topology. This supports
terminology only; the actual branch domains, Haar derivatives and
periodic ledger are proved for SGC01. No graph-only carrier or
analytic theorem is imported. This is not a systematic literature
review, novelty certification, local PDF page-anchor workflow or
human-read attestation.

The exact nearest candidate definitions and their nontransfer
boundaries appear in the scout record. The original prior-work
guide and every old candidate package remain unchanged.

## Frozen versions and review order

Original version-1 card SHA-256:

```text
440e90ebb6f3c4e3531b24d8a241df8184f6687f0db2d81ebf94b633affefcc7
```

Full 357-line manuscript SHA-256:

```text
0749940501fb24daadadab2ab01350f7ff591b796918d964a2821a98d002c816
```

The native reviewer receives the raw card before the manuscript,
derives the all-state owner and controls, then compares the whole
paper and conducts a final adverse check. The raw review separately
identified the root-2 extra packet before seeing the manuscript.
Root owns integration and companions; the reviewer owns its report.
Actual checkpoint completion and final bindings are recorded there
and in the verification receipt below.

ARS supplied the freeze-first, three-checkpoint discipline. The
critical extra packet causes the target stop; it is not repaired
or concealed to obtain a favorable review. AI assistance and shared
model/context lineage remain explicit. Internal review is not external
peer review, formal verification or independent-error certification.
The mathematical reviewer does not certify the other scout lanes.

## Scoped document verification method

Preserve the original card bytes when appending an administrative
outcome, using this read-only check:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/279-successor-gcd-carry-flow')
prefix = (pkg / 'candidate-card.md').read_bytes().split(
    b'\n## Appended audit outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    '440e90ebb6f3c4e3531b24d8a241df8184f6687f0db2d81ebf94b633affefcc7')
```

Check local links in the package and new 279 registry links, excluding
HTTP(S) and fragment-only references from filesystem tests. Check
the exact ID/status in card, paper, ledger, package README, evidence
README and both registries. Bind paper and review hashes. Inspect
new files directly for UTF-8, final newline, NUL/tabs and unintended
trailing spaces, since Git diff alone omits untracked files. Run:

```bash
git diff --check -- readme.md papers/README.md papers/279-successor-gcd-carry-flow
```

These checks do not prove mathematics. No staged files, commit,
deletion, old-source modification, PDF/LaTeX, publication or external
model transport belongs to this audit. Same-object ledger intact;
T3 NOT SUPPLIED / NOT PURSUED, classical A0/A1/A2 NOT APPLICABLE,
formal UNASSIGNED and B NOT INVOKED. 241/242 paused; goal active.

## Recorded verification results — 2026-09-20

All three internal review checkpoints completed with no mathematical
correction requested. Root read the entire 222-line final report,
whose SHA-256 is
`9a27d9bf52341a8c8c9827f4112e4866ebdbc87c3ed70a2646b5ba7fe589d128`.
The review passes the accuracy of this failure record, NOT the
candidate's prime-single-packet target. Shared-model/context limits
and exclusion of the other scout lanes are explicit in the report.

The complete 357-line manuscript retains its bound hash above. The
appended full card SHA-256 is
`477346a2e670a568ce526e53fdd708fcbe4ee32fa7a148b409722b22b76cce88`;
the original version-1 byte prefix was verified unchanged.

The scoped read-only checker returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 52
Exact candidate-ID/status checks: 7
Broken targets / identity / new-file hygiene issues: 0
Original card prefix and final manuscript/review bindings: PASS
```

The changed-path git diff --check exited 0 with no output. This
administrative receipt adds no scientific input or new link target;
its own line hygiene is checked after appending without rerunning
unchanged mathematics or source reads. Same-object ledger intact;
STOP / FORK, naturalness OPEN, T3 not pursued, formal UNASSIGNED,
B NOT INVOKED. 278 is preserved, 241/242 remain paused and the
programme goal remains active.
