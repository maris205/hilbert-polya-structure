# P187 source-only build and PDF QA

## Frozen object

- Reviewed PDF: `papers/187-cyclic-divisor-quotient/main_round0_original.pdf`
- SHA-256: `399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1`
- Source SHA-256: `e4dd2c5afb6381563476c6b6735f94c932403492165b8f21adeee6a448f7b83d`

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
`399ee1fd64a569ef3076e1049a5151e5b4b07d03d2c1592f84c5b2a811fbb8a1`:
each is byte-identical to the immutable Round-0 PDF and to the other cold
build.  Both final logs had zero LaTeX/package warnings, zero overfull boxes,
zero underfull boxes, and zero undefined references/citations.  Extracted
text from each build had SHA-256
`f59ee09e28bf77f48c26cde9ac2ee930579b97e621ea15c47606a0140e7bcac4`.

No cold-build file was copied into or used to alter the paper directory.

## Structural PDF checks

`pdfinfo`, `pdffonts`, text extraction, and raw dangerous-action scans report:

| check | result |
|---|---|
| pages | 4 |
| page geometry | every page `595.276 x 841.89 pt` (A4), rotation 0 |
| encryption | no |
| JavaScript | no; no `/JavaScript`, `/JS`, `/Launch`, `/EmbeddedFile`, or `/Encrypt` action token found |
| form | none |
| metadata stream / custom metadata | none / no |
| title, author, subject, keywords, creator, producer | all empty |
| fonts | 25 rows; every row embedded, subset, and Unicode-mapped |
| citation keys versus bibliography keys | exact set equality, 2 versus 2 |

The TeX source declares `Anonymous`, contains no affiliation,
acknowledgement, funding, email, or identity string, and the PDF metadata does
not reintroduce one.

## Visual inspection

All four rendered pages were inspected.  The title/abstract block is
balanced, theorem and display breaks are readable, hyperlinks do not obscure
text, proof-end symbols stay attached to their proofs, and the final
references page has no clipping, overlap, orphaned heading, or blank-content
page.  The compact last page is intentional and legible.

Build/PDF verdict: `PASS`.  This mechanical and visual QA is not a
mathematical proof and does not change `HOLD_EXTERNAL`.
