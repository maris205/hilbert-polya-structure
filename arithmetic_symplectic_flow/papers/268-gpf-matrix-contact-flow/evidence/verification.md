# Joint document verification — RGM01 and GMC01

Date: 2026-09-19. Candidates: `ANG-20260919-RGM01` and
`ANG-20260919-GMC01`. This is document/reproducibility QA, not a proof
certificate or a formal Route evaluation.

## Frozen-input preservation

Each outcome was appended after the initial card. The complete byte prefix
before `## Appended audit outcome` must match its pre-proof SHA-256:

| Card | Pre-proof SHA-256 |
| --- | --- |
| 267 reversible GPF memory | 3d4edcb97cac189ca6effcf378c2bdd6c845e550ea589e4ab2fc6deaad44f838 |
| 268 GPF matrix contact flow | 17d94ef5bb3121ed83668e913e0c95fdb35340081df4e95525f0315d2b1c3971 |

The final mathematical paper inputs supplied for review are:

| Paper | SHA-256 |
| --- | --- |
| 267 | 3e0fe94fad1fd35ec0fc997f5fae02d73b494e9a96c72493bb41e35cf78b30ec |
| 268 | 0c186e27af45fe9e5b3ead45bf951057c05f4ddfe704313b27e677eac990721c |

The 267 review first derived its fixed-state stop from the card. The 268
review first derived its full quotient/contact/return audit from the card.
Both were then compared with the respective manuscripts. The author of 268
also requested a narrower internal topology check; this does not replace
the independent raw-card review. All checks are same-family model work,
not external peer review or proof of independent error processes.

## Reproducible preservation check

Run from arithmetic_symplectic_flow:

```python
from pathlib import Path
import hashlib
spec = {
    '267-reversible-gpf-memory': (
        '3d4edcb97cac189ca6effcf378c2bdd6c845e550ea589e4ab2fc6deaad44f838',
        '3e0fe94fad1fd35ec0fc997f5fae02d73b494e9a96c72493bb41e35cf78b30ec'),
    '268-gpf-matrix-contact-flow': (
        '17d94ef5bb3121ed83668e913e0c95fdb35340081df4e95525f0315d2b1c3971',
        '0c186e27af45fe9e5b3ead45bf951057c05f4ddfe704313b27e677eac990721c'),
}
for slug, (card_sha, paper_sha) in spec.items():
    pkg = Path('papers') / slug
    raw = (pkg / 'candidate-card.md').read_bytes()
    old = raw.split(b'\n## Appended audit outcome', 1)[0]
    assert hashlib.sha256(old).hexdigest() == card_sha, slug
    assert hashlib.sha256((pkg / 'paper.md').read_bytes()).hexdigest() == paper_sha, slug
print('PASS: both frozen prefixes and both final paper hashes')
```

## Scope of remaining checks

Check local Markdown targets in both packages and the new 267/268 links in
the two registries; exclude external HTTP(S) and fragment-only links from
filesystem checks. Verify each candidate's exact ID/status in its paper,
card, claim ledger, package README, root README and paper registry.
Check new-file whitespace directly as well as changed-path `git diff --check`,
since untracked files are not covered by a normal Git diff.

No repeated 266 science or document audit is required: its inputs were only
read here. No frozen numerical files, Phase-I materials, Route mirrors or
paused 241/242 objects were changed. No staging, commit, push or deletion
was performed. Old registry entries remain historical; new summaries do
not transfer claims between the two new owners.

## Mathematical verification boundary

RGM01 needs no scientific run. GMC01 uses exact proof arithmetic for one
known mixed word and elementary asymptotics; the reviewer reports its
single exact symbolic command and output in
[independent-review.md](independent-review.md). That check is not an orbit
census or an empirical convergence test. The full ledger depends on the
identified 266 source theorem and the proved full return equation.

No trace, zeta or operator was added to GMC01 after its packet/clock stop.
The broader programme remains active; completed documents and internal
reviews do not establish the requested natural arithmetic/symplectic goal.

## Recorded results

The frozen-prefix and final-paper check above passed for both candidates.
After the GMC01 reviewer completed its final manuscript readback, the
scoped document check returned:

```text
Markdown files in the two new packages: 13
Local links checked, including new registry links: 65
Broken local targets: 0
Exact candidate-ID/status checks: 12
New-file line-hygiene issues: 0
GMC01 independent review checkpoints: 3 COMPLETE
GMC01 final manuscript hash binding: PASS
GMC01 final review file hash: PASS
```

The final GMC01 review file SHA-256 is
`0213bc9d41d9c393956123627faf99337e348cc0fdd7fc6b8131b14290cb1131`.
Its checkpoints bind the final paper hash above; they do not enlarge the
mathematical or Route claims. No paper input changed after this readback.

The changed-path whitespace command was:

```bash
git diff --check -- readme.md papers/README.md papers/267-reversible-gpf-memory papers/268-gpf-matrix-contact-flow
```

It exited 0 with no output. This receipt adds no new link or mathematical
input. Its own line hygiene is checked after the append; unchanged proofs
and the reviewer's exact symbolic calculation are not rerun.
