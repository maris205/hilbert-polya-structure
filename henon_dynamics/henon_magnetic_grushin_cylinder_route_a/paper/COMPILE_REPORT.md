# Deterministic compile report

LuaLaTeX was run for two passes in two isolated directories for each round
with `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
Both fresh outputs per round were byte-identical to the retained artifact.
The settled warning regex found no LaTeX/package warnings, overfull or
underfull boxes, undefined references/citations, rerun requests, or missing
characters.  Every font row was embedded and subset; all extracted-text
sentinels passed.  Page-by-page visual inspection found no clipping,
collision, blank content page, malformed formula, or corrupted control text.

| round | pages | font rows | SHA-256 |
|---|---:|---:|---|
| 0 | 2 | 23 | `3e7b203f3348837f846133f2079e58622737c83e6364ff20a874fd6f02d30638` |
| 1 | 3 | 24 | `a5563a310c68a4c150fcbe891b40bb48093aa39e28cbc9124291877cbab7df3a` |
| 2 | 4 | 26 | `3295011b255e5e70761bd1119af1b8b72453b0724cfbb21663614321a763935d` |

All hashes are distinct and `main.pdf == main_round2.pdf` byte for byte.
The final-round extracted text includes `75/75` and
`duplicate-key-rejecting evaluation YAML`.
