# Test report

Run from repository root:

```text
python .../code/c227_lorenz_producer.py
  C227_PRODUCER_PASS; 10 rows
python .../code/c227_lorenz_checker.py
  C227 independent checker: PASS (231 assertions)
python .../code/c227_lorenz_sympy_crosscheck.py
  C227 SymPy cross-check: PASS (14 symbolic identities)
python .../code/c227_lorenz_replay.py
  C227 canonical byte replay: PASS
python .../code/c227_lorenz_mutation.py
  C227 hostile mutation rejection: PASS 17/17
```

The release-manifest test additionally reruns those five programs, checks the
evaluator/source/scope locks, rejects build sidecars, requires exactly 27
payload paths, requires three distinct revision PDFs with `main.pdf` equal to
round 2, enforces a 2–6 page final PDF with embedded subset fonts, and scans
extracted text for the theorem and nonclaim literals.
