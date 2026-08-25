# C147 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `b3a1a175444f03a1edfa071e43212d3f60a2dc2c9e29b1bd598494c45da402da`
- PDF: `paper/main.pdf`
- PDF SHA-256: `d3468d9cb6c2b35fa4034042c388ea1e8e2f6c36e76d9cc5e0b744c073895a1b`
- Pages: 2
- File size: 267,501 bytes
- Engine: pdfTeX 1.40.22
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, `TZ=UTC`

## Retained revisions

- Round 0: `2f8bd1b21f171803d4f1166ad027bebf4b8904626e0d38a657306a6cd196b5b3`
- Round 1: `744b72419c591cc8aa4fbeccf17445867b5c0ec9df7757f7e4768fb14fa3c99a`
- Round 2/final: `d3468d9cb6c2b35fa4034042c388ea1e8e2f6c36e76d9cc5e0b744c073895a1b`

## Verification

Two fresh isolated `latexmk` builds at the fixed epoch produced
`d3468d9cb6c2b35fa4034042c388ea1e8e2f6c36e76d9cc5e0b744c073895a1b`;
both are byte-identical to one another, `main_round2.pdf`, and `main.pdf`.
Both isolated logs contain no LaTeX/package warning, overfull or underfull box,
undefined reference/citation, multiply defined label, or badness report.
`pdffonts` reports `emb=yes` for every font.  `pdfinfo`, `pdftotext`, and
`pdftoppm` read the artifact successfully; extracted text contains no
unresolved marker.

Both pages were rendered at 120 dpi and visually inspected.  There is no
clipping, collision, truncation, broken equation layout, unintended blank
page, or unreadable text.
