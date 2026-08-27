# C197 executable certificate

Run, from this directory or with absolute paths:

```bash
python c197_douglas_rachford_producer.py
python c197_douglas_rachford_checker.py
python c197_douglas_rachford_sympy_crosscheck.py
python c197_douglas_rachford_replay.py
python c197_douglas_rachford_mutation.py
```

The producer uses the closed principal-angle block formula.  The checker does
not import it: it reconstructs each block from two orthogonal projectors and
two reflections, then takes matrix powers directly.  The SymPy path separately
derives the symbolic block and all finite determinant factors.  Rational
Pythagorean angles are regression sentinels, not the proof of the theorem for
arbitrary subspaces.
