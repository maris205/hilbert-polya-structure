# P163 Review B — cold-build and PDF QA

**Frozen input PDF:** `papers/163-complemented-shadow-dynamics/main.pdf`  
**SHA-256:** `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf`  
**Bytes/pages:** 424,998 bytes / 5 pages  
**Round freeze:** `main.pdf`, `main_round0_original.pdf`, and
`main_round1.pdf` are byte-identical.

## Two source-only cold builds

Each build began in a fresh `/tmp` directory containing only `main.tex` and
`references.bib`.  The sequence was `pdflatex`, `bibtex`, `pdflatex`,
`pdflatex`, followed by one additional settling `pdflatex` pass.

| Build | pass-3 SHA-256 | settling-pass SHA-256 | bytes | canonical match |
|---|---|---|---:|---|
| cold 1 | `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf` | same | 424,998 | yes |
| cold 2 | `899e7c6b24f3a6e99041d05410db75c1de152f4d98b2e90d10e4619927b216bf` | same | 424,998 | yes |

Both builds settled before the extra pass and byte-match each other and the
frozen canonical PDF.  Targeted scans found zero LaTeX/package warnings,
undefined references/citations, rerun requests, overfull boxes, underfull
boxes, multiply-defined labels, or TeX errors.  Both BibTeX logs report
`warning$ -- 0`.

## PDF structure and anonymity

`pdfinfo` reports:

- 5 pages, A4 `595.276 x 841.89 pt`, rotation zero;
- unencrypted, no form, no JavaScript, no custom metadata stream;
- blank title, subject, keywords, and author metadata;
- file size 424,998 bytes, PDF 1.5.

`pdftotext` was scanned for email addresses, local paths, TODO/FIXME markers,
review/round edit markers, and affiliations.  The only affiliation-like hit
was “University of California Press” in a bibliography entry.  The visible
byline is `ANONYMOUS`, and `HOLD_EXTERNAL` is visible in both the abstract and
the final status section.

## Fonts

`pdffonts` reports 32 font-resource rows.  Every row is embedded, subset, and
Unicode-mapped (`emb=yes`, `sub=yes`, `uni=yes`); there are zero exceptions.

## All-page visual inspection

All five pages were rendered independently at 144 dpi and inspected.

| Page | Result |
|---:|---|
| 1 | title/byline/abstract and opening theorem are centered and legible; no clipping or collision |
| 2 | theorem continuation and displayed formulas fit the text block; no orphaned heading or margin intrusion |
| 3 | proof text and inverse proposition are balanced and legible; symbols and proof boxes render correctly |
| 4 | owner boundary, exact-control declaration, and declarations are intact; no overlap or cut-off |
| 5 | external-status warning and bibliography are complete; DOI line wraps are clean |

No blank page, raster artifact, clipped glyph, overlapping text, broken link
box, bad margin, or visibly non-anonymous editing residue was found.

## Build disposition

PASS.  No source or PDF modification is requested.  `qpdf` is not installed
in the environment, but `pdfinfo`, `pdffonts`, `pdftotext`, deterministic
cold reconstruction, and all-page rendering supplied the required checks.

