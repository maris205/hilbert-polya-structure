# Final QA report — Papers 87–91

Checkpoint: 2026-08-28 UTC

Result: **5/5 GO INTERNAL; FINAL FREEZE; EXTERNAL HOLD**

| Slot | Pages | Bytes | Deterministic control | Independent gate | Clean log | Embedded fonts | Visual pages |
|---:|---:|---:|---|---|---|---|---|
| P87 | 5 | 313,957 | 700,499 exact assertions | `GO_INTERNAL` | pass | 24/24 | 5/5 |
| P88 | 7 | 370,404 | 19,764 exact assertions, including `F_4` | `GO_INTERNAL` | pass | 28/28 | 7/7 |
| P89 | 6 | 320,648 | 66,787 exact assertions; 10 floating diagnostics | `GO_INTERNAL` | pass | 24/24 | 6/6 |
| P90 | 5 | 329,610 | 298,283 exact assertions | `GO_INTERNAL` | pass | 25/25 | 5/5 |
| P91 | 4 | 296,997 | 12,175 exact assertions / 20 group presentations | `GO_INTERNAL` | pass | 22/22 | 4/4 |

The canonical packet contains **27 A4 pages**, **1,631,616 PDF bytes**,
**1,097,508 exact assertions**, and 123/123 embedded, subsetted,
Unicode-mapped font records. P89's 10 floating evaluations are diagnostics
and are not included in the exact total.

After every hostile-review correction, the integrating pass rebuilt each
manuscript with `pdflatex -> bibtex -> pdflatex -> pdflatex`; all 20 stages
exited zero. The resulting PDFs reproduced the paper-local frozen digests, and
all five `sha256sum -c SHA256SUMS` checks passed entry by entry.

A uniform `main.log`/`main.blg` scan found no LaTeX or package warning,
undefined citation/reference/control sequence, overfull or underfull box,
fatal error, emergency stop, or rerun request. Source and extracted-PDF scans
found no `TODO`, `FIXME`, `XXX`, `TBD`, unresolved-reference sentinel,
verification marker, or placeholder. `pdfinfo` reported A4 and PDF 1.5 for
every paper; every PDF had a nonempty searchable text layer.

The integrating pass reran all five exact controls and rendered and visually
inspected all 27 pages. No page was clipped, overlapped, blank in error,
malformed, or missing content. Titles, matrices, theorem statements, long
formulas, ownership tables, numerical diagnostics, bibliographies, and page
furniture were legible. In particular, P88's previously displaced table and
equation (21), P89's annealed matrix exponent, and the full P90 orbit formula
were checked in the final PDF images.

The audits closed substantive issues: P87's direct fixed-product owner and
`a=1` transitivity endpoint; P88's quantifiers, extension-field control, and
reconstruction ownership; P89's delayed-renewal CLT clock; P90's sharp witness
and symmetry/Möbius boundaries; and P91's complete invariant decomposition and
full-shift endpoint.

Canonical PDF digests are frozen in `CANONICAL_PDF_MANIFEST.sha256`; every
paper package contains a source-and-artifact `SHA256SUMS`. This report
certifies internal reproducibility and mathematical consistency only. It does
not grant novelty, priority, authorship, venue fit, public release, or
submission clearance.
