# HCS-C21 test report

**Date:** 2026-08-08
**Environment:** Python 3, SymPy 1.14.0

## Commands

~~~bash
python code/c21_producer.py --output results/c21_certificate.json
python code/c21_independent_check.py \
  --certificate results/c21_certificate.json \
  --output results/c21_independent_check.json
python -m unittest discover -s code -p 'test_c21.py' -v
sha256sum -c results/ARTIFACT_HASHES.sha256
~~~

## Result

- Producer: PASS.
- Certificate SHA-256:
  `5386c95cbc65e6a4323cfcf230de6b41f353be909d197818f9c4fbf0a75a96fc`.
- Non-importing checker: PASS, 133 named checks.
- Unit/fail-closed suite: 14 tests passed.
- Artifact hash verification: all entries passed.
- Determinism control: two consecutive checker runs produced identical
  report hashes.

The test suite deliberately mutates the candidate identity, source
polynomial, ordered cover, sheet-separation resultant, genus, fixed field,
\(\tau\)-character, marker shadow, period threshold, and clock-averaging
flag.  Each mutation is rejected.
