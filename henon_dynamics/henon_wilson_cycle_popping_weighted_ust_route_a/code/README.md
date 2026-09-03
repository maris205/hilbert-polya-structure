# C338 executable lanes

Run from the package root with unoptimized Python:

```bash
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c338_wilson_ust_producer.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c338_wilson_ust_checker.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c338_wilson_ust_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c338_wilson_ust_replay.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c338_wilson_ust_mutation.py
PYTHONDONTWRITEBYTECODE=1 TZ=UTC python -B code/c338_release_manifest.py
```

The checker does not import the producer.  It reconstructs all 772 simple
graphs, 8,136 graph-tree pairs, 55,895 simple subset events, 24 weighted
multigraph cases, 7,032 weighted subset events, and 12,754 finite stack tables.
The SymPy lane separately owns symbolic triangle and parallel-edge identities.
Replay regenerates evidence in an isolated temporary directory.  Mutation uses
repaired outer hashes and strict JSON/YAML parser attacks.  Every script fails
closed under `python -O` and `python -OO`.
