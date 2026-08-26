# C188 code

- `c188_max_plus_producer.py`: exact `Fraction` cycle enumeration, critical
  graph, powers, CSR, vector periods and boundary evidence.
- `c188_max_plus_checker.py`: independent Karp/closure/Tarjan/distance-gcd,
  permutation-cycle, binary-power and exact-map checker; it imports no producer.
- `c188_sympy_crosscheck.py`: separate SymPy-rational reconstruction.
- `c188_replay.py`: isolated canonical byte replay.
- `c188_mutation.py`: repaired-hash semantic and stale-hash hostile tests.
- `c188_release_manifest.py`: self-excluded 27-payload release ledger.

All arithmetic is exact.  `None` is used internally for max-plus `-inf` and is
encoded as the string `"-inf"` in evidence.  The producer honors `C188_OUTPUT`
so replay never overwrites the released artifact.
