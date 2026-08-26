# C183 compile report

Status: PASS.

- Engine: LuaLaTeX, two passes, `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`.
- Final PDF: 2 pages, 186,555 bytes.
- Final SHA-256: `adb2790ddb8044151177f7b30ef93b2bc3dcc10ad3bf2ad62e8128ac569fc319`.
- Round hashes are pairwise distinct:
  - round 0: `550aa8cf9c039e6bb1f29881a9bc059c13c41643571a8cdd19a2b25c91f308d7`
  - round 1: `42a1183f766a6c34f1eeb9d765c0f4a48e0789cceda61bb1b44d0438a951be94`
  - round 2/final: `adb2790ddb8044151177f7b30ef93b2bc3dcc10ad3bf2ad62e8128ac569fc319`
- Every round contains the corrected owner boundary; their `Revision-round focus` paragraphs are content-distinct.
- Two clean fresh-directory, two-pass builds reproduced the final PDF byte for byte.
- Final and fresh log scans contain no LaTeX/package warning, overfull/underfull box, undefined reference, missing glyph, or fatal finding.
- `pdffonts`: every font is embedded and subset.
- Visual inspection: both rendered pages are complete, legible, non-overlapping, balanced, and free of clipping or blank regions.

Drafting improvements and visual checks are internal workflow artifacts, not external peer review.
