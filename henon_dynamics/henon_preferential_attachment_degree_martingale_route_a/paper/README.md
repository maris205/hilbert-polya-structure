# Paper build

`main.tex` is a three-round source controlled by `\CRevisionRound`.

- round 0: convention and exact all-order factorial law;
- round 1: fixed-vertex martingale limit plus global `L2` degree profile;
- round 2: exact evidence, source/collision audit, and Route-A closure.

The release gate compiles each round twice from a clean temporary directory with LuaLaTeX and a fixed source epoch, requires byte identity, scans settled logs, checks embedded subset fonts and page rasterization, and requires `main.pdf` to equal the round-2 archive.
