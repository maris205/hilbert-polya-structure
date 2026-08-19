# C75 code map

- `c75_closure_incidence_lift.py`: source-bound producer;
- `c75_closure_incidence_lift_checker.py`: independent checker;
- `c75_group_crosscheck.py`: GAP representation and structure check;
- `c75_closure_incidence_lift_replay_checker.py`: clean replay;
- `c75_mutation_test.py`: hostile semantic mutation audit.

Run from this directory:

```bash
python3 c75_closure_incidence_lift.py
python3 c75_closure_incidence_lift_checker.py
python3 c75_group_crosscheck.py
python3 c75_closure_incidence_lift_replay_checker.py
python3 c75_mutation_test.py
```
