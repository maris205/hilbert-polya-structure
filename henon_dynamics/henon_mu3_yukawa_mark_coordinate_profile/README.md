# HCS-C67: coordinate-wise mark integrality profile

Status: **PREFREEZE_COMPLETE_NOT_RELEASED**.

C67 refines the C66 abstract Smith cokernel by fixing the named C64 mark
coordinates. For the standard coordinate vector e_j, define

```text
o_j = min { n > 0 : n e_j belongs to M Z^16 }.
```

The exact coordinate profile is

```text
[36, 12, 6, 6, 2, 2, 36, 6, 16, 8, 6, 12, 2, 2, 36, 36]
```

For the transpose map the dual profile is

```text
[1, 4, 2, 2, 2, 2, 36, 6, 16, 8, 2, 4, 2, 2, 2, 2]
```

Both least common multiples and the global denominator of M^{-1} are 144;
the inverse has 43 nonzero entries. This is a coordinate embedding result
for the frozen 16-type map, not a canonical Smith basis or a full table of
marks. The scope firewall is `NO_BAD_EULER_OR_ROOT_NUMBER`.

Entry points:

- `code/c67_coordinate_profile.py`: exact rational-inverse producer;
- `code/c67_coordinate_profile_checker.py`: independent checker;
- `code/c67_coordinate_profile_replay_checker.py`: clean replay;
- `code/c67_rational_crosscheck.py`: independent SymPy check;
- `code/c67_mutation_test.py`: hostile mutations;
- `results/c67_coordinate_profile_evidence.json`: canonical evidence;
- `PILOT_REPORT.md`, `results/RESULTS.md`, and `results/HOSTILE_AUDIT.md`:
  human-readable pilot and hostile-audit receipts;
- `paper/main.pdf`: compiled manuscript.

The prefreeze manifest is a scoped ledger for the canonical executable,
evidence, and paper artifacts. The three narrative receipts above are
deliberately auxiliary and do not alter the frozen C67 authority bytes used by
C68; their numerical statements are reproduced by the checked evidence and
`results/TEST_REPORT.md`.
