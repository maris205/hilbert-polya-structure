# HCS-C50 paper compilation report

Status: **PASS; implementation provenance backfilled**

Compilation was performed on 14 August 2026 from `paper/` with

~~~text
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
~~~

The toolchain was latexmk 4.76 with pdfTeX 1.40.22 (TeX Live 2022).

## Build result

- output: `paper/main.pdf`;
- pages: 15;
- page size: A4;
- file size: 395170 bytes;
- SHA-256:
  `a44b1ac7f6a987a45a1c9a5d9677d0f8b401b81e9ae56b2dd97c0782b1b68a8c`;
- `main.tex` SHA-256:
  `bd17a9754208ef6a01b490b0bb528e7934c98a0bc1ee7fa6b95c00ad60519996`;
- `references.bib` SHA-256:
  `c985a29d83e69b2eed59a94ea0ede0b75d4a502ebd865b8b5b17cb78033730f9`.

The final log contains no LaTeX warning, overfull box, underfull box,
undefined citation, undefined reference, or rerun request. All nine
bibliography entries are cited, and every citation key resolves.

## PDF integrity

`pdfinfo` reports the title, author, subject, and keywords embedded in the
PDF metadata. `pdffonts` reports every font embedded and subsetted; no Type 3
font is present. Text extraction was checked for the title, abstract, main
theorem, Route-A tuple, declarations, exact-certificate appendix, and
bibliography.

Rendered-page inspection covered:

- page 1: title, abstract, and opening formulas;
- page 11: Det10/classical-Schatten firewall and Route-A table;
- page 12: exact evaluator tuple, next gate, and declarations opening; and
- page 15: finite validation table and complete bibliography.

No clipping, overlap, malformed glyph, broken table, or visibly unresolved
reference was found.

## Required manuscript content

The compiled paper includes Data and Code Availability, Ethics, CRediT
Author Contributions, Funding, Conflict of Interest, AI-use, and Limitations
statements. It also states the finite-bad-prime scope, the normalized
semifinite versus classical-trace firewall, and the absence of a proved full
Hénon functional equation or self-adjoint Hilbert--Pólya generator.

The PDF is frozen. Both Route-A records carry implementation commit
`c5e21168576f90ad12296849c7e9817a2d608c26`; the expanded release manifest
is refreshed only after this report and the provenance records are stable.
