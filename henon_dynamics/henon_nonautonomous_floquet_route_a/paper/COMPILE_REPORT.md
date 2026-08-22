# C110 compile report

- Engine: `latexmk -pdf` / pdfTeX with `SOURCE_DATE_EPOCH=0`.
- Isolated build A: 2 pages, SHA-256
  `f1cd7c4e24c12bed43ed77b568802ce93f4f9de96c6e8247198ed42454711776`.
- Isolated build B: 2 pages, the identical SHA-256
  `f1cd7c4e24c12bed43ed77b568802ce93f4f9de96c6e8247198ed42454711776`.
- Checked-in `main.pdf`: the same SHA-256 and 2 pages.
- `pdffonts`: all listed fonts are embedded subsets.
- Layout scan: no `Overfull`, `Underfull`, undefined-reference, or
  multiply-defined-label diagnostics.

The three round snapshots (`main_round0_original.pdf`, `main_round1.pdf`, and
`main_round2.pdf`) are byte-identical to the final PDF.
