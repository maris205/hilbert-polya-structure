# C63 compilation report

- **Status:** SUCCESS
- **PDF:** `paper/main.pdf`
- **Pages:** 5 total; the main body ends on page 4 and references begin on
  page 5.
- **Undefined references:** 0
- **Undefined citations:** 0
- **Residual `[VERIFY]`, TODO, or FIXME markers:** 0
- **PDF size:** 232,461 bytes
- **Scope audit:** `NO_BAD_EULER_OR_ROOT_NUMBER` is explicit in the abstract,
  body, and nonclaim sections.

Build command:

```text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The bibliography contains only the three cited entries.  `pdftotext` and a
first-page raster inspection were used for the post-build check.
