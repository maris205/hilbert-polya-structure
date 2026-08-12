# Paper

`main.tex` is a standard article manuscript for the HCS-C33 Phase-3 exact
theorem.  It states the node/Hill--Kummer result, cites the generic mechanisms
as prior art, and preserves the fixed-period Route-A boundary.

Build with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`COMPILATION_REPORT.md` records the frozen PDF and log audit.
