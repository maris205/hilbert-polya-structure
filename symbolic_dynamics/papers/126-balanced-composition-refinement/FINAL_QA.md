# Final QA — P126

Status: **PASS / GO_INTERNAL / EXTERNAL HOLD**.

- Hostile Review A: 0 critical, 2 owner/scope major, 4 minor; every item
  repaired in round one and marked CLOSED on narrow re-entry.
- Hostile Review B: 0 critical, 0 mathematical major, 0 owner-scope major,
  0 minor.
- Canonical paper verifier: PASS, **8,756,710 exact assertions**; fresh stdout
  is byte-identical to `code/verification_output.txt`.
- Independent Review-B cut-set control: PASS, **116,995 assertions**.  The
  re-entry audit also reran the pinned 5,512,265-assertion proof-spike verifier
  with byte-identical output.
- Isolated four-stage LaTeX/BibTeX builds: PASS; settled errors, warnings,
  undefined citations/references, box warnings, and rerun requests: zero.
- Final `main.pdf`, `main_round1.pdf`, and support-only
  `main_round2.pdf`: byte-identical, **4 A4 pages, 319,631 bytes**, SHA-256
  `e5d7ab3986a635a490804a8a81d7b3873b5c8403456fccf138af30315751ed3e`.
- The immutable round-zero PDF remains preserved at SHA-256
  `d48125fc509fc972b2b705226c33d7915a529523917fd786a5eda2190106ca1e`.
- Bibliography: **9/9** cited sources resolved.  All 24 listed font rows are
  embedded, subsetted, and Unicode-mapped; metadata is anonymous; there is no
  form, JavaScript, encryption, or embedded file.
- All four current pages were independently raster-inspected by both review
  tracks; no clipping, overlap, missing glyph, malformed formula, unresolved
  marker, or layout regression was found.
- Owner result: bounded non-hit only.  External release, novelty, priority,
  posting, and submission remain **HOLD**.
