# P117 build record

Status: anonymous round-two internal freeze; external release HOLD.

Run from this directory:

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Expected toolchain: Python 3.12, pdfTeX from TeX Live, and BibTeX 0.99d.

## Round-two settled result

- verifier: PASS, 1,529,158 exact assertions;
- literal word orders: 1 through 16;
- even parity words: 349,524 through length 18, including 349,488 mixed
  four-unit cost-drop cases;
- canonical verifier transcript: 432 bytes and byte-identical to fresh
  stdout;
- LaTeX/BibTeX: four stages exited zero;
- `main_round0_original.pdf`: 6 A4 pages, 320,849 bytes;
- `main_round1.pdf`, `main_round2.pdf`, and current `main.pdf`:
  byte-identical, 6 A4 pages, 321,439 bytes;
- bibliography: 5 cited entries, all resolved and none uncited;
- settled diagnostics: zero warnings, errors, undefined references or
  citations, box warnings, and rerun requests;
- fonts: 23/23 embedded, subsetted, and Unicode mapped;
- metadata: empty Author, no dates, no form, JavaScript, or encryption.

The round-one change repairs the even-length domain of the realization
lemma, the empty-eroder convention, and the odd witness's final collapse. It
also adds direct boundary, eroder, realization, and cost-drop controls. PDF
metadata controls suppress dates and identity-bearing fields.  The second
review found no further source change necessary; `main_round2.pdf` is the
byte-identical signed freeze.
