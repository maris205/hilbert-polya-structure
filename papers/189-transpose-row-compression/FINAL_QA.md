# P189 terminal QA

terminal_status=PASS
open_findings=critical:0,major:0,minor:0
external_status=OWNER_AMBER/HOLD_EXTERNAL
cold_builds=2
pdf_sha256=6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81
pages=4
bibliography_records=4
author_assertions=5336613
review_a_assertions=1493113
review_b_assertions=1493195
visual_pages=4
visual_inspection=PASS_4_OF_4

**Decision:** `PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`

- The 5,336,613-assertion author control and both reviewer controls replay
  byte-identically to their canonical transcripts.
- Review A contributes 1,493,113 assertions and Review B 1,493,195; both close
  at `0 Critical / 0 Major / 0 Minor`.
- Round 0, Round 1, Round 2, and live PDF are byte-identical with SHA-256
  `6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`.
- Both physical source-only builds reproduce the 363,099-byte final PDF.
- The PDF is anonymous, A4, unencrypted, four pages, and has 29/29 embedded,
  subsetted, Unicode-mapped font rows and blank identifying metadata.
- The exact four-entry bibliography/citation-key sets agree. All four pages
  passed 220-dpi visual inspection.

Per-page visual observations:

- page 1: title, abstract, literal map, height calculus, and footnote material
  are fully visible without clipping.
- page 2: four-iterate normal form, recurrence census, and depth-layer formulas
  remain aligned and readable across the dense proof page.
- page 3: time-one/time-two fibre laws, control table, declarations, and all
  mathematical symbols render cleanly inside the margins.
- page 4: all four references are complete and legible; the sparse lower page
  is intentional rather than missing content.

This pass certifies internal proof-package and artifact consistency only. It
does not certify novelty, priority, ownership completeness, freedom to
operate, or readiness for external circulation.
