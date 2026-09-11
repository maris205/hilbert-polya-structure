# P191 terminal QA

terminal_status=PASS
open_findings=critical:0,major:0,minor:0
external_status=OWNER_AMBER/HOLD_EXTERNAL
cold_builds=2
pdf_sha256=d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b
pages=4
bibliography_records=5
author_assertions=3408240
review_a_assertions=2864221
review_b_assertions=164049
visual_pages=4
visual_inspection=PASS_4_OF_4

**Decision:** `PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`

- The 3,408,240-assertion author control and both reviewer controls replay
  byte-identically to their canonical transcripts.
- Review A contributes 2,864,221 assertions, found one Minor source-ledger
  issue, and accepted the repair; Review B contributes 164,049 assertions and
  found no new issue. No finding remains open.
- Round 0, Round 1, Round 2, and live PDF are byte-identical with SHA-256
  `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`.
- Both physical source-only builds reproduce the 380,787-byte final PDF.
- The PDF is anonymous, A4, unencrypted, four pages, and has 28/28 embedded,
  subsetted, Unicode-mapped font rows and blank identifying metadata.
- The exact five-entry bibliography/citation-key sets agree. All four pages
  passed 220-dpi visual inspection.

Per-page visual observations:

- page 1: title, abstract, cut filter, example orbit, and fixed-state recurrence
  are complete and visually separated.
- page 2: sharp clock, unique extremizer proof, fixed counts, and target-path
  recurrence are legible with no clipped equations.
- page 3: interval factorization, fibre mass, and control table render cleanly;
  all rows and captions remain inside the page.
- page 4: limitations, declarations, and all five references—including the
  OEIS entry—are complete and readable with no overlap or truncation.

This pass certifies internal proof-package and artifact consistency only. It
does not certify novelty, priority, ownership completeness, freedom to
operate, or readiness for external circulation.
