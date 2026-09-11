# P187 terminal QA

terminal_status=PASS
open_findings=critical:0,major:0,minor:0
external_status=OWNER_AMBER/HOLD_EXTERNAL
cold_builds=2
pdf_sha256=399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1
pages=4
bibliography_records=2
author_assertions=278456
review_a_assertions=1444819
review_b_assertions=219556
visual_pages=4
visual_inspection=PASS_4_OF_4

**Decision:** `PASS_INTERNAL / ROUND2_DUAL_REVIEW_FREEZE / HOLD_EXTERNAL`

- The 278,456-assertion author control and both reviewer controls replay
  byte-identically to their canonical transcripts.
- Review A contributes 1,444,819 assertions and Review B 219,556; both close
  at `0 Critical / 0 Major / 0 Minor`.
- Round 0, Round 1, Round 2, and live PDF are byte-identical with SHA-256
  `399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1`.
- Both physical source-only builds reproduce the 332,246-byte final PDF.
- The PDF is anonymous, A4, unencrypted, four pages, and has 25/25 embedded,
  subsetted, Unicode-mapped font rows and blank identifying metadata.
- The exact two-entry bibliography/citation-key sets agree. All four pages
  passed 220-dpi visual inspection.

Per-page visual observations:

- page 1: title, abstract, opening definitions, and displayed equations are
  fully visible with no clipping or overlap.
- page 2: theorem statements, fixed-state census, and proof blocks are aligned
  and readable; margins remain clear.
- page 3: inverse-fibre formulas and explanatory prose are complete, with no
  broken glyphs or overprinted material.
- page 4: concluding proof, limitations, declarations, and references render
  cleanly; the lower-page whitespace is intentional and contains no truncation.

This pass certifies internal proof-package and artifact consistency only. It
does not certify novelty, priority, ownership completeness, freedom to
operate, or readiness for external circulation.
