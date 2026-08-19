# C76 code map

- `c76_closure_orbit_atlas.py`: source-bound producer for the effective label
  group, closure table, support orbits, and minimality filters;
- `c76_closure_orbit_atlas_checker.py`: independent clean implementation of
  the same assertions;
- `c76_group_crosscheck.py`: GAP order and structure cross-check;
- `c76_closure_orbit_atlas_replay_checker.py`: clean-process replay;
- `c76_mutation_test.py`: hostile semantic mutation audit.

Run from this directory:

```bash
python3 c76_closure_orbit_atlas.py
python3 c76_closure_orbit_atlas_checker.py
python3 c76_group_crosscheck.py
python3 c76_closure_orbit_atlas_replay_checker.py
python3 c76_mutation_test.py
```

The producer writes the canonical JSON evidence under `results/`.  The
checker requires canonical JSON and validates the two C75 authority hashes
before recomputing any orbit or closure count.
