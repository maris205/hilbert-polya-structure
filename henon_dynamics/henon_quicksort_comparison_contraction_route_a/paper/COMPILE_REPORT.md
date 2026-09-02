# Compile report — HCS-C302

Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).  Every round was compiled
twice in each of two fresh directories with `SOURCE_DATE_EPOCH=1788307200`,
`FORCE_SOURCE_DATE=1`, and `TZ=UTC`; both fresh products and the archive were
byte-identical.

| Round | Pages | Embedded/subset font rows | Bytes | SHA-256 |
|---|---:|---:|---:|---|
| original (0) | 2 | 17 | 110081 | `a623329732dd0ca43dd54c1f1798b58b3ee4820d019f981759dff25c1f96f397` |
| improvement 1 | 2 | 17 | 129658 | `a8f95799b46c71ea7c67f3bd66e5f011a95a13ac577b810186d6b457003c7a46` |
| improvement 2 | 3 | 23 | 176209 | `e28a494e10ffa2f67f724b7458264bab62d30db6868a2c0ee38e50b46d5921bc` |

All three hashes are distinct.  Both second-pass logs for every round are free
of LaTeX/package, layout, undefined-reference/citation, rerun, and
missing-character warnings.  Poppler reads and rasterizes every page.  Every
font row reports embedded and subset `yes`.

`paper/main.pdf` is byte-identical to `paper/main_round2.pdf`; both have
SHA-256 `e28a494e10ffa2f67f724b7458264bab62d30db6868a2c0ee38e50b46d5921bc`.
