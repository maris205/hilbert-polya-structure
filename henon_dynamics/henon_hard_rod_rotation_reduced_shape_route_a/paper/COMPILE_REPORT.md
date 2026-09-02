# Deterministic compile report

LuaLaTeX was run for two passes in two isolated directories for each round
with `SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
Both fresh outputs per round were byte-identical to the retained artifact.
The settled warning regex found no LaTeX/package warnings, overfull or
underfull boxes, undefined references/citations, rerun requests, or missing
characters.  Every font row was embedded and subset.  Page-by-page visual
inspection found no clipping, overlap, blank content page, malformed formula,
or corrupted scope text; the corrected `sigma,c` equation is rendered with
its comma and spacing.

| round | substantive layer | pages | font rows | SHA-256 |
|---|---|---:|---:|---|
| 0 | corrected rotation quotient and exact conjugacy | 2 | 19 | `8ea2fd6618e41272a03c396a295957f1e02acbbc2a1e7cb3e56fbed96555d15b` |
| 1 | all events, invariants, no Zeno, unreduced obstruction | 3 | 17 | `9cac72b380bdbc9794037a113f1dd1b05629b9e6c9b00e1e8ac16308de56270f` |
| 2 | stabilizer return theorem, evidence, Route-A boundary | 4 | 18 | `dc8890acabb563e3de21572381e479c8ac7ea2a23e6e4077aab4f8bffa6589f9` |

All three hashes are distinct and `main.pdf == main_round2.pdf` byte for byte.
Extracted-text contracts include `Exact shape conjugacy`, `Why the unreduced
statement is false`, `Stabilizer and minimal-period theorem`, `HEN-O280`, `96/96`,
`ROUTE_A_REJECTED`, and `NO_BAD_EULER_OR_ROOT_NUMBER` in their required rounds.
