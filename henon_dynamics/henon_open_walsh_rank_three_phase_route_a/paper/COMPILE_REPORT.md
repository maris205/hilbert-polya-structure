# C168 compilation report

- Engine: LuaLaTeX via `latexmk -lualatex`.
- Reproducibility environment: `SOURCE_DATE_EPOCH=1787616000`,
  `FORCE_SOURCE_DATE=1`, and `TZ=UTC`.
- Status: SUCCESS; 2 A4 pages.
- Final PDF SHA-256:
  `68dcb55469222603236d6d496af5fc691fca882277b6bea20d5a89b3db39c679`.
- Final `main.pdf` is byte-identical to `main_round2.pdf`.
- Preserved stages: round 0 exact secular/phase theorem, round 1 joint
  mixed-transform theorem, and round 2 torsion/antiunitary hostile-control
  pass.  All three stage hashes differ.
- Abstracts/keywords: independently composed English and Simplified Chinese
  abstracts with six keywords in each language.
- Declarations: data/code availability, ethics, anonymous contribution
  record, funding, conflicts, and AI-use disclosure are present.
- Undefined references/citations: 0; no bibliography.
- Overfull/underfull boxes: 0.
- Missing glyphs and layout/reference/citation warnings: 0.
- Fonts: every font is embedded and subsetted according to `pdffonts`.
- Text extraction: title, both abstracts, all five theorem/control sections,
  scope literal, and declarations are present under `pdftotext -layout`.
- Visual inspection: both rendered pages have no clipping, overlap,
  truncation, malformed glyph, duplicate equation tag, or unintended blank
  region.
- Determinism: two fresh fixed-epoch builds are mutually byte-identical and
  identical to the release PDF.

Evidence and release hashes are closed by `C168_RELEASE_MANIFEST.json`.
