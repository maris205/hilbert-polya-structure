# HCS-C336 compile report

- Engine: LuaLaTeX, two passes per build.
- Fixed environment: `SOURCE_DATE_EPOCH=1788393600`,
  `FORCE_SOURCE_DATE=1`, `TZ=UTC`.
- Each of Rounds 0, 1 and 2 was built twice in fresh directories; the two
  builds of each round were byte-identical.
- Settled logs contain no LaTeX/package, overfull, underfull, reference,
  citation, rerun, missing-character or missing-glyph warning.
- Round hashes:
  - Round 0: `a055046d2fb2bbb5940fa3f3b9ecff8423ff09508947f123cc7800b448501a02`
  - Round 1: `f5ca1f243db737a0b4b2f86b4fd8dbbd074d5b734e0d3f2b0f27f4324f97e3bc`
  - Round 2/final: `cdde6ab95da987d1c21c816edc734c77d0d81a47ed9011076e75cd92cefd6d1a`
- All three revision hashes are distinct and `main.pdf` is byte-identical to
  Round 2.
- Final PDF: 3 pages, 175,899 bytes, 23 font rows; every font is embedded and
  subset.
- Extracted-text sentinels for all three revision layers pass; no control or
  literal-TeX garbage is present.
- All 3 final pages rasterized successfully and were visually inspected for
  clipping, overlap, missing glyphs and broken equations.
