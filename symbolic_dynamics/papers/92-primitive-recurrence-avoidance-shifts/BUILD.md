# P92 Build Record

## Environment

- LaTeX engine: `pdfTeX 3.141592653-2.6-1.40.22`
- BibTeX: `0.99d`
- TeX Live: 2022/Debian
- Python: `3.12.3`
- `latexmk`: unavailable; the explicit four-stage fallback was used
- Final build date: 2026-08-28 UTC

## Reproduction commands

Run from `papers/92-primitive-recurrence-avoidance-shifts/`:

```text
python3 code/verify_primitive_avoidance.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Final result

- Exact control: **PASS, 258 assertions**
- Compilation: **SUCCESS** through all four stages
- Artifact: `main.pdf`
- Pages: **6**
- Size: **325,223 bytes**
- SHA-256:
  `a120a809a8e1f444563fbc9ca1e7432ffeda2836d14ab89297f5c360dabb0092`
- Undefined references: **0**
- Undefined citations: **0**
- LaTeX/package warnings: **0**
- Overfull boxes: **0**
- Underfull boxes: **0**
- Fonts: **24/24 embedded, subset, and Unicode-mapped**
- Extracted-text anomaly scan: **PASS**

All six pages were rasterized at 144 dpi and inspected individually. The
title, abstract, theorem boxes, long formulas, control table, hyperlinks, and
references remain inside the page area with no clipping, collision, or
unintended blank page. See `FINAL_QA.md` for the page ledger and
`SHA256SUMS` for the sealed package manifest.

This build is approved for the internal theorem package only. Public posting,
submission, author contact, and priority language remain **HOLD**.
