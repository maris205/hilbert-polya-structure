# Final batch QA — P147–P151

**Date:** 2026-09-01 UTC.  **Result:** `PASS / GO_INTERNAL`.  **External
status:** `HOLD_EXTERNAL`.

## Terminal gate summary

| gate | accepted result |
|---|---|
| frozen contracts | 5/5 proved within the final owner-subtracted ceilings |
| hostile reviews | A: 1 Critical / 3 Major / 12 Minor; B: 0 / 1 / 2; all findings closed |
| discovery replay | 7/7 transcripts byte-identical; 33,456,994 assertions |
| paper replay | 5/5 transcripts byte-identical; 7,726,518 assertions |
| isolated paper builds | 10/10 successful; two per paper; canonical-PDF byte identity |
| visual inspection | 24/24 pages accepted after final repairs |
| references | 32/32 bibliography entries cited and resolved |
| fonts | 137/137 reported rows embedded, subsetted, and Unicode mapped |
| paper manifests | 106/106 entries pass |
| canonical PDF manifest | 5/5 entries pass |
| unresolved review severity | 0 Critical / 0 Major / 0 Minor |

Exact enumeration is counterexample pressure, never the proof of an
all-parameter theorem or an ownership certificate.

## Canonical PDF ledger

| paper | pages | bytes | references | font rows | visual pages | SHA-256 |
|---:|---:|---:|---:|---:|---:|---|
| P147 | 4 | 338,052 | 6 | 24 | 4/4 | `1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20` |
| P148 | 5 | 357,397 | 5 | 28 | 5/5 | `5c681793e5e97abb0ad718f876a2e0af11bd2d41585d860dc0c5b8c3992ed957` |
| P149 | 4 | 374,480 | 9 | 31 | 4/4 | `7a9e801bfecc08000db82ea37ff9b1e206e4e3ec0ca211c46481db1f401bbacb` |
| P150 | 5 | 403,358 | 5 | 29 | 5/5 | `26d0a73adb71b2e303ea637b5874939914cffd53f09a2230ded5775484c33dca` |
| P151 | 6 | 356,664 | 7 | 25 | 6/6 | `24fddbfb896510cf2712a8ade2a3ac37d04712676f635e39f1170c4cc334e8d9` |
| **total** | **24** | **1,829,951** | **32** | **137** | **24/24** | — |

All five PDFs are A4, rotation zero, unencrypted, form-free,
JavaScript-free, and attachment-free.  Identifying title, author, subject,
and keyword metadata are blank.  No clipping, overlap, blank page, corrupt
glyph, unresolved marker, illegible reference, or anonymity leak was found.
The accepted text layer contains 12,028 words and 95,175 bytes.

For every paper, `main.pdf` and `main_round2.pdf` are byte-identical.  Round-0,
Round-1, and Round-2 files are preserved as 15 read-only (`0444`) artifacts;
the distinct historical hashes remain in each paper's `BUILD.md` and
`SHA256SUMS`.

## Frozen exact-replay ledger

### Discovery lanes

| lane | assertions | cold replay |
|---|---:|---|
| algebraic | 929,002 | byte-identical / pass |
| algebraic replacement | 1,048,472 | byte-identical / pass |
| combinatorial | 20,638,365 | byte-identical / pass |
| combinatorial replacement | 3,464,224 | byte-identical / pass |
| root | 3,416,699 | byte-identical / pass |
| root replacement | 2,690,869 | byte-identical / pass |
| stochastic | 1,269,363 | byte-identical / pass |
| **total** | **33,456,994** | **7/7** |

These lanes examined 55 distinct new literal dynamical systems plus one
historical re-entry control.  Killed candidates remain in the permanent
collision and owner ledgers rather than being silently recycled.

### Paper lanes

| paper | assertions | frozen terminal marker | cold replay |
|---:|---:|---|---|
| P147 | 2,690,869 | `PASS` | byte-identical |
| P148 | 216,905 | `P148_THEOREM_INTERFACES_PASS` | byte-identical |
| P149 | 1,228,181 | `P149_THEOREM_INTERFACES_PASS` | byte-identical |
| P150 | 2,144,131 | `STATUS=PASS` | byte-identical |
| P151 | 1,446,432 | `PASS` | byte-identical |
| **total** | **7,726,518** | — | **5/5** |

The verifiers use deterministic exact arithmetic over their declared finite
boxes.  No sampling, floating-point inference, runtime web access, or
third-party proof oracle is used.

## Build replay

Each paper was copied into two fresh directories containing only `main.tex`
and `references.bib`, then rebuilt with the package's declared deterministic
`pdflatex -> bibtex -> pdflatex -> pdflatex` sequence.  All ten processes
returned zero and the two replicas for every paper matched each other and the
canonical package PDF byte for byte.  Settled logs contain no unresolved
citation/reference, rerun request, bad box, multiply defined label, or BibTeX
warning.

## Integrity manifests

The paper-local manifests intentionally exclude themselves.  Their final
entry counts and manifest-file digests are:

| paper | entries | manifest SHA-256 |
|---:|---:|---|
| P147 | 21 | `fe082e985c661e8a660195be211b42cc6f1ab56e35186c5fdbc460885b3d9533` |
| P148 | 22 | `e026abdb009672022a6f1fb9575bc4663bc227579d58f7b2b690aa0932f3613b` |
| P149 | 22 | `e7865d5d8aeee75ba82b5ad6b787babc0ddbfb86abbbf7275857a296c3ad9e52` |
| P150 | 20 | `18431641bf6960da6e998b141ac683cd5d00799f31a577e43a086e46c132d16f` |
| P151 | 21 | `93d106e3165789d6d2b9cc9000306e06d02717f1f44a3e0c54ea553936a210bd` |

These are the final manifest digests.  The controlling package-freeze replay
passes all 106/106 listed artifacts.

The canonical five-PDF manifest has SHA-256
`6ec8027961c47b6d6a6e8814ff362c3a49a1037ba7a74950139022e75a3a1089`
and passes 5/5 from its own directory.

## Owner and release boundary

P148's direct unordered contraction owner, P149's corrected static
two-zero-convention owner, and P151's generic time/place and tree-PGF owners
are fully subtracted in the final contracts.  P147 and P150 remain
owner-thin.  Source non-hits are described only as bounded non-hits.

This report certifies internal proof/artifact consistency.  It does not
certify novelty, priority, authorship, ownership completeness,
freedom-to-operate, public-release safety, or venue suitability.  No public
posting, circulation, specialist contact, submission, or other external
action is authorized.  Status remains `HOLD_EXTERNAL`.
