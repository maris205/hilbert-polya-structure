# Evidence and verification — SCF01

**Screen ID:** `ASFS-SCOUT-20260920-SCF01`  
**Status:** `NO MAIN ADMISSION; PRIME-SOURCE INTERFACES OPEN — STOP / FORK`.

- [Frozen scope](../candidate-card.md)
- [Full bounded comparison](../paper.md)
- [Claim ledger](../claim-ledger.md)
- [Scouting and collision-search limits](scout-record.md)
- [Three-checkpoint internal review](independent-review.md)

## Inputs and evidence method

Inputs are the two exact definition/source lanes in the card, the
named prior-work interface, selected old candidate definitions and
one primary article. Root compared supplied fields against admission
requirements. No theorem proof, scientific computation, cutoff,
precision setting, orbit table or generated dataset belongs here.
Source facts, unknown proposal fields and admission decisions have
different labels in the paper and ledger.

Primary identity: Pierre Arnoux and Sébastien Labbé, *On some symmetric
multidimensional continued fraction algorithms*,
[arXiv:1508.07814v3](https://arxiv.org/pdf/1508.07814v3), 2016-10-11.
Root directly read section 2 Remark 1; section 3 Definitions 6–8
and Remarks 9–10; section 6 definitions, Lemma 25 and Proposition 26.
Browser text extraction retained these locators. Searches for the
lemma via the browser find function returned no match; direct opening
of the later source passage resolved retrieval. A failed text search
was not treated as missing evidence. This is not a systematic review,
human-read attestation or local-PDF page-anchor verification.

The primary-derived factual summary is in paper section 3; the rest
of that section is explicitly root's project-admission inference.
The reviewer independently checked the same bounded primary passages,
not merely the scout's paraphrase. No unsupported all-state source
completion or projective no-go was added.

## Frozen bindings and staged review

Original version-1 card SHA-256:

```text
0fc191670f0ed909fb137a7ec943c26af9d78dfeed14bfe2ebc012a0d8f5e513
```

Full 175-line manuscript SHA-256:

```text
7ae71454d8a8e25f5c132db4403efe0af0730cd9a8a98a58ff9fae1fcb4fb436
```

The native reviewer completed the raw-card checkpoint before reading
the paper, preserving the strongest fair counterargument to each
proposed rejection. Checkpoints 2/3 compare the evidence and complete
manuscript, then test interpretation and handoff. Actual verdicts and
scope are in its exclusive report. Root owns the companion records.

ARS supplies the staged evidence discipline, not a main-candidate
pass. Shared model/context, nonblind later comparison and AI assistance
are explicit; no external peer review, formal verification or
independent-error certificate is claimed.

## Document verification method

After appending the outcome, preserve the card's original byte prefix:

```python
from pathlib import Path
import hashlib
pkg = Path('papers/281-source-clock-admission-frontier')
prefix = (pkg / 'candidate-card.md').read_bytes().split(
    b'\n## Appended admission outcome', 1)[0]
assert hashlib.sha256(prefix).hexdigest() == (
    '0fc191670f0ed909fb137a7ec943c26af9d78dfeed14bfe2ebc012a0d8f5e513')
```

Read-only checks cover package local links and new 281 registry links,
local heading anchors, seven ID/status locations, manuscript/review
bindings, UTF-8, final newlines, NUL/tabs and unintended trailing space.
New untracked files are checked directly because Git diff omits them.
The task-scoped Git command is:

```bash
git diff --check -- readme.md papers/README.md papers/281-source-clock-admission-frontier
```

These checks establish document integrity, not scientific correctness.
No stage, commit, deletion, external model transport, PDF/LaTeX or
publication action is taken. The programme goal remains active;
241/242 paused, formal coordinates UNASSIGNED and B NOT INVOKED.

## Recorded verification results — 2026-09-20

All three internal checkpoints completed without a correction request.
Root read the full 134-line final report, SHA-256
`4cd0bbe37ec66fb0c4f56db3477ec19ac68b4673c1c5ddd125e19d07533e9b1d`.
Its PASS is for this record's evidence scope, not main admission or
a new mathematical theorem. The report explicitly states its own
primary reading and excludes independent certification of historical
collision-search coverage. Shared-model limitations remain explicit.

The 175-line paper retains its bound hash above. The full appended
card SHA-256 is
`51f90151a4693bcf437a4b1ea1f58a17720fdf3f512228ef07605f5c4a8e3e99`;
the original byte prefix was verified unchanged.

The scoped read-only checker returned:

```text
Package Markdown files: 7
Local links checked, including new registry links: 42
Exact screen-ID/status checks: 7
Broken targets / anchors / identity / new-file hygiene issues: 0
Original card prefix and final manuscript/review/card bindings: PASS
```

The task-scoped git diff --check exited 0 with no output. This
receipt adds no scientific input or new local link; its line hygiene
is checked after appending. Unchanged source passages are not reread
and no unperformed mathematics is represented as verified. Portfolio
STOP / FORK, no main admission, no formal coordinate, B NOT INVOKED;
same-object comparison intact, prior packages preserved, 241/242
paused and the full programme goal remains active.
