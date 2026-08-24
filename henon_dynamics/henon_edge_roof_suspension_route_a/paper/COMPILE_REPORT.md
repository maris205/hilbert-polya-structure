# C135 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `4c09a486f9b30ebc31492740f576c91153715728ad696b88dde4f3354ea09646`
- PDF: `paper/main.pdf`
- PDF SHA-256: `0a0ab1a405e2fdec843d26a6fa1de81d74ce12768721dd21dcee29502882c808`
- Pages: 2
- File size: 310631 bytes
- Engine: pdfTeX 1.40.22
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787529600`, `TZ=UTC`

## Improvement artifacts

- Round 0: `b183a2c1d6235192dbfa27abd64c04b45f85f427ffe639e582b4068fb9144000`
- Round 1: `0f69e7f668e6d4bd3b5922a72937a4baad226c1b059f812df2495e8841b1a0a3`
- Round 2/final: `0a0ab1a405e2fdec843d26a6fa1de81d74ce12768721dd21dcee29502882c808`

## Verification

Two fresh isolated two-pass builds have SHA-256
`0a0ab1a405e2fdec843d26a6fa1de81d74ce12768721dd21dcee29502882c808`
and are byte-identical to each other, the checked-in final PDF, and
`main_round2.pdf`.

The isolated logs contain no LaTeX/package warning, overfull or underfull box,
undefined reference or citation, or multiply-defined label.  `pdffonts`
reports `emb=yes` for every font.  Both pages were rendered at 120 dpi and
visually inspected: there is no clipping, collision, truncation, unintended
blank page, or broken formula/table layout.
