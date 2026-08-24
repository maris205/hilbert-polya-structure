# C130 code

Run the programs from the package root in this order:

```bash
python3 code/c130_suspension_producer.py
python3 code/c130_suspension_checker.py
python3 code/c130_sympy_crosscheck.py
python3 code/c130_replay.py
python3 code/c130_mutation.py
```

- `c130_suspension_producer.py` creates the canonical exact evidence receipt.
- `c130_suspension_checker.py` is an independent standard-library validator;
  it does not import the producer or SymPy.
- `c130_sympy_crosscheck.py` reconstructs the determinant and traces afresh.
- `c130_replay.py` requires byte-for-byte evidence reproduction.
- `c130_mutation.py` separates 43 repaired-hash semantic mutations from one
  stale-hash gate mutation before asking the checker to reject them.
- `c130_release_manifest.py` hashes the final 27-file payload.

The period-10 replay is finite only for auditability.  The theorem follows
from the exact matrix trace-log identity and primitive-root decomposition and
has no period cutoff.
