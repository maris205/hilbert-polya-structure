# P164 Review B — cold-build and PDF QA

**Frozen input PDF:** `papers/164-cyclic-equality-feedback/main.pdf`  
**SHA-256:** `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26`  
**Bytes/pages:** 301,337 bytes / 4 pages  
**Round freeze:** current `main.pdf` is byte-identical to `main_round1.pdf`;
the distinct Round-0 artifact remains pinned and unchanged.

## Two source-only cold builds

Each build began in a fresh `/tmp` directory containing only `main.tex` and
`references.bib`.  The sequence was `pdflatex`, `bibtex`, `pdflatex`,
`pdflatex`, followed by one additional settling `pdflatex` pass.

| Build | final SHA-256 | bytes | other-build match | canonical match |
|---|---|---:|---|---|
| cold 1 | `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26` | 301,337 | yes | yes |
| cold 2 | `b1fb98834db37564a50869c1fd637ceb78a5565104fb1dbb096dbd9a6b9c2f26` | 301,337 | yes | yes |

The settled logs are retained under `cold_build_1/` and `cold_build_2/`.
Each final log has zero LaTeX/package/class warnings, undefined references or
citations, rerun requests, overfull boxes, underfull boxes, badness reports,
multiply defined labels, or TeX errors.  Each BibTeX transcript has zero
warnings.  As expected for a genuinely source-only build, the first passes
record unresolved citations/references and the second passes still request
citation settlement; all are gone after the prescribed build sequence and
the extra pass does not change the PDF.

Toolchain: pdfTeX 1.40.22 (TeX Live 2022/dev/Debian), BibTeX 0.99d, Poppler
22.02.0.

## PDF structure and anonymity

`pdfinfo` reports:

- 4 pages, A4 `595.276 x 841.89 pt`, rotation zero on every page;
- file size 301,337 bytes, PDF 1.5;
- unencrypted, no form, no JavaScript, no custom metadata stream;
- blank title, subject, keywords, and author metadata;
- creator `LaTeX with hyperref` and producer `pdfTeX-1.40.22`, neither
  identifying an author.

`pdftotext` was scanned for names beyond cited authors, email addresses,
affiliations, local paths, TODO/FIXME markers, review findings, and
round/editing residue.  None was found.  The only author-line tokens are the
visible `ANONYMOUS` byline/running head and the generic phrase “anonymous
author” in the conflict statement.  The visible final limitation paragraph
contains `HOLD_EXTERNAL` and prohibits posting, circulation, or submission.

## Fonts

`pdffonts` reports 23 font-resource rows.  Every row is embedded, subset, and
Unicode-mapped (`emb=yes`, `sub=yes`, `uni=yes`), with zero exceptions.

## All-page visual inspection

All four pages were rendered independently at 144 dpi and inspected.

| Page | Result |
|---:|---|
| 1 | title, anonymous byline, abstract, definitions and opening theorem are aligned and legible; no clipping or collision |
| 2 | theorem continuation, multiplicity lemma, tail lemma and last-shell proof fit cleanly; displayed inequalities and proof boxes render correctly |
| 3 | image/fibre proof, time-two and midpoint proofs, limitations and declarations are complete; `HOLD_EXTERNAL` is visible and unobstructed |
| 4 | all four references are present; DOI/URL lines wrap within margins with no overlap or cut-off |

No blank page, raster artifact, clipped glyph, overlapping text, broken
link box, margin intrusion, orphaned heading, or visibly identifying editing
residue was found.

## Build disposition

PASS.  No source or PDF modification is requested.  `qpdf` is not installed
in this environment; `pdfinfo`, `pdffonts`, `pdftotext`, deterministic cold
reconstruction, page separation, and all-page rendering supplied the required
checks.

