# P215 terminal artifact root acceptance

2026-09-11 UTC. Root independently accepts both separately authorized terminal
source-only builds. Each tree has exactly 165 regular files, zero symlinks, 15
zero exit roles, 27 empty stderr files, 227 runtime rows, 67 unique absolute
FLS inputs, 16 embedded/subset/Unicode fonts and six pages. The root checker
passed 2,153 assertions across both trees.

Terminal01 PDF is 200,921 bytes, SHA-256
`5496d730f292d3c9029343df14e7c3572a5192d818a6042866ce9116d0085237`;
terminal02 PDF is 200,921 bytes, SHA-256
`ac8c70fe4bbaa441df697230e3ba6f7debd21dfb6c49276b7f5b5a05bae2e396`.
Their differing build-time PDF metadata is explicitly not treated as RAW
equality. All six page renders, extracted text, aux, bbl and blg are RAW-equal
between runs. Root opened all twelve page images and found no visual defect.

Physical Round2 and both A/B final no-change reviews remain bound and current
findings are Critical 0 / Major 0 / Minor 0. This closes P215 terminal evidence;
the exact-five batch gate, central milestone and private Git sync remain
separate. `INTERNAL_COMPLETE / HOLD_EXTERNAL`.
