# Reproducibility contract

Run python -B code/c387_nilflow_producer.py, c387_nilflow_checker.py, c387_nilflow_sympy_crosscheck.py, c387_nilflow_replay.py and c387_nilflow_mutation.py from this package. Run python -B -m unittest tests/test_c387_smoke.py. RELEASE.md provides the aggregate release command, fresh deterministic PDF rebuilding and nonwrite comparison.

The producer uses exact Fraction arithmetic and the analytic phase formula. The independent checker does not import it: the checker composes group elements and directly asks whether all three lattice displacement coordinates are integers. The checker recursively compares every JSON leaf with exact type equality, so bool/int and float/int aliases are rejected. SymPy proves finite generic identities; it is not a high-precision numerical or interval calculation.

Replay runs the frozen producer from two distinct temporary working directories and compares output bytes. Mutations repair the evidence hash before semantic checking. Strict YAML rejects duplicate/nonstring keys, timestamps, anchors, aliases and merges, and pins the exact raw bytes. Six command-line scripts refuse -O/-OO. The manifest has exact physical and payload membership, not a permissive file list.
