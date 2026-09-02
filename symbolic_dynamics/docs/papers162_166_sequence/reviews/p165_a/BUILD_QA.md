# P165 source-only build and PDF QA

## Inputs and method

Each cold build received only the pinned `main.tex` and `references.bib` in
a new temporary directory.  No paper-local auxiliary, bibliography, log,
or PDF was copied into either directory.  Both builds used:

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=0 TZ=UTC bibtex main
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Reproducibility receipts

| item | cold build 1 | cold build 2 |
|---|---|---|
| source-only pipeline | PASS | PASS |
| final PDF bytes | 288,837 | 288,837 |
| final PDF SHA-256 | `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a` | `f974ff2a1f43f875c26f4ad754655801336fbb77ec317df69b0c5bdc2f144b5a` |
| final `main.log` SHA-256 | `f7afbad31e6b97b0ddd8372d90abdc499f8a1ba6aa06f1ee7c48352a1d424167` | `f7afbad31e6b97b0ddd8372d90abdc499f8a1ba6aa06f1ee7c48352a1d424167` |
| final `.bbl` SHA-256 | `d892ae169e3f71ea608f0c1312ec1b6b79e84be0295816fafd4d507dd4f88d59` | `d892ae169e3f71ea608f0c1312ec1b6b79e84be0295816fafd4d507dd4f88d59` |
| final-pass warnings/errors | 0 | 0 |
| BibTeX warnings/errors | 0 | 0 |

The cold PDFs are byte-identical to each other, to `main.pdf`, and to
`main_round0_original.pdf`.  Initial-pass undefined citations/references are
the expected pre-BibTeX transients; none remains in either settled pass.

## Structural PDF QA

- 4 pages, A4, PDF 1.5; no page rotation.
- 23 font rows; all 23 are embedded, subsetted, and Unicode mapped.
- `pdfimages -list` reports no raster images.
- No forms, JavaScript, encryption, suspect objects, custom metadata, or
  metadata stream is present.
- Title, author, subject, keywords, creator, and producer metadata fields are
  empty.  The visible byline is `Anonymous`.
- Extracted text contains no affiliation, email, ORCID, acknowledgement,
  funding/grant marker, `TODO`, `FIXME`, `VERIFY`, placeholder, undefined
  reference, or draft token.
- All three citations resolve in the settled bibliography.  The final logs
  contain no undefined citation/reference, multiply defined label,
  overfull/underfull box, or package warning.
- `HOLD_EXTERNAL` is visibly present as the intended lifecycle token.

## Full-page visual inspection

All four pages were rendered at 150 dpi and inspected individually.

| page | result |
|---:|---|
| 1 | Title, anonymous byline, abstract, literal-map display, theorem opening, margins, links, and footer render cleanly. |
| 2 | Theorem continuation, dyadic-budget proof, equations (4)--(8), and the image construction are unclipped and legible. |
| 3 | Extremal inverse proof, count, boundary audit, lifecycle token, and first reference render cleanly; no orphaned heading or overlap. |
| 4 | References (2)--(3) render cleanly.  The remaining white area is the natural end of a four-page note, not missing content. |

No clipping, overlap, missing glyph, broken formula, broken URL, anomalous
page break, or identifying information was observed.

## QA verdict

**PASS.**  The Round0 PDF is exactly reproducible from source, anonymous,
and mechanically clean.  This does not lift `HOLD_EXTERNAL`.
