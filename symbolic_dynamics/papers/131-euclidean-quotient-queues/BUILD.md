# Build protocol — P131

Run `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` in that order.  Final QA must
repeat the four-stage build in an isolated temporary directory, require a
clean settled log, byte-compare a fresh verifier run with the canonical
transcript, inspect every rasterized page, audit embedded fonts and anonymous
metadata, and hash every frozen source, control, review, and PDF artifact.

## Final round-two closure build

- Date: 2026-08-31 UTC.
- Fresh verifier: PASS / byte-identical, **6,101,926 assertions**.
- Isolated four-stage build from only `main.tex` and `references.bib`: PASS;
  its output is byte-identical to both final PDF copies.
- Settled errors, warnings, undefined citations/references, bad boxes, and
  actionable rerun requests: zero.
- `main.pdf` and `main_round2.pdf`: byte-identical, **4 A4 pages, 314,641
  bytes**, SHA-256
  `07c7d40c21e42dde6dd416ca1aa11aef60847d6e2e506df3db4a2e4bbfd7b4af`.
- All 21 font rows are embedded, subsetted, and Unicode-mapped; PDF author,
  title, subject, and keywords are blank; no form, JavaScript, or encryption.
- All four final pages were rasterized and inspected: no clipping,
  overlap, missing glyph, malformed display, or unexpected blank page.
- `main_round0_original.pdf` and `main_round1.pdf` are retained as historical
  snapshots and are not the final release candidate.
- Consolidated review and closure evidence are in `HOSTILE_REVIEW.md` and
  `FINAL_QA.md`; frozen artifact hashes are in `SHA256SUMS`.
