# C320 compile report

All rounds were compiled with LuaLaTeX, two passes per fresh build,
`SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
The release gate rebuilds every round twice in isolated directories and
requires both byte streams to equal the checked-in artifact.

| round | pages | bytes | embedded subset font rows | SHA-256 |
|---:|---:|---:|---:|---|
| 0 | 2 | 112967 | 17 | `4c898771ff034436adb5c632ea137a1ef724a784861df624a68198f107f75bd4` |
| 1 | 2 | 125058 | 17 | `59a2dfde55f43e69eaf0893e7b80228d46f95f5304292592ea2404212fa9d599` |
| 2 | 3 | 141265 | 18 | `9b84aca69f8dcb7bf92887f8eedb599d3c080764da1cfa475f887e9dfe99358b` |

`main.pdf` is byte-identical to round 2.  All final logs are free of LaTeX
and package warnings, overfull/underfull boxes, undefined references or
citations, rerun requests, and missing characters.  Every page rasterizes;
all fonts are embedded and subset.
