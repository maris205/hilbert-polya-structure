# Reproducibility

Run from this package directory with ordinary, nonoptimized Python:

```bash
python -B code/c375_lps_nonbacktracking_producer.py
python -B code/c375_lps_nonbacktracking_checker.py
python -B code/c375_lps_nonbacktracking_sympy_crosscheck.py
python -B code/c375_lps_nonbacktracking_replay.py
python -B code/c375_lps_nonbacktracking_mutation.py
python -m unittest tests/test_c375_smoke.py
python -B code/c375_release_manifest.py --write --build-pdfs
python -B code/c375_release_manifest.py
```

The producer normalizes a projective matrix by its first nonzero entry and
uses right multiplication.  The checker regenerates the four-square
solutions, normalizes by the last nonzero entry, and uses left
multiplication.  Their canonical group digests and all 60 trace rows agree.

The release gate refuses `python -O` and `python -OO`, parses JSON and YAML
strictly, locks evaluator raw and semantic bytes, repairs hashes before
hostile mutations, compiles all three paper rounds twice in fresh
directories under epoch `1788480000`, rejects warnings, checks subset
embedded fonts, extracts text, rasterizes every page, and closes a
self-excluding manifest.
