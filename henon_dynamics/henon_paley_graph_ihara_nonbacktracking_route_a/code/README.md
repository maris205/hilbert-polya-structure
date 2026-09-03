# C329 computation lanes

`c329_paley_ihara_producer.py` writes the canonical exact evidence.  The
checker reconstructs finite fields and every declared coordinate without
importing the producer.  The SymPy lane checks the determinant logarithm and
prime-field adjacency characteristic polynomials.  Replay regenerates the
evidence in an isolated directory, mutation attacks repaired hashes and strict
parsers, and the release script owns the 27-file payload ledger.

Run, in order:

```text
python code/c329_paley_ihara_producer.py
python code/c329_paley_ihara_checker.py
python code/c329_paley_ihara_sympy_crosscheck.py
python code/c329_paley_ihara_replay.py
python code/c329_paley_ihara_mutation.py
python code/c329_release_manifest.py --write
python code/c329_release_manifest.py
python code/c329_release_manifest.py
```
