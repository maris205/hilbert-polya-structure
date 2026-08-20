# C78 manuscript

`main.tex` is a self-contained theorem note for the exact deletion/repair
polynomial.  It has no external bibliography or venue style dependency.

Compile from this directory with:

```bash
SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

For the release gate, build twice in isolated directories and compare the
SHA-256 digests of `main.pdf`.  The canonical evidence hash is
`728d6462b337e3b22fe267ae9388da476a0f6409cc64a17ca659f53f1a8126ae`.
