# Paper build

`main.tex` is the release source. It defaults to revision round 2. The macro `\CRevisionRound` selects the archived substantive state: round 0 closes cycles and zeta; round 1 adds the full transient tree and boundary atlas; round 2 adds the complete Koopman Jordan atlas, executable receipts, and Route-A boundary.

Build with LuaLaTeX under `SOURCE_DATE_EPOCH=1788048000`. Each round is compiled twice in two fresh directories and the resulting bytes must agree. `main.pdf` is byte-identical to `main_round2.pdf`.
