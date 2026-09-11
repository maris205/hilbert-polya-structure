# P205 actual terminal cold-build pair and all-page viewing

2026-09-06 UTC. Root performed two new physical source-only builds after
actual A/B accepted deltas and creation of the 22-file Round2 freeze.
The unchanged live and frozen TeX/bibliography inputs agree exactly.

From the workspace root, `bash docs/papers204_208_sequence/qa/cold_build.sh`
was executed twice with the absolute `frozen_round2` source directory,
distinct nonexistent destinations `qa_final/cold_build_1` and
`qa_final/cold_build_2`, and the frozen PDF as the comparison reference.
Both helper processes exited zero. Each created a distinct temporary
stage and copied only eight TeX/bibliography source files, with no PDF,
auxiliary or compiled bibliography as input. Each actually ran pdflatex,
BibTeX, pdflatex, pdflatex under guarded failure handling. Full source pins,
engine versions, environment, pass logs, recorder and products remain in
the two build directories. No failed or intermediate log was normalized.

The manual engine sequence is the disclosed fallback for unavailable
latexmk, not a claimed latexmk execution. Settings in both stages were
SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1, TZ=UTC and LC_ALL=C.
Both final PDFs have three A4 pages, 306,286 bytes and SHA-256
`f4aec5af74f6ab4a78e1120270e818f20b412694d9d7938145564b9b447e41cc`.
Each helper actually raw-compared its PDF with frozen Round2; root also
raw-compared the two final PDFs, all comparator exits zero. Final logs
have no warning, undefined citation/reference, overflow or underfull box;
all 25 font rows are embedded Type 1 and identifying metadata are blank.

Root rendered build 1 at 120 dpi and actually opened and read each of its
three pages. Page-specific observations and exact image pins are in
[PAGE_VIEWS.json](PAGE_VIEWS.json). The second PDF is byte-identical, so
no different page content is inferred or separately claimed to be viewed.
These are the two terminal builds, not relabelled reviewer/initial builds.
This artifact evidence does not by itself establish five-paper completion.
