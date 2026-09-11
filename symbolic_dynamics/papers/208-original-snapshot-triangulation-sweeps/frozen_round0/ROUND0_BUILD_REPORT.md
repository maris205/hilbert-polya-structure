# P208 adoption of source-only Round0 build evidence

2026-09-06 UTC. Root adopts the author's actual preparation_02 and
preparation_03 as the two stable pre-review source-only builds. Root did
not launch these builds. Their original preparation-role receipts remain
unchanged; the separate physical Round0 freeze is root's next action.
These are not the required post-B terminal builds.

Root read the complete build recorder and actual build/command records,
checked the before/after/copy maps for all 11 source files, all 146 consumed
external TeX inputs against the recorded 105,987-file pre-build inventories,
and all tool/shared-library pins. All 15 child commands per preparation
exited zero. Both builds used three pdflatex passes and intervening BibTeX,
no shell escape, SOURCE_DATE_EPOCH=1788652800 and FORCE_SOURCE_DATE=1.
All evidence is in qa_build and the root
[input inspection](../../docs/papers204_208_sequence/qa/p208_round0_input_inspection_v2/RECEIPT.json).
Checking the consumed subset does not claim a fresh hash of every unused
installed TeX file or a hermetic environment.

Both stable PDFs are seven pages, 376,433 bytes, SHA-256
dc3b6471ac0d62e887887a20a133b96a96d420b3ea65b3b06fb847f478038b62.
The actual author raw comparison exited zero; root's separate actual raw
comparison also exited zero. The sealed main.pdf is identical and is not
overwritten. All 27 font rows have embedding yes in the embedding column.
No final undefined citation/reference or overfull box remains.

Root actually viewed every final page, with page-specific observations and
render hashes in the [seven-page viewing record](../../docs/papers204_208_sequence/qa/P208_ROUND0_PAGE_VIEWS.md).
This is an actual root visual inspection, not a digest-only inference.
The real bibliography underfull hbox, badness 5681 at generated bbl lines
9--13, remains disclosed and its loose spacing is readable within margins.

Preparation_01 and its original source/PDF/logs/renders remain unchanged.
It compiled but had a real 44.62468pt overfull hbox in equation (6). Only
sections/04_extremum.tex differs from that old preparation: h and E were
split across two aligned rows. The stable pair and all later author-code
receipts use the repaired source. No failed or deficient output is erased.

Reuse is restricted to this exact final PDF and unchanged relevant source,
tool, configuration and consumed-resource dependencies. A and B still need
their own actual manuscript/build inspections; terminal cold builds and
all-page views remain after accepted B. OWNER_AMBER / HOLD_EXTERNAL.
