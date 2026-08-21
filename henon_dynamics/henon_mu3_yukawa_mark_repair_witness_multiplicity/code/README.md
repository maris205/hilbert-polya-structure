# C79 reproducibility commands

From this directory's parent project:

```bash
python3 code/c79_repair_witness_multiplicity.py
python3 code/c79_repair_witness_multiplicity_checker.py
python3 code/c79_sympy_crosscheck.py
python3 code/c79_repair_witness_multiplicity_replay_checker.py
python3 code/c79_mutation_test.py
```

The producer writes the canonical JSON receipt.  The checker rebuilds the
finite group closure independently; the SymPy script checks the block-state
polynomial; replay runs the checker in a clean process; mutation testing must
reject all 22 semantic edits.
