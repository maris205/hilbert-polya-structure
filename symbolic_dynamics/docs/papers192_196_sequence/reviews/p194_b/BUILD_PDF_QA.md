# P194 Review-B build and PDF QA

## Artifact identity

Review B distinguishes the immutable input from the accepted repair:

| artifact | pages | bytes | SHA-256 | role |
|---|---:|---:|---|---|
| `papers/194-least-raising-crystal-words/main_round1.pdf` | 4 | 370,448 | `9f1b67680b4c915e5bd60d01730095d5d06817368244d83ecfc84d39a86bf207` | immutable Round-1 review input |
| `papers/194-least-raising-crystal-words/main.pdf` | 5 | 372,121 | `682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b` | current accepted source-repair artifact |

The current PDF is intentionally not byte-identical to the immutable input:
the Defant--Williams paragraph and sixth bibliography item add one page.

## Exact verifier replays

The following commands were run from the workspace root in fresh processes:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 papers/194-least-raising-crystal-words/code/verify.py \
  | cmp - papers/194-least-raising-crystal-words/code/CANONICAL.txt

PYTHONDONTWRITEBYTECODE=1 python3 docs/papers192_196_sequence/reviews/p194_b/verify_review_b_p194.py \
  | cmp - docs/papers192_196_sequence/reviews/p194_b/CANONICAL.txt
```

Each command was executed twice.  All four processes exited zero and were
byte-identical to their respective canonical files.  The reviewer control
imports neither the author implementation nor Review A.

## Two source-only cold builds

Two independent temporary directories received only current `main.tex` and
`references.bib`.  Each used

```bash
export SOURCE_DATE_EPOCH=1704067200
export TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

Both cold outputs had SHA-256
`682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b`
and were byte-identical to the current `main.pdf`.  Each was five A4 pages,
372,121 bytes, PDF 1.5.  No LaTeX warning, package warning, bad box, undefined
reference, undefined citation, or BibTeX warning matched the logs.

## Mechanical PDF inspection

```text
pages: 5
page size: A4, 595.276 x 841.89 pt
PDF version: 1.5
encrypted: no
forms: none
JavaScript: no
embedded attachments: 0
metadata stream: no
title/subject/keywords/author/creator/producer: blank
font rows: 27
embedded/subsetted/Unicode: 27/27/27
citation keys / bibliography keys: 6 / 6, exact equality
```

Extracted text contains the anonymous byline and both occurrences of
`OWNER_AMBER / HOLD_EXTERNAL`.  It contains no unresolved marker, author
identity, affiliation, email address, ORCID, grant acknowledgment, or local
path.

## Visual inspection

All five pages were rasterized at 150 dpi and inspected individually.

- Page 1: title, anonymous byline, abstract, literal signature, scheduler,
  example orbit, and new subtraction paragraph are legible and unclipped.
- Page 2: clock theorem and proof have intact displays, theorem numbering,
  and margins.
- Page 3: Schur product, fixed census, and fibre-set display are aligned;
  no symbols or braces are clipped.
- Page 4: fibre proof, stable threshold, evidence boundary, and bibliography
  entries 1--4 are intact.
- Page 5: bibliography entries 5--6 are present and legible.  The page is
  sparse but not blank; no orphaned heading or missing reference was found.

No overlap, malformed display, missing glyph, unintended blank page, broken
hyperlink text, or identifying metadata was found.  Build and visual status:
`PASS`.
