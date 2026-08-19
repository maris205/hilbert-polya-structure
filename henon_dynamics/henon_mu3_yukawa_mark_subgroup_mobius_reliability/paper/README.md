# C77 manuscript

`main.tex` is a self-contained theorem note for the exact subgroup-lattice
Möbius/reliability calculation.  It has no external bibliography and uses a
dependency-light article layout.

Compile from this directory with:

```bash
SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The canonical evidence hash is
`f7e2db84698ec61bf6283175368d2749d7f17ac77baeda37fd0a5cb8caf1c634`.
For the release gate, perform two isolated clean builds and compare the
SHA-256 digests of `main.pdf`.  The PDF should contain no unresolved
references, citation warnings, or `[VERIFY]` markers.
