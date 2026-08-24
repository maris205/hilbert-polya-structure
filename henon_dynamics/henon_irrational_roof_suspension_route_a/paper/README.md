# C130 paper artifacts

- `main.tex`: final source after two review/fix rounds.
- `main_round0_original.pdf`: baseline draft.
- `main_round1.pdf`: convergence and sector/orbit boundary revision.
- `main_round2.pdf`: final nonperiodicity and Route-A boundary revision.
- `main.pdf`: byte-identical to `main_round2.pdf`.
- `COMPILE_REPORT.md`: deterministic build, font, warning, and visual audit.

Build with fixed metadata:

```bash
SOURCE_DATE_EPOCH=1787529600 TZ=UTC latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The build auxiliaries are intentionally excluded from the release manifest and
removed after the final audit.
