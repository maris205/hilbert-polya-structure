# P162 Round-1 source-only build and PDF QA

## Frozen artifacts

| artifact | bytes | SHA-256 |
|---|---:|---|
| `main_round0_original.pdf` | 399,805 | `e496ce1be3084e61616494cab2ca405238adfa575a6484db93029f8dae01de46` |
| `main_round1.pdf` | 399,828 | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` |
| `main.pdf` | 399,828 | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` |

The saved Round-0 hash is unchanged from Hostile Review A.  `main.pdf` and
`main_round1.pdf` are byte-identical.  Text comparison confirms the intended
abstract repair from “worst-source absorption clock” to
“worst-non-full-source emptying clock”; theorem and proof formulas are
unchanged.  Normal line reflow follows from the longer phrase.

## Source-only cold builds

Two fresh temporary directories each received only the pinned `main.tex` and
`references.bib`.  Neither received auxiliary files, a `.bbl`, logs, or a PDF.
Each ran

```bash
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=0 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

| check | cold build 1 | cold build 2 |
|---|---|---|
| complete source-only sequence | PASS | PASS |
| PDF bytes | 399,828 | 399,828 |
| PDF SHA-256 | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` | same |
| final `main.log` SHA-256 | `6d1f0c19174359b3eb5a42600fc4fd7e077938069479eb760f31e5db8ad62b89` | same |
| final LaTeX/package warnings or errors | 0 | 0 |
| undefined citations/references | 0 | 0 |
| box/rerun warnings | 0 | 0 |
| BibTeX warnings/errors | 0 | 0 |

Both cold PDFs are byte-identical to frozen Round 1.

## Automated PDF inspection

- 4 pages, A4 (`595.276 x 841.89 pt`), PDF 1.5.
- 30 font rows; all 30 are embedded, subsetted, and Unicode mapped.
- No raster images, forms, JavaScript, encryption, suspect objects, or page
  rotation.
- PDF Title, Author, Subject, and Keywords metadata fields are blank.
- The visible byline is `Anonymous`.  No name, affiliation, email, ORCID,
  acknowledgement, institution, local path, or editorial marker appears.
- Extracted text has no `??`, `[?]`, `[VERIFY]`, `TODO`, or `FIXME` token.
- `HOLD_EXTERNAL` is visible in both the abstract and lifecycle section.

## Full-page visual inspection

Every page was rasterized at 150 dpi and inspected at original resolution.

| page | result |
|---:|---|
| 1 | Title, anonymous byline, repaired abstract, definitions, theorem (1)--(2), equations (1)--(6), and margins are clean. |
| 2 | Mean, fibre/recovery statements, erosion lemma, rank proof, sharp witness, and section transition are clean. |
| 3 | Fixed-span fibre, every-target proof, recovery proof, controls, limitations, and Data Availability are clean. |
| 4 | Ethics/author/funding/lifecycle declarations and all four references are clean; the remaining white area is the natural end of the manuscript. |

No clipping, overlap, malformed exponent, missing glyph, broken URL, orphaned
heading, footer collision, or illegible reference was observed.

## Build verdict

**PASS.**  Round 1 is deterministic, anonymous, visually sound, and retains
the required `HOLD_EXTERNAL` lifecycle.
