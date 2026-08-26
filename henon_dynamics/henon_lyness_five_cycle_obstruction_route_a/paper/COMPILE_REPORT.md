# C173 deterministic compile report

- Engine: LuaHBTeX / LuaLaTeX.
- Fixed build epoch: `SOURCE_DATE_EPOCH=1787702400` (2026-08-26 UTC).
- Final pages: 2, A4.
- Final file size: 176,454 bytes.
- Final PDF SHA-256:
  `74d495da262be5ee425e0a61772553809929249f63a7335d62ca9dc96d442570`.
- Final TeX SHA-256:
  `57d3a4c56ed861108c473ac9331c6d6a2995b902173f080d4616b3153c92935f`.

## Snapshot closure

| Snapshot | SHA-256 |
|---|---|
| round 0 original | `ade50dc61eb35435b56e16d8b32f1c9e74c55a5f6bf1cfd951a14bcee7cb66d9` |
| round 1 | `7ca08b856abe48cb2c3749fe4dbdb3032aa25facd439114bb41db2aae7ef1099` |
| round 2 / final | `74d495da262be5ee425e0a61772553809929249f63a7335d62ca9dc96d442570` |

All three snapshot hashes are distinct, and `main.pdf` is byte-identical to
`main_round2.pdf`.  Round 0 exposed missing Latin glyphs inside the Chinese
language block; round 1 fixed that issue.  Round 2 added the full
infinite-multiplicity proof and route boundary.

## Release checks

- Two builds in separate empty temporary directories were byte-identical to
  each other and to the packaged final PDF.
- The second-pass final logs contain no warnings, overfull or underfull
  boxes, missing glyphs, or undefined references.
- `pdffonts` reports every font embedded.
- Visual inspection of both rendered pages found no clipping, overlap, or
  unreadable glyph.
- English and Simplified Chinese abstracts each have six keywords.
- Citation population and bibliography population are both zero.
