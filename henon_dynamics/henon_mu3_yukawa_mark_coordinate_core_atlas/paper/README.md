# C72 paper

Build with `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex`.
The final prefreeze gate uses two isolated clean builds with
`SOURCE_DATE_EPOCH=0` and requires byte-identical PDFs.
