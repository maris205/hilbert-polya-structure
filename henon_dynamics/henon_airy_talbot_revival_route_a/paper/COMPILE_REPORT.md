# C261 compile report

All three revision sources were compiled with LuaLaTeX on 2026-08-31 UTC.
Each round was built twice in independent fresh directories with
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`; every
pair was byte-identical.  A fixed LuaTeX trailer ID removes temporary-path
variation.

| artifact | SHA-256 | pages |
|---|---|---:|
| `main_round0_original.pdf` | `3ee130933d97763a0961db59f4e459f5b3b68d41ee2c0ce5085425eb4be96b8c` | 2 |
| `main_round1.pdf` | `1ee5ada298c0cea9d23ae6a65ff1ef54819bd66298639f0ffd738c8979bd96ba` | 2 |
| `main_round2.pdf` | `67090f077d783a12ba504dc43c91e144d88a214319121b462a0b895872e0ffbd` | 2 |
| `main.pdf` (copy of round 2) | `67090f077d783a12ba504dc43c91e144d88a214319121b462a0b895872e0ffbd` | 2 |

The final PDF has 23 embedded and subsetted Latin Modern/AMS font entries;
none is unembedded.  The settled second-pass logs have no overfull or
underfull box, undefined reference/citation, multiply-defined label, package
warning, or rerun request.  Text extraction contains the Airy equation,
cubic Talbot theorem, fixed-space and state-period laws, noncompact boundary,
Route-A tuple, scope literal, and explicit no-arithmetic stop.  Visual raster
inspection of both final pages found no clipping, collision, malformed
formula, or unreadable table.

After the final integrity pass corrected the author order of the second
reference and anchored both registered sources in the manuscript body, round
2 was rebuilt twice again in independent fresh directories.  Those two builds
were byte-identical, warning-free, and visually rechecked; the historical
round-0 and round-1 artifacts were not rewritten.

All build sidecars remain in temporary directories and are excluded from the
release payload.
