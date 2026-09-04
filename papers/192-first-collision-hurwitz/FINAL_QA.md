# P192 terminal QA

terminal_status=PASS
open_findings=critical:0,major:0,minor:0
historical_findings=critical:0,major:1,minor:3,all_resolved:true
external_status=OWNER_RED_AMBER/HOLD_EXTERNAL
cold_builds=2
pdf_sha256=e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57
pages=4
bibliography_records=6
font_rows_embedded_subsetted_unicode=25/25/25/25
author_assertions=1962920
review_a_assertions=305104
review_b_assertions=4606117
visual_pages=4
visual_inspection=PASS_4_OF_4

**Decision:** `PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`

- The 1,962,920-assertion author control and both process-separated reviewer
  controls replay byte-identically to their canonical transcripts.  A separate
  C++ stream also exhausts all 4,782,969 Prüfer words at `n=9`.
- Review A's one Major and three Minor findings were repaired; Review B found no
  new issue.  No finding remains open.
- Round 1, Round 2, and the live PDF are byte-identical with SHA-256
  `e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57`.
  The distinct Round-0 PDF is preserved with SHA-256
  `aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1`.
- Both physical source-only builds reproduce the 323,972-byte final PDF.  The
  PDF is anonymous, A4, unencrypted, four pages, and has 25/25 embedded,
  subsetted, Unicode-mapped font rows and blank identifying metadata.
- The exact six-entry bibliography/citation-key sets agree.  All four pages
  passed 180-dpi visual inspection.

Per-page visual observations:

- page 1: title, abstract, literal Hurwitz convention, subtraction boundary,
  and owner warning are complete and unobstructed.
- page 2: scheduler theorem, sharp boundary cases, fixed census, and opening
  inverse definitions are legible with no clipped equations.
- page 3: complete fibre theorem, proof, conjecture boundary, and control
  limitations render cleanly; the history law is visibly labelled conjecture.
- page 4: all six references, including the repaired Campion Loth--Rattan
  record, are readable with no overlap or truncation.

This pass certifies internal proof-package and artifact consistency only.  It
does not certify the all-`n` history conjecture, novelty, priority, ownership
completeness, freedom to operate, or readiness for external circulation.
