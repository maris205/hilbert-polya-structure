# P97 final QA

QA date: 2026-08-29 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS.  External release: HOLD.**

The two-round hostile review remains the mathematical and scope gate.  This
final pass changed no theorem or proof after the production replay; it reran
the exact control, completed the required four-stage build, audited the
resulting PDF mechanically and visually, and froze the requested
evidence-bearing files.

## Exact-control gate

- Command: `python3 code/verify_sumset_squaring.py`
- Exit status: 0
- Registered exact assertions: 91,509
- Literally enumerated nonempty states: 10,403
- Literally enumerated ordered sumset pairs: 17,139
- Registered arithmetic-progression layers: 266
- Arithmetic layer: exact integer and finite-set operations only; no random
  seed, floating-point theorem comparison, CAS, or optimization solver
- Final line: `sumset-squaring exact control: PASS`
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
- Bibliography audit: five cited keys, five resolved entries, zero missing or
  uncited entries

## PDF gate

- Artifact: `main.pdf`
- SHA-256:
  `4f1647b3f8e95b2ea7b60025bcbc40d0079f19c79391d2a1c8de27aa0b642952`
- Pages: 5
- Geometry: A4, 595.276 by 841.89 points, rotation 0
- File size: 351,013 bytes
- PDF version: 1.5
- Encryption, JavaScript, forms, and suspect objects: absent
- Visible author: Anonymous; PDF Author metadata: empty
- Fonts: 26 listed subsets; 26/26 embedded, subsetted, and Unicode-mapped

## Text and visual gate

- `pdftotext -layout` extracted 17,883 bytes over five pages.
- No `??`, `[?]`, `[VERIFY]`, `TODO`, `FIXME`, `PLACEHOLDER`, or
  `DRAFTNOTE` sentinel was found.
- Title, theorem numbering, all displayed formulas, cross-references, DOI
  strings, code path, and bibliography text are extractable.
- All five pages were rendered at 150 dpi and inspected individually.
- Page 1 title, abstract, principal formulas, introduction, and footer are
  unclipped.
- The complete six-part theorem, boxed layer-depth formula, and owner boundary
  on pages 2--3 remain inside the text block with no overlap or missing glyph.
- The proof displays and example table on page 4 are aligned and uncropped.
- The endpoint ledger and all five references on page 5 are complete; the
  remaining lower-page white space is benign.
- No malformed page transition, broken link text, cropped proof terminator,
  or font substitution was observed.

## Package and release boundary

`SHA256SUMS` covers exactly the requested manuscript source, bibliography,
control program, package documentation, hostile review, final QA, and PDF.
Its final `sha256sum -c SHA256SUMS` verification passes for every entry.

The bounded literature audit remains negative evidence rather than a priority
proof.  Public posting, submission, venue choice, author contact, and absolute
novelty or priority language remain **HOLD** pending specialist review.
