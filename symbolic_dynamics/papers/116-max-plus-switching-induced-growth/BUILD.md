# Author Build Record

Status: **PASS / anonymous author-stage build / external HOLD**.

This is a reproducible author build record after hostile-review repairs, not
a final-QA report, release approval, or package hash seal.

## Environment

```text
working directory: papers/116-max-plus-switching-induced-growth/
LaTeX engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
bibliography: BibTeX 0.99d, plainnat
Python: 3.12.3; standard-library verifier; no external package
latexmk: unavailable in this environment
```

Because `latexmk` is unavailable, the source was built with the equivalent
manual sequence:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Compiled artifact

```text
PDF: main.pdf
Pages: 10
File size: 419,711 bytes
PDF version: 1.5
```

All 29 font rows reported by `pdffonts` are embedded, subset, and Unicode
mapped. The manuscript is
anonymous (`\author{Anonymous}`) and contains no affiliation, email address,
acknowledgment, grant identifier, external repository link, or author date.

## Clean-log counts

The settled `main.log` and `main.blg` contain:

```text
LaTeX/package warnings: 0
undefined references: 0
undefined citations: 0
multiply-defined labels: 0
overfull hbox/vbox: 0
underfull hbox/vbox: 0
rerun requests: 0
BibTeX warnings/errors: 0
```

All eight files in `sections/` are referenced by `main.tex`; there are no
orphan section sources. All 14 BibTeX entries are cited, and every cited key
is present in `references.bib`. PDF text extraction and visual inspection of
the Perron-derivative display confirm that the former literal `qquad` token
is gone and the intended spacing is present.

## Exact-control build

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python code/verify.py
```

Result:

```text
PASS
exact assertions: 1,183,356
literal words: 131,071 through n <= 16
biased law/PGF horizon: n <= 32
bytecode artifacts: 0
```

Exact stdout is retained as `code/verify.out`. A fresh 34-line, 974-byte run
compared byte-for-byte equal to that stored transcript. The new reset lane
classifies all words through length three, while the support lane checks
every parity-compatible height and its explicit witness. See
`CONTROL_RESULTS.md` for lane counts and evidence limitations.

## Scope boundary

No Git command, final-QA artifact, checksum/hash file, public posting,
submission action, novelty decision, or priority claim was produced in this
author-stage build. `HOSTILE_REVIEW.md` is only the repair-resolution ledger;
external circulation remains HOLD.
