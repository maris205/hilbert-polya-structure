# P114 final QA

QA date: 2026-08-29 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS. External release: HOLD.**

Two independent nonauthor reviews reconstructed the theorem tree.  The final
repairs define every empty and small-`n` boundary, separate the determinant
and local-fibre edge cases, and subtract the direct parallel-`RAKE`, pruning,
height-enumeration, and all-minors owners.  No unresolved critical or
mathematical major defect remains.

## Exact-control gate

- command: `PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py`;
- exit status: 0; fresh stdout matches the stored transcript byte for byte;
- exact assertions: **400,105**;
- exhaustive parent-map dynamics for every subset of `[n]` through `n=6`,
  including all 26,830 states in the largest lane;
- exact rational EGF coefficients, every endpoint/depth cell, every target
  fibre, fixed states, deepest states, and the basin partition;
- 8 transcript lines and 422 bytes; no sampling or floating-point fitting.

## Build and bibliography gate

- sequence: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX; all stages exited 0;
- a deterministic extra pdfLaTeX pass reproduced the PDF SHA-256;
- LaTeX/package warnings, undefined citations/references, multiply-defined
  labels, overfull/underfull boxes, errors, and actionable rerun requests: 0;
- bibliography: 11 local entries, all 11 cited and resolved, with 0 missing or
  uncited entries.

## PDF gate

- artifact: `main.pdf`;
- SHA-256: `43a5fb7ca92581326e0f7844e5717ebb510f983039b089acdbe8d588ff396d8c`;
- 3 A4 pages; 318,137 bytes; PDF 1.5; rotation 0;
- encryption, JavaScript, forms, metadata stream, and embedded files: absent;
- visible author: Anonymous; PDF Author metadata: empty; deterministic date
  metadata: absent;
- fonts: 24/24 embedded, subsetted, and Unicode-mapped;
- searchable layout text: 16,441 bytes, 213 lines; sentinel scan: clean.

## Visual gate and release boundary

All three final pages were freshly rendered at 150 dpi and inspected.  The
abstract, the theorem continuation across pages 1--2, boundary conventions,
all-minors orientation sentence, determinant and EGF arguments, local-fibre
display, owner firewall, and eleven references are legible and uncropped.
There is no overlap, malformed display, unintended blank page, broken
citation, missing glyph, or stray source token.

`SHA256SUMS` covers the final evidence package and verifies entry by entry.
The bounded owner audit is not a novelty or priority clearance.  External
posting, submission, specialist contact, venue choice, and any novelty or
priority statement remain **HOLD**.
