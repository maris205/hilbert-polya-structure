# Paper package

`paper.pdf` is the release copy of *Which Operator Owns the Zeta? Koopman and
Frobenius Ledgers of an Arithmetic Suspension*.

## Contents

- `manuscript.tex`: XeLaTeX source.
- `references.bib`: source-locked BibTeX database.
- `figures/operator_ownership.tex`: native TikZ figure.
- `paper.pdf`: release PDF.
- `manuscript.pdf`: direct build target.

The manuscript contains an English abstract, a simplified-Chinese abstract,
seven theorem/lemma/corollary results, an operator-ownership figure, typed
Route-A/Route-B decisions, limitations, reproducibility declarations, CRediT,
funding, conflict-of-interest and AI-assistance statements.

## Build

```bash
latexmk -xelatex -interaction=nonstopmode -halt-on-error manuscript.tex
cp manuscript.pdf paper.pdf
```

The release build is 9 pages.  BibTeX and cross-references resolve cleanly;
the log has no undefined citations/references, overfull boxes, missing glyphs,
or package errors.  One nonfatal underfull box occurs in the deterministic
controls paragraph.  See `../notes/release_audit.md` for the post-build audit.
