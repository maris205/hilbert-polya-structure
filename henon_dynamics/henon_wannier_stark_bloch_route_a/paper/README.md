# PDF build

Compile each revision twice in a fresh temporary directory with LuaLaTeX and
`SOURCE_DATE_EPOCH=1788048000`.  The revision command injects `\CRevisionRound` before loading `main.tex`.
Round 0 is the spectral/dynamical core, round 1 adds transport and degenerations, and round 2 adds the
operator-ideal theorem, evidence boundary, and Route-A decision.  `main.pdf` must equal round 2 byte for byte.
