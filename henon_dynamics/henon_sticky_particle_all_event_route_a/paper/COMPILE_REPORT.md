# Deterministic compile report

LuaLaTeX was run for two passes in two isolated directories for each round
with `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
Both fresh outputs for every round were byte-identical to the retained file.
The settled warning regex found no LaTeX/package warnings, overfull or
underfull boxes, undefined references/citations, rerun requests, or missing
characters.  Every `pdffonts` row was embedded and subset; extracted-text
contracts passed.  Visual inspection found no clipping, collision, blank
content page, or malformed display.

| round | pages | font rows | SHA-256 |
|---|---:|---:|---|
| 0 | 2 | 16 | `b361f9926d5ff4cf166f3f8d450b9002935cf983c12b0b0a6db4c5299508f884` |
| 1 | 3 | 16 | `f3cec9741098acaa31816b43af464544b4025a96d63936b8b3f9222b979c3f16` |
| 2 | 4 | 19 | `b91f101d7947d4a5e5feeaf3a2dd2d405a3308ed1e0ec8bf984be2cdf262f6d8` |

All round hashes are distinct.  `main.pdf` is byte-identical to
`main_round2.pdf`.
The final-round extracted text includes `66/66` and
`duplicate-key-rejecting evaluation YAML`.
