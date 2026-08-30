# C244 manuscript build

'main.tex' is the source for three substantive revision rounds.  Round 0
freezes the cubic and critical-value split; round 1 adds root chambers and the
three quadratures; round 2 adds the global pole chart, corrected action
cross-check, and the matrix-column monodromy convention.  The final
'main.pdf' equals 'main_round2.pdf'.

Builds use LuaLaTeX with SOURCE_DATE_EPOCH=1788048000,
FORCE_SOURCE_DATE=1, and TZ=UTC, in two fresh temporary trees per round.
Auxiliary files never enter the package manifest.
