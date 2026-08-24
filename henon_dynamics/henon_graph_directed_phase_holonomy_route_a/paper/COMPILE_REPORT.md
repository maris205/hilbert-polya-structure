# C129 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `130d7fd72ab001e5185abf77aca789dec2f80b3c59ff900e5a7b67c7febcaeb0`
- PDF: `paper/main.pdf`
- PDF SHA-256: `c3e4fc5b46116583dea7f1dff2c084e0ea348adff269b4484f3579d36e86ae35`
- Pages: 2
- File size: 285327 bytes
- Engine: pdfTeX 1.40.22 via latexmk 4.76
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787529600`, `TZ=UTC`

## Improvement artifacts

- Round 0: `be2fad2716ec5be544202d0b7e889151b6c1b06ff7a203856826fd1e3b1493e9`
- Round 1: `f0ea2c28381c18438d925707916c535e16701e2d2bd452883407288ddd3142b3`
- Round 2/final: `c3e4fc5b46116583dea7f1dff2c084e0ea348adff269b4484f3579d36e86ae35`

## Verification

Two fresh isolated two-pass builds have SHA-256
`c3e4fc5b46116583dea7f1dff2c084e0ea348adff269b4484f3579d36e86ae35`
and are byte-identical to each other and the checked-in final PDF.

The final and isolated logs contain no LaTeX/package warning, overfull or
underfull box, undefined reference, multiply-defined label, or citation
warning. `pdffonts` reports `emb=yes` for every font. Both rendered pages were
inspected at 120 dpi: there is no clipping, collision, truncation, unintended
blank page, or broken formula/table layout.

The final PDF is byte-identical to `main_round2.pdf`; all three improvement
artifacts are retained.
