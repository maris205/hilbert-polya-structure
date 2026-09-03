# HCS-C340 test report

- `python -B code/c340_lame_producer.py`: PASS, 199 rows.
- `python -B code/c340_lame_checker.py`: PASS, 9,068 checks.
- `python -B code/c340_lame_sympy_crosscheck.py`: PASS, 618 identities.
- `python -B code/c340_lame_replay.py`: PASS, two isolated builds,
  175,409 byte-identical bytes.
- `python -B code/c340_lame_mutation.py`: PASS, 55/55 rejected.
- Every lane rejects both `python -O` and `python -OO`.
- Strict JSON/YAML and canonical rational gates are active.
- The symbolic lane checks every coefficient of the commutator and cubic
  differential-operator relation after reduction by both stationary
  identities.
- Each paper revision is rebuilt twice in fresh directories and compared
  byte-for-byte with the checked-in PDF.
