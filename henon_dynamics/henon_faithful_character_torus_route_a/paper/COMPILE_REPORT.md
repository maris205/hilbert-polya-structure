# C134 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `14389b9dee189cedd74d185c24660d5002bb095b1747f853b7fbf2c6f69f06e5`
- PDF: `paper/main.pdf`
- PDF SHA-256: `404b2618ff7e51c6018a7b9c007b0d683dd3ade8ac6af0484f3f782692d651d5`
- Pages: 2
- File size: 311410 bytes
- Engine: pdfTeX 1.40.22
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787529600`, `TZ=UTC`

## Improvement artifacts

- Round 0: `84e5d1eb91433d3ad2f751c3b8169dfb17eabc3250fd5fe267e4cf66fd26c8ca`
- Round 1: `751171724c399735be658f1f0d5c47343ac988a7406773f165300944301f1b7d`
- Round 2/final: `404b2618ff7e51c6018a7b9c007b0d683dd3ade8ac6af0484f3f782692d651d5`

## Verification

Two fresh isolated two-pass builds have SHA-256
`404b2618ff7e51c6018a7b9c007b0d683dd3ade8ac6af0484f3f782692d651d5`
and are byte-identical to each other, the checked-in final PDF, and
`main_round2.pdf`.

The isolated logs contain no LaTeX/package warning, overfull or underfull box,
undefined reference or citation, or multiply-defined label.  `pdffonts`
reports `emb=yes` for every font.  Both pages were rendered at 120 dpi and
visually inspected: there is no clipping, collision, truncation, unintended
blank page, or broken formula/table layout.
