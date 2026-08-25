# C139 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `359944eae1d852ab997908fa6cdaba79d5a559dffef4b696714599514e43c0d4`
- PDF: `paper/main.pdf`
- PDF SHA-256: `abd5a3ca4d98b181eb8bfe6c1fd30cc9728ca98510e4a021177a57b26dd493d5`
- Pages: 2
- File size: 323,670 bytes
- Engine: pdfTeX 1.40.22
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, `TZ=UTC`

## Retained revisions

- Round 0: `6b04104ab5d2e7ea1ff3d6cab245a38d60d6375a276ee7d03e8f8b45e6ea4e47`
- Round 1: `270ca5c48fbd8b87a438b338d71284f916edb5720559ee7737c39de7c027c4b5`
- Round 2/final: `abd5a3ca4d98b181eb8bfe6c1fd30cc9728ca98510e4a021177a57b26dd493d5`

## Verification

Two fresh isolated `latexmk` builds at the fixed epoch both produced
`abd5a3ca4d98b181eb8bfe6c1fd30cc9728ca98510e4a021177a57b26dd493d5`;
they are byte-identical to one another, `main_round2.pdf`, and `main.pdf`.
Both isolated logs contain no LaTeX/package warning, overfull or underfull box,
undefined reference/citation, or multiply defined label.  `pdffonts` reports
`emb=yes` for every font.  `pdfinfo`, `pdftotext`, and `pdftoppm` read the
artifact successfully; no unresolved marker appears in extracted text.

Both pages were rendered at 120 dpi and visually inspected.  There is no
clipping, collision, truncation, broken equation/table layout, unintended
blank page, or unreadable text.
