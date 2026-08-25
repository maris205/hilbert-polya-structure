# C155 compilation report

- Engine: LuaLaTeX via `latexmk -lualatex`.
- Reproducibility environment: `SOURCE_DATE_EPOCH=1787616000`, `TZ=UTC`.
- CJK font: Droid Sans Fallback, embedded and subsetted.
- Status: SUCCESS; 2 pages.
- Typography: normal 10-point body; the finite-size boundary, validation, and
  declarations share the second page without a global size reduction.
- Final PDF: `main.pdf`, byte-identical to `main_round2.pdf`.
- Preserved stages: round 0 original, round 1, round 2.
- Abstracts/keywords: independently structured English and Chinese abstracts;
  seven keywords in each language.
- Declarations: data/code, ethics, CRediT/provenance, conflicts, funding, and
  AI-use disclosures present.
- Undefined references/citations: 0; no bibliography.
- Overfull/underfull boxes: 0.
- Missing glyphs and layout/reference/citation warnings: 0.
- Fonts: all embedded according to `pdffonts`.
- Visual inspection: both rendered pages have no clipping, overlap,
  truncation, malformed glyph, or layout-failure blank region.
- Determinism: two clean fixed-epoch builds in fresh directories were
  byte-identical.

Final SHA-256 values are recorded by `C155_RELEASE_MANIFEST.json`.
