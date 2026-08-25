# C164 deterministic code

Run from the package root with Python 3:

```text
python code/c164_owner_producer.py
python code/c164_owner_checker.py
python code/c164_sympy_crosscheck.py
python code/c164_replay.py
python code/c164_mutation.py
python code/c164_release_manifest.py
```

`c164_owner_producer.py` is the only evidence writer.  The checker does not
import it and independently reconstructs Thue--Morse parity, all formal
series, branch rows, the bounded-weight control, scope flags, and claim
boundaries.  SymPy separately reconstructs a finite symbolic branch operator
with arbitrary gauges.  Replay requires canonical byte identity.  Mutation
tests repair payload hashes before invoking the checker, plus one stale-hash
control.  The release manifest excludes itself and build debris.
