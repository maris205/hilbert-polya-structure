# C106 paper build

`main.tex` is the short paper generated from the exact evidence artifact. Compile with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The release manifest excludes LaTeX auxiliary files and records the final PDF hash.
