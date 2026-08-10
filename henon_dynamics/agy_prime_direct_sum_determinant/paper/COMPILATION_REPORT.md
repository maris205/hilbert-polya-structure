# C28 paper compilation report

## Outcome

- **Status:** PASS
- **Document class:** standard article, 11 pt
- **Main source:** main.tex
- **PDF:** main.pdf
- **Pages:** 17
- **PDF size:** 353,157 bytes
- **PDF SHA-256:** 93593889bd04bbdaa62741f90d03f6005bba5d1f9ebdf9dd77058167244580a1
- **Page format:** US Letter, 612 by 792 points
- **PDF version:** 1.5

## Build environment and command

- latexmk 4.76
- pdfTeX 3.141592653-2.6-1.40.22
- BibTeX 0.99d
- TeX Live 2022/dev

Final forced rebuild:

    latexmk -g -pdf -interaction=nonstopmode -halt-on-error main.tex

The forced rebuild completed at 2026-08-10 19:51:25 CST.  A final
up-to-date latexmk status transcript is captured in compile.log.

## Source inventory

- main.tex
- math_commands.tex
- references.bib
- 11 section files under sections/
- generated bibliography main.bbl
- compiled paper main.pdf

All LaTeX input targets used by main.tex exist.  The bibliography contains
seven cited, primary or standard monograph sources with verified DOI or
arXiv metadata.

## Warning and reference audit

The final main.log and forced-rebuild compile.log contain:

- 0 LaTeX warnings;
- 0 undefined citations;
- 0 undefined references;
- 0 multiply defined labels;
- 0 overfull boxes;
- 0 underfull boxes.

Static source checks found:

- 0 CR or NUL control characters in the four project documents and
  paper sources;
- 0 TODO, TBD, FIXME, VERIFY, or placeholder markers;
- no malformed nested inline-math delimiters;
- no global fractional-power notation for the normalized determinant.

The normalized determinant is consistently written as

    \exp\!\left[p^{-2}\Log_0\cD_p(s,u)\right],

with the logarithm branch fixed at the origin.

## PDF audit

pdffonts reports 24 font subsets; every listed font is embedded and has a
Unicode map.  The pdftotext layout extraction was searched for unresolved
markers and literal (p)/(p^2) placeholder-style prose; none were found.  The
first page was rasterized and inspected: the title, abstract, first displayed
theorem formula, introduction, and margins render cleanly.

## Scope audit

The compiled paper retains the following firewalls:

- the sharp if-and-only-if Schatten threshold is proved with a locally
  uniform finite-head/uniform-tail lower bound and
  \(m_{\delta,K}>0\);
- quadratic \(L\)-data are used only for \(D_w\ne0\), with the odd-prime
  correction \(-\chi(2)2^{-\zeta}\);
- the normalized-character application is restricted to the source-locked
  positive AGY monoid and a common compact-uniform \(u\)-disc;
- P073 is called a full-C24 dimension-normalized **MARKED** control and
  never a C26 induced branch;
- the prime direct sum is not labeled an adelic Weil representation.
