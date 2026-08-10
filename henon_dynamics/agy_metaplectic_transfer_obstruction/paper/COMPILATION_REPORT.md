# C25 paper compilation report

## Material Passport

- Origin Skill: `paper-compile`
- Origin Mode: `validate`
- Origin Date: `2026-08-10T00:00:00Z`
- Verification Status: `VERIFIED`
- Version Label: `c25_paper_compile_v2`

## Result

- Status: `SUCCESS`
- Engine: `pdflatex` through `latexmk`
- PDF: `main.pdf`
- Total pages: 12
- Main body through conclusion: pages 1--11
- Bibliography begins on page 11; appendix: page 12
- PDF size: 297,890 bytes at the registered clean build
- PDF SHA-256: `882722cf1214c1a2305653d856dec066ad75ac173a7cff971792e6b9d66a4edc`
- Undefined references: 0
- Undefined citations: 0
- Overfull boxes: 0
- Unembedded fonts: 0
- `TODO` / `FIXME` / `XXX` / `[VERIFY]` markers: 0
- Orphan section files: 0

The title/abstract page, decoder theorem, scalar essential-norm proof, and
exact-certificate table received visual inspection after rasterization.
Hyperlinks are hidden for print cleanliness.  No missing glyph, clipped
table, or placeholder was observed.

Rebuild with:

```bash
latexmk -C
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
