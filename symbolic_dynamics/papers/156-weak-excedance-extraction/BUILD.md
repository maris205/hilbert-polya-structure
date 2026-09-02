# Build and QA record — P156

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Settled author build

- Engine: pdfTeX 1.40.22 / LaTeX2e; BibTeX 0.99d.
- Sequence: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- `main.pdf`: 4 A4 pages, 336,311 bytes.
- `main_round2.pdf`: byte-identical to `main.pdf`, SHA-256
  `7e222ce483cc755d4bb732f14ecf94d92ea13c505eba91212150308bebcc7979`.
- `main_round1.pdf` preserves the Review-A repair freeze at the same SHA-256;
  Review B required no mathematical, source, verifier, transcript, build, or
  PDF change.
- `main_round0_original.pdf` remains unchanged at SHA-256
  `ee5cedd089d9d837839f9fc715aae9530e19fc4f414dfcbef77ad0adfafa256c`.
- Bibliography: 8/8 primary-source entries cited and resolved.
- Settled logs: zero unresolved citation/reference, rerun request, build
  error, BibTeX warning, overfull box, underfull box, or multiply defined
  label.
- Fonts: all 27 reported font rows are embedded, subsetted, and
  Unicode-enabled.
- PDF: version 1.5, A4, unencrypted, zero embedded files, no detected
  JavaScript/AcroForm marker, and blank identifying title/author/subject/
  keyword metadata.  Volatile dates and trailer IDs are suppressed.
- Visual QA: all 4/4 pages rasterized at 120 dpi and inspected; no clipping,
  overlap, broken formula, unresolved marker, bad glyph, or illegible
  reference was found.

## Reproducibility

Two fresh temporary directories containing only `main.tex` and
`references.bib` were built with the four-stage sequence.  Both isolated PDFs
were 4 pages, 336,311 bytes, and byte-identical to `main.pdf` at the SHA-256
above.

## Exact control

- Literal states through rank nine: 409,113.
- Image target/rank cells: 99,451.
- Constructive section cells: 1,704.
- Every-target fibre cells: 6,985.
- Explicit `n<m` fibre-boundary cells: 316,646.
- Explicit `n=m` fibre-boundary cells: 46,233.
- Canonical tower targets: 46,225, six levels each.
- Assertions: 3,689,489; `status=PASS`.
- Fresh stdout is byte-identical to `verification_output.txt`.
- Transcript SHA-256:
  `5c78864527c5781da43f79f8b2b667f9d915fd13fadaea09abe6a7c49f76f53e`.

The transcript separately records the false pointwise clock counterexample,
the absent global maximum-clock claim, and the absent global multi-step
minimality claim.  Enumeration remains counterexample pressure, not proof.

## Review boundary

Hostile Review A returned 0 Critical / 0 Major / 2 Minor; both were closed in
Round 1.  Hostile Review B returned 0 Critical / 0 Major / 1 Minor: the
Round-1 PDF had 27 conforming font rows while two author ledgers retained the
Round-0 count of 26.  The ledger count is corrected in Round 2 and mapped in
`IMPROVEMENT_LOG.md`; all review findings are closed.  P156 is internally
accepted under `HOLD_EXTERNAL`.  Scoped repository synchronization is governed
by the standing batch authorization; posting, specialist contact, submission,
novelty/priority assertions, and external release are not authorized by this
paper-local acceptance.
