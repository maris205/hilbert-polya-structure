# C213 test report

The exact producer and producer-independent checker agree on all 700 block
rows and 25 parameter-pair gap rows.  Every nonzero serialized decimal has 82
significant digits and is independently recomputed at 100-digit precision.
SymPy checks the centered-block square, matrix-exponential initial-value/ODE
identity, characteristic polynomial, telegraph identity, critical condition
and diffusive gap relation.  Replay is
byte-identical; mutation tests cover route/scope/theorem corruption,
duplicates, matrix/eigenvalue rows, unknown keys and stale hashes.
