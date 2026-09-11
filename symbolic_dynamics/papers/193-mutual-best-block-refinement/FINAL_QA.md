# P193 terminal QA

terminal_status=PASS
open_findings=critical:0,major:0,minor:0
historical_findings=critical:0,major:1,minor:0,all_resolved:true
external_status=OWNER_AMBER/HOLD_EXTERNAL
cold_builds=2
pdf_sha256=b5b2f4e77bada6229a0716d9780a871f95b8e6ba75fa2c9e6794b5bf524ad0d9
pages=5
bibliography_records=4
font_rows_embedded_subsetted_unicode=29/29/29/29
author_assertions=7985745
review_a_assertions=917785
review_b_assertions=1170066
visual_pages=5
visual_inspection=PASS_5_OF_5

**Decision:** `PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`

- The 7,985,745-assertion author control and both process-separated reviewer
  controls replay byte-identically to their canonical transcripts.
- Review A's one Major source-collision finding was repaired; Review B found no
  new issue.  No finding remains open.
- Round 1, Round 2, and the live PDF are byte-identical with SHA-256
  `b5b2f4e77bada6229a0716d9780a871f95b8e6ba75fa2c9e6794b5bf524ad0d9`.
  The distinct Round-0 PDF is preserved with SHA-256
  `e41e171c8f412cf93aae9510052ed0d8ad165125be1bd4c04133f1b410048267`.
- Both physical source-only builds reproduce the 390,196-byte final PDF.  The
  PDF is anonymous, A4, unencrypted, five pages, and has 29/29 embedded,
  subsetted, Unicode-mapped font rows and blank identifying metadata.
- The exact four-entry bibliography/citation-key sets agree.  All five pages
  passed 180-dpi visual inspection.

Per-page visual observations:

- page 1: title, abstract, map definition, matching subtraction, and direct-sum
  setup are complete and visually separated.
- page 2: block surgery, Lyapunov statistic, recursive clock, and sharp-depth
  theorem are legible with no clipping.
- page 3: depth-layer recurrence and indecomposable-parent lemma render cleanly,
  including all displayed generating functions.
- page 4: target-resolved fibre product, image census, maximum proof, and
  limitation text remain inside the page.
- page 5: exact-control table, same-carrier separations, declarations, and all
  four references are complete and readable.

This pass certifies internal proof-package and artifact consistency only.  It
does not certify novelty, priority, ownership completeness, freedom to
operate, or readiness for external circulation.
