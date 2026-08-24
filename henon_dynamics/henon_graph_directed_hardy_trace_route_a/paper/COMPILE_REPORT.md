# C124 compile report

## Final artifact

- Source: `paper/main.tex`
- Source SHA-256: `5ff83142b0c84d97d98811260b979e84a89a403c48dd58b69b98c5a565d84b63`
- PDF: `paper/main.pdf`
- PDF SHA-256: `72b54fd5a91c8d23b4a2939fa1a57728ae488a37c47e7e2f67ad87edc127a9a1`
- Pages: 2
- Engine: pdfTeX 1.40.22 via latexmk 4.76
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787529600`, `TZ=UTC`

## Verification

Two fresh isolated two-pass builds have SHA-256
`72b54fd5a91c8d23b4a2939fa1a57728ae488a37c47e7e2f67ad87edc127a9a1`
and are byte-identical to each other and to the checked-in final PDF.

The final logs contain no LaTeX/package warning, overfull or underfull box,
undefined reference, multiply-defined label, or citation warning. `pdffonts`
reports `emb=yes` for every font. Both rendered pages were inspected: no
clipping, collision, truncation, blank region, or broken formula/table layout
was found.

The final PDF is byte-identical to `main_round2.pdf`; round-zero and round-one
artifacts are retained separately as required by the paper-writing workflow.
