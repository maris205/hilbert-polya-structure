# Compilation and actual visual inspection

Engine LuaLaTeX; frozen epoch 1788566400; two fresh directories and two passes
per round. Three source drivers select actual new theorem sections.
Rounds: 2 / 3 / 4 pages. Final SHA256:
`6b46c9c8fddd921ffa5b9518fedfe283da6eef581698c0ba4bdacb5af010b6bf`. The final file equals `main_round2.pdf`.

All final fonts are embedded and subset (eight font records).
Text extraction contains both abstracts, six English and six Chinese keywords,
correct revision labels and expected proof-section markers. No unresolved
citations/references, placeholder, control character, missing glyph or settled
layout warning remains. Initial font and overfull-line failures were fixed,
not suppressed; actual settled compiler logs remain byte-preserved.

Root opened **all four final pages** using view_image after 95-dpi Poppler
rasterization. Equations, Chinese/Latin spans, bottom lines, theorem boundaries
and references are visible without clipping or missing boxes.
This does not claim a venue submission, human review or publication-readiness
certificate. Fresh reproducibility is rerun by the release command.
