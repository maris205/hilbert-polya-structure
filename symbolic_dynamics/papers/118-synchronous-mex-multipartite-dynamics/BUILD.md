# P118 build record

Status: anonymous round-two repair build; external release HOLD.

Run from this directory:

    PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

## Round-two settled result

- verifier: PASS, 202,965 exact assertions across 15 parameter lanes;
- canonical transcript: 1,586 bytes and byte-identical to fresh stdout;
- LaTeX/BibTeX: four stages exited zero;
- `main_round0_original.pdf`: 7 A4 pages, 378,072 bytes;
- `main_round1.pdf`: 7 A4 pages, 379,370 bytes;
- `main_round2.pdf` and current `main.pdf`: byte-identical, 7 A4 pages,
  380,381 bytes;
- bibliography: 6 cited entries, all resolved and none uncited;
- settled diagnostics: zero warnings, errors, undefined references or
  citations, box warnings, and rerun requests;
- fonts: 27/27 embedded, subsetted, and Unicode mapped;
- metadata: empty Author, no dates, no form, JavaScript, or encryption.

Round one adds the missing \(m=g\) branch to quotient exhaustion, separates
the edgeless \(k=1\) case, and credits the 2018 synchronous-protocol neighbor.
Round two removes a false converse about periodic labelled colourings,
states the exact lift/intertwining relation, and adds complete quotient
transition and two-step-entrance controls.  Metadata controls suppress dates
and identity-bearing fields.
