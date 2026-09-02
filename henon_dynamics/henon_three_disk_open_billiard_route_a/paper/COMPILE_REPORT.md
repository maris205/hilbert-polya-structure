# Compile report

Engine: LuaLaTeX.  Each revision was compiled for two passes in each of two
isolated directories with `SOURCE_DATE_EPOCH=1788307200`,
`FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The two fresh builds of each round were
byte-identical to one another and to the archived PDF.

| Round | Pages | Embedded/subset font rows | SHA-256 |
|---|---:|---:|---|
| 0 original | 3 | 20 | `b3ca978ef07c70e038fac52d960970b9e1e728038295082a963b9c0cd4490965` |
| 1 proof-hardened | 3 | 20 | `e94f2d1c50fb73ec9292e33dbcaaf7ffaa88f9a9dba04db89850965cb4430921` |
| 2 audit-hardened | 4 | 21 | `a8d7f4c1a0aa4b2bca95435348e6305c942cf226f3201157d8a2e0f8105606d8` |

The three hashes are distinct, and `paper/main.pdf` is byte-identical to
`paper/main_round2.pdf`.  A settled warning regex found no LaTeX/package
warning, overfull/underfull box, undefined citation/reference, rerun request,
or missing character.  Poppler reported every font embedded and subset.
Raster inspection covered all 10 pages and found no clipping, collision,
blank-page defect, or unreadable table/equation.
