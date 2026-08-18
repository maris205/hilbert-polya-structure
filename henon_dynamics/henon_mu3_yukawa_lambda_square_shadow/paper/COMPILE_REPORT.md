# C62 compilation report

- **Status:** SUCCESS
- **PDF:** `paper/main.pdf`
- **Pages:** 3
- **Undefined references:** 0
- **Undefined citations:** 0
- **Residual `[VERIFY]` markers:** 0
- **Scope audit:** `NO_BAD_EULER_OR_ROOT_NUMBER` appears in the manuscript;
  arithmetic-field and local claims are explicitly excluded.

Build command:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The PDF is 197,775 bytes and was checked with `pdfinfo` and `pdftotext`.
