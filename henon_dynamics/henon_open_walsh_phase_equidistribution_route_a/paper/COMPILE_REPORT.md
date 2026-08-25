# C163 compilation report

- Engine: LuaLaTeX via `latexmk -lualatex`.
- Reproducibility environment: `SOURCE_DATE_EPOCH=1787616000`,
  `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
- CJK font: Droid Sans Fallback, embedded and subsetted.
- Status: SUCCESS; 2 pages.
- Final PDF: `main.pdf`, byte-identical to `main_round2.pdf`.
- Preserved stages: round 0 original, round 1 mathematical strengthening,
  and round 2 hostile-scope/reproducibility pass; all three hashes differ.
- Abstracts/keywords: independently composed, structurally aligned English
  and Simplified Chinese abstracts; 156 English words, 236 Han characters,
  and six keywords in each language.
- Declarations: package data/code availability, ethics, anonymous role
  provenance, funding, conflicts, and AI-use disclosures are present.
- Undefined references/citations: 0; no bibliography.
- Overfull/underfull boxes: 0.
- Missing glyphs and layout/reference/citation warnings: 0.
- Fonts: all embedded and subsetted according to `pdffonts`.
- Text extraction: title, English and Chinese abstracts, formulas, joint
  theorem, scope literal, and declarations are present in `pdftotext -layout`.
- Visual inspection: both rendered pages have no clipping, overlap,
  truncation, duplicate equation number, malformed glyph, or layout-failure
  blank region.
- Determinism: two clean fixed-epoch builds in separate fresh directories
  were mutually byte-identical and identical to the release PDF.

Final SHA-256 values are recorded by `C163_RELEASE_MANIFEST.json`.
