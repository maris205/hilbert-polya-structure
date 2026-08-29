# P105 final QA

QA date: 2026-08-29 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS after evidence-language repair.
External release: HOLD.**

Two nonauthor reviews independently reconstructed the full iterate, layer
census, and one-step fibre bijection.  Review B corrected the meaning of the
trajectory-step counter without changing any theorem or assertion.

## Exact-control gate

- command: `python3 code/verify_cycle_minimum_pruning.py`;
- exit status: 0; stored stdout: byte-for-byte match;
- exact assertions: **17,219,241**;
- literal permutations and fibre-formula output states: 409,113 each;
- nontrivial trajectory-step evaluations: 1,981,326, with repeated edge
  traversal across starting states explicitly allowed;
- restricted-cycle recurrence through `n=50`; Möbius/zeta through period 60;
- arithmetic: finite permutations, integers, and exact rationals only.

## Build and bibliography gate

- sequence: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX; all stages exited 0;
- LaTeX/package warnings, undefined citations/references, multiply-defined
  labels, overfull/underfull boxes, errors, and rerun requests: **0**;
- bibliography: 5 cited keys, 5 resolved entries, 0 missing, 0 uncited.

## PDF gate

- artifact: `main.pdf`;
- SHA-256: `f4a6f777cda71f702edb979e0d9ddb33ba9f77646d1cbbdbe02e50c3905bd85f`;
- 5 A4 pages; 331,334 bytes; PDF 1.5; rotation 0;
- encryption, JavaScript, and forms: absent;
- visible author: Anonymous; PDF Author metadata: empty;
- fonts: 24/24 embedded, subsetted, and Unicode-mapped;
- searchable layout text: 17,919 bytes; sentinel scan: clean.

## Visual gate and release boundary

All five pages were rendered and inspected.  The surgery definition, iterate
normal form, depth/zeta statements, EGF and recurrence, depth table, boxed
fibre formula, repaired trajectory-counter wording, and references are
complete and uncropped.  No collision, malformed glyph, blank-error page, or
broken page transition was found.

`SHA256SUMS` covers and verifies the final evidence package.  Classical
cycle enumeration and longest-cycle theory remain owner-subtracted, and the
exact surgery owner search remains bounded.  Posting, submission, contact,
venue choice, and priority language remain **HOLD**.
