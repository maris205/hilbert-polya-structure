# Test report

Run from the package root:

```text
python3 -B code/c288_delta_producer.py
python3 -B code/c288_delta_checker.py
python3 -B code/c288_delta_sympy_crosscheck.py
python3 -B code/c288_delta_replay.py
python3 -B code/c288_delta_mutation.py
```

Expected pass markers are `C288_PRODUCER_PASS`,
`C288 independent Laplace/interface checker: PASS`, `C288_SYMPY_PASS`,
`C288 byte replay: PASS`, and
`C288 hostile mutation audit: PASS 30/30`.

All commands passed on 2026-09-02 with Python bytecode disabled and UTC
environment.  The checker reported 1,726 assertions, SymPy reported 46
identities, and the mutation suite rejected 30/30 specimens.  The release
script reruns them and performs six fresh deterministic PDF builds before
writing the manifest.
