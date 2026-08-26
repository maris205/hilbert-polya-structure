# Paper build

Use LuaLaTeX under the frozen source-date epoch:

```bash
SOURCE_DATE_EPOCH=1787760000 TZ=UTC latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The saved round PDFs are content-distinct. The final `main.pdf` equals `main_round2.pdf`; temporary TeX files are removed before manifest closure.
