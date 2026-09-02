# Reproducibility code

- `c302_quicksort_producer.py` expands exact rational PGFs through `n=12`,
  records permutation counts and moments, and emits every `(n+1)`-centered
  pivot/toll row through `n=32`.
- `c302_quicksort_checker.py` imports no producer code.  It exhaustively runs
  all permutations through `n=9`, constructs an independent integer-count
  convolution through `n=12`, and enforces exact JSON/YAML semantics.
- `c302_quicksort_sympy_crosscheck.py` independently differentiates PGFs,
  checks mean/variance recurrences through `n=80`, validates finite centering,
  differentiates the beta integral, and derives `16*zeta(3)-19`.
- `c302_quicksort_replay.py` requires two fresh evidence runs to be
  byte-identical to the archive.
- `c302_quicksort_mutation.py` attacks model, endpoint, PGF, moment,
  normalization, integral, Route-A, scope, JSON, and YAML contracts.
- `c302_release_manifest.py` rebuilds the full package and enforces the exact
  27-payload/28-physical-file release tree.

Python 3 is required; the strict YAML lane uses PyYAML and the symbolic lane
uses SymPy.  PDF release requires LuaLaTeX and Poppler utilities.
