# Paper build

`main.tex` uses LuaLaTeX and a fixed revision macro `CRevisionRound`.
Round 0 contains the semigroup core, round 1 adds all dynamical boundaries,
and round 2 adds executable/Route-A closure. The released `main.pdf` is
byte-identical to `main_round2.pdf`. The released revision page counts are
2, 2, and 3.

Build with `SOURCE_DATE_EPOCH=1787788800` and keep `.aux`, `.log`, `.out`, and
other engine sidecars outside the 27-payload release ledger.
