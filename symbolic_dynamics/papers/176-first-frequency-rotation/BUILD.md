# Build record — P176

The first section is the immutable author Round-0 receipt.  The live Round-2
build superseding it is recorded at the end of this file.

**Build date:** 2026-09-03 UTC  
**Status:** `AUTHOR_ROUND0_PASS / AMBER_INTERNAL_NEAR_P166 / HOLD_EXTERNAL`

## Toolchain

```text
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
Python 3.12.3
pdfinfo / pdffonts 22.02.0
```

`latexmk` was unavailable, so the explicit deterministic sequence was used:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four commands exited zero.  The settled log contains no LaTeX/package
error, undefined citation/reference, multiply defined label, overfull box,
or underfull box.  The three bibliography entries are all cited and resolve
in `main.bbl`.

## Source-only reproducibility

Two fresh temporary directories received only `main.tex` and
`references.bib`.  Each ran the four-command sequence above with exit codes
`0 0 0 0`.  Neither settled log contains a warning or box defect.  Both cold
PDFs and the working-tree PDF have the same SHA-256:

```text
5a8977524f5f7f5f654442bb3ac98cf74872de297277e9ffb0ff5c23878e69ba
```

Both byte comparisons returned zero.  The compact command tails are retained
in `build_cold1.log` and `build_cold2.log`.

## PDF audit

```text
pages:             4
paper:             A4, 595.276 x 841.89 pt
size:              395,769 bytes
fonts:             all embedded (Type 1 subsets)
metadata fields:   Title/Author/Creator/Producer blank
JavaScript:        none
encryption:        none
```

All four rendered pages were inspected.  The comparison table, displayed
formulas, long status strings, URLs, page headers, and references remain
inside the text block; no overlap, clipping, or blank page was observed.

`main_round0_original.pdf` was copied only after the settled build and is
byte-identical to `main.pdf`:

```text
5a8977524f5f7f5f654442bb3ac98cf74872de297277e9ffb0ff5c23878e69ba  main.pdf
5a8977524f5f7f5f654442bb3ac98cf74872de297277e9ffb0ff5c23878e69ba  main_round0_original.pdf
```

## Exact verifier audit

```bash
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 code/verify_p176.py
```

The run exited zero, reported `2,828,503` assertions, and a second fresh
process matched `code/CANONICAL.txt` byte for byte.

```text
c4a499855a50bc0ba64a78d69d3842a15375edcacdd9fad0e8dab39654956491  code/verify_p176.py
71720878a3498347661bad83838c3dbbc47c5c64c76ad7b70f6d5f02e7029190  code/CANONICAL.txt
```

## Live Round-2 build after Review B

The source/ownership and verifier-provenance repairs were compiled with the
same four-command sequence.  All five bibliography entries resolve.  The
settled Round-2 and final-cold logs contain no genuine warning, error,
undefined citation/reference, rerun request, or bad box.

```text
main.tex:             ff1f7d45c7ac7146a06f737a7187a9cedd451591ab9cbffeccf2d35eadc5874a
references.bib:       f47ccab745c702d4024276abb40d0fa5426df71cbab1e461749b9c609aab7307
main.pdf/round2:      c13ca3f5e3673bb5dd9c01bdf7c8913f78425cdbfeb2a52e2d9b096a34122db4
live verifier:        2dd56b882925c908565a9a213c42db7acccbf4fc214b54460619b71fe0587b50
live canonical:       3d0947a4df32f8e583e28d1964a52523602d61c64dde7b259bfdd15e71e4003b
pages / bytes:        4 / 397,525
font rows:            31/31 embedded, subsetted, Unicode mapped
isolated cold builds: 2/2 byte-identical to main.pdf
```

`main_round0_original.pdf` and `main_round1.pdf` remain byte-identical at
SHA-256 `5a8977524f5f7f5f654442bb3ac98cf74872de297277e9ffb0ff5c23878e69ba`;
`main.pdf` and `main_round2.pdf` are byte-identical at the live hash above.
