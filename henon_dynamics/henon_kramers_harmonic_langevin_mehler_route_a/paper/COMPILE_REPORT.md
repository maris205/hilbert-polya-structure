# C237 compile report

Build date: 2026-08-29.  Each round was compiled in a fresh temporary
directory with two passes of LuaLaTeX:

```text
SOURCE_DATE_EPOCH=1787875200 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C
lualatex -interaction=nonstopmode -halt-on-error main.tex
```

Round 0 is the initial compact theorem, round 1 adds the explicit
controllability/boundary discussion, and round 2 is the final critical-rate,
scope, and row-semantic-audit revision.  The second pass of every round exits
cleanly with **no layout/reference warnings** (and no overfull or underfull
boxes).  The revised round-2 source was independently built twice in fresh
temporary trees; both builds produced the same SHA-256.  `main.pdf` is copied
from round 2.

| artifact | pages | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 2 | `4c2fdb942f4b72c36691ed7ee2ee0057b8c98508034dd4e79e7070b0cfb732cb` |
| `main_round1.pdf` | 2 | `002e7c2610732a97b96fa338c35def16dcdc34a8a08d547fa9904dffc852383d` |
| `main_round2.pdf` | 2 | `cc6a5969a7dd5b333097565b231f5142c0282d71739095bffc55616bdf9783ab` |
| `main.pdf` (round 2 copy) | 2 | `cc6a5969a7dd5b333097565b231f5142c0282d71739095bffc55616bdf9783ab` |

`pdfinfo` reports an unencrypted A4 two-page PDF.  `pdffonts` reports embedded subset fonts
(Latin Modern text and math).  A `pdftotext` scan confirms the
all-damping, Mehler, Gibbs, Kalman, critical-damping, spectral-abscissa,
`ROUTE_A_REJECTED`, `A4_FORMAL_HINT`, scope, 411-assertion/32-mutation
audit-count and non-peer-review phrases.  Temporary `.aux`, `.log`, `.out` and
other build sidecars remain outside this package and are excluded from the
manifest.
