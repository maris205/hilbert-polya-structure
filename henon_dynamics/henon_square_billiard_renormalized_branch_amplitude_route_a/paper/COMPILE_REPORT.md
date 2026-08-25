# C162 compile report

- Engine: LuaLaTeX.
- Fixed epoch: `SOURCE_DATE_EPOCH=1787616000`.
- Pass-one SHA-256: `1bbae9d35ac4d54f97f76a020ef1ed85ae1f87d9df9d41cb2faf27394ada19e6`.
- Pass-two SHA-256: `1bbae9d35ac4d54f97f76a020ef1ed85ae1f87d9df9d41cb2faf27394ada19e6`.
- Deterministic double build: **PASS**.
- Pages: 2.
- The preserved stages are content-distinct:
  - round 0, one page: `0f55d23072249e06a8c9e4c3396255c525a116ebce5fe6cbc596b69c6ec015da`;
  - round 1, one page: `18361cc51a26e126a793ebc5536d3d5c6fb1c533a6f8ee05fde7afd76958b913`;
  - round 2, two pages: `1bbae9d35ac4d54f97f76a020ef1ed85ae1f87d9df9d41cb2faf27394ada19e6`.
- `main.pdf` is byte-identical to `main_round2.pdf`.
- Font audit: all fonts reported by `pdffonts` are embedded; the CJK font is
  `DroidSansFallback` and visual inspection shows no missing glyphs.
- Log audit: zero LaTeX warnings, missing characters, undefined references,
  overfull boxes, or underfull boxes in every preserved stage and both final
  release passes.
- Visual audit: both pages inspected; the normalized coefficient, uniform tail
  proof, bilingual abstract, Route-A boundary, and declarations are legible and
  unclipped.
