# C158 compilation report

- Engine: LuaLaTeX via `latexmk -lualatex`.
- Reproducibility environment: `SOURCE_DATE_EPOCH=1787616000`,
  `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
- CJK font: Droid Sans Fallback, embedded and subsetted.
- Status: SUCCESS; 2 pages.
- Final PDF: `main.pdf`, byte-identical to `main_round2.pdf`.
- Preserved stages: round 0 original, round 1, and round 2.
- Abstracts/keywords: independently composed, structurally aligned English
  and Simplified Chinese abstracts; 175 English words, 317 Han characters,
  and six keywords in each language.
- Declarations: package data/code availability, ethics, anonymous CRediT-role
  provenance, conflicts, funding, and AI-use disclosures are present.
- Undefined references/citations: 0; no bibliography.
- Overfull/underfull boxes: 0.
- Missing glyphs and layout/reference/citation warnings: 0.
- Fonts: all embedded according to `pdffonts`.
- Text extraction: English, Chinese, formulas, tables, scope, and declarations
  are present in `pdftotext -layout` output.
- Visual inspection: both rendered pages have no clipping, overlap,
  truncation, malformed glyph, or layout-failure blank region.
- Determinism: two clean fixed-epoch builds in fresh directories were
  byte-identical.

Final SHA-256 values are recorded by `C158_RELEASE_MANIFEST.json`.
