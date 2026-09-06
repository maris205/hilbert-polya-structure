# P207 source-only build and actual all-page inspection

2026-09-06 UTC. Operator and manuscript contributor: root.
Final Round0 source-only builds: `build_round0_03/`, `build_round0_04/`.
Both actual commands used the batch's unchanged `qa/cold_build.sh` with
the absolute paper directory and a new absolute build directory. The
second command also supplied `build_round0_03/main.pdf` as the raw-byte
comparison target. Both commands exited zero, including the actual `cmp`.

Each build began in a fresh temporary directory populated only by
main.tex, math_commands.tex, references.bib and the six modular sections.
The installed `latexmk` command is absent. The disclosed compile-skill
fallback is the existing pdflatex/bibtex/pdflatex/pdflatex sequence, not a
fabricated latexmk run. The build directories retain exact source hashes,
engine versions, SOURCE_DATE_EPOCH=1704067200, FORCE_SOURCE_DATE=1,
TZ=UTC, LC_ALL=C, all pass logs, BibTeX output, recorder files and PDF data.

Both PDFs are seven pages and 407,557 bytes, SHA-256
`5e74fa6a334f1cbc23837632b364729d97111b231e1ef8c3fd6a40a8dbc78759`.
Final DIAGNOSTICS.txt is empty: zero undefined citations/references or
overfull-box warnings. All 31 listed font rows are embedded. The complete
extracted text contains no TODO/FIXME/XXX/[VERIFY] or unresolved `??`
markers. `main.pdf` is a byte copy of the successful fourth attempt's PDF.

## Failures and earlier layout preserved

The first cold attempt exited one before producing a PDF because the
two DeclareMathOperator macro names lacked backslashes. Its complete
source/log directory was moved intact from its temporary name to
`failed_build_round0_01/`; the live macro declarations alone were fixed.
The second cold attempt succeeded, with a two-line 11.20634pt overfull
diagnostic on a kernel display. Its original PDF/logs remain in
`build_round0_02/`. Splitting the matrix row produced the clean third
attempt, and the fourth reproduced that PDF exactly. No failed attempt
is counted as a successful build.

## Actual visual inspection

Root rendered `build_round0_03/main.pdf` with
`pdftoppm -r 105 -png ... views_round0/page` and actually opened all seven
images, pages 1–3 together and 4–7 together. Checked: anonymous front
matter and literal equation; certificate domains and theorem breaks;
role-transition table and seed formula; full source-string table;
all eight matrices and norm exponents; mixed/equality branches and scope;
four references and their DOI/URL rendering. No cropped equation/table,
overlap, unreadable label or missing glyph was observed. Page 7 contains
references only and is intentionally sparsely filled. No artificial
compression removed a proof to reduce the page count.

| Page | Actual viewed PNG SHA-256 |
|---|---|
| 1 | ae0bc555f8857f08f53d4246d55ca0a48da25f409159df55a5fe2ddebc028410 |
| 2 | 2e3869358de479de69e13f83fd7c73c6306fd4045a37f0d2c3fe4e7e431869ff |
| 3 | b998823379bbba47d70aef9da25ecb3abd8703627a692a6dda4445b22717e9e9 |
| 4 | 769d9d58dab1430bf8d39359285dce4416e0e0824ebee54940c135f83cf622df |
| 5 | a539f2796c5d5c5ac4072ca9fcedd7e5a2c81d400df5f2d2f9a4ae72fe628ff7 |
| 6 | c383a5807d6ed22fd9fa12580cfbede229b296646ab4c5d7ea60b63bad23da4d |
| 7 | 4497cef8cab1e0f2ec938cb8fb8a58a7c9d4cc187e19e7ad25b86cd372514b14 |

These hashes pin images that were actually viewed; hashes or PNG existence
alone are not visual review. The fourth PDF is raw-identical, so the same
page inspection applies. This is author-level Round0 build/view evidence,
not manuscript A/B or either post-review terminal build. HOLD_EXTERNAL.
