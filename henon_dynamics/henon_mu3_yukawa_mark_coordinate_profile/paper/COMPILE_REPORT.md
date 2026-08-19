# C67 compile report

The final build used

```text
SOURCE_DATE_EPOCH=0 latexmk -C
SOURCE_DATE_EPOCH=0 latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The two-page letter PDF has no LaTeX errors, undefined references, overfull
boxes, TODO markers, or FIXME markers in the final log. All listed fonts are
embedded. Two clean builds were byte-identical with SHA-256

```text
cb37a923fe9dd0364a9b752bc6523621d86b3f16829f0805382cb188fb19d708
```
