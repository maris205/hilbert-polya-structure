# C186 paper build

The final source is `main.tex`. Build with LuaLaTeX under a fixed epoch:

```bash
SOURCE_DATE_EPOCH=1787702400 FORCE_SOURCE_DATE=1 lualatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1787702400 FORCE_SOURCE_DATE=1 lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The round archives are produced from the same source with
`\CRevisionRound` set to 0, 1, and 2; each setting changes a substantive
revision-focus paragraph. Round 2 is byte-identical to `main.pdf`.

Determinism, fonts, warnings, page count, and rendered inspection are recorded
in `COMPILE_REPORT.md`. Internal drafting rounds are not external peer review.
