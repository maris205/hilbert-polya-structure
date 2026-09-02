# Compile report

Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).  Every round was compiled
twice in each of two fresh temporary directories with
`SOURCE_DATE_EPOCH=1788307200`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  The two
fresh products and the archived product were byte-identical.

| Round | Pages | Embedded/subset font rows | Bytes | SHA-256 |
|---|---:|---:|---:|---|
| original (0) | 2 | 23 | 166140 | `a11bf5746fc2a2056754139143d5abde3ee4f56b56c287c923ce6768a3d0669f` |
| improvement 1 | 3 | 26 | 196386 | `8cd42fe5a6b46792c7a57b9e372a398a0806dd6a6931ec887a28ca99f84055c2` |
| improvement 2 | 3 | 27 | 207849 | `f09a3fc6ee5f1a2c0954d7d4d7db11d98f01cfc7741e9c82a0a8fb98f92ce872` |

All three hashes are distinct.  The second-pass logs contain no LaTeX/package,
layout, undefined-reference/citation, rerun, or missing-character warnings.
Poppler read and rasterized every page.  Every font row reports both embedded
and subset `yes`.

`paper/main.pdf` is byte-identical to `paper/main_round2.pdf` and has SHA-256
`f09a3fc6ee5f1a2c0954d7d4d7db11d98f01cfc7741e9c82a0a8fb98f92ce872`.
