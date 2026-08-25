# C148 compilation report

## Final artifact

- Status: SUCCESS
- Source: `paper/main.tex`
- PDF: `paper/main.pdf`
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`
- Engine: pdfLaTeX via latexmk
- Pages: 2
- Bytes: 376,195
- SHA-256: `7d74eb952880972d2d73a87e32eb69bbcdd65f430c19aa1ab168bc1e3548dd89`
- `main_round2.pdf`: byte-identical to `main.pdf`

## Build command

```text
SOURCE_DATE_EPOCH=1787616000 FORCE_SOURCE_DATE=1 TZ=UTC \
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final source was copied into two fresh `/tmp/c148-final-*` directories and
built with the same command.  Both independent build PDFs and the checked
release PDF had SHA-256
`7d74eb952880972d2d73a87e32eb69bbcdd65f430c19aa1ab168bc1e3548dd89`.

## Automated checks

- LaTeX errors: 0
- warnings: 0
- overfull boxes: 0
- underfull boxes: 0
- undefined references: 0
- undefined citations: 0
- multiply defined labels: 0
- literal source-token scan (`qquad`, `??`): clean
- `pdffonts`: every listed font is embedded and subset
- `pdfinfo`: two pages, valid 376,195-byte PDF
- `pdftotext`: successful extraction of both pages

## Visual inspection

Both pages were rasterized at 144 dpi and inspected.  The title, abstract,
theorem, all eight numbered displays, coefficient table, controls, Route-A
verdict, and boundary are legible.  There is no clipping, collision, truncated
line, broken glyph, unexpected token, or blank page.
