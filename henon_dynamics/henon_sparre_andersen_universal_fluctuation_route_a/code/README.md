# Executable certificate

- `c273_sparre_andersen_producer.py` writes deterministic exact evidence.
- `c273_sparre_andersen_checker.py` independently rebuilds every formula and
  enumeration; it does not import the producer.
- `c273_sparre_andersen_sympy_crosscheck.py` checks the univariate and
  bivariate generating functions symbolically.
- `c273_sparre_andersen_replay.py` requires fresh-process byte identity.
- `c273_sparre_andersen_mutation.py` repairs each mutated payload hash and
  requires rejection.
- `c273_release_manifest.py` reruns all gates and closes the 27-payload ledger.

Run from the repository root with `PYTHONDONTWRITEBYTECODE=1 python3 -B`.
