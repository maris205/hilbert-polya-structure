# C163 paper build

The release manuscript is `main.pdf`; `main.tex` is the final source.
Three preserved stages record the theorem draft, mathematical strengthening,
and hostile-scope/reproducibility pass:

- `main_round0_original.pdf`
- `main_round1.pdf`
- `main_round2.pdf`

Rebuild with LuaLaTeX under the frozen environment:

```bash
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -lualatex -interaction=nonstopmode -halt-on-error main.tex
```

The final build is two pages, warning-free, uses embedded/subsetted fonts, and
is byte-identical across two clean fixed-epoch builds.  See
`COMPILE_REPORT.md` for audit details.
