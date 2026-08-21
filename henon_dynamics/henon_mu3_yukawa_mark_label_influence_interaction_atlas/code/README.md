# C87 reproducibility commands

Run from the package root:

```bash
PYTHONHASHSEED=0 LC_ALL=C python3 code/c87_label_influence_interaction_atlas.py
PYTHONHASHSEED=0 LC_ALL=C python3 code/c87_label_influence_interaction_atlas_checker.py
PYTHONHASHSEED=0 LC_ALL=C python3 code/c87_sympy_crosscheck.py
PYTHONHASHSEED=0 LC_ALL=C python3 code/c87_replay_checker.py
PYTHONHASHSEED=0 LC_ALL=C python3 code/c87_mutation_test.py
```

The producer uses C73 edge containment.  The checker uses C78's structural
block criterion and does not reuse the producer's predicate implementation.
The SymPy kernel builds the unique multilinear Boolean polynomial and derives
all coalition-size first and second derivative enumerators symbolically.

All counts and normalizations are exact.  The only non-standard Python
dependency is SymPy; no network access or random sampling is used.
