# P195 Review-A build and PDF QA

## Frozen replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
exit: 0
```

## Reviewer replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a_p195.py | cmp - CANONICAL.txt
expected exit: 0
transitions: 2,223,278
checks: 6,551,607
digest: 80a123832d9e869492b8e833db108521319a4715718498294a140c819033d0d9
```

## Round-0 cold build

Only frozen `main.tex` and `references.bib` were copied to a fresh temporary
directory.  With `SOURCE_DATE_EPOCH=1704067200` and `TZ=UTC`, the sequence
`pdflatex; bibtex; pdflatex; pdflatex` produced:

```text
pages: 3
page size: A4, 595.276 x 841.89 pt
bytes: 315,629
SHA-256: bc0723b0b4417125122a40784f444565cdbd5565c5b65ac477042be2c209de3f
warning/bad-box/unresolved/fatal matches: 0
font rows embedded/subsetted/Unicode: 23/23/23
encrypted: no
forms: none
JavaScript: no
metadata stream: no
```

The hash equals the preserved `main_round0_original.pdf`.

## Accepted-delta cold build

The repaired `main.tex` and `references.bib` were copied to a second fresh
directory and rebuilt with the same four-pass recipe:

```text
pages: 3
page size: A4, 595.276 x 841.89 pt
bytes: 318,096
SHA-256: d5dbac8ed78f1f3eccc3c7aeccda852e6f44f77a513091032120254119ff9c0a
warning/bad-box/unresolved/fatal matches: 0
font rows embedded/subsetted/Unicode: 23/23/23
```

The cold hash equals the repaired `main.pdf`.

## Visual inspection

Both frozen and repaired three-page PDFs were rasterized at 120 dpi and
inspected individually.  The
long title, abstract, theorem displays, EGF formulae, local inverse formula,
and bibliography are legible and inside the page box.  No clipping, overlap,
missing glyph, malformed display, stranded heading, or unintended blank page
was found.

Build/PDF decision: `PASS`; P195-A1/A2 are accepted and there are zero open
build findings.
