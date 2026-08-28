# Build record — P95

## Environment

- LaTeX engine: `pdfTeX 3.141592653-2.6-1.40.22`
- BibTeX: `0.99d`
- TeX Live: 2022/Debian
- Python: `3.12.3`
- `latexmk`: unavailable; the explicit four-stage fallback was used
- Final build date: 2026-08-28 UTC

## Reproduction commands

From this directory, run:

```text
python3 code/verify_no_repeat.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Final result

- Exact control: **PASS, 5,031 assertions**
- Independent literal enumeration: **99,058 cyclic words**
- Compilation: **SUCCESS** through all four stages
- Artifact: `main.pdf`
- Pages: **4**
- Size: **289,151 bytes**
- SHA-256:
  `c783ead4bd43089c836079dcaf361c6ba0802ec2b084dfd14441db96f895823b`
- Undefined references: **0**
- Undefined citations: **0**
- LaTeX/package warnings: **0**
- Overfull boxes: **0**
- Underfull boxes: **0**
- Fonts: **23/23 embedded, subset, and Unicode-mapped**
- Extracted-text anomaly scan: **PASS**

All four pages were rasterized at 144 dpi and inspected individually. The
title, formulas, theorem statements, return-law derivation, and references
remain inside the page area with no clipping, collision, or unintended blank
page. See `FINAL_QA.md` for the page ledger and `SHA256SUMS` for the sealed
package manifest.

This build is approved for the internal theorem package only. Public posting,
submission, author contact, and priority language remain **HOLD**.
