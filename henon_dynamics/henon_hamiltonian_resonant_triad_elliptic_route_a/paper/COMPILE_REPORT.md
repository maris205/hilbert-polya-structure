# Compile report

All rounds were compiled with LuaLaTeX twice in each of two fresh directories under `SOURCE_DATE_EPOCH=1788393600`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.  Each pair was byte-identical and equals the checked-in PDF.

| round | pages | font rows | SHA-256 |
|---:|---:|---:|---|
| 0 | 2 | 13 | `37c8032ed49567157bd882a3cb5145c89958c45c37f8ccdaa14c03ebc4db225e` |
| 1 | 3 | 13 | `18512e3cdb2e0441448de19380bdaffc8d7a06c0b12aa9984d1d920f9c20172c` |
| 2 | 3 | 13 | `9872da46013d60d25a0ccbcb94d993fd1241d123620440240f4b7c55bbea2432` |

`main.pdf` is byte-identical to round 2.  Settled logs contain no LaTeX/package warning, overfull/underfull box, undefined reference/citation, rerun request, or missing-character event.  All font rows are embedded and subset.  `pdftotext -layout` contains no forbidden control byte or drafting/TeX-garbage sentinel, and all eight pages across the three rounds rasterize successfully.  The three final pages were also inspected visually: equations, margins, page breaks, references, and footer placement are clean.
