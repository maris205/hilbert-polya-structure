# C168 manuscript build

Compile `main.tex` with LuaLaTeX under the fixed environment

```bash
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The release preserves three content-distinct snapshots: round 0 establishes
the spectrum/secular/phase theorem, round 1 adds the joint mixed-transform
limit, and round 2 adds torsion/antiunitary controls and hostile boundaries.
The final `main.pdf` is byte-identical to `main_round2.pdf`.  Full build and
visual checks are recorded in `COMPILE_REPORT.md`.
