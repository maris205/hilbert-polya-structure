# C304 deterministic compile report

- Engine: LuaLaTeX; two settled passes per build.
- Environment: `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- Each of the three round variants is rebuilt in two fresh isolated
  directories; both outputs must be byte-identical to the archived PDF.
- Round 0: 2 pages, 24 embedded/subset font rows,
  SHA-256 `5bd10d6e78d18bbdeeffe967329a80bb7e896ab13bba9d2ebec60149505752b1`.
- Round 1: 2 pages, 25 embedded/subset font rows,
  SHA-256 `6b5ed469f5a8bda8113fd3ea7a8444fdfb2f7f6597331ed8fb0ae25afa6370fe`.
- Round 2/final: 3 pages, 26 embedded/subset font rows,
  SHA-256 `9d9525ab50369f110dbfd0a98ff3f153b7c6c146b3c0facfe0f1f2ac9f2b3c47`.
- `paper/main.pdf` is the byte-identical final alias of
  `paper/main_round2.pdf`.
- Settled logs contain no matched LaTeX/package, overfull/underfull,
  undefined-reference/citation, rerun, or missing-character warning.
- All final pages rasterize successfully, and PDF text sentinels are present.

The release script enforces these values and records fresh-build hashes and
raster byte sizes in the closed manifest.
