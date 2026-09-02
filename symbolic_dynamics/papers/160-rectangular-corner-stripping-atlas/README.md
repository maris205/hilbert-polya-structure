# P160 replacement — rectangular-corner stripping

**Status:** `ANONYMOUS ROUND-2 / INTERNAL ACCEPT / HOLD_EXTERNAL`

This four-page note treats the deterministic partition map that repeatedly
deletes the first `a` rows and first `b` columns and translates the southeast
remainder. Its residual claim package starts only at:

```text
fixed (a,b) literal crop through every time
+ arbitrary prescribed target
+ separate empty-target branch
+ exact support under every cap
+ ordered recovery from target probes.
```

Generalized/rational-slope Durfee rectangles, static two-boundary symbols or
decompositions, and the two-Pochhammer factorization receive zero contribution
credit. The bounded source search supports no novelty, priority, owner-absence,
or release claim.

## Review-A repairs

- M1: exact support now uses `gamma=(d), beta=empty` (`gamma=empty` at
  `d=0`), replacing the invalid arbitrary-unit-parts claim.
- M2: Gordon–Houten (1968), Andrews (1971), and Chen–Ji–Zang (2015) are
  directly verified, cited, and subtracted at the static rectangle/symbol/
  factorization level.
- P113 is included in the central collision firewall.

See `IMPROVEMENT_LOG.md` for the repair map. `HOSTILE_REVIEW_A.md` remains the
unchanged independent review.

## Review-B acceptance

Independent Review B returned `ACCEPT — 0 Critical / 0 Major / 0 Minor`.
Its independently written verifier performs 11,287,366 exact assertions; two
reviewer runs have SHA-256
`b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a`.
Review B required no mathematical, source, or reproducibility repair. The only
Round-2 source change is the batch-lifecycle consistency sentence
`This artifact remains HOLD_EXTERNAL`; it is not a Review-B finding.

## Exact controls

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p160.py
PYTHONDONTWRITEBYTECODE=1 python3 \
  ../../docs/papers157_161_sequence/reviews/p160_rcs_a/verify_p160_rcs_review_a.py
PYTHONDONTWRITEBYTECODE=1 python3 \
  ../../docs/papers157_161_sequence/reviews/p160_rcs_b/verify_p160_review_b.py
```

The author verifier (3,462,895 assertions) replayed twice; the independent
Review-A verifier (7,332,616 assertions) and Review-B verifier (11,287,366
assertions) were also replayed. Every run matched its frozen transcript byte
for byte.

## Build and frozen PDFs

The standard `pdflatex / bibtex / pdflatex / pdflatex` sequence settles with
zero real warning or bad box. Two builds from only `main.tex` and
`references.bib` matched `main.pdf` byte for byte.

- `main.pdf` and `main_round2.pdf`: 4 A4 pages, 316,629 bytes, SHA-256
  `ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352`.
- `main_round1.pdf`: preserved unchanged, 294,530 bytes, SHA-256
  `3bbbb6f3243171d612f86a17cd88b58f56bc5ec80c3533dc30464343931def03`.
- `main_round0_original.pdf`: preserved unchanged, 295,886 bytes, SHA-256
  `2be90261ae3b636aa8db684597896f7e7d549363879936b3f6539877577f7d08`.
- 23 font rows: all embedded, subsetted, and Unicode mapped; the additional
  row is the subsetted monospaced face used by the visible lifecycle token.
- Blank title/author/subject/keyword metadata; no encryption, forms, or JS.
- All four pages visually inspected at 144 dpi.

## Package map

- `main.tex`, `references.bib`: repaired anonymous manuscript and five cited
  verified records.
- `main.pdf`, `main_round0_original.pdf`, `main_round1.pdf`,
  `main_round2.pdf`: current canonical and the three immutable round freezes.
- `NARRATIVE_REPORT.md`, `PAPER_PLAN.md`, `PROOF_PACKAGE.md`,
  `CLAIMS_EVIDENCE.md`: synchronized result/proof/claim spine.
- `SOURCE_VERIFICATION.md`, `CONTROL_RESULTS.md`, `SELF_QA.md`, `BUILD.md`:
  source, verifier, visual/anonymity, and reproducibility records.

The existing `SHA256SUMS` is retained as a Round-0 record and intentionally
not regenerated into a final manifest in this author freeze; `FINAL_QA.md`
is likewise reserved for the batch final-QA pass.
Posting, submission, circulation, and other external actions remain on hold.
