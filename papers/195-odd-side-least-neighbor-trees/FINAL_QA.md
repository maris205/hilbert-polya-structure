# P195 terminal QA

terminal_status=PASS
open_findings=critical:0,major:0,minor:0
historical_findings=critical:0,major:1,minor:1,all_resolved:true
external_status=OWNER_AMBER/HOLD_EXTERNAL
cold_builds=2
pdf_sha256=d5dbac8ed78f1f3eccc3c7aeccda852e6f44f77a513091032120254119ff9c0a
pages=3
bibliography_records=4
font_rows_embedded_subsetted_unicode=23/23/23/23
author_assertions=4328312
review_a_assertions=6551607
review_b_assertions=9390311
visual_pages=3
visual_inspection=PASS_3_OF_3

**Decision:** `PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`

- The 4,328,312-assertion author control and both process-separated reviewer
  controls replay byte-identically to their canonical transcripts.
- Review A's one Major and one Minor findings were repaired; Review B found no
  new issue.  No finding remains open.
- Round 1, Round 2, and the live PDF are byte-identical with SHA-256
  `d5dbac8ed78f1f3eccc3c7aeccda852e6f44f77a513091032120254119ff9c0a`.
  The distinct Round-0 PDF is preserved with SHA-256
  `bc0723b0b4417125122a40784f444565cdbd5565c5b65ac477042be2c209de3f`.
- Both physical source-only builds reproduce the 318,096-byte final PDF.  The
  PDF is anonymous, A4, unencrypted, three pages, and has 23/23 embedded,
  subsetted, Unicode-mapped font rows and blank identifying metadata.
- The exact four-entry bibliography/citation-key sets agree.  All three pages
  passed 180-dpi visual inspection.

Per-page visual observations:

- page 1: title, abstract, literal rooted-tree map, ownership boundary, and
  recurrent-classification theorem are complete and unobstructed.
- page 2: nonuniqueness warning, sharp clock, and both parity-dependent EGF
  formulas are legible with no clipped displays.
- page 3: recurrent counts, zeta function, local inverse atlas, sharp fibre
  proof, controls, and all four references render cleanly.

This pass certifies internal proof-package and artifact consistency only.  It
does not certify novelty, priority, ownership completeness, freedom to
operate, or readiness for external circulation.
