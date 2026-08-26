# Paper build

Compile with LuaLaTeX through `latexmk` under a fixed source-date epoch:

```bash
SOURCE_DATE_EPOCH=1787760000 TZ=UTC latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The final `main.pdf` is byte-identical to `main_round2.pdf`. The three round PDFs are intentionally content-distinct. Transient TeX files are excluded from the release manifest and removed after validation.
