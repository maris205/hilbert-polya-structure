# Manuscript build

The release gate builds rounds 0, 1, and 2 twice each in fresh directories
with LuaLaTeX, `SOURCE_DATE_EPOCH=1788480000`, `FORCE_SOURCE_DATE=1`, and
`TZ=UTC`.  Round 0 owns the coefficient reduction; round 1 adds the exact
first-cusp theorem; round 2 adds the complete boundary, source, evidence, and
route closure.  `main.pdf` is byte-identical to round 2.

Run:

```bash
python -B code/c368_release_manifest.py --write --build-pdfs
```
