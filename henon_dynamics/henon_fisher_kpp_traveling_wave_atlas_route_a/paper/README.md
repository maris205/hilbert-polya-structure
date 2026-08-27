# C202 paper build

`main.tex` is the final round-2 source.  The three revision artifacts are
built by defining `\CRevisionRound` as 0, 1 and 2.  LuaLaTeX is run twice at a
fixed source epoch; final `main.pdf` must be byte-identical to
`main_round2.pdf` and to two fresh-directory rebuilds.

The manuscript is a compact independent theorem paper with English and
Chinese abstracts, proof, counter-regimes, declarations and exact source
locators.  No external review or score is claimed.
