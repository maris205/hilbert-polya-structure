# P99 final QA

QA date: 2026-08-29 UTC

## Verdict

**Internal Stage 2 package: mechanical PASS.  External release: HOLD.**

The two-round hostile review, including a separate read-only Round 2, is the
mathematical, scope, and ownership gate.  This final pass replayed the exact
control and production build, checked the resulting PDF mechanically and
visually, and froze the requested evidence-bearing files.  No external
submission or priority claim is authorized.

## Exact-control gate

- Command: `python3 code/verify_shear_sublattices.py`
- Exit status: 0
- Registered exact assertions: 93,912
- Canonical HNF states inspected: 11,973 over `1<=N<=120`
- Fixed-time cases: 14,520; Möbius cases: 7,260
- Prime-power pairs: 40; valuation/unit cases: 680
- Arithmetic layer: Python integers only; no random seed, floating-point
  tolerance, numerical spectrum, or computer-algebra oracle
- Fresh output is byte-identical to `code/verification_output.txt` and agrees
  with `CONTROL_RESULTS.md`.

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
  `311d64d0d6b8d8236e6b6b8e193a10869e66cad705ad8cc1ed14d29c77424c01`
- Pages: 4
- Geometry: A4, 595.276 by 841.89 points, rotation 0
- File size: 284,865 bytes
- PDF version: 1.5
- Encryption, JavaScript, forms, and suspect objects: absent
- Visible author: Anonymous; PDF Author metadata: empty
- Fonts: 22 listed subsets; 22/22 embedded, subsetted, and Unicode-mapped

## Text and visual gate

- `pdftotext -layout` extracted 14,922 bytes over four pages.
- No `??`, `[?]`, `[VERIFY]`, `TODO`, `FIXME`, `placeholder`, ChatGPT, or
  AI-generated sentinel was found.
- Title, theorem numbering, all displayed formulas, cross-references, DOI
  strings, and bibliography text are extractable.
- All four pages were rendered at 150 dpi and inspected individually.
- Page 1 has an unclipped title, abstract, owner boundary, and complete
  Proposition 2.1 statement; its footer and internal date are clear.
- Pages 2 and 3 contain the census, example table, prime-power theorem, and
  start of recovery without collision, clipping, or malformed equations.
- Page 4 cleanly completes recovery, controls, limitations, conclusion, and
  all three references.
- No overlap, missing glyph, broken link text, cropped footer, malformed page
  transition, or poor table fit was observed.

## Package and release boundary

`SHA256SUMS` covers the manuscript source, bibliography, exact program,
stored control output, package documentation, hostile review, final QA, and
PDF.  Its final `sha256sum -c SHA256SUMS` replay passes for every entry.

The bounded literature audit remains negative evidence rather than a
novelty or priority proof.  Public posting, submission, author contact, and
absolute novelty or priority language remain **HOLD** pending specialist
review.
