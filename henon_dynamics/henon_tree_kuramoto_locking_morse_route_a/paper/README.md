# Paper artifacts

- `main.tex` is the settled round-2 source.
- `main_round0_original.pdf` is the frozen theorem skeleton.
- `main_round1.pdf` adds explicit reconstruction, branch distribution, and
  the degeneration ledger.
- `main_round2.pdf` adds the executable audit and full claim boundary.
- `main.pdf` is byte-identical to `main_round2.pdf`.

All PDF builds use LuaLaTeX, the fixed trailer ID in `main.tex`, and
`SOURCE_DATE_EPOCH=1788048000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
