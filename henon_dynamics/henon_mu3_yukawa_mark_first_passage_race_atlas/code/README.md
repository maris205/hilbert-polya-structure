# C91 code

- `c91_first_passage_race_atlas.py`: canonical producer.
- `c91_first_passage_race_atlas_checker.py`: independent reconstruction from
  C88 hit bitsets and source authority chain.
- `c91_sympy_crosscheck.py`: exact rational and generating-function checks.
- `c91_replay_checker.py`: clean-process deterministic replay.
- `c91_mutation_test.py`: hostile semantic mutation audit.

Run from this directory or the repository root with Python 3.11+ and SymPy:

```text
python c91_first_passage_race_atlas.py
python c91_first_passage_race_atlas_checker.py
python c91_sympy_crosscheck.py
python c91_replay_checker.py
python c91_mutation_test.py
```
