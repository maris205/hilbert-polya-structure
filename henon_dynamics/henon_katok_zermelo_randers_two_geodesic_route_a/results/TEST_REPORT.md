# HCS-C339 test report

- `python -B code/c339_katok_producer.py`: PASS, 158 rows.
- `python -B code/c339_katok_checker.py`: PASS, 3,916 checks.
- `python -B code/c339_katok_sympy_crosscheck.py`: PASS, 639 identities.
- `python -B code/c339_katok_replay.py`: PASS, two isolated builds,
  73,089 byte-identical bytes.
- `python -B code/c339_katok_mutation.py`: PASS, 54/54 rejected.
- Every lane rejects both `python -O` and `python -OO`.
- Strict JSON rejects duplicate and nonfinite data; strict YAML rejects
  duplicate/non-string keys, anchors, aliases, merges, and malformed roots.
- Release builds each revision twice in fresh directories at epoch
  1788393600 and requires both bytes to match the checked-in PDF.
