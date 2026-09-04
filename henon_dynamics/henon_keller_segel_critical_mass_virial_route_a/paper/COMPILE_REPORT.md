# Compile report: HCS-C363

All revisions are compiled from `main.tex` with LuaLaTeX at fixed epoch
`1788480000`, and each checked PDF must equal two independent fresh two-pass
builds.

- Round 0: 2 pages, 18 font rows, SHA-256
  `7805d8a4b2f83eec0b89f389e9e8bf541d9b77be3ce07d4c580d9e96ef187150`;
- Round 1: 2 pages, 18 font rows, SHA-256
  `8589f9a3e85ad4a7f4515a34d42754ca37baf56c6c7e1774dba07feeef82a75c`;
- Round 2/final: 3 pages, 18 font rows, SHA-256
  `e41913ba13b6dfe9a0b0911b00e86b3602f7d5cdf7e94ca99041e423b3cd391a`.

The release gate requires three distinct revision digests,
`main.pdf == main_round2.pdf`, settled warning-free logs, no overfull or
underfull boxes, no undefined references or missing characters, embedded and
subset fonts, clean UTF-8 extracted text, and successful rasterization of
every page.  The manifest records exact byte and raster receipts.
