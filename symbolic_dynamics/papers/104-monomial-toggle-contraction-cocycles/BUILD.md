# Build record — P104

Status: **final internal mechanical PASS / external HOLD**.

Run from this directory:

```text
python3 code/verify_monomial_toggle.py
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

The exact verifier passed **741,486 assertions**. All four LaTeX/BibTeX
stages exited zero. The final `main.log` and `main.blg` scan has no match for
`Warning`, `Overfull`, `Underfull`, `undefined`, `multiply defined`, or
`Error`.

## Final artifact

```text
pages=5 total
main_body_through_conclusion=5 pages (references begin on page 5)
page_size=A4 (595.276 x 841.89 pt)
pdf_version=1.5
bytes=307296
sha256=194185a2d754b1d3c5f2d958a8f2282612670ea159c56f9767331b78be14c71a
```

`pdftotext -layout` recovered 17,326 bytes and includes the title, abstract,
all theorem/proof headings, the HOLD statement, collision firewall, and all
three references. `pdffonts` reports 23 entries; every entry is embedded,
subsetted, and Unicode-mapped. Deterministic PDF settings suppress volatile
creation metadata and trailer identifiers.

The hash above is canonical for this internal freeze.  Two independent
hostile reviews found no theorem repair, `FINAL_QA.md` records the final
inspection, and `sha256sum -c SHA256SUMS` passes entry by entry.  External
release remains **HOLD**.
