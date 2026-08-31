# Final QA — P131 Euclidean quotient queues

**Date:** 2026-08-31 UTC.  **Result:** **PASS**.  **Internal status:**
**GO_INTERNAL**.  **External status:** **HOLD_EXTERNAL**.

## 1. Final payload

- Source: `main.tex`.
- Bibliography: `references.bib`.
- Canonical PDF copies: `main.pdf`, `main_round2.pdf`.
- PDF size: **314,641 bytes** each.
- PDF SHA-256:
  `07c7d40c21e42dde6dd416ca1aa11aef60847d6e2e506df3db4a2e4bbfd7b4af`.
- Pages: **4**, A4, rotation zero.
- Exact assertions: **6,101,926**.
- Final decision: internal continuation allowed; every external action remains
  on hold.

`main_round0_original.pdf` and `main_round1.pdf` are historical snapshots and
are not final release candidates.

## 2. Fresh canonical verifier

The final QA ran:

```sh
fresh=$(mktemp /tmp/p131-final-verify-XXXXXX.txt)
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py > "$fresh"
cmp -s "$fresh" code/verification_output.txt
sha256sum "$fresh" code/verification_output.txt
wc -c "$fresh" code/verification_output.txt
```

Results:

- `cmp` return code: `0`;
- fresh and canonical transcripts: **1,868 bytes** each;
- both transcript SHA-256 values:
  `caa4df1e70fd2bdb86aa5aeb1308c2baa74b5d5e560d73980f1f6886c91bc8c6`;
- fresh terminal lines: `ASSERTIONS=6101926`, `STATUS=PASS`;
- finite-scope and external-hold sentinels are present.

The verifier source itself has SHA-256
`94939887128cf0d487e6b054d5113c3fcd6f0921c880c07de5351a5b5eb9d07a`.
The finite range is exact counterexample pressure, not a proof of the
all-parameter theorems or of novelty.

## 3. Isolated four-stage build

Only `main.tex` and `references.bib` were copied into the isolated temporary
directory `/tmp/p131-final-build-SzBZ9t`.  The exact sequence was:

```sh
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four commands returned success.  The isolated PDF byte-matched both
canonical final copies (`cmp=0` for each).  All three files were **314,641
bytes** and had SHA-256
`07c7d40c21e42dde6dd416ca1aa11aef60847d6e2e506df3db4a2e4bbfd7b4af`.

The settled LaTeX log and BibTeX log contain:

- errors or fatal stops: 0;
- LaTeX/package warnings: 0;
- undefined citations or references: 0;
- multiply defined labels: 0;
- overfull or underfull boxes: 0;
- actionable rerun requests: 0;
- BibTeX warnings: 0.

The two `microtype` character-029 lines are `Package ... Info` notices about
ignored protrusion settings, not warnings or missing rendered glyphs.
BibTeX's `missing$ -- 6` line is a function-execution count; its actual
`warning$` count is zero.

## 4. PDF structure, fonts, text, and anonymity

`pdfinfo` reports:

- PDF 1.5, A4 (`595.276 x 841.89 pt`), 4 pages, rotation zero;
- unencrypted;
- no form, JavaScript, custom metadata, metadata stream, user properties, or
  suspect object;
- blank title, subject, keywords, and author metadata fields;
- creator `LaTeX with hyperref` and producer `pdfTeX-1.40.22`, with no personal
  identity.

The visible author is `Anonymous`.  Extracted text contains no affiliation,
institution, email address, or personal author name.  The only occurrence of
“authorship” is the explicit sentence keeping authorship and external-release
decisions on hold.

`pdffonts` reports **21/21** rows embedded, subsetted, and Unicode-mapped; all
are Type 1 fonts.  `pdfimages -list` reports no embedded raster image.

Extracted PDF text contains no `??`, `[?]`, `[VERIFY]`, TODO, or FIXME marker.
Each page has nonempty extractable text.

## 5. Four-page visual inspection

All pages were rasterized at 160 dpi and inspected individually.

- Page 1: title, anonymous author, abstract, carrier, Euclidean convention,
  update, and owner paragraph are clean; the page break is intentional.
- Page 2: the `N=2,3` isomorphism exception is visible and correctly placed;
  the terminal-core theorem, example, and raw map fit without collision.
- Page 3: raw conjugacy/inverse proof, depth OGFs, and singleton `eta` display
  are legible and correctly aligned.
- Page 4: fibre theorem, image/Garden boundaries, Burnside formula, control
  limitations, and all six bibliography entries are complete and readable.

No page has clipping, overlap, missing glyphs, malformed mathematics,
unexpected blank space, accidental blank pages, broken hyperlink text, or an
unreadable reference.

## 6. Review and status consistency

- Review-A conditions M1, M2, O1, singleton `eta`, marked-cut example, and
  support synchronization are closed.
- Review B's sole minor is closed by the explicit `N=2,3` exception and
  `N>=4` levelwise statement in `main.tex`.
- `README.md`, `BUILD.md`, and `IMPROVEMENT_LOG.md` now state final QA status
  and the round-two PDF bytes/hash.
- `HOSTILE_REVIEW.md` consolidates the immutable A/B round records and reports
  zero outstanding findings.
- `SHA256SUMS` covers every frozen source, control, review, support, and PDF
  artifact; transient LaTeX intermediates are intentionally excluded.

## 7. Final release gate

**PASS / GO_INTERNAL.**  The final source, exact control, isolated build,
four-page visual inspection, fonts, metadata, anonymity, and documentation
are mutually consistent.

**HOLD_EXTERNAL.**  The owner search is bounded and cannot establish novelty
or priority.  Posting, submission, authorship, and every other external action
require a separate authorized decision after the re-entry work described in
`HOSTILE_REVIEW.md`.
