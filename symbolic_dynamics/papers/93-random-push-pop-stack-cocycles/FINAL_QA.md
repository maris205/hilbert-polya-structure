# Final QA — P93

Freeze date: 2026-08-28 UTC  
Disposition: **internal GO / external HOLD**

## Mathematical and computational gate

- Two independent hostile-review passes completed. The second pass returned
  `REVISE`, and both mandatory proof repairs were implemented before freeze.
- `python3 code/verify_push_pop.py` passed **265,861 exact integer/rational
  assertions**.
- The five separately labelled floating diagnostics passed and remain
  excluded from the theorem-evidence count.
- The added endpoint layer checks `b=2,3,5`, `p=0,1`, and `0<=n<=20`
  against both direct propagation and the closed endpoint laws.

## Reproducible build gate

The final package was rebuilt in order:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

- Artifact: `main.pdf`
- Format: PDF 1.5, A4
- Pages: 7
- Size: 350,677 bytes
- SHA-256: `63afc0cc7da30743ec7e94b9b141a5668b98e9d56c4343f0c0ee38d894fe73f6`
- Final-log undefined citations/references: 0
- Final-log LaTeX warnings: 0
- Overfull/underfull boxes: 0/0

## PDF integrity and visual gate

- `pdffonts` reports 25/25 fonts embedded, subsetted, and Unicode-mapped.
- `pdftotext` completed successfully and produced 620 lines, 3,382 words,
  and 17,882 bytes of extractable text.
- All seven pages were rendered to PNG and inspected. No clipping,
  collision, missing glyph, broken display, anomalous margin, or blank page
  was found. The reference list is complete on page 7.
- Source/evidence placeholder scan found no `TODO`, `FIXME`, `TBD`, `XXX`,
  placeholder text, or unresolved citation marker.

## Freeze boundary

`SHA256SUMS` covers the manuscript source, bibliography, exact-control code,
the evidence/review/build/QA records, and the canonical PDF. Public posting,
submission, author contact, and absolute novelty or priority language remain
unauthorized.
