# C65 compile report

Command:

```text
SOURCE_DATE_EPOCH=0 latexmk -C
SOURCE_DATE_EPOCH=0 latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The final clean build completed with no LaTeX errors, undefined citations, or
undefined references. The only warnings in the captured transcript are the
normal first-pass BibTeX warnings; the final main.log is clean. The proof
paragraph has no overfull or underfull boxes.

The PDF has 2 pages on letter paper, all listed fonts are embedded, and two
independent clean builds produced the same SHA-256:

```text
2bf84d08510f8de277ea4e1897efd886084fed9aceefcb9528824a8f07088362
```
