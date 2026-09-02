# C305 deterministic compile report

- LuaLaTeX, two settled passes per build.
- Fixed environment: `SOURCE_DATE_EPOCH=1788393600`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Every round is rebuilt in two isolated directories and required to be
  byte-identical to its archive.
- Round 0: 2 pages, 20 embedded/subset font rows,
  SHA-256 `e4cb469251a2626bb8d0bdcda23cd9e00765092de4e9c88b26deb63b87cc4af1`.
- Round 1: 2 pages, 20 embedded/subset font rows,
  SHA-256 `321e68a9f67939550ed259b70c26242fc3ed011db08ebd210d0a3d1825fdb06a`.
- Round 2/final: 3 pages, 21 embedded/subset font rows,
  SHA-256 `26b69034b7cef082f01028a5c2c8b74c45d313aa1324ccdacfe434eae9bf6eea`.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- Settled logs contain no matched LaTeX/package, overfull/underfull,
  undefined-reference/citation, rerun, or missing-character warning.
- All final pages rasterize and all PDF text sentinels are present.

The release manifest records both fresh-build hashes, font rows, page counts,
and raster sizes.
