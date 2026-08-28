# Test report

Run from the package root:

```text
python3 -B code/c223_jaynes_cummings_producer.py
python3 -B code/c223_jaynes_cummings_checker.py
python3 -B code/c223_jaynes_cummings_sympy_crosscheck.py
python3 -B code/c223_jaynes_cummings_replay.py
python3 -B code/c223_jaynes_cummings_mutation.py
```

All commands pass.  The checker imports no producer code and enforces exact
recursive schema closure.  It reconstructs the center, detuning, Rabi square,
dressed pair, trace/determinant and mixing fraction, then builds each unitary
matrix directly and checks probabilities and unitarity.  A separately built
truncated atom--Fock Hamiltonian commutes with total excitation and yields the
expected blocks.  SymPy checks the generic algebra; replay uses a clean
subprocess; repaired and stale hashes are attacked separately.
