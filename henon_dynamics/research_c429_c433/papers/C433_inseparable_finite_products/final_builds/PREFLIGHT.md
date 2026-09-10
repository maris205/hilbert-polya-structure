# C433 final-build preflight

Observed 2026-09-10 UTC, before either final compilation.

The literal paper root is
/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c429_c433/papers/C433_inseparable_finite_products.

Each ancestor from / through that root, and its sections directory,
was tested as a directory and not a symlink. The ten input paths below
were tested as regular, nonsymlink files with link count exactly one.
The final_builds directory and FINAL_BUILD_REPORT.md were absent
(including no dangling symlink) before creation. The final_builds,
clean01/source, clean02/source and both sections directories were
created explicitly fresh; their types and nonsymlink status were then
checked again. The observations are not a hostile-concurrency or
filesystem-snapshot guarantee.

Input path | Bytes | Link count
--- | ---: | ---:
main.tex | 2495 | 1
references.bib | 1277 | 1
sections/01_introduction.tex | 3132 | 1
sections/02_statement.tex | 4523 | 1
sections/03_cycles.tex | 5088 | 1
sections/04_extractor.tex | 4099 | 1
sections/05_transfer.tex | 6001 | 1
sections/06_rank.tex | 4844 | 1
sections/07_decision.tex | 2941 | 1
sections/08_conclusion.tex | 1938 | 1

Input hashes are preserved verbatim in INPUT_HASHES.sha256. Each
copied input in each fresh source directory passed byte comparison
against its original and a regular/nonsymlink/single-link check.
Only these ten files were copied. Macros are inline; the extensionless
section declarations resolve to the eight named .tex files. The bounded
source declaration scan found no additional local input or figure.

Reviewed PDF before building:

- main.pdf: regular, nonsymlink file; link count 1; 374934 bytes.
- SHA256: 489a1038a9e6f27f589e63b2be6dfe69485a6bd2ab6672360d4407b3ea49a7fa.
- 11 pages, US letter, PDF 1.5; producer pdfTeX-1.40.22.

Observed executable paths:

/usr/bin/latexmk
/usr/bin/pdflatex
/usr/bin/bibtex
/usr/bin/pdfinfo
/usr/bin/pdffonts
/usr/bin/pdftotext
/usr/bin/pdftoppm
/usr/bin/kpsewhich

Observed tool versions:

- Latexmk, John Collins, 20 November 2021. Version 4.76.
- pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian).
- kpathsea version 6.3.4/dev.
- pdfTeX compiled with libpng 1.6.37, zlib 1.2.11, xpdf 4.03.
- BibTeX 0.99d (TeX Live 2022/dev/Debian).
- pdfinfo, pdffonts, pdftotext, pdftoppm: Poppler 22.02.0.

The system bibliography style resolved to
/usr/share/texlive/texmf-dist/bibtex/bst/base/plain.bst,
SHA256 19f2cf88686b86aaa8e65d5f0313a92499815761e04b42e84ea2c3dc3685ada9.
System package/font inputs are additionally recorded by each actual
build's main.fls and engine log. No package or executable was installed
or modified.

The paper-compile skill was read in full. The explicit final-build
authorization overrides its cleanup/source-repair/retry examples:
there is no cleanup, source repair, third build, venue page limit or
submission action here.
