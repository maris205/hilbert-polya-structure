# Paper artifacts

- `main.tex`: final source.  With no injected round flag it builds Round 2.
- `main_round0_original.pdf`: core source theorem, Smith order, and preliminary Route boundary.
- `main_round1.pdf`: exact multiplicities, global aggregation, and boundary closure added.
- `main_round2.pdf`: attribution, independent certificate, seven-mode integrity audit, and final Route verdict added.
- `main.pdf`: byte-identical copy of `main_round2.pdf`.
- `COMPILE_REPORT.md`: deterministic build, font, log, page, and visual audit.

The source supports content-distinct round builds with

```text
lualatex --jobname=main_round0_original '\def\RoundZero{1}\input{main.tex}'
lualatex --jobname=main_round1 '\def\RoundOne{1}\input{main.tex}'
lualatex main.tex
```

Every build uses two passes and fixed `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
