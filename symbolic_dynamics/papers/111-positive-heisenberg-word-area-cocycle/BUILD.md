# Build Record — P111

Status: **FINAL INTERNAL MECHANICAL PASS / EXTERNAL HOLD**.

Run from this directory:

```text
python3 code/verify.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

## Toolchain

```text
Python 3.12.3
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
```

The fresh verifier passed **421,285 exact assertions**, and a second fresh
run was byte-identical to `code/verify.out`. All four LaTeX/BibTeX stages
exited zero. The final `main.log`/`main.blg` scan has no actual match for
`Warning`, `Overfull`, `Underfull`, `undefined`, `multiply defined`, or
`Error` (the strings `infwarerr` and BibTeX's summary `warning$ -- 0` are
nonwarnings).

## Author-stage PDF artifact

```text
pages=7 total
references_begin=page 7
page_size=A4 (595.276 x 841.89 pt)
pdf_version=1.5
bytes=313738
sha256=775b225c95e91c1e7d1e08417c6dc916580d21bafde4476f9960e97615f7036d
```

An immediate deterministic rebuild reproduced the same PDF hash. The
deterministic settings suppress creation dates and trailer identifiers.
`pdftotext -layout` recovered 24,459 bytes and 383 lines, including the
title, all theorem/proof headings, owner/HOLD boundary, and four references.
`pdffonts` reports 21 entries; all are embedded, subsetted, and
Unicode-mapped. All seven pages were rendered to PNG and inspected; a
detected missing backslash before `\qquad` in the product convention was
repaired before this final author build, and the rerender passed.

The author-stage bibliography contained four DOI-checked records. This
build record does not certify direct-owner completeness or authorize
external release.

## Review-A rebuild

Review A added direct-owner subtraction for the fair binary specialization:
Janson (2012), DOI 10.37236/2188, and Takács (1986), DOI
10.1016/0378-3758(86)90016-9. The bibliography now contains six
DOI-checked records. No theorem or verifier code changed.

A fresh verifier run again passed **421,285 exact assertions** and was
byte-identical to code/verify.out. The full four-stage build exited zero;
the final log scan found no warnings, undefined citations/references,
overfull/underfull boxes, multiply defined labels, or errors. An additional
determinism pass reproduced the PDF hash.

    pages=7 total
    references_begin=page 7
    page_size=A4 (595.276 x 841.89 pt)
    pdf_version=1.5
    bytes=316032
    sha256=b8e12c56d072ef7e3fa7fe6c478256f6fbeb6da2dc37126453e079174c5c4476

pdftotext -layout recovered 25,570 bytes and 397 lines. pdffonts reported 21
entries, all embedded, subsetted, and Unicode-mapped. All seven pages were
freshly rendered at 150 dpi and inspected; no clipping, overlap, broken
citation, malformed equation, or illegible bibliography was found.

## Final production freeze

After both hostile ledgers were consolidated, the verifier was run once more
from the frozen source tree and matched `code/verify.out` byte for byte.  The
prescribed four-stage build passed, and an immediate additional pdfLaTeX pass
reproduced the same PDF hash.  The final log/BibTeX, metadata, font, searchable
text, citation-closure, sentinel, and seven-page visual checks all pass.

```text
assertions=421285
bibliography=6/6 cited and resolved
pages=7
bytes=316032
pdftotext_layout=25570 bytes, 397 lines
fonts=21/21 embedded, subsetted, Unicode-mapped
sha256=b8e12c56d072ef7e3fa7fe6c478256f6fbeb6da2dc37126453e079174c5c4476
```

`FINAL_QA.md` records the complete gate and `SHA256SUMS` seals the evidence
package.  External circulation remains **HOLD**.
