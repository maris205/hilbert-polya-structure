# Author-side build record

Date: 2026-09-01 UTC.  External status: `HOLD_EXTERNAL`.

## Canonical verifier replay

```bash
cmp -s code/verification_output.txt \
  <(PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py)
```

Result: `cmp=0`.  The replay completed in approximately 22 seconds in the
current environment and ended with

```text
TOTAL_ASSERTIONS=18504770
STATUS=PASS
```

## Settled manuscript build

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages exited zero.  The settled log/BLG contain zero LaTeX or
package warnings, bad boxes, undefined citations/references, multiply defined
labels, or actionable rerun requests.

## Isolated reproducibility build

Only `main.tex` and `references.bib` were copied to the fresh directory
`/tmp/p137-isolated.c0wqXx` and rebuilt with the same four stages.  The
isolated `main.pdf` compared byte for byte with the paper-local PDF
(`cmp=0`), and the isolated settled warning scan returned zero hits.

## PDF audit

```text
pages=5
page_size=A4 (595.276 x 841.89 pt)
file_size=400794 bytes
pdf_version=1.5
encrypted=no
forms=none
javascript=no
metadata_stream=no
visible_author=Anonymous
pdf_author_metadata=blank
fonts=33
nonembedded_fonts=0
```

All five pages were rasterized at 130 dpi and inspected.  No clipping,
collision, malformed display, orphaned heading, or illegible reference was
found.  Page 5 contains the five-item bibliography and intentional residual
whitespace.

## Frozen core hashes

```text
ee654e1de7900435356ec258761c58603aa8b028eccad1c3d9020a907c5a89a9  main.tex
707964a92855a3ffba09743ce1a14bc4dad9bd6f3e1ab1c3e249bcedfa81b3be  references.bib
7f21edb43343eb6889816c875c6a840fe0c2992de5364e299af536294b3bd5f0  main.pdf
920dfc55087f617f4e1fd1d8febfadca75664c14de9375ea7be3eda579b33128  code/verify.py
7ae1064fd1a2b585c77702d4af04c5acb5934be90d31c5e4f0da8f2e9a049df6  code/verification_output.txt
```

These are author-side draft pins, not an external-release freeze or owner
clearance.
