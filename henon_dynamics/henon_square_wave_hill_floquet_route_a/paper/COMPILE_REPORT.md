# C262 compile report

All three revision sources were compiled with LuaLaTeX on 2026-08-31 UTC.
Each round was built twice in independent fresh directories with
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`; every
pair was byte-identical.  A fixed LuaTeX trailer ID removes temporary-path
variation.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `ef3a0bbdc96b613011d4f72515132727ed69829c81d4c67f5d846a44abe51181` | 2 |
| `main_round1.pdf` | `ff8cd4acc356674fd0d0d83851931268923360eda4f28d40d7cffd8bcb59f92c` | 2 |
| `main_round2.pdf` | `d3b6743904caea88860c38635602a3395fabfdd795b326d12cdb1b82cd604cb9` | 2 |
| `main.pdf` (copy of round 2) | `d3b6743904caea88860c38635602a3395fabfdd795b326d12cdb1b82cd604cb9` | 2 |

The final PDF has 21 embedded and subsetted Latin Modern/AMS font entries;
none is unembedded.  The settled second-pass logs have no overfull or
underfull box, undefined reference/citation, multiply-defined label, package
warning, or rerun request.  Text extraction contains the Hill equation,
Floquet discriminant, scalar/Jordan split, Chebyshev convention, all-sign
faces, Route-A tuple, scope literal, and explicit no-arithmetic stop.  Visual
raster inspection of both pages found no clipping, collision, malformed
formula, or unreadable table.

The final integrity pass added explicit manuscript anchors for both
registered historical sources.  Two new fresh-directory builds were
byte-identical, warning-free, and visually rechecked; the historical round-0
and round-1 artifacts were not rewritten.

All build sidecars remain in temporary directories and are excluded from the
release payload.
