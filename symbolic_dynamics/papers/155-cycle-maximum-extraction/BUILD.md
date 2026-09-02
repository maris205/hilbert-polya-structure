# Build and QA record — P155

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Settled author build

- Engine: pdfTeX 1.40.22 / LaTeX2e; BibTeX 0.99d.
- Sequence: `pdflatex -> bibtex -> pdflatex -> pdflatex`.
- `main.pdf`: 4 A4 pages, 345,390 bytes.
- `main_round1.pdf`: byte-identical to `main.pdf`, SHA-256
  `54fb1fb0a2519950d3b5725ea5e02c09eb89de13048bf7a97c62d41a9f99ebd1`.
- `main_round2.pdf`: byte-identical to `main_round1.pdf` and `main.pdf` at
  the same SHA-256; Review B required no manuscript rebuild or content change.
- `main_round0_original.pdf` remains unchanged at SHA-256
  `f1025e7a19e40eed7dc2608bdebad47ebed998345bc58d94aec6b27025c6b3c8`.
- Bibliography: 4/4 primary-source entries cited and resolved.
- Settled logs: zero unresolved citation/reference, rerun request, build
  error, BibTeX warning, overfull box, underfull box, or multiply defined
  label.
- Fonts: all 28 reported font rows embedded and subsetted.
- PDF: version 1.5, A4, unencrypted, zero embedded files, no detected
  JavaScript/AcroForm marker, and blank identifying title/author/subject/
  keyword metadata.  Volatile dates and trailer IDs are suppressed.
- Visual QA: all 4/4 pages rasterized at 120 dpi and inspected; no clipping,
  overlap, broken formula, unresolved marker, bad glyph, or illegible
  reference was found.

## Reproducibility

Two fresh temporary directories containing only `main.tex` and
`references.bib` were built with the four-stage sequence.  Both isolated PDFs
were 4 pages, 345,390 bytes, and byte-identical to `main.pdf` at the SHA-256
above.

## Exact control

- Literal states through rank ten: 4,037,913.
- Image target/rank cells: 145,684.
- Independent endpoint-DP targets: 46,233.
- Constructive section cells: 3,161.
- Every-target fibre cells: 53,218.
- Assertions: 16,473,121; `status=PASS`.
- Fresh stdout is byte-identical to `verification_output.txt`.
- Transcript SHA-256:
  `b398a0cade8b64cdab92ee6c638e7607f3310cf9e304a52e8df07ca7d57e410c`.

Enumeration is exact falsification pressure, not proof or source ownership.
The transcript marks the power-of-two clock `NOT_CLAIMED`.

## Review boundary

Hostile Review A returned 0 Critical / 0 Major / 2 Minor; both are closed in
Round 1 and mapped in `IMPROVEMENT_LOG.md`. Hostile Review B returned
`ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`. Round 2 is a
byte-identical mechanical acceptance freeze with no manuscript, bibliography,
verifier, or transcript change. Scoped repository synchronization is governed
by the standing batch authorization; posting, specialist contact, submission,
novelty/priority assertions, and external release remain unauthorized.
