# Compile report

LuaLaTeX built all three conditional revisions twice from clean temporary directories with `SOURCE_DATE_EPOCH=1788393600`; the paired bytes were identical and the final logs contained no layout, citation, reference, rerun, or missing-character warnings.

- Round 0: 2 pages, 128,208 bytes, SHA-256 `dea6caf29d13b75effd2caed8a62d73cb30fc5b0877cbeaeb9ffadc79bf4a582`.
- Round 1: 3 pages, 136,021 bytes, SHA-256 `e47dcca6d65014aeaca742854ef32b28f439c6a28aeea60a7dab08c6d93890a2`.
- Round 2/final: 3 pages, 145,355 bytes, SHA-256 `fc60a7ad8bc10257f9d9e99502cfa2ec9dabaca4981281c55e5af6e12bee9f85`.

The three revision hashes are distinct; `main.pdf` is byte-identical to round 2.  All fonts are embedded and subset, extracted text passes the draft-token/control-character audit, and every page rasterizes nontrivially.
