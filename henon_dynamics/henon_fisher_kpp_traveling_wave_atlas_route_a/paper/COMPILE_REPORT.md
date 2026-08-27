# C202 compile report

## Final build

- engine: LuaLaTeX;
- fixed `SOURCE_DATE_EPOCH`: `1787788800`;
- pages: 3;
- final bytes: 181,588;
- final SHA-256:
  `674a6e9d137f4593caee9ad77cf8c7de407896eabf1c08adec396b6d64a1d711`.

The final PDF log is clean: zero LaTeX warnings, undefined references,
undefined citations, missing-character messages, overfull boxes, underfull
boxes and badness warnings.  `pdffonts` reports every font embedded.
`pdftotext` extracts the theorem, source locators, scope literal and strict
Route-A verdict without unresolved markers.

## Revision artifacts

- round 0:
  `073627219f6158e56699baaef3b0fd32243a827227ba455f209b96f021fa89e1`;
- round 1:
  `7d0cd80d3ad7b87dc30d36ea4d0c76a038557da73721a10f5067721970289b59`;
- round 2:
  `674a6e9d137f4593caee9ad77cf8c7de407896eabf1c08adec396b6d64a1d711`.

All three hashes are distinct, and `main.pdf == main_round2.pdf` byte for
byte.  Round 0 contains the threshold trapping theorem; round 1 adds the full
speed atlas and asymptotics; round 2 adds the exact control, evidence boundary,
source ownership, declarations and strict Route-A stop.

## Reproducibility and visual audit

Two fresh isolated two-pass builds from the same `main.tex` and fixed epoch
both produced the final SHA-256 above and clean logs.  Rasterizations of pages
1, 2 and 3 were inspected at 150 dpi: equations, Chinese and English text,
citations, page numbers and margins are legible; there is no clipping,
overlap, missing glyph or blank content page.
