# C146 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `e4671846a768600c592075ab7860a15437e7b3b89391d9d826ade9c0b616bbea`
- PDF: `paper/main.pdf`
- PDF SHA-256: `8ee75e2e8e293cf3c65856d8c03056dcb52762d92629439170cdaa79e10c80c3`
- Pages: 2
- File size: 254,534 bytes
- Engine: pdfTeX 1.40.22
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`, `TZ=UTC`

## Retained revisions

- Round 0: `873cb632e5e1a1bacd08c787b0be8bfd8c0ddbf868d4fa72bebee3d850665cad`
- Round 1: `0f95051d9f87fbb7ddc7d263b94b0b150eddd8bc544e3bac6548d819941b65d0`
- Round 2/final: `8ee75e2e8e293cf3c65856d8c03056dcb52762d92629439170cdaa79e10c80c3`

## Verification

Two fresh isolated `latexmk` builds at the fixed epoch produced
`8ee75e2e8e293cf3c65856d8c03056dcb52762d92629439170cdaa79e10c80c3`;
both are byte-identical to one another, `main_round2.pdf`, and `main.pdf`.
Both isolated logs contain no LaTeX/package warning, overfull or underfull box,
undefined reference/citation, multiply defined label, or badness report.
`pdffonts` reports `emb=yes` for every font.  `pdfinfo`, `pdftotext`, and
`pdftoppm` read the artifact successfully; extracted text contains no
unresolved marker.

Both pages were rendered at 120 dpi and visually inspected.  There is no
clipping, collision, truncation, broken equation layout, unintended blank
page, or unreadable text.
