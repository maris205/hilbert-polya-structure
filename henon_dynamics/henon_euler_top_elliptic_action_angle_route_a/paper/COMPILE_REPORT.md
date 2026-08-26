# C186 compile report

Status: PASS.

- Engine: LuaLaTeX, two passes, `SOURCE_DATE_EPOCH=1787702400`, `FORCE_SOURCE_DATE=1`.
- Final PDF: 2 pages, 141,393 bytes.
- Final SHA-256: `43565cd22e891ca2d89aff7791b536a8acb8adc64b319b3ca290b5daaf140d20`.
- Round hashes are pairwise distinct:
  - round 0: `aa0eac8666eead3bfcb1942ea42f4f39b563edbb563fb4264b08dc773f18329e`
  - round 1: `0a244032292a3dbbb0a202a9f22055180e724a28605e9fa21c84155448b1633e`
  - round 2/final: `43565cd22e891ca2d89aff7791b536a8acb8adc64b319b3ca290b5daaf140d20`
- The three revision-focus paragraphs are content-distinct and correspond to the improvement log.
- Two clean fresh-directory, two-pass builds reproduced the final PDF byte for byte.
- Final and fresh log scans contain no LaTeX/package warning, overfull/underfull box, undefined reference, missing glyph, or fatal finding.
- `pdffonts`: every font is embedded and subset.
- Visual inspection: both rendered pages are complete, legible, balanced, non-overlapping, and free of clipping or blank regions. Equation (5), the frozen Poisson convention, both cap momenta, and both action quadratures were checked at rendered resolution.

Drafting improvements and visual checks are internal workflow artifacts, not external peer review.
