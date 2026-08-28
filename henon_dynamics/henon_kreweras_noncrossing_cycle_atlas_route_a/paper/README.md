# Manuscript build

`main.tex` is compiled with LuaLaTeX in two fresh fixed-epoch passes per round.
`main_round0_original.pdf`,
`main_round1.pdf`, and `main_round2.pdf` are retained as immutable round
artifacts; `main.pdf` is byte-identical to round 2 after the final compile.
The paper is a source-derived theorem synthesis and states all low-dimensional
clock boundaries and the no-arithmetic scope firewall.
