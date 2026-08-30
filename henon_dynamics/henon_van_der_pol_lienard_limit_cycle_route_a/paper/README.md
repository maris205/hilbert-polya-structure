# C249 manuscript build

`main.tex` is the source for three substantive revision rounds.  Round 0
freezes the model and sign faces; round 1 adds the energy/divergence/Floquet
identities and finite return receipt; round 2 adds the collision audit,
reproducibility gates, and explicit Route-A boundary.  The final `main.pdf`
equals `main_round2.pdf`.

Builds use LuaLaTeX in two independent fresh trees per round with
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
Auxiliary files are removed before manifest generation.
