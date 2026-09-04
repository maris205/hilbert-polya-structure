# P191 Review A — source-only build and PDF QA

## Cold build

**PASS.**  Only the frozen `main.tex` and `references.bib` were copied to a
fresh temporary directory.  Under `SOURCE_DATE_EPOCH=1704067200` and `TZ=UTC`,
the sequence `pdflatex`, `bibtex`, `pdflatex`, `pdflatex` completed normally.
The settled log contains no warning, undefined citation/reference, rerun
request, overfull/underfull box, fatal error, or emergency stop.

The cold artifact is byte-identical to the immutable Round-0 PDF:

```text
pages: 4
bytes: 380787
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
SHA-256: d8675928ecfe528b950af5402097b5f69657efc9cba7c8eb0bb5c27ec96df78b
byte comparison: PASS
```

## Mechanical checks

- `pdfinfo`: unencrypted; no forms, JavaScript, metadata stream, or identity
  metadata in title/author/subject/keywords/creator/producer.
- `pdffonts`: 28 of 28 rows embedded, 28 of 28 subsetted, and 28 of 28
  Unicode-mapped.
- text layer: 223 lines / 16,011 bytes; the two main theorems, `K_*`, CRediT
  roles, references, anonymity label, and `HOLD_EXTERNAL` are extractable.
- source/bibliography: five distinct cite keys and exactly the same five
  bibliography keys; no unresolved marker.

## Visual checks

All four pages of the byte-identical frozen/cold artifact were inspected.
The title/abstract, divisor recurrence, sharp-clock proof, global recurrence,
interval factors, product, table, declarations, and bibliography have no
clipping, overlap, malformed formula, margin escape, corruption, or
unintended blank page.  `CRediT roles.` has one full stop.  The displayed
`K_*` formula visibly leaves the final endpoint untested.

No manuscript/PDF defect was found.  Historical finding `P191-A-MI-01`
concerned only companion `SOURCE_VERIFICATION.md` metadata and its accepted
repair did not require recompiling the paper.  `main_round1.pdf` and live
`main.pdf` remain byte-identical to the frozen artifact above.  Build success
is artifact evidence, not theorem proof or owner clearance.
