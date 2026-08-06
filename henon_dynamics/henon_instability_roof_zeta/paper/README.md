# Paper

main.pdf is the compiled 13-page research note. The LaTeX source is modular
under sections/, and the data-driven vector figure is under figures/.

Compile from this directory with:

    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    bibtex main
    pdflatex -interaction=nonstopmode -halt-on-error main.tex
    pdflatex -interaction=nonstopmode -halt-on-error main.tex

The environment does not provide latexmk, so the recorded build used the
manual equivalent above. There are no undefined references or citations, all
fonts are embedded, and the PDF figure uses TrueType rather than Type-3 fonts.

