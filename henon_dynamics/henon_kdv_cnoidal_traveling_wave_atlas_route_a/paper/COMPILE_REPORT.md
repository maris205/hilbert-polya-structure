# C256 compile report

The three revision sources were compiled with LuaLaTeX on 2026-08-31 UTC.
Each round was built twice in independent fresh directories with
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`; every
pair was byte-identical.  A fixed LuaTeX trailer ID makes the result
independent of the temporary path.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `97656fc7eacc963301526437b0330ac66bdada25646088d43150f9a6e45472fe` | 2 |
| `main_round1.pdf` | `bc16c08cf29d101aad4a1f02cb92fe06e20e16ac059ba8e7163b983a1b956442` | 2 |
| `main_round2.pdf` | `803a7637889627a99cd962a97ad1798719424a33b6e9d6bdbcd828cb5b5d186e` | 3 |
| `main.pdf` (copy of round 2) | `803a7637889627a99cd962a97ad1798719424a33b6e9d6bdbcd828cb5b5d186e` | 3 |

The final PDF has 21 embedded and subsetted Latin Modern/AMS font entries;
none is unembedded.  The second pass has no overfull or underfull box,
undefined reference/citation, multiply-defined label, or package warning.
`pdftotext` contains the KdV equation, cnoidal and soliton theorem, Galilean
face, independent receipt, `A1_WEAK`, `ROUTE_A_REJECTED`, scope literal, and
explicit no-arithmetic boundary.  Visual raster inspection of all three final pages
found no clipping, collision, malformed equation, or unreadable table.

All build sidecars stay in temporary directories and are absent from the
release payload.
