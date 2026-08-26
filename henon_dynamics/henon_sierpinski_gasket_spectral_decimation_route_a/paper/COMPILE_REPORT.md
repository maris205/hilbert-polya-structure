# C184 compile report

Status: PASS.

- Engine: LuaLaTeX, two passes per artifact,
  `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`.
- Final PDF: 2 pages, 192,786 bytes.
- Final SHA-256:
  `3ae96a32319b2af57b72b73ab3085cfbe38c88b24f5fc0a831107ed44274230d`.
- Round hashes are pairwise distinct:
  - round 0:
    `e9c07ef24ebcc021cb2bc154daa56a4019adf2a0f44b620f0e06d52b070cc68e`
  - round 1:
    `6f2971b373b08684017749ed070df171a7d0a4ab3a9be7a88bb31787fb7698f9`
  - round 2/final:
    `3ae96a32319b2af57b72b73ab3085cfbe38c88b24f5fc0a831107ed44274230d`
- Every round is two pages and contains a content-distinct
  `Revision-round focus` paragraph; `main.pdf` is byte-identical to round 2.
- Two new temporary directories, each built twice from only `main.tex`,
  reproduced the final PDF byte for byte.
- Final and fresh second-pass log scans contain no LaTeX/package warning,
  overfull or underfull box, undefined reference, missing character, or fatal
  finding.
- `pdffonts`: every listed font is embedded; all CID fonts are subset and
  Unicode mapped.  Legacy Computer Modern math fonts are embedded/subset
  with their standard built-in encoding.
- Visual inspection at 120 dpi: both pages are complete, legible,
  non-overlapping, balanced, and free of clipping, blank spill pages, missing
  glyphs, or malformed equations.  The formerly visible `qquad` typo was
  corrected to mathematical spacing before the final build.

Drafting improvements, build checks, and visual inspection are internal
workflow artifacts, not external peer review.
