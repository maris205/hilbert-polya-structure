# Final mechanical QA — P94

QA date: 2026-08-28 UTC  
Disposition: **internal Stage 2 frozen package: PASS / external release: HOLD**

This is the final mechanical audit of the reviewed internal package. The
mathematical and scope audit is recorded in `HOSTILE_REVIEW.md`. Neither that
record nor this mechanical pass is external peer review, specialist
clearance, or evidence of novelty or priority.

## Exact-control gate

From the P94 directory,

```text
python3 code/verify_marked_s_adic.py
```

completed with exit status zero and reported:

```text
marked symmetric S-adic exact control: PASS
assertions=90509
literal_marker_words=2286
cyclic_phase_words=2286
incidence_bias_cases=28050
inverse_limit_cases=170
```

The literal lane checked linear and cyclic `10` markers and exact block
decoding. The independent incidence lane checked the normalized matrix
orientation, symmetric and antisymmetric directions, products, finite
inverse-limit lifts, and the two product specializations. The displayed
long quadratic-product comparison is a labelled floating-point sanity check;
the theorem-bearing finite recurrences use exact rational arithmetic.

## Build and log gate

The complete production sequence

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

completed with exit status zero at every stage. The final `main.log` and
`main.blg` contain:

- LaTeX or package warnings: 0;
- undefined citations: 0;
- undefined references: 0;
- multiply defined labels: 0;
- overfull boxes: 0;
- underfull boxes: 0;
- rerun requests: 0;
- BibTeX errors or missing-entry warnings: 0.

## PDF and extracted-text gate

`pdfinfo` reports:

- artifact: `main.pdf`;
- pages: 7;
- geometry: A4, 595.276 by 841.89 points, rotation 0;
- file size: 352,417 bytes;
- PDF version: 1.5;
- encryption: none;
- JavaScript: none;
- forms: none;
- suspect objects: none;
- visible author: Anonymous; PDF Author metadata: empty.

Canonical PDF SHA-256:

```text
e078bd56c7c8c2c8180ad9068f00fd2e62b7ed9d89accf11267214dd56d590a0  main.pdf
```

`pdffonts` reports 25 font rows. All 25 fonts are embedded, subsetted, and
Unicode-mapped. `pdftotext -layout` extracted 23,406 bytes. The title,
abstract, theorem numbers, displayed formulas, links, citations, and all six
references are extractable. The extracted PDF text contains no unresolved
cross-reference marker or editorial sentinel.

## Page-by-page visual gate

All seven pages were rasterized at 110 dpi and inspected individually.

1. The title, anonymous byline, abstract, corrected finite-prefix bias radius,
   introduction, contribution list, and footer are complete and unclipped.
2. The prior-results boundary, directive language, marker statement, and
   first half of its proof are legible; citations and formulas remain inside
   the text block.
3. Marker uniqueness, minimality, aperiodicity, tower definitions, matrices,
   and the affine-bijection statement have no collision or malformed glyph.
4. The measure construction, boundary estimate, inverse argument, and bias
   setup are aligned and fully visible.
5. The exact measure interval, zero-product tail argument, summability
   transition, and endpoint conclusion have no clipped display or proof end.
6. Both closed directive specializations, exact-control scope, HOLD boundary,
   and the beginning of the bibliography render correctly.
7. All remaining references are present and readable. The unused lower-page
   white space is benign; there is no unintended blank page.

No overlap, cropping, broken hyperlink coloring, missing symbol, malformed
proof terminator, footer collision, or page-transition defect was observed.

## Frozen manifest and release boundary

`SHA256SUMS` covers exactly these ten files:

1. `main.tex`;
2. `references.bib`;
3. `code/verify_marked_s_adic.py`;
4. `README.md`;
5. `CLAIMS_EVIDENCE.md`;
6. `CONTROL_RESULTS.md`;
7. `BUILD.md`;
8. `HOSTILE_REVIEW.md`;
9. `FINAL_QA.md`;
10. `main.pdf`.

The final `sha256sum -c SHA256SUMS` replay passes every entry. This seal is
for reproducibility only; derived auxiliary LaTeX files are deliberately not
part of the ten-file manifest.

The bounded owner search remains negative evidence rather than a priority
proof. Public posting, submission, author contact, venue claims,
specialist-clearance language, and absolute novelty or priority language
remain **HOLD**.
