# P104 final QA

QA date: 2026-08-29 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS. External release: HOLD.**

Both nonauthor hostile reviews independently reconstructed the composition
orientation, singular spectrum, folded CLT, endpoints, Perron root, and
strict gap.  Neither found a theorem or source defect requiring repair.

## Exact-control gate

- command: `python3 code/verify_monomial_toggle.py`;
- exit status: 0; stored stdout: byte-for-byte match;
- exact assertions: **741,486**;
- literal normal-form words: 122,865; signed-transform words: 61,425;
- additional lanes: occupation distributions and moments, tilted transfers,
  Cayley--Hamilton recurrences, CLT variance algebra, and both endpoints;
- all quantities use exact `Fraction` arithmetic, with no randomness or
  floating-point theorem comparison.

## Build and bibliography gate

- sequence: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX; all stages exited 0;
- LaTeX/package warnings, undefined citations/references, multiply-defined
  labels, overfull/underfull boxes, errors, and rerun requests: **0**;
- bibliography: 3 cited keys, 3 resolved entries, 0 missing, 0 uncited.

## PDF gate

- artifact: `main.pdf`;
- SHA-256: `194185a2d754b1d3c5f2d958a8f2282612670ea159c56f9767331b78be14c71a`;
- 5 A4 pages; 307,296 bytes; PDF 1.5; rotation 0;
- encryption, JavaScript, and forms: absent;
- visible author: Anonymous; PDF Author metadata: empty;
- fonts: 23/23 embedded, subsetted, and Unicode-mapped;
- searchable layout text: 17,326 bytes; sentinel scan: clean.

## Visual gate and release boundary

All five pages were rendered and inspected.  The generator convention,
normal form, singular values, CLT normalization, endpoint cases, annealed
root, strict-gap proof, collision firewall, and references are legible and
within the text block.  No clipping, overlap, malformed formula, unintended
blank page, or orphaned heading was found.

`SHA256SUMS` covers the full final evidence package and verifies entry by
entry.  General random-product, generalized-Lyapunov, and martingale-CLT
machinery remains owner-subtracted; the exact-atom direct-owner gate is not
closed.  External circulation, submission, contact, and priority language
remain **HOLD**.
