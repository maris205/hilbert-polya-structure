# C136 paper

`main.tex` is the final four-page manuscript.  The snapshots are successive
real revisions:

- `main_round0_original.pdf`: complete baseline;
- `main_round1.pdf`: convention and unitary-obstruction revision;
- `main_round2.pdf`: antiunitary, fixed-ordered-leaf, hostile-scope, and
  reproducibility revision;
- `main.pdf`: byte-identical to `main_round2.pdf` and the release PDF.

Build from this directory with:

```bash
SOURCE_DATE_EPOCH=1787529600 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

The release check performs two fresh isolated builds rather than trusting the
working-directory auxiliary files.  See `COMPILE_REPORT.md` for hashes, fonts,
warnings, and visual inspection.
