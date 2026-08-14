# Compilation report

- **Status:** SUCCESS
- **Compiler:** `pdflatex`, `bibtex`, `pdflatex`, `pdflatex`
  (`latexmk` is not installed on this server)
- **PDF:** `paper/paper.pdf`
- **Pages:** 6 total, including references and appendix
- **Size:** 215951 bytes at the recorded build
- **Undefined references:** 0
- **Undefined citations:** 0
- **Stale section files:** 0
- **Embedded fonts:** all reported fonts embedded
- **Residual issues:** none affecting the build or claim boundary

The first attempt exposed a server-specific non-scalable T1 font-expansion
failure.  Removing the unnecessary `fontenc` import restored the same
Computer Modern setup used by predecessor papers.
