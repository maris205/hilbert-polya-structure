# Manuscript builds

`main.tex` is a deterministic three-round source.  Define `\CRevisionRound` as 0, 1, or 2 before input:

- round 0: positive-OBC algebraic core;
- round 1: canonical left/right modes, skin-density distinction, conditioning, propagation, and resolvent;
- round 2/final: PBC, all degenerate faces, evidence, Route-A scope, and AI-use disclosure.

All archived PDFs are built twice in fresh temporary directories with LuaLaTeX, `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  `main.pdf` is byte-identical to `main_round2.pdf`.
