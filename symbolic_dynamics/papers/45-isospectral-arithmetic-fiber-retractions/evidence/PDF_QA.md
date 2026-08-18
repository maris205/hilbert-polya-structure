# Final PDF quality assurance

Status: PASS for the writer-side checks recorded here. The candidate remains
`HOLD_FOR_INDEPENDENT_WRITER_AUDIT`; this document is not an independent clean
finding.

## Reproducible build

- Fixed environment: `SOURCE_DATE_EPOCH=1787011200`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- Two fresh and independent pdfLaTeX/BibTeX build directories produced
  byte-identical PDFs.
- Final `main.pdf` and `main_round2.pdf` SHA-256:
  `072bfb9de07b46f7705118ce8342b3f56a90fef45240ee24be33c9931b908783`.
- Final size: 397713 bytes; 17 A4 pages; PDF 1.5; no creation or modification
  date is present in `pdfinfo`.
- Preserved round-zero PDF SHA-256:
  `4bc233960f6da4467b7ebbe517466cd8a9407d23c86f0fed6d22703aa0dfa2a3`.
- Preserved round-one PDF SHA-256:
  `14fa5152e225102931628bab8193c27c3fb1fd6df75c697d312048d9f3861aed`.
- Final compile log SHA-256:
  `92e801645db3405c27bd3df7ebc081ca09d0e80c084bc6c1ad1a1c90f320d042`.
- Final bibliography artifact SHA-256:
  `7257a9891c2e58223a1a17e947635b3698c2adf3eeb1fc0b70b5272dfbbffd12`.

The final log has zero undefined citations/references, overfull boxes,
underfull boxes, or badness diagnostics.

## Fonts, text, and bounding boxes

- `pdffonts` reports 24 font rows; every row is embedded, subsetted, and has a
  Unicode map. No Type 3 font occurs.
- Layout text extraction has 57620 bytes and 1027 lines. The only C0 bytes are
  line feeds and the 17 ordinary form-feed page separators emitted by
  `pdftotext`; unexpected C0 count is zero and U+FFFD count is zero.
- Required extracted markers are present: the title, Theorem 4.2, the
  three-regime maximal-order theorem, the self-commutator section, and the
  references.
- The bbox XHTML parses as XML and contains 17 pages and 7308 words. It has
  zero negative coordinates and zero words outside their page bounds.

## Page-by-page visual review

All pages were rasterized from the final PDF and inspected at full-page scale.

| Page | Check | Result |
|---:|---|:---:|
| 1 | title, abstract, contents, margins | PASS |
| 2 | theorem opening, equations, contents continuation | PASS |
| 3 | main theorem continuation and related work | PASS |
| 4 | arithmetic fibers and block formulas | PASS |
| 5 | fiber schematic, labels, transition to Section 3 | PASS |
| 6 | Schatten theorem and spectral ledger | PASS |
| 7 | table, determinant text, similarity lemma | PASS |
| 8 | similarity gap and exact optimizer | PASS |
| 9 | phase diagram, two condition boxes, theorem start | PASS |
| 10 | maximal-order proof and Section 6 opening | PASS |
| 11 | Tauberian lemma and saturated Weyl law | PASS |
| 12 | modulo/eigenvalue laws and commutator theorem | PASS |
| 13 | commutator proof and controls section | PASS |
| 14 | limitations, conclusion, Appendix A | PASS |
| 15 | Appendices A--C and determinant formulas | PASS |
| 16 | Tauberian close, canonical evidence, references | PASS |
| 17 | references tail and terminal page number | PASS |

An earlier draft placed the two lower condition boxes of the phase diagram on
top of one another. They were stacked, the paper was rebuilt from scratch, and
page 9 was inspected separately at original raster resolution before the full
17-page replay above.
