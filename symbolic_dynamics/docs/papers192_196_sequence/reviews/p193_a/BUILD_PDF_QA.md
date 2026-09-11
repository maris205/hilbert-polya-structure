# P193 Review-A build and PDF QA

## Frozen replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
exit: 0
```

## Reviewer replay

```text
PYTHONDONTWRITEBYTECODE=1 python3 verify_review_a_p193.py | cmp - CANONICAL.txt
expected exit: 0
transitions: 46,233
checks: 917,785
digest: eaec02e654c02452ec757536456a3743a9ba333a78d2641dc61c5002fb5e7827
```

## Round-0 cold build

Only frozen `main.tex` and `references.bib` were copied to a fresh temporary
directory.  With `SOURCE_DATE_EPOCH=1704067200` and `TZ=UTC`, the sequence
`pdflatex; bibtex; pdflatex; pdflatex` produced:

```text
pages: 5
page size: A4, 595.276 x 841.89 pt
bytes: 389,209
SHA-256: e41e171c8f412cf93aae9510052ed0d8ad165125be1bd4c04133f1b410048267
warning/bad-box/unresolved/fatal matches: 0
font rows embedded/subsetted/Unicode: 29/29/29
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
pages: 5
page size: A4, 595.276 x 841.89 pt
bytes: 390,196
SHA-256: b5b2f4e77bada6229a0716d9780a871f95b8e6ba75fa2c9e6794b5bf524ad0d9
warning/bad-box/unresolved/fatal matches: 0
font rows embedded/subsetted/Unicode: 29/29/29
```

The cold hash equals the repaired `main.pdf`.

## Visual inspection

Both frozen and repaired five-page PDFs were rasterized at 120 dpi and
inspected individually.  The
title, abstract, equations, theorem blocks, table, declarations, and
bibliography are visible and within the page box.  No clipping, overlap,
missing glyph, malformed display, stranded heading, or unintended blank page
was found.

Build/PDF decision: `PASS`; P193-A1 is accepted and there are zero open build
findings.
