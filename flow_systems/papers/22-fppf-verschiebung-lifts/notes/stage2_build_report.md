# Paper 22 Stage-2 build report

Date: **2026-08-24**

## Build result

**PASS**

The manuscript was rebuilt from the current LaTeX and BibTeX sources with
BibTeX followed by two LuaLaTeX passes.

| Metric | Result |
|---|---|
| PDF pages | 12 |
| Page size | A4 |
| PDF version | 1.5 |
| PDF size | 143,594 bytes |
| unresolved citations | 0 |
| unresolved cross-references | 0 |
| overfull boxes | 0 |
| missing glyphs | 0 |
| fatal errors | 0 |
| embedded/subset fonts | yes |

Two nonblocking underfull-box notices remain in the manually line-broken
Chinese abstract. Visual inspection confirms that the text is legible,
left-aligned, inside the margins, and free of abnormal stretched spaces.

## Visual inspection

The final PDF was rasterized and checked at:

- p. 1: title, English abstract, Chinese abstract, keywords, and opening;
- p. 7: the truncated-ring detector and all-index proof;
- p. 12: limitations and the complete bibliography, including the rendered
  arXiv DOI.

No clipping, equation overflow, missing text, broken links, or font
substitution was observed.

## Final artifact hashes

| Artifact | SHA-256 |
|---|---|
| manuscript.tex | 04968dd2a46708f3b79da59370d27af4ad5329115fef610b0e090c922c53bda1 |
| references.bib | bd03813691db911316b18620ee4a1d212ac284fce7fb79af9f1b1cbc7ea71093 |
| paper.bbl | 4244c70dea32b053dc2df1c1435ebfeccc1e26f93dbe80179a523950ed091156 |
| paper.log | 70b69583177e0051f8e31049c57fb71d938cc6b39d1bbb5f4717632d77e7c9d5 |
| paper.pdf | 2fac65d734308ba0353d39c4af172bfdc1d720054d54839c511656dabb4d9d2c |

The PDF and log are newer than both source files. This report records the
post-revision build that rendered the Deninger arXiv DOI.
