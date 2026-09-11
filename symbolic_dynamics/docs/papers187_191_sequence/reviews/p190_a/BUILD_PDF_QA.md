# P190 Review A — source-only build and PDF QA

## Cold-build result

**PASS_DELTA_ACCEPTED.**  A new fresh temporary directory was populated with
only the Round-1 `main.tex` and unchanged `references.bib`.  The following
sequence was run under the author's deterministic environment:

```bash
SOURCE_DATE_EPOCH=1704067200 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1704067200 TZ=UTC bibtex main
SOURCE_DATE_EPOCH=1704067200 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
SOURCE_DATE_EPOCH=1704067200 TZ=UTC pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The settled artifact was byte-identical to `main_round1.pdf`:

```text
pages: 4
bytes: 383748
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
SHA-256: 81c785768621a2c3450fc67eeabc9b91d8cfda67d1061aad851844b5dd68905d
frozen byte comparison: PASS
```

The initial-pass unresolved-reference messages disappeared after BibTeX and
the settling passes.  The final `main.log` has zero LaTeX/package warnings,
undefined citations/references, rerun requests, overfull/underfull boxes,
fatal errors, or emergency stops.

## Mechanical PDF checks

- `pdfinfo`: four A4 pages; unencrypted; no forms; no JavaScript; no metadata
  stream; title, author, subject, keywords, creator, and producer blank.
- `pdffonts`: 29 of 29 rows embedded, 29 of 29 subsetted, 29 of 29 Unicode
  mapped.
- text extraction: the theorem, declarations,
  references, anonymous label, and `HOLD_EXTERNAL` boundary are extractable.
- exact citation keys: five in the source and five matching bibliography
  entries; no unresolved marker remains.

## Visual inspection

All four pages retain the Round-0 layout; pages 3 and 4 were cold-rendered and
inspected at 144 dpi after the delta.  The title block, display equations,
theorem breaks, table, declarations, and bibliography have no clipping,
collision, corruption, unintended blank page, or margin escape.  The PDF is
anonymous in the manuscript sense: it prints `ANONYMOUS` and no affiliation,
email, grant identifier, or repository identity.

Both historical visible defects are closed:

1. Page 3, Eq. (11), now renders the two intended indices without an empty
   leading field: `P190-A-MI-01 ACCEPTED`.
2. Page 4 renders the declaration heading as exactly `CRediT.`:
   `P190-A-MI-02 ACCEPTED`.

The PDF text-layer diff against Round 0 contains those two token changes plus
their deterministic horizontal reflow; it exposes no content change to a
theorem, proof, table, citation, owner statement, or lifecycle boundary.  No
new PDF defect was found.  Source-only build success is artifact evidence,
not mathematical proof or ownership clearance.
