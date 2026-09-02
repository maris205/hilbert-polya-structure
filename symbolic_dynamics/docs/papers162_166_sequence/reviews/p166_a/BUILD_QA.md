# P166 Hostile Review A: build and PDF QA

**Verdict:** `PASS`.  **External state:** `HOLD_EXTERNAL`.

## Pinned Round-0 inputs

| artifact | SHA-256 |
|---|---|
| `main.tex` | `a709e1b8dc6f50059cf85c8a2c922455b7812b24f4e38ebab88c77123f279ce8` |
| `references.bib` | `fcd2132a399ed5d21d75035aaadc234cce79dc4040613a9c5cc54ca9c896c500` |
| `main_round0_original.pdf` | `f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c` |

Each cold directory initially received only the two pinned source files.
Both ran `pdflatex`, `bibtex`, two further `pdflatex` passes, and one settling
pass under `SOURCE_DATE_EPOCH=0`, `TZ=UTC`.

| check | cold build 1 | cold build 2 |
|---|---|---|
| source hashes equal pins | yes | yes |
| pass 3 equals settling pass | yes | yes |
| PDF bytes | 294,007 | 294,007 |
| PDF SHA-256 | `f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c` | same |
| equals frozen Round 0 | yes | yes |
| final log SHA-256 | `13ffb4163036bf95147065d6e7555e778d38cb79c34678dbd3ddfb7690002b6d` | same |
| final BBL SHA-256 | `02b1c2afb509a6eaff68b41779fd7e964d4a3632a0f2aab253751133d7108bdf` | same |
| warning/error/undefined/rerun/bad-box findings | 0 | 0 |
| BibTeX warnings/errors | 0 | 0 |

## Independent verifier

- `verify_review_a.py` SHA-256:
  `2f717ff4cd557e353b94826c85238cff19497d622f4d498b1b549cdc786be4ef`;
- `CANONICAL.txt` SHA-256:
  `bee2274c898591173b9fdda41b728f627c7dc30faedbf2eea70efee967ecf46d`;
- assertions: `11,795,304`, result `PASS`;
- two fresh process-separated runs are byte-identical to the canonical
  transcript.

## PDF and anonymity checks

- 4 pages; every page A4 `595.276 x 841.89 pt`, rotation zero;
- PDF 1.5, 294,007 bytes; no encryption, form, JavaScript, metadata stream,
  custom metadata, suspect objects, or raster image;
- Title, Author, Subject, Keywords, Creator, and Producer fields are blank;
- 24/24 font rows are embedded, subsetted, and Unicode mapped;
- extracted text contains the anonymous byline and visible `HOLD_EXTERNAL`;
- no email, affiliation, ORCID, acknowledgement, local path, review marker,
  `TODO`, `FIXME`, `[VERIFY]`, or draft marker was found.

## Four-page 144-dpi visual inspection

- Page 1: title/byline, abstract, subtraction boundary, equations (1)--(6),
  margins, and running footer are clean.
- Page 2: oracle, cycle lemma, recurrent theorem, zeta formulas, and the
  beginning of the depth proof are clean.
- Page 3: depth summation, last shell, fibre formula, EGF, and extremal proof
  are legible with no clipping or collision.
- Page 4: controls, visible lifecycle sentinel, and all six references render
  cleanly; remaining whitespace is ordinary end-of-note space.

All retained 144-dpi page renders are under `render_144dpi/`.
