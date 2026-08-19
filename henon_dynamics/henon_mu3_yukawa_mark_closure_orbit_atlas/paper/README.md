# C76 manuscript

`main.tex` is a compact theorem note for the finite support-closure orbit
atlas.  It uses the same anonymous, dependency-light layout as the C75 note.
Compile with:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The paper is intentionally self-contained and cites no external literature:
all numerical statements are tied to the canonical C76 evidence JSON and its
source-bound C75 authorities.
