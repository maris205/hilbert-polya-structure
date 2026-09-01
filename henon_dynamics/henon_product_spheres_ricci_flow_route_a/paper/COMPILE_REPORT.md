# Compile report

- Engine: LuaHBTeX 1.14.0 (TeX Live 2022/dev/Debian).
- Command source: `\def\CRevisionRound{r}\input{paper/main.tex}`.
- Environment: `SOURCE_DATE_EPOCH=1788220800`, `FORCE_SOURCE_DATE=1`,
  `TZ=UTC`.
- Two LuaLaTeX passes per build; two independent fresh-directory builds per
  round.

| Round | Pages | SHA-256 | Fresh trial 1 | Fresh trial 2 |
|---:|---:|---|---|---|
| 0 | 2 | `5659c753df3f3823ff40b8a6640a5010a9d8898d6256a09098ef40bf488ec139` | byte-identical | byte-identical |
| 1 | 3 | `780fe2fdd67de3b12768212711c45d7ab073c4b1758809f557bb973739b0b4d3` | byte-identical | byte-identical |
| 2 | 4 | `93b6aaf8229ec317c4933cf5bf264f82501c64ec1c7121625f2b27860e6a4d8a` | byte-identical | byte-identical |

The three hashes are distinct because the rounds are substantively different.
`paper/main.pdf` is byte-identical to `paper/main_round2.pdf`.

Every final second-pass log is warning-free: no LaTeX/package warning,
overfull or underfull box, undefined reference, rerun request, or missing
character.  `pdffonts` reports 22, 22, and 23 font rows respectively; every
font is embedded and subset.  `pdftotext` extracts 1,672 words from the final
PDF and retains the candidate ID, theorem constants, evidence counts, scope,
strict tuple, verdict, and both DOI strings.

The four final pages were rasterized at 110 dpi and visually inspected.  The
title/abstract, every displayed formula, theorem/proof boundary, two-column
equation pair, boundary table, references, page numbers, and margins are
legible; there is no clipping, overlap, blank page, broken glyph, or orphaned
heading.  The added Ricci residue, finite-tail receipt, corrected abstract word
spacing, and both `\quad`/`\qquad` equation separators were also checked in
extracted text.
