# P191 source-only build and PDF QA

## Frozen object

- Reviewed PDF: `papers/191-prefix-divisibility-cuts/main_round0_original.pdf`
- SHA-256: `d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`
- Source SHA-256: `bdccfa1e266988c1215c7a6735f25f334a39eb99963320b7d8bf43e0d5e6db84`

## Two source-only cold builds

Two fresh temporary directories outside the paper tree received only
`main.tex` and `references.bib`.  Each ran the documented sequence under
`SOURCE_DATE_EPOCH=1704067200` and `TZ=UTC`:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Both outputs had SHA-256
`d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b`:
each is byte-identical to the immutable Round-0 PDF and to the other cold
build.  Both final logs had zero LaTeX/package warnings, zero overfull boxes,
zero underfull boxes, and zero undefined references/citations.  Extracted
text from the first cold build had SHA-256
`79d8804ff1325215282a5c16607e5a2fba7f93a92d79d947ec101c57805e963e`.

No cold-build file was copied into or used to alter the paper directory.

## Structural PDF checks

`pdfinfo`, `pdffonts`, text extraction, and raw dangerous-action scans report:

| check | result |
|---|---|
| pages | 4 |
| page geometry | every page `595.276 x 841.89 pt` (A4), rotation 0 |
| encryption | no |
| JavaScript | no |
| form | none |
| metadata stream / custom metadata | none / no |
| title, author, subject, keywords, creator, producer | all empty |
| fonts | 28 rows; every row embedded, subset, and Unicode-mapped |
| citation keys versus bibliography keys | exact set equality, 5 versus 5 |

The TeX source declares `Anonymous`, contains no affiliation,
acknowledgement, funding, email, or identity string, and the PDF metadata does
not reintroduce one.

## Visual inspection

All four rendered pages were inspected.  The title/abstract block is
balanced, theorem and display breaks are readable, the control table fits the
page cleanly, and the declarations/references page has no clipping, overlap,
or blank-content failure.  The fourth page remains intentionally sparse but is
not empty.

Build/PDF verdict: `PASS`.  This mechanical and visual QA is not a
mathematical proof and does not change `HOLD_EXTERNAL`.
