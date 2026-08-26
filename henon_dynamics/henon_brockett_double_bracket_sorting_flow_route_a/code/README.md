# C185 exact code

Run in package order:

```bash
python code/c185_brockett_producer.py
python code/c185_brockett_checker.py
python code/c185_sympy_crosscheck.py
python code/c185_replay.py
python code/c185_mutation.py
python code/c185_release_manifest.py
```

- `c185_brockett_producer.py` writes canonical exact evidence.
- `c185_brockett_checker.py` imports no producer code and independently rebuilds
  all metadata, 5,912 permutations, 118,004 pair modes, rational matrix rows,
  source registry, Route-A qualifications, and boundary controls.
- `c185_sympy_crosscheck.py` reconstructs the symbolic Lyapunov,
  isospectral-trace, and linearization identities through a separate algebra
  path, then checks every finite pair mode.
- `c185_replay.py` regenerates the evidence in a temporary directory and
  requires byte equality.
- `c185_mutation.py` repairs the payload hash after each semantic attack and
  also runs a stale-hash attack.
- `c185_release_manifest.py` hashes the 27 payload files and excludes itself
  plus transient LaTeX files.

No randomness, floating-point integrator, network call, target table, or
package-external data file is used.  The finite ledger is regression evidence;
the all-size proof is textual and algebraic.
