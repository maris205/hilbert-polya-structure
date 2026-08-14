# COMPILATION REPORT

## Artifact

- Source: `main.tex` with seven main sections, one appendix, one pure-TikZ
  figure, and `references.bib`.
- Output: `main.pdf`.
- Pages: 14.
- Paper size: A4 (`595.276 x 841.89 pt`).
- PDF version: 1.5.
- File size: 455,114 bytes.
- SHA-256:
  `57e7ac235f1b6f697bd32a1464eea1da4440c4cb070293d4352fa3cbff26f5c4`.

## Clean build

The final artifact was rebuilt from a clean auxiliary state with the required
four LaTeX passes:

```text
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four `pdflatex` passes produced a 14-page PDF.  The final log contains no
LaTeX/package warnings, undefined references or citations, overfull boxes,
underfull boxes, or fatal errors.

## Typography and visual inspection

- All fonts reported by `pdffonts` are embedded and subsetted.
- The title page, source-lock status box, figure page, experiment table, route
  table, bibliography transition, and appendix were visually inspected.
- Figure 1 is vector TikZ only.  Fixed-width nodes and a vertical dashed
  generic-inventory branch prevent label or node overlap.
- The strict Route-A tuple and `ROUTE_A_REJECTED` label render without clipping.

## Cleanup

Build auxiliaries (`main.aux`, `main.bbl`, `main.blg`, `main.log`, and
`main.out`) were retained only through final validation and then removed.
The deliverable source, bibliography, and `main.pdf` remain reproducible by
the commands above.
