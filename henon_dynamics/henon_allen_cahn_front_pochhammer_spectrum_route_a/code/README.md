# C231 code

`c231_allen_cahn_producer.py` writes a deterministic JSON receipt with rational
epsilon/speed/profile probes and 90-digit decimal values.  The checker rebuilds
all identities independently and rejects unknown keys, stale payload hashes,
scope violations, and citation drift.  SymPy checks the profile ODE,
equipartition, factorization, bound states, essential edge, and surface-energy
integral.  Replay compares producer bytes in a separate process; mutation runs
21 repaired and stale attacks, including nested unknown and citation fields.

No package imports producer code from the checker, and no numerical fit or
external target data is used.
