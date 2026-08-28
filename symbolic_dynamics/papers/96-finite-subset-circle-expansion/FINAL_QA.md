# P96 final QA

QA date: 2026-08-28 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS.  External release: HOLD.**

The two-round hostile review remains the mathematical and scope gate.  This
final pass changed no theorem statement or proof; it replayed the exact
control and production build, checked the resulting PDF mechanically and
visually, and froze the requested evidence-bearing files.

## Exact-control gate

- Command: `python3 code/verify_finite_subset_circle.py`
- Exit status: 0
- Registered exact assertions: 7,000
- Individually enumerated literal subsets: 189,245
- Arithmetic layer: integer only; no random seed or floating-point theorem
  check
- Final line: `finite-subset circle exact control: PASS`
- Recorded output agrees with `CONTROL_RESULTS.md`.

## Build and log gate

- Toolchain: pdfLaTeX, BibTeX, pdfLaTeX, pdfLaTeX
- All four stages exited successfully.
- LaTeX errors: 0
- Undefined citations: 0
- Undefined references: 0
- Multiply defined labels: 0
- LaTeX/package warnings on the final pass: 0
- Overfull boxes: 0
- Underfull boxes: 0
- Rerun requests on the final pass: 0

## PDF gate

- Artifact: `main.pdf`
- SHA-256:
  `99e8dc79d7a2882afad5de08f8ab633e8bddb30b60d1d40848cbcefcec45f8a3`
- Pages: 8
- Geometry: A4, 595.276 by 841.89 points, rotation 0
- File size: 350,561 bytes
- PDF version: 1.5
- Encryption, JavaScript, forms, and suspect objects: absent
- Visible author: Anonymous; PDF Author metadata: empty
- Fonts: 23 listed subsets; 23/23 embedded, subsetted, and Unicode-mapped

## Text and visual gate

- `pdftotext -layout` extracted 28,476 bytes over 8 pages.
- No `??`, `[?]`, `[VERIFY]`, `TODO`, or `FIXME` sentinel was found.
- Title, theorem numbering, displayed formulas, cross-references, URLs, and
  bibliography text are extractable.
- All eight pages were rendered at 150 dpi and inspected individually.
- Page 1 title, abstract, opening theorem summary, and footer are unclipped.
- Theorems and displays on pages 2--6 remain inside the text block; no line,
  table, equation, or proof terminator is cut off.
- The scope boundary and references begin cleanly on page 7.  The final
  Tuffley reference continues on page 8; the remaining white space is benign.
- No overlap, missing glyph, broken URL, cropped footer, or malformed page
  transition was observed.

## Package and release boundary

`SHA256SUMS` covers exactly the requested manuscript source, bibliography,
control program, package documentation, hostile review, final QA, and PDF.
Its final `sha256sum -c SHA256SUMS` verification passes for every entry.

The bounded literature audit remains negative evidence rather than a priority
proof.  Public posting, submission, author contact, and absolute novelty or
priority language remain **HOLD** pending specialist review.
