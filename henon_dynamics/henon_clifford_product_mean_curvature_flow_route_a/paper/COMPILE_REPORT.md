# C319 compile report

All rounds were compiled with LuaLaTeX, two passes per fresh build,
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
The release gate rebuilds every round twice in isolated directories and
requires both byte streams to equal the checked-in artifact.

| round | pages | bytes | embedded subset font rows | SHA-256 |
|---:|---:|---:|---:|---|
| 0 | 1 | 142237 | 20 | `a9d40b4e2b5ca8ea0794e8f5000b83e4d4d5bf1067e0fcda28f02685805e5b64` |
| 1 | 2 | 151619 | 21 | `517819ee4830055ac19edf6112ba05289c40638a735becb1b511378c6cf4102e` |
| 2 | 3 | 168397 | 22 | `9935c1106625dad7feb22437d5ae45eac9c3d74cc618d58d8372713596f39882` |

`main.pdf` is byte-identical to round 2.  All final logs are free of LaTeX
and package warnings, overfull/underfull boxes, undefined references or
citations, rerun requests, and missing characters.  Every page rasterizes;
all fonts are embedded and subset.
