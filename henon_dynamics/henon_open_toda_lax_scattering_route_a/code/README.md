# C230 executable audit chain

The package is intentionally source-local.  Run the following from the
package root, with bytecode disabled when reproducing the release:

```text
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_producer.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_replay.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_open_toda_mutation.py
PYTHONDONTWRITEBYTECODE=1 python3 -B code/c230_release_manifest.py
```

`c230_open_toda_producer.py` uses only rational Jacobi sentinels and a fixed
high-precision RK4 grid.  It records 30 finite Lax rows, 15 exact N=2 closed
form rows, six endpoint scattering diagnostics, and nine simple-spectrum
norming-coordinate rows.  The checker reconstructs the flow without importing
the producer.  The SymPy process verifies the Lax commutator, trace
invariants, characteristic polynomials, the N=2 sech solution, and the
normalized exponential norming flow.  Replay tests canonical bytes; mutation
tests repair hashes before attempting to pass altered semantics; the hostile
suite rejects 22/22 altered receipts.

Finite endpoint errors are diagnostics only.  The global scattering theorem,
simple-spectrum statement, and boundary distinctions are theorem claims in the
displayed conventions; no arithmetic data are read.  Build sidecars and the
self-excluded manifest are not payload files.
