# P214 Review A source-only build grant request

NOT GRANTED / NOT EXECUTED. Root has accepted A initial DATA, canonical and
strict pair. The only live TeX delta is the accepted abstract terminology
change fixed by `SOURCE_EXPECTED.sha256`; all other eight source files equal
Round0. Output must be a new absent tree
`docs/papers211_215_sequence/reviews/p214_a/build01`.

Requested one-use operation: an ordinary staged source-only build copying
exactly the nine pinned sources into `build01/source_only`, then running
`pdflatex -no-shell-escape`, `bibtex`, and two further identical pdflatex
passes under the already accepted P214 ordinary build policy. It must capture
complete commands, stdout/stderr/native statuses, pre/post source and runtime
keys, pass-by-pass products, ordered FLS, final AUX/BBL/BLG/LOG/PDF, pdfinfo,
pdffonts, layout text, diagnostics, and PNG rendering of every actual page.

Before grant, root must bind current runtime/configuration inputs, verify the
fresh output parent and absence of the exact output tree (including dangling
links), read the complete chosen build recipe, and bind these three science
receipts plus the accepted delta. No old grant may be reused. No retry,
cleanup, PDF adoption, Round1, B or terminal-build credit is authorized.
OWNER_AMBER / HOLD_EXTERNAL.
