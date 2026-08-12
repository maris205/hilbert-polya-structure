# HCS-C33 paper compilation report

Compilation was performed from `paper/` with

~~~bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
~~~

on 2026-08-12.  The released artifact is an eight-page A4 PDF produced by
pdfTeX 1.40.22:

- `main.pdf` SHA-256:
  `0e32c227126dda3e096f3c72a75a9d2a3215154175d5557e46a9218b207f3ba6`;
- main text: pages 1--7;
- references: pages 7--8;
- exact-ledger and scope appendices: page 8.

The final `main.log` has zero LaTeX/package errors, zero undefined
references or citations, zero warnings, and zero overfull or underfull
boxes.  `pdffonts` reports that every one of the 21 font subsets is embedded
and has a Unicode map.  `pdftotext` was used to verify the final theorem,
irreducibility, Kummer, Route-A, and claim-boundary language.  The first page
was also inspected visually after the final rebuild.
