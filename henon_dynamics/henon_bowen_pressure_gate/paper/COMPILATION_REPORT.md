# Compilation report

## Build status

- Status: **PASS**
- Final build: 2026-08-11 13:07 UTC
- Entry point: `main.tex`
- Command: `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`
- Engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
- Driver: latexmk 4.76
- Bibliography: BibTeX with `plainnat`; ten source records
- Output: `main.pdf`
- Pages: 9
- Page size: A4, 595.276 by 841.89 pt
- PDF version: 1.5
- PDF size: 345,092 bytes

## Final hashes

```text
565e781b94a2e8399f7b8ce416e09a23adfd40c7b2e466f715c53b0e832dc6d0  main.pdf
9921014314cd7229d658f6876c210dee6a80fbfef5a37be2f287041495d428bb  main.tex
5f9f48d0fd1999dc51e5c24d8fa3c05854af5567626404971346ba938ad356ab  references.bib
```

## Log audit

The converged `main.log` was searched for errors, undefined references and
citations, multiply defined labels, LaTeX/package warnings, and overfull or
underfull boxes.  All final counts are zero.

## Semantic and rendering audit

- `pdftotext -layout` contains no unresolved references, release placeholders,
  or draft markers.
- A byte-level scan of `main.tex`, `math_commands.tex`, `references.bib`, and
  all ten section files found no carriage returns or unintended C0 control
  characters.
- All fonts reported by `pdffonts` are embedded and subsetted with Unicode
  maps.
- The first page was rendered to a bitmap and visually inspected; the title,
  abstract, principal expansion bound, root bracket, and opening section are
  legible without clipping.
- The extracted PDF preserves the distinction between the suspension-zeta
  pressure boundary, an inverse-determinant zero convention, and a
  Hilbert--P\'olya spectral claim.
