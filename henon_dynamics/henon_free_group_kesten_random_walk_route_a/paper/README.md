# Paper build

`main.tex` is a single deterministic LuaLaTeX source controlled by `\CRevisionRound`.

- Round 0: root spectrum, radial chain, exact even returns.
- Round 1: adds whole-space pure absolute continuity and first returns.
- Round 2: adds escape laws, rank-one boundary, evidence and Route-A closure.

The release gate builds every round twice in fresh directories with `SOURCE_DATE_EPOCH=1788393600`.  `main.pdf` must be byte-identical to `main_round2.pdf`.
