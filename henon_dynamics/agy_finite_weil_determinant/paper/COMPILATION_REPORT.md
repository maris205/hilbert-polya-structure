# HCS-C27 compilation report

## Release build

- Date: 2026-08-10
- Engine: pdfLaTeX through `latexmk`
- Source: `paper/main.tex`
- Output: `paper/main.pdf`
- Length: 15 pages
- PDF size: 342900 bytes in the release build
- Bibliography: BibTeX, with all citations resolved

## Verification

The release build completed with exit status zero. The final log contains:

- no undefined citations or references;
- no overfull or underfull boxes;
- no multiply defined labels;
- no request for another LaTeX rerun.

The remaining `hyperref` messages concern mathematical notation removed from
two PDF bookmarks; they do not affect the printed manuscript, cross-references,
or mathematical content.

## Rebuild

```bash
cd henon_dynamics/agy_finite_weil_determinant/paper
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```
