# C86 paper build

Build from this directory with

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

`main.pdf` is accepted only after two isolated deterministic builds agree
byte for byte, all fonts are embedded, references are resolved, and a visual
first-page inspection passes.
