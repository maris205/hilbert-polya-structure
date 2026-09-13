# Hash-bound layout visual inspection

Decision: PASS for main-agent visual inspection, not independent mathematical or build acceptance.

PDF inspected: `build/layout-20260905-r0/main.pdf`, SHA256 `ab195a2b49012e9b4b320ddbabffd9666c076b37b09a8b9dc20c400dd266a5b4`, 29 pages. Main source SHA256 `9fbc475fa435b66983fe97807e7fdf5544dbd9cc8952e892d0830848b39724a8`.

The main agent rendered all 29 pages locally with `/usr/bin/pdftoppm -r 72 -png` into the newly created temporary directory `/tmp/p27-visual-IPpLGP` and opened every page image. Render session 88301 completed with exit 0 and no diagnostic output. Neither PDF nor build source was modified. Temporary images are viewing derivatives, not publication-root artifacts or scientific evidence.

All pages show readable normal-size type, intact mathematical displays and page numbering, with no visible column collisions, clipped lines, missing regions or blank proof pages at this review resolution. The title and Anonymous line are clean. Main-theorem clauses continue coherently over pages 7–8; proof text and displayed formulas continue through the substantive body.

The corrected degree-set/cardinality display on page 13 fits without changing its mathematical definitions. Tables 1–2 on pages 22–23 preserve six aligned row IDs, source states, score columns and carries. The repaired Table 3 has P1–Q1 on page 24 and Q2–Q3 on page 25 with an intact repeated header; split score labels/equalities do not overlap adjacent cells. The matrices, typed path and determinant conclusions remain visible afterward.

The page-26 boundary table has visibly loose justification and hyphenated narrow labels but readable, separated columns; all seven witnesses and consequences fit. This agrees with the independent diagnostic report's disposition of 17 table underfull warnings. The page-4 literature paragraph has mildly loose spacing (the remaining single underfull warning), with intact prose/citations. These 18 warnings are disclosed and accepted as spacing/hyphenation only, not suppressed. No visual evidence of lost content was found in their regions.

The conclusion ends on page 27. References occupy pages 28–29, visibly numbered 1–20, with no appendix, theorem or resumed body afterward. This is a full-page visual review at 72 dpi, not a claim of character-perfect pixel comparison or independent proof verification. The separately hash-bound source-equivalence and completed-output diagnostic reviews provide the complementary semantic checks. The failed builder classification for these bytes remains unchanged; only a later actual successful dual build may establish deterministic-build acceptance.
