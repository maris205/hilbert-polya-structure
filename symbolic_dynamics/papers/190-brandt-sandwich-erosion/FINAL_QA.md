# P190 terminal QA

terminal_status=PASS
open_findings=critical:0,major:0,minor:0
external_status=OWNER_AMBER/HOLD_EXTERNAL
cold_builds=2
pdf_sha256=81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d
pages=4
bibliography_records=5
author_assertions=1555420
review_a_assertions=2615881
review_b_assertions=1438171
visual_pages=4
visual_inspection=PASS_4_OF_4

**Decision:** `PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`

- The 1,555,420-assertion author control and both reviewer controls replay
  byte-identically to their canonical transcripts.
- Review A contributes 2,615,881 assertions, found two Minor presentation
  issues, and accepted both repairs; Review B contributes 1,438,171
  assertions and found no new issue. No finding remains open.
- Round 0 preserves SHA-256
  `5fb58fae99f49f14653f5eee283e2f66c3af87c06fca65e1b982e5936123eb66`;
  Round 1, Round 2, and live PDF share
  `81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d`.
- Both physical source-only builds reproduce the 383,748-byte final PDF.
- The PDF is anonymous, A4, unencrypted, four pages, and has 29/29 embedded,
  subsetted, Unicode-mapped font rows and blank identifying metadata.
- The exact five-entry bibliography/citation-key sets agree. All four pages
  passed 220-dpi visual inspection.

Per-page visual observations:

- page 1: title, abstract, Brandt multiplication law, local map, and opening
  lemma are complete, centered, and free of collisions.
- page 2: normal form, fixed census, sharp-tail formulas, and trace expression
  are fully readable with no marginal overflow.
- page 3: anchor-gap product, zero-fibre spectrum, image criterion, and mass
  identity render cleanly with intact delimiters and proof boxes.
- page 4: control table, limitations, declarations, and five references are
  complete; no clipping, overlap, or broken glyph is visible.

This pass certifies internal proof-package and artifact consistency only. It
does not certify novelty, priority, ownership completeness, freedom to
operate, or readiness for external circulation.
