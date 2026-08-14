# COMPILATION REPORT — SD-C20

**Build date:** 2026-08-14
**Engine:** pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022)
**Target:** main.tex to A4 PDF

## Clean build protocol

The diagnostic build products were removed first.  The final build then used
the following deterministic sequence:

~~~text
pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass 1
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass 2
pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass 3
pdflatex -interaction=nonstopmode -halt-on-error main.tex   # pass 4
~~~

All four LaTeX passes exited successfully and each reported
“Output written on main.pdf”.

## Final PDF

| item | value |
|---|---|
| pages | 14 |
| page geometry | 595.276 × 841.89 pt (A4) |
| file size | 539,782 bytes |
| SHA-256 | 987854729cb2293b161f7e9d28995a38cda7ce79a35d33f8e9a981499f381758 |
| PDF version | 1.5 |
| encryption | none |
| suspect objects | none |

## Warning, citation, and reference audit

The fourth-pass log was searched for “Warning”, “undefined”, “Overfull”,
“Underfull”, multiply defined labels, citation failures, reference failures,
and errors.  The search returned zero matches.

BibTeX loaded plainnat.bst and the 16-entry references.bib database without
warnings.  Every cited key resolved.  DOI/title metadata was checked against
publisher or Crossref records; the final database includes the correct
Boyle--Schmieding DOI 10.1017/etds.2015.87, Adachi--Sunada DOI
10.1016/0022-1236(87)90014-0, and the 2025 title
*Godsil--McKay Switchings for Gain Graphs*.

## Font audit

pdffonts found 33 font rows.  Every row is a Type 1 font and every row is
embedded and subsetted; all rows report Unicode mappings.  No bitmap or
unembedded font is present.

## Source hashes

| file | SHA-256 |
|---|---|
| main.tex | ab9fb83e81e0e116b5195fd6eff52f23070a5c5fea14ef5da6b6f9ce186e482d |
| references.bib | 91349e2310704b558b02ff5372b68f065040c174c8fdd00884a58b0955d809db |
| SOURCE_LOCK.md | 3e3d3503987de15ff294015eb8e10993f77c7220ed4498a4c3c521c7e6e08dc8 |

The modular LaTeX source comprises 1,201 lines across main.tex,
math_commands.tex, references.bib, and the section files.

## Visual inspection

Raster checks were performed on the title/status page, the TikZ overview,
the exact-standard-block/enumeration page, and the final scope-ledger page.
The figure, equations, tables, hyperlinks, page numbers, and appendix layout
are within the A4 text area and legible.  No clipping or overlap was found.

## Cleanup

After the audits above, generated auxiliary files were removed.  The
shareable build keeps main.pdf, main.tex, modular sources, the TikZ figure,
bibliography, and this report.
