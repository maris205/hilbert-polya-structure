# Compile report

Engine: LuaLaTeX.  Each revision was compiled for exactly two passes in each
of two isolated directories with `SOURCE_DATE_EPOCH=1788307200`,
`FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The two fresh builds of each round were
byte-identical to one another and to the archived PDF.

| Round | Pages | Embedded/subset font rows | SHA-256 |
|---|---:|---:|---|
| 0 original | 3 | 21 | `0d8d6e35da94f740b9246155b3adaf44b2769700dd352c89f8bc8f6b32b388db` |
| 1 proof-hardened | 4 | 22 | `b33a6ebe333284632d72bd20ccaec7f065f32d4c7a40dfa164d632147449dde7` |
| 2 audit-hardened | 4 | 23 | `37c2512b70f1042b18b3fc89282fa58f82d65897e9e4c6aab6f8199957477295` |

The three hashes are distinct, and `paper/main.pdf` is byte-identical to
`paper/main_round2.pdf`.  A settled warning regex found no LaTeX/package
warning, overfull/underfull box, undefined citation/reference, rerun request,
or missing character.  Poppler reported every font embedded and subset.
Raster and visual inspection covered all 11 archived pages and found no
clipping, collision, blank-page defect, or unreadable equation.
