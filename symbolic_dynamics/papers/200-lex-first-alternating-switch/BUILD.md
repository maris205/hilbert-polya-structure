# P200 Round 0 build and replay

pdfLaTeX and BibTeX are installed. latexmk is unavailable, so use this
equivalent explicit sequence from the paper directory:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

Only main.tex and references.bib are source inputs. The two fresh
round0_snapshot/cold_build_1 and cold_build_2 directories start with
those files only, run the full sequence, and yield the same four-page PDF.
PDF SHA-256: 7226b56257356fe3869a957983e0c92a7dbc79470f3e504f0f031c4b6248b3ea.
Source SHA-256: 0827a2bf6d3162699074bbfbe5152108bd9bda897c8b1a08e924b514cc83e8ea.
All fonts are embedded; identity/date metadata is suppressed. No undefined
references or citations, overfull boxes or remaining TeX warnings occur.

Reproduce the verifier with:

    python3 -B code/verify.py

Two fresh full runs in code/RUN1.txt and RUN2.txt match CANONICAL.txt:
9f1c320e2a79248ae2c9ba9b04bfee45540b3063e6d137f12996b898e9715f83.
Each run checks 13 boxes/273,040 complete states and 38 wide witness
itineraries, totaling 3,595,488 assertions. This is an author verifier
adapted from the author's earlier Stage-1 independent control, not a
new independent paper reviewer.

main_round0_original.pdf and round0_snapshot/ are immutable after
handoff. Later revisions must preserve their bytes and manifests.
