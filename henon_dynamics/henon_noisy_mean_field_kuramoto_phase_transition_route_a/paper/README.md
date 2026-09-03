# Paper artifacts

- `main.tex` is the single revision-parameterized source.
- `main_round0_original.pdf` contains flow, energy, and stationary-flux closure.
- `main_round1.pdf` adds the strict Turán/threshold and full Fourier proof.
- `main_round2.pdf` adds critical asymptotics, evidence, boundaries, sources, and Route-A closure.
- `main.pdf` is byte-identical to round 2.

Each round is compiled twice in a fresh directory with LuaLaTeX and `SOURCE_DATE_EPOCH=1788393600`. The release gate verifies deterministic bytes, settled logs, embedded/subset fonts, extracted-text sentinels, and per-page rasterization.
