# C229 compilation report

Compiler: LuaLaTeX, two passes per revision, `SOURCE_DATE_EPOCH=1787875200`,
fresh isolated build directories.  Settled logs contain no warnings,
overfull/underfull boxes, undefined references, missing characters or errors.

| revision | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 2 | `78fe86692874515923a06e75369b473e0375ccf7a934822acf726fde7ccd4b71` |
| `main_round1.pdf` | 2 | `7b986fe7315ee3618baaf83c1541b5396a67a4de8f8ed97ca3aa7d4d23481fb4` |
| `main_round2.pdf` | 3 | `ccc5644b1c14415e6e7bd8bcd19265ab102dfd76fca0ac7b26ffe7a103b15088` |

`paper/main.pdf` is byte-identical to `main_round2.pdf`.  Fonts are embedded
and subset; all pages were rendered and visually inspected.  The final paper
contains the theorem, controls, audit counts, `ROUTE_A_REJECTED`, and the
`NO_BAD_EULER_OR_ROOT_NUMBER` declaration.
