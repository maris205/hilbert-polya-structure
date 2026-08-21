# C88 reproducibility commands

Run from the C88 project directory:

```bash
python3 code/c88_subgroup_first_passage_atlas.py
python3 code/c88_subgroup_first_passage_atlas_checker.py
python3 code/c88_sympy_crosscheck.py
python3 code/c88_replay_checker.py
PYTHONDONTWRITEBYTECODE=1 python3 code/c88_mutation_test.py
```

The producer uses indexed closure transitions.  The checker independently
enumerates the twenty subgroups, directly expands finite point sets,
enumerates each target's minimal generating-support antichain, and
reconstructs the hit up-set from antichain containment.  The checker never
reads a producer intermediate table.  The mutation test builds
the independent expected object once and submits forty altered receipts to
the same validation function.
