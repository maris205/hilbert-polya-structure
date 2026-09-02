# Author self-QA — P160 RCS Round 2

**Result:** `ANONYMOUS ROUND-2 / INTERNAL ACCEPT / HOLD_EXTERNAL`  
**Date:** 2026-09-02 UTC

## Mathematical repairs

- [x] M1: every excess `d>0` uses `gamma=(d), beta=empty`; at `d=0` both
  are empty. The witness has one part and respects `length(gamma)<=h`.
- [x] The invalid `gamma=(1^d)` construction is identified and not used.
- [x] Empty and nonempty targets remain separate; `t=0` and `N=0` are explicit.
- [x] Rectangle witness, all-time crop, fibre bijection, cap support,
  conjugation, and ordered recovery were re-read end to end.

## Source and claim repairs

- [x] Gordon–Houten 1968 DOI metadata directly verified and cited.
- [x] Andrews 1971 DOI/volume/issue/pages directly verified and cited.
- [x] Chen–Ji–Zang 2015 DOI/arXiv/volume/pages and Section 3 definition-level
  content directly verified and cited.
- [x] Generalized/rational-slope rectangles, static two-boundary symbols and
  decompositions, and two-Pochhammer factorization are explicit zero credit.
- [x] Residual starts only at fixed-`(a,b)` all-time literal crop + arbitrary
  prescribed target + separate empty branch + exact cap support + ordered
  recovery.
- [x] P113 collision separation is in the central firewall.
- [x] No novelty, firstness, priority, or owner-absence claim appears.

## Executable gate

- [x] Author verifier: two fresh byte-matching replays; 3,462,895 assertions.
- [x] Independent Review-A verifier: two fresh byte-matching replays;
  7,332,616 assertions; author code not imported.
- [x] Author, Review-A, and Review-B frozen transcripts end in `PASS`.
- [x] Review B returned `ACCEPT — 0 Critical / 0 Major / 0 Minor`.
- [x] Review-B verifier replay: 11,287,366 assertions, output SHA-256
  `b6034231aa620d0de80a56bfcda69f8ddfe047e343498896426699252b918b8a`.

## Build, font, anonymity, and visual gate

- [x] Anonymous four-page A4 `amsart`; blank identifying metadata.
- [x] Settled log: zero real warnings, errors, rerun requests, undefined
  citations/references, overfull boxes, or underfull boxes.
- [x] Two source-only cold builds are byte-identical to `main.pdf`.
- [x] All 23 font rows are embedded, subsetted, and Unicode mapped.
- [x] All four 144-dpi pages inspected; no clipping, overlap, broken glyph,
  table collision, or illegible formula/reference.
- [x] `main_round2.pdf` equals `main.pdf` byte for byte.
- [x] `main_round1.pdf` retains its Round-1 hash and size.
- [x] `main_round0_original.pdf` retains its original hash and size.

## Frozen Round-2 artifact

`main_round2.pdf`: 4 A4 pages, 316,629 bytes, SHA-256
`ce59fbfca3f50ee917089175817885fc5630b807483b7a16a5d291c69292e352`.

The visible `HOLD_EXTERNAL` sentence is a batch-lifecycle consistency change,
not a Review-B finding or mathematical repair. No `FINAL_QA.md` or final
`SHA256SUMS` was generated. External actions remain on hold.
