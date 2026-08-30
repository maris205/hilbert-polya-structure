# C247 compile report

The three revision artifacts were compiled in two independent fresh trees,
with two LuaLaTeX passes per tree, `TZ=UTC`,
`SOURCE_DATE_EPOCH=1788048000`, and `FORCE_SOURCE_DATE=1`.  Each A/B pair was
byte-identical, and the three revision hashes are distinct.  The final
`main.pdf` is a byte-identical copy of `main_round2.pdf`.

| artifact | SHA-256 | pages | embedded/subset font entries |
|---|---|---:|---:|
| `main_round0_original.pdf` | `4a0a42058e8464ba748155f2fea67335c8d149bfa518a713adb77f537f011b52` | 2 | 22 |
| `main_round1.pdf` | `c00484fe48a4f8898a945ffe3cd6ca9c7991459b3c190ad8a7a1450cc4d5e6ef` | 2 | 22 |
| `main_round2.pdf` | `e5b63849bd252b3922268016ba378650123f9b71d85a995675700f64ddeef8c1` | 2 | 23 |
| `main.pdf` (copy of round 2) | `e5b63849bd252b3922268016ba378650123f9b71d85a995675700f64ddeef8c1` | 2 | 23 |

`pdffonts` reports `emb=yes` and `sub=yes` for every entry in every final
artifact.  On each fresh tree the first pass emits only the standard
undefined-reference/rerun notices (two rerun notices and five warnings in
the captured log); the second pass is clean: no undefined references,
overfull/underfull boxes, multiply-defined labels, or fatal errors.  `pdfinfo`
confirms two pages and `pdftotext`/visual inspection confirms the map,
primitive classification, caustic/action formulas, clean kernel, merged
diameter, one-sided grazing, Dirichlet/Neumann limitation, route tuple, and
scope boundary.  Build sidecars remain in the temporary trees and are not
part of the package.
