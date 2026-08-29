# Test report

```text
c228_coagulation_producer.py
  C228_PRODUCER_PASS; 40 coefficient rows; 13 branch rows
c228_coagulation_checker.py
  C228 independent checker: PASS (696 assertions)
c228_coagulation_sympy_crosscheck.py
  C228 SymPy cross-check: PASS (29 symbolic identities)
c228_coagulation_replay.py
  C228 canonical byte replay: PASS
c228_coagulation_mutation.py
  C228 hostile mutation rejection: PASS 28/28
```

The release-manifest gate reruns all programs with bytecode disabled, validates
the scope/evaluator/source locks, requires exactly 27 payload paths and no
sidecars, verifies three distinct revision PDFs with final equal to round 2,
and checks pages, embedded subset fonts and required extracted text.
