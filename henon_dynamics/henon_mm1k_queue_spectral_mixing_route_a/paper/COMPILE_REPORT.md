# Compile report

## Build record

- Engine: LuaHBTeX / LuaLaTeX
- Fixed epoch: `SOURCE_DATE_EPOCH=1787875200`
- Optional metadata suppression: `\pdfvariable suppressoptionalinfo 611`
- Final pages: 3 (A4)
- Fonts: 16 reported entries; every font embedded and subset
- Final-pass logs: no `Warning`, overfull/underfull boxes, undefined references,
  multiply-defined labels or residual warnings.  First-pass citation warnings
  are the normal two-pass bootstrap and disappear on pass 2.
- Text audit: title, spectral theorem, capacity boundary, audit count,
  Route-A verdict and scope literal are extractable.
- Visual audit: all three pages rasterized at 120 dpi; equations, headings,
  references and page boundaries are clean with no clipping.

## Revision hashes

- round 0 (`main_round0_original.pdf`):
  `522b4bec182ecc8ed0098feb42ec414c3c350a91b95ab08113141ddd417e29f7`
- round 1 (`main_round1.pdf`):
  `c3d7d40fe03da0db418761e6b72739332dea859b00a9c144bfa79d4ebe6e3d77`
- round 2/final (`main_round2.pdf`, `main.pdf`):
  `3754930aa79f7b967c83698b6bf01db15dc11dc464f6c5bf852be9711e403379`

All three revision hashes differ, and `main.pdf` is byte-for-byte equal to
`main_round2.pdf`.  Each revision was compiled twice in a fresh temporary
directory under the fixed epoch; these are deterministic double builds.
